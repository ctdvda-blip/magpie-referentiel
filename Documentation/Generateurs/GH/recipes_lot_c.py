# -*- coding: utf-8 -*-
"""Recettes de construction du LOT C — projets appliques.

Le corrige d'un projet ne reproduit pas le projet : il etablit son INDICATEUR.
La resille se relaxe avec un plugin, le devis se structure par lot, le plan
d'imbrication sort en DXF — rien de tout cela ne se corrige automatiquement, et
rien de tout cela n'a a l'etre. Ce qui se verifie, c'est le chiffre que le
metier regarde : lineaire de barres, total general, taux de chute.

Deux exercices passent par l'ETALON plutot que par une chaine : C-03, dont la
progression des gradins est recursive — chaque rang depend du precedent — et
C-11, dont le decompte des plis par segment ne se calcule pas sans condition.
Dans les deux cas l'etalon montre exactement ce que l'apprenant devait
produire, et se lit d'un coup d'oeil.
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

import skill_c as C

R = {}

_1, _2, _3 = C.D_C01, C.D_C02, C.D_C03
_5, _6, _7 = C.D_C05, C.D_C06, C.D_C07
_8, _9, _10, _11, _12 = C.D_C08, C.D_C09, C.D_C10, C.D_C11, C.D_C12


R["C-01"] = dict(
    sujet=[
        ("e", "SLIDER", 0, 0,
         {"slider": (100, 1200, _1["entraxe"], 0), "nick": u"Entraxe des lames"}),
        ("h", "SLIDER", 0, 1,
         {"slider": (10, 85, _1["hauteur_solaire"], 0), "nick": u"Hauteur solaire"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'ombre d'une lame descend de sa profondeur multipliée par la "
         u"tangente de la hauteur solaire. Pour qu'elle atteigne la lame "
         u"suivante, il faut donc DIVISER l'entraxe par cette tangente", [
            ("rad", "Radians", 1, 0, {}),
            ("tan", "Tangent", 2, 0, {}),
            ("p", "Division", 3, 0, {}),
        ]),
        (u"249,95 mm. Multiplier au lieu de diviser donnerait 640 mm — une "
         u"lame qui se recouvre elle-même sur un entraxe de 400, et une "
         u"façade devenue mur", [
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("h", "rad", 0), ("rad", "tan", 0),
           ("e", "p", 0), ("tan", "p", 1),
           ("p", "pan", 0), ("p", "rep", 0)],
)

R["C-02"] = dict(
    sujet=[
        ("la", "SLIDER", 0, 0,
         {"slider": (6000, 40000, _2["largeur"], 0), "nick": u"Largeur"}),
        ("pr", "SLIDER", 0, 1,
         {"slider": (6000, 40000, _2["profondeur"], 0), "nick": u"Profondeur"}),
        ("m", "SLIDER", 0, 2,
         {"slider": (500, 4000, _2["maille"], 0), "nick": u"Maille"}),
        ("rep", "REPONSE", 10, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le nombre de panneaux dans chaque sens : 12 par 8", [
            ("nx", "Division", 1, 0, {}),
            ("ny", "Division", 1, 3, {}),
        ]),
        (u"Les horizontales courent sur chaque rangée de nœuds — il y en a "
         u"une de plus que de panneaux ; de même pour les verticales", [
            ("ny1", "Addition", 2, 0, {"val": [(1, "Number", [1])]}),
            ("nx1", "Addition", 2, 3, {"val": [(1, "Number", [1])]}),
            ("h1", "Multiplication", 3, 0, {}),
            ("hz", "Multiplication", 4, 0, {}),
            ("v1", "Multiplication", 3, 3, {}),
            ("vt", "Multiplication", 4, 3, {}),
        ]),
        (u"Une diagonale par panneau, longue de √2 fois la maille. Ce sont "
         u"elles qui TRIANGULENT : sans elles, la résille est une grille "
         u"articulée, et le chiffrage tombe à 424 m au lieu de 695", [
            ("np", "Multiplication", 3, 6, {}),
            ("r2", "Square Root", 4, 6, {"val": [(0, "Number", [2])]}),
            ("ld", "Multiplication", 5, 6, {}),
            ("dg", "Multiplication", 6, 6, {}),
        ]),
        (u"695,53 m de barres", [
            ("s1", "Addition", 7, 0, {}),
            ("s2", "Addition", 8, 0, {}),
            ("met", "Division", 9, 0, {"val": [(1, "Number", [1000])]}),
            ("pan", "PANEL", 9, 3, {}),
        ]),
    ],
    wires=[("la", "nx", 0), ("m", "nx", 1),
           ("pr", "ny", 0), ("m", "ny", 1),
           ("ny", "ny1", 0), ("nx", "nx1", 0),
           ("ny1", "h1", 0), ("nx", "h1", 1), ("h1", "hz", 0), ("m", "hz", 1),
           ("nx1", "v1", 0), ("ny", "v1", 1), ("v1", "vt", 0), ("m", "vt", 1),
           ("nx", "np", 0), ("ny", "np", 1),
           ("m", "ld", 0), ("r2", "ld", 1),
           ("np", "dg", 0), ("ld", "dg", 1),
           ("hz", "s1", 0), ("vt", "s1", 1),
           ("s1", "s2", 0), ("dg", "s2", 1),
           ("s2", "met", 0), ("met", "pan", 0), ("met", "rep", 0)],
)


def _hauteurs_c03():
    h = [0.0]
    for i in range(1, _3["rangs"]):
        dp = _3["foyer"] + (i - 1) * _3["profondeur"]
        dc = _3["foyer"] + i * _3["profondeur"]
        h.append((h[-1] + _3["degagement"]) * dc / dp)
    return h


R["C-03"] = dict(
    sujet=[
        ("n", "SLIDER", 0, 0,
         {"slider": (4, 40, _3["rangs"], 0), "nick": u"Rangs"}),
        ("p", "SLIDER", 0, 1,
         {"slider": (600, 1400, _3["profondeur"], 0), "nick": u"Profondeur de rang"}),
        ("c", "SLIDER", 0, 2,
         {"slider": (60, 150, _3["degagement"], 0), "nick": u"Degagement"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon porte les dix-huit hauteurs. La progression est "
         u"RÉCURSIVE : chaque rang se déduit du précédent, multiplié par le "
         u"rapport des distances au foyer — elle ne s'écrit pas sans boucle, "
         u"et c'est pourquoi le corrigé la donne relevée", [
            ("h", "DATA:Number", 1, 0,
             {"nick": u"HAUTEUR_DE_CHAQUE_RANG", "data": _hauteurs_c03()}),
        ]),
        (u"3 105 mm au dernier rang. Ajouter 90 mm par rang en donnerait "
         u"1 530 — la moitié. Le dégagement ne s'ajoute pas, il se propage, "
         u"et d'autant plus qu'on s'éloigne du foyer", [
            ("bor", "Bounds", 2, 0, {}),
            ("dd", "Deconstruct Domain", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("h", "bor", 0), ("bor", "dd", 0),
           ("dd", 1, "pan", 0), ("dd", 1, "rep", 0)],
)

_QTE = [q for _n, lignes in C.D_C04_LOTS for _d, q, _u, _pu in lignes]
_PU = [pu for _n, lignes in C.D_C04_LOTS for _d, _q, _u, pu in lignes]

R["C-04"] = dict(
    sujet=[
        ("q", "DATA:Number", 0, 0, {"nick": u"QUANTITES", "data": _QTE}),
        ("pu", "DATA:Number", 0, 4, {"nick": u"PRIX_UNITAIRES", "data": _PU}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Chaque ligne : sa quantité par son prix unitaire. Les unités "
         u"diffèrent — m³, tonne, unité, m² — de sorte que sommer les "
         u"quantités n'aurait aucun sens", [
            ("m", "Multiplication", 1, 0, {}),
        ]),
        (u"55 099,00 €. Un devis à trois lots et neuf lignes se vérifie de "
         u"deux façons — par les lots et par les lignes — et les deux doivent "
         u"tomber sur le même chiffre", [
            ("tot", "Mass Addition", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("q", "m", 0), ("pu", "m", 1),
           ("m", "tot", 0), ("tot", "pan", 0), ("tot", "rep", 0)],
)

R["C-05"] = dict(
    sujet=[
        ("l", "SLIDER", 0, 0,
         {"slider": (800, 6000, _5["largeur"], 0), "nick": u"Largeur"}),
        ("em", "SLIDER", 0, 1,
         {"slider": (400, 1200, _5["entraxe_max"], 0), "nick": u"Entraxe maximal"}),
        ("tp", "SLIDER", 0, 2,
         {"slider": (1, 10, _5["tablettes_par_travee"], 0), "nick": u"Tablettes par travee"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le nombre de travées est imposé par la portée maximale d'une "
         u"tablette : 3 200 ÷ 800 fait exactement 4, arrondi au supérieur", [
            ("dv", "Division", 1, 0, {}),
            ("rd", "Round", 2, 0, {}),
        ]),
        (u"Les montants sont un de plus que les travées — cinq, pas quatre. "
         u"Le meuble monté sur le compte faux n'a pas de joue à une "
         u"extrémité", [
            ("mo", "Addition", 3, 0, {"val": [(1, "Number", [1])]}),
        ]),
        (u"Plus les tablettes, deux traverses et un fond : 28 panneaux", [
            ("tb", "Multiplication", 3, 3, {}),
            ("s1", "Addition", 4, 0, {}),
            ("s2", "Addition", 5, 0, {"val": [(1, "Number", [3])]}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("l", "dv", 0), ("em", "dv", 1), ("dv", "rd", 0),
           ("rd", 2, "mo", 0),
           ("rd", 2, "tb", 0), ("tp", "tb", 1),
           ("mo", "s1", 0), ("tb", "s1", 1),
           ("s1", "s2", 0),
           ("s2", "pan", 0), ("s2", "rep", 0)],
)

R["C-06"] = dict(
    sujet=[
        ("c", "SLIDER", 0, 0,
         {"slider": (100, 1200, _6["corde"], 0), "nick": u"Corde de la directrice"}),
        ("f", "SLIDER", 0, 1,
         {"slider": (10, 300, _6["fleche"], 0), "nick": u"Fleche"}),
        ("e", "SLIDER", 0, 2,
         {"slider": (2, 20, _6["epaisseur"], 0), "nick": u"Epaisseur de lamelle"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le rayon d'un arc se retrouve de sa corde ET de sa flèche : "
         u"(c² / 4 + f²) ÷ 2f. Ni la flèche ni la demi-corde ne sont le "
         u"rayon", [
            ("c2", "Multiplication", 1, 0, {}),
            ("c4", "Division", 2, 0, {"val": [(1, "Number", [4])]}),
            ("f2", "Multiplication", 1, 3, {}),
            ("num", "Addition", 3, 0, {}),
            ("den", "Multiplication", 2, 5, {"val": [(1, "Number", [2])]}),
            ("r", "Division", 4, 0, {}),
        ]),
        (u"371,73 mm, contre 200 admissibles pour une lamelle de 8 mm au "
         u"rapport 25 : conforme, avec 86 % de marge", [
            ("mini", "Multiplication", 5, 3,
             {"val": [(1, "Number", [_6["rapport_mini"]])]}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("c", "c2", 0), ("c", "c2", 1), ("c2", "c4", 0),
           ("f", "f2", 0), ("f", "f2", 1),
           ("c4", "num", 0), ("f2", "num", 1),
           ("f", "den", 0),
           ("num", "r", 0), ("den", "r", 1),
           ("e", "mini", 0),
           ("r", "pan", 0), ("r", "rep", 0)],
)

R["C-07"] = dict(
    sujet=[
        ("b", "SLIDER", 0, 0,
         {"slider": (100, 800, _7["base"], 0), "nick": u"Prix de base"}),
        ("pi", "SLIDER", 0, 1,
         {"slider": (50, 250, C.D_C07_PIEDS[_7["choix"][0]], 0),
          "nick": u"Prix du pied choisi"}),
        ("nt", "SLIDER", 0, 2,
         {"slider": (0, 5, _7["choix"][1], 0), "nick": u"Tiroirs"}),
        ("pt", "SLIDER", 0, 3,
         {"slider": (20, 200, _7["par_tiroir"], 0), "nick": u"Prix par tiroir"}),
        ("k", "SLIDER", 0, 4,
         {"slider": (1, 2, C.D_C07_MATIERE[_7["choix"][2]], 2),
          "nick": u"Coefficient matiere"}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le meuble hors matière : base, pied, et les tiroirs", [
            ("ti", "Multiplication", 1, 0, {}),
            ("s1", "Addition", 2, 0, {}),
            ("s2", "Addition", 3, 0, {}),
        ]),
        (u"Le coefficient de matière s'applique à TOUT le meuble — pieds et "
         u"tiroirs compris. Ne majorer que la base donnerait 858,20 € au lieu "
         u"de 1 033,76 : un sixième du prix, toujours à la perte", [
            ("px", "Multiplication", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("nt", "ti", 0), ("pt", "ti", 1),
           ("b", "s1", 0), ("pi", "s1", 1),
           ("s1", "s2", 0), ("ti", "s2", 1),
           ("s2", "px", 0), ("k", "px", 1),
           ("px", "pan", 0), ("px", "rep", 0)],
)

R["C-08"] = dict(
    sujet=[
        ("t", "SLIDER", 0, 0,
         {"slider": (40, 70, _8["taille"], 0), "nick": u"Taille (circonference)"}),
        ("la", "SLIDER", 0, 1,
         {"slider": (1, 6, _8["largeur"], 1), "nick": u"Largeur de l'anneau"}),
        ("ep", "SLIDER", 0, 2,
         {"slider": (0.8, 3, _8["epaisseur"], 2), "nick": u"Epaisseur"}),
        ("ch", "SLIDER", 0, 3,
         {"slider": (0, 120, _8["chaton"], 0), "nick": u"Volume du chaton"}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"La matière ne court pas sur la circonférence du DOIGT mais sur la "
         u"fibre moyenne de l'anneau, à mi-épaisseur : la taille plus π fois "
         u"l'épaisseur", [
            ("pi", "Pi", 1, 0, {"val": [(0, "Number", [1])]}),
            ("pe", "Multiplication", 2, 0, {}),
            ("cm", "Addition", 3, 0, {}),
        ]),
        (u"Le volume de l'anneau, puis celui du chaton et des griffes", [
            ("v1", "Multiplication", 4, 0, {}),
            ("v2", "Multiplication", 5, 0, {}),
            ("v", "Addition", 6, 0, {}),
        ]),
        (u"L'or 750 pèse 15,6 g par centimètre cube : 3,011 g, sous la limite "
         u"de 3,2. Le calcul sur la circonférence nominale donnerait 2,845 — "
         u"0,17 g de moins, soit plus de trois fois la tolérance, et toujours "
         u"en dessous de la vérité", [
            ("m", "Multiplication", 7, 0,
             {"val": [(1, "Number", [_8["densite"]])]}),
            ("g", "Division", 8, 0, {"val": [(1, "Number", [1000])]}),
            ("pan", "PANEL", 8, 3, {}),
        ]),
    ],
    wires=[("ep", "pe", 0), ("pi", "pe", 1),
           ("t", "cm", 0), ("pe", "cm", 1),
           ("cm", "v1", 0), ("la", "v1", 1),
           ("v1", "v2", 0), ("ep", "v2", 1),
           ("v2", "v", 0), ("ch", "v", 1),
           ("v", "m", 0), ("m", "g", 0),
           ("g", "pan", 0), ("g", "rep", 0)],
)

R["C-09"] = dict(
    sujet=[
        ("s", "SLIDER", 0, 0,
         {"slider": (50, 800, _9["surface"], 0), "nick": u"Surface a paver"}),
        ("d", "SLIDER", 0, 1,
         {"slider": (0.5, 5, _9["diametre"], 2), "nick": u"Diametre de pierre"}),
        ("me", "SLIDER", 0, 2,
         {"slider": (0.1, 1, _9["metal"], 2), "nick": u"Metal entre pierres"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le pas d'une pierre à la suivante n'est pas son diamètre : c'est "
         u"le diamètre PLUS le métal qui les sépare", [
            ("pas", "Addition", 1, 0, {}),
        ]),
        (u"Dans une maille hexagonale — la plus dense — chaque pierre occupe "
         u"√3/2 fois le carré du pas, soit 4,00 mm² ici. Des disques ne "
         u"pavent pas un plan : même sans écart, 9 % de vide subsiste", [
            ("p2", "Multiplication", 2, 0, {}),
            ("r3", "Square Root", 2, 3, {"val": [(0, "Number", [3])]}),
            ("k", "Division", 3, 3, {"val": [(1, "Number", [2])]}),
            ("au", "Multiplication", 3, 0, {}),
        ]),
        (u"64 pierres. Diviser par l'aire d'une pierre seule en donnerait 96 "
         u"— une commande fausse de moitié", [
            ("n", "Division", 4, 0, {}),
            ("rd", "Round", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("d", "pas", 0), ("me", "pas", 1),
           ("pas", "p2", 0), ("pas", "p2", 1),
           ("r3", "k", 0),
           ("p2", "au", 0), ("k", "au", 1),
           ("s", "n", 0), ("au", "n", 1),
           ("n", "rd", 0),
           ("rd", 1, "pan", 0), ("rd", 1, "rep", 0)],
)

R["C-10"] = dict(
    sujet=[
        ("s", "SLIDER", 0, 0,
         {"slider": (50, 500, _10["surface"], 0), "nick": u"Surface du corps"}),
        ("ac", "SLIDER", 0, 1,
         {"slider": (0.5, 4, _10["aire_cellule"], 1), "nick": u"Aire de cellule visee"}),
        ("fi", "SLIDER", 0, 2,
         {"slider": (0.05, 1, _10["filet"], 2), "nick": u"Filet"}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le côté d'une cellule d'aire donnée : sa racine carrée, 1,22 mm", [
            ("c", "Square Root", 1, 0, {}),
        ]),
        (u"Le filet court AUTOUR de chaque cellule : le pas réel est le côté "
         u"plus le filet, 1,47 mm — soit 2,17 mm² par cellule au lieu de 1,5, "
         u"45 % de plus", [
            ("pas", "Addition", 2, 0, {}),
            ("au", "Multiplication", 3, 0, {}),
        ]),
        (u"77 cellules. Ignorer le filet en donnerait 112 : le motif arrive "
         u"trop dense, et le filet disparaît au polissage", [
            ("n", "Division", 4, 0, {}),
            ("rd", "Round", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("ac", "c", 0),
           ("c", "pas", 0), ("fi", "pas", 1),
           ("pas", "au", 0), ("pas", "au", 1),
           ("s", "n", 0), ("au", "n", 1),
           ("n", "rd", 0),
           ("rd", 1, "pan", 0), ("rd", 1, "rep", 0)],
)


def _plats_c11():
    out = []
    for i, c in enumerate(_11["cotes"]):
        nb = 1 if i in (0, len(_11["cotes"]) - 1) else 2
        out.append(c - nb * (_11["rayon"] + _11["epaisseur"]))
    return out


R["C-11"] = dict(
    sujet=[
        ("co", "DATA:Number", 0, 0,
         {"nick": u"COTES_EXTERIEURES", "data": list(_11["cotes"])}),
        ("ep", "SLIDER", 0, 4,
         {"slider": (0.5, 6, _11["epaisseur"], 1), "nick": u"Epaisseur"}),
        ("ra", "SLIDER", 0, 5,
         {"slider": (0.5, 10, _11["rayon"], 1), "nick": u"Rayon interieur"}),
        ("k", "SLIDER", 0, 6,
         {"slider": (0.3, 0.5, _11["k"], 2), "nick": u"Facteur K"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon porte les parties réellement PLATES. Le décompte se fait "
         u"segment par segment : les quatre segments intérieurs portent DEUX "
         u"plis, les deux extrémités un seul. C'est une condition, pas un "
         u"calcul — d'où le relevé", [
            ("pl", "DATA:Number", 1, 0,
             {"nick": u"PARTIES_PLATES", "data": _plats_c11()}),
            ("sp", "Mass Addition", 2, 0, {}),
        ]),
        (u"L'allongement d'un pli à 90° : un quart de cercle sur la fibre "
         u"neutre, à r + K·e du centre de courbure", [
            ("ke", "Multiplication", 1, 4, {}),
            ("rn", "Addition", 2, 4, {}),
            ("q", "Pi", 3, 4, {"val": [(0, "Number", [0.5])]}),
            ("ba", "Multiplication", 4, 4, {}),
        ]),
        (u"Cinq plis : 500,47 mm de développé. La somme des cotes extérieures "
         u"donnerait 520 — près de 20 mm de bande en trop", [
            ("n5", "Multiplication", 5, 4,
             {"val": [(1, "Number", [len(_11["cotes"]) - 1])]}),
            ("tot", "Addition", 6, 0, {}),
            ("pan", "PANEL", 7, 0, {}),
        ]),
    ],
    wires=[("pl", "sp", 0),
           ("k", "ke", 0), ("ep", "ke", 1),
           ("ra", "rn", 0), ("ke", "rn", 1),
           ("rn", "ba", 0), ("q", "ba", 1),
           ("ba", "n5", 0),
           ("sp", "tot", 0), ("n5", "tot", 1),
           ("tot", "pan", 0), ("tot", "rep", 0)],
)

_A12 = [float((a + _12["espacement"]) * (b + _12["espacement"]))
        for a, b in C.D_C12_PIECES]
_NUE12 = [float(a * b) for a, b in C.D_C12_PIECES]

R["C-12"] = dict(
    sujet=[
        ("nue", "DATA:Number", 0, 0,
         {"nick": u"AIRES_NUES", "data": _NUE12}),
        ("esp", "DATA:Number", 0, 5,
         {"nick": u"AIRES_AVEC_ESPACEMENT", "data": _A12}),
        ("ut", "DATA:Number", 0, 9,
         {"nick": u"SURFACE_UTILE_D_UNE_PLAQUE",
          "data": [(C.D_C12_PLAQUE[0] - 2 * _12["bord"])
                   * (C.D_C12_PLAQUE[1] - 2 * _12["bord"])]}),
        ("pl", "DATA:Number", 0, 11,
         {"nick": u"SURFACE_D_UNE_PLAQUE",
          "data": [C.D_C12_PLAQUE[0] * C.D_C12_PLAQUE[1]]}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"C'est la surface AVEC espacement qui décide du nombre de plaques, "
         u"et la surface utile — bords perdus déduits — qui sert de "
         u"référence : 13,45 m² ne tiennent pas dans les 13,10 m² utiles de "
         u"trois plaques", [
            ("se", "Mass Addition", 1, 0, {}),
            ("dv", "Division", 2, 0, {}),
            ("rd", "Round", 3, 0, {}),
        ]),
        (u"Quatre plaques. Le calcul sur les surfaces nues en annoncerait "
         u"trois — et la découpe s'arrêterait en fin de série, une plaque "
         u"manquante au bon de commande", [
            ("sn", "Mass Addition", 1, 5, {}),
            ("dispo", "Multiplication", 4, 0, {}),
        ]),
        (u"27,36 % de chute. C'est un MINORANT, comme en B-13 : le placement "
         u"réel ajoute la sienne", [
            ("part", "Division", 5, 0, {}),
            ("un", "Subtraction", 6, 0, {"val": [(0, "Number", [1])]}),
            ("cent", "Multiplication", 7, 0, {"val": [(1, "Number", [100])]}),
            ("pan", "PANEL", 8, 0, {}),
        ]),
    ],
    wires=[("esp", "se", 0), ("nue", "sn", 0),
           ("se", "dv", 0), ("ut", "dv", 1),
           ("dv", "rd", 0),
           ("rd", 2, "dispo", 0), ("pl", "dispo", 1),
           ("sn", "part", 0), ("dispo", "part", 1),
           ("part", "un", 1), ("un", "cent", 0),
           ("cent", "pan", 0), ("cent", "rep", 0)],
)
