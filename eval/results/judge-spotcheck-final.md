# Judge spot-check: opt-nano-high-newest-r1 (final Week 8 setup)

15 judge verdicts, sampled at random (seed 7) from the final setup's run 1, checked against
the answer **and the source chunks the model saw** (not only against the judge's reasons).

**Result: 14 / 15 correctness verdicts agree (93%); faithfulness and citation verdicts agree
on 15 / 15.** The one disagreement (q014) is the judge being too lenient: it accepted an
answer that leads with a fee that only applies to health studies.

Also noticed: in 3 of the 15 reasons (q011, q009, q006) the judge writes a stray word in
another script (Hebrew/Chinese, e.g. "L’ענה"). The verdict fields are unaffected.


## q048: judge says correct, faithful=True, citations=True
**Q:** Si j'arrive en Allemagne pour mes études universitaires avant mon immatriculation, quelle assurance maladie dois-je avoir ?  
**Gold:** Une assurance maladie privée pour 90 jours à compter de l'arrivée, car l'assurance légale n'est possible qu'après l'immatriculation. (Pour un cours de langue préparatoire, l'assurance privée doit couvrir toute la durée du visa ; une assurance limitée à 90 jours ne suffit pas.)  
**Answer:** Si vous arrivez en Allemagne avant votre immatriculation pour vos études universitaires, vous devez prouver que vous disposez d’une assurance maladie privée pour 90 jours à compter de votre arrivée. [S3]  
**Judge's reason:** La réponse reprend exactement l’exigence indiquée par la source: une assurance maladie privée pendant 90 jours à compter de l’arrivée avant l’immatriculation. Elle ne contient pas de fait non soutenu par les sources citées.  
**Agree?** agree. S3 states the 90-day private insurance rule before enrolment.

