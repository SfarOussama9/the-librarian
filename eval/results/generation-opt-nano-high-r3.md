# Generation evaluation: opt-nano-high-r3

125 questions · answer model `gpt-5.4-nano` (effort high) · judge `gpt-5.4-mini` · 20261025-202039

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **90.0%** |
| Correctness on answerable questions (partial = 0.5) | 88.6% |
| Strictly correct on answerable questions | 85.5% |
| Faithfulness (all claims supported by sources) | 95.2% |
| Citation accuracy | 87.6% |
| "I don't know" on unanswerable questions | 100.0% |
| "I don't know" on answerable questions (false refusals) | 4.5% |
| Correct answers whose gold passage was not retrieved | 6 |
| Cost per question (answer only) | $0.0005 |
| Latency end to end, p50 / p95 | 3.8 s / 7.3 s |
| Tokens per question, in / out | 1346 / 172 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 62.5% |
| cross_lingual | 27 | 77.8% |
| date | 11 | 90.9% |
| fact | 13 | 96.2% |
| list | 3 | 83.3% |
| number | 40 | 95.0% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 100.0% |
| yes_no | 11 | 90.9% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q009** correct, faithful=True, citations=False: La réponse donne bien la durée du BUT et la période de candidature demandées, conformément au gold. En revanche, l’une des citations associées à la deuxième phrase n’est pas pertinente/suffisante pour soutenir cette affirmation.
- **q012** partially_correct, faithful=True, citations=True: L’ענה donne bien la date limite actuelle du calendrier officiel 2026/2027 : le 11/12/2026. Mais il ajoute aussi le 31 janvier comme limite générale, ce qui peut prêter à confusion alors que la question demande une seule date limite.
- **q013** incorrect, faithful=False, citations=False: La réponse donne la mauvaise échéance pour déposer le dossier hors-DAP. D’après la source, la date limite de soumission est le 18/12/2026, pas le 31/05/2027.
- **q014** partially_correct, faithful=True, citations=True: La réponse donne bien le montant de 400 DT pour les frais de dossier, mais elle ajoute aussi 150 TND de frais d’authentification, qui n’est pas ce que la question demande. Elle ne précise pas non plus la condition/date “depuis le 1er août 2025”.
- **q015** refused an answerable question. Gold passage retrieved: False
- **q018** correct, faithful=True, citations=False: The answer matches the gold answer: certified photocopies/copies conformes are not accepted and originals are required. All factual claims are supported by the sources, but the standalone 'No.' sentence lacks a citation.
- **q027** refused an answerable question. Gold passage retrieved: False
- **q033** refused an answerable question. Gold passage retrieved: False
- **q042** correct, faithful=True, citations=False: The answer gives the same password-reset steps as the source: click 'mot de passe oublié', enter the account email, use the emailed link to set a new password, and check spam if needed. However, it does not include any citations, so the citation requirement is not met.
- **q043** incorrect, faithful=True, citations=True: The answer gives the wrong amount for the student visa blocked account. The gold answer is 11 904 EUR for one year, or 992 EUR per month, not 1 027 EUR per month or 10 236 EUR.
- **q044** partially_correct, faithful=True, citations=True: The answer is supported by the sources, but it does not give the specific amount asked for. The gold answer expects €11,904 per year (€992 per month), while the response only says the amount varies and points to where to check it.
- **q045** partially_correct, faithful=True, citations=True: La réponse donne correctement la condition de cours, mais elle se trompe sur le financement actuel : elle cite 1 027 €/mois au lieu du montant actuel de 11 904 EUR pour une année. Toutes les affirmations qu’elle contient sont toutefois appuyées par les sources fournies.
- **q047** refused an answerable question. Gold passage retrieved: False
- **q050** incorrect, faithful=False, citations=False: The answer does not give the gold answer’s response that sworn translators are not required for the German visa procedure. Instead, it introduces an unsupported requirement about certified translations from an unrelated source, so it is both incorrect and not properly grounded in the provided sources.
- **q053** correct, faithful=True, citations=False: The answer matches the gold answer: the Federal Foreign Office does not recommend a specific blocked account provider and says prior listing did not count as a recommendation. All substantive claims are supported by the source, but the first standalone "No." is uncited.
- **q062** partially_correct, faithful=True, citations=True: The answer gives the monthly amount for international students correctly as 992 EUR, but it misses the health insurance/repaid details from the gold answer and adds the doctoral amount, which the question did not ask for. All factual claims it makes are supported by the sources and cited correctly.
- **q070** correct, faithful=True, citations=False: The answer matches the gold answer: you cannot apply directly as an individual and must go through the national committee. All factual claims are supported by the sources, but the citation placement is incomplete because the first sentence is uncited.
- **q074** correct, faithful=False, citations=False: The answer correctly says KAAD does fund German language courses and gives the 6-month limit, matching the gold answer. However, it adds an unsupported location phrasing about the course being 'in your home country/in preparation.'
- **q075** correct, faithful=True, citations=False: The answer gives the correct amounts for a single applicant outside Quebec for both relevant time periods, matching the gold answer. However, the first sentence is under-cited because its date range is not supported by the cited source alone.
- **q081** correct, faithful=True, citations=False: The answer gives the key minimum length of 8 months, which matches the gold answer. It is supported by the sources, though one of the citations is unnecessary/mismatched.
- **q086** incorrect, faithful=False, citations=False: The answer gives the opposite of the correct rule: during an authorized leave you cannot work on or off campus, and the leave can be no longer than 150 days. The rest of the answer is mostly supported, but the main answer is wrong.
- **q092** partially_correct, faithful=True, citations=True: It correctly says a SIN is a 9-digit Government of Canada number and that students need one to work in Canada. It leaves out the study-permit work-condition requirement, which is part of the full answer.
- **q105** partially_correct, faithful=False, citations=False: The answer correctly identifies two relevant masters, but it misses REM Plus Plus, which the gold answer also includes. Its factual claims are not fully faithful because it presents an incomplete set as exhaustive, and the opening claim is uncited.
- **q108** correct, faithful=True, citations=False: The answer matches the gold answer: recent graduates can do an Erasmus+ traineeship abroad. Its factual content is supported by the sources, though one citation is not well matched to the claim.
