"""Turn the raw HTML pages and PDFs in corpus/raw/ into clean text.

HTML: each publisher's site keeps its content in a known container (CONTENT
below). We take that container, drop navigation, forms and widgets, and convert
it to Markdown so headings, lists and tables survive for the chunker. Sites
without a known container fall back to trafilatura's boilerplate removal.

PDF: text is extracted page by page so chunks can cite a page number.

Output: corpus/text/docs.jsonl, one document per line with its manifest
metadata, a title, and `blocks`: [{"page": n | null, "text": markdown}].

Usage: python scripts/extract_text.py
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

import pymupdf
import trafilatura
from bs4 import BeautifulSoup
from markdownify import markdownify

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
MANIFEST = CORPUS / "manifest.jsonl"
OUT = CORPUS / "text" / "docs.jsonl"

# CSS selector of the main content container, per publisher (tried in order).
CONTENT = {
    "Campus France Tunisie": ["div.region-content", "main"],
    "Campus France": ["div.region-content", "main"],
    "France-Visas": ["div#main-content"],
    "Ambassade d'Allemagne à Tunis": ["main#main"],
    "Auswärtiges Amt (Federal Foreign Office)": ["main#main"],
    "DAAD Tunisie": ["main"],
    "DAAD Scholarship Database": ["div#ifa-stipendien-detail"],
    "Immigration, Refugees and Citizenship Canada (IRCC)": ["main"],
    "EduCanada (Global Affairs Canada)": ["main"],
    "European Commission (Erasmus+)": ["main#main-content", "main"],
    "Bureau National Erasmus+ Tunisie": ["article"],
}

# Removed from inside the content container on every site. <aside> is kept on
# purpose: the embassy's info boxes and Canada.ca alerts live in asides.
NOISE = [
    "script", "style", "noscript", "svg", "nav", "form", "button", "iframe",
    "[role=navigation]", ".breadcrumb", "#wb-dtmd", ".pagedetails",  # Canada.ca page footer
    ".social-share", ".share", ".c-share", ".ecl-social-media-share",
]
# Extra removals per publisher.
SITE_NOISE = {
    "DAAD Tunisie": ["aside"],  # the scholarship search filter box
    # Taxonomy tags ("Démarches administratives", "Étudiants", ...) and photo credits.
    # ...plus the "Suivez les grandes étapes" timeline and the FAQ contact box.
    "Campus France Tunisie": [".field--name-field-themes", ".field--name-field-publics-cibles",
                              ".field--name-field-domaines-etude", ".field--name-field-credits",
                              ".push-timeline", ".block-campus-search-contactez-nous"],
    # Application box listing every country in the world, plus the result-list link.
    # ...and the tab menu ("Overview / Application requirements / ...").
    "DAAD Scholarship Database": ["#select-application-info", ".back-to-results", "#programTab"],
}
# Site banners marked up as headings, e.g. the German embassy's
# "Bienvenue sur les pages du Ministère fédéral des Affaires étrangères".
BANNER_HEADINGS = re.compile(r"^(Bienvenue sur les pages|Willkommen auf den Seiten)", re.IGNORECASE)

# Whole lines that are site furniture rather than content.
JUNK_LINES = re.compile(
    r"^(- )?(Share this page|Report a problem.*|Date modified:.*|Imprimer|Partager|"
    r"Pour mettre en favoris un contenu.*|Je me connecte|Je crée mon compte|ou|Top of page|"
    r"Facebook|Twitter|LinkedIn|Courriel|X|WhatsApp|E-?mail)$",
    re.IGNORECASE,
)
# Sentences the DAAD database repeats on every programme page.
JUNK_SENTENCES = re.compile(
    r"(« Search results|Do you have any questions about DAAD scholarships\?|You will find the answers here!|"
    r"Please also take note of our important scholarship information\.|"
    r"\*\*Please note:\*\*|The usage of the application portal is possible only to a limited extent with "
    r"mobile devices\. Please use your desktop computer\. Technical requirements|"
    r"A print version of this announcement \(PDF\) is available in the further tabs \(e\.g\. “[^”]*”\)\.|"
    r"Eine Druckversion dieser Ausschreibung \(PDF\) steht Ihnen in den weiteren Registerkarten "
    r"\(z\.B\. „[^“]*“\) zur Verfügung\.)"
)


MONTHS = {m: i for i, m in enumerate(
    "janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split(), 1)}
MONTHS |= {m: i for i, m in enumerate(
    "january february march april may june july august september october november december".split(), 1)}

# Publication / last-update dates as each site prints them, most specific first.
HTML_DATES = [
    (re.compile(r"Date modified:\s*(\d{4})-(\d{2})-(\d{2})"), "ymd"),          # Canada.ca
    (re.compile(r"(\d{2})\.(\d{2})\.(\d{4})\s*-\s*Article"), "dmy"),           # German embassy / AA
    (re.compile(r"Mise à jour le\s+(\d{1,2})\s+(\w+)\s+(\d{4})", re.I), "d_month_y"),  # Campus France
    (re.compile(r"Last updated:?\s*(\d{1,2})\s+(\w+)\s+(\d{4})", re.I), "d_month_y"),  # Erasmus+
    (re.compile(r"Last updated:?\s*(\d{1,2})/(\d{1,2})/(\d{4})", re.I), "dmy"),
]
URL_DATE = re.compile(r"/(20\d{2})/(\d{2})/(\d{2})/")  # dated posts, e.g. daad.tn/fr/2026/03/16/...


def document_date(soup, url=""):
    """Best guess at when a page was published or last updated (YYYY-MM-DD), or None."""
    for prop in ("article:modified_time", "article:published_time", "dcterms.modified",
                 "dcterms.issued", "dc.date", "date"):
        tag = soup.find("meta", attrs={"property": prop}) or soup.find("meta", attrs={"name": prop})
        if tag and re.match(r"\d{4}-\d{2}-\d{2}", tag.get("content", "")):
            return tag["content"][:10]
    m = URL_DATE.search(url)
    if m:
        return "-".join(m.groups())
    tag = soup.find("time", attrs={"datetime": re.compile(r"^\d{4}-\d{2}-\d{2}")})
    if tag:
        return tag["datetime"][:10]
    text = soup.get_text(" ", strip=True)
    for pattern, kind in HTML_DATES:
        m = pattern.search(text)
        if not m:
            continue
        if kind == "ymd":
            y, mo, d = m.groups()
        elif kind == "dmy":
            d, mo, y = m.groups()
        else:
            d, month, y = m.groups()
            mo = MONTHS.get(month.lower())
            if not mo:
                continue
        return f"{int(y):04d}-{int(mo):02d}-{int(d):02d}"
    return None


def pdf_date(metadata):
    raw = metadata.get("modDate") or metadata.get("creationDate") or ""
    m = re.match(r"D:(\d{4})(\d{2})(\d{2})", raw)
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else None


def clean_markdown(md):
    md = JUNK_SENTENCES.sub("", md)
    lines = [line.rstrip() for line in md.splitlines()]
    lines = [line for line in lines if not JUNK_LINES.match(line.strip())]
    md = "\n".join(lines)
    md = re.sub(r"\n{3,}", "\n\n", md)  # collapse runs of blank lines
    return md.strip()


def html_to_markdown(raw, publisher, url=""):
    soup = BeautifulSoup(raw, "html.parser")
    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    published = document_date(soup, url)  # read before the page footer is stripped
    for selector in CONTENT.get(publisher, []):
        node = soup.select_one(selector)
        if node and len(node.get_text(" ", strip=True).split()) > 20:
            for junk in node.select(", ".join(NOISE + SITE_NOISE.get(publisher, []))):
                junk.decompose()
            for heading in node.find_all(["h1", "h2"]):
                if BANNER_HEADINGS.match(heading.get_text(" ", strip=True)):
                    heading.decompose()
            h1 = node.find("h1")
            if h1:
                title = h1.get_text(" ", strip=True)
            md = markdownify(str(node), heading_style="ATX", bullets="-", strip=["a", "img"])
            return title, clean_markdown(md), "selector", published
    md = trafilatura.extract(raw, output_format="markdown", include_tables=True,
                             include_links=False, favor_recall=True) or ""
    return title, clean_markdown(md), "trafilatura", published


def pdf_to_blocks(path):
    with pymupdf.open(path) as pdf:
        title = (pdf.metadata or {}).get("title") or ""
        published = pdf_date(pdf.metadata or {})
        pages = [page.get_text("text").splitlines() for page in pdf]
    # Running headers and footers: short lines repeated on many pages.
    counts = Counter(line.strip() for lines in pages for line in set(lines) if line.strip())
    repeated = {line for line, n in counts.items()
                if len(pages) >= 4 and n >= 0.4 * len(pages) and len(line.split()) <= 12}
    blocks = []
    for number, lines in enumerate(pages, 1):
        text = clean_markdown("\n".join(l for l in lines if l.strip() not in repeated))
        if text:
            blocks.append({"page": number, "text": text})
    return title, blocks, published


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    entries = [json.loads(line) for line in MANIFEST.read_text(encoding="utf-8").splitlines()]
    methods, thin, dated = {}, [], 0
    with open(OUT, "w", encoding="utf-8") as out:
        for entry in entries:
            path = CORPUS / entry["file"]
            if entry["format"] == "pdf":
                title, blocks, published = pdf_to_blocks(path)
                method = "pdf"
            else:
                title, text, method, published = html_to_markdown(
                    path.read_text(encoding="utf-8", errors="ignore"), entry["publisher"], entry["url"])
                blocks = [{"page": None, "text": text}] if text else []
            dated += published is not None
            words = sum(len(b["text"].split()) for b in blocks)
            methods[method] = methods.get(method, 0) + 1
            if words < 100:
                thin.append((entry["id"], words))
            doc = {k: entry[k] for k in ("id", "url", "publisher", "country", "topic", "lang", "format", "fetched_at")}
            doc.update(title=" ".join(title.split()), published=published, words=words,
                       method=method, blocks=blocks)
            out.write(json.dumps(doc, ensure_ascii=False) + "\n")

    print(f"{len(entries)} documents -> {OUT.relative_to(ROOT)}")
    print("extraction:", methods)
    print(f"publication date found for {dated}/{len(entries)} documents")
    if thin:
        print(f"{len(thin)} documents with under 100 words:")
        for doc_id, words in thin:
            print(f"  {doc_id}: {words}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
