# Generation evaluation: opt-nano-high-ex-r2

125 questions · answer model `gpt-5.4-nano` (effort high) · judge `gpt-5.4-mini` · 20261025-203401

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **90.8%** |
| Correctness on answerable questions (partial = 0.5) | 89.5% |
| Strictly correct on answerable questions | 87.3% |
| Faithfulness (all claims supported by sources) | 95.2% |
| Citation accuracy | 91.3% |
| "I don't know" on unanswerable questions | 100.0% |
| "I don't know" on answerable questions (false refusals) | 5.5% |
| Correct answers whose gold passage was not retrieved | 7 |
| Cost per question (answer only) | $0.0004 |
| Latency end to end, p50 / p95 | 4.1 s / 8.4 s |
| Tokens per question, in / out | 2117 / 204 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 50.0% |
| cross_lingual | 27 | 75.9% |
| date | 11 | 86.4% |
| fact | 13 | 100.0% |
| list | 3 | 83.3% |
| number | 40 | 98.8% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 100.0% |
| yes_no | 11 | 95.5% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q009** correct, faithful=True, citations=False: L პასუხը donne bien les deux informations demandées : le BUT dure 3 ans et la candidature est ouverte du 1er octobre 2026 au 18 décembre 2026. La réponse est fidèle aux sources, mais la citation de la deuxième phrase n’appuie pas aussi clairement la mention de la rentrée 2027.
- **q013** incorrect, faithful=False, citations=False: La réponse donne la mauvaise date limite pour le dépôt hors-DAP : c’est le 18/12/2026, pas le 31/05/2027. Elle ajoute en plus une information sur la DAP, non demandée par la question.
- **q015** refused an answerable question. Gold passage retrieved: False
- **q027** refused an answerable question. Gold passage retrieved: False
- **q033** incorrect, faithful=False, citations=False: La réponse inverse la bonne information : la bourse Eiffel se candidate via les établissements français d’enseignement supérieur, pas en candidature directe par le postulant. La citation utilisée ne prouve pas cette conclusion.
- **q044** refused an answerable question. Gold passage retrieved: False
- **q045** incorrect, faithful=True, citations=True: L’answer donne bien la règle des 20 heures/semaine et le financement de 11.904 EUR, mais elle présente aussi 1.027 €/mois comme condition actuelle alors que la source actuelle indique que ce montant est dépassé. Toutes les phrases factuelles sont correctement citées et soutenues par les sources.
- **q047** refused an answerable question. Gold passage retrieved: False
- **q050** refused an answerable question. Gold passage retrieved: False
- **q062** partially_correct, faithful=True, citations=True: It gives the correct monthly amount for international students (992 EUR), but it also adds the doctoral amount, which the question did not ask for. All factual claims are supported by the sources and the citations are appropriate.
- **q065** partially_correct, faithful=True, citations=True: The answer gives the scholarship deadline range correctly, but it does not directly resolve the Tunisian applicant’s deadline as 1 March (non-EU/non-European), which is what the question asks. All factual claims made are supported by the sources and the citations are placed appropriately.
- **q072** correct, faithful=True, citations=False: The answer matches the gold answer: DAAD Doctoral Programmes can fund research phases outside Germany if they are critical, and these visits must not exceed one quarter of the funding period. However, the earlier factual claims are not cited directly, so the citation formatting is not fully correct.
- **q075** correct, faithful=False, citations=False: The answer gives the correct living-expenses amounts for a single applicant outside Quebec. However, one citation is incomplete because the date range attached to the $22,895 amount is not supported by the cited source alone.
- **q086** partially_correct, faithful=False, citations=False: The answer ultimately gives the right bottom line that you cannot work during an authorized leave and that the leave can be up to 150 days, but it includes a contradictory and unsupported statement about being allowed to work. The citation on that statement is also wrong.
- **q087** partially_correct, faithful=True, citations=True: The answer is supported by the sources, but it does not directly answer the question with the main rule: changing schools in Canada generally requires a new PAL/TAL. It instead discusses related cases (in-progress applications, extensions, status restoration) and omits the key 22 January 2025 rule.
- **q092** correct, faithful=True, citations=False: The answer correctly defines a SIN and answers yes to the student-work question, matching the gold answer. It is faithful to the sources, but it lacks citations for its factual claims.
- **q103** correct, faithful=True, citations=False: The answer correctly says that Erasmus Mundus offers cybersecurity-related master programmes and gives valid examples consistent with the sources. The only issue is citation formatting/support for the standalone yes and the mixed citation on the CYBER example.
- **q105** partially_correct, faithful=False, citations=False: The answer includes the gold examples EU-CORE, RESCO, and REM Plus Plus, so it is broadly on topic. However, it also adds DENSYS 2.0 as renewable-energy related without source support, and the opening sentence lacks a citation.
