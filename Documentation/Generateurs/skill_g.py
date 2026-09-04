# -*- coding: utf-8 -*-
"""Couche pedagogique du LOT G, superposee aux fiches d'origine.

Meme montage que `skill_b.py` et `skill_c.py` : `exos_g.py` n'est pas touche.

CE QUE LE LOT G A DE PARTICULIER
--------------------------------
Ce sont des exercices GAMIFIES : une technique de jeu par exercice — score
visible, barre de progression, vies, serie, coffre a butin, golf, boss de fin
de chapitre. La technique est le sujet ; l'exercice de Grasshopper en est le
support.

D'ou le principe retenu pour les reponses : **l'indicateur verifiable est la
metrique du jeu lui-meme**. Le score d'un tableau des scores, le nombre de
coups d'un golf, l'index trouve d'une chasse au tresor, la longueur cumulee
d'une animation a mi-parcours. On ne plaque pas un nombre sur un jeu — on lit
celui qu'il affiche deja.

CE QUI A DU ETRE CORRIGE
------------------------
Les fiches d'origine, ecrites avant la refonte pedagogique du 26/08,
annoncaient des livrables la ou le correcteur attend des valeurs — « la barre
a 100 % », « les sons correctement declenches », « l'arbre de competences
dessine ». Et elles employaient deux modes que le checker Magpie ne peut pas
tenir :

- **GeometryTolerance** ne compare QU'UN SEUL element. Six exercices en
  declaraient un tout en produisant cinq formes, douze modules ou une harde
  entiere : ils etaient incorrigibles tels qu'ecrits.
- **SetEquality** compare un ensemble de NOMBRES, sans doublon. Huit
  exercices l'employaient sur des choses qui n'en sont pas — « 24 modules
  produits et les trois defauts corriges », « la definition complete produite
  par les deux contributions ».

Chacun bascule sur la mesure caracteristique de ce qu'il produit. Ce n'est pas
un contournement : le score d'un scoreboard EST un nombre, et le perimetre
d'une harde disposee en cercle dit si elle l'est bien.

TOUTES LES VALEURS SONT CALCULEES par `verifier_lot_g.py`.
"""

import math


# ---------------------------------------------------------------------------
# Le generateur des jeux de donnees
# ---------------------------------------------------------------------------

def suite(n, graine, bas, haut, pas=1):
    """Suite deterministe, reproductible a l'identique partout.

    Elle lit les bits de POIDS FORT. Le premier essai lisait le reste modulo
    l'etendue : sur un generateur congruentiel de module 2^31, le bit de poids
    faible ALTERNE strictement, et la parite de G-06 devenait devinable sans
    regarder une seule donnee — la moitie exacte des index, un sur deux.
    """
    out, x = [], graine
    span = int((haut - bas) / pas) + 1
    for _ in range(n):
        x = (1103515245 * x + 12345) % 2147483648
        out.append(bas + ((x >> 13) % span) * pas)
    return out


# ---------------------------------------------------------------------------
# Jeux de donnees
# ---------------------------------------------------------------------------

#: G-01 — douze valeurs a trier, 10 points la bonne place, -5 la mauvaise
D_G01 = [847, 132, 596, 274, 913, 458, 61, 725, 389, 168, 502, 941]

#: G-02 — les cinq formes du logo : chacune vaut un jalon de 20 %
D_G02 = dict(rayon=45.0, rectangle=(120.0, 70.0), triangle=88.0,
             hexagone=52.0, segment=134.0)

#: G-03 — cinq listes, cinq extractions, cent-quatre-vingts secondes
D_G03 = [
    [318, 745, 129, 806, 452, 973, 264, 587],
    [61, 903, 447, 218, 675, 334, 891, 156, 729],
    [512, 87, 640, 293, 758, 421, 965, 176],
    [234, 819, 405, 672, 148, 583, 927, 361, 796],
    [703, 259, 846, 132, 578, 964, 315, 487],
]

#: G-04 — deux listes de tailles differentes, et les trois appariements
D_G04 = dict(a=11, b=7)

#: G-05 — le portique, et ses six badges
D_G05 = dict(hauteur=4200.0, entraxe=6800.0, section=340.0, epaisseur=12.0,
             largeur=180.0, densite=7.85e-6)

#: G-06 — soixante valeurs, trois niveaux qui se debloquent l'un l'autre
D_G06 = suite(60, 4177, 100, 999)

#: G-07 — la trame, et ses etoiles
D_G07 = dict(longueur=3400.0, largeur=2100.0, pas_x=260.0, pas_y=185.0)

#: G-08 — seize valeurs, huit manipulations enchainees
D_G08 = suite(16, 90211, 10, 990)

#: G-09 — les quatorze valeurs que porte le composant masque
D_G09 = suite(14, 31337, 100, 999)

#: G-10 — vingt coffres, trois recompenses
D_G10 = suite(20, 7, 10, 99)

#: G-11 — les sept mots de la grille
D_G11 = [u"SERIES", u"CULL", u"GRAFT", u"DISPATCH", u"WEAVE", u"JITTER",
         u"PARTITION"]

#: G-12 — les six paires du memory, cartes numerotees de 1 a 12
D_G12 = [(1, 8), (2, 11), (3, 6), (4, 12), (5, 9), (7, 10)]

#: G-13 — trois rouleaux de huit motifs ; UN SEUL motif leur est commun
D_G13 = [
    [1, 2, 4, 1, 3, 2, 3, 1],
    [5, 4, 6, 5, 6, 5, 6, 6],
    [7, 4, 8, 7, 8, 9, 9, 7],
]
D_G13_CENTRE = 3

#: G-14 — les six sommets de la polyligne cible
D_G14 = [(0.0, 0.0), (340.0, 0.0), (340.0, 190.0), (620.0, 190.0),
         (620.0, 470.0), (180.0, 470.0)]

#: G-15 — la moitie gauche du motif, axe en x = 0
D_G15 = [(0.0, 0.0), (-120.0, 40.0), (-185.0, 145.0), (-150.0, 260.0),
         (-60.0, 330.0), (0.0, 355.0)]

#: G-16 — cinq cents points, un seul hors du volume de reference
D_G16_VOLUME = (2000.0, 1200.0, 800.0)
D_G16_ABERRANT = 337
D_G16_X = suite(500, 1861, 0, 2000)
D_G16_Y = suite(500, 2749, 0, 1200)
D_G16_Z = suite(500, 3391, 0, 800)
D_G16_X[D_G16_ABERRANT] = 2480
D_G16_Y[D_G16_ABERRANT] = 1465
D_G16_Z[D_G16_ABERRANT] = 962

