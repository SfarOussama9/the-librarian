"""Check data/eval_questions.jsonl before using it.

For every question: required fields are present, ids are unique, and every
evidence quote really appears in the cited document's text (corpus/text/docs.jsonl).
Quotes are matched after normalising case, whitespace, Markdown emphasis and
typographic quotes, so "l’entretien" matches "l'entretien".

Gold answers are tied to documents and quotes, not chunk ids, so the set stays
valid when the corpus is re-chunked with a different size.

Usage: python eval/check_questions.py
"""

import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import QUESTIONS, normalise  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "corpus" / "text" / "docs.jsonl"
REQUIRED = {"id", "question", "lang", "answer", "evidence", "country", "topic", "type", "difficulty"}


def main():
    docs = {}
    for line in DOCS.read_text(encoding="utf-8").splitlines():
        d = json.loads(line)
        docs[d["id"]] = normalise("\n".join(b["text"] for b in d["blocks"]))

    questions = [json.loads(line) for line in QUESTIONS.read_text(encoding="utf-8").splitlines() if line.strip()]
    problems = []
    ids = Counter(q.get("id") for q in questions)
    problems += [f"duplicate id {i}" for i, n in ids.items() if n > 1]

    for q in questions:
        missing = REQUIRED - q.keys()
        if missing:
            problems.append(f"{q.get('id')}: missing fields {sorted(missing)}")
        if q["type"] == "unanswerable":
            if q["evidence"]:
                problems.append(f"{q['id']}: unanswerable but has evidence")
            continue
        if not q["evidence"]:
            problems.append(f"{q['id']}: no evidence")
        for ev in q["evidence"] + q.get("outdated_evidence", []):
            if ev["doc"] not in docs:
                problems.append(f"{q['id']}: unknown doc {ev['doc']}")
            elif normalise(ev["quote"]) not in docs[ev["doc"]]:
                problems.append(f"{q['id']}: quote not found in {ev['doc']}: {ev['quote'][:70]!r}")

    print(f"{len(questions)} questions")
    for field in ("type", "lang", "country", "difficulty"):
        print(f"  {field}: {dict(Counter(q.get(field) for q in questions))}")
    if problems:
        print(f"\n{len(problems)} problems:")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    print("\nall quotes found in their documents")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
