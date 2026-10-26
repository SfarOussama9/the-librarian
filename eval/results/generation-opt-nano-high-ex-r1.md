# Generation evaluation: opt-nano-high-ex-r1

125 questions · answer model `gpt-5.4-nano` (effort high) · judge `gpt-5.4-mini` · 20261025-203330

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **88.8%** |
| Correctness on answerable questions (partial = 0.5) | 88.2% |
| Strictly correct on answerable questions | 86.4% |
| Faithfulness (all claims supported by sources) | 94.2% |
| Citation accuracy | 93.3% |
| "I don't know" on unanswerable questions | 93.3% |
| "I don't know" on answerable questions (false refusals) | 5.5% |
| Correct answers whose gold passage was not retrieved | 7 |
| Cost per question (answer only) | $0.0006 |
| Latency end to end, p50 / p95 | 3.9 s / 7.3 s |
| Tokens per question, in / out | 2117 / 177 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 62.5% |
| cross_lingual | 27 | 75.9% |
| date | 11 | 90.9% |
| fact | 13 | 100.0% |
| list | 3 | 83.3% |
| number | 40 | 93.8% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 93.3% |
| yes_no | 11 | 90.9% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q013** incorrect, faithful=False, citations=False: La date donnée est mauvaise : pour les formations hors-DAP, le dossier doit être soumis au plus tard le 18/12/2026. Le 31/05/2027 concerne le choix définitif, pas le dépôt du dossier.
- **q015** refused an answerable question. Gold passage retrieved: False
- **q026** correct, faithful=False, citations=False: The answer gives the correct 2026–2027 Master’s fee for non-EU students: €3,950 per year. However, it adds an extra claim about public universities that is not explicitly supported by the cited source.
- **q027** refused an answerable question. Gold passage retrieved: False
- **q033** refused an answerable question. Gold passage retrieved: False
- **q040** incorrect, faithful=True, citations=True: La réponse donne 15 224 pour la France, alors que la question demande les effectifs de mobilité et la fiche indique 10 068 pour la France. Le chiffre pour l’Allemagne est correct, mais la réponse ne correspond pas à la question.
- **q043** incorrect, faithful=True, citations=True: La réponse ne donne pas le montant attendu pour le visa étudiant : la source de référence indique 11 904 EUR par an, soit 992 EUR par mois. Les montants avancés (10 236/10 332 EUR et 1 027 EUR/mois) sont tirés des sources mais ne répondent pas correctement à la question.
- **q044** incorrect, faithful=True, citations=True: The answer does not give the actual amount requested, which the gold answer says is €11,904 per year (€992 per month). Its factual claims are supported by the sources, but it fails to answer the question as asked.
- **q045** partially_correct, faithful=True, citations=True: La réponse donne bien les conditions actuelles du cours (au moins 20 h/semaine) et le financement annuel de 11 904 EUR. Elle ajoute toutefois le montant de 1 027 €/mois du compte bloqué, qui provient d’un ancien document et n’est pas présenté comme obsolète.
- **q047** refused an answerable question. Gold passage retrieved: False
- **q050** refused an answerable question. Gold passage retrieved: False
- **q062** partially_correct, faithful=True, citations=True: It correctly gives the monthly amount for international students as 992 EUR. It also adds the doctoral amount, which is supported by the sources but is extra beyond what the question asks.
- **q075** correct, faithful=False, citations=False: The answer gives the correct living-expense amounts for someone coming alone outside Quebec. However, the “before September 1, 2026” claim is not directly stated in the cited source, so the citation is not fully supported.
- **q086** incorrect, faithful=False, citations=False: The gold answer says you cannot work during an authorized leave and that the leave can be at most 150 days. The response muddles the main answer by claiming a contradiction and adding an unsupported statement about being allowed to work.
- **q087** partially_correct, faithful=False, citations=False: La réponse est globalement dans le bon sens, mais elle ne répond pas directement à la question sur le changement d’établissement et déplace à tort la règle du 22 janvier 2025 vers le changement de niveau. Elle contient aussi une citation incorrecte sur ce point.
- **q090** correct, faithful=True, citations=False: The answer correctly says that post-secondary international students in Canada do not need a co-op work permit for internships as of April 1, 2026. It adds an extra statement about secondary students that is supported by the sources, but the citation attached to that sentence is not the right one.
- **q105** partially_correct, faithful=False, citations=False: The answer names two relevant Erasmus Mundus masters correctly, but it omits REM Plus Plus from the gold answer and makes an unsupported exhaustive-sounding claim in the intro. The listed items themselves are supported by the sources.
- **u003** answered an unanswerable question: The Erasmus+ catalogue page provided for EU-CORE does not give a specific single date, but it states that **most** master’s programmes require applica