#: G-17 — dix questions sur les comportements implicites, quatre propositions
#: chacune. La bonne reponse est reperee par son rang, de 1 a 4.
D_G17 = [
    (u"Deux listes de 7 et 11 éléments alimentent un même composant en "
     u"appariement « le plus long ». Que reçoit le composant pour les quatre "
     u"éléments qui manquent à la plus courte ?",
     [u"rien : ces quatre calculs ne sont pas faits",
      u"zéro, valeur par défaut du type",
      u"le dernier élément de la liste courte, répété",
      u"une erreur qui met le composant en rouge"], 3),
    (u"Un arbre de 5 branches et une liste simple de 3 éléments entrent dans "
     u"le même composant. Combien de fois la liste simple est-elle utilisée ?",
     [u"une seule fois, sur la première branche",
      u"cinq fois, une par branche",
      u"trois fois, une par élément",
      u"quinze fois, en produit croisé"], 2),
    (u"Que fait `Flatten` sur un arbre de 4 branches de 6 éléments ?",
     [u"il garde 4 branches et trie chacune",
      u"il produit 6 branches de 4 éléments",
      u"il produit une branche unique de 24 éléments",
      u"il supprime les branches vides seulement"], 3),
    (u"`Graft` appliqué à une liste de 10 éléments produit :",
     [u"10 branches d'un élément",
      u"une branche de 10 éléments",
      u"2 branches de 5 éléments",
      u"rien : Graft ne s'applique qu'aux arbres"], 1),
    (u"Un slider entier réglé sur 7 est branché sur une entrée attendant un "
     u"nombre décimal. Que se passe-t-il ?",
     [u"le composant passe en rouge",
      u"le composant passe en orange et ignore l'entrée",
      u"la conversion est implicite et vaut 7,0",
      u"la valeur est arrondie à l'entier supérieur"], 3),
    (u"`Cull Pattern` avec un motif {vrai, faux} sur une liste de 9 "
     u"éléments garde :",
     [u"les 9 éléments",
      u"les 4 éléments de rang pair",
      u"les 4 éléments de rang impair",
      u"les 5 éléments de rang pair, motif répété cycliquement"], 4),
    (u"Deux courbes de longueurs différentes sont divisées en 10 par "
     u"`Divide Curve`. Les points sont espacés :",
     [u"selon la longueur d'arc, donc régulièrement sur chaque courbe",
      u"selon le paramètre, donc irrégulièrement",
      u"selon la courbure locale",
      u"selon la distance au repère"], 1),
    (u"Un `Series` de départ 0, pas 5 et compte 4 produit :",
     [u"0, 5, 10, 15, 20",
      u"5, 10, 15, 20",
      u"0, 5, 10, 15",
      u"0, 1, 2, 3"], 3),
    (u"`Mass Addition` reçoit un arbre de 3 branches. Il rend :",
     [u"un seul nombre, la somme de tout",
      u"trois nombres, un par branche",
      u"la somme de la première branche seulement",
      u"une erreur : il n'accepte que les listes"], 2),
    (u"Un composant `Panel` affiche `{0;1}` en tête d'un bloc de valeurs. "
     u"Cela signifie :",
     [u"que la valeur est comprise entre 0 et 1",
      u"que le panneau contient 1 élément",
      u"le chemin de la branche affichée",
      u"le numéro de version de la donnée"], 3),
]

#: G-18 — quinze affirmations ; celles qui sont VRAIES, par leur rang
D_G18 = [
    (u"Un nombre décimal branché sur une entrée entière est arrondi.", True),
    (u"`Flatten` et `Simplify` font la même chose.", False),
    (u"Un texte « 12 » branché sur une entrée numérique est converti.", True),
    (u"Deux courbes identiques mais de sens opposés sont égales pour "
     u"`Equality`.", False),
    (u"`Larger Than` rend un booléen, pas un nombre.", True),
    (u"Une liste vide et une branche vide sont la même chose.", False),
    (u"`List Length` sur un arbre rend un nombre par branche.", True),
    (u"Un point et un vecteur de mêmes coordonnées sont interchangeables.",
     False),
    (u"`Shift List` avec un décalage négatif décale vers la fin.", True),
    (u"`Sort List` trie les textes dans l'ordre alphabétique.", False),
    (u"Un `Boolean Toggle` peut alimenter une entrée numérique : vrai vaut 1.",
     True),
    (u"`Cross Reference` produit toujours plus d'éléments que ses entrées.",
     False),
    (u"Un cercle est une courbe fermée pour `Closed Curve`.", True),
    (u"`Area` rend le centre de gravité en plus de l'aire.", True),
    (u"Une surface et un Brep d'une seule face sont le même type.", False),
]

#: G-19 — le jeu de preuve, applique aux quatre composants reconnus
D_G19 = [58, 91, 23, 77, 46, 88, 12, 65, 39, 94, 51, 30]

#: G-20 — la definition fautive devrait produire 24 modules, elle en fait 6
D_G20 = dict(nx=6, ny=4, cote=310.0, produits=6)

#: G-21 — l'etoile a neuf branches, cible du golf
D_G21 = dict(rayon=240.0, dents=9, creux=46.0, par=7)

#: G-22 — deux cent quarante valeurs, trois phases sans validation
D_G22 = suite(240, 55117, 10, 999)
D_G22_BRANCHES = 8

#: G-23 — la nomenclature de l'assemblage du duel
D_G23 = [(u"montant", 14), (u"traverse", 22), (u"lisse", 9), (u"panne", 31),
         (u"contrefiche", 6), (u"platine", 44), (u"gousset", 18),
         (u"tirant", 27)]

#: G-24 — l'enigme qui declenche le son de victoire
D_G24 = suite(80, 60613, 1, 400)

#: G-25 — les quarante barres de l'animation
D_G25 = suite(40, 27183, 300, 1900)
D_G25_T = 0.375

#: G-26 — vingt pieces, tolerance de 400 a 900 mm
D_G26 = suite(20, 82241, 250, 1150, 10)
D_G26_BORNES = (400.0, 900.0)

#: G-27 — l'abreuvoir et la harde
D_G27 = dict(rayon_abreuvoir=1800.0, ecart=950.0, animaux=12)

#: G-28 — l'avatar : 3 formes, 4 motifs, 6 couleurs
D_G28 = dict(formes=3, motifs=4, couleurs=6)

#: G-29 — le jeu du jour
D_G29 = suite(41, 19860, 120, 2400)

#: G-30 — le relais : quatre-vingt-seize valeurs, six branches de seize
D_G30 = suite(96, 71099, 20, 980)
D_G30_BRANCHES = 6
D_G30_ECARTES = 2

#: G-31 — quarante-huit notions : ce qu'elles portent, ce qui est valide
D_G31_PORTE = [1 + (v % 4) for v in suite(48, 44029, 100, 999)]
D_G31_VALIDE = [w % 5 for w in suite(48, 90403, 100, 999)]

#: G-32 — l'arbre source a restructurer
D_G32 = suite(72, 13577, 100, 999)
D_G32_BRANCHES = 9


# ---------------------------------------------------------------------------
# La couche
# ---------------------------------------------------------------------------

