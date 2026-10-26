# Judge spot-check: opt-nano-r1

For each item, read the answer and decide whether you agree with the judge. Write agree / disagree. The agreement rate goes in the report.

## q048: judge says partially_correct, faithful=True, citations=True
**Q:** Si j'arrive en Allemagne pour mes études universitaires avant mon immatriculation, quelle assurance maladie dois-je avoir ?  
**Gold:** Une assurance maladie privée pour 90 jours à compter de l'arrivée, car l'assurance légale n'est possible qu'après l'immatriculation. (Pour un cours de langue préparatoire, l'assurance privée doit couvrir toute la durée du visa ; une assurance limitée à 90 jours ne suffit pas.)  
**Answer:** Si vous arrivez en Allemagne avant votre immatriculation, vous devez prouver que vous disposez d’une assurance maladie privée. [S2]
Pour un cours de langue préparatoire aux études, la preuve d’une assurance maladie privée est nécessaire pour toute la durée de validité du visa (en général 6 mois), et une assurance limitée à 90 jours ne convient pas. [S1]  
**Judge's reason:** L’answer dit correctement qu’avant l’immatriculation il faut une assurance maladie privée, mais elle ne donne pas la durée correcte demandée pour des études universitaires (90 jours). Elle ajoute à la place la règle du cours de langue préparatoire, qui n’est pas la réponse principale à la question.  
**Agree?** 

## q021: judge says correct, faithful=False, citations=False
**Q:** Are Tunisian students exempt from the TCF-DAP French test since French is widely spoken in Tunisia?  
**Gold:** No. Tunisia's only official language is Arabic, so Tunisian candidates must take the TCF-DAP unless they hold another exemption, such as a DELF B2, a DALF C1/C2 or a French baccalauréat.  
**Answer:** No. Campus France Tunisia states that Tunisia is one of the countries where **only Arabic is an official language**, and therefore **candidates from Algeria, Morocco, Lebanon and Tunisia are concerned by the TCF-DAP**—so they are not exempt just because French is widely used. [S1][S2]  
**Judge's reason:** The answer correctly says Tunisian students are not exempt from the TCF-DAP on the basis of French being widely spoken. However, it adds an unsupported claim about French's widespread use in Tunisia that is not stated in the provided sources.  
**Agree?** 

## q058: judge says correct, faithful=True, citations=True
**Q:** Quand a eu lieu le séminaire en ligne du DAAD Tunis sur le doctorat en Allemagne ?  
**Gold:** Le 21 mai 2026, de 14h00 à 15h00 (heure tunisienne), en anglais.  
**Answer:** Le séminaire en ligne du DAAD Tunisie sur le doctorat en Allemagne a eu lieu le 21 mai 2026, de 14h00 à 15h00 (heure tunisienne, GMT +1). [S1][S2]  
**Judge's reason:** L’ענה répond exactement à la date et à l’heure du séminaire, ce qui correspond à la réponse de référence. Les citations [S1][S2] soutiennent bien cette information, et la mention GMT+1 est aussi présente dans les sources.  
**Agree?** 

## q091: judge says correct, faithful=True, citations=True
**Q:** Can I start working in Canada as soon as I arrive, before my classes start?  
**Gold:** No. You can't work on or off campus until you begin your studies in Canada.  
**Answer:** No. You can only start working in Canada when you start your study program—you can’t work before your studies begin (even if you arrive before classes start). [S2][S3]  
**Judge's reason:** The answer matches the gold answer: you cannot work in Canada before your studies begin. Its citations support that rule.  
**Agree?** 

## q008: judge says correct, faithful=True, citations=True
**Q:** By when do CampusArt applicants have to confirm their enrolment in a programme?  
**Gold:** By 31 May 2027, on their CampusArt account.  
**Answer:** CampusArt applicants must confirm their admission to the programme by **31 May 2027** on their CampusArt account. [S1]  
**Judge's reason:** The answer matches the source: applicants must confirm their enrolment/entry into the programme by 31 May 2027 on their CampusArt account. The citation points to the relevant deadline in the source.  
**Agree?** 

