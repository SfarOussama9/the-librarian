# Generation evaluation: opt-nano-high-r2

125 questions · answer model `gpt-5.4-nano` (effort high) · judge `gpt-5.4-mini` · 20261025-202035

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **91.2%** |
| Correctness on answerable questions (partial = 0.5) | 90.0% |
| Strictly correct on answerable questions | 88.2% |
| Faithfulness (all claims supported by sources) | 95.2% |
| Citation accuracy | 94.2% |
| "I don't know" on unanswerable questions | 100.0% |
| "I don't know" on answerable questions (false refusals) | 5.5% |
| Correct answers whose gold passage was not retrieved | 7 |
| Cost per question (answer only) | $0.0005 |
| Latency end to end, p50 / p95 | 3.9 s / 7.7 s |
| Tokens per question, in / out | 1346 / 170 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 62.5% |
| cross_lingual | 27 | 77.8% |
| date | 11 | 90.9% |
| fact | 13 | 100.0% |
| list | 3 | 100.0% |
| number | 40 | 93.8% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 100.0% |
| yes_no | 11 | 100.0% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q012** partially_correct, faithful=True, citations=True: L’ענה donne bien la date actuelle correcte, le 11 décembre 2026, mais ajoute aussi l’ancienne date du 31 janvier sans préciser clairement qu’elle n’est plus la référence. Les citations soutiennent les deux phrases.
- **q013** incorrect, faithful=True, citations=True: La réponse donne la mauvaise échéance pour le dépôt du dossier : elle indique le 31/05/2027, alors que pour la procédure hors-DAP la date limite de soumission et de paiement est le 18/12/2026. La citation appuie bien la date mentionnée, mais elle ne répond pas correctement à la question.
- **q015** refused an answerable question. Gold passage retrieved: False
- **q026** correct, faithful=False, citations=False: The answer gives the correct 2026–2027 Master's tuition fee for a non-EU student: €3,950 per year. However, it adds an unsupported claim about public universities, so it is not fully faithful to the sources.
- **q027** refused an answerable question. Gold passage retrieved: False
- **q030** correct, faithful=False, citations=False: L’ענה répond bien que non, la CVEC n’est pas exonérée. En revanche, la justification reliant explicitement la bourse tunisienne à une bourse d’un gouvernement étranger n’est pas directement étayée par la source citée.
- **q033** refused an answerable question. Gold passage retrieved: False
- **q039** partially_correct, faithful=True, citations=True: L’ענה donne bien la durée de validité demandée : entre 3 mois et 1 an. En revanche, il ne mentionne pas la condition indiquée dans la réponse de référence selon laquelle il faut ensuite demander un titre de séjour au-delà de cette durée.
- **q040** incorrect, faithful=True, citations=True: L’answer donne 15 224 pour la France, alors que la fiche mobilité indique 10 068 étudiants tunisiens en France et 7 062 en Allemagne. Les citations utilisées soutiennent bien les nombres cités, mais la réponse ne correspond pas à la question.
- **q043** incorrect, faithful=False, citations=False: La réponse donne des montants différents de l’énoncé de référence : 1.027 € par mois et 10.236 €, alors que la bonne réponse est 11.904 € par an, soit 992 € par mois. Elle ne répond donc pas correctement à la question.
- **q044** partially_correct, faithful=True, citations=True: The answer is supported by the sources, but it does not give the specific amount the question asks for. The gold answer expects the current student visa blocked-account amount (€11,904 per year / €992 per month), not just that it varies.
- **q045** partially_correct, faithful=True, citations=True: L’ענה donne bien les conditions actuelles de cours (20 h/semaine) et de financement (11 904 EUR/an), mais ajoute aussi une ancienne exigence de 18 h/semaine sans préciser qu’elle est dépassée, ce qui le rend seulement partiellement correct par rapport à la réponse attendue.
- **q047** refused an answerable question. Gold passage retrieved: False
- **q050** refused an answerable question. Gold passage retrieved: False
- **q070** correct, faithful=True, citations=False: The answer matches the gold answer: you cannot apply directly as an individual and must go through the IAESTE national committee in your home country. All factual claims are supported by the sources, but the citation formatting is incomplete because the first factual sentence lacks an explicit citation.
- **q075** correct, faithful=False, citations=False: The answer gives the right living-expense amounts for one person outside Quebec, matching the gold answer. However, one date condition is not directly supported by the cited source, and the citation for that sentence is therefore not correct.
- **q098** correct, faithful=False, citations=False: The answer gives the correct duration and ECTS credits for an Erasmus Mundus Joint Master. However, it adds an unsupported detail about programme structure, so it is not fully faithful.
