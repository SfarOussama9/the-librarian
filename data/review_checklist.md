# Evaluation set: review checklist

> **Status: reviewed by the team on 25 Oct 2026; all 125 questions accepted.**
> **Corrections after a check against the original sources (25 Oct 2026):** q011 and q013 (the later calendar steps were in the wrong columns; submission dates were right), and q045 (now uses the current embassy page; the 2022 PDF amount is marked outdated). All 23 hard questions were then re-checked against their sources by Claude: q036 (missing master-diploma condition) and q075 (date range of the older amount) were made more precise; the rest were correct. After the first generation evaluation, q048, q054 and q066 were fixed too: the system's answers were more complete than the gold answers (two programmes / two cases the gold had missed). See `data/eval_questions.jsonl` for the corrected answers.

**Every question is checked by a person before we use it.**
The script `eval/check_questions.py` already confirmed that every quote exists in its document; what it can't check is whether
the question is sensible and the answer is **correct and complete**.

## How to review (about 30–45 minutes per person)

For each question:
1. Open the source link and find the quoted passage (Ctrl+F part of the quote).
2. Check: is the question something a real student would ask? Is the answer right and complete according to the source?
3. Tick `[x]` if it's fine. If not, write what's wrong after **Fix:** (don't edit the JSONL; we'll apply fixes together).
4. For "I don't know" questions: check that the answer really isn't in our sources.

Put your name next to your part when you start.

## Part 1 (q001–q032), reviewer: ______