## q011: judge says correct, faithful=True, citations=True
**Q:** Jusqu'à quand puis-je soumettre mon dossier DAP pour une Licence 1 à la rentrée 2027 ?  
**Gold:** Jusqu'au 11/12/2026 pour soumettre le dossier et payer (création à partir du 01/10/2026 ; entretien Campus France jusqu'au 15/03/2027 ; réponses des établissements jusqu'au 30/04/2027 ; choix définitif au plus tard le 31/05/2027).  
**Answer:** Pour une Licence 1 en procédure DAP (rentrée 2027), vous devez déposer votre dossier au plus tard le **11 décembre 2026**. [S3]  
**Judge's reason:** L’ענה répond bien à la date limite demandée : le 11 décembre 2026. Cette information est conforme à la source citée et rien de contraire n’est ajouté.  
**Agree?** 

## q076: judge says correct, faithful=True, citations=True
**Q:** How many hours per week can I work off campus in Canada during the school term?  
**Gold:** Up to 24 hours per week during regular school terms.  
**Answer:** During regular school terms or semesters, you can work up to **24 hours per week** off campus (while meeting the conditions on your study permit). [S1]  
**Judge's reason:** The answer matches the gold answer: 24 hours per week during regular school terms. The citation supports that statement.  
**Agree?** 

## q014: judge says incorrect, faithful=True, citations=True
**Q:** Combien coûtent les frais de dossier Campus France en Tunisie ?  
**Gold:** 400 DT depuis le 1er août 2025.  
**Answer:** Les frais d’authentification (dossier Campus France) en Tunisie s’élèvent à **150 TND** pour l’instruction du dossier. [S1][S4]  
**Judge's reason:** La réponse donne 150 TND, qui correspond aux frais d’authentification, alors que la question demande les frais de dossier Campus France en Tunisie. Le bon montant attendu est 400 DT depuis le 1er août 2025.  
**Agree?** 

## q054: judge says correct, faithful=True, citations=True
**Q:** Qui peut postuler au programme KOSPIE du DAAD et en quoi consiste-t-il ?  
**Gold:** Les étudiants tunisiens en ingénierie ou en informatique en deuxième année du cycle d'ingénieur (annonce du DAAD Tunis) ; la fiche du DAAD parle plus largement des étudiants de master ou de diplôme d'ingénieur et d'informatique dans un établissement tunisien public ou reconnu. La bourse finance un séjour de six mois dans une université allemande pour le projet de fin d'études.  
**Answer:** Peuvent postuler au programme KOSPIE (DAAD) les étudiants diplômés/« Master’s » (selon la base DAAD) inscrits dans les sciences de l’ingénierie (y compris un axe “green engineering”) et en informatique dans une université publique ou reconnue par l’État en Tunisie. [S2] 

Le programme consiste en un séjour d’étude et pratique de 6 mois dans des universités allemandes sélectionnées pour y réaliser le projet de fin d’études (final project) dans le cadre d’un cursus d’ingénierie. [S3]  
**Judge's reason:** La réponse donne bien les critères d’éligibilité et décrit correctement le programme comme un séjour de 6 mois pour réaliser le projet de fin d’études en Allemagne. Toutes les affirmations sont étayées par les sources citées.  
**Agree?** 

## q082: judge says correct, faithful=True, citations=True
**Q:** Do I need a provincial attestation letter (PAL) to apply for a Canadian study permit for a master's at a public university?  
**Gold:** No. Since 1 January 2026, master's and doctoral students in degree-granting programmes at public institutions don't need a PAL/TAL (Quebec still has its own requirements).  
**Answer:** If you’re applying to a **degree-granting graduate program (master’s or doctoral) at a public DLI starting January 1, 2026**, you **don’t need** a provincial attestation letter (PAL) (nor a territorial attestation letter). [S1]  
**Judge's reason:** The answer directly states the exemption for a master’s program at a public institution starting January 1, 2026, which matches the source and the gold answer. It is fully supported and the citation is attached to the factual claim.  
**Agree?** 

