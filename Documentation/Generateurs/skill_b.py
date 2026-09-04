# -*- coding: utf-8 -*-
"""Couche pedagogique du LOT B, superposee aux fiches d'origine.

Meme demarche que `skill_a.py` : `exos_b.py` n'est pas touche, sa redaction
d'origine reste lisible et comparable. Ce module ajoute ce que la skill
`magpie-conception-exercices` demande et que le lot B n'avait pas, ayant ete
ecrit avant la refonte du 26/08/2026 :

    competence · bloom · contexte · erreur · donnees_note · limite · verdict

et surtout une REPONSE ATTENDUE VERIFIABLE. Les fiches d'origine annoncaient
« l'escalier modelise, le nombre de marches et la valeur de Blondel affiches » :
c'est la description d'un livrable, pas une valeur que le correcteur puisse
comparer.

UN DEFAUT DE CONCEPTION CORRIGE
-------------------------------
Huit exercices du lot etaient declares en `GeometryTolerance`. Or ce mode ne
compare QU'UN SEUL element (contrainte du checker, §8 du journal plugin), et
ces exercices en produisent 96, 130, 24 ou 9. Ils etaient donc incorrigibles
tels quels. Chacun bascule sur une MESURE CARACTERISTIQUE de ce qu'il produit —
aire percee, volume pave, surface developpee, lineaire de nervure — qui est ce
que le metier regarde de toute facon.

Ce n'est pas un contournement : un calepinage se juge sur sa surface, pas sur
la position exacte de son premier panneau.

TOUTES LES VALEURS SONT CALCULEES par `verifier_lot_b.py`.
"""

import math

# ---------------------------------------------------------------------------
# Jeux de donnees
# ---------------------------------------------------------------------------

#: B-01 — deux niveaux, un giron impose, une hauteur de marche visee
D_B01 = dict(hauteur=2850.0, giron=280.0, visee=172.5)

#: B-02 — une main courante, des barreaux, un espacement libre maximal
D_B02 = dict(longueur=3240.0, diametre=16.0, libre_max=110.0)

#: B-03 — une trame de facade et un attracteur, en nombre de mailles
D_B03 = dict(nx=12, ny=8, pas=1200.0, attracteur=(7.5, 3.5),
             rayon_min=50.0, rayon_max=350.0)

#: B-04 — un pavage hexagonal sur une surface rectangulaire
D_B04 = dict(cote=400.0, epaisseur=60.0, largeur=9600.0, profondeur=6400.0)

#: B-05 — une poutre treillis Warren
D_B05 = dict(portee=12000.0, hauteur=900.0, panneaux=8)

#: B-06 et B-07 — un caisson de meuble, et le tiroir qui va dedans
D_B06 = dict(largeur=800.0, hauteur=720.0, profondeur=400.0,
             epaisseur=19.0, rainure=6.0)
D_B07 = dict(jeu_lateral=13.0, jeu_hauteur=2.0)

#: B-08 — six tablettes, entre-deux en progression arithmetique
D_B08 = dict(hauteur=2000.0, tablettes=6, epaisseur=22.0, mini=180.0)

#: B-09 — quatre griffes inclinees autour d'une pierre
D_B09 = dict(griffes=4, hauteur=3.6, inclinaison=12.0, fil=0.9, pierre=5.0)

#: B-10 — un anneau et son motif repetitif
D_B10 = dict(circonference=54.0, modules=12, largeur=4.0)

#: B-11 — des maillons qui se recouvrent le long d'une courbe
D_B11 = dict(courbe=187.5, maillon=4.0, recouvrement=1.2)

#: B-12 — la nomenclature d'un assemblage
D_B12 = dict(pieces=14)

#: B-13 — vingt-deux pieces a debiter dans des plaques
D_B13_PLAQUE = (2800.0, 2070.0)
D_B13_PIECES = [(1200, 600), (900, 450), (1800, 400), (750, 750), (1100, 300),
                (600, 600), (1500, 500), (400, 400), (2000, 350), (850, 650),
                (1300, 450), (700, 700), (1600, 300), (950, 550), (500, 500),
                (1750, 400), (800, 800), (1050, 350), (1400, 600), (650, 450),
                (1900, 300), (1000, 1000)]

