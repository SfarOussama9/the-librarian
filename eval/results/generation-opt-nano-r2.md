# Generation evaluation: opt-nano-r2

125 questions · answer model `gpt-5.4-nano` · judge `gpt-5.4-mini` · 20261025-195403

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **86.8%** |
| Correctness on answerable questions (partial = 0.5) | 85.0% |
| Strictly correct on answerable questions | 80.9% |
| Faithfulness (all claims supported by sources) | 94.2% |
| Citation accuracy | 91.3% |
| "I don't know" on unanswerable questions | 100.0% |
| "I don't know" on answerable questions (false refusals) | 5.5% |
| Correct answers whose gold passage was not retrieved | 6 |
| Cost per question (answer only) | $0.0004 |
| Latency end to end, p50 / p95 | 3.9 s / 7.7 s |
| Tokens per question, in / out | 1346 / 85 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 50.0% |
| cross_lingual | 27 | 72.2% |
| date | 11 | 81.8% |
| fact | 13 | 92.3% |
| list | 3 | 83.3% |
| number | 40 | 92.5% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 100.0% |
| yes_no | 11 | 95.5% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q009** refused an answerable question. Gold passage retrieved: True
- **q013** incorrect, faithful=False, citations=False: La date donnée est fausse : pour le hors-DAP, la source indique un dépôt du dossier jusqu’au 18/12/2026, pas au 31/05/2027. La réponse confond la date limite de choix définitif avec celle du dépôt.
- **q014** incorrect, faithful=True, citations=True: La réponse donne 150 TND pour les frais d’authentification, alors que la question porte sur les frais de dossier Campus France en Tunisie, qui sont de 400 DT depuis le 1er août 2025. La citation est correcte pour le montant mentionné, mais la réponse ne répond pas à la bonne question.
- **q015** partially_correct, faithful=False, citations=False: It correctly says cheque payments are not accepted, but it fails to answer whether applications can be sent by post. It also overstates what the source says by claiming that only online payment methods are accepted.
- **q027** refused an answerable question. Gold passage retrieved: False
- **q030** incorrect, faithful=False, citations=False: La bonne réponse est non : une bourse du gouvernement tunisien ne donne pas droit à l’exonération de la CVEC. L’assistant affirme l’inverse et mélange des catégories de bourses qui ne répondent pas correctement à la question.
- **q033** refused an answerable question. Gold passage retrieved: False
- **q039** partially_correct, faithful=True, citations=True: L回答 donne correctement la durée de validité indiquée dans les sources, mais il omet la précision de la réponse de référence selon laquelle, au-delà de cette durée, il faut demander un titre de séjour en préfecture. La citation fournie soutient bien l’énoncé.
- **q043** incorrect, faithful=True, citations=True: La réponse donne 10 236 € alors que l’attendu est 11 904 € pour une année d’études. La seule affirmation chiffrée est bien appuyée par la source citée, mais elle ne répond pas correctement à la question.
- **q044** incorrect, faithful=False, citations=False: The answer avoids giving the required blocked-account amount and instead gives only a general description. It also makes a specific student-visa claim that is not supported by the sources.
- **q045** incorrect, faithful=True, citations=True: La réponse donne bien la condition de cours et le montant actuel de financement, mais elle ajoute aussi le montant de 1027 €/mois du PDF de 2022 alors que la source actuelle indique que ce montant est dépassé. Toutes les affirmations sont néanmoins appuyées par les sources citées.
- **q047** refused an answerable question. Gold passage retrieved: False
- **q050** refused an answerable question. Gold passage retrieved: False
- **q053** correct, faithful=True, citations=False: The answer matches the gold answer: the Federal Foreign Office does not recommend a specific blocked account provider and says its old provider list was not a recommendation. The content is supported by the sources, but the citation placement is incomplete.
- **q054** partially_correct, faithful=True, citations=True: La réponse donne correctement le public visé par l’annonce DAAD Tunis et décrit bien le programme. Elle omet toutefois l’autre formulation plus large de la fiche DAAD (master ou diplôme d’ingénieur/informatique dans un établissement tunisien public ou reconnu), donc elle ne couvre pas complètement la question.
- **q062** partially_correct, faithful=True, citations=True: It correctly gives the 992 EUR monthly amount and cites the source for the doctoral amount as well, but it misses the health insurance funding and repayment detail from the gold answer. The extra doctoral figure is supported by the sources, but it goes beyond what the question’s expected answer asks for.
- **q070** correct, faithful=True, citations=False: The answer correctly says you cannot apply directly as an individual and must go through the IAESTE national committee. It does not contradict the sources, though the citation placement is slightly imperfect.
- **q086** partially_correct, faithful=False, citations=False: The answer gets the 150-day limit right and does say you can't work during an authorized leave, but it also adds a contradictory unsupported statement implying you can work if conditions are met. That makes it only partially correct and not fully faithful to the sources.
- **q087** partially_correct, faithful=False, citations=False: La réponse dit bien qu’il faut généralement une nouvelle attestation, mais elle ajoute une exception mal formulée et confond CAQ et PAL/TAL. Elle ne reprend pas correctement la règle générale datée du 22 janvier 2025.
- **q092** partially_correct, faithful=True, citations=True: The answer correctly defines a SIN and correctly says you need one to work in Canada as a student. It leaves out the study-permit condition for getting a SIN, so it is slightly incomplete compared with the gold answer.
- **q102** partially_correct, faithful=True, citations=True: The answer correctly says you can apply in your last year of licence, but it omits the condition that you must graduate before the master starts. The cited source supports the statement made.
- **q104** correct, faithful=True, citations=False: La réponse correspond à l’oracle : il existe bien un programme Erasmus Mundus appelé « Data Engineering and Artificial Intelligence » (DEAI). En revanche, la citation n’est pas placée sur la première phrase factuelle (« Oui. »).
- **q110** partially_correct, faithful=True, citations=True: The answer gives the main covered items (travel, visa, and living/subsistence costs) and is supported by the sources, but it omits the participation costs that the question asks for. The citations are attached to supported factual statements.
