"""Helpers shared by the evaluation scripts."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUESTIONS = ROOT / "data" / "eval_questions.jsonl"


def normalise(text):
    """Compare text ignoring case, whitespace, Markdown emphasis and typographic quotes."""
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    text = text.replace(" ", " ").replace(" ", " ")
    text = re.sub(r"[*\\]", "", text)
    return " ".join(text.lower().split())


def load_questions(path=QUESTIONS):
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]


def contains_evidence(chunk, question):
    """True if the chunk comes from a gold document and contains its quote."""
    text = normalise(chunk["text"])
    return any(chunk["doc_id"] == ev["doc"] and normalise(ev["quote"]) in text for ev in question["evidence"])
