# Generation evaluation: baseline

125 questions · answer model `gpt-5.4-mini` · judge `gpt-5.4-mini` · 20261025-173039

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **91.2%** |
| Correctness on answerable questions (partial = 0.5) | 90.0% |
| Strictly correct on answerable questions | 89.1% |
| Faithfulness (all claims supported by sources) | 95.1% |
| Citation accuracy | 96.1% |
| "I don't know" on unanswerable questions | 100.0% |
| "I don't know" on answerable questions (false refusals) | 6.4% |
| Correct answers whose gold passage was not retrieved | 7 |
| Cost per question (answer only) | $0.0015 |
| Latency end to end, p50 / p95 | 5.3 s / 9.1 s |
| Tokens per question, in / out | 1254 / 119 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 50.0% |
| cross_lingual | 27 | 77.8% |
| date | 11 | 100.0% |
| fact | 13 | 92.3% |
| list | 3 | 83.3% |
| number | 40 | 98.8% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 100.0% |
| yes_no | 11 | 90.9% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q012** incorrect, faithful=True, citations=True: La réponse donne comme date limite principale le 31 janvier, alors que la référence actuelle indiquée dans le gold est le 11/12/2026. Les phrases citées sont bien appuyées par les sources, mais la réponse ne correspond pas à la bonne date demandée.
- **q015** refused an answerable question. Gold passage retrieved: False
- **q027** refused an answerable question. Gold passage retrieved: False
- **q033** refused an answerable question. Gold passage retrieved: False
- **q044** refused an answerable question. Gold passage retrieved: False
- **q047** refused an answerable question. Gold passage retrieved: False
- **q048** incorrect, faithful=False, citations=False: La réponse contredit l’élément central de la réponse attendue : pour des études universitaires avant immatriculation, l’assurance demandée est une assurance privée pour 90 jours à compter de l’arrivée. Elle mélange en plus cette situation avec la règle spécifique du cours de langue préparatoire.
- **q050** refused an answerable question. Gold passage retrieved: False
- **q062** partially_correct, faithful=True, citations=True: The answer gives the correct monthly base amount of 992 EUR, but it leaves out that health insurance costs are also covered. The cited source supports the stated amount.
- **q065** correct, faithful=False, citations=False: The answer gives the correct deadline of 1 March for a Tunisian applicant. However, it adds an unsupported claim about Tunisia being outside the EU, which is not stated in the provided sources.
- **q066** correct, faithful=False, citations=True: The answer gives the correct age and German-language requirements: under 35 and at least B2. It also adds a comparison to the general IPS programme, which is consistent with the sources, but the Tunisian-applicant framing is not explicitly supported by the sources.
- **q095** incorrect, faithful=False, citations=False: The gold answer says you can keep working full-time while your PGWP is processed if specific conditions are met, but the answer says 'No' and reverses that conclusion. It also relies on a claim that the newer source overrides the older one, which is not stated in the sources.
- **q099** correct, faithful=False, citations=False: La réponse donne bien la bonne période de candidature, conforme au gold answer. En revanche, elle ajoute une affirmation non étayée sur l’ancienneté des sources, donc elle n’est pas entièrement fidèle et ses citations ne sont pas parfaitement correctes.
- **q110** partially_correct, faithful=True, citations=True: It correctly states the travel, visa, and living/subsistence support, but it leaves out that Erasmus Mundus scholarships also cover participation costs. All claims are supported by the sources and the citations are appropriate.
