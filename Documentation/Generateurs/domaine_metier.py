# -*- coding: utf-8 -*-
"""Domaines 4, 5 et 10 — geometrie restante, quantitatifs, fabrication.

Trois lots, tous a reponse numerique : ce sont les notions restantes qui se
pretent le mieux a l'auto-correction, et elles couvrent les gestes que le
metier demande le plus souvent — coter, metrer, chiffrer, imbriquer, deplier.

    GP  geometrie parametrique : plan cote, modele 3D, maillages et SubD
    QT  quantitatifs, chiffrage et export de donnees
    FA  aide a la fabrication : imbrication et mise a plat

VERSION : v0.1-260828
"""

VERSION = u"v0.1-260828"


# ---------------------------------------------------------------------------
# Jeux de donnees
# ---------------------------------------------------------------------------

# QT-01 — metre d'un plancher bois : sections et longueurs des solives
D_QT01_SECT = [(63, 175), (63, 200), (75, 225), (63, 175), (75, 225),
               (63, 200), (63, 175), (75, 200), (63, 225), (63, 175),
               (75, 225), (63, 200), (63, 175), (75, 200), (63, 225),
               (63, 200), (75, 225), (63, 175), (63, 200), (75, 200)]
D_QT01_LONG = [4180, 4620, 5240, 4180, 5240, 4620, 4180, 4870, 5510,
               4180, 5240, 4620, 4180, 4870, 5510, 4620, 5240, 4180,
               4620, 4870]

# QT-02 — bordereau : prix unitaires au metre lineaire, par section
D_QT02_PRIX = {(63, 175): 6.80, (63, 200): 7.90, (63, 225): 9.10,
               (75, 200): 9.40, (75, 225): 10.70}

# QT-03 — nomenclature de menuiseries a exporter
D_QT03_REP = [u"MEN-01", u"MEN-02", u"MEN-03", u"MEN-04", u"MEN-05",
              u"MEN-06", u"MEN-07", u"MEN-08", u"MEN-09", u"MEN-10",
              u"MEN-11", u"MEN-12", u"MEN-13", u"MEN-14", u"MEN-15",
              u"MEN-16", u"MEN-17", u"MEN-18"]
D_QT03_L = [1200, 900, 1800, 1200, 600, 2400, 900, 1500, 1200,
            1800, 600, 2100, 1500, 900, 1200, 2400, 1800, 1500]
D_QT03_H = [2150, 2150, 2400, 1450, 1450, 2400, 2150, 2400, 1450,
            2150, 1450, 2400, 2150, 1450, 2400, 2150, 1450, 2400]

# FA-01 — pieces a imbriquer dans des panneaux de 2500 x 1250 mm
D_FA01_L = [1180, 860, 1420, 640, 980, 1560, 720, 1120, 890, 1340,
            600, 1480, 760, 1050, 920, 1260, 680, 1390, 840, 1150]
D_FA01_H = [420, 610, 380, 540, 460, 320, 580, 400, 520, 350,
            630, 290, 560, 440, 490, 370, 600, 330, 510, 430]

# FA-02 — cone tronque a derouler : rayons et hauteur, en mm
D_FA02 = (180.0, 95.0, 340.0)      # grand rayon, petit rayon, hauteur


