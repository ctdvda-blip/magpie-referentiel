# -*- coding: utf-8 -*-
"""Couche de conception pedagogique du lot A.

Applique la skill « magpie-conception-exercices » v2.3 aux 49 exercices decrits
dans exos_a.py. exos_a.py n'est PAS modifie : ce module se superpose a lui, et
les generateurs fusionnent les deux. On conserve ainsi la tracabilite de la
version d'origine.

Champs, dans l'ordre impose par la skill (§2 : competence, tache, validation,
puis seulement la consigne) :

    comp     competence visee — ce que l'apprenant sait FAIRE apres coup
    bloom    case de la taxonomie revisee : processus cognitif x type de savoir
    ctx      contexte metier, une phrase (§4)
    eno      enonce reecrit : aucun nom de composant (§3), contexte integre
    att      resultat attendu
    err      erreur attendue, et ce qu'elle revele (§6)
    verdict  "competence" ou "connaissance"
    chn      question charniere, uniquement si verdict == "connaissance" (§1)
    data     jeu de donnees refondu (§5), source unique pour fiches et .gh
    don      justification du jeu de donnees
    mode/tol correction des contraintes du checker, si necessaire

VERSION : v0.3-260826
"""

VERSION = u"v0.3-260826"
SKILL = u"magpie-conception-exercices v2.3"

# ---------------------------------------------------------------------------
# Jeux de donnees refondus (§5 : longs, non ordonnes, non devinables).
# Definis ici une seule fois : les recettes .gh et les fiches y puisent.
# ---------------------------------------------------------------------------

# A-08 — cotes relevees sur un lot de traverses, en mm. Seuil de conformite 5 mm
#        d'ecart sur une cote nominale de 1 200 mm : on compte les hors-tolerance.
D_A08 = [1203, 1198, 1207, 1199, 1201, 1194, 1206, 1200, 1211, 1197,
         1202, 1188, 1205, 1200, 1196, 1209, 1193, 1204, 1199, 1214,
         1201, 1191, 1208, 1200, 1195, 1210, 1198, 1202]
# ecart absolu > 5 mm  ->  1188, 1211, 1214, 1191, 1210  ... calcule a la volee

# A-09 — releve de hauteurs d'allege importe d'un tableur, cellules vides incluses
D_A09 = [1050, 950, None, 1120, 1080, None, 990, 1150, 1020, None,
         1075, 1005, 1130, None, 960, 1095, 1040, None, 1110, 985,
         1065, 1025, None, 1085]

# A-11 — longueurs de debit, en mm, non ordonnees
D_A11 = [2450, 1830, 3120, 2075, 1640, 2890, 3450, 1975, 2310, 2660,
         1520, 3080, 2185, 2740, 1890, 3260, 2020, 2555, 1735, 2960,
         3340, 1680, 2405, 2830]

# A-12 — epaisseurs de placage relevees, en centiemes de mm
D_A12 = [62, 58, 71, 55, 67, 60, 74, 53, 69, 57,
         64, 76, 51, 68, 59, 72, 56, 65, 61, 78,
         54, 70, 63, 66, 52, 75, 58, 73]

# A-13 — six pieces, nom et longueur (mm) : le tri porte sur la longueur
D_A13_NOMS = [u"MONT-A", u"TRAV-B", u"MONT-C", u"TRAV-D", u"MONT-E", u"TRAV-F"]
D_A13_LONG = [2340, 1875, 2610, 1420, 2185, 1960]

# A-14 — 36 lames de bardage : on en depose une sur trois
D_A14 = [1840, 1795, 1920, 1755, 1880, 1810, 1965, 1730, 1855, 1900,
         1770, 1835, 1945, 1785, 1870, 1825, 1990, 1745, 1865, 1910,
         1760, 1845, 1935, 1800, 1890, 1815, 1975, 1740, 1860, 1905,
         1780, 1850, 1925, 1765, 1885, 1830]

# A-15 — 24 panneaux, surface en m2 : au-dela de 2,50 m2 la pose est a deux
D_A15 = [1.84, 3.12, 2.07, 2.95, 1.62, 3.40, 2.21, 1.97, 2.66, 3.28,
         1.53, 2.88, 2.14, 3.06, 1.73, 2.49, 2.72, 1.68, 3.34, 2.02,
         2.83, 1.91, 3.19, 2.36]

# A-17 — alternance de deux essences sur un plateau
D_A17_A = [u"CHENE-01", u"CHENE-02", u"CHENE-03", u"CHENE-04", u"CHENE-05"]
D_A17_B = [u"NOYER-01", u"NOYER-02", u"NOYER-03", u"NOYER-04", u"NOYER-05"]

# A-18 — 28 releves altimetriques le long d'un profil en long, en mm
D_A18 = [412, 438, 401, 455, 427, 466, 419, 448, 433, 471,
         405, 459, 424, 443, 462, 416, 451, 430, 468, 409,
         446, 435, 457, 421, 464, 414, 441, 453]

# A-30 — 24 pieces de debit, longueur en mm : retenir 500 <= L <= 1500
D_A30 = [1240, 480, 890, 1620, 1075, 500, 1500, 340, 1180, 760,
         1550, 620, 1420, 295, 985, 1330, 545, 1710, 830, 1150,
         465, 1275, 705, 1505]


# ---------------------------------------------------------------------------
# La couche pedagogique, exercice par exercice
# ---------------------------------------------------------------------------

