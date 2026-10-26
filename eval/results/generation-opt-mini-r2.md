# Generation evaluation: opt-mini-r2

125 questions · answer model `gpt-5.4-mini` · judge `gpt-5.4-mini` · 20261025-195419

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **92.0%** |
| Correctness on answerable questions (partial = 0.5) | 90.9% |
| Strictly correct on answerable questions | 90.0% |
| Faithfulness (all claims supported by sources) | 97.1% |
| Citation accuracy | 98.1% |
| "I don't know" on unanswerable questions | 100.0% |
| "I don't know" on answerable questions (false refusals) | 6.4% |
| Correct answers whose gold passage was not retrieved | 6 |
| Cost per question (answer only) | $0.0015 |
| Latency end to end, p50 / p95 | 4.3 s / 8.3 s |
| Tokens per question, in / out | 1346 / 119 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 25.0% |
| cross_lingual | 27 | 75.9% |
| date | 11 | 100.0% |
| fact | 13 | 100.0% |
| list | 3 | 100.0% |
| number | 40 | 98.8% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 100.0% |
| yes_no | 11 | 100.0% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q012** incorrect, faithful=True, citations=True: La réponse donne comme date limite principale le 31 janvier, alors que la référence actuelle indiquée dans les sources est le 11 décembre 2026. Elle mentionne bien aussi le 11 décembre 2026, mais seulement comme condition liée à d’autres formations Hors-DAP, ce qui ne répond pas correctement à la question.
- **q015** refused an answerable question. Gold passage retrieved: False
- **q027** refused an answerable question. Gold passage retrieved: False
- **q033** refused an answerable question. Gold passage retrieved: False
- **q044** refused an answerable question. Gold passage retrieved: False
- **q045** incorrect, faithful=True, citations=True: La condition de cours est correcte, mais la réponse donne pour le financement le montant ancien de 1 027 €/mois au lieu du montant actuel de 11 904 € pour une année. Elle ne répond donc pas correctement à la question telle qu’elle est posée.
- **q047** refused an answerable question. Gold passage retrieved: False
- **q050** refused an answerable question. Gold passage retrieved: False
- **q062** partially_correct, faithful=True, citations=True: It gives the correct monthly amount for international students (992 EUR), but it also adds the doctoral amount, which the question did not ask for, and it omits the health insurance coverage mentioned in the gold answer. All cited factual claims are supported by the sources.
- **q065** correct, faithful=False, citations=True: The answer gives the correct deadline of 1 March, matching the sources. However, it also implicitly assumes a Tunisian applicant is in the non-European category, which is not explicitly stated in the provided sources.
- **q075** correct, faithful=False, citations=False: The answer gives the correct living-expenses amounts for a single applicant outside Quebec. However, one factual claim is not fully supported by the cited source, because the date range for the older amount is missing the needed citation.
- **q082** correct, faithful=False, citations=False: The answer gives the same substantive answer as the gold answer: no PAL/TAL is needed for a master’s degree-granting program at a public institution starting January 1, 2026. However, it adds an unsupported remark about what the sources say, so it is not fully faithful and the citation on that remark is not supported.
- **q087** partially_correct, faithful=True, citations=True: L’ענה dit bien que oui, il faut une nouvelle PAL/TAL depuis le 22 janvier 2025 quand on change d’établissement, ce qui est conforme aux sources. En revanche, il omet l’exception mentionnée dans la réponse de référence, donc la réponse est un peu incomplète.
