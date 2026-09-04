# -*- coding: utf-8 -*-
"""Recettes de construction de la vague 3.

Memes conventions et memes deux formes de corrige que la vague 2 — la CHAINE
quand elle mene naturellement au resultat, l'ETALON quand elle serait une
contorsion. Les helpers `_compte` et `_etalon` sont ceux de `recipes_vague2` :
les redefinir ici aurait invite a en corriger un seul le jour ou l'on corrige
l'autre.
"""
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

import exercices_vague3 as V3
import exercices_vague3_avance as V3A
from recipes_nouveaux import charniere as recette_charniere
from recipes_vague2 import _compte, _etalon

R = {}


def _e(eid):
    for lot in (V3.LOT_RH, V3.LOT_A, V3.LOT_GP, V3.LOT_MP,
                V3A.LOT_AV, V3A.LOT_WB, V3A.LOT_FA):
        for x in lot:
            if x["id"] == eid:
                return x
    return None


# ---------------------------------------------------------------------------
# RH-23, A-50 — deux etalons : ce qui a ete retenu, et pourquoi
# ---------------------------------------------------------------------------

_CAL, _TYP = V3.D_RH23_CIBLE

R["RH-23"] = _etalon(
    u"OBJETS_RETENUS",
    [u"%s / %s" % (c, t) for c, t in V3.D_RH23_OBJETS
     if c == _CAL and t == _TYP],
    "Text",
    u"L'étalon porte les objets qui satisfont les DEUX conditions : le calque "
    u"des porteurs ET le type courbe. Onze objets sont sur ce calque, onze "
    u"sont des courbes — les deux comptes partiels sont égaux, à dessein",
    u"Six objets seulement vérifient les deux ensemble. Un apprenant qui n'en "
    u"vérifie qu'une obtient onze des deux côtés et n'a aucune raison de se "
    u"méfier")

