# Week 8 optimisation report

**Target (from the brief):** cut cost per request or p95 latency by 50%, losing at most
2 points of accuracy, measured before and after on the same test set.

**Result:** cost per question went from **$0.00155 to $0.00048 (−69%)**, and accuracy from
**92.7% to 90.8% (−1.9 points)**. We changed the answer model from `gpt-5.4-mini` (low
reasoning) to `gpt-5.4-nano` with high reasoning, and now show dated sources newest first.
p95 latency is unchanged. We tried to cut latency by 50% and couldn't (section 4).

## 1. How we measured

- **The same 125 questions** (`data/eval_questions.jsonl`, all splits) and the same judge
  (`gpt-5.4-mini`, the prompt in `eval/generation_eval.py`) for every setup.
- **Search ran once.** Search is deterministic, so its results (the 4 chunks per question
  and the time taken) were saved in `eval/results/search-baseline.json`, measured with
  nothing else running. Every setup answers from the same chunks, so accuracy differences
  come from generation alone (`--retrieval` flag of `eval/generation_eval.py`).
- **3 runs per setup.** One run of the same setup varies by up to ~3 accuracy points (the
  answer model and the judge are not deterministic), which is more than the 2-point budget.
  Tables show the mean and the range (min–max). `eval/compare_runs.py` builds them from the
  result files.
- **Accuracy** = share of all 125 questions handled correctly: correct answer (partial = 0.5)
  on answerable questions, "I don't know" on unanswerable ones.
- **Cost** = answer-model tokens × OpenAI list prices (Oct 2026), retries included. The judge
  is not part of the service and is not counted.

## 2. Before and after

| | Before: mini, low | After: nano, high, newest first | Change |
|---|---|---|---|
| Accuracy | 92.7% (92.0–93.2) | 90.8% (90.4–91.2) | **−1.9 points** |
| Faithfulness | 96.8% | 96.2% | −0.6 |
| Citation accuracy | 95.5% | 94.6% | −0.9 |
| "I don't know" on unanswerable | 100% | 97.8% | −2.2 (1 question in 1 of 3 runs) |
| **Cost per question** | **$0.00155** | **$0.00048** | **−69%** |
| Latency end to end, p50 / p95 | 4.0 s / 7.0 s | 4.1 s / 7.6 s | ≈ same |
| Answer step, p50 / p95 | 1.6 s / 3.4 s | 1.7 s / 4.3 s | slightly slower |

Run files: `eval/results/generation-opt-mini-r{1,2,3}.md` and
`generation-opt-nano-high-newest-r{1,2,3}.md`.

## 3. Every setup we tried (cost)

| Setup | Runs | Accuracy | Faithfulness | Citations | Cost / question |
|---|---|---|---|---|---|
| mini, low reasoning (**before**) | 3 | 92.7 (92.0–93.2) | 96.8 | 95.5 | $0.00155 |
| nano, low | 2 | 86.8 (86.8–86.8) | 95.2 | 93.2 | $0.00037 |
| nano, medium | 2 | 88.2 (88.0–88.4) | 94.7 | 92.3 | $0.00043 |
| nano, high | 3 | 90.9 (90.0–91.6) | 94.9 | 91.4 | $0.00049 |
| nano, high + worked examples in the prompt | 3 | 89.6 (88.8–90.8) | 93.6 | 92.6 | $0.00046 |
| **nano, high + newest source first (after)** | 3 | **90.8 (90.4–91.2)** | **96.2** | **94.6** | **$0.00048** |

What each step taught us:

1. **A smaller model alone loses too much** (−5.9 points). With low effort, nano spends ~10
   reasoning tokens per question and misreads numbers and dates (number questions: 92.5%
   vs 100% for mini).
2. **More reasoning wins most of it back.** Nano's tokens are cheap ($1.25 per 1M output vs
   $4.50 for mini), so high effort (~98 reasoning tokens) still costs a third of mini.
3. **Worked examples did not help.** Five examples with invented sources (`EXAMPLES` in
   `librarian/generate.py`, switched off) made the prompt 1,156 tokens long. Accuracy fell
   by 1.3 points, so we dropped them.
4. **Newest source first** (`newest_first()` in `librarian/generate.py`): dated chunks are
   reordered newest first among the positions they already hold, and undated chunks stay
   where the reranker put them. Accuracy is the same, but faithfulness (+1.3) and citations
   (+3.2) come back close to mini, so we kept it.

### Prompt caching: tested, no saving

The brief suggests caching the fixed part of the prompt. OpenAI caches only prompts of at
least 1,024 tokens, and our fixed instructions are 385 tokens, so **in Week 7 nothing was
ever cached** (0 cached tokens in every run). With the worked examples the prefix reached
1,156 tokens. A direct test (3 identical prefixes in a row, with and without a
`prompt_cache_key`) showed:

- `gpt-5.4-mini` cached 1,024 tokens from the second call on;
- **`gpt-5.4-nano` cached 0 tokens**, in every request shape we tried.

