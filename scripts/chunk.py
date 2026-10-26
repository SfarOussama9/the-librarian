"""Split the extracted documents into chunks for indexing.

Documents are cut into paragraphs, lists, tables and heading lines, which are
packed in order into chunks of about --size words, with --overlap words repeated
between neighbouring chunks. Small sections share a chunk (their headings stay
in the text) and a heading is never left at the end of a chunk.
Lists and tables stay whole when they fit; a table that is too long is split
by rows and every piece keeps the header row.

Chunk size and overlap are experiment settings, not defaults to trust: run the
retrieval eval with several values and keep the best.

Each chunk keeps its document's metadata, the heading path it sits under and,
for PDFs, its page, so answers can cite the exact source. Chunks whose text
already appeared elsewhere (site boilerplate repeated on many pages) are dropped.

Usage:
    python scripts/chunk.py                         # 150 words, 25 overlap (chosen, see eval/results/chunking-dev.md)
    python scripts/chunk.py --size 400 --overlap 60 --out corpus/chunks-400.jsonl
"""

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "corpus" / "text" / "docs.jsonl"
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
LIST_ITEM = re.compile(r"^(-|\d+\.)\s")  # top-level item only (no indentation)
MIN_WORDS = 12  # chunks shorter than this carry no answer (lone headings, labels)


def sections(text):
    """Yield (heading path, body) for each heading-delimited section."""
    path, body = [], []
    for line in text.splitlines():
        m = HEADING.match(line)
        if m:
            if body:
                yield list(path), "\n".join(body)
                body = []
            level = len(m.group(1))
            title = re.sub(r"[*_]+", "", m.group(2)).replace("•", "-")  # drop Markdown emphasis
            path = path[: level - 1] + [" ".join(title.split()).strip(" -#")]
        else:
            body.append(line)
    if body:
        yield list(path), "\n".join(body)


def paragraphs(body, size):
    """Split a section into units: paragraphs, whole lists, table pieces."""
    for para in re.split(r"\n\s*\n", body):
        para = para.strip()
        if not para:
            continue
        lines = para.splitlines()
        if lines[0].startswith("|") and len(para.split()) > size:
            # Long table: split by rows, repeating the header (row + separator).
            header, rows = lines[:2], lines[2:]
            piece = []
            for row in rows:
                piece.append(row)
                if len(" ".join(header + piece).split()) >= size:
                    yield "\n".join(header + piece)
                    piece = []
            if piece:
                yield "\n".join(header + piece)
        elif LIST_ITEM.match(lines[0]) and len(para.split()) > size:
            # Long list: split between top-level items (nested lines stay with their item).
            piece = []
            for line in lines:
                if LIST_ITEM.match(line) and piece and len(" ".join(piece + [line]).split()) > size:
                    yield "\n".join(piece)
                    piece = []
                piece.append(line)
            if piece:
                yield "\n".join(piece)
        elif len(para.split()) > size:
            # Long prose: split at sentence ends.
            sentences = re.split(r"(?<=[.!?])\s+", para)
            buf = []
            for s in sentences:
                if buf and len(" ".join(buf + [s]).split()) > size:
                    yield " ".join(buf)
                    buf = []
                buf.append(s)
            if buf:
                yield " ".join(buf)
        else:
            yield para


def units(text, size):
    """Yield (unit text, heading path, is_heading) for a whole document block.

    Heading lines are kept as their own units so that small neighbouring
    sections can share a chunk without losing their titles.
    """
    for path, body in sections(text):
        if path:
            yield "#" * len(path) + " " + path[-1], path, True
        for para in paragraphs(body, size):
            yield para, path, False


def pack(items, size, overlap):
    """Greedily pack units into (text, heading path) chunks of ~size words."""
    chunks, current, current_path = [], [], None
    for text, path, is_heading in items:
        current_words = len(" ".join(t for t, _ in current).split())
        # Close the chunk when the next unit would overflow it, unless it is still
        # small: a question and its long answer should not be split apart.
        if current and current_words >= size // 3 and current_words + len(text.split()) > size:
            # A heading belongs with what follows it, not at the end of a chunk.
            carry = []
            while current and current[-1][1]:
                carry.insert(0, current.pop()[0])
            if current:
                body = [t for t, _ in current]
                chunks.append(("\n\n".join(body), current_path))
                tail = " ".join(" ".join(body).split()[-overlap:]) if overlap and not carry else ""
                current = [(tail, False)] if tail else []
            current += [(t, True) for t in carry]
            current_path = None
        if current_path is None and not is_heading:
            current_path = path
        current.append((text, is_heading))
    if current and any(not h for _, h in current):
        chunks.append(("\n\n".join(t for t, _ in current), current_path))
    return chunks


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--size", type=int, default=150, help="target chunk size in words")
    parser.add_argument("--overlap", type=int, default=25, help="words repeated between chunks")
    parser.add_argument("--out", default=str(ROOT / "corpus" / "chunks.jsonl"))
    args = parser.parse_args()

    seen, out_chunks = set(), []
    dropped = Counter()
    for line in DOCS.read_text(encoding="utf-8").splitlines():
        doc = json.loads(line)
        n = 0
        for block in doc["blocks"]:
            for text, path in pack(units(block["text"], args.size), args.size, args.overlap):
                path = path or []
                words = len(text.split())
                if words < MIN_WORDS:
                    dropped["too short"] += 1
                    continue
                key = hashlib.sha1(" ".join(text.lower().split()).encode()).hexdigest()
                if key in seen:
                    dropped["duplicate"] += 1
                    continue
                seen.add(key)
                n += 1
                out_chunks.append({
                    "chunk_id": f"{doc['id']}#{n}",
                    "doc_id": doc["id"],
                    "title": doc["title"],
                    "heading": " > ".join(path),
                    "page": block["page"],
                    "text": text,
                    "words": words,
                    **{k: doc[k] for k in ("url", "publisher", "country", "topic", "lang",
                                           "published", "fetched_at")},
                })

    out = Path(args.out)
    with open(out, "w", encoding="utf-8") as f:
        for chunk in out_chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    sizes = sorted(c["words"] for c in out_chunks)
    print(f"{len(out_chunks)} chunks -> {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    print(f"words per chunk: median {sizes[len(sizes) // 2]}, 90th pct {sizes[int(len(sizes) * 0.9)]}, max {sizes[-1]}")
    print("dropped:", dict(dropped))
    print("by country:", dict(Counter(c["country"] for c in out_chunks)))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