SKILL_A = {

# ============================ A1 · Interface, flux, parametres ==============

u"A-01": dict(
    lim=u"La somme vaut 2 400, ce qui ne dit pas que la répartition est "
        u"CONSTRUCTIBLE : une imposte de 200 mm ou un châssis de 2 200 "
        u"mm satisfont l'égalité et ne se fabriquent pas. Les plages "
        u"admissibles ne sont pas dans l'exercice.",
    comp=u"Raccorder deux sources sur les deux entrées d'un même opérateur et "
         u"lire la valeur produite.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Un ensemble menuisé se compose d'une imposte et d'un châssis "
        u"superposés ; leur hauteur cumulée doit remplir exactement la baie.",
    eno=u"La baie mesure 2 400 mm de haut. Une valeur de hauteur vous est déjà "
        u"fournie pour l'imposte. Ajoutez une seconde valeur réglable pour le "
        u"châssis, faites-en la somme, et réglez les deux hauteurs pour que la "
        u"baie soit exactement remplie.",
    att=u"La somme des deux hauteurs vaut exactement 2 400.",
    err=u"Brancher les deux sources sur la même entrée : l'opérateur additionne "
        u"alors les deux valeurs sur une seule entrée et laisse l'autre vide. "
        u"Le résultat est faux d'un facteur qui trahit la confusion entre "
        u"« deux câbles » et « deux entrées ».",
    verdict=u"competence"),

u"A-02": dict(
    lim=u"Le point est au bon endroit dans le REPÈRE DU MODÈLE. Que ce "
        u"repère coïncide avec celui du géomètre — origine, orientation, "
        u"système de projection — est une convention de projet que rien "
        u"ici ne vérifie, et c'est la première cause de calages faux.",
    comp=u"Construire une position dans l'espace à partir de trois valeurs "
         u"séparées, y compris négatives.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Le géomètre communique la position d'un repère de nivellement par "
        u"rapport à la borne de chantier.",
    eno=u"Le repère se trouve à 30 m à l'est, 15 m au sud et 8 m au-dessus de "
        u"la borne, laquelle est à l'origine du modèle. Placez ce repère dans "
        u"le modèle à partir de trois valeurs réglables indépendantes.",
    att=u"Un point unique aux coordonnées (30 ; −15 ; 8).",
    err=u"Laisser la valeur nord-sud bornée aux positifs : le repère se place "
        u"au nord au lieu du sud. L'erreur révèle qu'on a réglé une valeur sans "
        u"vérifier l'étendue autorisée.",
    verdict=u"competence"),

u"A-03": dict(
    comp=u"—",
    bloom=u"Comprendre × conceptuelle",
    ctx=u"Un fond de plan doit être transmis à un confrère sans la chaîne de "
        u"calcul qui l'a produit.",
    eno=u"",
    att=u"",
    err=u"",
    verdict=u"connaissance",
    chn=u"Vous figez un point dans un paramètre autonome, puis vous supprimez "
        u"toute la chaîne qui l'avait produit. Le point reste affiché. "
        u"Pourquoi ?\n"
        u"a) Grasshopper garde en mémoire le dernier calcul effectué.\n"
        u"b) La donnée a été recopiée dans le paramètre, qui ne dépend plus de "
        u"rien. ← réponse\n"
        u"c) Le paramètre reconstruit le point à chaque ouverture du fichier.\n"
        u"d) L'affichage est un reste à l'écran, il disparaîtra au prochain "
        u"recalcul.\n\n"
        u"Valeur diagnostique : (a) et (d) révèlent qu'on confond persistance "
        u"et cache d'affichage ; (c) qu'on croit le paramètre encore lié à sa "
        u"source. Aucune de ces confusions ne se verrait dans un exercice où "
        u"le montage fonctionne."),

u"A-04": dict(
    lim=u"Trois cercles décalés prouvent que le référencement PAR CALQUE "
        u"fonctionne. Il ne prouve pas qu'il tiendra : un cercle ajouté "
        u"au calque demain entrera dans le flux sans prévenir, ce qui "
        u"est l'intérêt du procédé et son risque.",
    comp=u"Faire circuler une géométrie entre Rhino et Grasshopper dans les "
         u"deux sens, par calque plutôt que par sélection manuelle.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Le géomètre a livré l'implantation des poteaux sous forme de cercles ; "
        u"le bureau d'études doit en produire un calque de contrôle décalé.",
    eno=u"Les cercles d'implantation occupent le calque « CERCLES » du fichier "
        u"Rhino. Récupérez-les sans les désigner un par un — l'implantation "
        u"peut encore changer — remontez-les de 50 mm, et déposez le résultat "
        u"dans le modèle sur le calque « COPIES ».",
    att=u"Trois cercles présents sur le calque COPIES, décalés de 50 mm en Z.",
    err=u"Désigner les cercles à la main : le montage cesse de suivre dès que "
        u"le géomètre ajoute un poteau. L'erreur ne se voit pas au premier "
        u"essai, seulement à la mise à jour.",
    verdict=u"competence"),

u"A-05": dict(
    comp=u"—",
    bloom=u"Comprendre × factuelle",
    ctx=u"Reprise d'une définition écrite par un tiers, dont on ignore ce que "
        u"transportent les liaisons.",
    eno=u"",
    att=u"",
    err=u"",
    verdict=u"connaissance",
    chn=u"Une liaison transporte une donnée que vous n'avez pas produite. "
        u"Sans rien modifier, où lisez-vous d'un coup d'œil le nombre "
        u"d'éléments qu'elle transporte, leur type et leur structure ?\n"
        u"a) En survolant la sortie du composant amont. ← réponse\n"
        u"b) En ouvrant les propriétés du composant aval.\n"
        u"c) En branchant obligatoirement un afficheur.\n"
        u"d) Cette information n'est pas accessible sans calcul.\n\n"
        u"Valeur diagnostique : (c) révèle qu'on croit devoir modifier le "
        u"graphe pour l'inspecter — le réflexe qui fait casser les définitions "
        u"des autres ; (d) qu'on ignore l'existence de l'infobulle."),

u"A-06": dict(
    comp=u"—",
    bloom=u"Comprendre × conceptuelle",
    ctx=u"Un nombre de travées calculé produit une valeur décimale, alors que "
        u"le composant en aval attend un compte entier.",
    eno=u"",
    att=u"",
    err=u"",
    verdict=u"connaissance",
    chn=u"Une valeur décimale de 4,6 alimente une entrée qui n'accepte que des "
        u"entiers. Que vaut l'entier réellement utilisé ?\n"
        u"a) 4 — la partie entière est conservée.\n"
        u"b) 5 — la valeur est toujours arrondie au supérieur.\n"
        u"c) 5 — la valeur est arrondie au plus proche. ← réponse\n"
        u"d) Le composant se met en erreur.\n\n"
        u"Valeur diagnostique : c'est la question la plus utile du lot, parce "
        u"que (a) et (c) donnent tous deux la bonne réponse pour 4,6 et se "
        u"trompent pour 4,4. Un apprenant qui coche (c) « réussit » et garde "
        u"une règle fausse. Sur un approvisionnement — où il faut au moins "
        u"autant de pièces — c'est bien un arrondi au supérieur qu'il faut, et "
        u"il doit être posé explicitement : la conversion implicite ne le fera "
        u"pas."),

u"A-07": dict(
    comp=u"—",
    bloom=u"Comprendre × factuelle",
    ctx=u"Une donnée saisie en toutes lettres remonte d'un tableur mal rempli.",
    eno=u"",
    att=u"",
    err=u"",
    verdict=u"connaissance",
    chn=u"Un composant passe en orange et sa sortie est vide. Que faites-vous "
        u"en premier ?\n"
        u"a) Vous le supprimez et le reposez.\n"
        u"b) Vous survolez la pastille pour lire le message, qui nomme "
        u"l'entrée fautive. ← réponse\n"
        u"c) Vous rebranchez toutes les entrées.\n"
        u"d) Vous relancez le recalcul du document.\n\n"
        u"Valeur diagnostique : (a) et (c) sont le réflexe de l'apprenant qui "
        u"ne sait pas que Grasshopper dit précisément ce qui ne va pas ; "
        u"l'orange signale un avertissement, pas une panne."),

u"A-08": dict(
    lim=u"Onze traverses sortent de la tolérance ANNONCÉE. La tolérance "
        u"réelle d'un lot se lit sur le plan et dépend de l'assemblage : "
        u"5 mm sur une traverse vissée n'a pas le même sens que sur une "
        u"traverse encastrée.",
    dep=u"Les 28 cotes relevées sur le lot, en millimètres, ainsi que la cote nominale de 1 200 mm et la tolérance de 5 mm.",
    comp=u"Dénombrer les éléments d'un lot qui satisfont une condition, en "
         u"exploitant l'équivalence entre vrai et 1.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Le contrôle de réception d'un lot de traverses porte sur une cote "
        u"nominale de 1 200 mm, avec une tolérance de ± 5 mm.",
    eno=u"Les cotes relevées sur les 28 traverses du lot vous sont fournies. "
        u"Comptez combien de traverses sortent de la tolérance, sans écarter "
        u"aucun élément de la liste.",
    att=u"Le nombre de traverses dont l'écart à 1 200 mm dépasse 5 mm.",
    err=u"Compter les traverses conformes au lieu des rebuts — le complément "
        u"à 28 — ou traiter l'écart sans le ramener en valeur absolue, ce qui "
        u"ne retient que les cotes trop grandes et laisse passer les trop "
        u"petites.",
    verdict=u"competence",
    data=u"D_A08",
    don=u"28 cotes réelles resserrées autour de 1 200 : impossible de compter "
        u"à l'œil, il faut monter la comparaison. Les hors-tolérance sont "
        u"répartis dans les deux sens pour que l'oubli de la valeur absolue "
        u"soit détectable."),

u"A-09": dict(
    lim=u"Dix-huit hauteurs sont RENSEIGNÉES. Renseignée ne veut pas "
        u"dire juste : une valeur saisie par erreur passe le comptage. "
        u"Distinguer la donnée absente de la donnée fausse demande un "
        u"contrôle de vraisemblance, que l'exercice n'aborde pas.",
    dep=u"Le relevé des 24 baies, cellules non renseignées comprises.",
    alerte=u"La solution de référence tient en peu de composants : l'exercice mesure surtout la connaissance du composant de nettoyage. En parcours, le fusionner avec un calcul qui exploite le relevé nettoyé.",
    comp=u"Écarter les valeurs manquantes d'un relevé et dénombrer ce qui reste "
         u"exploitable.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Un relevé de hauteurs d'allège importé d'un tableur comporte des "
        u"cellules restées vides.",
    eno=u"Le relevé porte sur 24 baies, mais certaines lignes n'ont pas été "
        u"renseignées. Indiquez combien de hauteurs sont réellement "
        u"exploitables.",
    att=u"Le nombre de valeurs non vides du relevé.",
    err=u"Compter la longueur brute de la liste — 24 — sans voir que les "
        u"cellules vides y figurent encore. L'erreur révèle qu'on confond "
        u"« absence de valeur » et « absence d'élément ».",
    verdict=u"competence",
    data=u"D_A09",
    don=u"24 lignes dont 5 vides, dispersées et non groupées en fin de liste, "
        u"pour que le nettoyage ne puisse pas se deviner."),

u"A-10": dict(
    lim=u"Les sept abscisses supposent le premier portique À L'ORIGINE "
        u"de la file. Un décalage d'implantation translate toute la "
        u"liste, et c'est une donnée de projet, pas de calcul : la "
        u"formule reste juste et le résultat devient faux.",
    exempt5=u"L'effectif est le sujet même de l'exercice : distinguer 7 axes de 7 intervalles. L'allonger le dénaturerait.",
    comp=u"Produire une suite régulière de positions à partir d'un pas et d'un "
         u"nombre d'intervalles.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Les axes de portique d'une halle sont espacés régulièrement le long "
        u"d'une file.",
    eno=u"La halle compte 7 portiques espacés de 5 400 mm, le premier à "
        u"l'origine de la file. Produisez la liste des abscisses des 7 axes.",
    att=u"0, 5400, 10800, 16200, 21600, 27000, 32400.",
    err=u"Produire 7 intervalles au lieu de 7 axes, et donc 8 valeurs : la "
        u"confusion entre le nombre d'éléments et le nombre d'espaces entre "
        u"eux, qui se paie d'un portique en trop sur le chantier.",
    verdict=u"competence"),

u"A-11": dict(
    lim=u"Les deux longueurs valent POUR CE DÉBIT. Celle du dernier rang "
        u"est prise par index négatif précisément parce que le débit "
        u"s'allongera : la quatrième, elle, restera la quatrième — ce "
        u"qui est une convention, pas une propriété.",
    dep=u"Les 24 longueurs de débit, en millimètres, dans l'ordre du bon de commande.",
    comp=u"Atteindre un élément par son rang, et atteindre le dernier sans "
         u"présumer de l'effectif.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Une liste de débit est reprise par un opérateur qui doit contrôler "
        u"deux pièces précises avant lancement.",
    eno=u"Le débit comporte 24 pièces. Relevez la longueur de la quatrième "
        u"pièce, puis celle de la dernière — sachant que le débit s'allongera "
        u"la semaine prochaine et que votre montage devra encore désigner la "
        u"dernière pièce sans être retouché.",
    att=u"Deux longueurs : celle du rang 4 et celle du dernier rang.",
    err=u"Saisir en dur le rang de la dernière pièce. Le montage donne la "
        u"bonne réponse aujourd'hui et la mauvaise dès que le débit change — "
        u"une erreur qu'un exercice sans la clause d'évolution ne révélerait "
        u"jamais.",
    verdict=u"competence",
    data=u"D_A11",
    don=u"24 longueurs non ordonnées : le rang 4 et le dernier rang ne sont "
        u"identifiables que par construction."),

u"A-12": dict(
    lim=u"Effectif, minimum et maximum décrivent l'ÉTENDUE du lot, pas "
        u"sa dispersion. Deux lots de mêmes bornes peuvent être l'un "
        u"centré, l'autre bimodal ; c'est l'écart type qui le dirait, et "
        u"il n'est pas demandé.",
    dep=u"Les 28 épaisseurs relevées sur le lot, en centièmes de millimètre.",
    comp=u"Caractériser un lot par son effectif et ses valeurs extrêmes.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Un lot de placage est contrôlé en épaisseur avant mise en presse.",
    eno=u"Les épaisseurs relevées sur le lot vous sont fournies, en centièmes "
        u"de millimètre. Produisez, dans cet ordre, l'effectif du lot, "
        u"l'épaisseur la plus faible et l'épaisseur la plus forte.",
    att=u"Trois valeurs : effectif, minimum, maximum.",
    err=u"Trier la liste puis lire les extrémités à l'œil : la réponse est "
        u"juste, mais le montage ne suit plus si le lot change. La difficulté "
        u"est ici de résister au contournement, pas de trouver le composant.",
    verdict=u"competence",
    data=u"D_A12",
    don=u"28 valeurs dispersées entre 51 et 78, sans ordre, pour que les "
        u"extrêmes ne sautent pas aux yeux."),

u"A-13": dict(
    lim=u"L'ordre de débit est celui de la plus longue d'abord. Il ne "
        u"tient pas compte des CHUTES réutilisables : un atelier réel "
        u"intercale les pièces courtes dans les chutes des longues, et "
        u"l'ordre optimal n'est plus celui-là.",
    dep=u"Les six repères de pièces et les six longueurs correspondantes, dans deux listes de même rang.",
    comp=u"Réordonner une liste selon les valeurs portées par une autre.",
    bloom=u"Appliquer × procédurale",
    ctx=u"L'atelier veut débiter les pièces les plus longues en premier, pour "
        u"engager la barre la plus contraignante tant que le stock est intact.",
    eno=u"Six pièces portent chacune un repère et une longueur. Produisez la "
        u"liste des repères, de la pièce la plus longue à la plus courte.",
    att=u"MONT-C, MONT-A, MONT-E, TRAV-F, TRAV-B, TRAV-D.",
    err=u"Trier les repères eux-mêmes, ce qui donne un classement "
        u"alphabétique sans rapport avec les longueurs. L'erreur révèle qu'on "
        u"n'a pas vu que le tri devait être commandé par une autre liste.",
    verdict=u"competence",
    data=u"D_A13_NOMS / D_A13_LONG",
    don=u"Les repères sont volontairement construits de sorte que l'ordre "
        u"alphabétique diffère de l'ordre des longueurs : l'erreur devient "
        u"visible."),

u"A-14": dict(
    lim=u"Douze lames sont posées selon le motif DONNÉ. Que le motif « "
        u"une sur trois » convienne au calepinage — qu'il tombe juste en "
        u"rive, qu'il ne crée pas d'alignement disgracieux — est une "
        u"décision de projet que le comptage ne juge pas.",
    dep=u"Le calepinage plein : les 36 longueurs de lames, en millimètres.",
    alerte=u"Un seul composant fait le travail. À terme, mieux vaut l'absorber dans un exercice de calepinage complet que le maintenir isolé.",
    comp=u"Éliminer les éléments d'une liste selon un motif régulier.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Un bardage à claire-voie se pose en déposant une lame sur trois du "
        u"calepinage plein.",
    eno=u"Le calepinage plein comporte 36 lames. Produisez la liste des lames "
        u"réellement posées, sachant qu'on conserve la première puis une sur "
        u"trois.",
    att=u"12 lames : les rangs 0, 3, 6, … 33.",
    err=u"Décaler le motif d'un cran et commencer par déposer la première "
        u"lame : on obtient encore 12 lames, mais pas les mêmes. L'effectif "
        u"seul ne suffit donc pas à valider — c'est pourquoi la réponse porte "
        u"sur les longueurs conservées.",
    verdict=u"competence",
    data=u"D_A14",
    don=u"36 lames de longueurs voisines mais toutes distinctes : un décalage "
        u"du motif change la réponse, alors qu'il ne changerait pas un simple "
        u"comptage."),

u"A-15": dict(
    lim=u"Onze panneaux dépassent 2,50 m². Le seuil de pose en binôme "
        u"dépend aussi du POIDS et de l'encombrement, pas de la seule "
        u"surface : un panneau étroit et long se pose à deux bien avant "
        u"2,50 m².",
    dep=u"Les 24 surfaces de panneaux, en mètres carrés, et le seuil de 2,50 m².",
    comp=u"Scinder un lot en deux ensembles selon une condition, en conservant "
         u"les deux.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Au-delà de 2,50 m², un panneau ne se pose plus seul : il faut "
        u"séparer ce qui part en pose individuelle de ce qui part en binôme.",
    eno=u"Les surfaces des 24 panneaux du chantier vous sont fournies. "
        u"Séparez-les en deux groupes selon qu'ils dépassent ou non 2,50 m², "
        u"et donnez le nombre de panneaux à poser en binôme.",
    att=u"Le nombre de panneaux de surface strictement supérieure à 2,50 m².",
    err=u"Ne conserver qu'un seul des deux groupes, puis ne plus pouvoir "
        u"vérifier que la somme des deux effectifs vaut bien 24.",
    verdict=u"competence",
    data=u"D_A15",
    don=u"24 surfaces réelles, dont une exactement à 2,49 et une à 2,49 pour "
        u"éprouver la frontière ; aucune n'est posée à 2,50 pile, ce qui "
        u"rendrait l'exercice dépendant du sens de l'inégalité."),

u"A-16": dict(
    lim=u"Le contour fermé prouve que le décalage circulaire est juste. "
        u"Il ne dit pas que les lisses sont CONSTRUCTIBLES : huit "
        u"segments qui se rejoignent bout à bout supposent des "
        u"assemblages d'angle, absents du modèle.",
    exempt5=u"Huit montants parce que le contour est un octogone : la géométrie impose l'effectif.",
    alerte=u"Le décalage circulaire est un vrai geste de conception, mais la solution reste courte : le rapprocher d'un exercice de contour fermé.",
    comp=u"Relier chaque élément d'une liste au suivant en refermant la boucle, "
         u"sans traiter le dernier cas à part.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Un garde-corps polygonal doit être chiffré en longueur de lisse : "
        u"il faut les segments entre montants, y compris celui qui referme le "
        u"contour.",
    eno=u"Huit montants sont disposés en octogone. Tracez les huit lisses qui "
        u"relient chaque montant au suivant, la dernière revenant au premier, "
        u"en n'employant qu'une seule fois le composant de tracé.",
    att=u"Huit segments formant un contour fermé.",
    err=u"Obtenir sept segments et refermer le contour à la main. Le montage "
        u"marche pour huit montants et sera à refaire pour dix : l'exercice "
        u"vise justement le décalage circulaire qui évite le cas particulier.",
    verdict=u"competence"),

u"A-17": dict(
    lim=u"L'ordre de pose alterne les deux essences. Il ne tient pas "
        u"compte du SENS DU FIL ni de la teinte réelle des lames : un "
        u"platelage se calepine aussi à l'œil, en atelier, avant d'être "
        u"vissé.",
    dep=u"Les cinq lames de chêne et les cinq lames de noyer, dans deux listes séparées.",
    alerte=u"Un seul composant suffit. La compétence réelle — choisir entre mettre bout à bout et entrelacer — gagnerait à être posée en question charnière avant l'exercice.",
    comp=u"Entrelacer deux listes selon un motif d'alternance.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Un plateau se compose de lames de deux essences posées en "
        u"alternance stricte.",
    eno=u"Cinq lames de chêne et cinq lames de noyer vous sont fournies dans "
        u"deux listes séparées. Produisez l'ordre de pose du plateau, une "
        u"essence sur deux en commençant par le chêne.",
    att=u"CHENE-01, NOYER-01, CHENE-02, NOYER-02, … CHENE-05, NOYER-05.",
    err=u"Mettre les deux listes bout à bout : on obtient les dix lames, dans "
        u"un ordre où les cinq chênes précèdent les cinq noyers. L'effectif "
        u"est bon, le plateau est faux.",
    verdict=u"competence",
    data=u"D_A17_A / D_A17_B",
    don=u"Les repères sont numérotés pour que la concaténation et "
        u"l'entrelacement se distinguent au premier coup d'œil sur la fiche, "
        u"mais pas dans la sortie brute."),

u"A-18": dict(
    lim=u"Les huit relevés de la section courante sont EXTRAITS par leur "
        u"rang. Que les rangs 5 à 12 correspondent bien à la section "
        u"courante est une donnée du relevé : un point de plus au début "
        u"décale tout, sans que rien ne le signale.",
    dep=u"Les 28 relevés altimétriques du profil en long, en millimètres.",
    comp=u"Prélever une tranche continue d'une liste par ses rangs.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Sur un profil en long, seule la section courante intéresse le calcul ; "
        u"les relevés d'extrémité relèvent des ouvrages voisins.",
    eno=u"Le profil compte 28 relevés altimétriques. Isolez ceux des rangs 5 à "
        u"12 inclus, qui correspondent à la section courante.",
    att=u"Huit relevés, du rang 5 au rang 12.",
    err=u"Livrer sept valeurs, en oubliant que la borne haute est incluse — ou "
        u"neuf, en comptant deux fois une extrémité. L'écart d'une unité est "
        u"l'erreur canonique sur les domaines de rangs.",
    verdict=u"competence",
    data=u"D_A18",
    don=u"28 altitudes non ordonnées : la tranche demandée n'a aucune "
        u"signature visuelle, il faut la prélever."),

u"A-19": dict(
    lim=u"Quatre branches décrit la STRUCTURE du flux, pas son sens. "
        u"Deux flux à quatre branches peuvent ranger par file et par "
        u"niveau ou l'inverse : c'est le chemin, pas le compte, qui "
        u"porte l'information — d'où A-23.",
    comp=u"Lire la structure d'un flux arborescent : nombre de branches et "
         u"chemin d'une branche donnée.",
    bloom=u"Analyser × conceptuelle",
    ctx=u"Une définition reçue d'un confrère produit des résultats groupés ; "
        u"avant d'y brancher quoi que ce soit, il faut savoir comment.",
    eno=u"Le flux fourni est structuré en branches. Indiquez combien il en "
        u"compte.",
    att=u"Le nombre de branches du flux.",
    err=u"Répondre par le nombre total d'éléments, en confondant l'effectif "
        u"global et le nombre de regroupements.",
    verdict=u"competence"),

u"A-20": dict(
    lim=u"Neuf segments prouve que le produit croisé est obtenu. Il ne "
        u"dit pas que neuf haubans sont VOULUS : passer de trois à neuf "
        u"est un choix de structure, et l'exercice montre le mécanisme "
        u"sans trancher l'opportunité.",
    alerte=u"Le geste tient en une option de menu contextuel. L'intérêt est dans la conséquence sur le résultat, ce que l'énoncé exploite déjà ; surveiller qu'il ne se réduise pas à « savoir où cliquer ».",
    comp=u"Modifier la structure d'un flux pour obtenir un croisement complet "
         u"plutôt qu'un appariement terme à terme.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Une passerelle est haubanée : chaque ancrage de rive doit être relié "
        u"à chaque ancrage de mât, et non au seul ancrage de même rang.",
    eno=u"Trois ancrages de rive et trois ancrages de mât vous sont fournis. "
        u"Le tracé livre aujourd'hui trois haubans, un par paire de même rang. "
        u"Obtenez les neuf haubans de toutes les combinaisons possibles, sans "
        u"dupliquer le composant de tracé.",
    att=u"Neuf segments.",
    err=u"Dupliquer le tracé et le brancher trois fois : on obtient neuf "
        u"segments par force brute, et un montage qui ne tiendra pas à quatre "
        u"ancrages. La contrainte d'un seul composant ferme cette voie sans "
        u"nommer la solution.",
    verdict=u"competence"),

u"A-21": dict(
    lim=u"Quatre chemins simplifiés valident le NETTOYAGE. La lisibilité "
        u"d'un arbre tient aussi aux noms des groupes en amont : un "
        u"chemin court mais opaque ne vaut pas mieux qu'un chemin long, "
        u"et cela ne se mesure pas.",
    comp=u"Supprimer les niveaux de regroupement devenus inutiles sans détruire "
         u"le regroupement utile.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Un enchaînement d'opérations a empilé des niveaux de branche dont "
        u"aucun ne porte plus de sens.",
    eno=u"Le flux fourni porte des chemins à quatre niveaux, dont trois ne "
        u"distinguent plus rien. Ramenez-le à un seul niveau, sans fusionner "
        u"les groupes entre eux. Indiquez le nombre de branches obtenu.",
    att=u"Quatre branches, aux chemins {0} à {3}.",
    err=u"Tout aplatir : on obtient une branche unique et le regroupement est "
        u"perdu. C'est l'erreur qui distingue « simplifier » de « écraser ».",
    nb=4,
    verdict=u"competence"),

u"A-22": dict(
    lim=u"Les trois branches restituent les listes de départ. Cela "
        u"prouve que rien n'a été PERDU, pas que la structure est la "
        u"bonne : trois branches ou trois listes séparées se valent ici, "
        u"et le choix ne se justifie que par ce qui suit.",
    alerte=u"Assembler puis redécomposer reste un aller-retour scolaire. En parcours, lui donner une finalité : trois lots qui doivent rester distincts jusqu'à l'export.",
    comp=u"Assembler plusieurs listes en un flux structuré, puis en réextraire "
         u"chaque groupe.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Trois lots de fabrication doivent voyager ensemble dans la "
        u"définition tout en restant distincts à l'arrivée.",
    eno=u"Trois listes de longueurs différentes vous sont fournies. Faites-les "
        u"circuler dans un flux unique où chacune reste un groupe séparé, puis "
        u"récupérez les trois listes d'origine à l'identique.",
    att=u"Un flux à trois branches, puis trois sorties identiques aux listes "
        u"de départ.",
    err=u"Obtenir moins de sorties que de groupes : le composant de "
        u"décomposition n'expose que le nombre de sorties qu'on lui a "
        u"demandé, et perd silencieusement le reste.",
    verdict=u"competence"),

u"A-23": dict(
    lim=u"La permutation des deux niveaux est faite. Qu'elle soit la "
        u"bonne dépend de ce qu'on veut GROUPER ensuite — par file ou "
        u"par niveau — et c'est une question de projet, non de structure "
        u"de données.",
    alerte=u"Le composant de réécriture des chemins est à lui seul la solution. Le maintenir comme exercice n'a de sens que si l'appariement qui suit est réellement demandé.",
    comp=u"Réécrire les chemins d'un flux pour préparer une mise en "
         u"correspondance.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Deux flux décrivent le même ouvrage, l'un rangé par niveau puis par "
        u"file, l'autre par file puis par niveau : ils ne s'apparient pas.",
    eno=u"Le flux fourni est rangé par niveau puis par file. Réorganisez-le "
        u"par file puis par niveau, sans modifier les éléments eux-mêmes. "
        u"Indiquez le nombre de branches obtenu.",
    att=u"Un flux dont les deux niveaux de chemin sont permutés.",
    err=u"Réordonner les éléments au lieu des chemins : le contenu bouge, la "
        u"structure reste, et l'appariement échoue toujours.",
    nb=3,
    verdict=u"competence"),

u"A-24": dict(
    comp=u"—",
    bloom=u"Comprendre × conceptuelle",
    ctx=u"Deux listes de tailles différentes arrivent dans un même opérateur.",
    eno=u"",
    att=u"",
    err=u"",
    verdict=u"connaissance",
    chn=u"Une liste de 10 valeurs et une liste de 4 valeurs entrent dans un "
        u"même opérateur, sans réglage particulier. Combien de résultats "
        u"sortent ?\n"
        u"a) 4 — la liste la plus courte impose sa longueur.\n"
        u"b) 10 — la liste la plus courte est complétée par répétition de son "
        u"dernier élément. ← réponse\n"
        u"c) 40 — toutes les combinaisons sont calculées.\n"
        u"d) 14 — les deux listes sont mises bout à bout.\n\n"
        u"Valeur diagnostique : (a) est la représentation fausse la plus "
        u"répandue, et elle est dangereuse — elle fait croire qu'un "
        u"appariement déséquilibré se voit, alors qu'il produit "
        u"silencieusement six résultats calculés sur une valeur répétée. "
        u"(c) confond le comportement par défaut avec le croisement explicite, "
        u"qui fait l'objet de l'exercice suivant."),

u"A-25": dict(
    lim=u"Dix puis quarante montrent la différence entre appariement par "
        u"file et produit croisé. Ils ne disent pas lequel est ATTENDU : "
        u"le même graphe rend l'un ou l'autre selon l'intention, et "
        u"c'est l'intention qui doit être écrite quelque part.",
    exempt5=u"Les tailles 10 et 4 SONT l'objet de l'exercice — c'est le déséquilibre qui rend l'appariement observable.",
    comp=u"Choisir délibérément un mode d'appariement entre deux listes de "
         u"tailles différentes.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Un calepinage croise 10 files et 4 niveaux : selon qu'on veut une "
        u"valeur par file ou une valeur par intersection, l'appariement change.",
    eno=u"Une liste de 10 valeurs et une liste de 4 valeurs vous sont "
        u"fournies. Produisez d'abord un résultat par file — 10 valeurs — puis "
        u"un résultat par intersection file × niveau — 40 valeurs.",
    att=u"Deux effectifs : 10 puis 40.",
    err=u"Obtenir 40 dans les deux cas en laissant un croisement branché, ou "
        u"10 dans les deux cas en ne changeant que la position des câbles. "
        u"L'appariement est un réglage, pas une conséquence du câblage.",
    verdict=u"competence"),

u"A-26": dict(
    comp=u"—",
    bloom=u"Comprendre × conceptuelle",
    ctx=u"Deux branches indépendantes cohabitent sur un même canvas.",
    eno=u"",
    att=u"",
    err=u"",
    verdict=u"connaissance",
    chn=u"Deux branches indépendantes produisent chacune un résultat. Dans "
        u"quel ordre sont-elles évaluées ?\n"
        u"a) De gauche à droite, selon leur position sur le canvas.\n"
        u"b) Dans l'ordre où elles ont été créées.\n"
        u"c) L'ordre entre deux branches indépendantes n'est pas défini ; "
        u"seules les dépendances imposent un ordre. ← réponse\n"
        u"d) Simultanément, sur plusieurs cœurs.\n\n"
        u"Valeur diagnostique : (a) est la croyance qui pousse à ranger le "
        u"canvas pour « corriger » un résultat — un temps perdu considérable. "
        u"(d) fait espérer un gain de performance qui n'existe pas ici."),

u"A-27": dict(
    exempt5=u"Le sujet est le format de l'étiquette, pas le dénombrement ; cinq pièces suffisent et la fiche reste lisible.",
    comp=u"Composer un libellé exploitable à partir de valeurs numériques et "
         u"de fragments de texte.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Chaque pièce débitée part à l'atelier avec une étiquette portant son "
        u"repère et sa longueur.",
    eno=u"Les numéros et les longueurs des 5 pièces vous sont fournis dans "
        u"deux listes. Produisez les cinq étiquettes au format "
        u"« PIECE-01 : 1250 mm », le numéro étant cadré sur deux chiffres.",
    att=u"Cinq libellés au format demandé.",
    err=u"Livrer « PIECE-1 » au lieu de « PIECE-01 » : le cadrage sur deux "
        u"chiffres saute, et le tri alphabétique des étiquettes à l'atelier "
        u"place la pièce 10 avant la pièce 2.",
    verdict=u"competence"),

u"A-28": dict(
    exempt5=u"Le sujet est le découpage d'une référence ; six références suffisent à éprouver le séparateur.",
    comp=u"Extraire un fragment d'une référence structurée et le normaliser.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Les références fournisseur encodent la famille, le code produit et "
        u"l'essence ; seul le code produit alimente la commande.",
    eno=u"Les références vous sont fournies au format « MEUB-A12-CHENE ». "
        u"Extrayez le seul code central et livrez-le en minuscules.",
    att=u"Six codes en minuscules : a12, b07, …",
    err=u"Découper par position de caractère plutôt que par séparateur : le "
        u"montage tient tant que la famille fait quatre lettres, et se rompt à "
        u"la première référence au format différent.",
    verdict=u"competence"),

u"A-29": dict(
    comp=u"—",
    bloom=u"Comprendre × conceptuelle",
    ctx=u"Deux cotes calculées par des chemins différents devraient coïncider.",
    eno=u"",
    att=u"",
    err=u"",
    verdict=u"connaissance",
    chn=u"Vous comparez 0,1 + 0,2 à 0,3 par un test d'égalité stricte. Le "
        u"résultat est faux. Pourquoi ?\n"
        u"a) Grasshopper arrondit les affichages à trois décimales.\n"
        u"b) Les nombres à virgule sont codés en binaire : la somme vaut "
        u"0,30000000000000004. ← réponse\n"
        u"c) Le test d'égalité ne fonctionne pas sur les décimaux.\n"
        u"d) Il faut convertir en entiers avant de comparer.\n\n"
        u"Valeur diagnostique : c'est la connaissance qui, non transmise, "
        u"produit des heures de débogage sur des géométries « qui devraient "
        u"se toucher ». Elle explique aussi pourquoi le mode de validation "
        u"tolérant existe."),

u"A-30": dict(
    lim=u"Seize chutes repartent en stock, bornes INCLUSES. La "
        u"convention d'inclusion des bornes est un choix d'atelier : une "
        u"chute exactement à la longueur minimale se garde ou se jette "
        u"selon l'usage, et l'écart est ici de deux pièces.",
    dep=u"Les 24 longueurs de chutes du jour, en millimètres, et les deux bornes de 500 et 1 500 mm.",
    comp=u"Combiner deux conditions en une décision unique par élément.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Seules les chutes comprises entre 500 et 1 500 mm sont remises en "
        u"stock : en deçà elles partent au rebut, au-delà elles retournent en "
        u"barre.",
    eno=u"Les longueurs des 24 chutes du jour vous sont fournies. Comptez "
        u"celles qui repartent en stock, bornes incluses.",
    att=u"Le nombre de chutes dont la longueur est comprise entre 500 et "
        u"1 500 mm, bornes incluses.",
    err=u"Traiter les bornes en strict : les chutes à 505 et 1 495 restent "
        u"prises, mais une chute à exactement 500 ou 1 500 serait écartée. Le "
        u"jeu de données contient l'une et l'autre pour que l'écart se voie.",
    verdict=u"competence",
    data=u"D_A30",
    don=u"24 longueurs, dont 505, 545, 1 495 et 1 505 : les valeurs sont "
        u"placées juste de part et d'autre des bornes pour que le sens de "
        u"l'inégalité change la réponse."),

u"A-31": dict(
    lim=u"L'interrupteur bascule bien l'affichage. Il ne DÉSACTIVE pas "
        u"la branche masquée : les deux variantes continuent de se "
        u"calculer, ce qui est sans conséquence ici et devient coûteux "
        u"sur une définition lourde — c'est l'objet du lot MP.",
    comp=u"Orienter un flux vers l'une ou l'autre de deux sorties selon une "
         u"condition, sans démonter le montage.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Deux variantes de remplissage sont à l'étude ; le client veut les "
        u"voir alternativement sans qu'on retouche la définition devant lui.",
    eno=u"Les deux variantes de remplissage sont montées et fonctionnent. "
        u"Faites en sorte qu'un seul interrupteur bascule l'affichage de "
        u"l'une à l'autre, sans supprimer ni débrancher aucun composant.",
    att=u"Une seule géométrie affichée à la fois, commandée par "
        u"l'interrupteur.",
    err=u"Couper un câble pour masquer une variante : l'affichage est bon, "
        u"mais la bascule n'est plus réversible et la seconde variante est "
        u"perdue. La contrainte « sans débrancher » ferme cette voie.",
    verdict=u"competence"),

# ============================ A3 · Geometrie parametrique ===================

u"A-32": dict(
    lim=u"Les deux vecteurs ont la bonne longueur et la bonne direction. "
        u"Un vecteur n'a pas de POINT D'APPLICATION : que le second "
        u"tirant parte du même endroit que le premier est une décision "
        u"de construction, pas une propriété du vecteur.",
    comp=u"Construire un vecteur entre deux points, puis en régler la longueur "
         u"sans en changer la direction.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Une potence de levage est reprise par un tirant : la direction est "
        u"imposée par la géométrie, la longueur par la portée à couvrir.",
    eno=u"Le tirant part de l'origine et rejoint le point situé à 30 en X et "
        u"40 en Y. Construisez sa direction, puis produisez un second tirant "
        u"de même direction mais de 100 unités de long.",
    att=u"Un vecteur de longueur 50 et un vecteur de longueur 100, de même "
        u"direction.",
    err=u"Multiplier le vecteur par 100 au lieu de porter sa longueur à 100 : "
        u"on obtient 5 000 unités. L'erreur révèle qu'on confond mise à "
        u"l'échelle et fixation d'amplitude.",
    verdict=u"competence"),

u"A-33": dict(
    lim=u"Le cercle est dans le plan demandé. Que ce plan soit celui du "
        u"PERCEMENT réel dépend de la machine : une inclinaison de 30° "
        u"se perce en repositionnant la pièce, et l'atelier redéfinit "
        u"son propre repère.",
    comp=u"Poser un repère orienté et y construire une géométrie.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Une buse traverse un mur en biais : son tracé se pose dans un plan "
        u"incliné, pas dans le plan horizontal.",
    eno=u"Le percement est circulaire, de 20 de rayon, centré à 50 au-dessus "
        u"de l'origine, et son plan est incliné de 30° autour de l'axe X. "
        u"Construisez ce tracé.",
    att=u"Un cercle de rayon 20 dans le plan incliné demandé.",
    err=u"Construire le cercle à plat puis le faire tourner : le résultat est "
        u"visuellement identique mais le repère local ne suit pas, et tout ce "
        u"qu'on y accrochera ensuite sera mal orienté.",
    verdict=u"competence"),

u"A-34": dict(
    lim=u"L'hexagone inscrit et le carré circonscrit encadrent le "
        u"fourreau. L'exercice suppose un fourreau CIRCULAIRE : sur un "
        u"fourreau ovalisé — cas courant après cintrage — ni l'inscrit "
        u"ni le circonscrit ne se construisent ainsi.",
    comp=u"Produire des primitives filaires en maîtrisant ce que désignent "
         u"leurs paramètres.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Un poteau de section hexagonale est inscrit dans un fourreau "
        u"circulaire, lui-même logé dans un coffrage carré.",
    eno=u"Le fourreau a 40 de rayon. Construisez la section hexagonale "
        u"inscrite dans ce fourreau, ainsi que le carré de coffrage "
        u"circonscrit au même fourreau.",
    att=u"Un hexagone de rayon 40 et un carré de 80 × 80.",
    err=u"Prendre 40 pour l'apothème de l'hexagone au lieu du rayon "
        u"circonscrit : la section ne tient plus dans le fourreau. Inscrit et "
        u"circonscrit ne se devinent pas, ils se vérifient.",
    verdict=u"competence"),

u"A-35": dict(
    lim=u"Douze colliers régulièrement espacés le long du tracé. "
        u"L'espacement réel se décide par la PORTÉE admissible du "
        u"conduit et par les points durs du bâtiment ; la régularité est "
        u"une commodité de modèle, pas une règle de pose.",
    exempt5=u"Le nombre de colliers est une donnée de la consigne, pas un résultat à trouver.",
    comp=u"Répartir des positions régulières le long d'une courbe et récupérer "
         u"le repère local en chaque position.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Un conduit souple est maintenu par des colliers régulièrement "
        u"espacés le long de son tracé ; chaque collier est perpendiculaire au "
        u"conduit.",
    eno=u"Le tracé du conduit vous est fourni. Placez 12 colliers de 5 de "
        u"rayon, régulièrement espacés le long du tracé et perpendiculaires à "
        u"celui-ci en chaque point.",
    att=u"12 cercles de rayon 5, perpendiculaires au tracé.",
    err=u"Placer les colliers à plat dans le plan horizontal : ils sont bien "
        u"répartis, mais aucun n'enserre le conduit. L'erreur révèle qu'on a "
        u"récupéré les positions sans les repères qui les accompagnent.",
    verdict=u"competence"),

u"A-36": dict(
    lim=u"Les deux courbes s'appuient sur les mêmes points. Laquelle "
        u"convient dépend de la NATURE des points : des points relevés, "
        u"entachés d'erreur, appellent l'approximation ; des points de "
        u"conception appellent l'interpolation. Le modèle ne le sait "
        u"pas.",
    exempt5=u"Six points de passage : l'effectif est imposé par la comparaison entre les deux tracés.",
    comp=u"Distinguer une courbe qui passe par des points d'une courbe que ces "
         u"points contrôlent.",
    bloom=u"Analyser × conceptuelle",
    ctx=u"Un profil de main courante est défini par des points de passage "
        u"imposés ; un second tracé, plus souple, sert d'étude de forme.",
    eno=u"Six points vous sont fournis. Tracez la courbe qui passe exactement "
        u"par chacun d'eux, puis celle qui ne fait que s'en approcher en les "
        u"prenant pour points de commande. Superposez les deux.",
    att=u"Deux courbes distinctes appuyées sur les mêmes points.",
    err=u"Obtenir deux courbes confondues : signe qu'on a employé deux fois la "
        u"même construction. Les deux tracés ne coïncident qu'aux extrémités.",
    verdict=u"competence"),

u"A-37": dict(
    lim=u"Six entretoises au bon espacement. Le premier décalage de 120 "
        u"mm et le pas de 24 mm sont des DONNÉES : leur cumul doit "
        u"tomber sous la hauteur disponible, ce que l'exercice ne "
        u"vérifie pas.",
    comp=u"Appliquer une translation et l'échelonner, en sachant que la "
         u"transformation ne consomme pas l'original.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Une rangée d'entretoises est répartie sur la hauteur d'un montant.",
    eno=u"L'entretoise de base vous est fournie. Remontez-la de 120 mm, puis "
        u"produisez cinq entretoises supplémentaires échelonnées tous les "
        u"24 mm au-dessus d'elle, sans employer de composant de réseau.",
    att=u"Six entretoises espacées de 24 mm.",
    err=u"Croire que la translation déplace l'original et compter cinq "
        u"entretoises au lieu de six. La transformation produit une copie ; "
        u"l'original reste dans le flux.",
    verdict=u"competence"),

u"A-38": dict(
    lim=u"Le profil tourné et son symétrique sont produits. Une symétrie "
        u"INVERSE le sens de parcours de la courbe : sans conséquence à "
        u"l'affichage, elle en a une dès qu'on extrude ou qu'on décale, "
        u"et c'est un piège classique.",
    comp=u"Faire tourner une géométrie autour d'un axe choisi et en produire "
         u"le symétrique par rapport à un plan choisi.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Un profil d'angle se décline en version droite et version gauche, "
        u"orientées à 45° sur la trame.",
    eno=u"Le profil vous est fourni. Faites-le tourner de 45° autour de l'axe "
        u"vertical passant par l'origine, puis produisez sa version "
        u"symétrique par rapport au plan vertical contenant l'axe X.",
    att=u"Le profil tourné et son symétrique.",
    err=u"Prendre le mauvais plan de symétrie et obtenir une version "
        u"superposable à l'originale par rotation : une pièce gauche et une "
        u"pièce droite ne sont pas superposables, c'est le contrôle à faire.",
    verdict=u"competence"),

u"A-39": dict(
    lim=u"Vingt modules en trame et douze en couronne. Aucun des deux "
        u"réseaux ne vérifie que les modules ne se RECOUVRENT pas : sur "
        u"la couronne, un module large et un rayon court se chevauchent "
        u"sans que le compte bouge.",
    comp=u"Produire des répétitions régulières en trame et en couronne, et "
         u"lire la structure de données obtenue.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Une façade est calepinée en modules réguliers ; une verrière "
        u"circulaire reprend le même module en couronne.",
    eno=u"Le module vous est fourni. Produisez la trame de 5 modules en "
        u"largeur et 4 en hauteur, espacés de 600 mm et 400 mm, puis la "
        u"couronne de 12 modules répartis sur un tour complet.",
    att=u"20 modules en trame et 12 modules en couronne.",
    err=u"Produire 12 modules répartis sur 360° en comptant la position "
        u"d'origine deux fois : le douzième se superpose au premier et il n'y "
        u"a que 11 modules visibles.",
    verdict=u"competence"),

u"A-40": dict(
    lim=u"Les deux mises à l'échelle sont justes. Une échelle non "
        u"uniforme déforme les CONGÉS et les épaisseurs : un profil deux "
        u"fois plus haut n'a plus les mêmes rayons de raccordement, et "
        u"n'est plus fabricable avec le même outil.",
    comp=u"Mettre à l'échelle une géométrie, en maîtrisant le centre et en "
         u"distinguant l'échelle uniforme de l'échelle par direction.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Un profil de menuiserie est décliné en une version réduite et une "
        u"version surhaussée, sans changer sa largeur de passage.",
    eno=u"Le profil vous est fourni. Produisez d'abord une version réduite à "
        u"60 % autour de son propre centre de gravité, puis une version deux "
        u"fois plus haute dont la largeur reste inchangée.",
    att=u"Un profil réduit centré et un profil étiré verticalement.",
    err=u"Réduire autour de l'origine du modèle plutôt qu'autour du centre du "
        u"profil : la taille est bonne, la position ne l'est plus.",
    verdict=u"competence"),

u"A-41": dict(
    lim=u"Les deux surfaces sont produites. Elles n'ont pas la même "
        u"NATURE : la transition entre deux profils dépend de leur "
        u"paramétrage et peut se vriller, là où l'extrusion ne le peut "
        u"pas. Deux surfaces d'apparence proche se comportent "
        u"différemment en aval.",
    comp=u"Passer d'une courbe à une surface par extrusion et par transition "
         u"entre profils.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Une trémie relie deux sections différentes ; un conduit droit relie "
        u"deux sections identiques.",
    eno=u"Deux profils fermés superposés vous sont fournis. Produisez la "
        u"surface de transition qui les relie, puis, séparément, la surface "
        u"obtenue en poussant le profil du bas de 200 mm vers le haut. "
        u"Comparez les deux.",
    att=u"Une surface de transition et une surface d'extrusion.",
    err=u"Obtenir une transition vrillée parce que les deux profils ne "
        u"démarrent pas au même endroit : la surface est valide mais "
        u"inconstruisible.",
    verdict=u"competence"),

u"A-42": dict(
    lim=u"Le tube et la surface de révolution sont engendrés. Le "
        u"balayage le long d'un guide courbe peut PINCER la surface "
        u"quand le rayon du guide approche celui du profil — l'exercice "
        u"reste dans le cas sain, et rien ne signale l'autre.",
    comp=u"Engendrer une surface par déplacement d'un profil le long d'un "
         u"guide, et par rotation autour d'un axe.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Une main courante tubulaire suit un limon ; un fût de colonne est "
        u"engendré par rotation de son profil.",
    eno=u"Le profil circulaire et son guide vous sont fournis, ainsi qu'un "
        u"profil plan. Engendrez le tube en promenant le profil circulaire le "
        u"long du guide, puis le fût en faisant tourner le profil plan autour "
        u"de l'axe vertical.",
    att=u"Un tube et une surface de révolution.",
    err=u"Omettre de désigner l'axe de rotation : le composant reste en "
        u"attente et ne produit rien, sans que le montage paraisse faux.",
    verdict=u"competence"),

u"A-43": dict(
    lim=u"Un volume non nul prouve la FERMETURE. Il ne prouve pas la "
        u"propreté : faces retournées, arêtes dupliquées ou "
        u"auto-intersections peuvent subsister et se manifester "
        u"seulement à l'export ou à l'impression.",
    comp=u"Refermer une enveloppe ouverte et établir qu'elle constitue bien un "
         u"solide.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Un caisson doit être étanche avant d'être chiffré en volume de "
        u"remplissage ; une enveloppe ouverte n'a pas de volume.",
    eno=u"L'enveloppe fournie présente deux ouvertures. Refermez-la, puis "
        u"établissez par une valeur numérique qu'elle est désormais un solide.",
    att=u"Une valeur numérique attestant le caractère fermé, et un volume non "
        u"nul.",
    err=u"Se fier à l'aspect visuel : une enveloppe non fermée s'affiche "
        u"exactement comme une enveloppe fermée. Seul le contrôle numérique "
        u"tranche — c'est tout l'objet de l'exercice.",
    verdict=u"competence"),

u"A-44": dict(
    lim=u"Le volume retiré est celui des quatre cylindres. Il ne dit "
        u"rien de la TENUE de la platine percée, ni de la faisabilité du "
        u"perçage : quatre trous de 20 mm dans une platine mince "
        u"l'affaiblissent, et c'est un calcul de résistance.",
    comp=u"Combiner des solides par soustraction et quantifier la matière "
         u"retirée.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Une platine d'assemblage est percée pour le passage des boulons ; "
        u"le poids retiré entre dans le bilan de charge.",
    eno=u"La platine vous est fournie. Percez-la de quatre trous traversants "
        u"de 20 mm de diamètre, puis donnez le volume de matière retirée.",
    att=u"La platine percée et le volume retiré.",
    err=u"Calculer le volume des quatre cylindres entiers plutôt que la "
        u"différence des volumes : si les cylindres dépassent de la platine "
        u"pour garantir le percement, l'écart est exactement la partie qui "
        u"dépasse.",
    verdict=u"competence"),

u"A-45": dict(
    lim=u"Le linéaire du contour de coupe est juste à mi-hauteur. Une "
        u"coupe à une autre altitude peut donner un contour de topologie "
        u"DIFFÉRENTE — deux boucles au lieu d'une — et le linéaire seul "
        u"ne le signale pas.",
    comp=u"Extraire le contour d'intersection entre un solide et un plan, et "
         u"le mesurer.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Une coupe horizontale à mi-hauteur sert à chiffrer le linéaire de "
        u"joint périphérique.",
    eno=u"Le solide vous est fourni. Établissez son contour de coupe à "
        u"mi-hauteur et donnez le linéaire total de ce contour.",
    att=u"Le contour de coupe et son linéaire total.",
    err=u"Ne mesurer qu'un seul morceau du contour quand la coupe en produit "
        u"plusieurs : le linéaire est sous-évalué sans que rien ne le signale.",
    verdict=u"competence"),

u"A-46": dict(
    lim=u"Le nombre de blocs en interférence est établi GÉOMÉTRIQUEMENT. "
        u"Un gabarit de passage réel intègre des jeux de sécurité et de "
        u"pose : un bloc qui affleure sans pénétrer est compté conforme "
        u"ici, et refusé sur chantier.",
    comp=u"Identifier, dans un ensemble, les objets qui interfèrent avec un "
         u"volume donné.",
    bloom=u"Analyser × procédurale",
    ctx=u"Un gabarit de passage doit rester libre : tout élément qui y pénètre "
        u"est à reprendre.",
    eno=u"Quinze blocs sont disposés autour du gabarit de passage fourni. "
        u"Indiquez combien d'entre eux empiètent sur ce gabarit.",
    att=u"Le nombre de blocs en interférence avec le gabarit.",
    err=u"Obtenir une réponse unique pour l'ensemble au lieu d'une réponse par "
        u"bloc : le test renvoie un verdict global si on ne lui présente pas "
        u"les blocs un à un.",
    verdict=u"competence"),

# ============================ A4 · Mesures et analyse ======================

u"A-47": dict(
    lim=u"Linéaire, surface et volume décrivent l'assemblage TEL QU'IL "
        u"EST MODÉLISÉ. Un assemblage dont les pièces s'interpénètrent "
        u"compte deux fois la matière commune : les trois valeurs "
        u"restent cohérentes entre elles et fausses ensemble.",
    comp=u"Mesurer les trois grandeurs de base d'un assemblage en choisissant "
         u"l'outil adapté à chaque type de géométrie.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Un chiffrage rapide demande le linéaire d'arêtes à souder, la "
        u"surface à peindre et le volume de matière.",
    eno=u"L'assemblage vous est fourni. Donnez, dans cet ordre, le linéaire "
        u"total des arêtes, la surface développée et le volume.",
    att=u"Trois valeurs : linéaire, surface, volume.",
    err=u"Additionner des grandeurs de natures différentes ou mesurer la "
        u"surface sur les arêtes : chaque grandeur suppose un type de "
        u"géométrie, et l'assemblage en contient plusieurs.",
    verdict=u"competence"),

u"A-48": dict(
    lim=u"Le rayon au point le plus serré est le minimum SUR LES POINTS "
        u"ÉCHANTILLONNÉS. La courbure varie continûment : un pas trop "
        u"large manque le vrai minimum, et le résultat reste stable, "
        u"plausible et faux — c'est ce que DV-02 traite en grand.",
    comp=u"Analyser localement une courbe pour y localiser la zone la plus "
         u"contraignante.",
    bloom=u"Analyser × procédurale",
    ctx=u"Un profilé cintré ne peut descendre sous un rayon de cintrage "
        u"minimal : c'est le point le plus serré du tracé qui décide de la "
        u"faisabilité.",
    eno=u"Le tracé vous est fourni. Localisez son point le plus serré et "
        u"donnez le rayon de cintrage à cet endroit.",
    att=u"Le point de courbure maximale et son rayon de courbure.",
    err=u"Confondre courbure et rayon, qui varient en sens inverse : chercher "
        u"le rayon maximal conduit au point le plus plat, c'est-à-dire "
        u"exactement l'inverse de ce que la fabrication demande.",
    verdict=u"competence"),

u"A-49": dict(
    lim=u"Les six étiquettes sont aux centres de gravité GÉOMÉTRIQUES, "
        u"c'est-à-dire à densité uniforme. Une pièce composite — bois et "
        u"métal, ou creuse d'un côté — a un centre de masse différent, "
        u"et c'est lui qui compte à la manutention.",
    comp=u"Localiser le centre de gravité de pièces et s'en servir comme point "
         u"d'accroche.",
    bloom=u"Appliquer × procédurale",
    ctx=u"Chaque pièce d'un lot reçoit son repère au centre, à l'endroit où "
        u"l'étiquette sera collée et où l'élingue sera accrochée.",
    eno=u"Six pièces vous sont fournies. Placez au centre de gravité de "
        u"chacune une étiquette portant son numéro.",
    att=u"Six étiquettes numérotées, placées aux centres de gravité.",
    err=u"Prendre le centre de la boîte englobante plutôt que le centre de "
        u"gravité : les deux coïncident sur une pièce symétrique et divergent "
        u"sur une pièce en L — et c'est précisément là que l'élingue compte.",
    verdict=u"competence"),
}