LOT_GP = [

dict(id=u"GP-01", titre=u"Un plan coté qui suit ses paramètres",
     them=u"GP1 · Plan paramétrique",
     ref=u"REF-065, REF-066",
     niv=u"Débutant", duree=25, prereq=u"A-34",
     competence=u"Produire un tracé 2D dont les cotes se mettent à jour avec "
                u"la géométrie, plutôt que d'être écrites à côté.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Un plan de réservation part au gros œuvre ; la dimension "
              u"bouge encore, et une cote fausse coûte un percement au "
              u"mauvais endroit.",
     obj=u"Produire un tracé 2D dont les cotes se mettent à jour avec la "
         u"géométrie, plutôt que d'être écrites à côté.",
     enonce=u"La réservation est rectangulaire, avec un congé de 60 mm à "
            u"chaque angle. Produisez son tracé pour une réservation de "
            u"1 400 × 850 mm, et donnez le périmètre développé du contour.",
     depart=u"Deux valeurs réglables pour la largeur et la hauteur, et une "
            u"troisième pour le rayon de congé.",
     att=u"Le périmètre du contour congé compris, à 0,1 mm près.",
     erreur=u"Calculer le périmètre du rectangle nu et y ajouter les quatre "
            u"quarts de cercle, sans retrancher ce que les congés ont "
            u"supprimé des côtés droits. On obtient une valeur trop grande "
            u"d'environ 4 × (2r − πr/2), soit une erreur systématique que le "
            u"contexte ne signale pas.",
     donnees_note=u"Le congé de 60 mm est assez grand pour que l'oubli du "
                  u"retranchement se voie au dixième de millimètre, et assez "
                  u"petit pour rester une réservation plausible.",
     mode=u"NumericTolerance", tol=u"0,1", nb=6,
     comp=u"Rectangle, Length, Panel",
     etapes=[u"Construire le rectangle à partir des deux valeurs réglables.",
             u"Appliquer le congé par le paramètre du composant de tracé "
             u"plutôt qu'en raccordant les angles après coup.",
             u"Mesurer la longueur du contour obtenu.",
             u"Faire varier la largeur et vérifier que la cote suit.",
             u"Contrôler le résultat sur un cas connu : congé nul, le "
             u"périmètre doit valoir deux fois la somme des côtés."],
     pieges=[u"Congé appliqué après coup : le contour cesse d'être une seule "
             u"courbe et la mesure porte sur des morceaux.",
             u"Rayon de congé supérieur à la moitié du petit côté : le tracé "
             u"devient impossible et le composant se met en défaut."],
     var=[u"Ajouter une cotation automatique de la largeur et vérifier "
          u"qu'elle suit la valeur réglable.",
          u"Passer le congé à zéro et retrouver le périmètre du rectangle."],
     gamif=u"G-02 Barre de progression",
     bareme=u"1 point si le périmètre est juste à 0,1 mm près et si la cote "
            u"suit une modification de largeur.",
     verdict=u"competence"),

dict(id=u"GP-02", titre=u"Un modèle paramétrique de bout en bout",
     them=u"GP2 · Synthèse géométrie",
     ref=u"REF-073",
     niv=u"Intermédiaire", duree=45, prereq=u"GP-01, A-41",
     competence=u"Enchaîner tracé, surface et volume dans une définition "
                u"unique dont un seul paramètre commande l'ensemble.",
     bloom=u"Créer × procédurale",
     contexte=u"Un escalier droit doit être chiffré en volume de béton avant "
              u"que sa hauteur d'étage soit figée.",
     obj=u"Enchaîner tracé, surface et volume dans une définition unique dont "
         u"un seul paramètre commande l'ensemble.",
     enonce=u"L'escalier fait 1 100 mm de large, avec un giron de 280 mm et "
            u"une paillasse de 150 mm d'épaisseur. Pour une hauteur d'étage "
            u"de 2 700 mm et des marches de 175 mm, produisez le volume de "
            u"béton, en mètres cubes.",
     depart=u"Trois valeurs réglables : hauteur d'étage, hauteur de marche "
            u"visée et giron.",
     att=u"Le volume de béton, en mètres cubes, à 0,001 près.",
     erreur=u"Prendre 2 700 ÷ 175 = 15,43 marches et arrondir au plus proche. "
            u"Un escalier a un nombre entier de contremarches, et c'est la "
            u"hauteur de marche qui s'ajuste, pas la hauteur d'étage. "
            u"Arrondir la marche au lieu du compte donne un escalier qui "
            u"n'arrive pas au niveau.",
     donnees_note=u"2 700 n'est pas divisible par 175 : c'est le cas normal, "
                  u"et c'est ce qui oblige à comprendre lequel des deux "
                  u"nombres est la donnée et lequel est le résultat.",
     mode=u"NumericTolerance", tol=u"0,001", nb=9,
     comp=u"Series, Rectangle, Extrude, Solid Union, Volume, Panel",
     etapes=[u"Établir le nombre de contremarches : hauteur d'étage divisée "
             u"par la hauteur visée, arrondi à l'entier le plus proche.",
             u"En déduire la hauteur de marche réelle : hauteur d'étage "
             u"divisée par ce nombre entier.",
             u"Répartir les marches par une suite régulière.",
             u"Construire la paillasse et les marches, les réunir en un "
             u"solide unique.",
             u"Mesurer le volume et convertir en mètres cubes."],
     pieges=[u"Réunir les volumes sans booléenne : les recouvrements sont "
             u"comptés deux fois.",
             u"Oublier que la dernière contremarche arrive au niveau fini, "
             u"et poser une marche de trop."],
     var=[u"Faire varier la hauteur d'étage et vérifier que le nombre de "
          u"marches se recale seul.",
          u"Ajouter un palier intermédiaire et reprendre le calcul."],
     gamif=u"G-25 Projet jalonné",
     bareme=u"Grille : nombre de marches juste (1), hauteur réelle recalculée "
            u"(1), volume juste (2).",
     verdict=u"competence"),

dict(id=u"GP-03", titre=u"Un maillage qu'on peut imprimer",
     them=u"GP3 · Maillages et SubD",
     ref=u"REF-074, REF-075, REF-076",
     niv=u"Perfectionnement", duree=30, prereq=u"RH-08",
     competence=u"Produire un maillage à partir d'une surface, en maîtriser "
                u"la finesse, et le rendre exploitable.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Une pièce de forme libre part en impression : le trancheur "
              u"n'accepte qu'un maillage fermé, et la finesse décide de la "
              u"qualité comme du poids du fichier.",
     obj=u"Produire un maillage à partir d'une surface, en maîtriser la "
         u"finesse, et le rendre exploitable.",
     enonce=u"La surface fournie doit devenir un maillage fermé dont l'écart "
            u"à la surface d'origine ne dépasse nulle part 0,2 mm. Donnez le "
            u"nombre de faces du maillage obtenu.",
     depart=u"Un fichier contenant la surface fermée d'origine.",
     att=u"Le nombre de faces du maillage respectant l'écart demandé.",
     erreur=u"Augmenter la densité jusqu'à ce que « ça ait l'air bien ». "
            u"L'écart maximal est un réglage explicite : à l'œil, on produit "
            u"soit un maillage grossier qui passe pour lisse à l'écran, soit "
            u"un maillage inutilement lourd.",
     donnees_note=u"La surface présente une zone de forte courbure et une "
                   u"zone plane : un maillage à densité uniforme y est "
                   u"toujours mauvais quelque part, ce qui oblige à passer "
                   u"par le critère d'écart.",
     limite=u"Le nombre de faces dépend de la version de Rhino et du "
            u"mailleur : la correction accepte une plage plutôt qu'une "
            u"valeur unique. C'est le respect du critère d'écart qui est "
            u"évalué, pas le compte exact.",
     mode=u"NumericTolerance", tol=u"5 %", nb=6,
     comp=u"Mesh Brep, Mesh Join, Face Count, Panel",
     etapes=[u"Mailler la surface en fixant l'écart maximal, non la densité.",
             u"Vérifier que le maillage est fermé et sans face dégénérée.",
             u"Réparer les jonctions si le maillage sort en morceaux.",
             u"Compter les faces.",
             u"Contrôler le poids du fichier exporté : c'est la contrepartie "
             u"directe de la finesse."],
     pieges=[u"Régler la densité au lieu de l'écart : le résultat n'est plus "
             u"contrôlable.",
             u"Maillage en plusieurs morceaux non joints : il paraît fermé et "
             u"ne l'est pas."],
     var=[u"Doubler l'écart admis et mesurer le gain en nombre de faces.",
          u"Lisser le maillage et vérifier ce que le lissage fait à l'écart."],
     gamif=u"G-06 Cible et précision",
     bareme=u"1 point si l'écart maximal est respecté et le maillage fermé.",
     verdict=u"competence"),

dict(id=u"GP-04", titre=u"SubD ou NURBS ?",
     them=u"GP3 · Maillages et SubD",
     ref=u"REF-077, REF-078",
     niv=u"Perfectionnement", duree=7, prereq=u"GP-03",
     competence=u"—", bloom=u"Évaluer × conceptuelle",
     contexte=u"Une poignée de meuble doit être dessinée en forme libre, puis "
              u"usinée.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Vous devez dessiner une poignée de forme libre, qui sera "
               u"ensuite usinée à partir d'un modèle exact. Par quoi "
               u"commencez-vous ?\n"
               u"a) Directement en NURBS, puisque c'est ce qu'il faut à la "
               u"fin.\n"
               u"b) En SubD pour la recherche de forme, converti en NURBS "
               u"pour l'usinage. ← réponse\n"
               u"c) En maillage, plus simple à déformer.\n"
               u"d) Peu importe, les trois sont équivalents.\n\n"
               u"Valeur diagnostique : (a) est le réflexe de qui connaît la "
               u"contrainte de sortie et pas les outils de forme — on y passe "
               u"un temps considérable à recaler des points de contrôle. (c) "
               u"donne une forme facile à modeler et impossible à usiner "
               u"proprement. La bonne réponse tient à ce que SubD et NURBS ne "
               u"s'opposent pas : l'un sert la conception, l'autre la "
               u"fabrication, et la conversion est prévue pour."),
]


