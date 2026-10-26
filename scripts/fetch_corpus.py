"""Download every document listed in corpus/sources.toml into corpus/raw/.

Each document is fetched from the live site. Groups marked `fetch = "archive"`
(sites that block scripts), and live fetches that fail, use the newest Wayback
Machine snapshot instead; `fetch = "reader"` goes through Jina Reader. Groups
marked `fetch = "manual"` are saved by hand from a browser (see
corpus/manual_download.md) and only picked up here. Every document gets a line in corpus/manifest.jsonl
recording where it came from, when, and its checksum.

Already-downloaded documents are skipped, so an interrupted run can be resumed.

Usage:
    python scripts/fetch_corpus.py              # fetch what is missing
    python scripts/fetch_corpus.py --force      # re-fetch everything
    python scripts/fetch_corpus.py --only ca-   # only ids starting with "ca-"
"""

import argparse
import hashlib
import json
import re
import sys
import time
import tomllib
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
RAW = CORPUS / "raw"
SOURCES = CORPUS / "sources.toml"
MANIFEST = CORPUS / "manifest.jsonl"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)
LIVE_DELAY = 1.5      # seconds between requests to the same live host
ARCHIVE_DELAY = 10.0  # web.archive.org answers 429 if hit faster than this
# fetch = "reader": sites that refuse direct and archive access from our network
# are retrieved through the Jina Reader service, which returns the page's HTML.
READER = "https://r.jina.ai/"
READER_DELAY = 4.0
READER_TIMEOUT = 90   # seconds the reader may wait for the target page
RATE_LIMIT_WAIT = 60 # seconds to back off after a 429 without a Retry-After header
TIMEOUT = 45
MAX_ATTEMPTS = 4
RETRYABLE = {429, 500, 502, 503, 504}


class FetchError(Exception):
    pass


class RateLimited(FetchError):
    """The server keeps answering 429; further requests only extend the block."""


def load_sources():
    """Flatten the groups in sources.toml into one dict per document."""
    with open(SOURCES, "rb") as f:
        config = tomllib.load(f)
    docs, seen = [], set()
    for group in config["group"]:
        for src in group["sources"]:
            if src["id"] in seen:
                sys.exit(f"duplicate id in sources.toml: {src['id']}")
            seen.add(src["id"])
            docs.append({
                "id": src["id"],
                "url": src.get("url") or urljoin(group["base"], src["path"]),
                "publisher": group["publisher"],
                "country": group["country"],
                "topic": src["topic"],
                "lang": src.get("lang", group["lang"]),
                "fetch": group.get("fetch", "live"),
            })
    return docs


_last_request = {}


def throttled_get(session, url, delay):
    """GET with a per-host delay and exponential backoff on transient errors."""
    host = urlparse(url).netloc
    error = None
    for attempt in range(MAX_ATTEMPTS):
        wait = _last_request.get(host, 0) + delay - time.monotonic()
        if wait > 0:
            time.sleep(wait)
        _last_request[host] = time.monotonic()
        try:
            if url.startswith(READER):
                # The reader renders the page in a browser; slow sites need the longer wait.
                headers = {"X-Return-Format": "html", "X-Timeout": str(READER_TIMEOUT)}
                resp = session.get(url, headers=headers, timeout=READER_TIMEOUT + 30)
            else:
                resp = session.get(url, timeout=TIMEOUT)
        except requests.RequestException as e:
            error = type(e).__name__
        else:
            if resp.status_code == 200:
                return resp
            error = f"HTTP {resp.status_code}"
            # The reader answers 422 when the target page timed out; that is worth a retry.
            retryable = RETRYABLE | {422} if url.startswith(READER) else RETRYABLE
            if resp.status_code not in retryable:
                break
            if resp.status_code == 429:
                # Rate limits last a while; a short backoff only extends the block.
                if attempt > 0:
                    raise RateLimited(f"{host} is rate-limiting (HTTP 429)")
                time.sleep(retry_after(resp))
                continue
        time.sleep(delay * 2 ** attempt)
    raise FetchError(error)


def retry_after(resp):
    try:
        return int(resp.headers.get("Retry-After", ""))
    except ValueError:
        return RATE_LIMIT_WAIT


def archive_url(url):
    # Asking for "now" makes the Wayback Machine redirect to the newest snapshot;
    # the id_ flag returns the original bytes without the archive's toolbar.
    now = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    return f"https://web.archive.org/web/{now}id_/{url}"


def check_content(body, content_type=None):
    """Return the file extension, or raise if the body is not a real document."""
    if body.startswith(b"%PDF"):
        return "pdf"
    head = body[:4096].lower()
    if (b"<html" in head or b"<!doctype html" in head) and len(body) > 2000:
        return "html"
    raise FetchError(f"unexpected content ({content_type}, {len(body)} bytes)")


