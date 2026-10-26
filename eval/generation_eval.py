"""Generation evaluation: are the Librarian's answers correct, faithful and honest?

Each question goes through the full pipeline (search + reranker + answer). Then:

  "I don't know"   counted directly from the model's `answerable` flag:
                     - unanswerable questions it refused      (should be high)
                     - answerable questions it refused        (should be low)
  correctness      LLM judge: does the answer match the gold answer?
                     correct = 1, partially correct = 0.5, incorrect = 0
  faithfulness     LLM judge: is every claim supported by the sources shown?
  citations        LLM judge: does each cited [S#] really support what it is cited for?
  wrong passage    answer judged correct although no source shown contains the gold
                   quote ("a good answer from the wrong passage is a bug", brief slide 9)

Headline "accuracy" (the number the Week 8 "at most 2 points lost" rule applies to):
share of all questions handled correctly = answerable questions scored by correctness,
plus unanswerable questions counted 1 if refused, 0 otherwise.

The judge is another model call and can be wrong: eval/results/judge-spotcheck-*.md
lists a random sample of verdicts for a person to check.

Usage:
    python eval/generation_eval.py                 # all 125 questions
    python eval/generation_eval.py --split dev     # tune on dev
    python eval/generation_eval.py --model gpt-5.4-nano --label nano
"""

import argparse
import json
import random
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "eval"))

from common import contains_evidence, load_questions  # noqa: E402
from librarian.generate import INSTRUCTIONS, Librarian, cost, format_sources  # noqa: E402

JUDGE_MODEL = "gpt-5.4-mini"
RESULTS = ROOT / "eval" / "results"

JUDGE_INSTRUCTIONS = """You grade answers produced by a retrieval-augmented assistant for students.
You receive: the question, a GOLD answer written by the evaluation team, the SOURCES the assistant
was given (labelled [S1], [S2]...), and the assistant's ANSWER with its [S#] citations.

Judge three things:
1. correctness: does the ANSWER answer what the QUESTION asks, in agreement with the GOLD answer?
   - Grade against what the question asks. The gold answer may contain extra context (how to apply,
     related limits, side notes); leaving out details the question did not ask for is NOT an error.
   - "correct": gives the facts the question asks for (numbers, dates, yes/no, names) as in the gold
     answer, and contradicts nothing in it. Different wording or language is fine.
   - "partially_correct": answers only part of what the question asks (e.g. one of two requested
     facts), or is right but misses a condition that changes the answer.
   - "incorrect": wrong key fact, contradicts the gold answer, or says it doesn't know.
2. faithful: true if EVERY factual claim in the ANSWER is supported by the SOURCES (not by the gold
   answer, not by general knowledge). List any unsupported claims.
3. citations_correct: true if each [S#] citation points to a source that actually supports the
   sentence it is attached to, and every factual sentence has a citation. List any problems.

Be strict about numbers, dates and conditions. Write "reason" in one or two plain English sentences.
Return JSON only."""

JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "correctness": {"type": "string", "enum": ["correct", "partially_correct", "incorrect"]},
        "faithful": {"type": "boolean"},
        "unsupported_claims": {"type": "array", "items": {"type": "string"}},
        "citations_correct": {"type": "boolean"},
        "citation_problems": {"type": "array", "items": {"type": "string"}},
        "reason": {"type": "string"},
    },
    "required": ["correctness", "faithful", "unsupported_claims", "citations_correct",
                 "citation_problems", "reason"],
    "additionalProperties": False,
}
SCORE = {"correct": 1.0, "partially_correct": 0.5, "incorrect": 0.0}


def judge(client, question, gold, answer_text, chunks):
    response = client.responses.create(
        model=JUDGE_MODEL,
        instructions=JUDGE_INSTRUCTIONS,
        input=(f"QUESTION: {question}\n\nGOLD ANSWER: {gold}\n\nSOURCES:\n\n{format_sources(chunks)}"
               f"\n\nANSWER: {answer_text}"),
        reasoning={"effort": "medium"},
        text={"format": {"type": "json_schema", "name": "verdict", "schema": JUDGE_SCHEMA, "strict": True}},
    )
    u = response.usage
    usage = {"input_tokens": u.input_tokens, "output_tokens": u.output_tokens,
             "cached_input_tokens": getattr(u.input_tokens_details, "cached_tokens", 0) or 0}
    return json.loads(response.output_text), cost(JUDGE_MODEL, usage)