SKILL_G = {

"G-01": dict(
  competence=u"Trier une liste et lire le score que le tri produit, en "
             u"distinguant ce qui est compté de ce qui est trié.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le tableau des scores rend la performance immédiate. Il ne "
           u"récompense pas l'effort mais le résultat, et l'apprenant le voit "
           u"avant de soumettre.",
  att=u"Les douze valeurs triées : 61, 132, 168, 274, 389, 458, 502, 596, "
      u"725, 847, 913, 941.",
  erreur=u"Trier une COPIE de la liste sans la rebrancher sur le paramètre de "
         u"réponse. Le canvas affiche alors une liste triée, le score reste à "
         u"zéro, et rien n'indique pourquoi — c'est le défaut le plus fréquent "
         u"du lot, et le tableau des scores est justement là pour le rendre "
         u"visible en une seconde.",
  donnees_note=u"Douze valeurs de 61 à 941, sans ordre ni régularité : "
               u"aucune ne se devine, et le tri doit être fait. Le score de "
               u"120 n'est atteint qu'à douze bonnes places sur douze — un "
               u"score partiel n'est pas une réussite partielle.",
  limite=u"Le score mesure le RÉSULTAT, pas la méthode. Trier douze valeurs "
         u"à la main dans un panneau donne le même score que `Sort List`, et "
         u"ne s'effondre qu'au treizième.",
  mode=u"ExactOrderedList", tol=u"0"),

"G-02": dict(
  competence=u"Construire cinq primitives distinctes et mesurer l'ensemble "
             u"qu'elles forment, chaque forme étant un jalon.",
  bloom=u"Appliquer × procédurale",
  contexte=u"La barre de progression soutient l'effort en découpant une tâche "
           u"longue en jalons visibles. Sans elle, cinq formes à poser se "
           u"vivent comme une seule tâche qui n'avance pas.",
  att=u"1 372,74 mm — la somme des cinq périmètres, à 0,01 près.",
  erreur=u"Prendre le côté du triangle et de l'hexagone pour leur périmètre : "
         u"936,74 au lieu de 1 372,74. Un polygone régulier de côté c a un "
         u"périmètre de n×c, et l'erreur passe inaperçue tant qu'on ne compare "
         u"pas le cercle aux autres.",
  donnees_note=u"Cinq formes de familles différentes — cercle, rectangle, "
               u"triangle, hexagone, segment — pour que la somme ne puisse pas "
               u"se retrouver par une seule formule. Le cercle apporte π, ce "
               u"qui rend le total non entier et donc non devinable.",
  limite=u"La somme des périmètres dit que les cinq formes ont la bonne "
         u"TAILLE, pas qu'elles sont au bon endroit. Le positionnement sur le "
         u"gabarit se juge à l'œil, et c'est le rôle de la barre.",
  mode=u"NumericTolerance", tol=u"0.01"),

"G-03": dict(
  competence=u"Enchaîner cinq extractions de liste de natures différentes "
             u"sans confondre rang, position et valeur.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le contre-la-montre travaille la vitesse sur des gestes déjà "
           u"acquis. Il ne s'adresse pas à qui découvre : il sert à rendre "
           u"automatique ce qui est encore réfléchi.",
  att=u"Les cinq extractions, dans l'ordre : 806, 729, 965, 148, 578.",
  erreur=u"Confondre le rang et la valeur : rendre 3 au lieu de 806 pour "
         u"« l'élément d'index 3 ». Sous chronomètre, cette confusion coûte "
         u"plus que le temps qu'elle fait gagner.",
  donnees_note=u"Cinq listes de 8 ou 9 valeurs, de longueurs inégales pour "
               u"que le médian ne tombe pas au même endroit. Les cinq "
               u"extractions sont de cinq natures différentes — index, "
               u"dernier, maximum, minimum, médian — de sorte qu'un seul "
               u"composant ne peut pas toutes les faire.",
  limite=u"Le chronomètre n'entre PAS dans la validation : une réponse juste "
         u"hors délai reste juste. Il ne pilote que le bonus, et c'est "
         u"délibéré — un exercice qui refuse une bonne réponse pour un retard "
         u"n'enseigne plus rien.",
  mode=u"ExactOrderedList", tol=u"0"),

"G-04": dict(
  verdict=u"connaissance", competence=u"—",
  charniere=u"Deux listes de 11 et 7 éléments entrent dans un même composant. "
            u"Combien de résultats sort-il en appariement « le plus court », "
            u"« le plus long », puis « référence croisée » ? Donne la somme "
            u"des trois nombres.",
  bloom=u"Comprendre × conceptuelle",
  contexte=u"Les modes d'appariement sont la première cause de résultats "
           u"inexplicables. Trois vies suffisent : au-delà, c'est qu'on "
           u"devine au lieu de raisonner.",
  att=u"95 — soit 7 + 11 + 77.",
  erreur=u"Croire que la référence croisée donne 11 + 7 = 18 au lieu de "
         u"11 × 7 = 77. C'est un PRODUIT, pas une somme : la référence "
         u"croisée apparie chaque élément de l'une avec chacun de l'autre, et "
         u"c'est ce qui la rend si coûteuse sur de grandes listes.",
  donnees_note=u"11 et 7 sont premiers entre eux et tous deux impairs : "
               u"aucune des trois réponses ne coïncide avec une autre, et la "
               u"somme 95 ne peut pas s'obtenir par un autre chemin.",
  limite=u"Les trois modes nommés ne sont pas les seuls : Grasshopper en "
         u"expose d'autres par le menu du composant. L'exercice ne traite que "
         u"les trois qui expliquent la quasi-totalité des surprises.",
  mode=u"SingleValue", tol=u"0"),

"G-05": dict(
  competence=u"Produire une famille complète de mesures sur un même "
             u"assemblage, en gardant la cohérence des unités.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le badge récompense la maîtrise d'une famille entière, pas d'un "
           u"geste isolé. Un métreur qui sait mesurer une longueur mais pas "
           u"un volume n'est pas un métreur.",
  att=u"Les six mesures : 15 200 mm de développé, 11 904 mm² de section, "
      u"180 940,8 cm³, 1 420,385 kg, 4 370 mm hors tout, 6 620 mm de portée.",
  erreur=u"Calculer l'aire de la section comme un plein, 180 × 340 = 61 200, "
         u"au lieu de déduire l'intérieur du profil creux : 11 904. Le volume "
         u"et la masse suivent, et le portique est annoncé cinq fois trop "
         u"lourd — une erreur qui se propage à toute la collection de badges.",
  donnees_note=u"Un profil creux 180 × 340 de 12 mm d'épaisseur : le rapport "
               u"plein/creux est de 5,14, assez pour que l'erreur soit "
               u"flagrante à la lecture. Les six mesures s'enchaînent — "
               u"section, développé, volume, masse — de sorte qu'une seule "
               u"fausse en compromet trois.",
  limite=u"La masse est celle de la MATIÈRE. Assemblages, platines et "
         u"soudures ajoutent couramment 8 à 12 % qu'aucune de ces six mesures "
         u"ne voit.",
  mode=u"NumericTolerance", tol=u"1"),

"G-06": dict(
  competence=u"Enchaîner trois filtres dont chacun s'applique au résultat du "
             u"précédent, et non aux données de départ.",
  bloom=u"Analyser × procédurale",
  contexte=u"Le déblocage progressif protège l'apprenant d'une difficulté "
           u"qu'il n'est pas prêt à affronter. Il rend aussi visible qu'un "
           u"filtre s'applique à ce qui reste, pas à tout.",
  att=u"Les index survivants : 0, 8, 11, 26, 27, 31, 36, 53.",
  erreur=u"Prendre la moyenne des SOIXANTE valeurs de départ, 518,93, au lieu "
         u"de celle des seize qui ont franchi le niveau 2, 771,50. Le niveau 3 "
         u"garde alors quinze index au lieu de huit — presque le double. Un "
         u"filtre s'applique à ce qui RESTE, jamais aux données de départ, et "
         u"c'est toute la différence entre trois niveaux enchaînés et trois "
         u"conditions indépendantes.",
  donnees_note=u"Soixante valeurs de 100 à 999. Le premier niveau en garde "
               u"32, le deuxième 16, le troisième 8 : chaque niveau divise "
               u"exactement par deux, ce qui donne à la progression une allure "
               u"de niveaux de jeu. Le seuil du niveau 3 est une moyenne "
               u"CALCULÉE sur les survivants — c'est ce qui rend le "
               u"chaînage obligatoire, et le résultat impossible à retrouver "
               u"de tête.",
  limite=u"Le déblocage est ici SIMULÉ par des groupes grisés. Grasshopper ne "
         u"sait pas verrouiller un groupe : rien n'empêche l'apprenant "
         u"d'ouvrir le niveau 3 d'emblée, et l'exercice ne le détecte pas.",
  mode=u"SetEquality", tol=u"0"),

"G-07": dict(
  competence=u"Construire une trame dont le nombre de modules découle du pas, "
             u"et non l'inverse.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Les étoiles distinguent la réussite de la réussite élégante. "
           u"Une trame juste mais figée vaut une étoile ; la même trame "
           u"paramétrique en vaut trois, et c'est la seule qui survivra au "
           u"prochain changement de cote.",
  att=u"143 modules — 13 par 11.",
  erreur=u"Diviser sans arrondir vers le bas : 3 400 / 260 = 13,08, et un "
         u"quatorzième module sort du cadre. Sur les deux axes, l'erreur "
         u"donne 14 × 12 = 168 au lieu de 143, soit 25 modules fantômes.",
  donnees_note=u"3 400 / 260 et 2 100 / 185 tombent tous deux JUSTE au-dessus "
               u"d'un entier — 13,08 et 11,35. C'est le cas où l'arrondi "
               u"compte, et il a été choisi pour cela : avec des divisions "
               u"exactes, l'erreur n'apparaîtrait pas.",
  limite=u"143 dit que la trame a le bon COMPTE. La troisième étoile — "
         u"rester juste après changement des paramètres — ne se vérifie pas "
         u"automatiquement : c'est le formateur qui bouge les sliders.",
  mode=u"SingleValue", tol=u"0"),

"G-08": dict(
  competence=u"Enchaîner huit manipulations de listes sans rompre la série, "
             u"chacune portant sur une propriété différente du même jeu.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le multiplicateur de série récompense la régularité plutôt que "
           u"le coup de chance. Sept bonnes réponses suivies d'une erreur "
           u"valent moins que huit réponses moyennes enchaînées.",
  att=u"Les huit réponses : 11, 962, 69, 7 133, 404, 1 119, 5, 1 348.",
  erreur=u"Prendre le médian d'une liste de 16 éléments sans la TRIER "
         u"d'abord : on rend l'élément de rang 8 de la liste brute, 857 au "
         u"lieu de 404 — plus du double. Le médian est une valeur de la liste "
         u"ORDONNÉE, et la série se casse sur cette seule réponse.",
  donnees_note=u"Seize valeurs de 10 à 990. Les huit résultats sont deux à "
               u"deux DISTINCTS — 11 pairs, 5 au-dessus de 500, médian 404 — "
               u"de sorte qu'une confusion entre deux questions se voit. Le "
               u"jeu a été choisi pour que l'élément brut de rang 8 (857) "
               u"diffère nettement du médian (404) : sans quoi le piège de la "
               u"cinquième question serait muet.",
  limite=u"Le multiplicateur est une mécanique de SCORE : il ne change ni la "
         u"validation ni la difficulté. Un apprenant qui reprend depuis le "
         u"début obtient le même verdict, avec moins de points.",
  mode=u"ExactOrderedList", tol=u"0"),

"G-09": dict(
  competence=u"Explorer un canvas pour y trouver ce qui a été rendu "
             u"invisible, puis exploiter la donnée trouvée.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le composant caché récompense l'exploration des menus "
           u"contextuels — l'endroit où se trouvent la moitié des réponses "
           u"aux questions que les débutants posent.",
  att=u"8 538 — la somme des quatorze valeurs que porte le composant masqué.",
  erreur=u"Chercher le composant à l'œil en déplaçant les autres, au lieu "
         u"d'ouvrir Edit > Arrange ou de tout sélectionner par Ctrl+A : un "
         u"composant masqué reste SÉLECTIONNABLE, il ne disparaît que de "
         u"l'aperçu. C'est la leçon de l'exercice, et elle sert ensuite tous "
         u"les jours.",
  donnees_note=u"Quatorze valeurs de trois chiffres, sans motif : la somme "
               u"8 538 ne se retrouve ni de tête ni par un raccourci. Il faut "
               u"réellement avoir mis la main sur le composant.",
  limite=u"« Masqué » veut dire aperçu désactivé, pas protégé. Rien n'empêche "
         u"d'ouvrir le fichier dans un éditeur de texte et d'y lire les "
         u"quatorze valeurs — l'exercice suppose la bonne foi, comme tous les "
         u"jeux de piste.",
  mode=u"SingleValue", tol=u"0"),

"G-10": dict(
  competence=u"Identifier les extrêmes d'un jeu de valeurs et en rendre les "
             u"INDEX plutôt que les valeurs.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le coffre à butin introduit une part d'aléatoire maîtrisé : le "
           u"contenu change à chaque tirage, la méthode pour le trouver non. "
           u"C'est ce qui permet de rejouer l'exercice.",
  att=u"Les index des trois coffres pleins : 7, 13, 16.",
  erreur=u"Rendre les valeurs — 87, 95, 93 — au lieu des index. Un index "
         u"désigne une POSITION ; c'est lui qui permet ensuite d'aller "
         u"chercher le coffre correspondant dans la trame, et les deux sont "
         u"ici du même ordre de grandeur, ce qui rend la confusion "
         u"invisible au premier regard.",
  donnees_note=u"Vingt contenus de 10 à 99. Les trois plus riches — 95, 93 et "
               u"87 — sont nettement détachés du quatrième (86), de sorte que "
               u"le seuil ne prête pas à discussion. Aucun ex æquo : "
               u"l'ensemble des trois index est unique.",
  limite=u"L'aléatoire est FIGÉ par la graine. Deux apprenants trouvent les "
         u"mêmes coffres, ce qui rend l'exercice corrigeable mais retire au "
         u"loot box sa surprise dès la deuxième session.",
  mode=u"SetEquality", tol=u"0"),

"G-11": dict(
  competence=u"Retrouver le nom anglais des composants natifs à partir de "
             u"leur effet, et contrôler sa grille par une mesure globale.",
  bloom=u"Se rappeler × factuelle",
  contexte=u"Le vocabulaire des composants est la barrière la plus basse et "
           u"la plus haute : on ne trouve pas ce dont on ignore le nom. Les "
           u"mots croisés le travaillent sans réciter.",
  att=u"43 — la somme des longueurs des sept mots placés.",
  erreur=u"Écrire `SORT` pour « ranger une liste » alors que la grille "
         u"attend `SERIES` pour « produire une suite régulière » : la "
         u"définition parle de PRODUIRE, pas de ranger. Une case de trop ou de "
         u"moins fait tomber la somme, et c'est ce qui la signale.",
  donnees_note=u"Sept mots de 4 à 9 lettres, tous des composants natifs "
               u"réellement employés dans le référentiel. La somme 43 ne se "
               u"devine pas : elle exige les sept mots, et un seul faux la "
               u"décale.",
  limite=u"La somme des longueurs ne dit pas que les mots sont les BONS : "
         u"deux mots de même longueur se substituent sans qu'elle bouge. "
         u"C'est un contrôle de cohérence, pas une correction lettre à "
         u"lettre — le mot final grisé, lui, se lit sur la fiche.",
  mode=u"SingleValue", tol=u"0"),

"G-12": dict(
  competence=u"Associer chaque composant à son effet sur la structure des "
             u"données, et exprimer l'appariement de façon exploitable.",
  bloom=u"Comprendre × conceptuelle",
  contexte=u"Le memory fait travailler l'association plutôt que la "
           u"définition. Savoir que `Graft` fait une branche par élément vaut "
           u"mieux que savoir réciter sa description.",
  att=u"Le partenaire de chaque carte, dans l'ordre des cartes : 8, 11, "
      u"6, 12, 9, 3, 10, 1, 5, 7, 2, 4.",
  erreur=u"Rendre les six paires comme six couples, dans un ordre libre. "
         u"L'ordre libre n'est pas comparable — deux apprenants justes "
         u"rendraient deux listes différentes. La forme demandée, un "
         u"partenaire PAR CARTE, est unique par construction.",
  donnees_note=u"Douze cartes, six paires, aucune carte appariée avec sa "
               u"voisine immédiate : la liste des partenaires ne présente "
               u"aucune régularité, et se lit comme une permutation "
               u"involutive — chaque carte est le partenaire de son "
               u"partenaire.",
  limite=u"L'appariement se vérifie, la MÉMOIRE non. Un apprenant qui retourne "
         u"les douze cartes et les compare une à une obtient le même résultat "
         u"que celui qui les a retenues.",
  mode=u"ExactOrderedList", tol=u"0"),

"G-13": dict(
  competence=u"Chercher le décalage cyclique qui aligne trois séquences, en "
             u"raisonnant sur le modulo plutôt que par essais.",
  bloom=u"Analyser × procédurale",
  contexte=u"La machine à sous rend tangible la logique des motifs "
           u"cycliques — celle qui régit `Shift List`, les listes de "
           u"répétition et tout calepinage à motif alterné.",
  att=u"Les trois décalages, dans l'ordre : 7, 6, 6.",
  erreur=u"Chercher un décalage qui aligne les PREMIÈRES cases plutôt que la "
         u"ligne centrale. Le centre est en position 3 : décaler pour amener "
         u"le motif en tête donne trois valeurs fausses de 3, et l'affichage "
         u"ne montre pas l'erreur puisque les rouleaux tournent quand même.",
  donnees_note=u"Neuf motifs répartis sur trois rouleaux de huit, choisis "
               u"pour qu'UN SEUL motif — le 4 — soit présent dans les trois, "
               u"et une seule fois dans chacun. La solution est donc unique : "
               u"avec des rouleaux ordinaires, huit triplets alignent, et la "
               u"question n'aurait pas de réponse.",
  limite=u"Un seul triplet aligne ici. Une vraie machine à sous en aurait "
         u"plusieurs, et il faudrait alors demander le plus petit — "
         u"l'exercice évite cette complication au lieu de la traiter.",
  mode=u"ExactOrderedList", tol=u"0"),

"G-14": dict(
  competence=u"Rétablir un câblage à partir du seul résultat attendu, en "
             u"lisant les types d'entrée et de sortie.",
  bloom=u"Analyser × procédurale",
  contexte=u"Un câblage se lit avant de s'écrire. Le puzzle enlève les "
           u"câbles et laisse les composants : ce qui reste à trouver est "
           u"exactement ce qu'on ne voit pas quand on recopie un tutoriel.",
  att=u"2 033,29 mm — la longueur du contour fermé, à 0,01 près.",
  erreur=u"Oublier de refermer le contour : 1 530,00 mm, soit le seul "
         u"chemin ouvert. La différence est le segment de retour, 503,29 mm — "
         u"un quart de la réponse, et l'aperçu ne le montre pas puisqu'une "
         u"polyligne ouverte se dessine comme une fermée à un segment près.",
  donnees_note=u"Six sommets en marches d'escalier, tous à coordonnées "
               u"entières, mais dont le segment de fermeture est oblique : la "
               u"longueur totale est irrationnelle et ne se devine pas, alors "
               u"que chaque segment se vérifie de tête.",
  limite=u"La longueur dit que le contour est le BON, pas qu'il a été obtenu "
         u"avec les six composants imposés. Le respect du nombre de "
         u"composants se compte à l'œil, sur le canvas.",
  mode=u"NumericTolerance", tol=u"0.01"),

"G-15": dict(
  competence=u"Reconstituer une figure par symétrie et la refermer, puis "
             u"mesurer ce qu'on a produit.",
  bloom=u"Appliquer × procédurale",
  contexte=u"La silhouette à compléter fait travailler la déduction "
           u"géométrique : ce qui manque se déduit de ce qui est là, sans "
           u"cote supplémentaire.",
  att=u"91 550 mm² d'aire et 1 098,42 mm de périmètre.",
  erreur=u"Reproduire la moitié droite en la DÉCALANT au lieu de la "
         u"symétriser : la figure obtenue a le même périmètre mais une aire "
         u"nulle ou doublée selon le sens. C'est pourquoi les deux mesures "
         u"sont demandées — le périmètre seul ne distingue pas une symétrie "
         u"d'une translation.",
  donnees_note=u"Six sommets à gauche, dont deux sur l'axe : la moitié droite "
               u"n'en compte que quatre, et recopier les six produit deux "
               u"sommets en double sur l'axe. L'aire ne bouge pas, le "
               u"périmètre si — le contrôle croisé attrape le cas.",
  limite=u"Aire et périmètre ne disent pas que la figure est SYMÉTRIQUE : "
         u"une figure quelconque de mêmes mesures les satisferait. Ils disent "
         u"qu'elle est fermée et de la bonne taille, ce qui écarte les erreurs "
         u"réellement rencontrées.",
  mode=u"NumericTolerance", tol=u"0.01"),

"G-16": dict(
  competence=u"Isoler la donnée aberrante d'un ensemble volumineux par un "
             u"test d'appartenance, et en rendre l'index.",
  bloom=u"Analyser × procédurale",
  contexte=u"Un point hors volume dans un nuage de cinq cents, c'est le cas "
           u"réel du relevé qui contient une mesure parasite. Le trouver à "
           u"l'œil est impossible ; le trouver par un test est immédiat.",
  att=u"337 — l'index du point aberrant.",
  erreur=u"Chercher le point le plus ÉLOIGNÉ du centre au lieu de celui qui "
         u"sort du volume. Le plus éloigné du centre est un coin parfaitement "
         u"légitime du volume : la méthode donne un index faux et paraît "
         u"pourtant raisonnable, ce qui en fait l'erreur la plus coûteuse de "
         u"l'exercice.",
  donnees_note=u"Cinq cents points tirés dans le volume 2 000 × 1 200 × 800, "
               u"plus un seul qui en sort sur les TROIS axes à la fois. Un "
               u"seul point est hors volume : la réponse est unique, et aucun "
               u"cas limite ne traîne sur une face.",
  limite=u"L'index dépend de l'ORDRE des points. Réordonner le nuage — par "
         u"un tri, une projection — change la réponse sans changer le point. "
         u"C'est vrai de tout index, et c'est ce qui les rend fragiles dans "
         u"les échanges.",
  mode=u"SingleValue", tol=u"0"),

"G-17": dict(
  verdict=u"connaissance", competence=u"—",
  charniere=u"Dix comportements implicites de Grasshopper, quatre "
            u"propositions chacun. Donne les dix rangs choisis, dans l'ordre "
            u"des questions.",
  bloom=u"Comprendre × conceptuelle",
  contexte=u"Ce qui coûte le plus cher n'est pas ce qu'on ignore, c'est ce "
           u"qu'on croit savoir. Le quiz éclair vise exactement ces "
           u"comportements que l'on subit sans les avoir jamais formulés.",
  att=u"Les dix rangs : 3, 2, 3, 1, 3, 4, 1, 3, 2, 3.",
  erreur=u"Croire que `Divide Curve` divise selon le PARAMÈTRE. Il divise "
         u"selon la longueur d'arc — c'est la question 7, et l'erreur "
         u"inverse a été mesurée sur DV-02 : elle donnait un résultat quatre "
         u"fois trop grand, parfaitement stable, et donc parfaitement "
         u"crédible.",
  donnees_note=u"Dix questions dont aucune ne porte sur un nom de composant : "
               u"toutes portent sur un COMPORTEMENT. Les bonnes réponses se "
               u"répartissent sur les quatre rangs — trois fois le rang 3, "
               u"deux fois le 1, deux fois le 2, une fois le 4 — de sorte "
               u"qu'aucune stratégie de rang constant ne dépasse trois "
               u"points.",
  limite=u"Trente secondes par question mesurent la réponse ACQUISE, pas la "
         u"réponse trouvée. Un apprenant qui saurait reconstruire chaque "
         u"comportement par le raisonnement échouerait au chronomètre — "
         u"l'exercice suppose l'entraînement fait.",
  mode=u"ExactOrderedList", tol=u"0"),

"G-18": dict(
  verdict=u"connaissance", competence=u"—",
  charniere=u"Quinze affirmations sur les types et les conversions. Donne les "
            u"rangs de celles qui sont VRAIES.",
  bloom=u"Comprendre × conceptuelle",
  contexte=u"Les conversions implicites sont commodes tant qu'on sait "
           u"lesquelles existent. Le vrai/faux à élimination décourage le "
           u"pile ou face, qui donnerait sept bonnes réponses sur quinze sans "
           u"rien savoir.",
  att=u"Les affirmations vraies : 1, 3, 5, 7, 9, 11, 13, 14.",
  erreur=u"Tenir pour vrai que « `Flatten` et `Simplify` font la même "
         u"chose ». `Flatten` écrase l'arbre en une branche ; `Simplify` ne "
         u"fait que raccourcir les chemins en retirant les niveaux inutiles, "
         u"et GARDE les branches. Les confondre détruit une structure de "
         u"données sans message d'erreur.",
  donnees_note=u"Huit vraies sur quinze : ni la majorité ni la moitié, de "
               u"sorte que répondre uniformément ne rapporte rien. Les "
               u"affirmations fausses sont toutes des idées reçues "
               u"réellement entendues en formation, pas des inventions.",
  limite=u"L'élimination des deux affirmations suivantes est une mécanique "
         u"de SCORE, appliquée par le formateur ou le plugin. La définition "
         u"Grasshopper, elle, accepte les quinze réponses et les compare "
         u"toutes.",
  mode=u"SetEquality", tol=u"0"),

"G-19": dict(
  verdict=u"connaissance", competence=u"—",
  charniere=u"Quatre clusters anonymes transforment les données. Identifie "
            u"le composant natif que chacun reproduit, puis applique-le au "
            u"jeu de preuve et donne les quatre résultats.",
  bloom=u"Analyser × conceptuelle",
  contexte=u"Reconnaître un composant à son comportement, c'est ce qu'on "
           u"fait devant la définition d'un confrère. La boîte noire "
           u"entraîne exactement ce geste.",
  att=u"Les quatre résultats sur le jeu de preuve : 7, 273, 9, 5.",
  erreur=u"Nommer le composant sans le VÉRIFIER sur le second jeu. Trois "
         u"composants différents se comportent à l'identique sur les données "
         u"de test — c'est pour cela que la preuve est demandée, et c'est "
         u"aussi pour cela que l'identification seule ne suffit jamais.",
  donnees_note=u"Douze valeurs de deux chiffres, dont sept supérieures à 50 "
               u"et cinq restes distincts modulo 7 : les quatre résultats "
               u"sont deux à deux différents, et aucun ne vaut la taille de "
               u"la liste. Une réponse recopiée d'une autre se voit.",
  limite=u"Quatre nombres justes PROUVENT le comportement, ils ne prouvent "
         u"pas l'identification. Deux composants indiscernables sur ce jeu le "
         u"resteraient — la fiche donne les quatre noms attendus, et c'est le "
         u"formateur qui tranche.",
  mode=u"ExactOrderedList", tol=u"0"),

"G-20": dict(
  competence=u"Diagnostiquer une définition qui produit un résultat "
             u"plausible mais faux, sans en changer la structure.",
  bloom=u"Analyser × procédurale",
  contexte=u"Une définition qui plante se répare ; une définition qui rend "
           u"six modules au lieu de vingt-quatre se livre. C'est le second "
           u"cas qui coûte cher, et c'est celui-là qu'on entraîne.",
  att=u"2 306 400 mm² — l'aire totale des 24 modules retrouvés.",
  erreur=u"Corriger le symptôme en ajoutant un `Duplicate Data` jusqu'à "
         u"obtenir vingt-quatre objets. Le compte devient juste, l'aire "
         u"aussi — et la définition reste fausse, puisqu'elle empile quatre "
         u"fois la même rangée au même endroit. Le compte seul ne suffit donc "
         u"pas à valider une correction.",
  donnees_note=u"Six par quatre, modules de 310 mm : 24 modules et "
               u"2 306 400 mm². Le nombre attendu est ANNONCÉ dans l'énoncé — "
               u"c'est l'aire qui est l'indicateur, précisément parce que le "
               u"compte est déjà connu et ne prouve rien.",
  limite=u"L'aire ne dit pas que les trois défauts ont été trouvés, ni qu'ils "
         u"l'ont été proprement. Elle dit que le résultat est revenu. La "
         u"qualité de la correction se lit sur le canvas.",
  mode=u"NumericTolerance", tol=u"1"),

"G-21": dict(
  competence=u"Produire une géométrie régulière par le chemin le plus "
             u"économe, en cherchant le composant qui fait le travail de "
             u"plusieurs.",
  bloom=u"Créer × procédurale",
  contexte=u"Le golf de composants entraîne l'élégance, qui n'est pas une "
           u"coquetterie : une définition de sept composants se relit, se "
           u"transmet et se modifie, une de trente non.",
  att=u"1 582,75 mm — le périmètre de l'étoile à neuf branches, à 0,01 près.",
  erreur=u"Construire l'étoile par dix-huit segments explicites : le "
         u"périmètre est juste, le score est catastrophique — dix-huit "
         u"composants pour un par de sept. `Polygon` en mode étoile fait le "
         u"même travail en un.",
  donnees_note=u"Neuf branches, rayon 240, creux 46 : un nombre IMPAIR de "
               u"branches, de sorte que l'étoile n'a pas d'axe de symétrie "
               u"horizontal et ne peut pas se construire par simple miroir. "
               u"Le périmètre irrationnel exclut toute réponse devinée.",
  limite=u"Le périmètre valide la GÉOMÉTRIE, pas le score. Le nombre de "
         u"composants se compte à l'œil sur le canvas — sliders et panneaux "
         u"compris, comme l'énoncé le précise.",
  mode=u"NumericTolerance", tol=u"0.01"),

"G-22": dict(
  competence=u"Enchaîner structuration en arbre, filtrage à deux conditions "
             u"et synthèse, sans validation intermédiaire.",
  bloom=u"Créer × procédurale",
  contexte=u"Le boss de fin de chapitre éprouve l'ensemble des notions du "
           u"chapitre en une seule tâche. Ce qu'il mesure n'est pas la "
           u"connaissance des composants mais la capacité à tenir une chaîne "
           u"longue sans se perdre.",
  att=u"Le tableau de synthèse : 6, 5, 6, 5, 5, 8, 10, 4, puis 3 585, 3 369, "
      u"4 380, 3 594, 3 792, 5 796, 7 818, 3 150.",
  erreur=u"Structurer en huit branches CONSÉCUTIVES de trente au lieu de "
         u"répartir une valeur sur deux — huit branches par pas de huit. Les "
         u"deux découpages donnent huit branches de trente ; les comptes "
         u"filtrés, eux, n'ont plus rien à voir, et rien ne signale lequel "
         u"était demandé sinon l'énoncé.",
  donnees_note=u"240 valeurs de 10 à 999. Le double filtre — supérieur à 400 "
               u"ET multiple de 3 — laisse de 4 à 10 valeurs par branche : "
               u"assez pour que les huit comptes diffèrent, trop peu pour "
               u"qu'ils se ressemblent. Les huit sommes vont de 3 150 à "
               u"7 818, sans recouvrement possible.",
  limite=u"« Toute erreur en phase 3 impose de reprendre depuis la phase 1 » "
         u"est une règle de JEU, pas une contrainte de l'outil. Rien "
         u"n'empêche de corriger la seule phase 3 ; c'est l'apprenant qui "
         u"s'impose la règle, et c'est tout l'intérêt.",
  mode=u"ExactOrderedList", tol=u"0"),

"G-23": dict(
  competence=u"Produire une nomenclature triée et la rendre sous une forme "
             u"comparable entre participants.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le duel confronte deux approches du même problème. Il n'a de "
           u"sens que si le résultat attendu est strictement le même pour "
           u"tous — sinon on compare des réponses, pas des méthodes.",
  att=u"Les quantités, par ordre décroissant : 44, 31, 27, 22, 18, 14, 9, 6.",
  erreur=u"Trier par ORDRE ALPHABÉTIQUE des désignations, ce que fait `Sort "
         u"List` sur des textes, au lieu de trier les quantités. On obtient "
         u"une nomenclature parfaitement présentable et un classement faux — "
         u"et comme les deux tris produisent huit lignes, rien ne le signale.",
  donnees_note=u"Huit pièces aux quantités toutes différentes, de 6 à 44, et "
               u"dont l'ordre alphabétique ne coïncide avec l'ordre des "
               u"quantités en aucun point : les deux tris sont totalement "
               u"disjoints, ce qui rend l'erreur immédiatement lisible.",
  limite=u"La justesse seule valide. Le nombre de composants et le temps "
         u"d'exécution départagent au CLASSEMENT, mais ne sont pas mesurés "
         u"par la définition — c'est le plugin Magpie qui les relève.",
  mode=u"ExactOrderedList", tol=u"0"),

"G-24": dict(
  competence=u"Composer trois conditions par un ET logique et compter ce qui "
             u"les satisfait toutes.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le retour sonore associe une perception immédiate à chaque "
           u"action. Il fait sentir la différence entre « une condition "
           u"vraie » et « toutes les conditions vraies », qui reste abstraite "
           u"tant qu'on ne l'entend pas.",
  att=u"8 — le nombre de valeurs qui remplissent les trois conditions.",
  erreur=u"Enchaîner les trois conditions par un OU au lieu d'un ET : 71 "
         u"valeurs sur 80 au lieu de 8. Le son de victoire retentit alors "
         u"presque toujours, ce qui le rend inaudible — et c'est exactement "
         u"pourquoi un retour sonore mal câblé est pire que pas de retour.",
  donnees_note=u"Quatre-vingts valeurs de 1 à 400. Les trois conditions se "
               u"recouvrent partiellement — tout multiple de 4 ne finit pas "
               u"par 0, 4 ou 8 — de sorte que le ET et le OU donnent des "
               u"comptes très éloignés, 8 contre 71 : l'erreur ne peut pas "
               u"passer pour du bruit.",
  limite=u"Le câblage SONORE lui-même n'est pas vérifié : Grasshopper joue "
         u"les sons par un plugin externe, et aucune valeur n'en sort. Seule "
         u"l'énigme logique qui les déclenche est corrigée.",
  mode=u"SingleValue", tol=u"0"),

"G-25": dict(
  competence=u"Piloter une révélation progressive par un paramètre unique et "
             u"savoir lire un état INTERMÉDIAIRE, pas seulement le final.",
  bloom=u"Créer × procédurale",
  contexte=u"Animer la construction d'un algorithme le rend enseignable : on "
           u"voit dans quel ORDRE les choses arrivent, ce que le résultat "
           u"final ne dit jamais.",
  att=u"8 508 mm — la longueur cumulée des barres visibles à t = 0,375.",
  erreur=u"Vérifier l'animation à t = 1 seulement. À t = 1 toute animation "
         u"juste ou fausse affiche les quarante barres : l'état final ne "
         u"prouve rien. C'est l'état intermédiaire qui dit si le pilotage est "
         u"réellement progressif, et c'est lui qu'on demande.",
  donnees_note=u"Quarante barres de 300 à 1 900 mm, révélées de la plus "
               u"courte à la plus longue : à t = 0,375, quinze barres sont "
               u"visibles et pèsent 8 508 mm sur 44 028 au total, soit 19 % "
               u"de la longueur pour 37,5 % des barres. Un cumul "
               u"proportionnel au temps — 16 510 mm — signalerait une "
               u"révélation dans le désordre.",
  limite=u"Trois secondes de durée sont une consigne de CONFORT, non "
         u"vérifiable : la vitesse de lecture du slider dépend de la machine "
         u"et de la complexité de la définition.",
  mode=u"SingleValue", tol=u"0"),

"G-26": dict(
  competence=u"Comparer une série de mesures à un intervalle de tolérance et "
             u"compter les écarts, des deux côtés.",
  bloom=u"Appliquer × procédurale",
  contexte=u"La coloration conditionnelle est le contrôle qualité du "
           u"modeleur : elle dit d'un coup d'œil ce qu'un tableau de vingt "
           u"lignes met une minute à dire.",
  att=u"8 pièces non conformes.",
  erreur=u"Ne tester qu'une borne — les pièces trop courtes — et compter 5 au "
         u"lieu de 8. Une tolérance a DEUX bornes : ici trois pièces "
         u"dépassent 900 mm, et un contrôle qui ne regarde que le bas les "
         u"laisse passer en vert.",
  donnees_note=u"Vingt longueurs de 250 à 1 150 mm : cinq sous 400, trois "
               u"au-dessus de 900, douze conformes. Les deux dépassements "
               u"sont de tailles différentes, de sorte que le compte partiel "
               u"(5) et le compte complet (8) ne se confondent pas — et "
               u"qu'aucun ne vaut la moitié de vingt.",
  limite=u"Le compte se vérifie, la COULEUR non : Grasshopper n'exporte pas "
         u"l'aperçu coloré sous forme de valeur. La coloration se juge à "
         u"l'écran.",
  mode=u"SingleValue", tol=u"0"),

"G-27": dict(
  competence=u"Disposer une série d'objets sur un cercle et mesurer la "
             u"disposition obtenue plutôt que de la constater.",
  bloom=u"Appliquer × procédurale",
  contexte=u"La scénarisation inscrit une série d'exercices dans un fil "
           u"narratif. Un apprenant qui construit une savane retient mieux "
           u"qu'un apprenant qui construit « une trame polaire de douze "
           u"éléments ».",
  att=u"17 082,06 mm — le périmètre du polygone que forment les douze "
      u"animaux, à 0,01 près.",
  erreur=u"Disposer les animaux sur le cercle de l'abreuvoir lui-même, rayon "
         u"1 800, au lieu du cercle à 950 mm au-delà : 11 180,98 mm. Les douze "
         u"animaux boivent alors les pieds dans l'eau — l'écart demandé est "
         u"une distance AU BORD, pas au centre.",
  donnees_note=u"Un abreuvoir de 1 800 mm de rayon, des animaux à 950 mm du "
               u"bord : le rayon de la harde vaut 2 750 mm, et le périmètre "
               u"du douzagone régulier 17 082,06. La confusion bord/centre "
               u"change la réponse de 53 %, ce qui ne peut pas passer pour un "
               u"arrondi.",
  limite=u"Le périmètre dit que les douze animaux sont bien RÉPARTIS sur le "
         u"bon cercle. Il ne dit rien de leur ORIENTATION vers le centre, qui "
         u"se juge à l'aperçu — un animal retourné laisse le périmètre "
         u"intact.",
  mode=u"NumericTolerance", tol=u"0.01"),

"G-28": dict(
  competence=u"Concevoir un codage qui reste valide sur TOUTES les "
             u"combinaisons, et le prouver en les parcourant.",
  bloom=u"Créer × procédurale",
  contexte=u"L'avatar est un objet que l'apprenant retrouve tout au long du "
           u"parcours. Il n'a de valeur que s'il ne casse jamais — d'où "
           u"l'exigence de robustesse sur les soixante-douze combinaisons.",
  att=u"16 452 — la somme des soixante-douze codes de configuration.",
  erreur=u"Vérifier son avatar sur la seule combinaison choisie. Un codage "
         u"qui marche sur 1-1-1 et casse sur 3-4-6 passe tous les contrôles "
         u"visuels — c'est la définition même d'une régression, et la somme "
         u"des 72 codes est le seul moyen simple de l'exclure.",
  donnees_note=u"3 formes, 4 motifs, 6 couleurs, code = forme×100 + "
               u"motif×10 + couleur : les codes vont de 111 à 346 sans "
               u"collision, et leur somme 16 452 n'est atteinte que si les "
               u"soixante-douze sont produits. Il en manque un, la somme le "
               u"dit.",
  limite=u"La somme prouve que les 72 codes sont PRODUITS, pas que les 72 "
         u"avatars sont beaux ni même géométriquement valides. La robustesse "
         u"visuelle se regarde.",
  mode=u"SingleValue", tol=u"0"),

"G-29": dict(
  competence=u"Trier une série et en extraire la médiane, en distinguant "
             u"médiane et moyenne.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le défi du jour installe une habitude : dix minutes, une "
           u"question, tous les jours. Sa vertu n'est pas la difficulté mais "
           u"la régularité.",
  att=u"1 119 mm — la longueur médiane.",
  erreur=u"Rendre la MOYENNE, 1 203 mm, au lieu de la médiane. Les deux "
         u"répondent à « la longueur typique » et ne diffèrent que de 84 mm "
         u"ici — assez pour fausser un débit, pas assez pour alerter. La "
         u"moyenne suit les extrêmes, la médiane non.",
  donnees_note=u"Quarante-et-une pièces — un nombre IMPAIR, de sorte que la "
               u"médiane est une valeur réellement présente dans la liste et "
               u"non une demi-somme. Les longueurs vont de 120 à 2 400 mm, "
               u"assez étalées pour que moyenne et médiane s'écartent "
               u"nettement.",
  limite=u"Le défi est présenté comme « différent chaque jour ». La "
         u"définition livrée en fige UN : la banque de trente micro-tâches "
         u"annoncée par la fiche reste à écrire, et l'exercice ne la fournit "
         u"pas.",
  mode=u"SingleValue", tol=u"0"),

"G-30": dict(
  competence=u"Structurer des données en branches puis les traiter branche "
             u"par branche, de façon qu'un tiers puisse reprendre le travail.",
  bloom=u"Créer × procédurale",
  contexte=u"Le relais mesure ce qu'aucun exercice individuel ne mesure : la "
           u"lisibilité. Une définition qu'un binôme ne peut pas reprendre "
           u"est une définition perdue, quelle que soit sa justesse.",
  att=u"2 904,3333 — la somme des six moyennes, à 0,0001 près.",
  erreur=u"Écarter les extrêmes sur l'ENSEMBLE des 96 valeurs avant de "
         u"répartir en branches, au lieu d'écarter deux valeurs hautes et "
         u"deux basses DANS CHAQUE branche. Les deux lectures sont "
         u"défendables à l'oral ; une seule donne 2 904,33, et c'est "
         u"exactement le genre d'ambiguïté qu'un relais révèle.",
  donnees_note=u"Quatre-vingt-seize valeurs de 20 à 980, en six branches de "
               u"seize. Écarter deux extrêmes de chaque côté laisse douze "
               u"valeurs par branche : les six moyennes vont de 415,0 à "
               u"579,25 et sont toutes différentes, de sorte qu'une branche "
               u"mal traitée se voit dans la somme.",
  limite=u"La somme valide le RÉSULTAT. La lisibilité — la moitié du barème "
         u"— est évaluée par le binôme, et ne peut pas l'être autrement : "
         u"aucune mesure automatique ne dit si une définition se comprend.",
  mode=u"NumericTolerance", tol=u"0.0001"),

"G-31": dict(
  competence=u"Croiser deux séries — ce qui est requis, ce qui est acquis — "
             u"et compter ce qui est complet.",
  bloom=u"Analyser × procédurale",
  contexte=u"L'arbre de compétences donne à l'apprenant la vue d'ensemble "
           u"qui manque toujours : ce qu'il a fait, ce qu'il lui reste, et "
           u"par où passer.",
  att=u"21 notions entièrement acquises.",
  erreur=u"Compter les notions ENTAMÉES — celles où au moins un exercice est "
         u"validé — au lieu des notions complètes : 37 au lieu de 21. L'arbre "
         u"paraît alors aux trois quarts vert alors qu'il est à 44 %, et "
         u"l'apprenant se croit plus avancé qu'il n'est.",
  donnees_note=u"Quarante-huit notions portant de 1 à 4 exercices, avec de 0 "
               u"à 4 validés. Une notion peut avoir PLUS de validés que "
               u"d'exercices portés — cas réel d'un exercice retiré du "
               u"référentiel — et la comparaison doit rester « au moins », "
               u"pas « exactement ».",
  limite=u"Le compte se vérifie ; la LISIBILITÉ de l'arbre — la moitié du "
         u"barème — non. Un nœud par notion et une branche par domaine se "
         u"jugent à l'œil, comme tout dessin.",
  mode=u"SingleValue", tol=u"0"),

"G-32": dict(
  competence=u"Restructurer un arbre pour atteindre une structure imposée, "
             u"et savoir décrire cette structure par ses effectifs.",
  bloom=u"Analyser × procédurale",
  contexte=u"L'économie d'indices responsabilise : demander de l'aide a un "
           u"coût, ne pas en demander quand on est bloqué en a un autre. "
           u"L'apprenant apprend à arbitrer, ce qui est le vrai sujet.",
  att=u"La structure cible, branche par branche : 4, 1, 0, 3, 2, 2, 3, 2, 2.",
  erreur=u"Rendre les VALEURS retenues au lieu des effectifs par branche. La "
         u"structure d'un arbre se décrit par le nombre d'éléments de chaque "
         u"branche — c'est ce que montre le Panel, et c'est ce qui permet de "
         u"comparer deux arbres sans comparer leur contenu.",
  donnees_note=u"Soixante-douze valeurs en neuf branches de huit. Une branche "
               u"est VIDE — zéro multiple de 5 — et deux branches ont le même "
               u"effectif : la structure ne peut pas se deviner par "
               u"régularité, et la branche vide vérifie qu'on ne supprime pas "
               u"les branches sans contenu.",
  limite=u"Les effectifs disent la FORME de l'arbre, pas son contenu. Deux "
         u"arbres de mêmes effectifs mais de valeurs différentes passeraient "
         u"tous deux — le contrôle porte sur la restructuration, qui est le "
         u"sujet de l'exercice.",
  mode=u"ExactOrderedList", tol=u"0"),

}


def fusionner(exo):
    """Rend la fiche d'origine enrichie de la couche pedagogique."""
    r = dict(exo)
    couche = SKILL_G.get(exo["id"])
    if not couche:
        return r
    for cle, valeur in couche.items():
        r[cle] = valeur
    r.setdefault(u"verdict", u"competence")
    if r[u"verdict"] == u"competence":
        r[u"competence"] = couche.get(u"competence", exo.get("obj", u""))
    return r
