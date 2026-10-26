# Postmortem

## What went wrong

### 1. The corpus was hard to collect
Canada.ca, DAAD and the Wayback Machine block automated requests from Tunisian networks (the whole
mobile network was flagged as bot traffic, HTTP 429). We lost about a day before switching to a
mixed strategy: direct download where possible, Jina Reader for blocked pages, and manual browser
saves for 16 DAAD Tunisie pages. Each document's collection method is recorded in the manifest, but
rebuilding the corpus from scratch still depends on a third-party reader service.

**Lesson:** test access to every source on day one, from the network you will actually use.

### 2. Paginated pages hid most of the content
The first fetch of the DAAD database captured 5 of 88 programmes, the Campus France FAQ had
questions without answers (each answer is a separate page), and the Erasmus Mundus catalogue
showed 1 page of 11. Word counts looked fine; only reading the extracted text showed the gaps. We
found DAAD's full data file (`scholarships.js`) and fetched every page and answer.

**Lesson:** read samples of the extracted text, don't just count it.

### 3. Over-eager cleaning deleted real content
Removing every `<aside>` element dropped the embassy's info boxes and a Canada.ca alert. A
general-purpose extractor (trafilatura) also cut content on several sites. We replaced it with one
content selector per publisher.

### 4. The first chunks were too small
The first chunker split at every heading: median chunk 69 words, with FAQ questions separated from
their answers. We added cross-section packing and a minimum chunk size, then tested 150/250/400
words. 150 won at equal context.

### 5. A stale official PDF gave a wrong answer
The German embassy's checklist PDF (2020) gives a €10,332 blocked account; the current figure is
€11,904. Both are official and both are online. Our download date couldn't tell them apart, so we
added publication-date extraction and a "newest source wins" rule.

### 6. The "newest source wins" rule misfired
The first version let a newer source override an older one even when they described different
situations (language course vs. degree studies), which broke 2 correct answers (q048, q095). We
rewrote the rule: only the same value in the same situation is a conflict. q048 and q095 were
fixed; test-split accuracy was 84.3%, against 80.0–84.3% for two runs of the old rule.

### 7. One eval run is not a measurement
Running the same setup twice moved accuracy by up to 3 points, which is more than the 2-point
budget for Week 8. Our first comparisons used single runs. For Week 8 we saved the search results
once and ran each setup 3 times.

### 8. The LLM judge needed fixing
The first judge marked answers wrong for leaving out details that the gold answer had but the
question didn't ask for. We rewrote it to grade only what the question asks. A spot-check of 15
verdicts found 14 correct; the one error was too lenient (q014). The judge also occasionally writes
words in other scripts (Hebrew, Chinese) in its reasons.

### 9. Small-model glitches
`gpt-5.4-mini` once answered an English question in French and once inserted a Hindi word into a
French answer. We added a language hint to every request and an automatic retry when another script
appears.

### 10. Deployment was slower than planned
Hugging Face Spaces now requires a paid plan for Docker apps (HTTP 402), so we moved to Modal. On
Modal the reranker took 55 s per question at first: ONNX Runtime saw the host's 20+ cores and
oversubscribed the 4 the container may use. Capping threads brought it to 6–16 s, but the int8
reranker still runs slowly on Modal's CPUs (no VNNI instructions). Answers take 12–22 s online
versus ~4 s on a laptop.

### 11. Week 8: we could not halve latency
At p95 the answer step alone takes 3.4 s, about half the total, so halving p95 would need near-zero
search time. Every faster reranker lost too much recall (the only fast one is English-only:
−16 points). We cut cost instead (−69%), and the smaller model now gets the German blocked-account
question in French (q043) wrong, which the larger model always got right.

### 12. Prompt caching did not work for us
Our fixed instructions (385 tokens) are under OpenAI's 1,024-token caching minimum. When we padded
them with worked examples to 1,156 tokens, `gpt-5.4-mini` cached the prefix but `gpt-5.4-nano`
cached nothing, and the examples lowered accuracy.

## What we would do differently
- Pick 10 hard questions on day one and track them through every change.
- Build the eval harness before the generation prompt, and always run it 3 times.
- Treat document dates as first-class metadata from the start.
- Translate or expand queries into both languages (cross-lingual retrieval is our largest error
  source).
- Choose the hosting platform early and benchmark the reranker on it before committing to a model.