#: B-14 — quatorze pieces a numeroter, dans l'ordre de leur saisie
D_B14_POSITIONS = [(1200, 300), (400, 300), (2000, 300), (800, 900),
                   (1600, 300), (400, 900), (2000, 900), (1200, 900),
                   (800, 300), (1600, 900), (400, 1500), (1200, 1500),
                   (2000, 1500), (1600, 1500)]
D_B14_CIBLE = (800, 900)

#: B-15 — trente longueurs a debiter dans des barres de six metres.
#: Jeu choisi pour que la regle du plus grand d'abord n'atteigne PAS la borne
#: theorique : c'est tout l'enseignement de l'exercice.
D_B15_BARRE = 6000.0
D_B15_LONGUEURS = [2250, 1370, 2620, 3930, 840, 970, 3340, 1080, 2470, 3580,
                   890, 3190, 1690, 790, 1040, 2820, 2740, 950, 1830, 1060,
                   3420, 2770, 900, 3490, 1230, 1740, 3820, 3810, 3580, 910]

#: B-16 — un abat-jour a lamelles de largeur variable
D_B16 = dict(lamelles=24, largeur_extremite=15.0, largeur_milieu=45.0,
             hauteur=420.0)

#: B-17 — une coque en arc, et ses nervures
D_B17 = dict(corde=3200.0, fleche=700.0, nervures=9)

#: B-18 — une vis metrique
D_B18 = dict(diametre=10.0, pas=1.5)


# ---------------------------------------------------------------------------
# La couche : ce que la skill demande, et la reponse verifiable
# ---------------------------------------------------------------------------