# ---------------------------------------------------------------------------
# Acces
# ---------------------------------------------------------------------------

JEUX = {
    u"D_A08": D_A08, u"D_A09": D_A09, u"D_A11": D_A11, u"D_A12": D_A12,
    u"D_A13_NOMS": D_A13_NOMS, u"D_A13_LONG": D_A13_LONG, u"D_A14": D_A14,
    u"D_A15": D_A15, u"D_A17_A": D_A17_A, u"D_A17_B": D_A17_B,
    u"D_A18": D_A18, u"D_A30": D_A30,
}

CONNAISSANCES = sorted([k for k, v in SKILL_A.items()
                        if v.get(u"verdict") == u"connaissance"])


def fusionner(exo):
    """Superpose la couche pedagogique sur un exercice de exos_a.py.

    Retourne un nouveau dictionnaire ; l'original n'est pas modifie.
    """
    s = SKILL_A.get(exo["id"])
    if not s:
        return dict(exo)
    r = dict(exo)
    r[u"competence"] = s.get(u"comp") or u""
    r[u"bloom"] = s.get(u"bloom") or u""
    r[u"contexte"] = s.get(u"ctx") or u""
    r[u"erreur"] = s.get(u"err") or u""
    r[u"verdict"] = s.get(u"verdict") or u"competence"
    r[u"charniere"] = s.get(u"chn") or u""
    r[u"jeu"] = s.get(u"data") or u""
    r[u"donnees_note"] = s.get(u"don") or u""
    r[u"limite"] = s.get(u"lim") or u""
    r[u"alerte"] = s.get(u"alerte") or u""
    r[u"exempt5"] = s.get(u"exempt5") or u""
    if s.get(u"dep"):
        r["depart"] = s[u"dep"]
    # §2 : l'objectif EST la competence visee. L'objectif d'origine, souvent
    # redige en « comprendre que… », decrivait un savoir, pas un savoir-faire.
    if s.get(u"comp") and s[u"comp"] != u"—":
        r[u"obj_origine"] = exo["obj"]
        r["obj"] = s[u"comp"]
    if s.get(u"nb"):
        r["nb"] = s[u"nb"]
    if s.get(u"eno"):
        r["enonce"] = s[u"eno"]
    if s.get(u"att"):
        r["att"] = s[u"att"]
    if s.get(u"mode"):
        r["mode"] = s[u"mode"]
    if s.get(u"tol"):
        r["tol"] = s[u"tol"]
    return r