## q022: judge says correct, faithful=True, citations=True
**Q:** Je candidate en master en France : où dois-je m'inscrire pour passer un test de français ?  
**Gold:** Il faut contacter directement l'antenne de l'Institut français de Tunisie la plus proche de chez vous (le TCF-DAP ne concerne que la licence 1/2 et les écoles d'architecture).  
**Answer:** Si vous candidatez en **master** (donc “autre type d’études”), vous devez **contacter directement l’antenne de l’Institut français de Tunisie la plus proche de votre domicile** pour vous inscrire aux épreuves de langue. [S1]
Pour savoir **si un test est nécessaire** et **quel test passer**, vous devez aussi **vous adresser à l’établissement** où vous souhaitez poursuivre vos études. [S2]  
**Judge's reason:** The answer correctly says that a master applicant should contact the nearest antenne of the Institut français de Tunisie to register for the French test. It also correctly adds, with support, that the institution can confirm whether a test is required and which one to take.  
**Agree?** agree. S1 says master's applicants contact the nearest Institut français antenna; S2 supports the second sentence.

## q058: judge says correct, faithful=True, citations=True
**Q:** Quand a eu lieu le séminaire en ligne du DAAD Tunis sur le doctorat en Allemagne ?  
**Gold:** Le 21 mai 2026, de 14h00 à 15h00 (heure tunisienne), en anglais.  
**Answer:** Le séminaire en ligne du DAAD Tunis sur « Faire un doctorat en Allemagne et les possibilités de financement du DAAD » a eu lieu le 21 mai 2026, de 14h00 à 15h00 (heure tunisienne, GMT +1). [S1][S2]  
**Judge's reason:** La réponse donne bien la date et l’heure du séminaire, conformément aux sources et à l’attendu. La citation appuyée par [S1][S2] est appropriée et toutes les affirmations factuelles sont sourcées.  
**Agree?** agree. 21 May 2026, 14:00-15:00, as in S1/S2.

## q091: judge says correct, faithful=True, citations=True
**Q:** Can I start working in Canada as soon as I arrive, before my classes start?  
**Gold:** No. You can't work on or off campus until you begin your studies in Canada.  
**Answer:** No. You can only start working in Canada when you start your study program, and you can’t work before your studies begin—so arriving before your classes start does not allow you to work right away. [S2][S3][S4]  
**Judge's reason:** The answer matches the sources: international students cannot work in Canada before their studies begin. The citations all support the statement and there are no unsupported factual claims.  
**Agree?** agree. S2-S4 say you can't work before your studies begin.

## q008: judge says correct, faithful=True, citations=True
**Q:** By when do CampusArt applicants have to confirm their enrolment in a programme?  
**Gold:** By 31 May 2027, on their CampusArt account.  
**Answer:** CampusArt applicants must confirm their entry into their training programme by **31 May 2027** on their CampusArt account. [S1]  
**Judge's reason:** The answer gives the correct deadline and account location from the source. Its only factual claim is supported by [S1], and the citation is appropriate.  
**Agree?** agree. 31 May 2027 on the CampusArt account (S1).

## q011: judge says correct, faithful=True, citations=True
**Q:** Jusqu'à quand puis-je soumettre mon dossier DAP pour une Licence 1 à la rentrée 2027 ?  
**Gold:** Jusqu'au 11/12/2026 pour soumettre le dossier et payer (création à partir du 01/10/2026 ; entretien Campus France jusqu'au 15/03/2027 ; réponses des établissements jusqu'au 30/04/2027 ; choix définitif au plus tard le 31/05/2027).  
**Answer:** Pour une **Licence 1 (procédure DAP Blanche)** à la rentrée 2027, vous devez **déposer votre dossier de candidature au plus tard le 11 décembre 2026**. [S3][S2]  
**Judge's reason:** L’ענה répond bien à la question en indiquant la bonne date limite de dépôt pour la Licence 1 DAP à la rentrée 2027. La citation renvoie à des sources qui soutiennent cette date.  
**Agree?** agree. S3 gives 11 December 2026 for DAP Licence 1; S2's table matches.

## q076: judge says correct, faithful=True, citations=True
**Q:** How many hours per week can I work off campus in Canada during the school term?  
**Gold:** Up to 24 hours per week during regular school terms.  
**Answer:** During regular school terms or semesters, you can work up to 24 hours per week off campus in Canada [S1]. Working more than 24 hours per week is a violation of your study permit conditions [S4].  
**Judge's reason:** The answer gives the correct limit for regular school terms: up to 24 hours per week. The extra statement about exceeding 24 hours is also supported by the sources and does not contradict the gold answer.  
**Agree?** agree. 24 h/week (S1). The second sentence comes from S4's 'no scheduled breaks' paragraph but applies to the same 24 h limit.

## q014: judge says correct, faithful=True, citations=True
**Q:** Combien coûtent les frais de dossier Campus France en Tunisie ?  
**Gold:** 400 DT depuis le 1er août 2025.  
**Answer:** Les frais d’authentification pour l’instruction du dossier (Campus France Tunisie) sont de **150 TND**. [S1][S2][S4]
En plus, dans la rubrique « Je procède au paiement des frais de dossier », il est indiqué que le paiement des « frais de dossier » est de **400 DT** après soumission correcte du dossier électronique (avec des cas d’exemption mentionnés). [S3]  
**Judge's reason:** L’answer donne bien le montant des frais de dossier demandé : 400 DT. La mention des 150 TND concerne des frais d’authentification séparés et est également soutenue par les sources.  
**Agree?** **disagree**: should be partially_correct. The answer leads with 150 TND as the Campus France file fee, but S1/S2/S4 give that as an authentication fee for health studies only; the general 400 DT fee comes second. Faithful and citations: agree (each figure is in its cited source).

## q054: judge says correct, faithful=True, citations=True
**Q:** Qui peut postuler au programme KOSPIE du DAAD et en quoi consiste-t-il ?  
**Gold:** Les étudiants tunisiens en ingénierie ou en informatique en deuxième année du cycle d'ingénieur (annonce du DAAD Tunis) ; la fiche du DAAD parle plus largement des étudiants de master ou de diplôme d'ingénieur et d'informatique dans un établissement tunisien public ou reconnu. La bourse finance un séjour de six mois dans une université allemande pour le projet de fin d'études.  
**Answer:** Au programme KOSPIE (DAAD), peuvent postuler des étudiants tunisiens en ingénierie et informatique inscrits dans une université publique ou reconnue, notamment des étudiants en sciences de l’ingénierie et en informatique (incluant éventuellement le green engineering), et (selon l’appel 2027) ceux actuellement inscrits en 2e année du cycle d’ingénieur. [S2][S1]
Le programme consiste en un séjour d’une durée de 6 mois dans une université allemande pour réaliser le projet de fin d’études (thèse/projet final) dans le cadre d’un cursus d’ingénieur, avec un volet étude et pratique afin d’améliorer les compétences scientifiques/techniques, pratiques et générales/interculturelles. [S1][S3][S2]  
**Judge's reason:** La réponse donne les critères d’éligibilité principaux et décrit correctement le contenu du programme, conformément au gold. Toutes les affirmations sont appuyées par les sources fournies et les citations sont bien placées.  
**Agree?** agree. Eligibility and the 6-month final-project stay match S1-S3.

## q082: judge says correct, faithful=True, citations=True
**Q:** Do I need a provincial attestation letter (PAL) to apply for a Canadian study permit for a master's at a public university?  
**Gold:** No. Since 1 January 2026, master's and doctoral students in degree-granting programmes at public institutions don't need a PAL/TAL (Quebec still has its own requirements).  
**Answer:** Starting January 1, 2026, if you’re applying for a study permit to attend a degree-granting master’s program at a public institution, you don’t need a provincial or territorial attestation letter (PAL/TAL). [S4][S1]
If you’re planning to study in Quebec, you still need to meet the province’s requirements. [S4]  
**Judge's reason:** The answer correctly says a PAL/TAL is not needed for a master’s program at a public institution starting January 1, 2026, and it notes Quebec’s separate requirements. All claims are supported by the cited sources.  
**Agree?** agree. PAL/TAL exemption from 1 Jan 2026 and the Quebec caveat (S1, S4).

## q009: judge says correct, faithful=True, citations=True
**Q:** Combien d'années dure le BUT et quand peut-on candidater pour la rentrée 2027 ?  
**Gold:** 3 ans (6 semestres) ; candidature ouverte du 1er octobre 2026 au 18 décembre 2026.  
**Answer:** Le BUT dure 3 ans. [S1]
Pour la rentrée 2027, la candidature au BUT (hors-DAP) est ouverte du 1er octobre 2026 au 18 décembre 2026. [S2]  
**Judge's reason:** L’ענה répond bien aux deux éléments demandés : durée du BUT et période de candidature pour la rentrée 2027. Toutes les affirmations sont appuyées par les sources citées.  
**Agree?** agree. 3 years (S1); 1 Oct-18 Dec 2026 (S2).

## q072: judge says correct, faithful=True, citations=True
**Q:** With a DAAD Doctoral Programmes scholarship, can I spend part of my PhD outside Germany?  
**Gold:** Yes, if it is critical for the doctorate, but such visits must be no more than one quarter of the total funding period.  
**Answer:** Yes. Under the DAAD Doctoral Programmes scholarship, research phases outside Germany can be funded if they are critical for successfully completing your doctorate, and the visits must make up **no more than one quarter** of the anticipated total funding period (details must be included in your application documents). [S2]  
**Judge's reason:** The answer matches the gold answer: it says you can spend time outside Germany if it is critical for the doctorate, and that it may be at most one quarter of the funding period. The citation to S2 supports the statement and no unsupported factual claims are made.  
**Agree?** agree. Research abroad if critical, max one quarter of the funding period (S2).

## q032: judge says correct, faithful=True, citations=True
**Q:** What is the age limit for the Eiffel scholarship?  
**Gold:** Up to 29 years old at master's level and up to 35 at PhD level.  
**Answer:** The Eiffel scholarship encourages applicants from foreign countries up to **29 years old** at **master’s** level, and applicants up to **35 years old** at **PhD** level. [S1]  
**Judge's reason:** The answer matches the source and the gold answer: the age limit is up to 29 for master’s level and up to 35 for PhD level. The citation [S1] supports the statement.  
**Agree?** agree. 29 (master's) / 35 (PhD), S1.

## q006: judge says correct, faithful=True, citations=True
**Q:** Combien faut-il payer pour obtenir un deuxième rendez-vous si on a manqué son entretien Campus France ?  
**Gold:** 100 TND de frais supplémentaires.  
**Answer:** En cas d’absence à votre rendez-vous d’entretien Campus France, vous devez payer **100 TND** pour obtenir un deuxième rendez-vous. [S1][S3]  
**Judge's reason:** L’ענה回答 donne le bon montant: 100 TND, conforme à la source. La citation [S1][S3] soutient bien cette information.  
**Agree?** agree. 100 TND (S1, S3).

## q013: judge says incorrect, faithful=False, citations=False
**Q:** Pour la procédure hors-DAP (BUT, master, école d'ingénieurs), jusqu'à quand puis-je soumettre mon dossier pour la rentrée 2027 ?  
**Gold:** Jusqu'au 18/12/2026 pour soumettre le dossier et payer (création à partir du 01/10/2026 ; entretien jusqu'au 15/03/2027 ; réponses des établissements jusqu'au 30/04/2027 ; choix définitif au plus tard le 31/05/2027). Ces dates valent pour BUT, Licence 2/3, Master 1/2, écoles d'ingénieurs et de commerce.  
**Answer:** Pour la procédure **hors-DAP** (BUT, Licence 2/3, Master, cycle ingénieur), vous pouvez soumettre votre dossier **au plus tard le 31/05/2027** pour la rentrée 2027 [S1].  
**Judge's reason:** La réponse donne la mauvaise date limite pour déposer le dossier : la source indique 18/12/2026, pas 31/05/2027. La citation est donc mal utilisée et la réponse ne correspond pas à la question.  
**Agree?** agree. 31/05/2027 is the final-choice date in S1's table, not the submission deadline (18/12/2026), so incorrect, unfaithful and wrongly cited.