LOT_QT = [

dict(id=u"QT-01", titre=u"Le métré d'un plancher bois",
     them=u"QT1 · Quantitatifs et chiffrage",
     ref=u"REF-082, REF-084",
     niv=u"Intermédiaire", duree=25, prereq=u"A-47",
     competence=u"Établir un métré à partir de sections et de longueurs, en "
                u"distinguant les grandeurs qui s'additionnent de celles qui "
                u"ne s'additionnent pas.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Un plancher bois se commande au volume de bois, mais se pose "
              u"au linéaire : le métré doit rendre les deux.",
     obj=u"Établir un métré à partir de sections et de longueurs, en "
         u"distinguant les grandeurs qui s'additionnent de celles qui ne "
         u"s'additionnent pas.",
     enonce=u"Les 20 solives du plancher vous sont fournies avec leur section "
            u"et leur longueur. Donnez le volume total de bois, en mètres "
            u"cubes.",
     depart=u"Les 20 sections, en millimètres, et les 20 longueurs "
            u"correspondantes, en millimètres.",
     att=u"Le volume total de bois, en mètres cubes, à 0,0001 près.",
     erreur=u"Multiplier la section moyenne par la longueur totale. Les "
            u"sections varient, et la moyenne ne rend pas le produit : "
            u"l'écart est faible, l'ordre de grandeur reste juste, et le "
            u"chiffrage est faux de quelques pour cent — le genre d'erreur "
            u"qu'on ne voit jamais.",
     donnees_note=u"Cinq sections courantes de charpente, réparties de façon "
                  u"que la corrélation entre section et longueur soit "
                  u"positive : la moyenne sous-estime alors le volume, "
                  u"toujours dans le même sens.",
     mode=u"NumericTolerance", tol=u"0,0001", nb=7,
     comp=u"Multiplication, Mass Addition, Division, Panel",
     etapes=[u"Calculer l'aire de chaque section, en millimètres carrés.",
             u"Multiplier chaque aire par la longueur de SA solive, terme à "
             u"terme.",
             u"Sommer les vingt volumes.",
             u"Convertir en mètres cubes : diviser par un milliard.",
             u"Contrôler l'ordre de grandeur : un plancher de cette taille "
             u"représente quelques dixièmes de mètre cube."],
     pieges=[u"Appariement des deux listes : sections et longueurs doivent "
             u"rester au même rang.",
             u"Conversion : un mètre cube vaut un milliard de millimètres "
             u"cubes, pas un million."],
     var=[u"Ajouter 10 % de chutes et refaire le chiffrage.",
          u"Sortir aussi le linéaire total et comparer les deux unités."],
     gamif=u"G-01 Score visible",
     bareme=u"1 point si le volume est juste à 0,0001 m³ près.",
     verdict=u"competence"),

dict(id=u"QT-02", titre=u"Du métré au prix",
     them=u"QT1 · Quantitatifs et chiffrage",
     ref=u"REF-083",
     niv=u"Intermédiaire", duree=25, prereq=u"QT-01",
     competence=u"Croiser un métré avec un bordereau de prix pour obtenir un "
                u"montant, sans apparier les mauvaises lignes.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le bordereau du fournisseur donne un prix au mètre linéaire "
              u"par section ; le métré donne des longueurs par solive.",
     obj=u"Croiser un métré avec un bordereau de prix pour obtenir un "
         u"montant, sans apparier les mauvaises lignes.",
     enonce=u"Le bordereau fournit un prix au mètre linéaire pour chacune des "
            u"cinq sections. Donnez le montant total du plancher, en euros.",
     depart=u"Les 20 solives avec leur section et leur longueur, et le "
            u"bordereau des cinq prix unitaires par section.",
     att=u"Le montant total, en euros, à 0,01 près.",
     erreur=u"Apparier le bordereau aux solives par leur rang plutôt que par "
            u"leur section. Il y a vingt solives et cinq prix : un "
            u"appariement par rang donne silencieusement un résultat, "
            u"calculé sur le mauvais prix répété — c'est le comportement par "
            u"défaut vu en A-24, appliqué ici à de l'argent.",
     donnees_note=u"Vingt solives pour cinq sections : le déséquilibre est "
                  u"volontaire, c'est lui qui rend l'erreur d'appariement "
                  u"possible et détectable.",
     mode=u"NumericTolerance", tol=u"0,01", nb=8,
     comp=u"Member Index, List Item, Multiplication, Mass Addition, Panel",
     etapes=[u"Convertir les longueurs en mètres.",
             u"Pour chaque solive, retrouver le RANG de sa section dans le "
             u"bordereau — c'est cet appariement-là qui compte.",
             u"Extraire le prix correspondant à ce rang.",
             u"Multiplier prix par longueur, solive par solive.",
             u"Sommer, et contrôler par un ordre de grandeur : longueur "
             u"totale multipliée par un prix moyen."],
     pieges=[u"Laisser les deux listes s'apparier par défaut.",
             u"Oublier la conversion en mètres : le prix est au mètre "
             u"linéaire, les longueurs sont en millimètres."],
     var=[u"Appliquer une remise de 8 % au-delà de 100 mètres linéaires.",
          u"Sortir le montant par section plutôt que le total."],
     gamif=u"G-21 Optimisation comparée",
     bareme=u"1 point si le montant est juste à 0,01 € près.",
     verdict=u"competence"),

dict(id=u"QT-03", titre=u"Une nomenclature exportable",
     them=u"QT2 · Export de données",
     ref=u"REF-085, REF-086, REF-087",
     niv=u"Intermédiaire", duree=30, prereq=u"A-27",
     competence=u"Mettre en forme des données de projet en un tableau "
                u"exportable, colonne par colonne, et le sortir en fichier.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le bureau d'études attend la nomenclature des menuiseries au "
              u"format tableur, pour la reprendre dans son chiffrage.",
     obj=u"Mettre en forme des données de projet en un tableau exportable, "
         u"colonne par colonne, et le sortir en fichier.",
     enonce=u"Les 18 menuiseries vous sont fournies avec leur repère, leur "
            u"largeur et leur hauteur. Produisez le tableau à quatre "
            u"colonnes — repère, largeur, hauteur, surface — et exportez-le "
            u"en CSV. Donnez la surface totale, en mètres carrés.",
     depart=u"Les 18 repères, les 18 largeurs et les 18 hauteurs, en "
            u"millimètres.",
     att=u"La surface totale des menuiseries, en mètres carrés, à 0,01 près.",
     erreur=u"Construire le tableau ligne par ligne en concaténant tout dans "
            u"une seule chaîne. Le fichier s'ouvre, et le tableur voit une "
            u"seule colonne : c'est le séparateur qui fait les colonnes, et "
            u"il faut décider lequel avant d'écrire quoi que ce soit.",
     donnees_note=u"Dix-huit menuiseries de dimensions courantes, avec des "
                  u"répétitions : le tableau doit rester lisible et le total "
                  u"vérifiable à la main sur quelques lignes.",
     limite=u"L'écriture du fichier elle-même n'est pas auto-corrigeable : "
            u"c'est la surface totale qui est validée. Le formateur ouvre le "
            u"CSV pour juger la mise en forme.",
     mode=u"NumericTolerance", tol=u"0,01", nb=9,
     comp=u"Concatenate, Text Join, Write File, Multiplication, Mass Addition",
     etapes=[u"Calculer la surface de chaque menuiserie, en mètres carrés.",
             u"Choisir le séparateur : le point-virgule s'impose en contexte "
             u"francophone, la virgule servant déjà de séparateur décimal.",
             u"Assembler chaque ligne en joignant les quatre valeurs par ce "
             u"séparateur.",
             u"Ajouter la ligne d'en-tête, puis écrire le fichier.",
             u"Ouvrir le CSV dans un tableur pour vérifier que les colonnes "
             u"se séparent bien."],
     pieges=[u"Virgule décimale et virgule séparatrice dans le même fichier : "
             u"chaque nombre décimal casse une ligne en deux colonnes.",
             u"Oublier l'en-tête : le tableur prend la première menuiserie "
             u"pour un titre."],
     var=[u"Ajouter une colonne de type d'ouvrant et trier par type.",
          u"Produire aussi un récapitulatif par dimension."],
     gamif=u"G-16 Enquête documentaire",
     bareme=u"1 point si la surface totale est juste et si le CSV s'ouvre en "
            u"quatre colonnes distinctes.",
     verdict=u"competence"),
]


