# Generation evaluation: opt-nano-medium-r1

125 questions · answer model `gpt-5.4-nano` (effort medium) · judge `gpt-5.4-mini` · 20261025-201123

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **88.0%** |
| Correctness on answerable questions (partial = 0.5) | 87.3% |
| Strictly correct on answerable questions | 84.5% |
| Faithfulness (all claims supported by sources) | 96.1% |
| Citation accuracy | 93.2% |
| "I don't know" on unanswerable questions | 93.3% |
| "I don't know" on answerable questions (false refusals) | 6.4% |
| Correct answers whose gold passage was not retrieved | 7 |
| Cost per question (answer only) | $0.0004 |
| Latency end to end, p50 / p95 | 3.7 s / 6.8 s |
| Tokens per question, in / out | 1346 / 136 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 25.0% |
| cross_lingual | 27 | 79.6% |
| date | 11 | 86.4% |
| fact | 13 | 100.0% |
| list | 3 | 100.0% |
| number | 40 | 92.5% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 93.3% |
| yes_no | 11 | 90.9% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q013** incorrect, faithful=False, citations=False: La bonne date limite pour soumettre le dossier hors-DAP est le 18/12/2026, pas le 31/05/2027. L’answer se trompe sur l’étape concernée et donne donc une réponse incorrecte.
- **q014** partially_correct, faithful=True, citations=True: L’answer contient bien le bon montant des frais de dossier Campus France en Tunisie : 400 DT. En revanche, elle ajoute aussi un montant différent (150 TND) qui concerne les frais d’authentification, et elle ne précise pas la date d’application indiquée dans la réponse de référence.
- **q015** partially_correct, faithful=True, citations=True: The answer correctly says cheque payments are not accepted, but it fails to answer the postal question with the correct no. The sources support the payment claim and the citations are attached appropriately.
- **q027** refused an answerable question. Gold passage retrieved: False
- **q033** refused an answerable question. Gold passage retrieved: False
- **q039** partially_correct, faithful=True, citations=True: La réponse donne bien la durée de validité du visa de long séjour : entre 3 mois et 1 an. En revanche, elle omet la précision importante selon laquelle au-delà de cette durée il faut demander un titre de séjour en préfecture.
- **q043** incorrect, faithful=False, citations=False: La réponse donne un montant erroné et ne correspond pas à la valeur attendue. En plus, la citation utilisée ne soutient pas le chiffre avancé.
- **q044** refused an answerable question. Gold passage retrieved: False
- **q045** incorrect, faithful=True, citations=True: La réponse donne bien la condition de cours à 20 heures/semaine, mais elle manque la condition de financement actuelle indiquée par la source de 2025 : 11 904 EUR pour une année. Elle reprend à la place l’ancien montant mensuel de 1 027 €/mois, qui est dépassé selon le gold answer.
- **q047** refused an answerable question. Gold passage retrieved: False
- **q050** refused an answerable question. Gold passage retrieved: False
- **q053** correct, faithful=True, citations=False: The answer matches the gold answer: the Federal Foreign Office does not recommend a specific blocked account provider and its old provider list was deleted. All factual claims are supported by the sources, but the first sentence lacks an inline citation.
- **q062** partially_correct, faithful=True, citations=True: The answer gives the monthly amount for international students correctly, but it also adds the doctoral-student amount instead of answering only the single amount the question asks for. All factual claims are supported by the sources and the citations are placed correctly.
- **q065** partially_correct, faithful=True, citations=True: The answer gives the relevant deadline options, but it does not directly answer the question for a Tunisian applicant as the gold answer does (1 March for non-EU applicants). It is otherwise supported by the sources.
- **q066** correct, faithful=True, citations=False: The answer gives the same age and German-language requirements as the gold answer: under 35 and at least B2 German. It is factually supported, but the first sentence should have cited the source that explicitly includes Tunisia.
- **q074** correct, faithful=True, citations=False: The answer correctly says KAAD can fund German language courses, matching the gold answer. All substantive content is supported by S1, but the initial uncited "Yes." sentence makes the citation handling imperfect.
- **q075** incorrect, faithful=False, citations=False: The answer gives the right amounts, but it गलतely states the 22,895 amount applies starting January 1, 2024 instead of January 1, 2025. That wrong condition makes the answer incorrect.
- **q086** refused an answerable question. Gold passage retrieved: True
- **q097** partially_correct, faithful=True, citations=True: The answer correctly states that the Canadian school/DLI can take up to 10 calendar days to confirm the LOA. It omits the follow-up point that IRCC aims to process the application within 2 weeks after verification.
- **q105** correct, faithful=False, citations=False: The answer names the key masters from the gold answer and is therefore correct for the question. However, it adds an unsupported renewable-energy claim for DENSYS 2.0 and leaves the introductory sentence uncited.
- **u003** answered an unanswerable question: The sources you provided don’t give an exact application deadline for the EU-CORE Erasmus Mundus master specifically. They only state that **most mast
