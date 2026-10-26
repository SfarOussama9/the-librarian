# Generation evaluation: conflict-rule-dev

90 questions · answer model `gpt-5.4-mini` · judge `gpt-5.4-mini` · 20261025-175116

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **94.4%** |
| Correctness on answerable questions (partial = 0.5) | 93.7% |
| Strictly correct on answerable questions | 92.4% |
| Faithfulness (all claims supported by sources) | 97.4% |
| Citation accuracy | 90.8% |
| "I don't know" on unanswerable questions | 100.0% |
| "I don't know" on answerable questions (false refusals) | 3.8% |
| Correct answers whose gold passage was not retrieved | 4 |
| Cost per question (answer only) | $0.0016 |
| Latency end to end, p50 / p95 | 5.6 s / 9.4 s |
| Tokens per question, in / out | 1321 / 128 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 3 | 66.7% |
| cross_lingual | 19 | 84.2% |
| date | 8 | 100.0% |
| fact | 9 | 100.0% |
| list | 1 | 50.0% |
| number | 30 | 98.3% |
| stale | 1 | 100.0% |
| unanswerable | 11 | 100.0% |
| yes_no | 8 | 100.0% |

### Failures

- **q012** incorrect, faithful=True, citations=True: L’ענה donne la mauvaise date limite : il cite l’ancienne FAQ (31 janvier) alors que la référence actuelle dans les sources est le 11/12/2026. La citation [S3] soutient bien la phrase écrite, mais elle ne répond pas correctement à la question.
- **q015** refused an answerable question. Gold passage retrieved: False
- **q033** refused an answerable question. Gold passage retrieved: False
- **q050** refused an answerable question. Gold passage retrieved: False
- **q053** correct, faithful=True, citations=False: The answer matches the gold answer: the Federal Foreign Office does not recommend a specific blocked account provider. Its supporting statement is also backed by the sources, though the citation formatting is slightly incomplete.
- **q065** correct, faithful=False, citations=False: The answer gives the correct deadline of 1 March. However, it adds an unsupported explanation that Tunisia is non-European/non-EU, which is not stated in the sources.
- **q066** correct, faithful=True, citations=False: The answer gives the correct age and German language requirements for a Tunisian applicant: under 35 and at least B2 German. All factual content is supported by the sources, though one citation is unnecessary for the language requirement.
- **q074** correct, faithful=True, citations=False: The answer correctly says that KAAD can fund a language course of up to 6 months. It omits the extra detail about preparatory German courses at home, but that was not required to answer the question.
- **q075** correct, faithful=True, citations=False: The answer gives the correct living-expense amounts for a single applicant outside Quebec, matching the gold answer. However, the second sentence’s citation is incomplete because [S1] does not by itself support the date range.
- **q081** partially_correct, faithful=True, citations=True: The answer gives the 8-month minimum, which matches the sources and the gold answer, but it leaves out the full-time requirement that is part of the question’s answer. Its factual claims are supported by the cited sources.
- **q091** correct, faithful=True, citations=False: The answer matches the sources: international students cannot work before their studies begin in Canada. The only issue is citation placement, since the first factual sentence is uncited.
- **q105** partially_correct, faithful=False, citations=False: The answer includes the three correct examples from the gold answer, but it also adds extra titles that are not clearly supported as renewable-energy Erasmus Mundus masters. Some of those additions are not supported by the provided sources.