# ---------------------------------------------------------------------------
# Correctifs « contraintes du checker »
#
# Le checker Magpie n'accepte en reponse ni texte ni booleen : la reponse doit
# etre ramenee a un nombre PAR LE MONTAGE DE L'APPRENANT, et cette conversion
# doit rester une etape naturelle de la tache (skill, section « Contraintes du
# checker »). Plusieurs exercices attendaient un nom de piece ou un libelle :
# ils sont ici ramenes a une reponse numerique sans perdre la competence visee,
# ou declares hors auto-correction quand le texte EST le livrable.
# ---------------------------------------------------------------------------

# A-13 — les pieces portent un numero de repere d'atelier, pas un nom.
# Le tri par cle est inchange ; seule la nature de la reponse devient numerique.
D_A13_REP = [4207, 4183, 4256, 4171, 4229, 4198]

# A-17 — les lames sont identifiees par leur longueur. Les deux essences
# occupent deux plages distinctes : l'alternance se verifie a la lecture, et
# une simple mise bout a bout se voit immediatement.
D_A17_LG_CHENE = [1245, 1268, 1231, 1287, 1252]
D_A17_LG_NOYER = [1418, 1463, 1437, 1409, 1481]

CORRECTIFS = {

u"A-13": dict(
    eno=u"Six pièces portent chacune un numéro de repère et une longueur. "
        u"L'atelier débite la plus longue en premier. Produisez la liste des "
        u"numéros de repère dans l'ordre de passage à la scie.",
    att=u"4256, 4207, 4229, 4198, 4183, 4171.",
    dep=u"Les six numéros de repère et les six longueurs correspondantes, "
        u"dans deux listes de même rang.",
    data=u"D_A13_REP / D_A13_LONG",
    don=u"Les numéros de repère sont volontairement décorrélés des longueurs : "
        u"un tri portant sur les repères eux-mêmes donne un ordre différent, "
        u"donc détectable. La réponse est numérique, comme l'exige le checker.",
    mode=u"ExactOrderedList", tol=u"—"),

u"A-17": dict(
    eno=u"Cinq lames de chêne et cinq lames de noyer vous sont fournies dans "
        u"deux listes séparées, repérées par leur longueur. Produisez l'ordre "
        u"de pose du plateau, une essence sur deux en commençant par le chêne.",
    att=u"1245, 1418, 1268, 1463, 1231, 1437, 1287, 1409, 1252, 1481.",
    dep=u"Les longueurs des cinq lames de chêne et des cinq lames de noyer, "
        u"dans deux listes séparées.",
    data=u"D_A17_LG_CHENE / D_A17_LG_NOYER",
    don=u"Les deux essences occupent deux plages de longueur distinctes — "
        u"chêne autour de 1 250, noyer autour de 1 440. L'alternance se "
        u"contrôle donc à la lecture, et une mise bout à bout se repère au "
        u"premier coup d'œil. La réponse est numérique, comme l'exige le "
        u"checker.",
    mode=u"ExactOrderedList", tol=u"—"),

u"A-15": dict(
    mode=u"SingleValue", tol=u"0"),

u"A-30": dict(
    mode=u"SingleValue", tol=u"0"),

u"A-27": dict(
    mode=u"Visuel", tol=u"—",
    limite=u"Le livrable de cet exercice est un texte, et le checker Magpie "
           u"ne sait comparer que des nombres. La validation est donc "
           u"visuelle : le formateur lit les cinq étiquettes. Ramener la "
           u"réponse à un nombre — un total de caractères, par exemple — "
           u"serait une gymnastique imposée par l'outil et non une étape de "
           u"la tâche ; la skill le déconseille explicitement."),

u"A-28": dict(
    mode=u"Visuel", tol=u"—",
    limite=u"Même limite qu'en A-27 : le livrable est une liste de codes en "
           u"minuscules, que le checker ne sait pas comparer. Validation "
           u"visuelle."),
}