R["A-50"] = dict(
    sujet=[
        ("brut", "DATA:Text", 0, 0,
         {"nick": u"LIBELLES_SAISIS", "data": list(V3.D_A50_LIBELLES)}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Retirer les espaces de bord — et EUX SEULS. Retirer tous les "
         u"espaces ferait perdre son sens à un libellé composé", [
            # « Text Trim », et non « Trim » : le composant natif de coupe
            # des espaces de bord porte le prefixe de sa famille.
            ("trim", "Text Trim", 1, 0, {}),
        ]),
        (u"Uniformiser la casse : « MEL-19 » et « mel-19 » désignent la même "
         u"référence, et ne se regroupent pas tant qu'elles ne s'écrivent "
         u"pas pareil", [
            # « Text Case » rend DEUX sorties, majuscules et minuscules :
            # on prend la premiere.
            ("maj", "Text Case", 2, 0, {}),
        ]),
        (u"Six références distinctes. Regrouper sans nettoyer en donnerait "
         u"dix-sept : le fournisseur recevrait dix-sept lignes pour six "
         u"produits, et le rapprochement de facture échouerait sans que rien "
         u"ne soit signalé", [
            ("set", "Create Set", 3, 0, {}),
            ("ll", "List Length", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("brut", "trim", 0), ("trim", "maj", 0), ("maj", 0, "set", 0),
           ("set", "ll", 0), ("ll", "pan", 0), ("ll", "rep", 0)],
)


# ---------------------------------------------------------------------------
# A-51 — le tri depend du type
# ---------------------------------------------------------------------------

R["A-51"] = dict(
    sujet=[
        ("rep_", "DATA:Text", 0, 0,
         {"nick": u"REPERES_EN_TEXTE", "data": list(V3.D_A51_REPERES)}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Trier les repères TELS QU'ILS SONT : du texte. La comparaison se "
         u"fait caractère par caractère, et « 1 » vient avant « 2 »", [
            # « Sort Text » et non « Sort List » : c'est lui qui compare
            # caractere par caractere, et c'est tout le sujet.
            ("tri", "Sort Text", 1, 0, {}),
        ]),
        (u"Le premier de ce tri est 10 — pas 2. Sur un bon de débit, les "
         u"pièces sortent alors dans un ordre qui n'est celui de personne. "
         u"Le remède se pose en amont, à la lecture du tableur : convertir "
         u"avant de trier", [
            ("prem", "List Item", 2, 0, {"val": [(1, "Integer", [0])]}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
        (u"À titre de comparaison, le tri des mêmes valeurs converties en "
         u"nombres commence par 2 et finit par 100 ; le tri de texte "
         u"commence par 10 et finit par 9", [
            ("note", "PANEL", 3, 2,
             {"text": u"texte  : 10 100 12 15 2 21 3 30 5 7 8 9\n"
                      u"nombre :  2 3 5 7 8 9 10 12 15 21 30 100",
              "h": 60, "w": 300}),
        ]),
    ],
    wires=[("rep_", "tri", 0), ("rep_", "tri", 1),
           ("tri", 0, "prem", 0),
           ("prem", "pan", 0), ("prem", "rep", 0)],
)


# ---------------------------------------------------------------------------
# Lot GP
# ---------------------------------------------------------------------------

_G9 = V3.D_GP09

R["GP-09"] = dict(
    sujet=[
        ("b", "SLIDER", 0, 0,
         {"slider": (500, 5000, _G9["base"], 0), "nick": u"Base"}),
        ("h", "SLIDER", 0, 1,
         {"slider": (200, 3000, _G9["hauteur"], 0), "nick": u"Hauteur"}),
        ("a", "SLIDER", 0, 2,
         {"slider": (10, 89, _G9["angle"], 0), "nick": u"Angle du fuyant"}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'angle est donné en degrés ; les fonctions trigonométriques "
         u"attendent des radians", [
            ("rad", "Radians", 1, 0, {}),
        ]),
        (u"Ce qu'on cherche est le RECUL horizontal du fuyant, pas sa "
         u"longueur : hauteur divisée par la tangente de l'angle, soit "
         u"727 mm. La longueur du fuyant vaut 1 941 mm — du même ordre que "
         u"les cotes du meuble, donc tout aussi crédible", [
            ("tan", "Tangent", 2, 0, {}),
            ("recul", "Division", 3, 0, {}),
        ]),
        (u"1 672,75 mm. Retrancher le fuyant au lieu de son recul donnerait "
         u"459 mm : positif, plausible sur un plan, et 1,2 m trop court à "
         u"l'atelier", [
            ("petite", "Subtraction", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("a", "rad", 0), ("rad", "tan", 0),
           ("h", "recul", 0), ("tan", "recul", 1),
           ("b", "petite", 0), ("recul", "petite", 1),
           ("petite", "pan", 0), ("petite", "rep", 0)],
)

_G11 = V3.D_GP11

R["GP-11"] = dict(
    sujet=[
        ("l", "SLIDER", 0, 0,
         {"slider": (200, 4000, _G11["longueur"], 0), "nick": u"Longueur"}),
        ("h", "SLIDER", 0, 1,
         {"slider": (200, 4000, _G11["hauteur"], 0), "nick": u"Hauteur"}),
        ("r", "SLIDER", 0, 2,
         {"slider": (0, 400, _G11["rayon"], 0), "nick": u"Rayon de conge"}),
        ("o", "SLIDER", 0, 3,
         {"slider": (0, 200, _G11["decalage"], 0), "nick": u"Decalage"}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Congé PUIS décalage : les parties droites sont amputées du rayon "
         u"aux quatre coins, et les congés, décalés vers l'extérieur, "
         u"deviennent des arcs de rayon + décalage", [
            ("r2", "Multiplication", 1, 0, {"val": [(1, "Number", [2])]}),
            ("dl", "Subtraction", 2, 0, {}),
            ("dh", "Subtraction", 2, 2, {}),
            ("droits1", "Addition", 3, 0, {}),
            ("d1", "Multiplication", 4, 0, {"val": [(1, "Number", [2])]}),
            ("ro", "Addition", 3, 4, {}),
            ("arcs1", "Pi", 4, 4, {"val": [(0, "Number", [2])]}),
            ("m1", "Multiplication", 5, 4, {}),
            ("p1", "Addition", 6, 0, {}),
        ]),
        (u"Décalage PUIS congé : le contour grandit de deux décalages dans "
         u"chaque dimension, et les congés gardent leur rayon d'origine", [
            ("o2", "Multiplication", 1, 6, {"val": [(1, "Number", [2])]}),
            ("gl", "Addition", 2, 6, {}),
            ("gh", "Addition", 2, 8, {}),
            ("dl2", "Subtraction", 3, 6, {}),
            ("dh2", "Subtraction", 3, 8, {}),
            ("droits2", "Addition", 4, 6, {}),
            ("d2", "Multiplication", 5, 6, {"val": [(1, "Number", [2])]}),
            ("arcs2", "Pi", 5, 8, {"val": [(0, "Number", [2])]}),
            ("m2", "Multiplication", 6, 8, {}),
            ("p2", "Addition", 7, 6, {}),
        ]),
        (u"68,67 mm d'écart sur 5 445 mm de périmètre, soit 1,3 % : trop peu "
         u"pour se voir à l'écran, assez pour que deux ateliers travaillant "
         u"chacun dans son ordre livrent des pièces qui ne s'assemblent pas", [
            ("dif", "Subtraction", 8, 0, {}),
            ("abs", "Absolute", 9, 3, {}),
            ("pan", "PANEL", 10, 0, {}),
        ]),
    ],
    wires=[("r", "r2", 0),
           ("l", "dl", 0), ("r2", "dl", 1),
           ("h", "dh", 0), ("r2", "dh", 1),
           ("dl", "droits1", 0), ("dh", "droits1", 1),
           ("droits1", "d1", 0),
           ("r", "ro", 0), ("o", "ro", 1),
           ("arcs1", "m1", 0), ("ro", "m1", 1),
           ("d1", "p1", 0), ("m1", "p1", 1),

           ("o", "o2", 0),
           ("l", "gl", 0), ("o2", "gl", 1),
           ("h", "gh", 0), ("o2", "gh", 1),
           ("gl", "dl2", 0), ("r2", "dl2", 1),
           ("gh", "dh2", 0), ("r2", "dh2", 1),
           ("dl2", "droits2", 0), ("dh2", "droits2", 1),
           ("droits2", "d2", 0),
           ("arcs2", "m2", 0), ("r", "m2", 1),
           ("d2", "p2", 0), ("m2", "p2", 1),

           ("p1", "dif", 0), ("p2", "dif", 1),
           ("dif", "abs", 0),
           ("abs", "pan", 0), ("abs", "rep", 0)],
)

_G12 = V3.D_GP12

R["GP-12"] = dict(
    sujet=[
        ("v", "DATA:Vector", 0, 0,
         {"nick": u"POSITION_DU_POINT",
          "data": [(_G12["point"][0], _G12["point"][1], 0.0)]}),
        ("t", "DATA:Vector", 0, 2,
         {"nick": u"TRANSLATION",
          "data": [(_G12["translation"][0], _G12["translation"][1], 0.0)]}),
        ("a", "SLIDER", 0, 4,
         {"slider": (0, 180, _G12["angle"], 0), "nick": u"Angle de rotation"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'axe de rotation est la verticale passant par l'origine, et "
         u"l'angle se donne en radians", [
            ("z", "Unit Z", 1, 0, {"val": [(0, "Number", [1])]}),
            ("rad", "Radians", 1, 2, {}),
        ]),
        (u"Premier ordre : tourner, puis déplacer. La rotation ne voit pas "
         u"encore la translation", [
            ("rot1", "Rotate", 2, 0, {}),
            ("som1", "Addition", 3, 0, {}),
        ]),
        (u"Second ordre : déplacer, puis tourner. La rotation autour de "
         u"l'ORIGINE emporte alors la translation déjà faite — c'est là que "
         u"les deux ordres divergent", [
            ("som2", "Addition", 2, 4, {}),
            ("rot2", "Rotate", 3, 4, {}),
        ]),
        (u"513,85 mm séparent les deux résultats. Sur un bras de 1,2 m, "
         u"c'est un point d'ancrage qui tombe à côté du poteau — et aucun "
         u"des deux aperçus ne paraît faux", [
            ("dif", "Subtraction", 4, 0, {}),
            ("d", "Vector Length", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("a", "rad", 0),
           ("v", "rot1", 0), ("z", "rot1", 1), ("rad", "rot1", 2),
           ("rot1", "som1", 0), ("t", "som1", 1),
           ("v", "som2", 0), ("t", "som2", 1),
           ("som2", "rot2", 0), ("z", "rot2", 1), ("rad", "rot2", 2),
           ("som1", "dif", 0), ("rot2", "dif", 1),
           ("dif", "d", 0),
           ("d", "pan", 0), ("d", "rep", 0)],
)


# ---------------------------------------------------------------------------
# Lot MP
# ---------------------------------------------------------------------------

R["MP-05"] = dict(
    sujet=[
        ("t", "DATA:Number", 0, 0,
         {"nick": u"TEMPS_PAR_COMPOSANT",
          "data": [x for _n, x in V3.D_MP05_TEMPS]}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le temps total : 7 900 ms", [
            ("tot", "Mass Addition", 1, 0, {}),
        ]),
        (u"Le plus lourd : 4 820 ms pour le maillage adaptatif. Les neuf "
         u"plus légers cumulés pèsent moins d'un quart de lui seul", [
            ("bor", "Bounds", 1, 3, {}),
            ("dd", "Deconstruct Domain", 2, 3, {}),
        ]),
        (u"61 % du temps tient dans un seul composant. Le diviser par dix "
         u"ferait gagner 55 % ; annuler complètement les onze autres n'en "
         u"ferait gagner que 39. C'est ce que le relevé dit et que "
         u"l'intuition ne dit pas", [
            ("part", "Division", 3, 0, {}),
            ("cent", "Multiplication", 4, 0, {"val": [(1, "Number", [100])]}),
            ("rd", "Round", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("t", "tot", 0), ("t", "bor", 0), ("bor", "dd", 0),
           ("dd", 1, "part", 0), ("tot", "part", 1),
           ("part", "cent", 0), ("cent", "rd", 0),
           ("rd", "pan", 0), ("rd", "rep", 0)],
)


# ---------------------------------------------------------------------------
# Lot AV
# ---------------------------------------------------------------------------

_A4 = V3.D_AV04

R["AV-04"] = dict(
    sujet=[
        ("d", "SLIDER", 0, 0,
         {"slider": (10, 200, _A4["depart"], 0), "nick": u"Tassement initial"}),
        ("f", "SLIDER", 0, 1,
         {"slider": (0.5, 0.99, _A4["facteur"], 2), "nick": u"Facteur par passe"}),
        ("s", "SLIDER", 0, 2,
         {"slider": (1, 40, _A4["seuil"], 0), "nick": u"Seuil"}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Après n passes, le tassement vaut le tassement initial multiplié "
         u"par le facteur élevé à la puissance n. On cherche le n qui le "
         u"ramène sous le seuil", [
            ("rap", "Division", 1, 0, {}),
        ]),
        (u"C'est un logarithme, dans la base du facteur : log₀,₈₅(5 ÷ 48) "
         u"vaut 13,92", [
            ("log", "Log N", 2, 0, {}),
        ]),
        (u"Arrondi au SUPÉRIEUR : 14 passes. La treizième laisse encore "
         u"5,80 mm. Fixer dix passes d'avance en laisserait 9,45 — près du "
         u"double du toléré, et la boucle se serait arrêtée sur un compte, "
         u"pas sur un état", [
            ("rd", "Round", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("s", "rap", 0), ("d", "rap", 1),
           ("rap", "log", 0), ("f", "log", 1),
           ("log", "rd", 0),
           ("rd", 2, "pan", 0), ("rd", 2, "rep", 0)],
)

R["AV-05"] = dict(
    sujet=[
        ("lg", "DATA:Number", 0, 0,
         {"nick": u"LONGUEURS_DANS_L_ORDRE",
          "data": list(V3.D_AV05_LONGUEURS)}),
        ("cap", "DATA:Number", 0, 4,
         {"nick": u"CAPACITE", "data": [V3.D_AV05_CAPACITE]}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le cumul PARTIEL, pièce après pièce — c'est lui qui porte "
         u"l'information, pas le total. C'est aussi ce qu'une boucle "
         u"transporterait d'un passage au suivant", [
            ("ma", "Mass Addition", 1, 0, {}),
        ]),
        (u"Comparer chaque cumul à la capacité, et repérer les rangs qui la "
         u"dépassent", [
            ("gt", "Larger Than", 2, 0, {}),
            ("rang", "Series", 2, 3,
             {"val": [(0, "Number", [1]), (1, "Number", [1]),
                      (2, "Integer", [len(V3.D_AV05_LONGUEURS)])]}),
            ("cull", "Cull Pattern", 3, 0, {}),
        ]),
        (u"Le premier d'entre eux : la huitième pièce, qui porte le cumul à "
         u"4 068 mm. La septième laissait 3 150 : c'est elle qu'on charge, "
         u"et la huitième qu'on repose", [
            ("prem", "List Item", 4, 0, {"val": [(1, "Integer", [0])]}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("lg", "ma", 0),
           ("ma", 1, "gt", 0), ("cap", "gt", 1),
           ("rang", "cull", 0), ("gt", "cull", 1),
           ("cull", "prem", 0),
           ("prem", "pan", 0), ("prem", "rep", 0)],
)


def _front():
    s = V3.D_AV07_SOLUTIONS
    out = []
    for nom, cout, perf in s:
        domine = any(c2 <= cout and p2 >= perf and (c2 < cout or p2 > perf)
                     for _n2, c2, p2 in s)
        if not domine:
            out.append(u"%s (%d € / %d)" % (nom, cout, perf))
    return out


R["AV-07"] = _etalon(
    u"SOLUTIONS_NON_SURPASSEES", _front(), "Text",
    u"L'étalon nomme les solutions qu'aucune autre ne surpasse sur les DEUX "
    u"critères à la fois — moins chère ET plus performante. Trois des huit "
    u"le sont ; les cinq autres restent défendables",
    u"Cinq sur huit. Ne garder que la moins chère, ou que la plus "
    u"performante, réduirait un arbitrage à un classement — et déciderait à "
    u"la place du projeteur sans le lui dire")


def _stables():
    r = V3.D_AV08_RESIDUS
    for k in range(len(r)):
        if all(v < V3.D_AV08_TOLERANCE for _i, v in r[k:]):
            return [i for i, _v in r[k:]]
    return []


# AV-08 ne se compte pas, il se PREND : la reponse est le premier rang de
# la liste, pas sa longueur. L'helper `_etalon` compte — on ecrit donc la
# recette en clair plutot que de le tordre.
R["AV-08"] = dict(
    sujet=[
        ("res", "DATA:Number", 0, 0,
         {"nick": u"RESIDU_PAR_PASSE",
          "data": [v for _i, v in V3.D_AV08_RESIDUS]}),
        ("tol", "DATA:Number", 0, 3,
         {"nick": u"TOLERANCE", "data": [V3.D_AV08_TOLERANCE]}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon porte les passes à partir desquelles le résidu ne remonte "
         u"PLUS. La sixième descend à 0,09 — sous la tolérance — puis la "
         u"septième remonte à 0,13 : la simulation passait, elle n'était pas "
         u"stabilisée", [
            ("st", "DATA:Number", 1, 0,
             {"nick": u"PASSES_DEFINITIVEMENT_SOUS_LE_SEUIL",
              "data": _stables()}),
        ]),
        (u"La première d'entre elles est la huitième. Répondre 6, le premier "
         u"passage sous la tolérance, fige une forme qui bougeait encore — et "
         u"rien à l'écran ne l'en distingue", [
            ("prem", "List Item", 2, 0, {"val": [(1, "Integer", [0])]}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("st", "prem", 0), ("prem", "pan", 0), ("prem", "rep", 0)],
)


# ---------------------------------------------------------------------------
# Lot WB
# ---------------------------------------------------------------------------

R["WB-08"] = dict(
    sujet=[
        ("h", "DATA:Number", 0, 0,
         {"nick": u"HAUTEUR_DU_MEUBLE",
          # IronPython fait fuiter la variable de boucle : la nommer `_e`
          # ecraserait la fonction `_e` definie plus haut, et les quatre
          # charnieres de la fin echoueraient sur « int is not callable ».
          # Le meme piege qu'a la vague 1, au meme endroit.
          "data": [haut for haut, _nb, _ep in V3.D_WB08_CAS]}),
        ("n", "DATA:Number", 0, 3,
         {"nick": u"NOMBRE_DE_TABLETTES",
          "data": [nb for _haut, nb, _ep in V3.D_WB08_CAS]}),
        ("ep", "DATA:Number", 0, 6,
         {"nick": u"EPAISSEUR",
          "data": [ep for _haut, _nb, ep in V3.D_WB08_CAS]}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Ce qu'une tablette occupe : la hauteur libre exigée, PLUS son "
         u"épaisseur. L'oublier fait passer trois réglages de plus", [
            ("occ", "Addition", 1, 0,
             {"val": [(0, "Number", [V3.D_WB08_LIBRE])]}),
        ]),
        (u"Ce qu'exige le meuble entier : autant de fois que de tablettes", [
            ("besoin", "Multiplication", 2, 0, {}),
        ]),
        (u"Comparer à la hauteur disponible. Trois réglages sur douze n'y "
         u"tiennent pas — alors que chaque paramètre, pris SÉPARÉMENT, est "
         u"dans sa plage. C'est leur croisement qui échoue, et une interface "
         u"qui borne les paramètres un à un ne le voit pas", [
            ("st", "Smaller Than", 3, 0, {}),
            ("cull", "Cull Pattern", 4, 0, {}),
            ("ll", "List Length", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("ep", "occ", 1),
           ("n", "besoin", 0), ("occ", "besoin", 1),
           ("h", "st", 0), ("besoin", "st", 1),
           ("h", "cull", 0), ("st", "cull", 1),
           ("cull", "ll", 0), ("ll", "pan", 0), ("ll", "rep", 0)],
)

_IDX = {u"geometrie": 1, u"unites": 2, u"calques": 3, u"matieres": 4,
        u"metadonnees": 5, u"courbes": 6}
_COL = lambda cle: [bool(f[_IDX[cle]]) for f in V3.D_WB09_FORMATS]

R["WB-09"] = dict(
    sujet=[
        ("geo", "DATA:Boolean", 0, 0,
         {"nick": u"PORTE_LA_GEOMETRIE", "data": _COL(u"geometrie")}),
        ("uni", "DATA:Boolean", 0, 2,
         {"nick": u"PORTE_LES_UNITES", "data": _COL(u"unites")}),
        ("cal", "DATA:Boolean", 0, 4,
         {"nick": u"PORTE_LES_CALQUES", "data": _COL(u"calques")}),
        ("cou", "DATA:Boolean", 0, 6,
         {"nick": u"PORTE_LES_COURBES", "data": _COL(u"courbes")}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'échange exige QUATRE choses. Un format qui n'en porte que trois "
         u"produit un fichier qui s'ouvre — et un bureau d'études qui "
         u"redemande le reste", [
            ("et1", "Gate And", 1, 0, {}),
            ("et2", "Gate And", 2, 0, {}),
            ("et3", "Gate And", 3, 0, {}),
        ]),
        (u"Trois formats sur six répondent aux quatre exigences. Retenir "
         u"tout ce qui porte la géométrie en retiendrait six, et la moitié "
         u"du travail de mise en ordre serait à refaire à l'arrivée", [
            ("cull", "Cull Pattern", 4, 0, {}),
            ("ll", "List Length", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("geo", "et1", 0), ("uni", "et1", 1),
           ("et1", "et2", 0), ("cal", "et2", 1),
           ("et2", "et3", 0), ("cou", "et3", 1),
           ("geo", "cull", 0), ("et3", "cull", 1),
           ("cull", "ll", 0), ("ll", "pan", 0), ("ll", "rep", 0)],
)


# ---------------------------------------------------------------------------
# Lot FA
# ---------------------------------------------------------------------------

_F6 = V3.D_FA06

R["FA-06"] = dict(
    sujet=[
        ("p", "SLIDER", 0, 0,
         {"slider": (500, 5000, _F6["panneau"], 0), "nick": u"Longueur du panneau"}),
        ("pc", "SLIDER", 0, 1,
         {"slider": (50, 1000, _F6["piece"], 0), "nick": u"Longueur d'une piece"}),
        ("tr", "SLIDER", 0, 2,
         {"slider": (0, 10, _F6["trait"], 0), "nick": u"Trait de scie"}),
        ("ri", "SLIDER", 0, 3,
         {"slider": (0, 50, _F6["rive"], 0), "nick": u"Rive a ecarter"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Retirer les DEUX rives : 2 476 mm utilisables sur 2 500", [
            ("r2", "Multiplication", 1, 0, {"val": [(1, "Number", [2])]}),
            ("utile", "Subtraction", 2, 0, {}),
        ]),
        (u"Entre n pièces il y a n − 1 traits de scie, d'où le trait ajouté "
         u"au numérateur et à la longueur de pièce", [
            ("num", "Addition", 3, 0, {}),
            ("den", "Addition", 3, 3, {}),
            ("div", "Division", 4, 0, {}),
        ]),
        (u"Arrondi à l'entier INFÉRIEUR : 6 pièces. Diviser 2 500 par 352 "
         u"en donnerait 7 — il en manque une. Rives et traits mangent 44 mm "
         u"à eux tous, moins de 2 % du panneau, et une pièce sur sept", [
            ("rd", "Round", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("ri", "r2", 0),
           ("p", "utile", 0), ("r2", "utile", 1),
           ("utile", "num", 0), ("tr", "num", 1),
           ("pc", "den", 0), ("tr", "den", 1),
           ("num", "div", 0), ("den", "div", 1),
           ("div", "rd", 0),
           ("rd", 1, "pan", 0), ("rd", 1, "rep", 0)],
)


# ---------------------------------------------------------------------------
# Les quatre questions charnieres de la vague 3
# ---------------------------------------------------------------------------

R["GP-10"] = recette_charniere(_e("GP-10"),
    u"Le choix se fait sur ce qu'on veut\n"
    u"MESURER, pas sur ce qu'on veut voir.\n\n"
    u"Grasshopper convertit tout seul —\n"
    u"et c'est justement le piege.")

R["AV-06"] = recette_charniere(_e("AV-06"),
    u"Objectif SANS contraintes : une solution\n"
    u"absurde mais optimale.\n\n"
    u"Contraintes SANS objectif : un ensemble\n"
    u"admissible, dont aucune n'est meilleure.")

R["AV-09"] = recette_charniere(_e("AV-09"),
    u"Une forme d'equilibre dit OU VA l'effort.\n"
    u"Elle ne dit pas s'il passe.\n\n"
    u"C'est ce qu'un logiciel de calcul\n"
    u"demandera en entree.")

R["FA-05"] = recette_charniere(_e("FA-05"),
    u"Aucun outil ne refuse de derouler.\n"
    u"Ils deforment.\n\n"
    u"L'ecart se chiffre — et il se chiffre\n"
    u"AVANT de decouper en bandes.")