SKILL_B = {

"B-01": dict(
  competence=u"Dimensionner un ouvrage dont le nombre d'éléments est un "
             u"ENTIER imposé par une contrainte de confort, et recaler les "
             u"dimensions réelles sur cet entier.",
  bloom=u"Appliquer × procédurale",
  contexte=u"L'escalier relie deux niveaux dont la distance est donnée : "
           u"c'est le nombre de contremarches qui s'ajuste, jamais la hauteur "
           u"d'étage.",
  att=u"615,29 mm — la valeur de Blondel, à 0,1 près.",
  erreur=u"Garder la hauteur de marche VISÉE (172,5 mm) au lieu de la "
         u"recalculer sur le nombre entier de contremarches. Blondel donne "
         u"alors 625 mm, également dans la plage admise — l'escalier semble "
         u"conforme, et il n'atteint pas l'étage : 17 × 172,5 fait 2 932 mm "
         u"pour 2 850 disponibles.",
  donnees_note=u"2 850 ÷ 172,5 vaut 16,52 : l'arrondi au plus proche donne 17 "
               u"contremarches, d'où une hauteur réelle de 167,65 mm — sous "
               u"la valeur visée, et toujours dans la plage 165-180. Les deux "
               u"valeurs de Blondel, 615,29 et 625, tiennent toutes deux dans "
               u"l'intervalle admis : le contrôle réglementaire ne rattrape "
               u"pas l'erreur.",
  limite=u"L'exercice valide Blondel. Il ne dit rien de l'échappée, de la "
         u"largeur de passage ni du garde-corps — trois contraintes qui "
         u"peuvent condamner un escalier par ailleurs conforme.",
  mode=u"NumericTolerance", tol=u"0.1"),

"B-02": dict(
  competence=u"Répartir des éléments sous une contrainte d'espacement LIBRE, "
             u"en distinguant l'entraxe de l'espace entre matières.",
  bloom=u"Appliquer × procédurale",
  contexte=u"L'espacement libre d'un garde-corps est une règle de sécurité : "
           u"c'est le vide qui est mesuré, pas la distance d'axe en axe.",
  att=u"25 barreaux, pour un espacement libre de 108 mm.",
  erreur=u"Diviser la longueur par l'espacement libre seul : on obtient "
         u"30 barreaux. Le barreau occupe 16 mm qu'il faut ajouter à chaque "
         u"pas — sinon cinq barreaux de trop sont commandés, et l'espacement "
         u"réel tombe à 92 mm au lieu des 108 possibles.",
  donnees_note=u"3 240 mm de main courante, barreaux de 16 mm, 110 mm de "
               u"libre admis : le calcul juste donne 25 barreaux et 108 mm de "
               u"libre — juste sous la limite, ce qui est le cas réel d'un "
               u"garde-corps optimisé. Le calcul faux en donne 30, soit 20 % "
               u"de matière en trop.",
  limite=u"Le compte suppose des barreaux de section CONSTANTE et une main "
         u"courante droite. Un garde-corps rampant — le long d'un escalier — "
         u"ne se calcule pas ainsi : l'espacement libre s'y mesure "
         u"perpendiculairement à la pente, et le compte change.",
  mode=u"SingleValue", tol=u"0"),

"B-03": dict(
  competence=u"Piloter une variation continue par la distance à un "
             u"attracteur, et en chiffrer l'effet global.",
  bloom=u"Appliquer × procédurale",
  contexte=u"La façade doit laisser passer plus de lumière près de l'atrium. "
           u"Le maître d'ouvrage, lui, achète du vitrage au mètre carré.",
  att=u"13,30 m² d'ouverture au total, à 0,01 près.",
  erreur=u"Prendre le rayon MOYEN et le multiplier par 96 : on obtient "
         u"12,06 m². L'aire varie comme le CARRÉ du rayon, jamais comme le "
         u"rayon — la moyenne des carrés n'est pas le carré de la moyenne, et "
         u"l'écart de 1,24 m² se paie au vitrage.",
  donnees_note=u"96 panneaux, rayon de 50 à 350 mm selon la distance à "
               u"l'attracteur : un rapport de sept sur le rayon, donc de "
               u"quarante-neuf sur l'aire. C'est cette non-linéarité qui rend "
               u"la moyenne trompeuse, et elle l'est toujours dans le même "
               u"sens — par défaut.",
  limite=u"L'exercice chiffre l'aire percée. Il ne vérifie pas que les "
         u"ouvertures restent dans leur panneau : au rayon maximal, 350 mm "
         u"dans une maille de 1 200, la marge est confortable — elle ne le "
         u"serait plus sur une trame plus serrée.",
  mode=u"NumericTolerance", tol=u"0.01"),

"B-04": dict(
  competence=u"Établir combien d'éléments d'une trame non orthogonale "
             u"tiennent dans une emprise donnée.",
  bloom=u"Analyser × procédurale",
  contexte=u"Le bardage hexagonal se commande à l'unité. Le pas d'une trame "
           u"hexagonale n'est pas son côté.",
  att=u"130 hexagones.",
  erreur=u"Diviser l'emprise par le CÔTÉ de l'hexagone au lieu de son pas. "
         u"Une trame hexagonale avance de √3 × côté horizontalement et de "
         u"1,5 × côté verticalement — jamais du côté lui-même. L'erreur donne "
         u"384 hexagones, soit trois fois trop.",
  donnees_note=u"Côté de 400 mm : pas horizontal 692,8 mm, pas vertical "
               u"600 mm. Sur 9 600 × 6 400 mm cela fait 13 × 10 = 130 "
               u"hexagones. Aucun des deux pas n'est un compte rond, et "
               u"aucun ne vaut le côté : l'erreur ne peut pas passer pour un "
               u"arrondi.",
  limite=u"130 est le nombre d'hexagones qui TIENNENT dans l'emprise, pas "
         u"celui des hexagones entiers : les rangs de bord sont coupés. Un "
         u"calepinage réel distingue les modules pleins des chutes de "
         u"rive, et l'exercice ne le fait pas.",
  mode=u"SingleValue", tol=u"0"),

"B-05": dict(
  competence=u"Chiffrer le linéaire d'une structure treillis en distinguant "
             u"ce qui court le long de la portée de ce qui la traverse en "
             u"diagonale.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le tube se commande au mètre. Une diagonale n'a pas la longueur "
           u"du panneau qu'elle traverse.",
  att=u"37,99 m de tube pour les membrures et les diagonales, à 0,01 près.",
  erreur=u"Compter la diagonale comme un panneau : on obtient 36,00 m. Une "
         u"diagonale sur un panneau de 1 500 mm et 900 mm de hauteur mesure "
         u"1 749 mm, pas 1 500 — et il y en a huit. Deux mètres de tube "
         u"manquent à la livraison.",
  donnees_note=u"Portée de 12 000 mm en 8 panneaux de 1 500, hauteur 900 : la "
               u"diagonale fait 1 749,3 mm, soit 17 % de plus que le pas. "
               u"L'écart est assez petit pour qu'on l'oublie, assez grand "
               u"pour manquer sur un chantier.",
  limite=u"Le linéaire annoncé ne compte pas les montants verticaux, qui "
         u"dépendent du schéma retenu — un Warren strict n'en a pas, un "
         u"Warren à montants en a neuf.",
  mode=u"NumericTolerance", tol=u"0.01"),

"B-06": dict(
  competence=u"Chiffrer la matière d'un assemblage en tenant compte des "
             u"recouvrements et des usinages qui la font varier.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le panneau se commande au mètre carré débité. La rainure "
           u"n'enlève pas de matière au fond : elle lui en AJOUTE, puisqu'il "
           u"faut le débiter plus grand.",
  att=u"32,73 dm³ de panneau, à 0,01 près.",
  erreur=u"Débiter le fond aux cotes intérieures nettes, sans la profondeur "
         u"des rainures : 32,40 dm³. Le fond entre DANS la rainure — il doit "
         u"donc mesurer 6 mm de plus de chaque côté, soit 12 mm dans chaque "
         u"dimension. Coupé trop court, il ne tient plus.",
  donnees_note=u"Un caisson de 800 × 720 × 400 en 19 mm, rainure de 6 mm : "
               u"l'écart entre les deux calculs vaut 0,33 dm³, soit 1 %. "
               u"Invisible sur un devis, fatal au montage.",
  limite=u"Le volume est celui du PANNEAU débité, pas celui de la matière "
         u"achetée : le débit se fait dans des plaques de format imposé, et "
         u"la chute de découpe s'y ajoute — de 15 à 30 % selon "
         u"l'imbrication. C'est l'objet de B-13.",
  mode=u"NumericTolerance", tol=u"0.01"),

"B-07": dict(
  competence=u"Appliquer un jeu fonctionnel du bon côté, et le bon nombre de "
             u"fois.",
  bloom=u"Appliquer × procédurale",
  contexte=u"La coulisse demande 13 mm de chaque côté. Un tiroir trop large "
           u"ne rentre pas ; trop étroit, il se met en travers.",
  att=u"736 mm de largeur de tiroir.",
  erreur=u"Ne retrancher le jeu qu'une fois : 749 mm. La coulisse se pose des "
         u"DEUX côtés, et 13 mm de trop suffisent à empêcher le tiroir "
         u"d'entrer. C'est l'erreur de jeu la plus répandue en agencement.",
  donnees_note=u"Caisson de 800 mm en panneaux de 19 : intérieur 762 mm, "
               u"moins deux fois 13 = 736. Les deux réponses, 736 et 749, ne "
               u"diffèrent que de 13 mm — assez peu pour n'être vues qu'au "
               u"montage.",
  limite=u"736 mm est la largeur du CAISSON de tiroir. La façade, elle, "
         u"suit un jeu différent — celui du rainurage entre façades, "
         u"typiquement 3 mm — et ne se déduit pas de ce calcul.",
  mode=u"SingleValue", tol=u"0"),

"B-08": dict(
  competence=u"Répartir des éléments selon une progression imposée en "
             u"respectant une hauteur totale et une valeur de départ.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Une bibliothèque range des livres de plus en plus grands vers "
           u"le haut. La hauteur totale, elle, ne bouge pas.",
  att=u"353,71 mm — le plus grand entre-deux, à 0,01 près.",
  erreur=u"Oublier l'épaisseur des tablettes et répartir 2 000 mm au lieu des "
         u"1 868 mm réellement libres : le plus grand entre-deux monte à "
         u"378,3 mm, et la dernière tablette dépasse du meuble de 132 mm.",
  donnees_note=u"Six tablettes de 22 mm laissent 1 868 mm libres à répartir "
               u"en sept entre-deux, le plus petit valant 180 mm. La raison "
               u"de la progression tombe sur 28,95 mm — jamais un compte "
               u"rond, donc jamais devinable.",
  limite=u"Le plus grand entre-deux dit que la répartition est correcte. Il "
         u"ne dit pas qu'elle est UTILISABLE : une étagère dont le plus "
         u"grand espace dépasse 400 mm fléchit sous charge, et c'est une "
         u"vérification de résistance, pas de géométrie.",
  mode=u"NumericTolerance", tol=u"0.01"),

"B-09": dict(
  competence=u"Chiffrer la matière d'un élément incliné, dont la longueur "
             u"n'est pas sa projection.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le fil d'or se pèse et se facture au millimètre. Une griffe "
           u"inclinée est plus longue que la hauteur qu'elle couvre.",
  att=u"14,72 mm de fil, à 0,01 près.",
  erreur=u"Prendre la hauteur droite : 14,40 mm. Une griffe inclinée de 12° "
         u"est 2,2 % plus longue que sa projection verticale. Sur une pièce "
         u"unique cela ne se voit pas ; sur une série, c'est du fil d'or qui "
         u"manque à chaque montage.",
  donnees_note=u"Quatre griffes de 3,6 mm inclinées à 12° : l'écart avec la "
               u"hauteur droite vaut 0,32 mm au total. À l'échelle de la "
               u"joaillerie, c'est un tiers de diamètre de fil.",
  limite=u"14,72 mm est la longueur de fil DÉVELOPPÉE. Le sertissage écrase "
         u"la griffe sur la pierre et la raccourcit de quelques dixièmes : "
         u"un joaillier ajoute une surlongueur d'atelier que ce calcul "
         u"n'anticipe pas.",
  mode=u"NumericTolerance", tol=u"0.01"),

"B-10": dict(
  competence=u"Répartir un motif répétitif sur un développé, en distinguant "
             u"la circonférence du diamètre.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le motif doit se refermer sur lui-même. Un raccord faux se voit "
           u"immédiatement, et se voit toujours au même endroit.",
  att=u"4,50 mm — la largeur d'un module, à 0,01 près.",
  erreur=u"Diviser le DIAMÈTRE par le nombre de modules : 1,43 mm. La taille "
         u"d'un anneau est une circonférence ; la confondre avec un diamètre "
         u"divise le motif par π, et les douze modules ne couvrent plus qu'un "
         u"tiers du tour.",
  donnees_note=u"Une circonférence de 54 mm en 12 modules donne exactement "
               u"4,5 mm : un compte rond, à dessein — il rend le raccord "
               u"vérifiable à la règle, et l'erreur d'un facteur π immédiate "
               u"à voir.",
  limite=u"Le calcul porte sur le développé. Appliqué sur l'anneau, le motif "
         u"subit la courbure : sa lisibilité dépend alors de la largeur de "
         u"l'anneau, que l'exercice ne juge pas.",
  mode=u"NumericTolerance", tol=u"0.01"),

"B-11": dict(
  competence=u"Compter des éléments qui se recouvrent, où le pas n'est pas "
             u"la taille de l'élément.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Les maillons d'une chaîne s'enfilent l'un dans l'autre : le pas "
           u"est plus court que le maillon, sans quoi la chaîne se casse.",
  att=u"66 maillons.",
  erreur=u"Diviser la longueur par la taille du maillon : 46. Le "
         u"recouvrement de 1,2 mm ramène le pas à 2,8 mm — il faut donc "
         u"43 % de maillons en plus. Une chaîne commandée sur le calcul faux "
         u"arrive vingt maillons trop courte.",
  donnees_note=u"187,5 mm de courbe, maillons de 4 mm recouverts de 1,2 : le "
               u"pas tombe à 2,8 mm. Les deux réponses, 46 et 66, sont "
               u"éloignées de moitié — impossible de confondre les deux "
               u"méthodes.",
  limite=u"66 maillons suivent la courbe THÉORIQUE. Une chaîne réelle "
         u"pend : sa ligne est une chaînette, plus longue que la courbe "
         u"dessinée, et le compte monte. L'exercice traite le cas guidé, "
         u"pas le cas suspendu.",
  mode=u"SingleValue", tol=u"0"),

"B-12": dict(
  competence=u"Produire un livrable d'échange dont on connaît la structure "
             u"avant de l'ouvrir.",
  bloom=u"Appliquer × procédurale",
  contexte=u"La nomenclature part au bureau des méthodes, qui l'importe "
           u"automatiquement. Un fichier mal structuré n'est pas rejeté : il "
           u"est importé de travers.",
  att=u"15 lignes — quatorze pièces, plus l'en-tête.",
  erreur=u"Oublier la ligne d'en-tête : la première pièce est alors lue "
         u"comme un nom de colonne et disparaît de la nomenclature, sans "
         u"message.",
  donnees_note=u"Quatorze pièces : les trois réponses possibles — 14, 15 et "
               u"le nombre de lignes du modèle source — sont distinctes. "
               u"C'est le même contrôle que QT-05, appliqué à un assemblage "
               u"plutôt qu'à un débit : la répétition espacée est "
               u"intentionnelle.",
  limite=u"Quinze lignes valident la STRUCTURE du fichier, pas son "
         u"encodage. Un CSV français ouvert par un tableur anglo-saxon "
         u"perd ses séparateurs décimaux — défaut classique que le "
         u"comptage de lignes ne voit pas.",
  mode=u"SingleValue", tol=u"0"),

"B-13": dict(
  competence=u"Estimer un taux de chute à partir des surfaces, en sachant "
             u"que c'est un MINORANT et pourquoi.",
  bloom=u"Analyser × procédurale",
  contexte=u"La plaque se commande à l'unité. Le taux de chute décide de la "
           u"marge, et il est toujours annoncé optimiste.",
  att=u"31,00 % de chute, à 0,01 près.",
  erreur=u"Annoncer ce taux comme celui du débit réel. Il ne compte que la "
         u"surface : le placement, lui, ajoute sa propre chute, et le taux "
         u"observé en atelier est toujours supérieur. Un devis calé sur "
         u"31 % perd de l'argent à chaque plaque.",
  donnees_note=u"22 pièces pour 12,00 m² dans des plaques de 5,80 m² : trois "
               u"plaques suffisent en surface, d'où 31 % de chute théorique. "
               u"Le rapport 11 997 500 ÷ 5 796 000 vaut 2,07 — juste au-dessus "
               u"de deux, ce qui rend l'arrondi au supérieur décisif.",
  limite=u"Le taux calculé est un plancher. Seule une imbrication réelle "
         u"donne le taux vrai, et FA-01 dit pourquoi aucune ne peut faire "
         u"mieux que ce plancher.",
  mode=u"NumericTolerance", tol=u"0.01"),

"B-14": dict(
  competence=u"Ordonner des éléments selon un critère composé, en respectant "
             u"l'ordre de priorité des critères.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le repérage suit l'ordre de pose : rangée du bas d'abord, de "
           u"gauche à droite. Le poseur lit les repères dans cet ordre-là.",
  att=u"7 — le rang de la pièce située à 800 mm en abscisse et 900 mm en "
      u"ordonnée.",
  erreur=u"Trier d'abord par abscisse : la pièce reçoit alors le rang 5. "
         u"L'ordre des critères n'est pas commutatif — trier par colonne "
         u"puis par rangée numérote le mur de haut en bas par bandes "
         u"verticales, et le poseur ne s'y retrouve plus.",
  donnees_note=u"Quatorze pièces sur trois rangées, saisies dans le désordre. "
               u"Pour la pièce visée, les trois lectures donnent trois rangs "
               u"différents : 7 dans l'ordre demandé, 5 en triant par "
               u"colonne, 4 dans l'ordre de saisie. Aucune confusion "
               u"possible.",
  limite=u"Le rang dépend de l'ordre des critères, qui est une CONVENTION "
         u"d'atelier. L'exercice en impose une ; un autre atelier "
         u"numéroterait autrement, et aurait raison. Ce qui se vérifie "
         u"est l'application de la convention, pas son bien-fondé.",
  mode=u"SingleValue", tol=u"0"),

"B-15": dict(
  competence=u"Appliquer une heuristique de découpe et mesurer l'écart entre "
             u"son résultat et la borne théorique.",
  bloom=u"Évaluer × procédurale",
  contexte=u"La barre se commande à l'unité. La règle du plus grand d'abord "
           u"est celle de l'atelier, parce qu'elle se tient de tête.",
  att=u"12 barres.",
  erreur=u"Diviser la longueur totale par celle d'une barre : 11. C'est la "
         u"BORNE théorique, et aucune découpe ne l'atteint ici — les "
         u"longueurs ne se combinent pas pour remplir onze barres. Annoncer "
         u"11 revient à promettre un rendement qu'aucun débit ne donnera.",
  donnees_note=u"30 longueurs pour 65 120 mm, soit 10,85 barres en surface : "
               u"la borne est 11, et la règle du plus grand d'abord en "
               u"consomme 12. L'écart d'une seule barre est le cas "
               u"intéressant — assez petit pour qu'on croie à une erreur de "
               u"calcul, assez réel pour se payer.",
  limite=u"12 est le résultat de CETTE heuristique. Un placement optimal "
         u"pourrait faire mieux — le trouver est un problème dont on ne "
         u"connaît pas de solution rapide, et c'est précisément pourquoi "
         u"l'atelier emploie une règle simple.",
  mode=u"SingleValue", tol=u"0"),

"B-16": dict(
  competence=u"Chiffrer une surface développée dont une dimension varie "
             u"continûment.",
  bloom=u"Appliquer × procédurale",
  contexte=u"La tôle de l'abat-jour se commande à plat, au mètre carré. La "
           u"lamelle est large au milieu et étroite aux extrémités.",
  att=u"0,3024 m² de surface développée, à 0,0001 près.",
  erreur=u"Prendre la largeur maximale partout : 0,4536 m², soit 50 % de "
         u"trop. La largeur varie linéairement — sa moyenne est la "
         u"demi-somme des extrêmes, pas le maximum.",
  donnees_note=u"24 lamelles de 420 mm, largeur de 15 à 45 mm : la largeur "
               u"moyenne vaut 30 mm, exactement le tiers de la somme des "
               u"extrêmes plus le minimum. Le rapport de 1,5 entre les deux "
               u"réponses est trop grand pour passer inaperçu sur une "
               u"commande.",
  limite=u"0,3024 m² est la surface DÉVELOPPÉE à plat. La lamelle cintrée "
         u"garde cette surface, mais son flan de découpe doit ajouter les "
         u"pertes de mise en forme — quelques millimètres par bord, selon "
         u"le matériau.",
  mode=u"NumericTolerance", tol=u"0.0001"),

"B-17": dict(
  competence=u"Mesurer le développé d'un élément courbe, et non sa corde.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Les nervures se débitent à plat puis se cintrent. C'est leur "
           u"longueur développée qu'on commande.",
  att=u"32,34 m de nervure au total, à 0,01 près.",
  erreur=u"Prendre la corde : 28,80 m. L'arc d'une coque de 3 200 mm de "
         u"corde et 700 mm de flèche mesure 3 594 mm, soit 12 % de plus. "
         u"Trois mètres et demi de nervure manqueraient à la livraison — et "
         u"le manque se répartit sur les neuf pièces, donc se voit tard.",
  donnees_note=u"Une flèche de 700 pour 3 200 de corde donne un rayon de "
               u"2 179 mm : une coque franchement courbe, où l'écart entre "
               u"arc et corde est net sans être caricatural.",
  limite=u"32,34 m est le linéaire des nervures SUR LA SURFACE. Une "
         u"nervure a une épaisseur : son développé réel, celui qui part en "
         u"découpe, se mesure sur sa fibre neutre et dépasse cette valeur "
         u"d'autant que la coque est courbe.",
  mode=u"NumericTolerance", tol=u"0.01"),

"B-18": dict(
  competence=u"Retrouver une cote fonctionnelle à partir d'une norme, plutôt "
             u"que de la mesurer sur un modèle.",
  bloom=u"Appliquer × conceptuelle",
  contexte=u"Le diamètre à fond de filet décide de la section résistante de "
           u"la vis. Il ne se lit pas sur la désignation.",
  att=u"8,16 mm — le diamètre à fond de filet, à 0,001 près.",
  erreur=u"Retrancher le pas au diamètre nominal : 8,50 mm. Le profil ISO "
         u"retire 1,2269 fois le pas, pas une fois — le filet est "
         u"triangulaire à 60° et tronqué. L'erreur surestime la section "
         u"résistante de 8 %, ce qui se traduit par une vis qu'on croit plus "
         u"solide qu'elle n'est.",
  donnees_note=u"M10 au pas de 1,5 : les trois lectures possibles donnent "
               u"8,16 (juste), 8,50 (pas retranché une fois) et 7,40 (deux "
               u"fois la hauteur théorique du triangle non tronqué). Trois "
               u"valeurs distinctes, dont deux plausibles.",
  limite=u"Le diamètre à fond de filet n'est pas le diamètre de la section "
         u"résistante, qui se calcule sur une moyenne avec le diamètre sur "
         u"flancs. L'exercice s'arrête au premier.",
  mode=u"NumericTolerance", tol=u"0.001"),

}


def fusionner(exo):
    """Rend la fiche d'origine enrichie de la couche pedagogique."""
    r = dict(exo)
    couche = SKILL_B.get(exo["id"])
    if not couche:
        return r
    for cle, valeur in couche.items():
        r[cle] = valeur
    r.setdefault(u"verdict", u"competence")
    r.setdefault(u"obj", exo.get("obj", u""))
    r[u"competence"] = couche.get(u"competence", exo.get("obj", u""))
    return r