LOT_FA = [

dict(id=u"FA-01", titre=u"Combien de panneaux pour ce débit",
     them=u"FA1 · Imbrication",
     ref=u"REF-113, REF-114",
     niv=u"Perfectionnement", duree=35, prereq=u"QT-01",
     competence=u"Estimer le nombre de panneaux nécessaires à un débit et "
                u"chiffrer la chute, avant toute imbrication réelle.",
     bloom=u"Analyser × procédurale",
     contexte=u"Le débit part sur une découpeuse à commande numérique ; le "
              u"panneau brut mesure 2 500 × 1 250 mm et se commande à "
              u"l'unité.",
     obj=u"Estimer le nombre de panneaux nécessaires à un débit et chiffrer "
         u"la chute, avant toute imbrication réelle.",
     enonce=u"Les 20 pièces à débiter vous sont fournies avec leurs "
            u"dimensions. Donnez le nombre minimal théorique de panneaux, "
            u"c'est-à-dire celui qu'imposerait déjà la seule surface, avant "
            u"toute contrainte de placement.",
     depart=u"Les 20 longueurs et les 20 hauteurs, en millimètres, et les "
            u"dimensions du panneau brut.",
     att=u"Le nombre minimal théorique de panneaux, arrondi au supérieur.",
     erreur=u"Arrondir le rapport de surfaces au plus proche. Un panneau se "
            u"commande entier : il en faut au moins autant que la surface "
            u"l'exige, donc un arrondi au supérieur. C'est la même règle "
            u"qu'en A-06, appliquée à un approvisionnement.",
     donnees_note=u"Vingt pièces de dimensions réalistes pour du mobilier, "
                  u"dont la surface totale tombe volontairement peu après un "
                  u"nombre entier de panneaux : arrondir au plus proche "
                  u"donnerait un panneau de moins, et le débit serait "
                  u"incomplet.",
     limite=u"Le nombre RÉEL de panneaux dépend de l'imbrication, qui relève "
            u"d'un plugin dédié et ne se calcule pas ici. C'est le minorant "
            u"théorique qui est validé — et c'est aussi ce que sert à "
            u"comprendre l'exercice : aucune imbrication ne peut faire mieux.",
     mode=u"SingleValue", tol=u"0", nb=8,
     comp=u"Multiplication, Mass Addition, Division, Round, Panel",
     etapes=[u"Calculer la surface de chaque pièce.",
             u"Sommer les vingt surfaces.",
             u"Diviser par la surface d'un panneau brut.",
             u"Arrondir au supérieur : c'est un approvisionnement.",
             u"Garder à l'esprit que le nombre réel sera supérieur — la "
             u"chute de placement s'ajoute à la chute de surface."],
     pieges=[u"Arrondir au plus proche.",
             u"Oublier que ce minorant est inatteignable en pratique et le "
             u"présenter comme la commande à passer."],
     var=[u"Ajouter un trait de scie de 4 mm autour de chaque pièce et "
          u"refaire l'estimation.",
          u"Comparer au résultat d'une imbrication réelle et chiffrer "
          u"l'écart : c'est le rendement de l'imbrication."],
     gamif=u"G-21 Optimisation comparée",
     bareme=u"1 point si le nombre est juste et arrondi au supérieur.",
     verdict=u"competence"),

dict(id=u"FA-02", titre=u"Le développé d'une virole",
     them=u"FA2 · Déroulé et mise à plat",
     ref=u"REF-115, REF-116",
     niv=u"Perfectionnement", duree=30, prereq=u"A-42",
     competence=u"Établir le développé à plat d'une surface réglée et le "
                u"contrôler par un calcul indépendant.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Une virole conique de ventilation se découpe à plat dans la "
              u"tôle avant d'être roulée.",
     obj=u"Établir le développé à plat d'une surface réglée et le contrôler "
         u"par un calcul indépendant.",
     enonce=u"La virole relie un diamètre de 360 mm à un diamètre de 190 mm "
            u"sur une hauteur de 340 mm. Produisez son développé à plat et "
            u"donnez la surface développée, en mètres carrés.",
     depart=u"Les deux rayons et la hauteur, en valeurs réglables.",
     att=u"La surface développée, en mètres carrés, à 0,0001 près.",
     erreur=u"Prendre la hauteur pour l'apothème. La génératrice d'un cône "
            u"tronqué vaut la racine de la hauteur au carré plus l'écart des "
            u"rayons au carré : ici 340 contre 348 mm. L'écart est de 2 %, "
            u"assez petit pour passer inaperçu et assez grand pour que la "
            u"virole ne se referme pas.",
     donnees_note=u"L'écart des rayons, 85 mm pour 340 de hauteur, place la "
                  u"génératrice juste assez loin de la hauteur pour que la "
                  u"confusion soit détectable au dixième de millimètre carré, "
                  u"sans être grossière.",
     mode=u"NumericTolerance", tol=u"0,0001", nb=8,
     comp=u"Cone, Unroll Brep, Area, Panel",
     etapes=[u"Construire la virole comme surface réglée entre les deux "
             u"cercles.",
             u"La dérouler à plat.",
             u"Mesurer l'aire du développé.",
             u"Contrôler par le calcul : π multiplié par la somme des rayons, "
             u"multiplié par la génératrice — et non par la hauteur.",
             u"Comparer les deux valeurs : elles doivent coïncider."],
     pieges=[u"Confondre hauteur et génératrice.",
             u"Dérouler une surface non développable : un cône l'est, une "
             u"double courbure ne l'est pas, et le résultat serait une "
             u"approximation silencieuse."],
     var=[u"Ajouter un recouvrement de 15 mm pour la soudure.",
          u"Passer à une virole excentrée et constater qu'elle ne se déroule "
          u"plus exactement."],
     gamif=u"G-06 Cible et précision",
     bareme=u"1 point si la surface développée est juste et si le contrôle "
            u"par le calcul est fourni.",
     verdict=u"competence"),
]


LOTS = [(u"GP", LOT_GP), (u"QT", LOT_QT), (u"FA", LOT_FA)]
TOUS = LOT_GP + LOT_QT + LOT_FA