## q009: judge says correct, faithful=True, citations=True
**Q:** Combien d'années dure le BUT et quand peut-on candidater pour la rentrée 2027 ?  
**Gold:** 3 ans (6 semestres) ; candidature ouverte du 1er octobre 2026 au 18 décembre 2026.  
**Answer:** Le BUT (Bachelor universitaire de technologie) se prépare en 3 ans, depuis la rentrée 2021. [S1] Pour la rentrée 2027, la candidature au BUT est ouverte du 01 octobre 2026 au 18 décembre 2026. [S2]  
**Judge's reason:** L’ענה répond exactement à la durée du BUT et aux dates de candidature demandées, sans contradiction avec la réponse de référence. Les deux phrases sont bien appuyées par les sources citées.  
**Agree?** 

## q072: judge says correct, faithful=True, citations=True
**Q:** With a DAAD Doctoral Programmes scholarship, can I spend part of my PhD outside Germany?  
**Gold:** Yes, if it is critical for the doctorate, but such visits must be no more than one quarter of the total funding period.  
**Answer:** Yes. Research phases outside Germany can be funded if they are critical for completing your doctoral degree, but the visits must make up **no more than one quarter** of the anticipated total funding period, and you must detail the planned visits in your study plan/time schedule in your application documents. [S2]  
**Judge's reason:** The answer matches the gold answer: part of the PhD can be spent outside Germany if it is critical for the doctorate, and the time abroad must not exceed one quarter of the funding period. The cited source supports all factual claims made.  
**Agree?** 

## q031: judge says correct, faithful=True, citations=True
**Q:** How can I get a refund of the CVEC if I become exempt during the year?  
**Gold:** Apply to CROUS before 31 May of the academic year concerned.  
**Answer:** If, during the academic year, you become exempt from paying the CVEC, you may be eligible to obtain a refund. [S1] To request the refund, apply to CROUS before May 31 of the academic year for which you are seeking the refund. [S1]  
**Judge's reason:** The answer matches the gold answer: apply to CROUS before May 31 of the relevant academic year. Both factual sentences are supported by [S1], and the citations are placed correctly.  
**Agree?** 

## q006: judge says correct, faithful=True, citations=True
**Q:** Combien faut-il payer pour obtenir un deuxième rendez-vous si on a manqué son entretien Campus France ?  
**Gold:** 100 TND de frais supplémentaires.  
**Answer:** Il faut payer **100 TND** pour obtenir un deuxième rendez-vous après avoir manqué son entretien Campus France. [S1][S2][S3][S4]  
**Judge's reason:** La réponse donne bien le montant demandé: 100 TND pour un deuxième rendez-vous après une absence à l’entretien Campus France. La phrase est entièrement appuyée par les sources citées.  
**Agree?** 

## q013: judge says incorrect, faithful=False, citations=False
**Q:** Pour la procédure hors-DAP (BUT, master, école d'ingénieurs), jusqu'à quand puis-je soumettre mon dossier pour la rentrée 2027 ?  
**Gold:** Jusqu'au 18/12/2026 pour soumettre le dossier et payer (création à partir du 01/10/2026 ; entretien jusqu'au 15/03/2027 ; réponses des établissements jusqu'au 30/04/2027 ; choix définitif au plus tard le 31/05/2027). Ces dates valent pour BUT, Licence 2/3, Master 1/2, écoles d'ingénieurs et de commerce.  
**Answer:** Pour la procédure **hors-DAP** (BUT, Licence 2/3, Master, cycle ingénieur), la soumission du dossier pour la rentrée 2027 peut se faire **jusqu’au 30/04/2027**. [S1]  
**Judge's reason:** La date donnée est fausse : pour la procédure hors-DAP, la date limite de soumission du dossier est le 18/12/2026, pas le 30/04/2027. La réponse confond avec la date des réponses des établissements.  
**Agree?** 

