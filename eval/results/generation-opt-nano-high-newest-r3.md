# Generation evaluation: opt-nano-high-newest-r3

125 questions · answer model `gpt-5.4-nano` (effort high) · judge `gpt-5.4-mini` · 20261025-204723

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **91.2%** |
| Correctness on answerable questions (partial = 0.5) | 90.0% |
| Strictly correct on answerable questions | 87.3% |
| Faithfulness (all claims supported by sources) | 94.3% |
| Citation accuracy | 92.4% |
| "I don't know" on unanswerable questions | 100.0% |
| "I don't know" on answerable questions (false refusals) | 4.5% |
| Correct answers whose gold passage was not retrieved | 8 |
| Cost per question (answer only) | $0.0005 |
| Latency end to end, p50 / p95 | 4.1 s / 7.6 s |
| Tokens per question, in / out | 1346 / 172 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 62.5% |
| cross_lingual | 27 | 79.6% |
| date | 11 | 90.9% |
| fact | 13 | 96.2% |
| list | 3 | 83.3% |
| number | 40 | 96.2% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 100.0% |
| yes_no | 11 | 95.5% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q011** correct, faithful=False, citations=False: La réponse donne bien la date limite demandée, le 11 décembre 2026, ce qui correspond au dossier DAP pour Licence 1. En revanche, la formulation "pour la rentrée 2027" n'est pas directement appuyée par la citation utilisée.
- **q013** incorrect, faithful=False, citations=False: La réponse donne la mauvaise date limite pour le dépôt du dossier hors-DAP. D’après la source, le dossier doit être soumis et payé au plus tard le 18/12/2026, pas le 31/05/2027.
- **q015** partially_correct, faithful=True, citations=False: The answer correctly says cheque payments are not accepted, but it misses the postal-application part that the question asks about. It is otherwise faithful to the source, though the citation on the uncertainty sentence is not appropriate.
- **q021** correct, faithful=False, citations=False: The answer gives the same substantive conclusion as the gold answer: Tunisian students are not automatically exempt from the TCF-DAP, though some specific exemptions exist. However, one factual claim is unsupported by the provided sources, and the first sentence lacks a citation.
- **q027** refused an answerable question. Gold passage retrieved: False
- **q030** correct, faithful=False, citations=True: L’ענה répond bien que la bourse du gouvernement tunisien n’exonère pas de la CVEC, conformément à la source. Une petite partie de la formulation identifie sans source explicite la bourse tunisienne comme une bourse de gouvernement étranger, mais cela ne change pas la réponse.
- **q033** refused an answerable question. Gold passage retrieved: False
- **q043** incorrect, faithful=True, citations=True: La réponse ne donne pas le montant attendu pour le visa étudiant en Allemagne : le gold indique 11 904 EUR par an, soit 992 EUR par mois, alors que la réponse parle de 1 027 EUR/mois et d’un autre cas en Tunisie. Les deux phrases sont bien appuyées par les sources, mais elles ne répondent pas correctement à la question.
- **q044** partially_correct, faithful=True, citations=True: The answer is supported by the sources, but it does not give the actual blocked-account amount asked for. The gold answer says the current student-visa amount is €11,904 per year (€992 per month).
- **q045** incorrect, faithful=True, citations=True: La condition de cours est correcte, mais le financement est incomplet et renvoie à l’ancien montant de 1 027 €/mois au lieu du montant actuel de 11 904 EUR pour une année indiqué dans la source récente. Les citations soutiennent bien les phrases de la réponse.
- **q047** refused an answerable question. Gold passage retrieved: False
- **q050** refused an answerable question. Gold passage retrieved: False
- **q055** correct, faithful=True, citations=False: The answer gives the same application route as the gold answer: through the DAAD scholarship database/portal, with application details there. Its facts are supported by the sources, but one citation is misplaced because the online submission step is only supported by [S2].
- **q062** partially_correct, faithful=True, citations=True: It gives the correct monthly amount for international students (992 EUR), but it also adds the doctoral amount, which is extra and not what the gold answer asks for. All factual claims are supported by the sources and cited correctly.
- **q075** correct, faithful=True, citations=False: The answer gives the correct non-Quebec, single-applicant living-expenses amounts for the two relevant date ranges. The only issue is citation placement: the second sentence’s date range is not supported by the cited source.
- **q086** partially_correct, faithful=False, citations=False: The answer gets the 150-day limit right, but it fails to give the clear answer on work: the correct answer is no, you cannot work during an authorized leave. It also incorrectly claims the sources disagree.
- **q091** correct, faithful=False, citations=False: The answer correctly says you cannot work until your study program begins. However, it adds an unsupported detail about arriving before classes start, and the citation does not fully support that added clause.
- **q092** partially_correct, faithful=True, citations=True: It correctly says a SIN is a 9-digit government-issued number and that students need one to work in Canada. However, it leaves out the condition from the gold answer that the study permit must show the proper work authorization to get a SIN.
- **q105** partially_correct, faithful=True, citations=True: The answer identifies two renewable-energy-related Erasmus Mundus masters correctly, but it misses REM Plus Plus, which the gold answer also includes. The claims it does make are supported by the provided sources and cited appropriately.
