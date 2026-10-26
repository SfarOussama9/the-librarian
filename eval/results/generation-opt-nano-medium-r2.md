# Generation evaluation: opt-nano-medium-r2

125 questions · answer model `gpt-5.4-nano` (effort medium) · judge `gpt-5.4-mini` · 20261025-201122

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **88.4%** |
| Correctness on answerable questions (partial = 0.5) | 86.8% |
| Strictly correct on answerable questions | 85.5% |
| Faithfulness (all claims supported by sources) | 93.3% |
| Citation accuracy | 91.3% |
| "I don't know" on unanswerable questions | 100.0% |
| "I don't know" on answerable questions (false refusals) | 5.5% |
| Correct answers whose gold passage was not retrieved | 8 |
| Cost per question (answer only) | $0.0004 |
| Latency end to end, p50 / p95 | 3.6 s / 6.8 s |
| Tokens per question, in / out | 1346 / 124 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 62.5% |
| cross_lingual | 27 | 74.1% |
| date | 11 | 86.4% |
| fact | 13 | 92.3% |
| list | 3 | 100.0% |
| number | 40 | 96.2% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 100.0% |
| yes_no | 11 | 81.8% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q009** partially_correct, faithful=False, citations=False: La durée du BUT est correcte, mais la réponse ne donne pas la fenêtre exacte de candidature demandée. Elle remplace cette information par une formulation générale sur le calendrier, ce qui la rend incomplète.
- **q013** incorrect, faithful=False, citations=False: La réponse donne la mauvaise date : pour le hors-DAP, la date limite de dépôt du dossier est le 18/12/2026, pas le 31/05/2027. La citation [S1] contient bien le 31/05/2027, mais pour le choix définitif, pas pour le dépôt du dossier.
- **q015** refused an answerable question. Gold passage retrieved: False
- **q018** correct, faithful=True, citations=False: The answer matches the gold answer: certified photocopies are not accepted, and originals are required. The content is supported by the sources, but the first sentence is uncited.
- **q027** refused an answerable question. Gold passage retrieved: False
- **q030** incorrect, faithful=False, citations=False: La question demande si une bourse du gouvernement tunisien exonère de la CVEC ; la bonne réponse est non. La réponse donnée dit d’abord oui, ce qui contredit la source et le gold answer.
- **q033** refused an answerable question. Gold passage retrieved: False
- **q038** correct, faithful=False, citations=True: The answer matches the gold answer: students in the Campus France procedure must book the TLScontact appointment through Campus France, and since 18 July 2023 they also need the France-Visas form. One phrasing choice is slightly unsupported, but it does not change the substance.
- **q043** incorrect, faithful=True, citations=True: La réponse donne le mauvais montant par rapport à la référence attendue : elle indique 10.236 € alors que la bonne réponse est 11.904 € pour une année d’études (992 € par mois). La citation renvoie bien à une source qui mentionne ce montant, donc le problème est la justesse de la réponse, pas la citation.
- **q044** partially_correct, faithful=True, citations=True: The answer is faithful to the source, but it does not give the actual amount needed for the German blocked account, which is what the question asks. It only explains where to find the amount.
- **q045** incorrect, faithful=True, citations=True: La réponse donne bien la condition de cours, mais elle se trompe sur le financement demandé par la page actuelle : le gold attend 11 904 EUR pour une année, pas seulement 1 027 €/mois d’après l’ancien PDF. Les citations utilisées soutiennent les affirmations, mais elles ne correspondent pas à la réponse attendue.
- **q047** refused an answerable question. Gold passage retrieved: False
- **q048** incorrect, faithful=False, citations=False: La réponse donnée ne reprend pas la règle demandée par la question/gold answer: pour des études universitaires avant immatriculation, il faut une assurance privée pour 90 jours à compter de l’arrivée. Elle affirme à la place une couverture jusqu’à la validité du visa, ce qui correspond plutôt au cas du cours de langue préparatoire.
- **q050** refused an answerable question. Gold passage retrieved: False
- **q062** partially_correct, faithful=True, citations=True: The answer gives the correct monthly amount for international students, 992 EUR, which matches the expected answer. However, it also adds the doctoral scholarship amount (1,500 EUR), which is not what the question is asking for.
- **q065** correct, faithful=False, citations=False: The answer gives the correct deadline, 1 March, for the relevant applicant category. However, it adds an unsupported parenthetical claim about Tunisia, which is not stated in the provided sources.
- **q075** correct, faithful=False, citations=False: The answer gives the correct living-expense amounts for a single applicant outside Quebec. However, it adds a date-range claim to the first sentence that is not fully supported by the cited source excerpt, so the answer is not fully faithful/citation-correct.
- **q082** incorrect, faithful=True, citations=True: The answer contains the correct rule that master’s students at a public institution starting January 1, 2026 do not need a PAL/TAL, but it begins with the opposite “Yes,” which contradicts the gold answer and the question. Its factual statements are supported by the provided sources.
- **q086** correct, faithful=True, citations=False: The answer matches the gold answer: you cannot work during an authorized leave, and the leave can be at most 150 days. The factual content is supported by the sources, though the citation on the second sentence includes an unnecessary/unsupported [S1].
- **q090** incorrect, faithful=True, citations=True: The answer starts with the wrong yes/no response (“Yes”), even though the rest of it states the correct fact that post-secondary international students do not need a co-op work permit. The cited sources support the substantive explanation.
- **q091** correct, faithful=True, citations=False: The answer matches the gold answer: you cannot work until you begin your studies in Canada. It is also factually supported by the sources, though the citation should include [S1] for the arrival-before-classes nuance.
