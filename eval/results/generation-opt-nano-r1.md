# Generation evaluation: opt-nano-r1

125 questions · answer model `gpt-5.4-nano` · judge `gpt-5.4-mini` · 20261025-195255

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **86.8%** |
| Correctness on answerable questions (partial = 0.5) | 85.9% |
| Strictly correct on answerable questions | 84.5% |
| Faithfulness (all claims supported by sources) | 96.1% |
| Citation accuracy | 95.1% |
| "I don't know" on unanswerable questions | 93.3% |
| "I don't know" on answerable questions (false refusals) | 6.4% |
| Correct answers whose gold passage was not retrieved | 7 |
| Cost per question (answer only) | $0.0004 |
| Latency end to end, p50 / p95 | 3.8 s / 7.1 s |
| Tokens per question, in / out | 1346 / 84 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 50.0% |
| cross_lingual | 27 | 75.9% |
| date | 11 | 90.9% |
| fact | 13 | 88.5% |
| list | 3 | 83.3% |
| number | 40 | 92.5% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 93.3% |
| yes_no | 11 | 90.9% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q013** incorrect, faithful=False, citations=False: La date donnée est fausse : pour la procédure hors-DAP, la date limite de soumission du dossier est le 18/12/2026, pas le 30/04/2027. La réponse confond avec la date des réponses des établissements.
- **q014** incorrect, faithful=True, citations=True: La réponse donne 150 TND, qui correspond aux frais d’authentification, alors que la question demande les frais de dossier Campus France en Tunisie. Le bon montant attendu est 400 DT depuis le 1er août 2025.
- **q015** partially_correct, faithful=True, citations=True: The answer correctly says cheque payment is not accepted, but it does not address the postal-application part of the question. Its factual claim about Campus France Tunisie not accepting cash or cheque is supported by the source.
- **q021** correct, faithful=False, citations=False: The answer correctly says Tunisian students are not exempt from the TCF-DAP on the basis of French being widely spoken. However, it adds an unsupported claim about French's widespread use in Tunisia that is not stated in the provided sources.
- **q027** refused an answerable question. Gold passage retrieved: False
- **q030** refused an answerable question. Gold passage retrieved: True
- **q033** refused an answerable question. Gold passage retrieved: False
- **q040** incorrect, faithful=True, citations=True: La réponse donne 15 224 pour la France, alors que la question demande le chiffre de la fiche mobilité pour les étudiants tunisiens en France et en Allemagne, soit 10 068 en France et 7 062 en Allemagne. Les citations soutiennent les nombres mentionnés, mais pas la réponse attendue à la question.
- **q042** correct, faithful=True, citations=False: The answer gives the same password-reset steps as the source and answers the question correctly. However, it is not properly cited because no [S#] citations are included for any factual claim.
- **q043** incorrect, faithful=True, citations=True: La réponse donne 10 236 € au lieu des 11 904 € attendus pour une année d’études. Elle est bien appuyée par la source citée, mais elle ne répond pas correctement à la question posée.
- **q044** refused an answerable question. Gold passage retrieved: False
- **q045** incorrect, faithful=True, citations=True: L’ענה répond partiellement sur les heures de cours, mais il donne un montant de financement obsolète de 1.027 €/mois au lieu du montant actuel de 11.904 € pour une année. Il manque donc l’information clé demandée sur le financement.
- **q047** refused an answerable question. Gold passage retrieved: False
- **q048** partially_correct, faithful=True, citations=True: L’answer dit correctement qu’avant l’immatriculation il faut une assurance maladie privée, mais elle ne donne pas la durée correcte demandée pour des études universitaires (90 jours). Elle ajoute à la place la règle du cours de langue préparatoire, qui n’est pas la réponse principale à la question.
- **q050** refused an answerable question. Gold passage retrieved: False
- **q086** incorrect, faithful=False, citations=False: The answer gives the opposite of the correct rule about working during an authorized leave. It is right that the leave must be authorized and no longer than 150 days, but the work-permission claim is wrong.
- **q100** incorrect, faithful=True, citations=True: The answer gives the wrong destination first: the question asks where students send an Erasmus Mundus Joint Master application, and the correct answer is directly to the institution/consortium running the chosen programme. It also adds an agency application route that applies to the action call, not the student application.
- **q105** partially_correct, faithful=False, citations=False: The answer includes the three masters named in the gold answer, but it also adds DENSYS 2.0 as a renewable-energy master without source support. So it is mostly right, but not fully faithful.
- **u003** answered an unanswerable question: Most master’s programmes require applications to be submitted between October and January for courses commencing the following academic year, so the E
