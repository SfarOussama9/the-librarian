# Generation evaluation: opt-nano-high-newest-r2

125 questions · answer model `gpt-5.4-nano` (effort high) · judge `gpt-5.4-mini` · 20261025-204705

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **90.8%** |
| Correctness on answerable questions (partial = 0.5) | 89.5% |
| Strictly correct on answerable questions | 87.3% |
| Faithfulness (all claims supported by sources) | 96.2% |
| Citation accuracy | 94.2% |
| "I don't know" on unanswerable questions | 100.0% |
| "I don't know" on answerable questions (false refusals) | 5.5% |
| Correct answers whose gold passage was not retrieved | 7 |
| Cost per question (answer only) | $0.0005 |
| Latency end to end, p50 / p95 | 4.1 s / 7.2 s |
| Tokens per question, in / out | 1346 / 177 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 87.5% |
| cross_lingual | 27 | 77.8% |
| date | 11 | 81.8% |
| fact | 13 | 100.0% |
| list | 3 | 83.3% |
| number | 40 | 95.0% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 100.0% |
| yes_no | 11 | 95.5% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q013** incorrect, faithful=False, citations=False: The answer gives the wrong deadline: for hors-DAP, the dossier submission deadline is 18/12/2026, not 31/05/2027. The citation is also incorrect because the source contradicts the stated date.
- **q015** refused an answerable question. Gold passage retrieved: False
- **q021** correct, faithful=False, citations=False: The answer matches the gold answer’s main point: Tunisian candidates are not exempt from the TCF-DAP just because French is spoken in Tunisia, and only specific exemptions apply. However, it includes an unsupported claim about French being widely used and does not cite each factual sentence separately.
- **q027** refused an answerable question. Gold passage retrieved: False
- **q030** correct, faithful=False, citations=False: La réponse donne la bonne conclusion : une bourse du gouvernement tunisien n’exonère pas de la CVEC. En revanche, elle ajoute une classification explicite du gouvernement tunisien comme « gouvernement étranger » qui n’est pas formulée telle quelle dans la source.
- **q033** refused an answerable question. Gold passage retrieved: False
- **q043** incorrect, faithful=True, citations=True: La réponse ne donne pas le montant demandé pour un visa étudiant en Allemagne. Elle parle à la place d’un visa de cours de langue et d’un compte bloqué en Tunisie, alors que la bonne réponse attendue est 11 904 EUR par an (992 EUR par mois).
- **q044** partially_correct, faithful=True, citations=True: The answer gives general guidance about blocked accounts, but it does not state the actual required amount the question asked for. Its factual claims are supported by the source, and the citation is appropriate.
- **q047** refused an answerable question. Gold passage retrieved: False
- **q050** incorrect, faithful=True, citations=True: The answer talks about a Canadian visa application, not a German visa application, so it does not answer the question asked. Its factual statement about certified translations is supported by the source, but it misses the German-visa/sworn-translator point entirely.
- **q062** partially_correct, faithful=True, citations=True: The answer gives the correct monthly amount for international students, 992 EUR, but it also adds the doctoral scholarship amount, which the question did not ask for. All factual claims are supported by the sources and cited correctly.
- **q065** refused an answerable question. Gold passage retrieved: True
- **q074** correct, faithful=True, citations=False: The answer matches the gold answer: KAAD does fund German language courses, up to 6 months. All factual claims are supported by the source, but the first sentence lacks an explicit citation.
- **q075** correct, faithful=False, citations=False: The answer gives the correct current amount and also includes the earlier amount, which matches the gold answer. However, the earlier-date claim is not fully supported by the cited source excerpt, so the answer is not fully faithful and the citation is not fully correct.
- **q081** partially_correct, faithful=True, citations=True: The answer gives the 8-month minimum, which matches the sources, but it omits the full-time condition from the gold answer. The cited sources support the statement as written.
- **q086** partially_correct, faithful=True, citations=True: It gives the main answer correctly: you cannot work during an authorized leave, and the leave can be up to 150 days. However, it adds an irrelevant strike-related exception that does not answer the question and could confuse the result.
- **q105** correct, faithful=True, citations=False: The answer names the same three renewable-energy-related Erasmus Mundus masters as the gold answer and does not contradict it. The only issue is citation formatting: the introductory sentence is uncited.
- **q110** partially_correct, faithful=True, citations=True: The answer correctly names the travel, visa, and living/subsistence support, but it omits the participation costs that the scholarship also covers. All factual claims in the answer are supported by the sources and cited appropriately.
