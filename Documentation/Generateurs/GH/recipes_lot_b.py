# -*- coding: utf-8 -*-
"""Recettes de construction du LOT B — algorithmes combines.

Memes conventions et memes deux formes de corrige que les vagues precedentes :
la CHAINE quand elle mene naturellement au resultat, l'ETALON quand elle
serait une contorsion — placement de plaques, numerotation par tri compose,
decoupe par heuristique.

Le lot B est presque entierement parametrique : ses donnees sont des cotes, et
elles vivent donc sur des curseurs. Faire varier la portee d'un treillis ou la
hauteur d'un escalier et voir la reponse suivre EST une partie de ce que
l'exercice enseigne.
"""
import math
import os
import sys

try:
    _ICI = os.path.dirname(os.path.abspath(__file__))
except NameError:
    _ICI = r"C:\Users\charl\.claude\projects\MAGPIE\Documentation\Generateurs\GH"
_GEN = os.path.abspath(os.path.join(_ICI, ".."))
for _p in (_ICI, _GEN):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import skill_b as B
from recipes_vague2 import _etalon

R = {}


# ---------------------------------------------------------------------------
# B-01 — l'escalier et la regle de Blondel
# ---------------------------------------------------------------------------

_1 = B.D_B01

R["B-01"] = dict(
    sujet=[
        ("h", "SLIDER", 0, 0,
         {"slider": (2000, 4000, _1["hauteur"], 0), "nick": u"Hauteur d'etage"}),
        ("g", "SLIDER", 0, 1,
         {"slider": (200, 350, _1["giron"], 0), "nick": u"Giron"}),
        ("v", "SLIDER", 0, 2,
         {"slider": (150, 200, _1["visee"], 1), "nick": u"Hauteur de marche visee"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le nombre de contremarches est un ENTIER : 2 850 ÷ 172,5 vaut "
         u"16,52, donc 17", [
            ("dv", "Division", 1, 0, {}),
            ("rd", "Round", 2, 0, {}),
        ]),
        (u"La hauteur réelle se recale sur cet entier : 2 850 ÷ 17 vaut "
         u"167,65 mm, et non les 172,5 visés. Garder la valeur visée donnerait "
         u"un escalier de 2 932 mm — qui dépasse l'étage de 82 mm", [
            ("hr", "Division", 3, 0, {}),
        ]),
        (u"Blondel : deux fois la hauteur, plus le giron. 615,29 mm, dans la "
         u"plage 600-650. La valeur fausse, 625, y est AUSSI — le contrôle "
         u"réglementaire ne rattrape donc pas l'erreur", [
            ("h2", "Multiplication", 4, 0, {"val": [(1, "Number", [2])]}),
            ("bl", "Addition", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("h", "dv", 0), ("v", "dv", 1), ("dv", "rd", 0),
           ("h", "hr", 0), ("rd", 0, "hr", 1),
           ("hr", "h2", 0), ("h2", "bl", 0), ("g", "bl", 1),
           ("bl", "pan", 0), ("bl", "rep", 0)],
)


# ---------------------------------------------------------------------------
# B-02 — le garde-corps
# ---------------------------------------------------------------------------

_2 = B.D_B02

R["B-02"] = dict(
    sujet=[
        ("l", "SLIDER", 0, 0,
         {"slider": (1000, 6000, _2["longueur"], 0), "nick": u"Main courante"}),
        ("d", "SLIDER", 0, 1,
         {"slider": (8, 30, _2["diametre"], 0), "nick": u"Diametre du barreau"}),
        ("li", "SLIDER", 0, 2,
         {"slider": (50, 200, _2["libre_max"], 0), "nick": u"Espace libre maximal"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le pas d'un barreau au suivant n'est pas l'espace libre : c'est "
         u"l'espace libre PLUS le diamètre du barreau", [
            ("pas", "Addition", 1, 0, {}),
        ]),
        (u"La longueur à répartir se compte entre nus de montants, d'où le "
         u"diamètre retranché une fois", [
            ("net", "Subtraction", 1, 3, {}),
            ("dv", "Division", 2, 0, {}),
        ]),
        (u"Arrondi au SUPÉRIEUR — un espace de trop violerait la règle — puis "
         u"un barreau de moins que d'espaces : 25 barreaux, pour 108 mm de "
         u"libre. Diviser par le seul espace libre en donnerait 30, soit 20 % "
         u"de matière en trop", [
            ("rd", "Round", 3, 0, {}),
            ("nb", "Subtraction", 4, 0, {"val": [(1, "Number", [1])]}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("li", "pas", 0), ("d", "pas", 1),
           ("l", "net", 0), ("d", "net", 1),
           ("net", "dv", 0), ("pas", "dv", 1),
           ("dv", "rd", 0), ("rd", 2, "nb", 0),
           ("nb", "pan", 0), ("nb", "rep", 0)],
)


# ---------------------------------------------------------------------------
# B-03 — la facade a trame variable
# ---------------------------------------------------------------------------

def _rayons_b03():
    d = B.D_B03
    att = (d["attracteur"][0] * d["pas"], d["attracteur"][1] * d["pas"])
    centres = [((i + 0.5) * d["pas"], (j + 0.5) * d["pas"])
               for j in range(d["ny"]) for i in range(d["nx"])]
    dist = [math.hypot(c[0] - att[0], c[1] - att[1]) for c in centres]
    dmin, dmax = min(dist), max(dist)
    return [d["rayon_max"] + (d["rayon_min"] - d["rayon_max"])
            * (x - dmin) / (dmax - dmin) for x in dist]


R["B-03"] = dict(
    sujet=[
        ("nx", "SLIDER", 0, 0,
         {"slider": (4, 20, B.D_B03["nx"], 0), "nick": u"Mailles en largeur"}),
        ("ny", "SLIDER", 0, 1,
         {"slider": (4, 20, B.D_B03["ny"], 0), "nick": u"Mailles en hauteur"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon porte les 96 rayons, tels que la distance à l'attracteur "
         u"les donne : de 350 mm au plus près à 50 mm au plus loin", [
            ("r", "DATA:Number", 1, 0,
             {"nick": u"RAYONS", "data": _rayons_b03()}),
        ]),
        (u"L'aire d'un disque va comme le CARRÉ du rayon. C'est ce qui rend "
         u"la moyenne trompeuse : la moyenne des carrés n'est pas le carré de "
         u"la moyenne, et l'écart est toujours dans le même sens", [
            ("r2", "Multiplication", 2, 0, {}),
            ("pi", "Pi", 3, 2, {"val": [(0, "Number", [1])]}),
            ("aire", "Multiplication", 3, 0, {}),
        ]),
        (u"13,30 m² au total. Le calcul par le rayon moyen en donnerait "
         u"12,06 — 1,24 m² de vitrage qui manquent à la commande", [
            ("som", "Mass Addition", 4, 0, {}),
            ("m2", "Division", 5, 0, {"val": [(1, "Number", [1000000])]}),
            ("pan", "PANEL", 6, 2, {}),
        ]),
    ],
    wires=[("r", "r2", 0), ("r", "r2", 1),
           ("r2", "aire", 0), ("pi", "aire", 1),
           ("aire", "som", 0), ("som", "m2", 0),
           ("m2", "pan", 0), ("m2", "rep", 0)],
)


# ---------------------------------------------------------------------------
# B-04 — le pavage hexagonal
# ---------------------------------------------------------------------------

_4 = B.D_B04

R["B-04"] = dict(
    sujet=[
        ("c", "SLIDER", 0, 0,
         {"slider": (100, 800, _4["cote"], 0), "nick": u"Cote de l'hexagone"}),
        ("la", "SLIDER", 0, 1,
         {"slider": (2000, 20000, _4["largeur"], 0), "nick": u"Largeur"}),
        ("pr", "SLIDER", 0, 2,
         {"slider": (2000, 20000, _4["profondeur"], 0), "nick": u"Profondeur"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le pas HORIZONTAL d'une trame hexagonale vaut √3 fois le côté — "
         u"692,8 mm ici, et non 400", [
            ("tr", "Square Root", 1, 0, {"val": [(0, "Number", [3])]}),
            ("px", "Multiplication", 2, 0, {}),
        ]),
        (u"Le pas VERTICAL vaut une fois et demie le côté : 600 mm. Les deux "
         u"pas diffèrent, c'est ce qui distingue une trame hexagonale d'une "
         u"trame carrée", [
            ("py", "Multiplication", 2, 3, {"val": [(1, "Number", [1.5])]}),
        ]),
        (u"13 colonnes et 10 rangées : 130 hexagones. Diviser par le CÔTÉ au "
         u"lieu du pas en donnerait 384, soit trois fois trop", [
            ("dx", "Division", 3, 0, {}),
            ("dy", "Division", 3, 3, {}),
            ("nx", "Round", 4, 0, {}),
            ("ny", "Round", 4, 3, {}),
            ("n", "Multiplication", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("c", "px", 0), ("tr", "px", 1),
           ("c", "py", 0),
           ("la", "dx", 0), ("px", "dx", 1),
           ("pr", "dy", 0), ("py", "dy", 1),
           ("dx", "nx", 0), ("dy", "ny", 0),
           ("nx", 1, "n", 0), ("ny", 1, "n", 1),
           ("n", "pan", 0), ("n", "rep", 0)],
)


# ---------------------------------------------------------------------------
# B-05 — la poutre treillis
# ---------------------------------------------------------------------------

_5 = B.D_B05

R["B-05"] = dict(
    sujet=[
        ("p", "SLIDER", 0, 0,
         {"slider": (4000, 30000, _5["portee"], 0), "nick": u"Portee"}),
        ("ht", "SLIDER", 0, 1,
         {"slider": (300, 2000, _5["hauteur"], 0), "nick": u"Hauteur"}),
        ("n", "SLIDER", 0, 2,
         {"slider": (2, 20, _5["panneaux"], 0), "nick": u"Panneaux"}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Les deux membrures courent sur toute la portée : 24 000 mm", [
            ("mem", "Multiplication", 1, 0, {"val": [(1, "Number", [2])]}),
        ]),
        (u"Le pas d'un panneau : 1 500 mm. La DIAGONALE, elle, traverse le "
         u"panneau en biais — c'est l'hypoténuse du pas et de la hauteur, "
         u"1 749 mm, soit 17 % de plus", [
            ("pas", "Division", 1, 3, {}),
            ("p2", "Multiplication", 2, 3, {}),
            ("h2", "Multiplication", 2, 5, {}),
            ("som", "Addition", 3, 3, {}),
            ("diag", "Square Root", 4, 3, {}),
        ]),
        (u"Huit diagonales : 13 994 mm. Total 37,99 m. Compter la diagonale "
         u"comme un panneau donnerait 36,00 m — deux mètres de tube qui "
         u"manquent", [
            ("tdiag", "Multiplication", 5, 3, {}),
            ("tot", "Addition", 6, 0, {}),
            ("m", "Division", 7, 0, {"val": [(1, "Number", [1000])]}),
            ("pan", "PANEL", 8, 0, {}),
        ]),
    ],
    wires=[("p", "mem", 0),
           ("p", "pas", 0), ("n", "pas", 1),
           ("pas", "p2", 0), ("pas", "p2", 1),
           ("ht", "h2", 0), ("ht", "h2", 1),
           ("p2", "som", 0), ("h2", "som", 1), ("som", "diag", 0),
           ("diag", "tdiag", 0), ("n", "tdiag", 1),
           ("mem", "tot", 0), ("tdiag", "tot", 1),
           ("tot", "m", 0), ("m", "pan", 0), ("m", "rep", 0)],
)


# ---------------------------------------------------------------------------
# B-06 et B-07 — le caisson et son tiroir
# ---------------------------------------------------------------------------

_6 = B.D_B06

R["B-06"] = dict(
    sujet=[
        ("l", "SLIDER", 0, 0,
         {"slider": (300, 1600, _6["largeur"], 0), "nick": u"Largeur"}),
        ("h", "SLIDER", 0, 1,
         {"slider": (300, 2200, _6["hauteur"], 0), "nick": u"Hauteur"}),
        ("p", "SLIDER", 0, 2,
         {"slider": (200, 700, _6["profondeur"], 0), "nick": u"Profondeur"}),
        ("e", "SLIDER", 0, 3,
         {"slider": (10, 30, _6["epaisseur"], 0), "nick": u"Epaisseur"}),
        ("ra", "SLIDER", 0, 4,
         {"slider": (0, 15, _6["rainure"], 0), "nick": u"Profondeur de rainure"}),
        ("rep", "REPONSE", 10, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Les deux joues, pleine hauteur et pleine profondeur", [
            ("j1", "Multiplication", 1, 0, {}),
            ("j2", "Multiplication", 2, 0, {}),
            ("joues", "Multiplication", 3, 0, {"val": [(1, "Number", [2])]}),
        ]),
        (u"Les deux traverses, entre les joues : la largeur diminue de deux "
         u"épaisseurs", [
            ("e2", "Multiplication", 1, 3, {"val": [(1, "Number", [2])]}),
            ("li", "Subtraction", 2, 3, {}),
            ("t1", "Multiplication", 3, 3, {}),
            ("t2", "Multiplication", 4, 3, {}),
            ("trav", "Multiplication", 5, 3, {"val": [(1, "Number", [2])]}),
        ]),
        (u"Le fond entre DANS les rainures : il se débite plus grand que le "
         u"vide intérieur, de deux fois la profondeur de rainure dans chaque "
         u"dimension. Le couper aux cotes nettes le rendrait inutilisable", [
            ("r2", "Multiplication", 1, 6, {"val": [(1, "Number", [2])]}),
            ("fl", "Addition", 2, 6, {}),
            ("hi", "Subtraction", 2, 8, {}),
            ("fh", "Addition", 3, 8, {}),
            ("f1", "Multiplication", 4, 6, {}),
            ("fond", "Multiplication", 5, 6, {}),
        ]),
        (u"32,73 dm³ de panneau. Sans les rainures : 32,40 — 1 % d'écart, "
         u"invisible au devis et fatal au montage", [
            ("s1", "Addition", 6, 0, {}),
            ("s2", "Addition", 7, 0, {}),
            ("dm3", "Division", 8, 0, {"val": [(1, "Number", [1000000])]}),
            ("pan", "PANEL", 9, 0, {}),
        ]),
    ],
    wires=[("h", "j1", 0), ("p", "j1", 1), ("j1", "j2", 0), ("e", "j2", 1),
           ("j2", "joues", 0),
           ("e", "e2", 0), ("l", "li", 0), ("e2", "li", 1),
           ("li", "t1", 0), ("p", "t1", 1), ("t1", "t2", 0), ("e", "t2", 1),
           ("t2", "trav", 0),
           ("ra", "r2", 0), ("li", "fl", 0), ("r2", "fl", 1),
           ("h", "hi", 0), ("e2", "hi", 1), ("hi", "fh", 0), ("r2", "fh", 1),
           ("fl", "f1", 0), ("fh", "f1", 1), ("f1", "fond", 0), ("e", "fond", 1),
           ("joues", "s1", 0), ("trav", "s1", 1),
           ("s1", "s2", 0), ("fond", "s2", 1),
           ("s2", "dm3", 0), ("dm3", "pan", 0), ("dm3", "rep", 0)],
)

R["B-07"] = dict(
    sujet=[
        ("l", "SLIDER", 0, 0,
         {"slider": (300, 1600, _6["largeur"], 0), "nick": u"Largeur du caisson"}),
        ("e", "SLIDER", 0, 1,
         {"slider": (10, 30, _6["epaisseur"], 0), "nick": u"Epaisseur du panneau"}),
        ("j", "SLIDER", 0, 2,
         {"slider": (5, 25, B.D_B07["jeu_lateral"], 0), "nick": u"Jeu par cote"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'intérieur du caisson : la largeur moins DEUX épaisseurs de joue, "
         u"soit 762 mm", [
            ("e2", "Multiplication", 1, 0, {"val": [(1, "Number", [2])]}),
            ("li", "Subtraction", 2, 0, {}),
        ]),
        (u"La coulisse se pose des DEUX côtés : le jeu se retranche deux "
         u"fois. 736 mm. Ne le retrancher qu'une fois donnerait 749 — 13 mm "
         u"de trop, et le tiroir n'entre pas", [
            ("j2", "Multiplication", 1, 3, {"val": [(1, "Number", [2])]}),
            ("lt", "Subtraction", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("e", "e2", 0), ("l", "li", 0), ("e2", "li", 1),
           ("j", "j2", 0), ("li", "lt", 0), ("j2", "lt", 1),
           ("lt", "pan", 0), ("lt", "rep", 0)],
)


# ---------------------------------------------------------------------------
# B-08 — l'etagere a pas variable
# ---------------------------------------------------------------------------

_8 = B.D_B08

R["B-08"] = dict(
    sujet=[
        ("h", "SLIDER", 0, 0,
         {"slider": (1000, 3000, _8["hauteur"], 0), "nick": u"Hauteur totale"}),
        ("n", "SLIDER", 0, 1,
         {"slider": (2, 12, _8["tablettes"], 0), "nick": u"Tablettes"}),
        ("e", "SLIDER", 0, 2,
         {"slider": (10, 40, _8["epaisseur"], 0), "nick": u"Epaisseur"}),
        ("m", "SLIDER", 0, 3,
         {"slider": (100, 300, _8["mini"], 0), "nick": u"Plus petit entre-deux"}),
        ("rep", "REPONSE", 10, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"La hauteur réellement LIBRE : le total moins l'épaisseur des six "
         u"tablettes, soit 1 868 mm et non 2 000", [
            ("ep", "Multiplication", 1, 0, {}),
            ("libre", "Subtraction", 2, 0, {}),
        ]),
        (u"Sept entre-deux pour six tablettes — un de plus, comme toujours "
         u"entre des intervalles et ce qui les sépare", [
            ("ne", "Addition", 1, 3, {"val": [(1, "Number", [1])]}),
        ]),
        (u"En progression arithmétique, la somme vaut n fois le premier terme "
         u"plus la raison multipliée par la somme des rangs — n(n−1)/2. On "
         u"inverse pour trouver la raison : 28,95 mm", [
            ("nm", "Multiplication", 3, 3, {}),
            ("reste", "Subtraction", 4, 0, {}),
            ("n1", "Subtraction", 3, 6, {"val": [(1, "Number", [1])]}),
            ("prod", "Multiplication", 4, 6, {}),
            ("demi", "Division", 5, 6, {"val": [(1, "Number", [2])]}),
            ("r", "Division", 6, 0, {}),
        ]),
        (u"Le plus grand entre-deux est le premier plus six fois la raison : "
         u"353,71 mm. Répartir 2 000 mm au lieu de 1 868 le porterait à "
         u"378,3, et la dernière tablette dépasserait du meuble", [
            ("nr", "Multiplication", 7, 0, {}),
            ("gr", "Addition", 8, 0, {}),
            ("pan", "PANEL", 9, 0, {}),
        ]),
    ],
    wires=[("n", "ep", 0), ("e", "ep", 1),
           ("h", "libre", 0), ("ep", "libre", 1),
           ("n", "ne", 0),
           ("ne", "nm", 0), ("m", "nm", 1),
           ("libre", "reste", 0), ("nm", "reste", 1),
           ("ne", "n1", 0), ("ne", "prod", 0), ("n1", "prod", 1),
           ("prod", "demi", 0),
           ("reste", "r", 0), ("demi", "r", 1),
           ("n1", "nr", 0), ("r", "nr", 1),
           ("m", "gr", 0), ("nr", "gr", 1),
           ("gr", "pan", 0), ("gr", "rep", 0)],
)


# ---------------------------------------------------------------------------
# B-09, B-10, B-11 — la joaillerie
# ---------------------------------------------------------------------------

_9 = B.D_B09

R["B-09"] = dict(
    sujet=[
        ("n", "SLIDER", 0, 0,
         {"slider": (2, 8, _9["griffes"], 0), "nick": u"Griffes"}),
        ("ht", "SLIDER", 0, 1,
         {"slider": (1, 10, _9["hauteur"], 1), "nick": u"Hauteur de griffe"}),
        ("a", "SLIDER", 0, 2,
         {"slider": (0, 45, _9["inclinaison"], 0), "nick": u"Inclinaison"}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Une griffe inclinée est plus longue que la hauteur qu'elle "
         u"couvre : sa longueur est la hauteur DIVISÉE par le cosinus de "
         u"l'inclinaison", [
            ("rad", "Radians", 1, 0, {}),
            ("cos", "Cosine", 2, 0, {}),
            ("lg", "Division", 3, 0, {}),
        ]),
        (u"Quatre griffes : 14,72 mm de fil. La hauteur droite en donnerait "
         u"14,40 — sur une série, c'est de l'or qui manque à chaque montage", [
            ("tot", "Multiplication", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("a", "rad", 0), ("rad", "cos", 0),
           ("ht", "lg", 0), ("cos", "lg", 1),
           ("lg", "tot", 0), ("n", "tot", 1),
           ("tot", "pan", 0), ("tot", "rep", 0)],
)

_10 = B.D_B10

R["B-10"] = dict(
    sujet=[
        ("c", "SLIDER", 0, 0,
         {"slider": (40, 80, _10["circonference"], 0), "nick": u"Circonference"}),
        ("n", "SLIDER", 0, 1,
         {"slider": (4, 24, _10["modules"], 0), "nick": u"Modules"}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"La taille d'un anneau est une CIRCONFÉRENCE, pas un diamètre. Le "
         u"motif se développe sur elle, et douze modules la partagent "
         u"exactement", [
            ("dv", "Division", 1, 0, {}),
            ("pan", "PANEL", 2, 0, {}),
        ]),
        (u"4,50 mm par module — un compte rond, qui rend le raccord "
         u"vérifiable à la règle. Prendre la circonférence pour un diamètre "
         u"donnerait 1,43 mm, et les douze modules ne couvriraient qu'un "
         u"tiers du tour", [
            ("note", "PANEL", 2, 2,
             {"text": u"Taille d'anneau = CIRCONFERENCE.\n\n"
                      u"54 / 12 = 4,50 mm\n"
                      u"54 / pi / 12 = 1,43 mm  (faux)",
              "h": 76, "w": 260}),
        ]),
    ],
    wires=[("c", "dv", 0), ("n", "dv", 1),
           ("dv", "pan", 0), ("dv", "rep", 0)],
)

_11 = B.D_B11

R["B-11"] = dict(
    sujet=[
        ("lc", "SLIDER", 0, 0,
         {"slider": (50, 500, _11["courbe"], 1), "nick": u"Longueur de courbe"}),
        ("m", "SLIDER", 0, 1,
         {"slider": (1, 20, _11["maillon"], 1), "nick": u"Maillon"}),
        ("rc", "SLIDER", 0, 2,
         {"slider": (0, 10, _11["recouvrement"], 1), "nick": u"Recouvrement"}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le pas d'un maillon au suivant n'est pas sa taille : les maillons "
         u"s'enfilent, d'où le recouvrement retranché. 4 − 1,2 = 2,8 mm", [
            ("pas", "Subtraction", 1, 0, {}),
        ]),
        (u"La longueur à couvrir après le premier maillon, divisée par le "
         u"pas, arrondie à l'entier INFÉRIEUR — un maillon qui dépasse ne "
         u"tient pas — puis le premier maillon rajouté", [
            ("net", "Subtraction", 1, 3, {}),
            ("dv", "Division", 2, 0, {}),
            ("rd", "Round", 3, 0, {}),
            ("n", "Addition", 4, 0, {"val": [(1, "Number", [1])]}),
        ]),
        (u"66 maillons. Diviser la courbe par la taille du maillon en "
         u"donnerait 46 — la chaîne arriverait vingt maillons trop courte", [
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("m", "pas", 0), ("rc", "pas", 1),
           ("lc", "net", 0), ("m", "net", 1),
           ("net", "dv", 0), ("pas", "dv", 1),
           ("dv", "rd", 0), ("rd", 1, "n", 0),
           ("n", "pan", 0), ("n", "rep", 0)],
)


# ---------------------------------------------------------------------------
# B-12 a B-15 — donnees, metres et livrables
# ---------------------------------------------------------------------------

R["B-12"] = dict(
    sujet=[
        ("n", "SLIDER", 0, 0,
         {"slider": (1, 60, B.D_B12["pieces"], 0), "nick": u"Pieces de l'assemblage"}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Une ligne par pièce, plus la ligne d'en-tête qui nomme les "
         u"colonnes. Quinze lignes", [
            ("add", "Addition", 1, 0, {"val": [(1, "Number", [1])]}),
            ("pan", "PANEL", 2, 0, {}),
        ]),
        (u"L'oublier fait lire la première pièce comme un nom de colonne : "
         u"elle disparaît de la nomenclature, sans erreur ni message. C'est "
         u"le même contrôle que QT-05, sur un assemblage plutôt qu'un débit", [
            ("note", "PANEL", 2, 2,
             {"text": u"14 pieces + 1 en-tete = 15 lignes.",
              "h": 44, "w": 240}),
        ]),
    ],
    wires=[("n", "add", 0), ("add", "pan", 0), ("add", "rep", 0)],
)

R["B-13"] = dict(
    sujet=[
        ("a", "DATA:Number", 0, 0,
         {"nick": u"AIRES_DES_PIECES",
          "data": [float(x * y) for x, y in B.D_B13_PIECES]}),
        ("pl", "DATA:Number", 0, 4,
         {"nick": u"AIRE_D_UNE_PLAQUE",
          "data": [B.D_B13_PLAQUE[0] * B.D_B13_PLAQUE[1]]}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"La surface à débiter : 12,00 m²", [
            ("som", "Mass Addition", 1, 0, {}),
        ]),
        (u"Rapportée à la plaque, elle en demande 2,07 — donc TROIS, "
         u"arrondi au supérieur : on ne commande pas 7 % de plaque", [
            ("dv", "Division", 2, 0, {}),
            ("rd", "Round", 3, 0, {}),
        ]),
        (u"La chute est ce qui reste des trois plaques : 31,00 %. C'est un "
         u"MINORANT — le placement réel ajoute sa propre chute, et le taux "
         u"d'atelier est toujours supérieur", [
            ("dispo", "Multiplication", 4, 0, {}),
            ("part", "Division", 5, 0, {}),
            ("un", "Subtraction", 6, 0, {"val": [(0, "Number", [1])]}),
            ("cent", "Multiplication", 7, 0, {"val": [(1, "Number", [100])]}),
            ("pan", "PANEL", 8, 0, {}),
        ]),
    ],
    wires=[("a", "som", 0),
           ("som", "dv", 0), ("pl", "dv", 1),
           ("dv", "rd", 0),
           ("rd", 2, "dispo", 0), ("pl", "dispo", 1),
           ("som", "part", 0), ("dispo", "part", 1),
           ("part", "un", 1), ("un", "cent", 0),
           ("cent", "pan", 0), ("cent", "rep", 0)],
)


def _rang_b14():
    pos = B.D_B14_POSITIONS
    ordre = sorted(range(len(pos)), key=lambda i: (pos[i][1], pos[i][0]))
    return [float(ordre.index(pos.index(B.D_B14_CIBLE)) + 1)]


R["B-14"] = dict(
    sujet=[
        ("x", "DATA:Number", 0, 0,
         {"nick": u"ABSCISSES", "data": [float(p[0]) for p in B.D_B14_POSITIONS]}),
        ("y", "DATA:Number", 0, 3,
         {"nick": u"ORDONNEES", "data": [float(p[1]) for p in B.D_B14_POSITIONS]}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon porte le rang cherché, obtenu en triant par ORDONNÉE "
         u"d'abord, puis par abscisse — l'ordre de pose, rangée du bas en "
         u"premier", [
            ("r", "DATA:Number", 1, 0,
             {"nick": u"RANG_DE_LA_PIECE_VISEE", "data": _rang_b14()}),
        ]),
        (u"Rang 7. Trier par colonne d'abord donnerait 5, et l'ordre de "
         u"saisie 4 : l'ordre des critères n'est pas commutatif, et le "
         u"poseur ne s'y retrouve que dans un seul des trois", [
            ("li", "List Item", 2, 0, {"val": [(1, "Integer", [0])]}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("r", "li", 0), ("li", "pan", 0), ("li", "rep", 0)],
)


def _barres_b15():
    restes = []
    for x in sorted(B.D_B15_LONGUEURS, reverse=True):
        for k, r in enumerate(restes):
            if r >= x:
                restes[k] = r - x
                break
        else:
            restes.append(B.D_B15_BARRE - x)
    return [float(B.D_B15_BARRE - r) for r in restes]


R["B-15"] = dict(
    sujet=[
        ("lg", "DATA:Number", 0, 0,
         {"nick": u"LONGUEURS_A_DEBITER",
          "data": [float(x) for x in B.D_B15_LONGUEURS]}),
        ("ba", "DATA:Number", 0, 5,
         {"nick": u"LONGUEUR_D_UNE_BARRE", "data": [B.D_B15_BARRE]}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon porte le CHARGEMENT de chaque barre tel que la règle du "
         u"plus grand d'abord le produit : on place la plus longue pièce "
         u"restante dans la première barre qui peut encore la recevoir, et "
         u"l'on n'ouvre une barre neuve que si aucune n'y suffit", [
            ("ch", "DATA:Number", 1, 0,
             {"nick": u"CHARGE_DE_CHAQUE_BARRE", "data": _barres_b15()}),
        ]),
        (u"Douze barres. La borne théorique — 65 120 ÷ 6 000, arrondi au "
         u"supérieur — en annonce onze, et AUCUNE découpe ne l'atteint : les "
         u"longueurs ne se combinent pas pour remplir onze barres", [
            ("n", "List Length", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
        (u"Ce que l'exercice enseigne : une borne n'est pas un objectif. "
         u"Annoncer onze barres promet un rendement qu'aucun débit ne "
         u"donnera", [
            ("note", "PANEL", 3, 2,
             {"text": u"borne theorique : 11 barres\n"
                      u"plus grand d'abord : 12 barres\n\n"
                      u"L'ecart d'une barre se paie.",
              "h": 76, "w": 260}),
        ]),
    ],
    wires=[("ch", "n", 0), ("n", "pan", 0), ("n", "rep", 0)],
)


# ---------------------------------------------------------------------------
# B-16, B-17, B-18 — design produit
# ---------------------------------------------------------------------------

_16 = B.D_B16

R["B-16"] = dict(
    sujet=[
        ("n", "SLIDER", 0, 0,
         {"slider": (6, 48, _16["lamelles"], 0), "nick": u"Lamelles"}),
        ("we", "SLIDER", 0, 1,
         {"slider": (5, 60, _16["largeur_extremite"], 0), "nick": u"Largeur aux extremites"}),
        ("wm", "SLIDER", 0, 2,
         {"slider": (5, 100, _16["largeur_milieu"], 0), "nick": u"Largeur au milieu"}),
        ("ht", "SLIDER", 0, 3,
         {"slider": (100, 900, _16["hauteur"], 0), "nick": u"Hauteur"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"La largeur varie LINÉAIREMENT : sa moyenne est la demi-somme des "
         u"extrêmes, 30 mm — jamais le maximum", [
            ("som", "Addition", 1, 0, {}),
            ("moy", "Division", 2, 0, {"val": [(1, "Number", [2])]}),
        ]),
        (u"Une lamelle développée : hauteur par largeur moyenne", [
            ("une", "Multiplication", 3, 0, {}),
        ]),
        (u"Vingt-quatre lamelles : 0,3024 m². Prendre la largeur maximale "
         u"partout donnerait 0,4536 m², soit 50 % de tôle en trop", [
            ("tot", "Multiplication", 4, 0, {}),
            ("m2", "Division", 5, 0, {"val": [(1, "Number", [1000000])]}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("we", "som", 0), ("wm", "som", 1), ("som", "moy", 0),
           ("ht", "une", 0), ("moy", "une", 1),
           ("une", "tot", 0), ("n", "tot", 1),
           ("tot", "m2", 0), ("m2", "pan", 0), ("m2", "rep", 0)],
)

_17 = B.D_B17

R["B-17"] = dict(
    sujet=[
        ("c", "SLIDER", 0, 0,
         {"slider": (500, 8000, _17["corde"], 0), "nick": u"Corde"}),
        ("f", "SLIDER", 0, 1,
         {"slider": (50, 2000, _17["fleche"], 0), "nick": u"Fleche"}),
        ("n", "SLIDER", 0, 2,
         {"slider": (2, 30, _17["nervures"], 0), "nick": u"Nervures"}),
        ("rep", "REPONSE", 11, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le rayon d'un arc se retrouve de sa corde et de sa flèche : "
         u"(c²/4 + f²) ÷ 2f, soit 2 179 mm", [
            ("c2", "Multiplication", 1, 0, {}),
            ("c4", "Division", 2, 0, {"val": [(1, "Number", [4])]}),
            ("f2", "Multiplication", 1, 3, {}),
            ("num", "Addition", 3, 0, {}),
            ("f2b", "Multiplication", 2, 5, {"val": [(1, "Number", [2])]}),
            ("r", "Division", 4, 0, {}),
        ]),
        (u"Le demi-angle au centre est l'arcsinus de la demi-corde sur le "
         u"rayon ; l'arc vaut deux fois cet angle multiplié par le rayon — "
         u"3 594 mm, contre 3 200 de corde", [
            ("c2b", "Division", 5, 3, {"val": [(1, "Number", [2])]}),
            ("rap", "Division", 6, 3, {}),
            ("as", "ArcSine", 7, 3, {}),
            ("a2", "Multiplication", 8, 3, {"val": [(1, "Number", [2])]}),
            ("arc", "Multiplication", 9, 3, {}),
        ]),
        (u"Neuf nervures : 32,34 m. La corde en donnerait 28,80 — trois "
         u"mètres et demi qui manquent, répartis sur les neuf pièces, donc "
         u"vus tard", [
            ("tot", "Multiplication", 9, 0, {}),
            ("m", "Division", 10, 0, {"val": [(1, "Number", [1000])]}),
            ("pan", "PANEL", 10, 3, {}),
        ]),
    ],
    wires=[("c", "c2", 0), ("c", "c2", 1), ("c2", "c4", 0),
           ("f", "f2", 0), ("f", "f2", 1),
           ("c4", "num", 0), ("f2", "num", 1),
           ("f", "f2b", 0),
           ("num", "r", 0), ("f2b", "r", 1),
           ("c", "c2b", 0),
           ("c2b", "rap", 0), ("r", "rap", 1),
           ("rap", "as", 0), ("as", "a2", 0),
           ("a2", "arc", 0), ("r", "arc", 1),
           ("arc", "tot", 0), ("n", "tot", 1),
           ("tot", "m", 0), ("m", "pan", 0), ("m", "rep", 0)],
)

_18 = B.D_B18

R["B-18"] = dict(
    sujet=[
        ("d", "SLIDER", 0, 0,
         {"slider": (3, 30, _18["diametre"], 0), "nick": u"Diametre nominal"}),
        ("p", "SLIDER", 0, 1,
         {"slider": (0.5, 4, _18["pas"], 2), "nick": u"Pas"}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le profil ISO retire 1,2269 fois le pas au diamètre nominal — le "
         u"filet est triangulaire à 60° et tronqué en fond comme en crête", [
            ("k", "Multiplication", 1, 0, {"val": [(1, "Number", [1.226869])]}),
            ("d3", "Subtraction", 2, 0, {}),
        ]),
        (u"8,16 mm. Retrancher le pas une seule fois donnerait 8,50 — la "
         u"section résistante paraîtrait 8 % plus grande qu'elle n'est, et "
         u"la vis plus solide qu'elle n'est", [
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("p", "k", 0), ("d", "d3", 0), ("k", "d3", 1),
           ("d3", "pan", 0), ("d3", "rep", 0)],
)