### [x] q001 · number · easy
**Q:** Combien d'heures par an un étudiant étranger peut-il travailler en France avec un titre de séjour « étudiant » ?  
**A:** 964 heures par an au maximum, l'activité devant rester accessoire aux études.  
**Source:** [fr-cft-faq-q12](https://www.tunisie.campusfrance.org/faq/faut-il-un-visa-specifique-pour-travailler-pendant-ses-etudes): "dans la limite d'une durée annuelle de travail de 964 heures"  
**Fix:** 

### [x] q002 · cross_lingual · medium
**Q:** Do I need to apply for a work authorisation to work part-time while studying in France on a student visa?  
**A:** No. A foreign student holding a residence permit or long-stay visa marked 'étudiant' can work as an employee without a work authorisation, as long as the work stays secondary to studies (max 964 hours a year).  
**Source:** [fr-cft-faq-q12](https://www.tunisie.campusfrance.org/faq/faut-il-un-visa-specifique-pour-travailler-pendant-ses-etudes): "peut travailler en qualité de salarié en France sans avoir à demander d'autorisation de travail"  
**Fix:** 

### [x] q003 · number · medium
**Q:** Combien de temps avant l'embauche l'employeur doit-il déclarer un étudiant étranger à la préfecture ?  
**A:** Au moins 2 jours ouvrables avant la date d'effet de l'embauche, avec une copie du titre de séjour ou du visa.  
**Source:** [fr-cft-faq-q12](https://www.tunisie.campusfrance.org/faq/faut-il-un-visa-specifique-pour-travailler-pendant-ses-etudes): "au moins 2 jours ouvrables avant la date d'effet de l'embauche"  
**Fix:** 

### [x] q004 · number · easy
**Q:** Combien de temps ai-je pour valider mon VLS-TS après mon arrivée en France ?  
**A:** Trois mois après l'arrivée ; la validation se fait en ligne.  
**Source:** [fr-cft-formalites-arrivee](https://www.tunisie.campusfrance.org/les-formalites-a-accomplir-a-l-arrivee-0): "Vous disposez de trois mois pour faire les démarches nécessaires"  
**Source:** [fr-cft-accepte](https://www.tunisie.campusfrance.org/je-suis-accepte-dans-un-etablissement-francais): "Vous disposez de trois mois pour faire les démarches nécessaires"  
**Fix:** 

### [x] q005 · cross_lingual · medium
**Q:** Since when is the validation of the French VLS-TS student visa done online?  
**A:** Since 18 February 2019.  
**Source:** [fr-cft-formalites-arrivee](https://www.tunisie.campusfrance.org/les-formalites-a-accomplir-a-l-arrivee-0): "Depuis le 18 février 2019, ces démarches se font en ligne"  
**Source:** [fr-cft-accepte](https://www.tunisie.campusfrance.org/je-suis-accepte-dans-un-etablissement-francais): "Depuis le 18 février 2019, ces démarches se font en ligne"  
**Fix:** 

### [x] q006 · number · easy
**Q:** Combien faut-il payer pour obtenir un deuxième rendez-vous si on a manqué son entretien Campus France ?  
**A:** 100 TND de frais supplémentaires.  
**Source:** [fr-cft-entretien](https://www.tunisie.campusfrance.org/l-entretien-campus-france): "d'un montant 100 TND"  
**Source:** [fr-cft-accepte](https://www.tunisie.campusfrance.org/je-suis-accepte-dans-un-etablissement-francais): "d'un montant de 100 TND"  
**Fix:** 

### [x] q007 · date · easy
**Q:** Quelle est la date limite de dépôt des candidatures sur la plateforme CampusArt pour la rentrée 2027 ?  
**A:** Le 28 février 2027 (constitution du dossier du 1er octobre 2026 au 28 février 2027).  
**Source:** [fr-cft-arts](https://www.tunisie.campusfrance.org/les-etudes-d-arts-et-d-architecture-campusart): "28 février 2027 : Date limite du dépôt de candidature sur la plateforme CampusArt"  
**Fix:** 

### [x] q008 · cross_lingual · medium
**Q:** By when do CampusArt applicants have to confirm their enrolment in a programme?  
**A:** By 31 May 2027, on their CampusArt account.  
**Source:** [fr-cft-arts](https://www.tunisie.campusfrance.org/les-etudes-d-arts-et-d-architecture-campusart): "31 mai 2027 : Date limite de confirmation d'entrée en formation"  
**Fix:** 

### [x] q009 · date · easy
**Q:** Combien d'années dure le BUT et quand peut-on candidater pour la rentrée 2027 ?  
**A:** 3 ans (6 semestres) ; candidature ouverte du 1er octobre 2026 au 18 décembre 2026.  
**Source:** [fr-cft-but](https://www.tunisie.campusfrance.org/but-ce-qu-il-faut-savoir-sur-ce-diplome): "Candidature ouverte du 01 octobre 2026 au 18 décembre 2026"  
**Source:** [fr-cft-but](https://www.tunisie.campusfrance.org/but-ce-qu-il-faut-savoir-sur-ce-diplome): "diplôme préparé en 03 ans"  
**Fix:** 

### [x] q010 · cross_lingual · medium
**Q:** What diploma did the French BUT replace, and since when?  
**A:** It replaced the DUT (Diplôme universitaire de technologie) from the 2021 academic year.  
**Source:** [fr-cft-but](https://www.tunisie.campusfrance.org/but-ce-qu-il-faut-savoir-sur-ce-diplome): "qui remplace le DUT (Diplôme universitaire de technologie), depuis la rentrée 2021"  
**Fix:** 

### [x] q011 · date · medium
**Q:** Jusqu'à quand puis-je soumettre mon dossier DAP pour une Licence 1 à la rentrée 2027 ?  
**A:** Jusqu'au 11/12/2026 (création du dossier à partir du 01/10/2026 ; paiement jusqu'au 15/03/2027 ; entretien jusqu'au 30/04/2027 ; choix définitif au plus tard le 31/05/2027).  
**Source:** [fr-cft-calendrier-2026-2027-pdf](https://www.tunisie.campusfrance.org/system/files/medias/documents/2026-10/calendrier%20EEF%202026_2027.pdf): "Licence 1 L.AS / PASS À partir du 01/10/2026 Jusqu'au 11/12/2026"  
**Note:** Table cells are flattened in the PDF text; check the column meaning against the original PDF.  
**Fix:** 

### [x] q012 · conflict · hard
**Q:** Quelle est la date limite pour déposer un dossier DAP ?  
**A:** Selon le calendrier officiel 2026/2027, jusqu'au 11/12/2026. Une ancienne page FAQ de Campus France indique encore le 31 janvier : le calendrier 2026/2027 est la référence actuelle.  
**Source:** [fr-cft-calendrier-2026-2027-pdf](https://www.tunisie.campusfrance.org/system/files/medias/documents/2026-10/calendrier%20EEF%202026_2027.pdf): "Licence 1 L.AS / PASS À partir du 01/10/2026 Jusqu'au 11/12/2026"  
**Outdated source:** [fr-cft-faq-q34](https://www.tunisie.campusfrance.org/faq/quand-et-comment-demander-une-pre-inscription-dans-un-etablissement-d-enseignement-superieur-en): "la date limite pour le dépôt de dossier DAP est le 31 janvie"  
**Fix:** 

### [x] q013 · date · hard
**Q:** Pour la procédure hors-DAP (BUT, master, école d'ingénieurs), jusqu'à quand puis-je soumettre mon dossier pour la rentrée 2027 ?  
**A:** Jusqu'au 18/12/2026 (ouverture le 01/10/2026 ; paiement jusqu'au 15/03/2027 ; entretien jusqu'au 30/04/2027).  
**Source:** [fr-cft-calendrier-2026-2027-pdf](https://www.tunisie.campusfrance.org/system/files/medias/documents/2026-10/calendrier%20EEF%202026_2027.pdf): "BUT À partir du 01/10/2026 Jusqu'au 18/12/2026"  
**Note:** The PDF text only shows dates next to BUT; check in the original PDF that Master and engineering-school rows share the HORS-DAP dates.  
**Fix:** 

### [x] q014 · number · easy
**Q:** Combien coûtent les frais de dossier Campus France en Tunisie ?  
**A:** 400 DT depuis le 1er août 2025.  
**Source:** [fr-cft-frais-dossier](https://www.tunisie.campusfrance.org/proceder-au-paiement-des-frais-de-dossier): "Depuis le 01 août 2025, les frais de dossier sont au montant de 400 DT"  
**Fix:** 

### [x] q015 · cross_lingual · medium
**Q:** Can I pay my Campus France application fees by cheque or send my application by post?  
**A:** No. Postal applications and payments are no longer accepted, and cheque payment has been suspended since 20 January 2025. Pay by card at the Campus France office or online.  
**Source:** [fr-cft-frais-dossier](https://www.tunisie.campusfrance.org/proceder-au-paiement-des-frais-de-dossier): "Depuis le 20 janvier 2025, et jusqu'à nouvel ordre, le paiement par chèque est suspendu"  
**Source:** [fr-cft-frais-dossier](https://www.tunisie.campusfrance.org/proceder-au-paiement-des-frais-de-dossier): "Les candidatures et paiements par voie postale ne sont plus acceptés"  
**Fix:** 

### [x] q016 · number · easy
**Q:** Combien de temps dure l'entretien Campus France ?  
**A:** Environ 20 minutes.  
**Source:** [fr-cft-entretien](https://www.tunisie.campusfrance.org/l-entretien-campus-france): "L'entretien dure environ 20 minutes"  
**Fix:** 

### [x] q017 · fact · easy
**Q:** Combien de temps à l'avance dois-je arriver à l'espace Campus France le jour de mon entretien ?  
**A:** Une demi-heure à l'avance ; tout retard entraîne l'annulation de l'entretien.  
**Source:** [fr-cft-entretien](https://www.tunisie.campusfrance.org/l-entretien-campus-france): "une demi-heure à l'avance"  
**Fix:** 

### [x] q018 · cross_lingual · medium
**Q:** Are certified photocopies of my diplomas accepted at the Campus France interview?  
**A:** No. You must bring the originals (Arabic and French versions); photocopies and certified copies are not accepted.  
**Source:** [fr-cft-entretien](https://www.tunisie.campusfrance.org/l-entretien-campus-france): "les photocopies et copies conformes ne seront donc pas considérées par nos services"  
**Fix:** 

### [x] q019 · number · easy
**Q:** Combien de demandes de préinscription puis-je faire via Campus France pour un master ?  
**A:** Au maximum 15 demandes hors DAP. (En DAP : trois vœux d'universités et deux en écoles d'architecture.)  
**Source:** [fr-cft-faq-q32](https://www.tunisie.campusfrance.org/faq/combien-de-demandes-de-preinscription-puis-je-faire): "vous pouvez formuler un maximum de 15 demandes"  
**Fix:** 

### [x] q020 · number · easy
**Q:** Combien de temps dure le TCF pour la DAP ?  
**A:** 3 heures au total (1 h 30 d'épreuves de compréhension et de structures, 1 h 30 d'expression écrite).  
**Source:** [fr-cft-faq-q28](https://www.tunisie.campusfrance.org/faq/qu-est-ce-que-le-tcf-pour-la-dap): "Le TCF pour la DAP dure au total 3 heures"  
**Fix:** 

### [x] q021 · cross_lingual · hard
**Q:** Are Tunisian students exempt from the TCF-DAP French test since French is widely spoken in Tunisia?  
**A:** No. Tunisia's only official language is Arabic, so Tunisian candidates must take the TCF-DAP unless they hold another exemption, such as a DELF B2, a DALF C1/C2 or a French baccalauréat.  
**Source:** [fr-cft-faq-q27](https://www.tunisie.campusfrance.org/faq/puis-je-etre-dispensee-du-tcf-dap): "Les candidats de ces 4 pays sont donc concernés par le TCF-DAP"  
**Source:** [fr-cft-faq-q27](https://www.tunisie.campusfrance.org/faq/puis-je-etre-dispensee-du-tcf-dap): "vous êtes titulaire du DELF de niveau B2 ou du DALF niveau C1 ou C2"  
**Fix:** 

### [x] q022 · fact · medium
**Q:** Je candidate en master en France : où dois-je m'inscrire pour passer un test de français ?  
**A:** Il faut contacter directement l'antenne de l'Institut français de Tunisie la plus proche de chez vous (le TCF-DAP ne concerne que la licence 1/2 et les écoles d'architecture).  
**Source:** [fr-cft-faq-q29](https://www.tunisie.campusfrance.org/faq/je-dois-passer-un-test-de-francais-a-qui-dois-je-m-adresser-pour-m-inscrire): "contacter directement l'antenne de l'Institut français de Tunisie"  
**Fix:** 

### [x] q023 · date · medium
**Q:** Avant quelle date l'université de mon premier choix DAP doit-elle me répondre ?  
**A:** Avant le 30 avril (deuxième choix avant le 31 mai, troisième avant le 30 juin).  
**Source:** [fr-cft-faq-q16](https://www.tunisie.campusfrance.org/faq/quand-vais-je-recevoir-les-reponses-des-universites-aupres-desquelles-j-ai-depose-une): "Avant le 30 avril: l'université correspondant à votre premier choix"  
**Fix:** 

### [x] q024 · cross_lingual · hard
**Q:** What share of students admitted to French engineering programmes hold a DUT or BTS?  
**A:** About 12% (closer to 5% in the top grandes écoles d'ingénieurs).  
**Source:** [fr-cft-faq-q30](https://www.tunisie.campusfrance.org/faq/la-poursuite-d-etudes-apres-un-diplome-de-technicien-superieur-bts): "environ 12% des étudiants admis dans les formations d'ingénieurs"  
**Fix:** 

### [x] q025 · number · easy
**Q:** Combien de crédits ECTS valent une licence et un master en France ?  
**A:** Licence : 6 semestres, 180 ECTS ; master : 4 semestres, 120 ECTS.  
**Source:** [fr-cft-lmd-equivalence](https://www.tunisie.campusfrance.org/diplome-francais-systeme-lmd-et-equivalence-0): "Licence (L) = 6 semestres = 180 ECTS"  
**Source:** [fr-cft-lmd-equivalence](https://www.tunisie.campusfrance.org/diplome-francais-systeme-lmd-et-equivalence-0): "Master (M) = 4 semestres = 120 ECTS"  
**Fix:** 

### [x] q026 · number · easy
**Q:** How much are tuition fees for a Master's at a French public university for a non-EU student in 2026-2027?  
**A:** €3,950 per year.  
**Source:** [fr-cf-tuition-fees](https://www.campusfrance.org/en/tuition-fees-France): "€3,950 per year for a Master's degree program"  
**Fix:** 

### [x] q027 · cross_lingual · medium
**Q:** Quels sont les frais d'inscription en licence et en doctorat pour un étudiant non européen en France en 2026-2027 ?  
**A:** 2 902 € par an en licence et 398 € par an en doctorat.  
**Source:** [fr-cf-tuition-fees](https://www.campusfrance.org/en/tuition-fees-France): "€2,902 per year for a Bachelor's degree program"  
**Source:** [fr-cf-tuition-fees](https://www.campusfrance.org/en/tuition-fees-France): "€398 per year for a Doctoral (PhD) program"  
**Fix:** 

### [x] q028 · yes_no · medium
**Q:** Do non-EU PhD students in France pay the higher differentiated tuition fees?  
**A:** No. Doctoral programmes are not subject to differentiated tuition fees.  
**Source:** [fr-cf-tuition-fees](https://www.campusfrance.org/en/tuition-fees-France): "Doctoral (PhD) programs are not subject to these differentiated tuition fees"  
**Fix:** 

### [x] q029 · number · easy
**Q:** How much is the CVEC for the 2026/27 academic year?  
**A:** €105, paid once per academic year.  
**Source:** [fr-cf-cvec](https://www.campusfrance.org/en/10-things-you-need-to-know-about-the-student-and-campus-life-contribution-cvec): "2026/27 academic year is €105"  
**Fix:** 

### [x] q030 · cross_lingual · hard
**Q:** Si j'ai une bourse du gouvernement tunisien, suis-je exonéré de la CVEC ?  
**A:** Non. Les étudiants qui reçoivent une bourse d'un gouvernement étranger ne sont pas exonérés de la CVEC.  
**Source:** [fr-cf-cvec](https://www.campusfrance.org/en/10-things-you-need-to-know-about-the-student-and-campus-life-contribution-cvec): "Students receiving foreign government scholarships"  
**Fix:** 

### [x] q031 · fact · medium
**Q:** How can I get a refund of the CVEC if I become exempt during the year?  
**A:** Apply to CROUS before 31 May of the academic year concerned.  
**Source:** [fr-cf-cvec](https://www.campusfrance.org/en/10-things-you-need-to-know-about-the-student-and-campus-life-contribution-cvec): "apply to CROUS before May 31 of the academic year"  
**Fix:** 

### [x] q032 · number · easy
**Q:** What is the age limit for the Eiffel scholarship?  
**A:** Up to 29 years old at master's level and up to 35 at PhD level.  
**Source:** [fr-cf-eiffel](https://www.campusfrance.org/en/france-excellence-eiffel-scholarship-program): "up to 29 years old at master's level, and applicants up to 35 years old at PhD level"  
**Fix:** 

## Part 2 (q033–q064), reviewer: ______

### [x] q033 · cross_lingual · medium
**Q:** Est-ce que je peux postuler moi-même à la bourse Eiffel ?  
**A:** Non. Seules les candidatures déposées par les établissements d'enseignement supérieur français sont acceptées ; il faut passer par l'établissement visé.  
**Source:** [fr-cf-eiffel](https://www.campusfrance.org/en/france-excellence-eiffel-scholarship-program): "Only applications submitted by French higher education institutions are accepted"  
**Fix:** 

### [x] q034 · stale · hard
**Q:** Quelle est la date limite pour la bourse Eiffel ?  
**A:** Le corpus ne décrit que la campagne 2026 : réception des candidatures par Campus France jusqu'au 8 janvier 2026 (ouverture le 1er octobre 2025). Le calendrier de la campagne suivante n'y figure pas ; il faut le vérifier sur le site de Campus France.  
**Source:** [fr-cf-eiffel](https://www.campusfrance.org/en/france-excellence-eiffel-scholarship-program): "Deadline for the reception of applications by Campus France: January 8, 2026 included"  
**Note:** Tests whether the answer flags that the only date available is for an earlier campaign.  
**Fix:** 

### [x] q035 · fact · easy
**Q:** Où un étudiant étranger peut-il consulter un médecin dans son université en France ?  
**A:** Au service de santé universitaire, le SUMPPS (Service universitaire de Médecine préventive et de Promotion de la Santé), où certaines consultations sont gratuites.  
**Source:** [fr-cft-sante](https://www.tunisie.campusfrance.org/sante-securite-sociale-et-mutuelle-0): "Service universitaire de Médecine préventive et de Promotion de la Santé (SUMPPS)"  
**Fix:** 

### [x] q036 · number · hard
**Q:** Quel salaire minimum faut-il pour obtenir une carte de séjour après les études en France avec un contrat de plus de 3 mois, et combien de temps est-elle valable ?  
**A:** Une rémunération brute annuelle d'au moins 1,5 fois le SMIC, soit 42 243 € bruts annuels en 2025 ; la carte est valable 4 ans maximum et renouvelable.  
**Source:** [fr-cft-travail-apres](https://www.tunisie.campusfrance.org/travailler-en-france-apres-mes-etudes): "42 243 € bruts annuels en 2025"  
**Source:** [fr-cft-travail-apres](https://www.tunisie.campusfrance.org/travailler-en-france-apres-mes-etudes): "Cette carte est valable 04 ans maximum et renouvelable"  
**Fix:** 

### [x] q037 · number · medium
**Q:** Combien d'heures maximum un étudiant peut-il travailler dans un emploi étudiant à l'université entre septembre et juin ?  
**A:** 670 heures entre le 1er septembre et le 30 juin (et 300 heures entre le 1er juillet et le 31 août).  
**Source:** [fr-cft-travail-etudes](https://www.tunisie.campusfrance.org/travailler-durant-mes-etudes-0): "La durée effective de travail n'excède pas 670 heures entre le 1er septembre et le 30 juin"  
**Fix:** 

### [x] q038 · cross_lingual · medium
**Q:** Do I have to go through Campus France to book my French student visa appointment at TLScontact?  
**A:** Yes. Since 1 May 2022, students in the Campus France procedure must book their TLScontact visa appointment through their Campus France office, after filling in the France-Visas form.  
**Source:** [fr-cft-vls-ts](https://www.tunisie.campusfrance.org/visa-etudiant-vls-ts): "Depuis le 01 mai 2022, les étudiants et demandeurs concernés par la procédure Campus France doivent obligatoirement passer par l'espace Campus France"  
**Fix:** 

### [x] q039 · number · easy
**Q:** Quelle est la durée de validité d'un visa de long séjour pour la France ?  
**A:** Entre 3 mois et un an ; au-delà, il faut demander un titre de séjour en préfecture.  
**Source:** [fr-fv-long-sejour](https://france-visas.gouv.fr/visa-de-long-sejour): "le visa de long séjour a une durée limitée comprise entre 3 mois et un an"  
**Fix:** 

### [x] q040 · number · medium
**Q:** Combien d'étudiants tunisiens étudient en France et en Allemagne selon la fiche mobilité de Campus France ?  
**A:** 10 068 en France et 7 062 en Allemagne (chiffres 2022 de la fiche mobilité Tunisie 2023-2024).  
**Source:** [fr-cft-statistiques-pdf](https://www.tunisie.campusfrance.org/system/files/medias/documents/2024-09/Statistiques_TN_20232024.pdf): "France 10 068 Allemagne 7 062 Canada 1 290"  
**Fix:** 

### [x] q041 · date · easy
**Q:** À partir de quand faut-il candidater sur la nouvelle plateforme « Études en France » ?  
**A:** À partir du 1er octobre 2026, sur https://etudesenfrance.diplomatie.gouv.fr/.  
**Source:** [fr-cft-plateforme-eef](https://www.tunisie.campusfrance.org/candidater-sur-la-nouvelle-plateforme-etudes-en-france): "A compter du 01 octobre 2026, candidatez sur la nouvelle plateforme"  
**Fix:** 

### [x] q042 · cross_lingual · easy
**Q:** I forgot my Études en France password. What should I do?  
**A:** On the Études en France site, click 'mot de passe oublié', enter your account e-mail, then open the link you receive to set a new password. Check your spam folder if the e-mail doesn't arrive.  
**Source:** [fr-cft-faq-q36](https://www.tunisie.campusfrance.org/faq/je-n-arrive-pas-a-retrouver-mon-login-et-mon-mot-de-passe-que-faire): "mot de passe oublié"  
**Fix:** 

### [x] q043 · number · easy
**Q:** Combien d'argent faut-il prévoir sur le compte bloqué pour un visa étudiant en Allemagne ?  
**A:** 11 904 EUR pour une année d'études, soit 992 EUR par mois.  
**Source:** [de-amb-etudes](https://tunis.diplo.de/tn-fr/service/05-visaeinreise/2573172-2573172): "11.904 EUR (992 EUR par mois)"  
**Source:** [de-amb-preparation-etudes](https://tunis.diplo.de/tn-fr/service/05-visaeinreise/2573166-2573166): "11.904 EUR"  
**Fix:** 

### [x] q044 · conflict · hard
**Q:** How much money do I need in a German blocked account for a student visa?  
**A:** €11,904 per year (€992 per month), according to the embassy's current pages. An older embassy PDF checklist from 2020 still gives €10,332, which is outdated.  
**Source:** [de-amb-etudes](https://tunis.diplo.de/tn-fr/service/05-visaeinreise/2573172-2573172): "11.904 EUR (992 EUR par mois)"  
**Outdated source:** [de-amb-preparation-etudes-pdf](https://tunis.diplo.de/resource/blob/1684456/07ce3a90734df1f243e801db5d3539e3/pr%C3%A9paration-aux-%C3%A9tudes-data.pdf): "10.332,00 €"  
**Fix:** 

### [x] q045 · stale · hard
**Q:** Quelles sont les conditions de financement et de durée de cours pour un visa « cours de langue » en Allemagne ?  
**A:** Selon la liste de l'ambassade (décembre 2022) : une inscription à un cours d'au moins 20 heures par semaine et un compte bloqué d'au moins 1027 €/mois. Le document date de 2022 ; le montant est à vérifier.  
**Source:** [de-amb-cours-langue-pdf](https://tunis.diplo.de/resource/blob/2103598/115ab3c48d59f598a288dea0ea10b3b0/d16-cours-de-langue-data.pdf): "cours de 20 heures par semaines au minimum"  
**Source:** [de-amb-cours-langue-pdf](https://tunis.diplo.de/resource/blob/2103598/115ab3c48d59f598a288dea0ea10b3b0/d16-cours-de-langue-data.pdf): "un compte bloqué au moins 1027 €/ mois"  
**Note:** The source PDF dates from December 2022; the expected answer should mention that.  
**Fix:** 

### [x] q046 · number · easy
**Q:** Combien de photos d'identité et quelle validité de passeport faut-il pour un visa d'études en Allemagne ?  
**A:** 3 photos d'identité biométriques et un passeport valable au moins 6 mois.  
**Source:** [de-amb-etudes](https://tunis.diplo.de/tn-fr/service/05-visaeinreise/2573172-2573172): "3 photos d'identité biométrique"  
**Source:** [de-amb-etudes](https://tunis.diplo.de/tn-fr/service/05-visaeinreise/2573172-2573172): "passeport du demandeur en cours de validité (minimum 6 mois)"  
**Fix:** 

### [x] q047 · cross_lingual · medium
**Q:** Which language certificates does the German embassy in Tunis accept for a student visa?  
**A:** DSH or TestDaF for programmes taught in German; IELTS, TOEFL or others for programmes taught in English.  
**Source:** [de-amb-etudes](https://tunis.diplo.de/tn-fr/service/05-visaeinreise/2573172-2573172): "pour des études enseignées en langue allemande: DSH ou TestDaF"  
**Source:** [de-amb-etudes](https://tunis.diplo.de/tn-fr/service/05-visaeinreise/2573172-2573172): "pour des études enseignées en langue anglaise: IELTS, TOEFL"  
**Fix:** 

### [x] q048 · fact · medium
**Q:** Si j'arrive en Allemagne avant mon immatriculation, quelle assurance maladie dois-je avoir ?  
**A:** Une assurance maladie privée pour 90 jours à compter de l'arrivée, car l'assurance légale n'est possible qu'après l'immatriculation.  
**Source:** [de-amb-etudes](https://tunis.diplo.de/tn-fr/service/05-visaeinreise/2573172-2573172): "assurance maladie privée pour 90 jours à compter de votre arrivée"  
**Fix:** 

### [x] q049 · yes_no · easy
**Q:** Puis-je agrafer ou relier mon dossier de visa étudiant allemand déposé chez TLScontact ?  
**A:** Non, le dossier ne doit être ni agrafé ni relié.  
**Source:** [de-amb-etudes](https://tunis.diplo.de/tn-fr/service/05-visaeinreise/2573172-2573172): "il ne doit pas être agrafé ni relié"  
**Fix:** 

### [x] q050 · cross_lingual · medium
**Q:** Do translations for my German visa application have to be done by a sworn translator?  
**A:** No. For the visa procedure, translations by local non-sworn translators are enough; the embassy no longer keeps its own translator list.  
**Source:** [de-amb-traducteurs](https://tunis.diplo.de/tn-fr/service/1515196-1515196): "il suffit de présenter des traductions faites par des traducteurs locaux non assermentés"  
**Fix:** 

### [x] q051 · number · easy
**Q:** Combien d'universités allemandes acceptent les candidatures de l'étranger via uni-assist ?  
**A:** Environ 180 universités.  
**Source:** [de-amb-faq-visas](https://tunis.diplo.de/tn-fr/service/05-visaeinreise/1672718-1672718): "Environ 180 universités allemandes acceptent les candidatures de l'étranger"  
**Fix:** 

### [x] q052 · number · medium
**Q:** Pour un visa de stage de recherche en Allemagne, combien de temps mon passeport doit-il encore être valable ?  
**A:** Au moins 3 mois après la date de retour.  
**Source:** [de-amb-stage-recherche](https://tunis.diplo.de/tn-fr/service/05-visaeinreise/2585062-2585062): "le passeport doit être en cours de validité minimum 3 mois après la date de retour"  
**Fix:** 

### [x] q053 · yes_no · medium
**Q:** Does the German Federal Foreign Office recommend a specific blocked account provider?  
**A:** No. It makes no recommendations and accepts no liability for providers; its old list of providers (until mid-2022) has been deleted.  
**Source:** [de-aa-compte-bloque](https://www.auswaertiges-amt.de/en/sperrkonto-388600): "The Federal Foreign Office does not make any recommendations"  
**Source:** [de-aa-compte-bloque](https://www.auswaertiges-amt.de/en/sperrkonto-388600): "The list of providers offering blocked accounts available up until the middle of 2022 has now been deleted"  
**Fix:** 

### [x] q054 · fact · easy
**Q:** Qui peut postuler au programme KOSPIE du DAAD et en quoi consiste-t-il ?  
**A:** Les étudiants tunisiens en ingénierie ou en informatique inscrits en deuxième année du cycle d'ingénieur ; la bourse finance un séjour de six mois dans une université allemande pour réaliser le projet de fin d'études.  
**Source:** [de-daad-kospie-2027](https://www.daad.tn/fr/2026/03/16/appel-a-candidatures-sejours-detudes-et-pratiques-combines-pour-les-ingenieurs-tunisiens-pour-2027-kospie/): "actuellement inscrits en deuxième année du cycle d'ingénieur"  
**Source:** [de-daad-kospie-2027](https://www.daad.tn/fr/2026/03/16/appel-a-candidatures-sejours-detudes-et-pratiques-combines-pour-les-ingenieurs-tunisiens-pour-2027-kospie/): "un séjour de six mois dans une université allemande afin de réaliser un projet de fin d'études"  
**Fix:** 

### [x] q055 · cross_lingual · medium
**Q:** How do I apply for the KOSPIE scholarship?  
**A:** Through the DAAD scholarship database, which also gives the application details.  
**Source:** [de-daad-kospie-2027](https://www.daad.tn/fr/2026/03/16/appel-a-candidatures-sejours-detudes-et-pratiques-combines-pour-les-ingenieurs-tunisiens-pour-2027-kospie/): "La procédure de candidature fonctionne par le biais de notre base de données des bourses d'études"  
**Fix:** 

### [x] q056 · date · medium
**Q:** Quelle est la durée minimale des cours d'été universitaires financés par le DAAD et quelle était la date limite de candidature ?  
**A:** Au moins 18 jours de cours (25 heures par semaine, généralement entre juin et septembre) ; date limite : 30 octobre 2025.  
**Source:** [de-daad-hsk-2026](https://www.daad.tn/fr/2025/09/11/aac-hsk-2026/): "au moins 18 jours de cours"  
**Source:** [de-daad-hsk-2026](https://www.daad.tn/fr/2025/09/11/aac-hsk-2026/): "Date limite de candidature : 30 Octobre 2025"  
**Fix:** 

### [x] q057 · date · medium
**Q:** Quel niveau d'allemand faut-il pour le programme VORsprung et quelle était la date limite ?  
**A:** Au moins B1.2 ; date limite le 15 janvier 2026 (23h59 CET).  
**Source:** [de-daad-vorsprung-2025](https://www.daad.tn/fr/2025/09/09/aac-vorsprung-f2/): "un niveau d'allemand d'au moins B1.2"  
**Source:** [de-daad-vorsprung-2025](https://www.daad.tn/fr/2025/09/09/aac-vorsprung-f2/): "Date limite de candidature : 15 janvier 2026"  
**Fix:** 

### [x] q058 · date · easy
**Q:** Quand a eu lieu le séminaire en ligne du DAAD Tunis sur le doctorat en Allemagne ?  
**A:** Le 21 mai 2026, de 14h00 à 15h00 (heure tunisienne), en anglais.  
**Source:** [de-daad-doctorat-2026](https://www.daad.tn/fr/2026/05/13/sl-faire-un-doctorat-en-allemagne/): "Le 21 mai 2026, de 14h00 à 15h00"  
**Fix:** 

### [x] q059 · list · easy
**Q:** En quelles langues sont disponibles les brochures du DAAD pour les parents ?  
**A:** En allemand, anglais, français et arabe.  
**Source:** [de-daad-parents-15-questions](https://www.daad.tn/fr/etudier-et-faire-de-la-recherche-en-allemagne/etudier-en-allemagne/pour-les-parents-15-questions-et-reponses/): "Les brochures sont disponibles en allemand, anglais, français et arabe"  
**Fix:** 

### [x] q060 · number · easy
**Q:** Combien de cours de langue et cours spécialisés en Allemagne le DAAD recense-t-il ?  
**A:** Plus de 350 cours, surtout en été.  
**Source:** [de-daad-allemand-allemagne](https://www.daad.tn/fr/etudier-et-faire-de-la-recherche-en-allemagne/apprendre-lallemand/apprendre-lallemand-en-allemagne/): "Vous avez le choix entre plus de 350 cours"  
**Fix:** 

### [x] q061 · number · easy
**Q:** How much is the Deutschlandstipendium per month?  
**A:** 300 EUR per month, for at least 2 semesters (about 34,000 students received it in 2025).  
**Source:** [de-daaddb-10000207](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000207): "300 EUR each month"  
**Fix:** 

### [x] q062 · number · easy
**Q:** How much does the Friedrich Ebert Foundation pay international scholarship holders per month?  
**A:** A monthly base amount of 992 EUR, plus health insurance costs; it does not have to be repaid.  
**Source:** [de-daaddb-10000153](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000153): "International students receive a monthly base amount of 992 EUR"  
**Fix:** 

### [x] q063 · cross_lingual · medium
**Q:** Quelles sont les dates limites de candidature pour la bourse d'études de la fondation Heinrich Böll ?  
**A:** Le 1er mars et le 1er septembre de chaque année.  
**Source:** [de-daaddb-10000124](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000124): "1 March and 1 September of each year"  
**Fix:** 

### [x] q064 · number · medium
**Q:** How much does the Hertie School Human Rights Scholarship cover?  
**A:** The full tuition fees of the Master of International Affairs, up to 38,500 EUR; 2 scholarships are offered.  
**Source:** [de-daaddb-10000429](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000429): "up to the value of 38,500 EUR"  
**Fix:** 

## Part 3 (q065–q095), reviewer: ______

### [x] q065 · date · medium
**Q:** What is the deadline for the RWTH Women in Engineering Scholarship for a Tunisian applicant?  
**A:** 1 March (the deadline for non-EU applicants), with a 500-word scholarship motivation letter.  
**Source:** [de-daaddb-10000422](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000422): "The deadline is 1 March for non-European and 15 July for European applicants"  
**Source:** [de-daaddb-10000422](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000422): "scholarship motivation letter of 500 words"  
**Fix:** 

### [x] q066 · number · medium
**Q:** What are the age and German language requirements for the Bundestag International Parliamentary Scholarship?  
**A:** Under 35 at the start of the scholarship and at least B2 German.  
**Source:** [de-daaddb-10000398](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000398): "under the age of 35 at the start of the scholarship"  
**Source:** [de-daaddb-10000398](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000398): "very good knowledge of the German language, at least B2 level"  
**Fix:** 

### [x] q067 · number · hard
**Q:** What does every Foundation of German Business (sdw) scholarship holder receive regardless of family income?  
**A:** A study allowance of 300 EUR per month that is not means-tested (living support of up to 855 EUR depends on family finances).  
**Source:** [de-daaddb-10000119](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000119): "not means-tested study allowance of 300 EUR per month"  
**Fix:** 

### [x] q068 · cross_lingual · medium
**Q:** Combien rapporte par mois la bourse Baden-Württemberg-STIPENDIUM ?  
**A:** Entre 800 EUR et 1 400 EUR par mois selon l'établissement et l'avancement des études.  
**Source:** [de-daaddb-10000178](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000178): "between 800 EUR and 1,400 EUR per month"  
**Fix:** 

### [x] q069 · number · medium
**Q:** What German level is required for the Bavarian Max Weber Programme, and what does it pay?  
**A:** At least B2/C1 German; it pays a semester allowance of 1,800 EUR plus funding for study projects abroad.  
**Source:** [de-daaddb-10000101](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000101): "at least B2 / C1"  
**Source:** [de-daaddb-10000101](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000101): "semester allowance of 1,800 EUR"  
**Fix:** 

### [x] q070 · yes_no · medium
**Q:** Can I apply directly to IAESTE for a technical internship in Germany as an individual?  
**A:** No. IAESTE internships are offered only through the IAESTE national committee in your home country, not to individual applicants.  
**Source:** [de-daaddb-57352834](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=57352834): "The IAESTE programme offers no internships to individual applicants outside this procedure"  
**Fix:** 

### [x] q071 · number · hard
**Q:** How much and for how long does the Mecklenburg-Western Pomerania doctoral scholarship pay?  
**A:** 1,500 EUR per month as standard funding, generally for up to 3 years (extendable by up to 6 months).  
**Source:** [de-daaddb-10000107](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000107): "standard funding: 1,500 EUR per month"  
**Source:** [de-daaddb-10000107](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000107): "Funding for doctoral candidates generally ends after 3 years"  
**Fix:** 

### [x] q072 · fact · hard
**Q:** With a DAAD Doctoral Programmes scholarship, can I spend part of my PhD outside Germany?  
**A:** Yes, if it is critical for the doctorate, but such visits must be no more than one quarter of the total funding period.  
**Source:** [de-daaddb-57135739](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=57135739): "no more than one quarter of the anticipated total funding period"  
**Fix:** 

### [x] q073 · cross_lingual · medium
**Q:** Qui finance les bourses DAAD « Doctoral Programmes in Germany » ?  
**A:** Le ministère fédéral allemand des Affaires étrangères (German Federal Foreign Office).  
**Source:** [de-daaddb-57135739](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=57135739): "The scholarships are funded by the German Federal Foreign Office"  
**Fix:** 

### [x] q074 · yes_no · medium
**Q:** Does the KAAD scholarship fund German language courses?  
**A:** Yes. Funding can be requested for a language course of up to 6 months (full-time or during studies), and candidates are expected to do preparatory German courses at home.  
**Source:** [de-daaddb-10000168](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000168): "it is possible to apply for funding for a language course of up to 6 months"  
**Fix:** 

### [x] q075 · conflict · hard
**Q:** How much money do I need to show for living expenses for a Canadian study permit if I'm coming alone (not to Quebec)?  
**A:** If you apply on or after 1 September 2026: CAN$23,448 for the first year, excluding tuition and travel. The earlier amount was CAN$22,895. Quebec has its own requirements (CAQ).  
**Source:** [ca-ircc-financial-support](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/get-documents/financial-support.html): "If you apply on or after September 1, 2026"  
**Source:** [ca-ircc-financial-support](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/get-documents/financial-support.html): "| 1 | $23,448 |"  
**Outdated source:** [ca-ircc-financial-support](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/get-documents/financial-support.html): "| 1 | $22,895 |"  
**Note:** The page lists two tables; the answer depends on the application date.  
**Fix:** 

### [x] q076 · number · easy
**Q:** How many hours per week can I work off campus in Canada during the school term?  
**A:** Up to 24 hours per week during regular school terms.  
**Source:** [ca-ircc-work-off-campus](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work/work-off-campus.html): "You can work up to 24 hours per week"  
**Fix:** 

### [x] q077 · cross_lingual · medium
**Q:** Combien d'heures par semaine puis-je travailler hors campus au Canada pendant les cours ?  
**A:** Jusqu'à 24 heures par semaine pendant les sessions régulières.  
**Source:** [ca-ircc-work-off-campus](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work/work-off-campus.html): "You can work up to 24 hours per week"  
**Fix:** 

### [x] q078 · number · easy
**Q:** How long after graduating do I have to apply for a post-graduation work permit (PGWP) in Canada?  
**A:** Up to 180 days after graduating.  
**Source:** [ca-ircc-pgwp-apply](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work/after-graduation/apply.html): "You have up to 180 days after you graduate to apply for a PGWP"  
**Fix:** 

### [x] q079 · number · easy
**Q:** How much is the fee for a post-graduation work permit?  
**A:** CAN$255.  
**Source:** [ca-ircc-pgwp](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work/after-graduation.html): "PGWP: $255"  
**Fix:** 

### [x] q080 · cross_lingual · medium
**Q:** Combien coûtent les données biométriques pour une demande canadienne individuelle ?  
**A:** 85 CAD pour un demandeur individuel (170 CAD maximum pour une famille).  
**Source:** [ca-ircc-pgwp-apply](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work/after-graduation/apply.html): "Individual applicant: CAD $85"  
**Fix:** 

### [x] q081 · number · medium
**Q:** What is the minimum length of a study programme to be eligible for a PGWP?  
**A:** The programme must have been full-time and 8 months or longer.  
**Source:** [ca-ircc-pgwp-documents](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work/after-graduation/get-documents.html): "a program that was 8 months or longer"  
**Fix:** 

### [x] q082 · yes_no · medium
**Q:** Do I need a provincial attestation letter (PAL) to apply for a Canadian study permit for a master's at a public university?  
**A:** No. Since 1 January 2026, master's and doctoral students in degree-granting programmes at public institutions don't need a PAL/TAL (Quebec still has its own requirements).  
**Source:** [ca-ircc-graduate-apply](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/graduate-student/how-to-apply.html): "Starting January 1, 2026, if you're planning to attend a degree-granting program at the master's or doctoral level at a public institution, you don't need a provincial or territorial attestation letter"  
**Fix:** 

### [x] q083 · cross_lingual · medium
**Q:** Combien de temps prend le traitement d'un permis d'études canadien pour un doctorant ?  
**A:** Environ 2 semaines grâce au traitement accéléré pour les doctorants (après vérification de la lettre d'acceptation par l'établissement, qui peut prendre jusqu'à 10 jours).  
**Source:** [ca-ircc-graduate-student](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/graduate-student.html): "Get your application processed in 2 weeks if you're a doctoral student"  
**Fix:** 

### [x] q084 · number · easy
**Q:** How long is a Canadian study permit usually valid?  
**A:** For the length of the study programme plus an extra 90 days.  
**Source:** [ca-ircc-while-you-study](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/while-you-study.html): "A study permit is usually valid for the length of your study program, plus an extra 90 days"  
**Fix:** 

### [x] q085 · number · easy
**Q:** When must I apply to extend my Canadian study permit?  
**A:** At least 30 days before the original expiry date.  
**Source:** [ca-ircc-extend-when](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/extend-study-permit/when-to-apply.html): "You must apply to extend your study permit at least 30 days before the original expiry date"  
**Fix:** 

### [x] q086 · yes_no · hard
**Q:** Can I work in Canada during an authorized leave from my studies, and how long can the leave be?  
**A:** No, you can't work on or off campus during an authorized leave, and the leave can't be longer than 150 days.  
**Source:** [ca-ircc-permit-conditions](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/while-you-study/study-permit-conditions.html): "no longer than 150 days"  
**Source:** [ca-ircc-permit-conditions](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/while-you-study/study-permit-conditions.html): "You can't work on or off campus during an authorized leave"  
**Fix:** 

### [x] q087 · cross_lingual · hard
**Q:** Si je change d'établissement au Canada, ai-je besoin d'une nouvelle lettre d'attestation provinciale ?  
**A:** Oui, sauf exception : depuis le 22 janvier 2025, il faut une nouvelle PAL/TAL valide pour changer d'établissement ou de niveau d'études.  
**Source:** [ca-ircc-change-schools](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/change-schools.html): "This is a new requirement as of January 22, 2025"  
**Source:** [ca-ircc-extend-how](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/extend-study-permit/how-to-apply.html): "you need to provide a new PAL or TAL if you're changing schools or levels of study"  
**Fix:** 

### [x] q088 · number · medium
**Q:** How fast is a study permit extension processed if I'm changing to a new post-secondary school in Canada?  
**A:** In 60 days, if you follow the instructions for faster processing.  
**Source:** [ca-ircc-extend-when](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/extend-study-permit/when-to-apply.html): "processed in 60 days if you're changing to a new post-secondary DLI"  
**Fix:** 

### [x] q089 · date · medium
**Q:** Until when is a PAL issued in 2026 valid?  
**A:** Until 31 December 2026 (unless it shows an earlier expiry date); a PAL from a previous cap year can't be used.  
**Source:** [ca-ircc-pal](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/get-documents/provincial-attestation-letter.html): "until December 31, 2026, for the 2026 study permit cap year"  
**Fix:** 

### [x] q090 · yes_no · medium
**Q:** Do I need a co-op work permit for an internship that is part of my Canadian college or university programme?  
**A:** No. Since 1 April 2026, post-secondary international students don't need a co-op work permit for student work placements such as co-op placements or internships.  
**Source:** [ca-ircc-work](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work.html): "As of April 1, 2026, post-secondary international students don't need a co-op work permit"  
**Fix:** 

### [x] q091 · yes_no · medium
**Q:** Can I start working in Canada as soon as I arrive, before my classes start?  
**A:** No. You can't work on or off campus until you begin your studies in Canada.  
**Source:** [ca-ircc-prepare-arrival](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/prepare-arrival.html): "You are not allowed to work on or off campus until you begin your studies in Canada"  
**Fix:** 

### [x] q092 · fact · easy
**Q:** What is a SIN and do I need one to work in Canada as a student?  
**A:** A social insurance number, a 9-digit number from the Government of Canada; you need one to work in Canada, and your study permit must show the right work condition to get it.  
**Source:** [ca-ircc-work-off-campus](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work/work-off-campus.html): "is a 9-digit number that the Government of Canada gives you"  
**Fix:** 

### [x] q093 · fact · medium
**Q:** Are Tunisian students eligible for the Study in Canada Scholarships, and can I apply myself?  
**A:** Tunisia is an eligible country, but individuals can't apply directly: a Canadian post-secondary institution selects the students and applies.  
**Source:** [ca-edu-study-in-canada-sep](https://www.educanada.ca/scholarships-bourses/can/institutions/study-in-canada-sep-etudes-au-canada-pct.aspx?lang=eng): "Middle East and North Africa: Algeria, Egypt, Jordan, Morocco, Tunisia"  
**Source:** [ca-edu-study-in-canada-sep](https://www.educanada.ca/scholarships-bourses/can/institutions/study-in-canada-sep-etudes-au-canada-pct.aspx?lang=eng): "Direct applications from individuals are not accepted"  
**Fix:** 

### [x] q094 · cross_lingual · medium
**Q:** Combien vaut une bourse Study in Canada pour un séjour de 5 à 6 mois en master ?  
**A:** 14 000 $ CA pour 5 à 6 mois d'études ou de recherche au niveau master ou doctorat (10 200 $ CA pour 4 mois).  
**Source:** [ca-edu-study-in-canada-sep](https://www.educanada.ca/scholarships-bourses/can/institutions/study-in-canada-sep-etudes-au-canada-pct.aspx?lang=eng): "$14,000 for 5 to 6 months for study or research at the graduate level"  
**Fix:** 

### [x] q095 · yes_no · hard
**Q:** Can I keep working in Canada while my PGWP application is being processed?  
**A:** Yes, full-time, if you had a valid study permit when you applied, completed your programme, and were eligible to work off campus without exceeding your allowed hours.  
**Source:** [ca-ircc-pgwp-path-to-pr](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work/after-graduation/path-to-pr.html): "You can work full-time until we make a decision on your work permit application"  
**Fix:** 

## Part 4 (q096–u015), reviewer: ______

### [x] q096 · fact · medium
**Q:** What extra document do I need to study in Quebec?  
**A:** A Quebec Acceptance Certificate (Certificat d'acceptation du Québec, CAQ), with Quebec's own financial requirements.  
**Source:** [ca-ircc-financial-support](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/get-documents/financial-support.html): "To obtain a Quebec Acceptance Certificate (Certificat d'acceptation du Québec [CAQ]) and study in Quebec"  
**Fix:** 

### [x] q097 · number · hard
**Q:** How long can it take my Canadian school to confirm my letter of acceptance for faster doctoral processing?  
**A:** Up to 10 calendar days; after that, IRCC aims to process the application within 2 weeks.  
**Source:** [ca-ircc-graduate-faster](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/graduate-student/faster-processing.html): "This can take up to 10 calendar days"  
**Fix:** 

### [x] q098 · number · easy
**Q:** How long does an Erasmus Mundus Joint Master last?  
**A:** 1 to 2 academic years (60, 90 or 120 ECTS credits).  
**Source:** [eu-emjm-students](https://erasmus-plus.ec.europa.eu/opportunities/individuals/students/erasmus-mundus-joint-masters): "1 to 2 academic years (60, 90 or 120 ECTS credits)"  
**Fix:** 

### [x] q099 · cross_lingual · medium
**Q:** Quand faut-il postuler à un master Erasmus Mundus ?  
**A:** En général entre octobre et janvier, pour une rentrée l'année académique suivante.  
**Source:** [eu-emjm-students](https://erasmus-plus.ec.europa.eu/opportunities/individuals/students/erasmus-mundus-joint-masters): "you should submit your application between October and January"  
**Fix:** 

### [x] q100 · fact · easy
**Q:** Where do I send my application for an Erasmus Mundus Joint Master?  
**A:** Directly to the institution (consortium) running the chosen programme.  
**Source:** [eu-emjm-students](https://erasmus-plus.ec.europa.eu/opportunities/individuals/students/erasmus-mundus-joint-masters): "Students apply directly to the institution running their chosen programme"  
**Fix:** 

### [x] q101 · number · easy
**Q:** How many universities and countries are involved in an Erasmus Mundus Joint Master?  
**A:** At least 3 institutions from at least 3 different countries.  
**Source:** [eu-emjm-students](https://erasmus-plus.ec.europa.eu/opportunities/individuals/students/erasmus-mundus-joint-masters): "They involve at least 3 institutions from at least 3 different countries"  
**Fix:** 

### [x] q102 · cross_lingual · medium
**Q:** Puis-je postuler à un master Erasmus Mundus si je suis encore en dernière année de licence ?  
**A:** Oui, à condition d'obtenir la licence avant le début du master.  
**Source:** [eu-emjm-students](https://erasmus-plus.ec.europa.eu/opportunities/individuals/students/erasmus-mundus-joint-masters): "or be in your last year of bachelor studies"  
**Fix:** 

### [x] q103 · fact · medium
**Q:** Is there an Erasmus Mundus master in cybersecurity?  
**A:** Yes, for example CYBERSURE (Programme in Cybersecurity and Assurance).  
**Source:** [eu-eacea-mundus-catalogue](https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus-catalogue_en): "Programme in Cybersecurity and Assurance CYBERSURE"  
**Fix:** 

### [x] q104 · cross_lingual · medium
**Q:** Existe-t-il un master Erasmus Mundus en data engineering et intelligence artificielle ?  
**A:** Oui, par exemple DEAI (Data Engineering and Artificial Intelligence).  
**Source:** [eu-eacea-mundus-catalogue](https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus-catalogue_en): "Data Engineering and Artificial Intelligence DEAI"  
**Fix:** 

### [x] q105 · list · hard
**Q:** Which Erasmus Mundus masters deal with renewable energy?  
**A:** For example REM Plus Plus (Renewable Energy in the Marine environment), EU-CORE (control of renewable energy systems) and RESCO (Renewable Energy and Sustainable Construction).  
**Source:** [eu-eacea-mundus-catalogue](https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus-catalogue_en): "Renewable Energy in the Marine environment REM Plus Plus"  
**Source:** [eu-eacea-mundus-catalogue-p4](https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus-catalogue_en?page=3): "EUropean master on COntrol of Renewable Energy systems EU-CORE"  
**Source:** [eu-eacea-mundus-catalogue](https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus-catalogue_en): "Renewable Energy and Sustainable COnstruction"  
**Note:** Answer spans several catalogue pages; a good test for retrieval depth.  
**Fix:** 

### [x] q106 · number · hard
**Q:** What travel grant does Erasmus+ give for a 500-1999 km mobility?  
**A:** 417 EUR with green travel, 309 EUR otherwise.  
**Source:** [eu-guide-he-mobility](https://erasmus-plus.ec.europa.eu/programme-guide/part-b/key-action-1/mobility-projects-for-higher-education-students-and-staff): "500 - 1999 km | 417 EUR | 309 EUR"  
**Fix:** 

### [x] q107 · fact · easy
**Q:** C'est quoi l'International Credit Mobility (ICM) d'Erasmus+ ?  
**A:** Une action clé 1 (KA1) d'Erasmus+ qui permet à un établissement d'un pays partenaire (comme la Tunisie) d'envoyer des étudiants et du personnel en mobilité dans un établissement d'un pays du programme, et inversement.  
**Source:** [eu-tn-icm](https://www.erasmusplus.tn/International-Credit-Mobility-(ICM).php): "L'International Credit Mobility (ICM) fait partie de l'action clé 1 (KA1) du programme Erasmus+"  
**Source:** [eu-tn-ka1](https://www.erasmusplus.tn/KA1%20Actions.php): "L'International Credit Mobility (ICM) fait partie de l'action clé 1 (KA1) du programme Erasmus+"  
**Fix:** 

### [x] q108 · yes_no · easy
**Q:** Can recent graduates do an Erasmus+ traineeship abroad?  
**A:** Yes, Erasmus+ traineeships are also open to recent graduates.  
**Source:** [eu-traineeships](https://erasmus-plus.ec.europa.eu/opportunities/individuals/students/traineeships-abroad-for-students): "These opportunities are also open to recent graduates"  
**Fix:** 

### [x] q109 · number · easy
**Q:** How many students have taken part in Erasmus Mundus since 2004?  
**A:** Almost 50,000.  
**Source:** [eu-emjm-students](https://erasmus-plus.ec.europa.eu/opportunities/individuals/students/erasmus-mundus-joint-masters): "Almost 50,000 students have taken part since 2004"  
**Fix:** 

### [x] q110 · list · medium
**Q:** What does an Erasmus Mundus scholarship cover?  
**A:** Your participation costs, plus a contribution to travel, visa and a living allowance.  
**Source:** [eu-emjm-students](https://erasmus-plus.ec.europa.eu/opportunities/individuals/students/erasmus-mundus-joint-masters): "Scholarships cover your participation costs and contribute to"  
**Fix:** 

### [x] u001 · unanswerable · easy
**Q:** What IELTS score do I need for a UK Student visa?  
**A:** I don't know: the UK is outside this assistant's sources (France, Germany, Canada, Erasmus+).  
**Fix:** 

### [x] u002 · unanswerable · easy
**Q:** Quel est le montant de la bourse Fulbright pour un master aux États-Unis ?  
**A:** Je ne sais pas : les États-Unis et la bourse Fulbright ne sont pas couverts par les sources.  
**Fix:** 

### [x] u003 · unanswerable · hard
**Q:** What is the application deadline for the EU-CORE Erasmus Mundus master?  
**A:** I don't know: the Erasmus Mundus catalogue only lists EU-CORE by name; its deadline is on the programme's own website, which is not in the sources.  
**Note:** Hard: the programme name is in the corpus, the deadline isn't.  
**Fix:** 

### [x] u004 · unanswerable · medium
**Q:** Combien coûte un billet d'avion Tunis–Paris pour un étudiant ?  
**A:** Je ne sais pas : les prix des billets d'avion ne figurent pas dans les sources.  
**Fix:** 

### [x] u005 · unanswerable · medium
**Q:** Can I bring my cat to Germany on a student visa?  
**A:** I don't know: rules on travelling with pets are not in the sources.  
**Fix:** 

### [x] u006 · unanswerable · medium
**Q:** Quels sont les frais de scolarité d'un master à l'Université de Toronto ?  
**A:** Je ne sais pas : les frais propres à chaque université canadienne ne figurent pas dans les sources.  
**Fix:** 

### [x] u007 · unanswerable · medium
**Q:** What minimum grade average do I need to be admitted to a master's at TU Munich?  
**A:** I don't know: admission criteria of individual German universities are not in the sources.  
**Fix:** 

### [x] u008 · unanswerable · easy
**Q:** Comment obtenir un visa étudiant pour l'Italie ?  
**A:** Je ne sais pas : l'Italie ne fait pas partie des pays couverts (France, Allemagne, Canada, Erasmus+).  
**Fix:** 

### [x] u009 · unanswerable · hard
**Q:** How many weeks does the Canadian visa office currently take to process a study permit from Tunisia?  
**A:** I don't know: current processing times are published on an IRCC tool that is not in the sources (only doctoral students' 2-week target is mentioned).  
**Note:** Hard: related processing-time facts exist (doctoral fast track), so the system may answer wrongly.  
**Fix:** 

### [x] u010 · unanswerable · easy
**Q:** Is the Chevening scholarship open to Tunisian students?  
**A:** I don't know: Chevening (UK) is not covered by the sources.  
**Fix:** 

### [x] u011 · unanswerable · medium
**Q:** What is the average salary of a software engineer in Montreal?  
**A:** I don't know: salary data is not in the sources.  
**Fix:** 

### [x] u012 · unanswerable · medium
**Q:** Quelles universités espagnoles proposent des masters en anglais ?  
**A:** Je ne sais pas : l'Espagne n'est pas couverte par les sources (sauf indirectement via les programmes Erasmus Mundus).  
**Fix:** 

### [x] u013 · unanswerable · hard
**Q:** Which Tunisian bank is cheapest for transferring money to a German blocked account?  
**A:** I don't know: bank fees are not in the sources, and the Federal Foreign Office makes no recommendations about providers.  
**Note:** Hard: blocked-account content is in the corpus, the bank comparison isn't.  
**Fix:** 

### [x] u014 · unanswerable · hard
**Q:** Combien coûte par mois une assurance santé privée pour un étudiant en Allemagne ?  
**A:** Je ne sais pas : les sources disent qu'une assurance privée est nécessaire avant l'immatriculation, mais ne donnent pas de prix.  
**Note:** Hard: the requirement is in the corpus, the price isn't.  
**Fix:** 

### [x] u015 · unanswerable · medium
**Q:** Which Tunisian students won the Eiffel scholarship in 2025?  
**A:** I don't know: the sources contain no list of laureates (and it would be personal data).  
**Fix:** 
