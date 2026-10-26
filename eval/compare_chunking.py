"""Compare chunk sizes fairly: at the same amount of text sent to the model.

Recall@k favours big chunks (a 400-word chunk contains more text, so it is more
likely to contain the gold quote) while also costing more per request. This
script reads the latest retrieval results for each chunk size and reports recall
at equal *word budgets*: k = budget / mean chunk length of that index.

Usage: python eval/compare_chunking.py [--split dev]
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "eval" / "results"
VARIANTS = {150: ROOT / "index", 250: ROOT / "index-250", 400: ROOT / "index-400"}
BUDGETS = (500, 1000, 1500)  # words of retrieved text handed to the model


def latest(label):
    files = sorted(RESULTS.glob(f"retrieval-{label}-2*.json"))
    return json.loads(files[-1].read_text(encoding="utf-8")) if files else None


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--split", default="dev")
    args = parser.parse_args()

    rows = []
    for size, index in VARIANTS.items():
        report = latest(f"chunks-{size}-{args.split}")
        if not report:
            print(f"no results for chunks-{size}-{args.split}; run eval/retrieval_eval.py first")
            continue
        words = [json.loads(line)["words"] for line in (index / "chunks.jsonl").read_text(encoding="utf-8").splitlines()]
        mean = sum(words) / len(words)
        for setup in report["summary"]:
            ranks = [per[setup] for per in report["per_question"].values()]
            cells = []
            for budget in BUDGETS:
                k = max(1, round(budget / mean))
                hit = sum(r is not None and r <= k for r in ranks) / len(ranks)
                cells.append(f"{hit:.3f} (k={k})")
            rows.append([str(size), f"{len(words)}", f"{mean:.0f}", setup] + cells)

    cols = ["chunk size", "chunks", "mean words", "setup"] + [f"recall @ {b} words" for b in BUDGETS]
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    lines += ["| " + " | ".join(r) + " |" for r in rows]
    out = "\n".join(lines)
    print(out)
    (RESULTS / f"chunking-{args.split}.md").write_text(
        f"# Chunk size at equal word budget ({args.split})\n\n"
        "k = budget / mean chunk length; ranks only go to 10, so a k above 10 is capped by the data.\n\n"
        + out + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
