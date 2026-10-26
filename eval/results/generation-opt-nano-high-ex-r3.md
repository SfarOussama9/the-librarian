# Generation evaluation: opt-nano-high-ex-r3

125 questions · answer model `gpt-5.4-nano` (effort high) · judge `gpt-5.4-mini` · 20261025-203355

| Metric | Value |
|---|---|
| **Accuracy** (all questions handled correctly) | **89.2%** |
| Correctness on answerable questions (partial = 0.5) | 87.7% |
| Strictly correct on answerable questions | 84.5% |
| Faithfulness (all claims supported by sources) | 91.3% |
| Citation accuracy | 93.3% |
| "I don't know" on unanswerable questions | 100.0% |
| "I don't know" on answerable questions (false refusals) | 5.5% |
| Correct answers whose gold passage was not retrieved | 5 |
| Cost per question (answer only) | $0.0004 |
| Latency end to end, p50 / p95 | 4.0 s / 7.7 s |
| Tokens per question, in / out | 2117 / 193 |
| API errors | 0 |

### Accuracy by question type

| type | n | accuracy |
|---|---|---|
| conflict | 4 | 62.5% |
| cross_lingual | 27 | 79.6% |
| date | 11 | 90.9% |
| fact | 13 | 100.0% |
| list | 3 | 83.3% |
| number | 40 | 92.5% |
| stale | 1 | 100.0% |
| unanswerable | 15 | 100.0% |
| yes_no | 11 | 81.8% |

### Failures

- **q002** refused an answerable question. Gold passage retrieved: False
- **q012** partially_correct, faithful=True, citations=True: L’ענה donne bien la date actuelle de référence, le 11 décembre 2026, mais il ajoute aussi l’ancienne date du 31 janvier, ce qui rend la réponse moins directement conforme à la question posée. Toutes les affirmations sont appuyées par les sources fournies.
- **q013** incorrect, faithful=False, citations=False: La réponse donne la mauvaise date limite pour le dépôt du dossier hors-DAP : c’est 18/12/2026, pas 31/05/2027. La citation est aussi mal attribuée car 31/05/2027 correspond au choix définitif, pas à la soumission du dossier.
- **q014** partially_correct, faithful=True, citations=True: L’ענה répond bien que les frais de dossier sont de 400 DT, ce qui correspond à la source. En revanche, elle ne mentionne pas la précision temporelle « depuis le 1er août 2025 » présente dans la réponse attendue.
- **q015** partially_correct, faithful=True, citations=True: The answer correctly says cheque payments are not accepted, but it fails to answer the postal-application part, which the gold answer says is also no. Its factual claims are supported by the source provided.
- **q027** refused an answerable question. Gold passage retrieved: False
- **q033** refused an answerable question. Gold passage retrieved: False
- **q043** incorrect, faithful=True, citations=True: La réponse cite des montants pour un visa de cours de langue et pour un compte bloqué après l’entrée en Allemagne, mais elle ne donne pas le montant demandé pour un visa étudiant. Le bon montant attendu est 11 904 EUR par an (992 EUR par mois).
- **q044** refused an answerable question. Gold passage retrieved: False
- **q047** refused an answerable question. Gold passage retrieved: False
- **q050** refused an answerable question. Gold passage retrieved: False
- **q054** correct, faithful=False, citations=False: L’ענה répond correctement à qui peut postuler et à quoi consiste le programme, conformément au GOLD. En revanche, une formulation précise n’est pas entièrement étayée par les sources, donc la fidélité et les citations ne sont pas parfaites.
- **q062** partially_correct, faithful=True, citations=True: The answer gives the correct monthly amount for international students, but it also adds the doctoral scholarship amount, which the question did not ask for. All stated facts are supported by the sources and the citations are appropriate.
- **q065** correct, faithful=False, citations=True: The answer gives the correct deadline of 1 March for non-European applicants, which matches the sources and applies to a Tunisian applicant. However, the Tunisian/non-European classification is not stated in the sources, so that part is unsupported.
- **q066** correct, faithful=False, citations=False: The answer gives the correct age and German-language requirements from the gold answer. However, it adds the unsupported claim that Tunisia is included in the programme, so it is not fully faithful and the citation does not support every factual part of the sentence.
- **q079** correct, faithful=False, citations=True: The answer gives the correct fee amount, matching the source and gold answer. The only issue is that it adds CAD, which is not explicitly stated in the cited source.
- **q081** partially_correct, faithful=True, citations=True: The answer correctly states the 8-month minimum length (and the Quebec-hour equivalent), which is the key fact asked. It does not mention the full-time requirement from the gold answer, so it is slightly incomplete.
- **q082** incorrect, faithful=False, citations=False: The question asks whether you need a PAL for a master's at a public university, and the source says no starting January 1, 2026. The answer contradicts that with an initial "Yes," so it is not correct.
- **q086** incorrect, faithful=False, citations=False: The answer contradicts the gold answer by implying you may work during an authorized leave, when the sources say you cannot. It also mixes in a separate strike-closure exception that is not the same as authorized leave.
- **q087** correct, faithful=False, citations=False: L’essentiel de la réponse est ճիշտ: pour un changement d’établissement, une nouvelle PAL/TAL est requise à partir du 22 janvier 2025. Toutefois, elle ajoute une précision non explicitement donnée par les sources et cite imparfaitement certaines phrases.
- **q088** partially_correct, faithful=True, citations=True: The answer gives the correct processing time of 60 days, but it omits the condition that faster processing applies only if you follow the instructions for faster processing. The citation supports the statement made.
- **q105** partially_correct, faithful=False, citations=False: The answer includes the three gold examples (EU-CORE, RESCO, REM Plus Plus), but it also adds items not supported as Erasmus Mundus masters, especially MIRET. Its citations are therefore not fully correct.
