"""Week 8: cheaper reranking options, compared on the same questions.

For every answerable question, hybrid search fetches the usual 20 candidates once.
Each option then picks the 4 chunks the answer model would read (TOP_K), and we
check whether the gold passage is among them (recall@4) and how long it took.

Options:
  rerank:<model>    rerank all 20 candidates with that cross-encoder
  skip-if-agree     no reranker when BM25 and vector search agree on the top
                    chunk (search is "confident"), else rerank with the default
  none              hybrid top 4, no reranker


Usage:
    python eval/rerank_options.py --split dev
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "eval"))

from common import contains_evidence, load_questions  # noqa: E402
from librarian.retrieve import RERANK_DEPTH, Retriever, searchable_text  # noqa: E402

RESULTS = ROOT / "eval" / "results"
TOP_K = 4
DEFAULT = "BAAI/bge-reranker-v2-m3-int8"
MODELS = [DEFAULT, "jinaai/jina-reranker-v2-base-multilingual", "Xenova/ms-marco-MiniLM-L-12-v2"]


def cross_encoder(name):
    from fastembed.rerank.cross_encoder import TextCrossEncoder
    from librarian.embed import THREADS
    return TextCrossEncoder(name, threads=THREADS)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--split", choices=["dev", "test", "all"], default="dev")
    parser.add_argument("--models", nargs="*", default=MODELS)
    args = parser.parse_args()

    questions = [q for q in load_questions() if q["type"] != "unanswerable"
                 and (args.split == "all" or q.get("split") == args.split)]
    r = Retriever()
    r.search("warm-up", k=1)

    # First stage, once per question: the 20 hybrid candidates and each ranking's top chunk.
    first = {}
    for q in questions:
        t = time.perf_counter()
        hits = r.search(q["question"], k=RERANK_DEPTH)
        first_s = time.perf_counter() - t
        bm25_top = r.search(q["question"], k=1, mode="bm25")
        vec_top = r.search(q["question"], k=1, mode="vector")
        first[q["id"]] = {
            "hits": [h.chunk for h in hits], "first_s": first_s,
            "agree": bool(bm25_top and vec_top and bm25_top[0].chunk["chunk_id"] == vec_top[0].chunk["chunk_id"]),
        }

    # Rerank scores per model (all 20 candidates), with timing.
    scores, timing = {}, {}
    for name in args.models:
        model = cross_encoder(name)
        list(model.rerank("warm-up", ["warm-up text"]))
        scores[name], timing[name] = {}, {}
        for q in questions:
            texts = [searchable_text(c) for c in first[q["id"]]["hits"]]
            t = time.perf_counter()
            scores[name][q["id"]] = [float(s) for s in model.rerank(q["question"], texts)]
            timing[name][q["id"]] = time.perf_counter() - t
        print(f"{name}: rerank p50 {np.percentile(list(timing[name].values()), 50):.2f}s")
        del model

    def recall(choose):
        """choose(q) -> (top-4 chunks, seconds spent after the first stage)."""
        hits, secs = 0, []
        for q in questions:
            chunks, s = choose(q)
            hits += any(contains_evidence(c, q) for c in chunks)
            secs.append(first[q["id"]]["first_s"] + s)
        return {"recall@4": hits / len(questions),
                "search_p50_s": float(np.percentile(secs, 50)), "search_p95_s": float(np.percentile(secs, 95))}

    def reranked(name):
        def choose(q):
            c, s = first[q["id"]]["hits"], scores[name][q["id"]]
            order = sorted(range(len(c)), key=lambda i: s[i], reverse=True)[:TOP_K]
            return [c[i] for i in order], timing[name][q["id"]]
        return choose

    rows = {"none": recall(lambda q: (first[q["id"]]["hits"][:TOP_K], 0.0))}
    for name in args.models:
        rows[f"rerank:{name}"] = recall(reranked(name))
    default = reranked(DEFAULT) if DEFAULT in scores else None
    if default:
        rows["skip-if-agree"] = recall(lambda q: (first[q["id"]]["hits"][:TOP_K], 0.0)
                                       if first[q["id"]]["agree"] else default(q))
    skipped = sum(f["agree"] for f in first.values()) / len(first)

    stamp = time.strftime("%Y%m%d-%H%M%S")
    md = [f"# Reranker options: {args.split}", "",
          f"{len(questions)} answerable questions · {RERANK_DEPTH} hybrid candidates · top {TOP_K} kept · "
          f"threads {os.getenv('ONNX_THREADS') or 'default'} · {stamp}", "",
          "| option | recall@4 | search p50 | search p95 |", "|---|---|---|---|"]
    md += [f"| {k} | {v['recall@4']:.3f} | {v['search_p50_s']:.2f} s | {v['search_p95_s']:.2f} s |"
           for k, v in rows.items()]
    md += ["", f"skip-if-agree skips the reranker on {skipped:.0%} of questions."]
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / f"rerank-options-{args.split}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (RESULTS / f"rerank-options-{args.split}-{stamp}.json").write_text(json.dumps(
        {"rows": rows, "skipped": skipped, "timing": timing, "scores": scores,
         "agree": {k: v["agree"] for k, v in first.items()}}, indent=2), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
