"""Split the evaluation questions into a development set and a held-out test set.

dev  : used to compare settings (chunk size, fusion, reranker depth, prompts...)
test : touched only for the final numbers in the report, so they are not
       flattered by tuning on the same questions

The split is stratified by country and question type (so both sets cover the
same mix) and uses a fixed seed, so re-running gives the same result. It writes a
"split" field into data/eval_questions.jsonl.

Usage: python eval/split_questions.py [--test-share 0.27]
"""

import argparse
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import QUESTIONS, load_questions  # noqa: E402

SEED = 2026


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--test-share", type=float, default=0.27)
    args = parser.parse_args()

    questions = load_questions()
    groups = defaultdict(list)
    for q in questions:
        groups[(q["country"], q["type"])].append(q)

    rng = random.Random(SEED)
    for key in sorted(groups, key=str):
        members = sorted(groups[key], key=lambda q: q["id"])
        rng.shuffle(members)
        # Round the test share per group, carrying the remainder so small groups still contribute.
        n_test = round(len(members) * args.test_share + rng.random() - 0.5)
        for i, q in enumerate(members):
            q["split"] = "test" if i < n_test else "dev"

    QUESTIONS.write_text("\n".join(json.dumps(q, ensure_ascii=False) for q in questions) + "\n", encoding="utf-8")
    for split in ("dev", "test"):
        part = [q for q in questions if q["split"] == split]
        print(f"{split}: {len(part)} questions, {sum(q['type'] != 'unanswerable' for q in part)} answerable")
        print(f"   country: {dict(Counter(q['country'] for q in part))}")
        print(f"   type:    {dict(Counter(q['type'] for q in part))}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