JEUX[u"D_A13_REP"] = D_A13_REP
JEUX[u"D_A17_LG_CHENE"] = D_A17_LG_CHENE
JEUX[u"D_A17_LG_NOYER"] = D_A17_LG_NOYER

_fusionner_base = fusionner


def fusionner(exo):
    """Fusion complete : couche pedagogique, puis correctifs du checker."""
    r = _fusionner_base(exo)
    c = CORRECTIFS.get(exo["id"])
    if not c:
        return r
    if c.get(u"eno"):
        r["enonce"] = c[u"eno"]
    if c.get(u"att"):
        r["att"] = c[u"att"]
    if c.get(u"dep"):
        r["depart"] = c[u"dep"]
    if c.get(u"data"):
        r[u"jeu"] = c[u"data"]
    if c.get(u"don"):
        r[u"donnees_note"] = c[u"don"]
    if c.get(u"mode"):
        r["mode"] = c[u"mode"]
    if c.get(u"tol"):
        r["tol"] = c[u"tol"]
    # Un correctif du checker ne REMPLACE la limite que s'il en porte une :
    # sans cette garde, il effacait celle posee par la couche pedagogique.
    if c.get(u"limite"):
        r[u"limite"] = c[u"limite"]
    return r


# ---------------------------------------------------------------------------
# Reponses attendues, relevees sur les jeux de donnees refondus.
# Elles ne sont PAS deduites de tete : voir Documentation/Generateurs/
# controle_reponses.py, qui les recalcule et fait echouer la generation en cas
# d'ecart (skill, « Vérifier avant de livrer », point 2).
# ---------------------------------------------------------------------------

