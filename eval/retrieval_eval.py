"""Retrieval evaluation and ablation: does search return the passage with the answer?

For each answerable question in data/eval_questions.jsonl, every search setup
returns its top 10 chunks. A chunk is a hit if it comes from a gold document and
contains the gold quote (see eval/common.py), so the gold set works for any
chunking. Reported per setup:

  recall@k   share of questions with a hit in the top k (k = 1, 3, 5, 10)
  MRR@10     mean of 1/rank of the first hit (0 if none): rewards ranking it high
  latency    p50 / p95 time of the search call

Setups (the ablation): bm25, vector, hybrid, hybrid+rerank.

Questions whose quote is not inside any single chunk (split across a chunk
boundary) can never be hit; they are counted as misses and listed, because they
are a property of the chunking being tested.

Usage:
    python eval/retrieval_eval.py                    # all four setups
    python eval/retrieval_eval.py --no-rerank        # skip the slow reranker
    python eval/retrieval_eval.py --index index-400 --label chunks-400 --split dev
"""

import argparse
import json
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "eval"))

from common import contains_evidence, load_questions  # noqa: E402
from librarian.retrieve import Retriever  # noqa: E402

KS = (1, 3, 5, 10)
SETUPS = {
    "bm25": dict(mode="bm25"),
    "vector": dict(mode="vector"),
    "hybrid": dict(mode="hybrid"),
    "hybrid+rerank": dict(mode="hybrid", rerank=True),
}
RESULTS = ROOT / "eval" / "results"


def first_hit(hits, question):
    for rank, hit in enumerate(hits, 1):
        if contains_evidence(hit.chunk, question):
            return rank
    return None


def summarise(ranks, latencies):
    n = len(ranks)
    out = {f"recall@{k}": sum(r is not None and r <= k for r in ranks) / n for k in KS}
    out["mrr@10"] = sum(1 / r for r in ranks if r) / n
    out["latency_p50_ms"] = float(np.percentile(latencies, 50))
    out["latency_p95_ms"] = float(np.percentile(latencies, 95))
    return out


def table(rows, columns):
    lines = ["| " + " | ".join(columns) + " |", "|" + "---|" * len(columns)]
    lines += ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--index", default=str(ROOT / "index"))
    parser.add_argument("--label", default="baseline", help="name for this run in the results file")
    parser.add_argument("--no-rerank", action="store_true")
    parser.add_argument("--split", choices=["dev", "test", "all"], default="all",
                        help="tune on dev; use test only for final numbers")
    args = parser.parse_args()

    questions = [q for q in load_questions() if q["type"] != "unanswerable"
                 and (args.split == "all" or q.get("split") == args.split)]
    if args.split != "all":
        args.label = f"{args.label}-{args.split}"
    retriever = Retriever(args.index)
    setups = {k: v for k, v in SETUPS.items() if not (args.no_rerank and v.get("rerank"))}

    # Gold quotes that no single chunk contains (split across a chunk boundary).
    unreachable = [q["id"] for q in questions
                   if not any(contains_evidence(c, q) for c in retriever.chunks)]

    retriever.search("warm-up", k=1)  # load the embedding model before timing
    if any(s.get("rerank") for s in setups.values()):
        retriever.search("warm-up", k=1, rerank=True)

    per_question, summary = defaultdict(dict), {}
    for name, params in setups.items():
        ranks, latencies = [], []
        start = time.time()
        for q in questions:
            t = time.perf_counter()
            hits = retriever.search(q["question"], k=10, **params)
            latencies.append((time.perf_counter() - t) * 1000)
            rank = first_hit(hits, q)
            ranks.append(rank)
            per_question[q["id"]][name] = rank
        summary[name] = summarise(ranks, latencies)
        print(f"{name:14} done in {time.time() - start:5.0f}s  recall@5={summary[name]['recall@5']:.3f}")

    # Breakdowns: where does each setup fail?
    breakdown = {}
    for field in ("type", "country", "lang", "difficulty"):
        groups = defaultdict(list)
        for q in questions:
            groups[q[field]].append(q["id"])
        breakdown[field] = {
            value: {"n": len(ids), **{name: sum(per_question[i][name] is not None and per_question[i][name] <= 5
                                                for i in ids) / len(ids) for name in setups}}
            for value, ids in sorted(groups.items(), key=lambda kv: str(kv[0]))
        }

    best = max(summary, key=lambda s: summary[s]["recall@5"])
    misses = [q["id"] for q in questions if per_question[q["id"]][best] is None]

    RESULTS.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    report = {"label": args.label, "index": args.index, "n_questions": len(questions),
              "unreachable": unreachable, "summary": summary, "breakdown": breakdown,
              "per_question": per_question, "misses_of_best": {"setup": best, "ids": misses}}
    (RESULTS / f"retrieval-{args.label}-{stamp}.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    cols = ["setup"] + [f"recall@{k}" for k in KS] + ["MRR@10", "p50 ms", "p95 ms"]
    rows = [[name] + [f"{s[f'recall@{k}']:.3f}" for k in KS] +
            [f"{s['mrr@10']:.3f}", f"{s['latency_p50_ms']:.0f}", f"{s['latency_p95_ms']:.0f}"]
            for name, s in summary.items()]
    md = [f"# Retrieval evaluation: {args.label}", "",
          f"{len(questions)} answerable questions · index `{Path(args.index).name}` · {stamp}", "",
          table(rows, cols), ""]
    for field, groups in breakdown.items():
        md += [f"### Recall@5 by {field}", "",
               table([[str(v), str(g["n"])] + [f"{g[s]:.2f}" for s in setups] for v, g in groups.items()],
                     [field, "n"] + list(setups)), ""]
    md += [f"Quotes not inside any single chunk ({len(unreachable)}): {', '.join(unreachable) or 'none'}", "",
           f"Misses of the best setup ({best}, top 10, {len(misses)}): {', '.join(misses) or 'none'}"]
    (RESULTS / f"retrieval-{args.label}.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print()
    print(table(rows, cols))
    print(f"\nunreachable quotes: {unreachable or 'none'}")
    print(f"misses of {best} in top 10: {misses}")
    print(f"\nreport: eval/results/retrieval-{args.label}.md")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
