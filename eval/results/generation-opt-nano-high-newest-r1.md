# Generation evaluation: opt-nano-high-newest-r1

125 questions · answer model `gpt-5.4-nano` (effort high) · judge `gpt-5.4-mini` · 20261025-204646

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **90.4%** |
| Correctness on answerable questions (partial = 0.5) | 90.0% |
| Strictly correct on answerable questions | 89.1% |
| Faithfulness (all claims supported by sources) | 98.1% |
| Citation accuracy | 97.1% |
| "I don't know" on unanswerable questions | 93.3% |
| "I don't know" on answerable questions (false refusals) | 6.4% |
| Correct answers whose gold passage was not retrieved | 8 |
| Cost per question (answer only) | $0.0005 |
| Latency end to end, p50 / p95 | 4.0 s / 7.3 s |
| Tokens per question, in / out | 1346 / 166 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 75.0% |
| cross_lingual | 27 | 74.1% |
| date | 11 | 90.9% |
| fact | 13 | 96.2% |
| list | 3 | 100.0% |
| number | 40 | 96.2% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 93.3% |
| yes_no | 11 | 100.0% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q013** incorrect, faithful=False, citations=False: La réponse donne la mauvaise date limite pour déposer le dossier : la source indique 18/12/2026, pas 31/05/2027. La citation est donc mal utilisée et la réponse ne correspond pas à la question.
- **q015** refused an answerable question. Gold passage retrieved: False
- **q021** correct, faithful=False, citations=True: The answer gives the same bottom line as the gold answer: Tunisian candidates are not automatically exempt from the TCF-DAP, with exemptions only in specific cases. However, it adds the unsupported claim that French is widely used in Tunisia, which is not stated in the provided sources.
- **q027** refused an answerable question. Gold passage retrieved: False
- **q030** refused an answerable question. Gold passage retrieved: True
- **q033** refused an answerable question. Gold passage retrieved: False
- **q042** correct, faithful=True, citations=False: The answer matches the source instructions for resetting an Études en France password and includes the spam-folder reminder. However, it provides no citations, so it does not satisfy the citation requirement.
- **q043** incorrect, faithful=True, citations=True: La réponse ne donne pas le bon montant demandé : le gold indique 11 904 € par an, soit 992 € par mois, alors que l’answer annonce 1 027 € par mois. Les citations utilisées soutiennent bien les phrases, mais elles ne correspondent pas à la réponse attendue.
- **q044** incorrect, faithful=True, citations=True: The answer does not give the actual amount required for a German student-visa blocked account, which is the key fact asked for. It only says the amount varies and tells you where to look for it.
- **q047** refused an answerable question. Gold passage retrieved: False
- **q050** refused an answerable question. Gold passage retrieved: False
- **q062** partially_correct, faithful=True, citations=True: The answer gives the correct monthly amount for international students, 992 EUR, but it also adds a separate doctoral-student amount that is not what the question asks for. All cited facts are supported by the sources.
- **q092** partially_correct, faithful=True, citations=True: The answer correctly says what a SIN is and that you need one to work in Canada as a student. It leaves out the study-permit work-condition requirement from the gold answer, so it is only partially complete.
- **q103** correct, faithful=True, citations=False: The answer correctly says that there is an Erasmus Mundus master in cybersecurity and gives a supported example. The only issue is citation formatting: the standalone "Yes." sentence is uncited.
- **u003** answered an unanswerable question: The Erasmus+ catalogue states that **most master’s programmes require applications to be submitted between October and January** for courses commencin