def pct(x):
    return "n/a" if x is None else f"{100 * x:.1f}%"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--split", choices=["dev", "test", "all"], default="all")
    parser.add_argument("--model", default=None, help="answer model (default: librarian.generate.MODEL)")
    parser.add_argument("--effort", default=None, help="reasoning effort (default: librarian.generate.EFFORT)")
    parser.add_argument("--examples", choices=["0", "1"], default=None, help="worked examples in the prompt")
    parser.add_argument("--newest-first", choices=["0", "1"], default=None, help="dated sources newest first")
    parser.add_argument("--label", default="baseline")
    parser.add_argument("--limit", type=int, default=None, help="only the first N questions (smoke test)")
    parser.add_argument("--retrieval", default=None,
                        help="JSON file of search results: reused if it exists, else written. Search is "
                             "deterministic, so runs that only change generation can share one (and "
                             "keep its timings, measured once on a quiet machine)")
    args = parser.parse_args()

    questions = [q for q in load_questions() if args.split == "all" or q.get("split") == args.split]
    if args.limit:
        questions = questions[: args.limit]
    label = args.label if args.split == "all" else f"{args.label}-{args.split}"

    lib = Librarian(**({"model": args.model} if args.model else {}), **({"effort": args.effort} if args.effort else {}),
                    **({"examples": args.examples == "1"} if args.examples else {}),
                    **({"newest": args.newest_first == "1"} if args.newest_first else {}))
    chunk_by_id = {c["chunk_id"]: c for c in lib.retriever.chunks}
    saved = {}
    if args.retrieval and Path(args.retrieval).exists():
        saved = json.loads(Path(args.retrieval).read_text(encoding="utf-8"))
    else:
        lib.retriever.search("warm-up", k=1, rerank=True)  # load models before timing

    records, judge_cost = [], 0.0
    start = time.time()
    for n, q in enumerate(questions, 1):
        try:
            if q["id"] in saved:
                result = lib.answer_from(q["question"], [chunk_by_id[c] for c in saved[q["id"]]["chunks"]],
                                         saved[q["id"]]["seconds"])
            else:
                result = lib.ask(q["question"])
        except Exception as e:  # keep going; a failed call counts as a wrong answer
            records.append({"id": q["id"], "error": f"{type(e).__name__}: {e}"})
            print(f"[{n}/{len(questions)}] {q['id']} ERROR {e}")
            continue
        chunks = [chunk_by_id[c] for c in result.sources]
        rec = {
            "id": q["id"], "split": q.get("split"), "type": q["type"], "country": q["country"],
            "lang": q["lang"], "question": q["question"], "gold": q["answer"],
            "answer": result.answer, "answerable_pred": result.answerable,
            "citations": [c["chunk_id"] for c in result.citations], "sources": result.sources,
            "gold_in_sources": (any(contains_evidence(c, q) for c in chunks)
                                if q["type"] != "unanswerable" else None),
            "usage": result.usage, "cost_usd": result.cost_usd, "latency_s": result.latency_s,
        }
        if q["type"] != "unanswerable" and result.answerable:
            verdict, c = judge(lib.client, q["question"], q["answer"], result.answer, chunks)
            rec["judge"], judge_cost = verdict, judge_cost + c
        records.append(rec)
        status = rec.get("judge", {}).get("correctness") or ("refused" if not result.answerable else "answered")
        print(f"[{n}/{len(questions)}] {q['id']:5} {status:18} {result.latency_s['total']:5.1f}s ${result.cost_usd:.4f}")

    if args.retrieval and not saved:
        Path(args.retrieval).write_text(json.dumps(
            {r["id"]: {"chunks": r["sources"], "seconds": r["latency_s"]["retrieval"]}
             for r in records if "error" not in r}, indent=1), encoding="utf-8")

    ok = [r for r in records if "error" not in r]
    answerable = [r for r in ok if r["type"] != "unanswerable"]
    unanswerable = [r for r in ok if r["type"] == "unanswerable"]
    judged = [r for r in answerable if "judge" in r]
    errors = len(records) - len(ok)

    correctness = [SCORE[r["judge"]["correctness"]] if "judge" in r else 0.0 for r in answerable]
    handled = correctness + [0.0 if r["answerable_pred"] else 1.0 for r in unanswerable]
    n_total = len(questions)  # errors count as failures
    totals = [r["latency_s"]["total"] for r in ok]
    summary = {
        "n_questions": n_total, "errors": errors,
        "accuracy": sum(handled) / n_total,
        "correctness_answerable": sum(correctness) / max(1, len(answerable)),
        "strictly_correct_answerable": sum(r.get("judge", {}).get("correctness") == "correct" for r in answerable) / max(1, len(answerable)),
        "faithfulness": sum(r["judge"]["faithful"] for r in judged) / max(1, len(judged)),
        "citation_accuracy": sum(r["judge"]["citations_correct"] for r in judged) / max(1, len(judged)),
        "refused_unanswerable": (sum(not r["answerable_pred"] for r in unanswerable) / len(unanswerable)) if unanswerable else None,
        "refused_answerable": sum(not r["answerable_pred"] for r in answerable) / max(1, len(answerable)),
        "correct_but_gold_not_retrieved": sum(r.get("judge", {}).get("correctness") == "correct" and not r["gold_in_sources"] for r in answerable),
        "cost_per_question_usd": sum(r["cost_usd"] for r in ok) / max(1, len(ok)),
        "judge_cost_usd": judge_cost,
        "latency_total_p50_s": float(np.percentile(totals, 50)),
        "latency_total_p95_s": float(np.percentile(totals, 95)),
        "latency_generation_p50_s": float(np.percentile([r["latency_s"]["generation"] for r in ok], 50)),
        "tokens_in_mean": float(np.mean([r["usage"]["input_tokens"] for r in ok])),
        "tokens_out_mean": float(np.mean([r["usage"]["output_tokens"] for r in ok])),
        "model": lib.model, "effort": lib.effort, "examples": lib.instructions != INSTRUCTIONS, "newest_first": lib.newest, "minutes": (time.time() - start) / 60,
    }

    # Accuracy by question type, to see where answers fail.
    by_type = defaultdict(list)
    for r, score in zip(answerable + unanswerable, handled):
        by_type[r["type"]].append(score)

    RESULTS.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    (RESULTS / f"generation-{label}-{stamp}.json").write_text(
        json.dumps({"label": label, "summary": summary, "records": records}, indent=2, ensure_ascii=False), encoding="utf-8")

    s = summary
    md = [f"# Generation evaluation: {label}", "",
          f"{n_total} questions · answer model `{s['model']}` (effort {s['effort']}) · judge `{JUDGE_MODEL}` · {stamp}", "",
          "| Metric | Value |", "|---|---|",
          f"| **Accuracy** (all questions handled correctly) | **{pct(s['accuracy'])}** |",
          f"| Correctness on answerable questions (partial = 0.5) | {pct(s['correctness_answerable'])} |",
          f"| Strictly correct on answerable questions | {pct(s['strictly_correct_answerable'])} |",
          f"| Faithfulness (all claims supported by sources) | {pct(s['faithfulness'])} |",
          f"| Citation accuracy | {pct(s['citation_accuracy'])} |",
          f"| \"I don't know\" on unanswerable questions | {pct(s['refused_unanswerable'])} |",
          f"| \"I don't know\" on answerable questions (false refusals) | {pct(s['refused_answerable'])} |",
          f"| Correct answers whose gold passage was not retrieved | {s['correct_but_gold_not_retrieved']} |",
          f"| Cost per question (answer only) | ${s['cost_per_question_usd']:.4f} |",
          f"| Latency end to end, p50 / p95 | {s['latency_total_p50_s']:.1f} s / {s['latency_total_p95_s']:.1f} s |",
          f"| Tokens per question, in / out | {s['tokens_in_mean']:.0f} / {s['tokens_out_mean']:.0f} |",
          f"| API errors | {errors} |", "",
          "### Accuracy by question type", "", "| type | n | accuracy |", "|---|---|---|"]
    md += [f"| {t} | {len(v)} | {pct(sum(v) / len(v))} |" for t, v in sorted(by_type.items())]
    md += ["", "### Failures", ""]
    for r in answerable:
        v = r.get("judge")
        if not v:
            md.append(f"- **{r['id']}** refused an answerable question. Gold passage retrieved: {r['gold_in_sources']}")
        elif v["correctness"] != "correct" or not v["faithful"] or not v["citations_correct"]:
            md.append(f"- **{r['id']}** {v['correctness']}, faithful={v['faithful']}, citations={v['citations_correct']}: {v['reason']}")
    for r in unanswerable:
        if r["answerable_pred"]:
            md.append(f"- **{r['id']}** answered an unanswerable question: {r['answer'][:150]}")
    (RESULTS / f"generation-{label}.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    # A random sample of judge verdicts for a person to check.
    sample = random.Random(7).sample(judged, min(15, len(judged)))
    spot = [f"# Judge spot-check: {label}", "",
            "For each item, read the answer and decide whether you agree with the judge. "
            "Write agree / disagree. The agreement rate goes in the report.", ""]
    for r in sample:
        v = r["judge"]
        spot += [f"## {r['id']}: judge says {v['correctness']}, faithful={v['faithful']}, citations={v['citations_correct']}",
                 f"**Q:** {r['question']}  ", f"**Gold:** {r['gold']}  ", f"**Answer:** {r['answer']}  ",
                 f"**Judge's reason:** {v['reason']}  ", "**Agree?** ", ""]
    (RESULTS / f"judge-spotcheck-{label}.md").write_text("\n".join(spot) + "\n", encoding="utf-8")

    print("\n" + "\n".join(md[4:18]))
    print(f"\njudge cost ${judge_cost:.3f} · report: eval/results/generation-{label}.md")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
