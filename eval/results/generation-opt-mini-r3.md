# Generation evaluation: opt-mini-r3

125 questions · answer model `gpt-5.4-mini` (effort low) · judge `gpt-5.4-mini` · 20261025-201959

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **92.8%** |
| Correctness on answerable questions (partial = 0.5) | 91.8% |
| Strictly correct on answerable questions | 90.0% |
| Faithfulness (all claims supported by sources) | 96.1% |
| Citation accuracy | 92.2% |
| "I don't know" on unanswerable questions | 100.0% |
| "I don't know" on answerable questions (false refusals) | 6.4% |
| Correct answers whose gold passage was not retrieved | 7 |
| Cost per question (answer only) | $0.0015 |
| Latency end to end, p50 / p95 | 3.7 s / 6.6 s |
| Tokens per question, in / out | 1346 / 122 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 75.0% |
| cross_lingual | 27 | 77.8% |
| date | 11 | 100.0% |
| fact | 13 | 96.2% |
| list | 3 | 83.3% |
| number | 40 | 98.8% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 100.0% |
| yes_no | 11 | 95.5% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q012** correct, faithful=True, citations=False: L’ענה donne bien la date limite actuelle du dossier DAP : le 11 décembre 2026, ce qui correspond au calendrier fourni. La remarque sur le 31 janvier est aussi cohérente avec les sources, mais la citation de cette seconde phrase est un peu faible.
- **q015** refused an answerable question. Gold passage retrieved: False
- **q027** refused an answerable question. Gold passage retrieved: False
- **q033** refused an answerable question. Gold passage retrieved: False
- **q044** refused an answerable question. Gold passage retrieved: False
- **q045** correct, faithful=False, citations=False: L’essentiel de la réponse correspond bien aux conditions demandées: 20 heures par semaine et un financement annuel de 11 904 €. En revanche, les comparaisons de date entre sources (« plus récente », « plus ancienne ») ne sont pas étayées par les sources fournies.
- **q047** refused an answerable question. Gold passage retrieved: False
- **q050** refused an answerable question. Gold passage retrieved: False
- **q055** correct, faithful=False, citations=False: The answer correctly says to apply through the DAAD portal/database and gives the relevant application steps. However, it adds that the recommendation form is signed, which is not stated in the provided sources.
- **q065** correct, faithful=False, citations=False: The answer gives the correct deadline of 1 March, matching the gold answer. However, it adds an unsupported claim about Tunisia’s status, and the citation does not fully support that claim.
- **q069** partially_correct, faithful=True, citations=True: The answer correctly gives the German requirement and the 1,800 EUR semester allowance, but it leaves out the additional funding for study projects abroad. All factual claims are supported by the cited sources and cited appropriately.
- **q074** correct, faithful=True, citations=False: The answer correctly says that KAAD can fund a German language course up to 6 months. All substantive claims are supported by the source, but the opening 'Yes.' is an uncited factual statement.
- **q075** correct, faithful=True, citations=False: The answer gives the correct living-expense amounts for a single applicant outside Quebec, matching the gold answer. Its factual claims are supported by the sources, but the first sentence is missing the citation that supports the applicable date range.
- **q082** partially_correct, faithful=True, citations=True: It correctly says a master’s student at a public institution does not need a PAL/TAL starting January 1, 2026. However, it omits the Quebec exception, which can change the answer in some cases.
- **q096** partially_correct, faithful=True, citations=True: The answer correctly identifies the Quebec Acceptance Certificate (CAQ). However, it leaves out the gold answer’s additional point that Quebec has its own financial requirements, so it is only partially complete.
- **q105** partially_correct, faithful=False, citations=False: The answer names two masters that are supported by the sources, but it misses RESCO from the gold answer and adds EMJM STEPS without source support for the renewable-energy claim. The citation for the sentence does not fully support the renewable-energy classification of EMJM STEPS.
- **q108** correct, faithful=True, citations=False: The answer gives the same yes/no conclusion as the gold answer and does not contradict the sources. The citation set is slightly off because [S1] is not direct support for the recent-graduate claim, although [S2] and [S3] are.
