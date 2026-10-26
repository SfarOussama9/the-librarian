# Generation evaluation: opt-mini-r1

125 questions · answer model `gpt-5.4-mini` · judge `gpt-5.4-mini` · 20261025-194310

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **93.2%** |
| Correctness on answerable questions (partial = 0.5) | 92.3% |
| Strictly correct on answerable questions | 91.8% |
| Faithfulness (all claims supported by sources) | 97.1% |
| Citation accuracy | 96.1% |
| "I don't know" on unanswerable questions | 100.0% |
| "I don't know" on answerable questions (false refusals) | 6.4% |
| Correct answers whose gold passage was not retrieved | 8 |
| Cost per question (answer only) | $0.0016 |
| Latency end to end, p50 / p95 | 3.9 s / 6.9 s |
| Tokens per question, in / out | 1346 / 124 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 75.0% |
| cross_lingual | 27 | 77.8% |
| date | 11 | 100.0% |
| fact | 13 | 92.3% |
| list | 3 | 83.3% |
| number | 40 | 100.0% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 100.0% |
| yes_no | 11 | 100.0% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q012** correct, faithful=False, citations=False: La réponse donne bien la date limite demandée : le 11 décembre 2026. En revanche, elle ajoute une justification sur la « source la plus récente » qui n’est pas appuyée par les sources.
- **q015** refused an answerable question. Gold passage retrieved: False
- **q027** refused an answerable question. Gold passage retrieved: False
- **q033** refused an answerable question. Gold passage retrieved: False
- **q044** refused an answerable question. Gold passage retrieved: False
- **q047** refused an answerable question. Gold passage retrieved: False
- **q048** incorrect, faithful=False, citations=False: La réponse donne la règle du cours de langue préparatoire, pas celle demandée pour des études universitaires avant immatriculation. Selon la source correspondant à ce cas, il faut une assurance privée pour 90 jours à compter de l'arrivée.
- **q050** refused an answerable question. Gold passage retrieved: False
- **q065** correct, faithful=False, citations=False: The answer gives the correct deadline of 1 March. However, it adds an unsupported Tunisia-specific classification that is not stated in the sources, so the response is not fully faithful.
- **q108** correct, faithful=True, citations=False: The answer matches the gold answer and is supported by the sources. The only issue is citation formatting: the affirmative first sentence is uncited.
- **q110** partially_correct, faithful=True, citations=True: The answer correctly mentions travel, visa, and living/subsistence support, but it leaves out that Erasmus Mundus scholarships also cover participation costs. All factual claims in the answer are supported by the cited sources.