REPONSES = {

u"A-08": dict(
    att=u"11 — le nombre de traverses dont l'écart à 1 200 mm dépasse 5 mm.",
    don=u"28 cotes resserrées autour de 1 200 : impossible de compter à l'œil. "
        u"Les 11 hors-tolérance sont répartis dans les deux sens — 7 trop "
        u"grandes, 4 trop petites — pour que l'oubli de la valeur absolue "
        u"donne 7 au lieu de 11 et se voie donc immédiatement."),

u"A-09": dict(
    att=u"18 — le nombre de hauteurs réellement renseignées.",
    don=u"24 lignes dont 6 non renseignées, dispersées et non groupées en fin "
        u"de liste, pour que le nettoyage ne puisse pas se deviner. Répondre "
        u"24 signale qu'on a mesuré la liste sans la nettoyer."),

u"A-11": dict(
    att=u"Deux longueurs, dans cet ordre : 2 075 mm puis 2 830 mm — celle du quatrième rang, puis celle du dernier.",
    don=u"24 longueurs non ordonnées : ni le rang 4 ni le dernier rang ne se "
        u"repèrent visuellement."),

u"A-12": dict(
    att=u"Trois valeurs, dans cet ordre : 28, 51, 78.",
    don=u"28 valeurs dispersées entre 51 et 78, sans ordre : les extrêmes ne "
        u"sautent pas aux yeux et doivent être extraits par construction."),

u"A-14": dict(
    att=u"12 longueurs : les rangs 0, 3, 6, … 33 du calepinage.",
    don=u"36 lames de longueurs voisines mais toutes distinctes : un décalage "
        u"du motif conserve l'effectif de 12 tout en changeant la réponse. "
        u"C'est pourquoi la validation porte sur les longueurs et non sur le "
        u"seul comptage."),

u"A-15": dict(
    att=u"11 — le nombre de panneaux de plus de 2,50 m², à poser en binôme.",
    don=u"24 surfaces réelles. Aucune ne vaut exactement 2,50 : la plus proche "
        u"est à 2,49, de sorte que l'exercice ne dépende pas du sens de "
        u"l'inégalité, qui n'est pas son objet. La somme des deux groupes doit "
        u"valoir 24, ce qui donne à l'apprenant son propre moyen de contrôle."),

u"A-18": dict(
    att=u"Huit relevés : 466, 419, 448, 433, 471, 405, 459, 424.",
    don=u"28 altitudes non ordonnées : la tranche demandée n'a aucune "
        u"signature visuelle, il faut la prélever."),

u"A-30": dict(
    att=u"16 — le nombre de chutes remises en stock, bornes incluses.",
    don=u"24 longueurs, dont une exactement à 500 et une exactement à 1 500. "
        u"C'est là tout l'intérêt du jeu : bornes incluses la réponse est 16, "
        u"bornes exclues elle tombe à 14. Un jeu de données sans valeur sur la "
        u"borne rendrait les deux montages indiscernables."),
}

