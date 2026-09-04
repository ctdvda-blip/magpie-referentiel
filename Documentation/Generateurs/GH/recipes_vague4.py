# -*- coding: utf-8 -*-
"""Recettes de construction de la vague 4.

Les tableaux de ces exercices sont des inventaires : types, calques, canaux
de distribution, verbes d'operation. Le checker Magpie ne compare que des
NOMBRES, et une definition ne manipule pas commodement du texte. Chaque
colonne est donc fournie CODEE — 1 pour vrai, 0 pour faux, ou un code par
valeur possible — et la legende figure dans le sujet.

Ce codage ne facilite pas la tache : il la deplace au bon endroit. Ce que
l'exercice travaille est le raisonnement logique sur l'inventaire, pas la
comparaison de chaines.

UN SEUL ETALON : PL-15. Trouver le plus petit ensemble de plugins couvrant
douze composants est un probleme de couverture, qui ne se pose pas avec des
composants natifs. L'etalon donne le minimum et le commentaire dit pourquoi.
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

import exercices_vague4 as V

R = {}

# Ces deux noms sont LONGS a dessein. En IronPython 2, la variable de
# boucle d'une comprehension fuit dans la portee englobante : un
# `for _n, p, _f in ...` ecrasait la fonction `_f` par un booleen, et
# la recette suivante echouait sur « bool is not callable ». C'est la
# troisieme fois que ce piege se referme dans ce projet.
def _nombres(xs):
    return [float(x) for x in xs]


def _drapeaux(xs):
    return [1.0 if x else 0.0 for x in xs]


# ---------------------------------------------------------------------------
# PL-13 — où trouver chaque plugin
# ---------------------------------------------------------------------------
R["PL-13"] = dict(
    sujet=[
        ("pm", "DATA:Number", 0, 0,
         {"nick": u"SUR_LE_GESTIONNAIRE", "data": _drapeaux([p for _n, p, _f in V.D_PL13])}),
        ("f4", "DATA:Number", 0, 4,
         {"nick": u"SUR_FOOD4RHINO", "data": _drapeaux([f for _n, _p, f in V.D_PL13])}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"« Seulement sur Food4Rhino » est une EXCLUSIVITÉ : présent d'un "
         u"côté, absent de l'autre. Compter la seule colonne Food4Rhino "
         u"donnerait treize", [
            ("abs", "Equality", 1, 0, {"val": [(1, "Number", [0])]}),
            ("pres", "Equality", 1, 4, {"val": [(1, "Number", [1])]}),
            ("et", "Gate And", 2, 0, {}),
        ]),
        (u"6 plugins imposeront un téléchargement, un déblocage du fichier et "
         u"un redémarrage sur chaque poste", [
            ("cu", "Cull Pattern", 3, 0, {}),
            ("nb", "List Length", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("pm", "abs", 0), ("f4", "pres", 0),
           ("abs", 0, "et", 0), ("pres", 0, "et", 1),
           ("f4", "cu", 0), ("et", "cu", 1),
           ("cu", "nb", 0), ("nb", "pan", 0), ("nb", "rep", 0)],
)


# ---------------------------------------------------------------------------
# PL-14 — ce que l'ergonomie coûte au démarrage
# ---------------------------------------------------------------------------
R["PL-14"] = dict(
    sujet=[
        ("ms", "DATA:Number", 0, 0,
         {"nick": u"TEMPS_DE_CHARGEMENT_MS", "data": _nombres([m for _n, m, _d in V.D_PL14])}),
        ("dj", "DATA:Number", 0, 3,
         {"nick": u"DEJA_EXIGE_PAR_UN_AUTRE", "data": _drapeaux([d for _n, _m, d in V.D_PL14])}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Ce qui est déjà exigé par un plugin installé n'est pas imputable "
         u"à l'ergonomie : le compter reviendrait à facturer deux fois la "
         u"même seconde", [
            ("non", "Equality", 1, 3, {"val": [(1, "Number", [0])]}),
            ("cu", "Cull Pattern", 2, 0, {}),
        ]),
        (u"1 220 ms ajoutés. Tout additionner en donnerait 1 395 — 14 % de "
         u"plus, assez pour fausser une décision d'équipement", [
            ("so", "Mass Addition", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("dj", "non", 0),
           ("ms", "cu", 0), ("non", 0, "cu", 1),
           ("cu", "so", 0), ("so", "pan", 0), ("so", "rep", 0)],
)


# ---------------------------------------------------------------------------
# PL-15 — combien de plugins pour douze composants  (étalon)
# ---------------------------------------------------------------------------
R["PL-15"] = dict(
    sujet=[
        ("n", "SLIDER", 0, 0,
         {"slider": (1, 20, len(V.D_PL15_BESOIN), 0),
          "nick": u"Composants requis"}),
        ("p", "SLIDER", 0, 1,
         {"slider": (1, 12, len(V.D_PL15_FOURNI), 0),
          "nick": u"Plugins candidats"}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Couvrir douze composants par le plus petit nombre de plugins est "
         u"un problème de COUVERTURE : il se résout en énumérant les "
         u"sous-ensembles, ce qu'aucun composant natif ne fait. L'étalon "
         u"porte le minimum, et deux quartets différents l'atteignent — "
         u"c'est pourquoi la question porte sur le nombre", [
            ("v", "DATA:Number", 1, 0,
             {"nick": u"PLUGINS_AU_MINIMUM", "data": [4.0]}),
            ("pan", "PANEL", 2, 0, {}),
        ]),
    ],
    wires=[("v", "pan", 0), ("v", "rep", 0)],
)


# ---------------------------------------------------------------------------
# PL-16 — ce qui tourne encore sous Rhino 8
# ---------------------------------------------------------------------------
R["PL-16"] = dict(
    sujet=[
        ("mi", "DATA:Number", 0, 0,
         {"nick": u"VERSION_MINIMALE", "data": _nombres([a for _n, a, _b in V.D_PL16])}),
        ("ma", "DATA:Number", 0, 4,
         {"nick": u"VERSION_MAXIMALE", "data": _nombres([b for _n, _a, b in V.D_PL16])}),
        ("v", "SLIDER", 0, 8, {"slider": (5, 9, 8, 0), "nick": u"Version cible"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Un intervalle a DEUX bornes. La borne minimale ne rejette "
         u"personne ici — le test naïf donne quatorze sur quatorze, le score "
         u"parfait, et c'est ce qui le rend crédible", [
            ("bas", "Smaller Than", 1, 0, {}),
            ("haut", "Larger Than", 1, 4, {}),
        ]),
        (u"10 plugins sur 14. Les quatre autres, abandonnés en version 6 ou "
         u"7, feront échouer la migration", [
            ("et", "Gate And", 2, 0, {}),
            ("cu", "Cull Pattern", 3, 0, {}),
            ("nb", "List Length", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("mi", "bas", 0), ("v", "bas", 1),
           ("ma", "haut", 0), ("v", "haut", 1),
           ("bas", 1, "et", 0), ("haut", 1, "et", 1),
           ("mi", "cu", 0), ("et", "cu", 1),
           ("cu", "nb", 0), ("nb", "pan", 0), ("nb", "rep", 0)],
)


# ---------------------------------------------------------------------------
# RH-24 — les parois trop minces après mise à l'échelle
# ---------------------------------------------------------------------------
R["RH-24"] = dict(
    sujet=[
        ("e", "DATA:Number", 0, 0,
         {"nick": u"EPAISSEURS_EN_CENTIEMES", "data": _nombres(V.D_RH24)}),
        ("k", "SLIDER", 0, 4,
         {"slider": (0.1, 1, V.D_RH24_ECHELLE, 2), "nick": u"Facteur d'echelle"}),
        ("m", "SLIDER", 0, 5,
         {"slider": (0.2, 3, V.D_RH24_MINI, 2), "nick": u"Minimum machine"}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Les centièmes deviennent des millimètres, puis la réduction "
         u"s'applique. Juger AVANT la mise à l'échelle en trouverait cinq", [
            ("mm", "Division", 1, 0, {"val": [(1, "Number", [100])]}),
            ("re", "Multiplication", 2, 0, {}),
        ]),
        (u"12 parois passent sous le minimum. Sept franchissent le seuil "
         u"pendant la réduction — rien dans le modèle au 1/1 ne le laissait "
         u"voir", [
            ("st", "Smaller Than", 3, 0, {}),
            ("cu", "Cull Pattern", 4, 0, {}),
            ("nb", "List Length", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("e", "mm", 0), ("mm", "re", 0), ("k", "re", 1),
           ("re", "st", 0), ("m", "st", 1),
           ("e", "cu", 0), ("st", 0, "cu", 1),
           ("cu", "nb", 0), ("nb", "pan", 0), ("nb", "rep", 0)],
)


# ---------------------------------------------------------------------------
# RH-25 — les volumes réellement étanches
# ---------------------------------------------------------------------------
R["RH-25"] = dict(
    sujet=[
        ("nu", "DATA:Number", 0, 0,
         {"nick": u"ARETES_NUES", "data": _nombres([a for a, _b in V.D_RH25])}),
        ("nm", "DATA:Number", 0, 3,
         {"nick": u"ARETES_NON_MANIFOLD", "data": _nombres([b for _a, b in V.D_RH25])}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Les DEUX compteurs doivent être à zéro. Ne regarder que les "
         u"arêtes nues en déclarerait huit bonnes : deux polysurfaces "
         u"fermées portent des arêtes non-manifold, où trois faces partagent "
         u"la même arête", [
            ("z1", "Equality", 1, 0, {"val": [(1, "Number", [0])]}),
            ("z2", "Equality", 1, 3, {"val": [(1, "Number", [0])]}),
            ("et", "Gate And", 2, 0, {}),
        ]),
        (u"6 polysurfaces sur 12 sont réellement étanches", [
            ("cu", "Cull Pattern", 3, 0, {}),
            ("nb", "List Length", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("nu", "z1", 0), ("nm", "z2", 0),
           ("z1", 0, "et", 0), ("z2", 0, "et", 1),
           ("nu", "cu", 0), ("et", "cu", 1),
           ("cu", "nb", 0), ("nb", "pan", 0), ("nb", "rep", 0)],
)


# ---------------------------------------------------------------------------
# RH-26 — le poids du fichier à envoyer
# ---------------------------------------------------------------------------
R["RH-26"] = dict(
    sujet=[
        ("t", "SLIDER", 0, 0,
         {"slider": (1000, 500000, V.D_RH26_TRIANGLES, 0), "nick": u"Triangles"}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le STL binaire réserve cinquante octets par triangle, plus "
         u"quatre-vingt-quatre d'en-tête. Le même maillage en ASCII pèserait "
         u"environ cinq fois plus, et le format par défaut de la boîte de "
         u"dialogue n'est pas toujours le binaire", [
            ("m", "Multiplication", 1, 0, {"val": [(1, "Number", [50])]}),
            ("a", "Addition", 2, 0, {"val": [(1, "Number", [84])]}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("t", "m", 0), ("m", "a", 0), ("a", "pan", 0), ("a", "rep", 0)],
)


# ---------------------------------------------------------------------------
# RH-27 — le volume d'un assemblage de primitives
# ---------------------------------------------------------------------------
_D27 = V.D_RH27
R["RH-27"] = dict(
    sujet=[
        ("l", "SLIDER", 0, 0,
         {"slider": (50, 600, _D27["longueur"], 0), "nick": u"Longueur du socle"}),
        ("la", "SLIDER", 0, 1,
         {"slider": (50, 400, _D27["largeur"], 0), "nick": u"Largeur du socle"}),
        ("h", "SLIDER", 0, 2,
         {"slider": (10, 120, _D27["hauteur"], 0), "nick": u"Hauteur du socle"}),
        ("r", "SLIDER", 0, 3,
         {"slider": (10, 120, _D27["rayon"], 0), "nick": u"Rayon du fut"}),
        ("hc", "SLIDER", 0, 4,
         {"slider": (20, 300, _D27["hauteur_cyl"], 0), "nick": u"Hauteur du fut"}),
        ("en", "SLIDER", 0, 5,
         {"slider": (0, 40, _D27["enfoncement"], 0), "nick": u"Enfoncement"}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le socle, puis le fût entier", [
            ("s1", "Multiplication", 1, 0, {}),
            ("soc", "Multiplication", 2, 0, {}),
            ("r2", "Multiplication", 1, 3, {}),
            ("pi", "Pi", 1, 5, {"val": [(0, "Number", [1])]}),
            ("dis", "Multiplication", 2, 3, {}),
            ("fut", "Multiplication", 3, 3, {}),
        ]),
        (u"La partie encastrée appartient aux DEUX : elle est comptée deux "
         u"fois. Additionner sans la déduire donnerait 2,2994 dm³, 4 % de "
         u"trop — assez pour fausser un devis de fonderie", [
            ("com", "Multiplication", 3, 6, {}),
            ("som", "Addition", 4, 0, {}),
            ("net", "Subtraction", 5, 0, {}),
            ("dm3", "Division", 6, 0, {"val": [(1, "Number", [1e6])]}),
            ("pan", "PANEL", 7, 0, {}),
        ]),
    ],
    wires=[("l", "s1", 0), ("la", "s1", 1),
           ("s1", "soc", 0), ("h", "soc", 1),
           ("r", "r2", 0), ("r", "r2", 1),
           ("r2", "dis", 0), ("pi", "dis", 1),
           ("dis", "fut", 0), ("hc", "fut", 1),
           ("dis", "com", 0), ("en", "com", 1),
           ("soc", "som", 0), ("fut", "som", 1),
           ("som", "net", 0), ("com", "net", 1),
           ("net", "dm3", 0), ("dm3", "pan", 0), ("dm3", "rep", 0)],
)


# ---------------------------------------------------------------------------
# RH-28 — la surface d'une extrusion
# ---------------------------------------------------------------------------
R["RH-28"] = dict(
    sujet=[
        ("x", "DATA:Number", 0, 0,
         {"nick": u"SOMMETS_X", "data": _nombres([p[0] for p in V.D_RH28])}),
        ("y", "DATA:Number", 0, 3,
         {"nick": u"SOMMETS_Y", "data": _nombres([p[1] for p in V.D_RH28])}),
        ("h", "SLIDER", 0, 6,
         {"slider": (500, 6000, V.D_RH28_HAUTEUR, 0), "nick": u"Hauteur de bardage"}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Les cinq sommets, puis la polyligne REFERMÉE. La laisser ouverte "
         u"donnerait 12,1166 m² : le segment de fermeture mesure 1 400 mm, "
         u"soit un mur entier, et l'aperçu ne les distingue pas", [
            ("pt", "Construct Point", 1, 0, {}),
            ("pl", "PolyLine", 2, 0, {"val": [(1, "Boolean", [True])]}),
            ("lg", "Length", 3, 0, {}),
        ]),
        (u"15,7566 m² de bardage", [
            ("mm2", "Multiplication", 4, 0, {}),
            ("m2", "Division", 5, 0, {"val": [(1, "Number", [1e6])]}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("x", "pt", 0), ("y", "pt", 1),
           ("pt", "pl", 0), ("pl", "lg", 0),
           ("lg", "mm2", 0), ("h", "mm2", 1),
           ("mm2", "m2", 0), ("m2", "pan", 0), ("m2", "rep", 0)],
)


# ---------------------------------------------------------------------------
# RH-29 — la platine percée en réseau
# ---------------------------------------------------------------------------
_D29 = V.D_RH29
R["RH-29"] = dict(
    sujet=[
        ("l", "SLIDER", 0, 0,
         {"slider": (200, 2000, _D29["longueur"], 0), "nick": u"Longueur"}),
        ("la", "SLIDER", 0, 1,
         {"slider": (200, 2000, _D29["largeur"], 0), "nick": u"Largeur"}),
        ("ep", "SLIDER", 0, 2,
         {"slider": (2, 40, _D29["epaisseur"], 0), "nick": u"Epaisseur"}),
        ("nx", "SLIDER", 0, 3,
         {"slider": (1, 20, _D29["nx"], 0), "nick": u"Trous en X"}),
        ("ny", "SLIDER", 0, 4,
         {"slider": (1, 20, _D29["ny"], 0), "nick": u"Trous en Y"}),
        ("d", "SLIDER", 0, 5,
         {"slider": (4, 80, _D29["diametre"], 0), "nick": u"Diametre des trous"}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"La platine pleine", [
            ("a", "Multiplication", 1, 0, {}),
            ("vp", "Multiplication", 2, 0, {}),
        ]),
        (u"Le RAYON, pas le diamètre : l'aire va comme son carré. La "
         u"confusion quadruple le volume percé et allège la platine de 5 %", [
            ("r", "Division", 1, 3, {"val": [(1, "Number", [2])]}),
            ("r2", "Multiplication", 2, 3, {}),
            ("pi", "Pi", 2, 6, {"val": [(0, "Number", [1])]}),
            ("dis", "Multiplication", 3, 3, {}),
            ("un", "Multiplication", 4, 3, {}),
            ("n", "Multiplication", 3, 6, {}),
            ("vt", "Multiplication", 5, 3, {}),
        ]),
        (u"6,3705 dm³ de matière restante", [
            ("net", "Subtraction", 6, 0, {}),
            ("dm3", "Division", 7, 0, {"val": [(1, "Number", [1e6])]}),
            ("pan", "PANEL", 8, 0, {}),
        ]),
    ],
    wires=[("l", "a", 0), ("la", "a", 1), ("a", "vp", 0), ("ep", "vp", 1),
           ("d", "r", 0), ("r", "r2", 0), ("r", "r2", 1),
           ("r2", "dis", 0), ("pi", "dis", 1),
           ("dis", "un", 0), ("ep", "un", 1),
           ("nx", "n", 0), ("ny", "n", 1),
           ("un", "vt", 0), ("n", "vt", 1),
           ("vp", "net", 0), ("vt", "net", 1),
           ("net", "dm3", 0), ("dm3", "pan", 0), ("dm3", "rep", 0)],
)


# ---------------------------------------------------------------------------
# RH-30 — ce que le filtre de sélection retient
# ---------------------------------------------------------------------------
_TYPES = {u"Courbe": 1, u"Surface": 2, u"Bloc": 3, u"Maillage": 4}
_CALQ = {u"10-Porteurs": 1, u"11-Cloisons": 2, u"20-Menuiseries": 3}

R["RH-30"] = dict(
    sujet=[
        ("ty", "DATA:Number", 0, 0,
         {"nick": u"TYPE_1COURBE_2SURFACE_3BLOC_4MAILLAGE",
          "data": _nombres([_TYPES[t] for t, _c, _v in V.D_RH30])}),
        ("ca", "DATA:Number", 0, 4,
         {"nick": u"CALQUE_1PORTEURS_2CLOISONS_3MENUISERIES",
          "data": _nombres([_CALQ[c] for _t, c, _v in V.D_RH30])}),
        ("ve", "DATA:Number", 0, 8,
         {"nick": u"VERROUILLE", "data": _drapeaux([v for _t, _c, v in V.D_RH30])}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Trois conditions : le bon type, le bon calque, et NON verrouillé. "
         u"Oublier la troisième en trouverait cinq — deux courbes du bon "
         u"calque sont verrouillées et n'entreront jamais dans la sélection", [
            ("t1", "Equality", 1, 0, {"val": [(1, "Number", [1])]}),
            ("c1", "Equality", 1, 4, {"val": [(1, "Number", [1])]}),
            ("v0", "Equality", 1, 8, {"val": [(1, "Number", [0])]}),
            ("e1", "Gate And", 2, 0, {}),
            ("e2", "Gate And", 3, 0, {}),
        ]),
        (u"3 objets sont retenus", [
            ("cu", "Cull Pattern", 4, 0, {}),
            ("nb", "List Length", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("ty", "t1", 0), ("ca", "c1", 0), ("ve", "v0", 0),
           ("t1", 0, "e1", 0), ("c1", 0, "e1", 1),
           ("e1", "e2", 0), ("v0", 0, "e2", 1),
           ("ty", "cu", 0), ("e2", "cu", 1),
           ("cu", "nb", 0), ("nb", "pan", 0), ("nb", "rep", 0)],
)


# ---------------------------------------------------------------------------
# RH-31 — ce qui reste visible
# ---------------------------------------------------------------------------
R["RH-31"] = dict(
    sujet=[
        ("cv", "DATA:Number", 0, 0,
         {"nick": u"CALQUE_VISIBLE", "data": _drapeaux([c for _g, c, _m in V.D_RH31])}),
        ("ma", "DATA:Number", 0, 4,
         {"nick": u"OBJET_MASQUE", "data": _drapeaux([m for _g, _c, m in V.D_RH31])}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Deux mécanismes produisent le même symptôme. Ne regarder que le "
         u"masquage d'objet en compterait treize : trois objets non masqués "
         u"reposent sur un calque éteint, et « Montrer tout » ne les fera "
         u"pas revenir", [
            ("v1", "Equality", 1, 0, {"val": [(1, "Number", [1])]}),
            ("m0", "Equality", 1, 4, {"val": [(1, "Number", [0])]}),
            ("et", "Gate And", 2, 0, {}),
        ]),
        (u"10 objets sont réellement visibles", [
            ("cu", "Cull Pattern", 3, 0, {}),
            ("nb", "List Length", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("cv", "v1", 0), ("ma", "m0", 0),
           ("v1", 0, "et", 0), ("m0", 0, "et", 1),
           ("cv", "cu", 0), ("et", "cu", 1),
           ("cu", "nb", 0), ("nb", "pan", 0), ("nb", "rep", 0)],
)


# ---------------------------------------------------------------------------
# RH-32 — ce qui suivra le calque
# ---------------------------------------------------------------------------
_COUL = {u"ParCalque": 0, u"Rouge": 1, u"Bleu": 2, u"Vert": 3, u"Jaune": 4}

R["RH-32"] = dict(
    sujet=[
        ("c", "DATA:Number", 0, 0,
         {"nick": u"COULEUR_0PARCALQUE_SINON_PROPRE",
          "data": _nombres([_COUL[x] for x in V.D_RH32])}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Suivront le calque : ceux dont la couleur est HÉRITÉE. Compter "
         u"les couleurs propres — sept — répond à la question inverse, et "
         u"les deux comptes se complètent à vingt", [
            ("z", "Equality", 1, 0, {"val": [(1, "Number", [0])]}),
            ("cu", "Cull Pattern", 2, 0, {}),
            ("nb", "List Length", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("c", "z", 0),
           ("c", "cu", 0), ("z", 0, "cu", 1),
           ("cu", "nb", 0), ("nb", "pan", 0), ("nb", "rep", 0)],
)


# ---------------------------------------------------------------------------
# GP-13 — la pièce qui enchaîne trois opérations
# ---------------------------------------------------------------------------
_D13 = V.D_GP13
R["GP-13"] = dict(
    sujet=[
        ("l", "SLIDER", 0, 0,
         {"slider": (100, 900, _D13["longueur"], 0), "nick": u"Longueur"}),
        ("la", "SLIDER", 0, 1,
         {"slider": (100, 600, _D13["largeur"], 0), "nick": u"Largeur"}),
        ("rc", "SLIDER", 0, 2,
         {"slider": (5, 80, _D13["conge"], 0), "nick": u"Rayon de conge"}),
        ("dp", "SLIDER", 0, 3,
         {"slider": (5, 60, _D13["percage"], 0), "nick": u"Diametre de percage"}),
        ("np", "SLIDER", 0, 4,
         {"slider": (0, 20, _D13["percements"], 0), "nick": u"Percements"}),
        ("ep", "SLIDER", 0, 5,
         {"slider": (2, 60, _D13["epaisseur"], 0), "nick": u"Epaisseur"}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le rectangle plein", [
            ("rect", "Multiplication", 1, 0, {}),
        ]),
        (u"Un congé de rayon r retire à chaque angle la différence entre le "
         u"carré de côté r et le quart de disque : (4 − π) r² pour les "
         u"quatre. Les oublier ne coûte qu'un demi-pour-cent — c'est "
         u"précisément pourquoi on ne le voit pas", [
            ("pi", "Pi", 1, 3, {"val": [(0, "Number", [1])]}),
            ("k", "Subtraction", 2, 3, {"val": [(0, "Number", [4])]}),
            ("rc2", "Multiplication", 1, 5, {}),
            ("cg", "Multiplication", 3, 3, {}),
        ]),
        (u"Puis les sept perçages", [
            ("r", "Division", 1, 7, {"val": [(1, "Number", [2])]}),
            ("r2", "Multiplication", 2, 7, {}),
            ("un", "Multiplication", 3, 7, {}),
            ("tp", "Multiplication", 4, 7, {}),
        ]),
        (u"1,8798 dm³", [
            ("a1", "Subtraction", 5, 0, {}),
            ("a2", "Subtraction", 6, 0, {}),
            ("vol", "Multiplication", 7, 0, {}),
            ("dm3", "Division", 8, 0, {"val": [(1, "Number", [1e6])]}),
            ("pan", "PANEL", 8, 4, {}),
        ]),
    ],
    wires=[("l", "rect", 0), ("la", "rect", 1),
           ("pi", "k", 1),
           ("rc", "rc2", 0), ("rc", "rc2", 1),
           ("k", "cg", 0), ("rc2", "cg", 1),
           ("dp", "r", 0), ("r", "r2", 0), ("r", "r2", 1),
           ("r2", "un", 0), ("pi", "un", 1),
           ("un", "tp", 0), ("np", "tp", 1),
           ("rect", "a1", 0), ("cg", "a1", 1),
           ("a1", "a2", 0), ("tp", "a2", 1),
           ("a2", "vol", 0), ("ep", "vol", 1),
           ("vol", "dm3", 0), ("dm3", "pan", 0), ("dm3", "rep", 0)],
)


# ---------------------------------------------------------------------------
# WB-10 — ce qu'un format d'échange laisse en route
# ---------------------------------------------------------------------------
_FORMATS = [u"3DM", u"STEP", u"DWG", u"OBJ", u"STL"]


def _colonne(fmt):
    return _drapeaux([fmt in formats for _a, formats in V.D_WB10])


R["WB-10"] = dict(
    sujet=[("f%d" % i, "DATA:Number", 0, i * 2,
            {"nick": u"PORTE_PAR_%s" % f, "data": _colonne(f)})
           for i, f in enumerate(_FORMATS)]
          + [("rep", "REPONSE", 5, 0, {"type": "Number"})],
    corrige=[
        (u"La colonne STEP, et ce qu'elle NE porte pas. Compter ce qu'elle "
         u"conserve — trois — répond à la question inverse : c'est la perte "
         u"qui décide, et un modèle exporté en STEP arrive sans matériaux, "
         u"sans blocs, sans historique, sans couleurs d'objet et sans "
         u"maillages", [
            ("z", "Equality", 1, 0, {"val": [(1, "Number", [0])]}),
            ("cu", "Cull Pattern", 2, 0, {}),
            ("nb", "List Length", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("f1", "z", 0),
           ("f1", "cu", 0), ("z", 0, "cu", 1),
           ("cu", "nb", 0), ("nb", "pan", 0), ("nb", "rep", 0)],
)


# ---------------------------------------------------------------------------
# WB-11 — le temps de calcul, une fois en ligne
# ---------------------------------------------------------------------------
R["WB-11"] = dict(
    sujet=[
        ("ms", "DATA:Number", 0, 0,
         {"nick": u"TEMPS_LOCAL_MS", "data": _nombres(V.D_WB11)}),
        ("k", "SLIDER", 0, 4,
         {"slider": (1, 5, V.D_WB11_FACTEUR, 1), "nick": u"Facteur serveur"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le total local passe sous la limite de vingt secondes : 10,489 s. "
         u"C'est le facteur serveur qui décide, et le profilage local donne "
         u"toujours le résultat rassurant", [
            ("so", "Mass Addition", 1, 0, {}),
            ("en", "Multiplication", 2, 0, {}),
            ("s", "Division", 3, 0, {"val": [(1, "Number", [1000])]}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("ms", "so", 0),
           ("so", "en", 0), ("k", "en", 1),
           ("en", "s", 0), ("s", "pan", 0), ("s", "rep", 0)],
)


# ---------------------------------------------------------------------------
# IA-26 — transposer, et le prouver sur un second jeu
# ---------------------------------------------------------------------------
R["IA-26"] = dict(
    sujet=[
        ("v", "DATA:Number", 0, 0,
         {"nick": u"JEU_DE_PREUVE", "data": _nombres(V.D_IA26)}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"`Mass Addition` rend aussi ses résultats PARTIELS : ce sont les "
         u"sommes cumulées. Le cumul est strictement croissant — un décalage "
         u"d'un rang se voit, une somme oubliée décale tout ce qui suit, et "
         u"c'est ce qui rend la comparaison sévère", [
            ("so", "Mass Addition", 1, 0, {}),
            ("pan", "PANEL", 2, 0, {}),
        ]),
    ],
    wires=[("v", "so", 0), ("so", 1, "pan", 0), ("so", 1, "rep", 0)],
)


# ---------------------------------------------------------------------------
# IA-27 — le script qui tourne et compte mal
# ---------------------------------------------------------------------------
R["IA-27"] = dict(
    sujet=[
        ("v", "DATA:Number", 0, 0,
         {"nick": u"LONGUEURS_RELEVEES", "data": _nombres(V.D_IA27)}),
        ("s", "SLIDER", 0, 4,
         {"slider": (100, 4000, V.D_IA27_SEUIL, 0), "nick": u"Seuil"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le comptage natif teste TOUTES les valeurs. La boucle fautive "
         u"s'arrête un cran trop tôt et ne voit jamais la dernière — qui "
         u"vaut 2 592 mm et dépasse largement", [
            ("gt", "Larger Than", 1, 0, {}),
            ("cu", "Cull Pattern", 2, 0, {}),
        ]),
        (u"15 longueurs dépassent le seuil, et non quatorze", [
            ("nb", "List Length", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("v", "gt", 0), ("s", "gt", 1),
           ("v", "cu", 0), ("gt", 0, "cu", 1),
           ("cu", "nb", 0), ("nb", "pan", 0), ("nb", "rep", 0)],
)


# ---------------------------------------------------------------------------
# IA-28 — regrouper des pièces par similarité
# ---------------------------------------------------------------------------
R["IA-28"] = dict(
    sujet=[
        ("lg", "DATA:Number", 0, 0,
         {"nick": u"LONGUEURS", "data": _nombres([a for a, _b in V.D_IA28])}),
        ("ep", "DATA:Number", 0, 4,
         {"nick": u"EPAISSEURS", "data": _nombres([b for _a, b in V.D_IA28])}),
        ("sl", "SLIDER", 0, 8,
         {"slider": (100, 2000, V.D_IA28_SEUILS[0], 0), "nick": u"Seuil de longueur"}),
        ("se", "SLIDER", 0, 9,
         {"slider": (5, 80, V.D_IA28_SEUILS[1], 0), "nick": u"Seuil d'epaisseur"}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Chaque pièce est jugée sur les DEUX critères. La longueur seule "
         u"donnerait deux groupes de dix ; c'est le croisement qui produit "
         u"quatre familles", [
            ("a", "Larger Than", 1, 0, {}),
            ("b", "Larger Than", 1, 4, {}),
            ("na", "Gate Not", 2, 2, {}),
            ("nb", "Gate Not", 2, 6, {}),
        ]),
        (u"Les quatre familles : longue et épaisse, longue et mince, courte "
         u"et épaisse, courte et mince", [
            ("f1", "Gate And", 3, 0, {}),
            ("f2", "Gate And", 3, 2, {}),
            ("f3", "Gate And", 3, 4, {}),
            ("f4", "Gate And", 3, 6, {}),
            ("c1", "Cull Pattern", 4, 0, {}),
            ("c2", "Cull Pattern", 4, 2, {}),
            ("c3", "Cull Pattern", 4, 4, {}),
            ("c4", "Cull Pattern", 4, 6, {}),
            ("n1", "List Length", 5, 0, {}),
            ("n2", "List Length", 5, 2, {}),
            ("n3", "List Length", 5, 4, {}),
            ("n4", "List Length", 5, 6, {}),
        ]),
        (u"10 pièces dans la plus fournie — la moitié du lot", [
            ("m1", "Merge", 6, 0, {}),
            ("m2", "Merge", 6, 4, {}),
            ("m3", "Merge", 7, 0, {}),
            ("bo", "Bounds", 7, 4, {}),
            ("dd", "Deconstruct Domain", 8, 0, {}),
            ("pan", "PANEL", 8, 4, {}),
        ]),
    ],
    wires=[("lg", "a", 0), ("sl", "a", 1),
           ("ep", "b", 0), ("se", "b", 1),
           ("a", 0, "na", 0), ("b", 0, "nb", 0),
           ("a", 0, "f1", 0), ("b", 0, "f1", 1),
           ("a", 0, "f2", 0), ("nb", "f2", 1),
           ("na", "f3", 0), ("b", 0, "f3", 1),
           ("na", "f4", 0), ("nb", "f4", 1),
           ("lg", "c1", 0), ("f1", "c1", 1),
           ("lg", "c2", 0), ("f2", "c2", 1),
           ("lg", "c3", 0), ("f3", "c3", 1),
           ("lg", "c4", 0), ("f4", "c4", 1),
           ("c1", "n1", 0), ("c2", "n2", 0), ("c3", "n3", 0), ("c4", "n4", 0),
           ("n1", "m1", 0), ("n2", "m1", 1),
           ("n3", "m2", 0), ("n4", "m2", 1),
           ("m1", "m3", 0), ("m2", "m3", 1),
           ("m3", "bo", 0), ("bo", "dd", 0),
           ("dd", 1, "pan", 0), ("dd", 1, "rep", 0)],
)


# ---------------------------------------------------------------------------
# IA-29 — les GUID qui cassent les définitions
# ---------------------------------------------------------------------------
R["IA-29"] = dict(
    sujet=[
        ("g", "DATA:Number", 0, 0,
         {"nick": u"GUID_CONSERVE", "data": _drapeaux([g for _c, g, _n in V.D_IA29])}),
        ("n", "DATA:Number", 0, 3,
         {"nick": u"DEFINITIONS_QUI_L_EMPLOIENT",
          "data": _nombres([n for _c, _g, n in V.D_IA29])}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Compter les COMPOSANTS régénérés en donnerait quatre. Un "
         u"composant casse autant de définitions qu'il en sert : le "
         u"préjudice se mesure chez les utilisateurs, pas dans le code", [
            ("z", "Equality", 1, 0, {"val": [(1, "Number", [0])]}),
            ("cu", "Cull Pattern", 2, 0, {}),
        ]),
        (u"16 définitions cassées", [
            ("so", "Mass Addition", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("g", "z", 0),
           ("n", "cu", 0), ("z", 0, "cu", 1),
           ("cu", "so", 0), ("so", "pan", 0), ("so", "rep", 0)],
)


# ---------------------------------------------------------------------------
# IA-30 — ce qu'un appel coûte
# ---------------------------------------------------------------------------
_D30 = V.D_IA30
R["IA-30"] = dict(
    sujet=[
        ("a", "SLIDER", 0, 0,
         {"slider": (1, 10, _D30["appels_par_recalcul"], 0),
          "nick": u"Appels par recalcul"}),
        ("r", "SLIDER", 0, 1,
         {"slider": (10, 1000, _D30["recalculs"], 0), "nick": u"Recalculs"}),
        ("p", "SLIDER", 0, 2,
         {"slider": (0.001, 0.05, _D30["prix"], 3), "nick": u"Prix par appel"}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Trois appels par recalcul, pas un. Compter un seul appel donnerait "
         u"0,96 € — trois fois moins, et c'est le genre de multiplication "
         u"qu'on ne découvre qu'à la facture", [
            ("n", "Multiplication", 1, 0, {}),
            ("c", "Multiplication", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("a", "n", 0), ("r", "n", 1),
           ("n", "c", 0), ("p", "c", 1),
           ("c", "pan", 0), ("c", "rep", 0)],
)


# ---------------------------------------------------------------------------
# IA-31 — ce que l'agent a modifié
# ---------------------------------------------------------------------------
_VERBES = {u"lire": 1, u"ajouter": 2, u"supprimer": 3, u"cabler": 4,
           u"deplacer": 5, u"renommer": 6}

R["IA-31"] = dict(
    sujet=[
        ("j", "DATA:Number", 0, 0,
         {"nick": u"JOURNAL_1LIRE_2AJOUTER_3SUPPRIMER_4CABLER_5DEPLACER_6RENOMMER",
          "data": _nombres([_VERBES[a] for a in V.D_IA31])}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Seule la lecture porte le code 1 : tout le reste écrit. Ne "
         u"compter que les ajouts et les suppressions en trouverait cinq — "
         u"câbler, déplacer et renommer modifient le document tout autant, "
         u"et un fil rebranché change le résultat sans que rien "
         u"n'apparaisse ni ne disparaisse", [
            ("gt", "Larger Than", 1, 0, {"val": [(1, "Number", [1])]}),
            ("cu", "Cull Pattern", 2, 0, {}),
        ]),
        (u"10 opérations ont modifié le document", [
            ("nb", "List Length", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("j", "gt", 0),
           ("j", "cu", 0), ("gt", 0, "cu", 1),
           ("cu", "nb", 0), ("nb", "pan", 0), ("nb", "rep", 0)],
)


# ---------------------------------------------------------------------------
# IA-32 — ce qu'une demande floue laisse passer
# ---------------------------------------------------------------------------
R["IA-32"] = dict(
    sujet=[
        ("v", "DATA:Number", 0, 0,
         {"nick": u"RELEVES", "data": _nombres(V.D_IA32)}),
        ("s", "SLIDER", 0, 4,
         {"slider": (100, 900, V.D_IA32_SEUIL, 0), "nick": u"Seuil"}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Un relevé vaut EXACTEMENT 500 : c'est lui qui sépare la "
         u"comparaison stricte de la comparaison large, et c'est le cas "
         u"limite qu'une spécification doit nommer", [
            ("st", "Larger Than", 1, 0, {}),
            ("c1", "Cull Pattern", 2, 0, {}),
            ("n1", "List Length", 3, 0, {}),
            ("c2", "Cull Pattern", 2, 3, {}),
            ("n2", "List Length", 3, 3, {}),
        ]),
        (u"La moyenne, 472,81, et la médiane, 491,50, encadrent le seuil "
         u"sans coïncider avec lui : aucune des quatre lectures n'est plus "
         u"légitime que les autres", [
            ("mo", "Average", 1, 6, {}),
            ("gm", "Larger Than", 2, 6, {}),
            ("c3", "Cull Pattern", 3, 6, {}),
            ("n3", "List Length", 4, 6, {}),
            ("tri", "Sort List", 1, 9, {}),
            ("me", "List Item", 2, 9,
             {"val": [(1, "Integer", [len(V.D_IA32) // 2])]}),
            ("mp", "List Item", 2, 11,
             {"val": [(1, "Integer", [len(V.D_IA32) // 2 - 1])]}),
            ("sm", "Addition", 3, 9, {}),
            ("md", "Division", 4, 9, {"val": [(1, "Number", [2])]}),
            ("gd", "Larger Than", 5, 9, {}),
            ("c4", "Cull Pattern", 6, 9, {}),
            ("n4", "List Length", 7, 9, {}),
        ]),
        (u"Les quatre comptes : 7, 8, 9, 8", [
            ("m1", "Merge", 5, 0, {}),
            ("m2", "Merge", 6, 0, {}),
            ("m3", "Merge", 8, 0, {}),
            ("pan", "PANEL", 8, 4, {}),
        ]),
    ],
    wires=[("v", "st", 0), ("s", "st", 1),
           ("v", "c1", 0), ("st", 0, "c1", 1), ("c1", "n1", 0),
           ("v", "c2", 0), ("st", 1, "c2", 1), ("c2", "n2", 0),
           ("v", "mo", 0),
           ("v", "gm", 0), ("mo", "gm", 1),
           ("v", "c3", 0), ("gm", 0, "c3", 1), ("c3", "n3", 0),
           ("v", "tri", 0), ("tri", "me", 0), ("tri", "mp", 0),
           ("me", "sm", 0), ("mp", "sm", 1), ("sm", "md", 0),
           ("v", "gd", 0), ("md", "gd", 1),
           ("v", "c4", 0), ("gd", 0, "c4", 1), ("c4", "n4", 0),
           ("n1", "m1", 0), ("n2", "m1", 1),
           ("m1", "m2", 0), ("n3", "m2", 1),
           ("m2", "m3", 0), ("n4", "m3", 1),
           ("m3", "pan", 0), ("m3", "rep", 0)],
)


# ---------------------------------------------------------------------------
# IA-33 — du texte aux paramètres
# ---------------------------------------------------------------------------
_D33 = V.D_IA33
R["IA-33"] = dict(
    sujet=[
        ("l", "SLIDER", 0, 0,
         {"slider": (500, 8000, _D33["largeur"], 0), "nick": u"Largeur de verriere"}),
        ("h", "SLIDER", 0, 1,
         {"slider": (500, 6000, _D33["hauteur"], 0), "nick": u"Hauteur de verriere"}),
        ("t", "SLIDER", 0, 2,
         {"slider": (1, 20, _D33["travees"], 0), "nick": u"Travees"}),
        ("m", "SLIDER", 0, 3,
         {"slider": (10, 200, _D33["montant"], 0), "nick": u"Largeur de montant"}),
        ("i", "SLIDER", 0, 4,
         {"slider": (0, 1000, _D33["imposte"], 0), "nick": u"Imposte"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Six travées, CINQ montants — un de moins, comme les barreaux de "
         u"garde-corps en B-02. Diviser la largeur par six sans les déduire "
         u"donnerait 533,33 mm, et la verrière déborderait de 300 mm au "
         u"montage", [
            ("nm", "Subtraction", 1, 0, {"val": [(1, "Number", [1])]}),
            ("tot", "Multiplication", 2, 0, {}),
            ("net", "Subtraction", 3, 0, {}),
            ("lt", "Division", 4, 0, {}),
        ]),
        (u"483,3333 mm de travée, puis 2 070 mm de hauteur vitrée", [
            ("hv", "Subtraction", 4, 4, {}),
            ("me", "Merge", 6, 0, {}),
            ("pan", "PANEL", 7, 0, {}),
        ]),
    ],
    wires=[("t", "nm", 0),
           ("nm", "tot", 0), ("m", "tot", 1),
           ("l", "net", 0), ("tot", "net", 1),
           ("net", "lt", 0), ("t", "lt", 1),
           ("h", "hv", 0), ("i", "hv", 1),
           ("lt", "me", 0), ("hv", "me", 1),
           ("me", "pan", 0), ("me", "rep", 0)],
)