So caching gives nothing with nano. With mini it would save only ~7% per question, because
the examples it needs add more tokens than caching saves. We keep `prompt_cache_key` in the
request since it costs nothing.

### Caching repeated questions (web app)

`app/server.py` keeps the last 500 answers, keyed by the question text with case, spacing
and end punctuation ignored. A repeated question gets the stored answer with no search, no
model call and no cost. It doesn't show up in the numbers above (the eval has no
repeats); its effect depends on how often real users repeat questions (the logs mark
cached answers with `"cached_answer": true`).

## 4. Latency: why we did not hit −50%

Before, p95 end to end is about 7 s on a laptop: **search** takes 2.3 s p50 / 4.7 s p95
(almost all of it the cross-encoder reranker), and the **answer** takes 1.6 s / 3.4 s. Halving
p95 means reaching about 3.5 s, but the answer step alone already takes 3.4 s at p95. So
search would have to take almost no time. We tested the reranker options on the dev
questions (`eval/rerank_options.py`, results in `eval/results/rerank-options-dev.md`):

| Option | Gold passage in the 4 chunks | Search p50 | Search p95 |
|---|---|---|---|
| No reranker (hybrid top 4) | 0.709 | 0.01 s | 0.01 s |
| bge-reranker-v2-m3 int8 (**current**) | **0.886** | 2.32 s | 4.84 s |
| jina-reranker-v2-base-multilingual | 0.873 | 2.12 s | 3.79 s |
| ms-marco-MiniLM-L-12 (English only) | 0.722 | 0.83 s | 1.13 s |
| Skip the reranker when BM25 and vector search agree on the top chunk (30% skipped) | 0.873 | 2.17 s | 4.71 s |

- The only reranker fast enough is English-only and loses 16 points of recall (58 of our
  125 questions are in French).
- Skipping the reranker when search is confident skips 30% of questions. That helps the
  median, but p95 is set by the questions that still get reranked.
- In Week 7 we also tried a rerank depth of 10 instead of 20, which lost 7.6 points of
  recall@3 on dev.

None of these keeps accuracy within 2 points while halving p95, so latency was left
unchanged and the saving was made on cost. (Running the reranker on a GPU would solve it,
but the hosting would cost more than the whole OpenAI bill.)

## 5. What got worse (per question, averaged over the 3 runs)

| Question | Before | After | What happens |
|---|---|---|---|
| q043 German blocked account, French | 1.0 | 0.0 | The 2025 page (€11,904 per year of study) is in [S1], but nano quotes older figures that say "compte bloqué" literally (€10,236 / €1,027 per month). Mini picks the 2025 figure every time. |
| q013 Campus France deadline outside DAP | 1.0 | 0.0 | Nano gives a later deadline from another procedure. |
| q014 Campus France fees, q040 student counts | 1.0 | 0.67 | One wrong or incomplete number in some runs. |
| q086 Canada work during authorised leave | 1.0 | 0.67 | Partly answered in one run. |
| q048 arriving in Germany before enrolment | 0.67 | 1.0 | Better. |
| q044 blocked account, English | 0.0 | 0.5 | Better. |

The q043 regression matters: it's one of the most-asked questions for our users. If we had
more budget, a deterministic fix would be to answer a short list of key figures (blocked
account, Campus France fees, work hours) from the newest dated source, outside the model.

## 6. Cost model, today and at 100×

| | Per question | 1,000 questions | 100,000 questions (100×) |
|---|---|---|---|
| Before (mini) | $0.00155 | $1.55 | $155 |
| **After (nano)** | **$0.00048** | **$0.48** | **$48** |

Hosting is separate. The demo runs on Modal's free plan (4 CPUs, scales to zero). At 100×
traffic one container would no longer be enough, and compute, not the model, would become
the main cost.

## 7. Caveats

- −1.9 points is close to the 2-point limit, and it's a mean over 3 runs. The ranges don't
  overlap (90.4–91.2 after vs 92.0–93.2 before), so the loss is real, not noise.
- The setups were compared and chosen on the same 125 questions, so the final number may be
  slightly optimistic. We had no extra held-out set left to confirm it.
- The judge is an LLM (`gpt-5.4-mini`) and the same for every setup. It occasionally writes
  a word in another script in its reasons (e.g. a Hebrew word); the verdict fields aren't
  affected.

## How to reproduce

```
# search once, then the "before" runs (Week 7 setup)
LIBRARIAN_NEWEST_FIRST=0 python eval/generation_eval.py --model gpt-5.4-mini --effort low --label opt-mini-r1 --retrieval eval/results/search-baseline.json
# the "after" runs (current defaults)
python eval/generation_eval.py --label opt-nano-high-newest-r1 --retrieval eval/results/search-baseline.json
python eval/compare_runs.py opt-mini opt-nano-high-newest
python eval/rerank_options.py --split dev
```