_fusionner_correctifs = fusionner


def fusionner(exo):
    """Fusion complete : pedagogie, correctifs checker, puis reponses relevees."""
    r = _fusionner_correctifs(exo)
    rep = REPONSES.get(exo["id"])
    if rep:
        if rep.get(u"att"):
            r["att"] = rep[u"att"]
        if rep.get(u"don"):
            r[u"donnees_note"] = rep[u"don"]
    return r


# ---------------------------------------------------------------------------
# Deux exercices renvoyaient une reponse que le checker ne sait pas comparer :
# A-19 un chemin de branche (texte), A-43 un booleen. Le defaut a echappe au
# premier passage parce que l'audit ne controlait que les couples mode/tolerance,
# pas la NATURE de la reponse. Il le controle desormais.
# ---------------------------------------------------------------------------

CORRECTIFS[u"A-19"] = dict(
    att=u"4 — le nombre de branches du flux.",
    mode=u"SingleValue", tol=u"0")

CORRECTIFS[u"A-43"] = dict(
    att=u"Le volume du solide refermé, non nul — c'est lui qui prouve la "
        u"fermeture : une enveloppe ouverte n'a pas de volume.",
    mode=u"NumericTolerance", tol=u"1",
    don=u"Le tube fourni est ouvert aux deux extrémités. Son volume vaut zéro "
        u"tant qu'il ne l'est pas : la preuve du caractère fermé est donc "
        u"déjà numérique, et il n'y a pas lieu de la traduire en booléen.")