def make_entry(doc, path, body, via, retrieved_from, snapshot, fetched_at):
    return {
        "id": doc["id"],
        "url": doc["url"],
        "file": path.relative_to(CORPUS).as_posix(),
        "format": path.suffix[1:],
        "publisher": doc["publisher"],
        "country": doc["country"],
        "topic": doc["topic"],
        "lang": doc["lang"],
        "via": via,
        "retrieved_from": retrieved_from,
        "snapshot": snapshot,
        "fetched_at": fetched_at,
        "bytes": len(body),
        "sha256": hashlib.sha256(body).hexdigest(),
    }


def import_manual(doc):
    """Record a page someone saved by hand as corpus/raw/<id>.html (or .pdf)."""
    for ext in ("html", "pdf"):
        path = RAW / f"{doc['id']}.{ext}"
        if path.exists():
            body = path.read_bytes()
            check_content(body)
            saved = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)
            return make_entry(doc, path, body, "manual", doc["url"], None,
                              saved.isoformat(timespec="seconds"))
    raise FetchError(f"not saved yet: save {doc['url']} as corpus/raw/{doc['id']}.html "
                     "(see corpus/manual_download.md)")


def fetch(session, doc):
    """Download one document; return its manifest entry."""
    if doc["fetch"] == "manual":
        return import_manual(doc)
    attempts = []
    if doc["fetch"] == "reader":
        attempts.append(("reader", READER + doc["url"], READER_DELAY))
    else:
        if doc["fetch"] == "live":
            attempts.append(("live", doc["url"], LIVE_DELAY))
        attempts.append(("archive", archive_url(doc["url"]), ARCHIVE_DELAY))

    errors = []
    for via, url, delay in attempts:
        try:
            resp = throttled_get(session, url, delay)
            ext = check_content(resp.content, resp.headers.get("content-type"))
        except RateLimited:
            raise
        except FetchError as e:
            errors.append(f"{via}: {e}")
            continue
        snapshot = re.search(r"/web/(\d{14})id_/", resp.url) if via == "archive" else None
        path = RAW / f"{doc['id']}.{ext}"
        path.write_bytes(resp.content)
        return make_entry(doc, path, resp.content, via, resp.url,
                          snapshot.group(1) if snapshot else None,
                          datetime.now(timezone.utc).isoformat(timespec="seconds"))
    raise FetchError("; ".join(errors))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--force", action="store_true", help="re-fetch documents already on disk")
    parser.add_argument("--only", default="", help="only fetch ids starting with this prefix")
    args = parser.parse_args()

    RAW.mkdir(parents=True, exist_ok=True)
    docs = load_sources()
    manifest = {}
    if MANIFEST.exists():
        for line in MANIFEST.read_text(encoding="utf-8").splitlines():
            entry = json.loads(line)
            manifest[entry["id"]] = entry

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept-Language": "fr,en;q=0.8"})

    failures = []
    todo = [d for d in docs if d["id"].startswith(args.only)]
    for i, doc in enumerate(todo, 1):
        done = manifest.get(doc["id"])
        if done and not args.force and (CORPUS / done["file"]).exists():
            continue
        try:
            entry = fetch(session, doc)
        except RateLimited as e:
            print(f"[{i}/{len(todo)}] STOP {doc['id']}: {e}. Re-run later to resume.")
            failures.append((doc["id"], str(e)))
            break
        except FetchError as e:
            failures.append((doc["id"], str(e)))
            print(f"[{i}/{len(todo)}] FAIL {doc['id']}: {e}")
            continue
        manifest[doc["id"]] = entry
        print(f"[{i}/{len(todo)}] ok   {doc['id']} ({entry['via']}, {entry['bytes'] // 1024} KB)")
        # Rewrite after every document so an interrupted run keeps its progress.
        write_manifest(manifest, docs)

    write_manifest(manifest, docs)
    kept = [manifest[d["id"]] for d in docs if d["id"] in manifest]
    print(f"\n{len(kept)}/{len(docs)} documents in corpus/raw/")
    print("by country:", dict(Counter(e["country"] for e in kept)))
    print("by source: ", dict(Counter(e["via"] for e in kept)))
    if failures:
        print(f"\n{len(failures)} failed:")
        for doc_id, err in failures:
            print(f"  {doc_id}: {err}")
        sys.exit(1)


def write_manifest(manifest, docs):
    # Follow sources.toml order and drop entries whose source was removed.
    lines = [json.dumps(manifest[d["id"]], ensure_ascii=False) for d in docs if d["id"] in manifest]
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
