# Generation evaluation: opt-nano-high-r1

125 questions · answer model `gpt-5.4-nano` (effort high) · judge `gpt-5.4-mini` · 20261025-201158

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **91.6%** |
| Correctness on answerable questions (partial = 0.5) | 90.5% |
| Strictly correct on answerable questions | 88.2% |
| Faithfulness (all claims supported by sources) | 94.2% |
| Citation accuracy | 92.3% |
| "I don't know" on unanswerable questions | 100.0% |
| "I don't know" on answerable questions (false refusals) | 5.5% |
| Correct answers whose gold passage was not retrieved | 7 |
| Cost per question (answer only) | $0.0005 |
| Latency end to end, p50 / p95 | 3.8 s / 7.2 s |
| Tokens per question, in / out | 1346 / 187 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 75.0% |
| cross_lingual | 27 | 77.8% |
| date | 11 | 90.9% |
| fact | 13 | 96.2% |
| list | 3 | 83.3% |
| number | 40 | 96.2% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 100.0% |
| yes_no | 11 | 100.0% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q013** incorrect, faithful=False, citations=False: La réponse donne la mauvaise date pour le dépôt hors-DAP : la source indique le 18/12/2026, pas le 31/05/2027. La seconde phrase sur la procédure DAP est correcte mais ne compense pas l’erreur principale.
- **q014** partially_correct, faithful=True, citations=True: La réponse mentionne bien les frais de dossier à 400 DT, mais elle ajoute aussi les frais d’authentification de 150 TND, qui sont un autre coût et brouillent la réponse attendue. Les deux montants sont toutefois bien étayés par les sources et correctement cités.
- **q015** refused an answerable question. Gold passage retrieved: False
- **q027** refused an answerable question. Gold passage retrieved: False
- **q033** refused an answerable question. Gold passage retrieved: False
- **q043** incorrect, faithful=True, citations=True: La réponse donne un montant ancien de 10 236 € (et 10 332 € en TND), alors que la bonne réponse attendue est 11 904 € pour une année d’études, soit 992 € par mois. Les phrases citées sont bien appuyées par les sources, mais elles ne répondent pas correctement à la question.
- **q044** partially_correct, faithful=True, citations=True: The answer is supported by the sources, but it does not give the specific amount the question asks for. It only says the exact amount varies and points to where to check it.
- **q045** partially_correct, faithful=True, citations=True: La réponse donne bien la condition de cours (20 heures/semaine) mais se trompe sur le financement actuel : la page actuelle indique 11 904 EUR pour une année, pas seulement 1 027 €/mois. Les affirmations citées sont toutefois toutes appuyées par les sources.
- **q047** refused an answerable question. Gold passage retrieved: False
- **q050** refused an answerable question. Gold passage retrieved: False
- **q065** correct, faithful=False, citations=False: The deadline given, 1 March, matches the source for non-European applicants. However, the answer adds an unsupported classification of a Tunisian applicant as non-European, which is not stated in the sources.
- **q066** correct, faithful=True, citations=False: The answer gives the key Tunisian-applicant requirements correctly: under 35 and at least B2 German. It also adds general IPS information that is true, but one cited sentence includes dates not supported by the cited source.
- **q070** correct, faithful=True, citations=False: The answer matches the gold answer: you cannot apply directly as an individual and must go through the IAESTE national committee in your home country. It is faithful to the sources, but it lacks citations for its factual statements.
- **q082** correct, faithful=False, citations=False: The answer correctly says that a master's at a public institution does not need a PAL/TAL starting January 1, 2026. However, it adds an unsupported caveat about what the sources do not say, and the citation on that sentence does not directly support it.
- **q091** correct, faithful=True, citations=False: The answer matches the gold answer: you cannot work before your studies begin. All factual claims are supported by the sources, but the response is uncited, so the citation requirement is not met.
- **q093** partially_correct, faithful=False, citations=False: The answer gets the main yes/no points right: Tunisia is eligible and individuals cannot apply directly. However, it adds an incorrect eligibility condition about studying in Canada, which is not supported by the sources and changes the meaning.
- **q096** correct, faithful=False, citations=True: The answer identifies the correct extra document for studying in Quebec: the Quebec Acceptance Certificate (CAQ). It adds one unsupported detail about Quebec’s financial requirements, but that does not change the main answer.
- **q105** partially_correct, faithful=False, citations=False: The answer correctly names REM Plus Plus, EU-CORE, and RESCO, but it also adds DENSYS 2.0, which is not identified in the sources as a renewable-energy master. One listed item is therefore unsupported, and the citations do not fully support the claims.
