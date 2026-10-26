# Generation evaluation: conflict-rule-test

35 questions · answer model `gpt-5.4-mini` · judge `gpt-5.4-mini` · 20261025-175721

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **84.3%** |
| Correctness on answerable questions (partial = 0.5) | 82.3% |
| Strictly correct on answerable questions | 77.4% |
| Faithfulness (all claims supported by sources) | 100.0% |
| Citation accuracy | 100.0% |
| "I don't know" on unanswerable questions | 100.0% |
| "I don't know" on answerable questions (false refusals) | 12.9% |
| Correct answers whose gold passage was not retrieved | 2 |
| Cost per question (answer only) | $0.0016 |
| Latency end to end, p50 / p95 | 5.8 s / 10.4 s |
| Tokens per question, in / out | 1388 / 118 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 1 | 0.0% |
| cross_lingual | 8 | 62.5% |
| date | 3 | 100.0% |
| fact | 4 | 87.5% |
| list | 2 | 75.0% |
| number | 10 | 95.0% |
| unanswerable | 4 | 100.0% |
| yes_no | 3 | 100.0% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q027** refused an answerable question. Gold passage retrieved: False
- **q044** refused an answerable question. Gold passage retrieved: False
- **q047** refused an answerable question. Gold passage retrieved: False
- **q062** partially_correct, faithful=True, citations=True: It correctly states the 992 EUR monthly amount for international students, but it omits the health insurance funding and non-repayment detail from the gold answer. It also adds the doctoral amount, which is supported by the sources but is not what the question is asking for.
- **q092** partially_correct, faithful=True, citations=True: The answer correctly says what a SIN is and that you need one to work in Canada as a student. It leaves out the study-permit work-condition requirement mentioned in the gold answer, so it is incomplete.
- **q110** partially_correct, faithful=True, citations=True: The answer correctly says the scholarship contributes to travel, visa, and living/subsistence costs, but it leaves out the participation costs that the gold answer includes. All factual claims are supported by the sources and cited appropriately.
