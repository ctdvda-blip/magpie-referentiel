# -*- coding: utf-8 -*-
"""Recettes de construction du LOT G — exercices gamifies.

Le corrige d'un exercice gamifie n'a pas a rejouer le jeu. Il etablit la
METRIQUE que le jeu affiche : le score du tableau des scores, l'index trouve
de la chasse au tresor, la longueur cumulee de l'animation a mi-parcours.

SIX EXERCICES PASSENT PAR L'ETALON
----------------------------------
G-11, G-12, G-13, G-17, G-18 et G-19. Ce sont des jeux de CONNAISSANCE — mots
croises, memory, quiz, vrai/faux, boite noire — dont la reponse ne se calcule
pas : elle se sait. Un corrige qui construirait une chaine de composants pour
retrouver le nom anglais de `Dispatch` mentirait sur la nature de la tache.
L'etalon montre la reponse, et le commentaire dit d'ou elle vient.

Partout ailleurs, la chaine fait le travail.
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

import skill_g as S

R = {}

_f = lambda xs: [float(x) for x in xs]


# ---------------------------------------------------------------------------
# G-01 — le tableau des scores
# ---------------------------------------------------------------------------
R["G-01"] = dict(
    sujet=[
        ("v", "DATA:Number", 0, 0,
         {"nick": u"VALEURS_MELANGEES", "data": _f(S.D_G01)}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"`Sort List` trie ses CLÉS et rend la liste triée. Le score en "
         u"découle : dix points par valeur bien placée, douze fois, cent "
         u"vingt", [
            ("tri", "Sort List", 1, 0, {}),
            ("pan", "PANEL", 2, 0, {}),
        ]),
    ],
    wires=[("v", "tri", 0), ("tri", "pan", 0), ("tri", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-02 — la barre de progression
# ---------------------------------------------------------------------------
_D2 = S.D_G02
R["G-02"] = dict(
    sujet=[
        ("r", "SLIDER", 0, 0,
         {"slider": (10, 200, _D2["rayon"], 0), "nick": u"Rayon du cercle"}),
        ("a", "SLIDER", 0, 1,
         {"slider": (10, 300, _D2["rectangle"][0], 0), "nick": u"Rectangle, cote A"}),
        ("b", "SLIDER", 0, 2,
         {"slider": (10, 300, _D2["rectangle"][1], 0), "nick": u"Rectangle, cote B"}),
        ("t", "SLIDER", 0, 3,
         {"slider": (10, 200, _D2["triangle"], 0), "nick": u"Cote du triangle"}),
        ("h", "SLIDER", 0, 4,
         {"slider": (10, 200, _D2["hexagone"], 0), "nick": u"Cote de l'hexagone"}),
        ("s", "SLIDER", 0, 5,
         {"slider": (10, 300, _D2["segment"], 0), "nick": u"Longueur du segment"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le cercle : 2πr. Le rectangle : deux fois la somme de ses côtés", [
            ("pi", "Pi", 1, 0, {"val": [(0, "Number", [2])]}),
            ("pc", "Multiplication", 2, 0, {}),
            ("ab", "Addition", 1, 3, {}),
            ("pr", "Multiplication", 2, 3, {"val": [(1, "Number", [2])]}),
        ]),
        (u"Le triangle et l'hexagone : n fois leur côté. C'est ici que se "
         u"perd le premier jalon — prendre le côté pour le périmètre donne "
         u"936,74 au lieu de 1 372,74", [
            ("pt", "Multiplication", 2, 6, {"val": [(1, "Number", [3])]}),
            ("ph", "Multiplication", 2, 8, {"val": [(1, "Number", [6])]}),
        ]),
        (u"1 372,74 mm : la barre passe au vert", [
            ("s1", "Addition", 3, 0, {}),
            ("s2", "Addition", 4, 0, {}),
            ("s3", "Addition", 5, 0, {}),
            ("s4", "Addition", 6, 0, {}),
            ("pan", "PANEL", 7, 0, {}),
        ]),
    ],
    wires=[("r", "pc", 0), ("pi", "pc", 1),
           ("a", "ab", 0), ("b", "ab", 1), ("ab", "pr", 0),
           ("t", "pt", 0), ("h", "ph", 0),
           ("pc", "s1", 0), ("pr", "s1", 1),
           ("s1", "s2", 0), ("pt", "s2", 1),
           ("s2", "s3", 0), ("ph", "s3", 1),
           ("s3", "s4", 0), ("s", "s4", 1),
           ("s4", "pan", 0), ("s4", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-03 — contre la montre
# ---------------------------------------------------------------------------
_L1, _L2, _L3, _L4, _L5 = S.D_G03
R["G-03"] = dict(
    sujet=[
        ("l1", "DATA:Number", 0, 0, {"nick": u"LISTE_1", "data": _f(_L1)}),
        ("l2", "DATA:Number", 0, 2, {"nick": u"LISTE_2", "data": _f(_L2)}),
        ("l3", "DATA:Number", 0, 4, {"nick": u"LISTE_3", "data": _f(_L3)}),
        ("l4", "DATA:Number", 0, 6, {"nick": u"LISTE_4", "data": _f(_L4)}),
        ("l5", "DATA:Number", 0, 8, {"nick": u"LISTE_5", "data": _f(_L5)}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Cinq extractions de cinq natures : l'élément d'index 3, le "
         u"dernier, le maximum, le minimum, le médian. Aucun composant ne "
         u"les fait toutes", [
            ("i1", "List Item", 1, 0, {"val": [(1, "Integer", [3])]}),
            ("rv", "Reverse List", 1, 2, {}),
            ("i2", "List Item", 2, 2, {"val": [(1, "Integer", [0])]}),
            ("b3", "Bounds", 1, 4, {}),
            ("d3", "Deconstruct Domain", 2, 4, {}),
            ("b4", "Bounds", 1, 6, {}),
            ("d4", "Deconstruct Domain", 2, 6, {}),
            ("t5", "Sort List", 1, 8, {}),
            ("i5", "List Item", 2, 8, {"val": [(1, "Integer", [4])]}),
        ]),
        (u"Les cinq réponses dans l'ordre. Rendre 3 au lieu de 806 pour "
         u"« l'élément d'index 3 » est l'erreur du chronomètre : le rang "
         u"n'est pas la valeur", [
            ("m1", "Merge", 3, 0, {}),
            ("m2", "Merge", 4, 0, {}),
            ("m3", "Merge", 5, 0, {}),
            ("m4", "Merge", 5, 4, {}),
            ("pan", "PANEL", 5, 8, {}),
        ]),
    ],
    wires=[("l1", "i1", 0),
           ("l2", "rv", 0), ("rv", "i2", 0),
           ("l3", "b3", 0), ("b3", "d3", 0),
           ("l4", "b4", 0), ("b4", "d4", 0),
           ("l5", "t5", 0), ("t5", "i5", 0),
           ("i1", "m1", 0), ("i2", "m1", 1),
           ("m1", "m2", 0), ("d3", 1, "m2", 1),
           ("m2", "m3", 0), ("d4", 0, "m3", 1),
           ("m3", "m4", 0), ("i5", "m4", 1),
           ("m4", "pan", 0), ("m4", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-04 — trois vies
# ---------------------------------------------------------------------------
R["G-04"] = dict(
    sujet=[
        ("a", "SLIDER", 0, 0,
         {"slider": (1, 30, S.D_G04["a"], 0), "nick": u"Taille de la liste A"}),
        ("b", "SLIDER", 0, 1,
         {"slider": (1, 30, S.D_G04["b"], 0), "nick": u"Taille de la liste B"}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le plus court rend 7 résultats, le plus long 11. La référence "
         u"croisée, elle, est un PRODUIT : 77, et non 18", [
            ("mi", "Minimum", 1, 0, {}),
            ("ma", "Maximum", 1, 3, {}),
            ("cr", "Multiplication", 1, 6, {}),
        ]),
        (u"95. Croire que la référence croisée additionne donne 36, et fait "
         u"perdre les trois vies d'un coup", [
            ("s1", "Addition", 2, 0, {}),
            ("s2", "Addition", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("a", "mi", 0), ("b", "mi", 1),
           ("a", "ma", 0), ("b", "ma", 1),
           ("a", "cr", 0), ("b", "cr", 1),
           ("mi", "s1", 0), ("ma", "s1", 1),
           ("s1", "s2", 0), ("cr", "s2", 1),
           ("s2", "pan", 0), ("s2", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-05 — la collection de badges
# ---------------------------------------------------------------------------
_D5 = S.D_G05
R["G-05"] = dict(
    sujet=[
        ("h", "SLIDER", 0, 0,
         {"slider": (1000, 8000, _D5["hauteur"], 0), "nick": u"Hauteur de poteau"}),
        ("e", "SLIDER", 0, 1,
         {"slider": (2000, 12000, _D5["entraxe"], 0), "nick": u"Entraxe"}),
        ("s", "SLIDER", 0, 2,
         {"slider": (100, 600, _D5["section"], 0), "nick": u"Hauteur de section"}),
        ("la", "SLIDER", 0, 3,
         {"slider": (50, 400, _D5["largeur"], 0), "nick": u"Largeur de section"}),
        ("ep", "SLIDER", 0, 4,
         {"slider": (4, 30, _D5["epaisseur"], 0), "nick": u"Epaisseur"}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Badge 1 — le développé : deux poteaux et une traverse", [
            ("h2", "Multiplication", 1, 0, {"val": [(1, "Number", [2])]}),
            ("dev", "Addition", 2, 0, {}),
        ]),
        (u"Badge 2 — l'aire de la section. Le profil est CREUX : on déduit "
         u"l'intérieur. Le calculer plein donne 61 200 au lieu de 11 904, et "
         u"fait rater trois badges d'un coup", [
            ("e2", "Multiplication", 1, 3, {"val": [(1, "Number", [2])]}),
            ("li", "Subtraction", 2, 3, {}),
            ("si", "Subtraction", 2, 5, {}),
            ("pl", "Multiplication", 3, 3, {}),
            ("cr", "Multiplication", 3, 5, {}),
            ("sec", "Subtraction", 4, 3, {}),
        ]),
        (u"Badges 3 et 4 — le volume, puis la masse à 7,85 g/cm³", [
            ("vol", "Multiplication", 5, 0, {}),
            ("cm3", "Division", 6, 0, {"val": [(1, "Number", [1000])]}),
            ("kg", "Multiplication", 6, 3,
             {"val": [(1, "Number", [_D5["densite"]])]}),
        ]),
        (u"Badges 5 et 6 — la hauteur hors tout et la portée libre. Six "
         u"badges : le badge doré ARPENTEUR", [
            ("s2", "Division", 5, 6, {"val": [(1, "Number", [2])]}),
            ("hht", "Addition", 6, 6, {}),
            ("por", "Subtraction", 6, 8, {}),
            ("m1", "Merge", 7, 0, {}),
            ("m2", "Merge", 7, 2, {}),
            ("m3", "Merge", 7, 4, {}),
            ("m4", "Merge", 8, 0, {}),
            ("m5", "Merge", 8, 4, {}),
            ("pan", "PANEL", 8, 8, {}),
        ]),
    ],
    wires=[("h", "h2", 0), ("h2", "dev", 0), ("e", "dev", 1),
           ("ep", "e2", 0),
           ("la", "li", 0), ("e2", "li", 1),
           ("s", "si", 0), ("e2", "si", 1),
           ("la", "pl", 0), ("s", "pl", 1),
           ("li", "cr", 0), ("si", "cr", 1),
           ("pl", "sec", 0), ("cr", "sec", 1),
           ("sec", "vol", 0), ("dev", "vol", 1),
           ("vol", "cm3", 0), ("vol", "kg", 0),
           ("s", "s2", 0), ("h", "hht", 0), ("s2", "hht", 1),
           ("e", "por", 0), ("la", "por", 1),
           ("dev", "m1", 0), ("sec", "m1", 1),
           ("cm3", "m2", 0), ("kg", "m2", 1),
           ("hht", "m3", 0), ("por", "m3", 1),
           ("m1", "m4", 0), ("m2", "m4", 1),
           ("m4", "m5", 0), ("m3", "m5", 1),
           ("m5", "pan", 0), ("m5", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-06 — le déblocage progressif
# ---------------------------------------------------------------------------
R["G-06"] = dict(
    sujet=[
        ("v", "DATA:Number", 0, 0,
         {"nick": u"SOIXANTE_VALEURS", "data": _f(S.D_G06)}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Niveau 1 — les valeurs paires : le reste modulo 2 vaut zéro. "
         u"Il en reste 32", [
            ("idx", "Series", 1, 4,
             {"val": [(0, "Number", [0]), (1, "Number", [1]),
                      (2, "Integer", [len(S.D_G06)])]}),
            ("mod", "Modulus", 1, 0, {"val": [(1, "Number", [2])]}),
            ("pair", "Equality", 2, 0, {"val": [(1, "Number", [0])]}),
        ]),
        (u"Niveau 2 — parmi CELLES-LÀ, celles qui dépassent 500. Il en "
         u"reste 16", [
            ("v1", "Cull Pattern", 3, 0, {}),
            ("i1", "Cull Pattern", 3, 4, {}),
            ("gt", "Larger Than", 4, 0, {"val": [(1, "Number", [500])]}),
            ("v2", "Cull Pattern", 5, 0, {}),
            ("i2", "Cull Pattern", 5, 4, {}),
        ]),
        (u"Niveau 3 — celles qui dépassent la moyenne DES SEIZE "
         u"SURVIVANTES, 771,50. Prendre la moyenne des soixante valeurs de "
         u"départ, 518,93, en garderait quinze au lieu de huit : un filtre "
         u"s'applique à ce qui reste", [
            ("moy", "Average", 6, 0, {}),
            ("gt2", "Larger Than", 7, 0, {}),
            ("i3", "Cull Pattern", 8, 0, {}),
            ("pan", "PANEL", 8, 4, {}),
        ]),
    ],
    wires=[("v", "mod", 0), ("mod", "pair", 0),
           ("v", "v1", 0), ("pair", "v1", 1),
           ("idx", "i1", 0), ("pair", "i1", 1),
           ("v1", "gt", 0),
           ("v1", "v2", 0), ("gt", 0, "v2", 1),
           ("i1", "i2", 0), ("gt", 0, "i2", 1),
           ("v2", "moy", 0),
           ("v2", "gt2", 0), ("moy", "gt2", 1),
           ("i2", "i3", 0), ("gt2", 0, "i3", 1),
           ("i3", "pan", 0), ("i3", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-07 — une, deux ou trois étoiles
# ---------------------------------------------------------------------------
_D7 = S.D_G07
R["G-07"] = dict(
    sujet=[
        ("lx", "SLIDER", 0, 0,
         {"slider": (500, 8000, _D7["longueur"], 0), "nick": u"Longueur de trame"}),
        ("ly", "SLIDER", 0, 1,
         {"slider": (500, 8000, _D7["largeur"], 0), "nick": u"Largeur de trame"}),
        ("px", "SLIDER", 0, 2,
         {"slider": (50, 600, _D7["pas_x"], 0), "nick": u"Pas en X"}),
        ("py", "SLIDER", 0, 3,
         {"slider": (50, 600, _D7["pas_y"], 0), "nick": u"Pas en Y"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"13,08 et 11,35 : le nombre de modules s'arrondit vers le BAS. "
         u"Arrondir au plus proche donnerait 13 et 11 ici, mais 14 et 12 sur "
         u"une trame à peine plus grande — et vingt-cinq modules hors cadre", [
            ("dx", "Division", 1, 0, {}),
            ("dy", "Division", 1, 3, {}),
            ("fx", "Round", 2, 0, {}),
            ("fy", "Round", 2, 3, {}),
        ]),
        (u"143 modules", [
            ("n", "Multiplication", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("lx", "dx", 0), ("px", "dx", 1),
           ("ly", "dy", 0), ("py", "dy", 1),
           ("dx", "fx", 0), ("dy", "fy", 0),
           ("fx", 0, "n", 0), ("fy", 0, "n", 1),
           ("n", "pan", 0), ("n", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-08 — la série de bonnes réponses
# ---------------------------------------------------------------------------
R["G-08"] = dict(
    sujet=[
        ("v", "DATA:Number", 0, 0,
         {"nick": u"SEIZE_VALEURS", "data": _f(S.D_G08)}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Réponses 1 à 4 — les pairs, le maximum, le minimum, la somme", [
            ("mod", "Modulus", 1, 0, {"val": [(1, "Number", [2])]}),
            ("eq", "Equality", 2, 0, {"val": [(1, "Number", [0])]}),
            ("cu", "Cull Pattern", 3, 0, {}),
            ("np", "List Length", 4, 0, {}),
            ("bo", "Bounds", 1, 3, {}),
            ("dd", "Deconstruct Domain", 2, 3, {}),
            ("so", "Mass Addition", 1, 5, {}),
        ]),
        (u"Réponse 5 — le médian, qui exige un TRI préalable. L'élément de "
         u"rang 8 de la liste brute vaut 857, le médian 404 : c'est là que "
         u"la série se casse", [
            ("tri", "Sort List", 1, 7, {}),
            ("med", "List Item", 2, 7, {"val": [(1, "Integer", [8])]}),
        ]),
        (u"Réponses 6 à 8 — premier plus dernier, le compte au-dessus de "
         u"500, la somme des quatre premières", [
            ("i0", "List Item", 1, 9, {"val": [(1, "Integer", [0])]}),
            ("rv", "Reverse List", 1, 11, {}),
            ("id", "List Item", 2, 11, {"val": [(1, "Integer", [0])]}),
            ("pd", "Addition", 3, 9, {}),
            ("gt", "Larger Than", 1, 13, {"val": [(1, "Number", [500])]}),
            ("cg", "Cull Pattern", 2, 13, {}),
            ("ng", "List Length", 3, 13, {}),
            ("dm", "Construct Domain", 1, 15,
             {"val": [(0, "Number", [0]), (1, "Number", [3])]}),
            ("sl", "Sub List", 2, 15, {}),
            ("s4", "Mass Addition", 3, 15, {}),
        ]),
        (u"Les huit réponses dans l'ordre, multiplicateur maximal", [
            ("m1", "Merge", 5, 0, {}),
            ("m2", "Merge", 5, 3, {}),
            ("m3", "Merge", 5, 6, {}),
            ("m4", "Merge", 5, 9, {}),
            ("m5", "Merge", 6, 0, {}),
            ("m6", "Merge", 6, 6, {}),
            ("m7", "Merge", 7, 0, {}),
            ("pan", "PANEL", 7, 6, {}),
        ]),
    ],
    wires=[("v", "mod", 0), ("mod", "eq", 0),
           ("v", "cu", 0), ("eq", "cu", 1), ("cu", "np", 0),
           ("v", "bo", 0), ("bo", "dd", 0),
           ("v", "so", 0),
           ("v", "tri", 0), ("tri", "med", 0),
           ("v", "i0", 0), ("v", "rv", 0), ("rv", "id", 0),
           ("i0", "pd", 0), ("id", "pd", 1),
           ("v", "gt", 0), ("v", "cg", 0), ("gt", 0, "cg", 1),
           ("cg", "ng", 0),
           ("v", "sl", 0), ("dm", "sl", 1), ("sl", "s4", 0),
           ("np", "m1", 0), ("dd", 1, "m1", 1),
           ("dd", 0, "m2", 0), ("so", "m2", 1),
           ("med", "m3", 0), ("pd", "m3", 1),
           ("ng", "m4", 0), ("s4", "m4", 1),
           ("m1", "m5", 0), ("m2", "m5", 1),
           ("m3", "m6", 0), ("m4", "m6", 1),
           ("m5", "m7", 0), ("m6", "m7", 1),
           ("m7", "pan", 0), ("m7", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-09 — le composant caché
# ---------------------------------------------------------------------------
R["G-09"] = dict(
    sujet=[
        ("v", "DATA:Number", 0, 0,
         {"nick": u"COMPOSANT_MASQUE", "data": _f(S.D_G09)}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le composant est masqué, pas supprimé : Ctrl+A le sélectionne "
         u"comme les autres, et Edit > Arrange le fait ressortir. Sa somme "
         u"vaut 8 538", [
            ("so", "Mass Addition", 1, 0, {}),
            ("pan", "PANEL", 2, 0, {}),
        ]),
    ],
    wires=[("v", "so", 0), ("so", "pan", 0), ("so", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-10 — le coffre à butin
# ---------------------------------------------------------------------------
R["G-10"] = dict(
    sujet=[
        ("v", "DATA:Number", 0, 0,
         {"nick": u"CONTENU_DES_VINGT_COFFRES", "data": _f(S.D_G10)}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le seuil : la troisième valeur en partant du haut, 87. Trier puis "
         u"lire l'avant-avant-dernière", [
            ("tri", "Sort List", 1, 0, {}),
            ("seuil", "List Item", 2, 0,
             {"val": [(1, "Integer", [len(S.D_G10) - 3])]}),
        ]),
        (u"Les coffres qui l'atteignent, et surtout leurs INDEX. Rendre les "
         u"contenus — 87, 95, 93 — au lieu des index est l'erreur : c'est "
         u"l'index qui désigne le coffre dans la trame", [
            ("idx", "Series", 1, 3,
             {"val": [(0, "Number", [0]), (1, "Number", [1]),
                      (2, "Integer", [len(S.D_G10)])]}),
            ("ge", "Larger Than", 3, 0, {}),
            ("cu", "Cull Pattern", 4, 0, {}),
            ("tr2", "Sort List", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("v", "tri", 0), ("tri", "seuil", 0),
           ("v", "ge", 0), ("seuil", "ge", 1),
           ("idx", "cu", 0), ("ge", 1, "cu", 1),
           ("cu", "tr2", 0),
           ("tr2", "pan", 0), ("tr2", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-11 — les mots croisés  (étalon)
# ---------------------------------------------------------------------------
R["G-11"] = dict(
    sujet=[
        ("n", "SLIDER", 0, 0,
         {"slider": (1, 15, len(S.D_G11), 0), "nick": u"Definitions de la grille"}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon porte la longueur de chacun des sept mots : SERIES (6), "
         u"CULL (4), GRAFT (5), DISPATCH (8), WEAVE (5), JITTER (6), "
         u"PARTITION (9). Un nom de composant ne se calcule pas — il se "
         u"sait, et c'est le sujet de l'exercice", [
            ("lg", "DATA:Number", 1, 0,
             {"nick": u"LONGUEUR_DE_CHAQUE_MOT",
              "data": _f([len(m) for m in S.D_G11])}),
        ]),
        (u"43. Écrire SORT (4) pour « produire une suite régulière » au lieu "
         u"de SERIES (6) décale la somme de deux, et la grille ne ferme plus", [
            ("so", "Mass Addition", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("lg", "so", 0), ("so", "pan", 0), ("so", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-12 — le memory  (étalon)
# ---------------------------------------------------------------------------
def _partenaires():
    part = [0] * 13
    for x, y in S.D_G12:
        part[x], part[y] = y, x
    return _f(part[1:])


R["G-12"] = dict(
    sujet=[
        ("n", "SLIDER", 0, 0,
         {"slider": (2, 24, 12, 0), "nick": u"Cartes du memory"}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon donne le partenaire de chaque carte, dans l'ordre des "
         u"cartes. Cette forme est UNIQUE, là où six couples rendus dans un "
         u"ordre libre ne le seraient pas — deux apprenants justes "
         u"rendraient deux listes différentes", [
            ("p", "DATA:Number", 1, 0,
             {"nick": u"PARTENAIRE_DE_CHAQUE_CARTE", "data": _partenaires()}),
            ("pan", "PANEL", 2, 0, {}),
        ]),
    ],
    wires=[("p", "pan", 0), ("p", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-13 — la machine à sous  (étalon)
# ---------------------------------------------------------------------------
R["G-13"] = dict(
    sujet=[
        ("r1", "DATA:Number", 0, 0, {"nick": u"ROULEAU_1", "data": _f(S.D_G13[0])}),
        ("r2", "DATA:Number", 0, 2, {"nick": u"ROULEAU_2", "data": _f(S.D_G13[1])}),
        ("r3", "DATA:Number", 0, 4, {"nick": u"ROULEAU_3", "data": _f(S.D_G13[2])}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le motif 4 est le SEUL présent dans les trois rouleaux, et une "
         u"seule fois dans chacun : la solution est unique. Il occupe les "
         u"positions 2, 1 et 1 ; la ligne centrale est en position 3, d'où "
         u"des décalages de 7, 6 et 6", [
            ("d", "DATA:Number", 1, 0,
             {"nick": u"DECALAGE_DE_CHAQUE_ROULEAU", "data": _f([7, 6, 6])}),
            ("pan", "PANEL", 2, 0, {}),
        ]),
    ],
    wires=[("d", "pan", 0), ("d", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-14 — le puzzle de câblage
# ---------------------------------------------------------------------------
R["G-14"] = dict(
    sujet=[
        ("x", "DATA:Number", 0, 0,
         {"nick": u"SOMMETS_X", "data": _f([p[0] for p in S.D_G14])}),
        ("y", "DATA:Number", 0, 3,
         {"nick": u"SOMMETS_Y", "data": _f([p[1] for p in S.D_G14])}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Six sommets, un point par couple de coordonnées", [
            ("pt", "Construct Point", 1, 0, {}),
        ]),
        (u"La polyligne FERMÉE. Laisser le contour ouvert donne 1 530,00 mm "
         u"au lieu de 2 033,29 : il manque le segment de retour, 503,29 mm — "
         u"un quart de la réponse, invisible à l'aperçu", [
            ("pl", "PolyLine", 2, 0, {"val": [(1, "Boolean", [True])]}),
            ("lg", "Length", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("x", "pt", 0), ("y", "pt", 1),
           ("pt", "pl", 0), ("pl", "lg", 0),
           ("lg", "pan", 0), ("lg", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-15 — le dessin à compléter
# ---------------------------------------------------------------------------
_PLEIN = S.D_G15 + [(-x, y) for x, y in reversed(S.D_G15[1:-1])]

R["G-15"] = dict(
    sujet=[
        ("x", "DATA:Number", 0, 0,
         {"nick": u"DEMI_FIGURE_X", "data": _f([p[0] for p in S.D_G15])}),
        ("y", "DATA:Number", 0, 3,
         {"nick": u"DEMI_FIGURE_Y", "data": _f([p[1] for p in S.D_G15])}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"La figure complétée : dix sommets et non douze. Les deux points "
         u"posés SUR l'axe ne se recopient pas — les redoubler laisse l'aire "
         u"inchangée mais allonge le périmètre, ce que le contrôle croisé "
         u"attrape", [
            ("x2", "DATA:Number", 1, 0,
             {"nick": u"FIGURE_COMPLETE_X", "data": _f([p[0] for p in _PLEIN])}),
            ("y2", "DATA:Number", 1, 3,
             {"nick": u"FIGURE_COMPLETE_Y", "data": _f([p[1] for p in _PLEIN])}),
            ("pt", "Construct Point", 2, 0, {}),
            ("pl", "PolyLine", 3, 0, {"val": [(1, "Boolean", [True])]}),
        ]),
        (u"91 550 mm² et 1 098,42 mm. Les deux mesures ensemble : le "
         u"périmètre seul ne distingue pas une symétrie d'une translation", [
            ("ai", "Area", 4, 0, {}),
            ("lg", "Length", 4, 3, {}),
            ("me", "Merge", 5, 0, {}),
            ("pan", "PANEL", 5, 4, {}),
        ]),
    ],
    wires=[("x2", "pt", 0), ("y2", "pt", 1),
           ("pt", "pl", 0),
           ("pl", "ai", 0), ("pl", "lg", 0),
           ("ai", 0, "me", 0), ("lg", "me", 1),
           ("me", "pan", 0), ("me", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-16 — la chasse au trésor
# ---------------------------------------------------------------------------
_LX, _LY, _LZ = S.D_G16_VOLUME

R["G-16"] = dict(
    sujet=[
        ("x", "DATA:Number", 0, 0, {"nick": u"POINTS_X", "data": _f(S.D_G16_X)}),
        ("y", "DATA:Number", 0, 3, {"nick": u"POINTS_Y", "data": _f(S.D_G16_Y)}),
        ("z", "DATA:Number", 0, 6, {"nick": u"POINTS_Z", "data": _f(S.D_G16_Z)}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Un test par axe : le point sort-il du volume 2 000 × 1 200 × 800 ? "
         u"Chercher le plus ÉLOIGNÉ DU CENTRE désignerait un coin "
         u"parfaitement légitime — la méthode paraît raisonnable et donne un "
         u"index faux", [
            ("gx", "Larger Than", 1, 0, {"val": [(1, "Number", [_LX])]}),
            ("gy", "Larger Than", 1, 3, {"val": [(1, "Number", [_LY])]}),
            ("gz", "Larger Than", 1, 6, {"val": [(1, "Number", [_LZ])]}),
        ]),
        (u"Un OU entre les trois : il suffit de sortir sur un axe", [
            ("o1", "Gate Or", 2, 0, {}),
            ("o2", "Gate Or", 3, 0, {}),
        ]),
        (u"L'index 337. `Cull Pattern` sur la série des index garde celui "
         u"des points retenus", [
            ("idx", "Series", 2, 6,
             {"val": [(0, "Number", [0]), (1, "Number", [1]),
                      (2, "Integer", [len(S.D_G16_X)])]}),
            ("cu", "Cull Pattern", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("x", "gx", 0), ("y", "gy", 0), ("z", "gz", 0),
           ("gx", 0, "o1", 0), ("gy", 0, "o1", 1),
           ("o1", "o2", 0), ("gz", 0, "o2", 1),
           ("idx", "cu", 0), ("o2", "cu", 1),
           ("cu", "pan", 0), ("cu", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-17, G-18, G-19 — les jeux de connaissance  (étalons)
# ---------------------------------------------------------------------------
R["G-17"] = dict(
    sujet=[
        ("n", "SLIDER", 0, 0,
         {"slider": (1, 20, len(S.D_G17), 0), "nick": u"Questions du quiz"}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Les dix rangs. Ils se répartissent sur les quatre propositions — "
         u"trois fois le rang 3, deux fois le 1, deux fois le 2, une fois le "
         u"4 — de sorte qu'aucune stratégie de rang constant ne dépasse trois "
         u"points sur dix", [
            ("v", "DATA:Number", 1, 0,
             {"nick": u"RANG_DE_LA_BONNE_REPONSE",
              "data": _f([q[2] for q in S.D_G17])}),
            ("pan", "PANEL", 2, 0, {}),
        ]),
    ],
    wires=[("v", "pan", 0), ("v", "rep", 0)],
)

R["G-18"] = dict(
    sujet=[
        ("n", "SLIDER", 0, 0,
         {"slider": (1, 30, len(S.D_G18), 0), "nick": u"Affirmations"}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Les huit affirmations vraies, par leur rang. Huit sur quinze : ni "
         u"la majorité ni la moitié, de sorte que répondre uniformément ne "
         u"rapporte rien", [
            ("v", "DATA:Number", 1, 0,
             {"nick": u"AFFIRMATIONS_VRAIES",
              "data": _f([i + 1 for i, (_t, ok) in enumerate(S.D_G18) if ok])}),
            ("pan", "PANEL", 2, 0, {}),
        ]),
    ],
    wires=[("v", "pan", 0), ("v", "rep", 0)],
)

R["G-19"] = dict(
    sujet=[
        ("j", "DATA:Number", 0, 0,
         {"nick": u"JEU_DE_PREUVE", "data": _f(S.D_G19)}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Les quatre clusters reproduisent : un comptage au-dessus de 50, "
         u"la somme des trois plus grandes, l'index du maximum, le nombre de "
         u"restes distincts modulo 7. Nommer le composant sans le vérifier "
         u"sur ce second jeu est l'erreur : trois composants différents se "
         u"comportent à l'identique sur les données de test", [
            ("v", "DATA:Number", 1, 0,
             {"nick": u"RESULTAT_DE_CHAQUE_CLUSTER",
              "data": _f([len([x for x in S.D_G19 if x > 50]),
                          sum(sorted(S.D_G19)[-3:]),
                          S.D_G19.index(max(S.D_G19)),
                          len(set(x % 7 for x in S.D_G19))])}),
            ("pan", "PANEL", 2, 0, {}),
        ]),
    ],
    wires=[("v", "pan", 0), ("v", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-20 — la chasse aux bugs
# ---------------------------------------------------------------------------
_D20 = S.D_G20
R["G-20"] = dict(
    sujet=[
        ("nx", "SLIDER", 0, 0,
         {"slider": (1, 20, _D20["nx"], 0), "nick": u"Modules en X"}),
        ("ny", "SLIDER", 0, 1,
         {"slider": (1, 20, _D20["ny"], 0), "nick": u"Modules en Y"}),
        ("c", "SLIDER", 0, 2,
         {"slider": (50, 800, _D20["cote"], 0), "nick": u"Cote du module"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Vingt-quatre modules retrouvés — le compte est annoncé dans "
         u"l'énoncé et ne prouve donc rien", [
            ("n", "Multiplication", 1, 0, {}),
        ]),
        (u"C'est l'AIRE qui est l'indicateur : 2 306 400 mm². Empiler quatre "
         u"fois la même rangée au même endroit donnerait vingt-quatre objets "
         u"et la bonne aire — mais la définition resterait fausse, et le "
         u"canvas le dirait", [
            ("a", "Multiplication", 1, 3, {}),
            ("t", "Multiplication", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("nx", "n", 0), ("ny", "n", 1),
           ("c", "a", 0), ("c", "a", 1),
           ("n", "t", 0), ("a", "t", 1),
           ("t", "pan", 0), ("t", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-21 — le golf de composants
# ---------------------------------------------------------------------------
_D21 = S.D_G21


def _etoile():
    n = _D21["dents"]
    xs, ys = [], []
    for i in range(2 * n):
        a = 2 * math.pi * i / (2 * n)
        r = _D21["rayon"] if i % 2 == 0 else _D21["rayon"] - _D21["creux"]
        xs.append(r * math.cos(a))
        ys.append(r * math.sin(a))
    return xs, ys


_EX, _EY = _etoile()

R["G-21"] = dict(
    sujet=[
        ("r", "SLIDER", 0, 0,
         {"slider": (50, 600, _D21["rayon"], 0), "nick": u"Rayon exterieur"}),
        ("d", "SLIDER", 0, 1,
         {"slider": (3, 20, _D21["dents"], 0), "nick": u"Branches"}),
        ("c", "SLIDER", 0, 2,
         {"slider": (5, 200, _D21["creux"], 0), "nick": u"Profondeur du creux"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Dix-huit sommets, alternant rayon extérieur et rayon de creux. "
         u"`Polygon` en mode étoile les produit en UN composant ; les poser "
         u"segment par segment en demande dix-huit, pour un par de sept", [
            ("x", "DATA:Number", 1, 0, {"nick": u"SOMMETS_X", "data": _f(_EX)}),
            ("y", "DATA:Number", 1, 3, {"nick": u"SOMMETS_Y", "data": _f(_EY)}),
            ("pt", "Construct Point", 2, 0, {}),
        ]),
        (u"1 582,75 mm de périmètre. Neuf branches : nombre impair, donc "
         u"aucun axe de symétrie horizontal — l'étoile ne se construit pas "
         u"par miroir", [
            ("pl", "PolyLine", 3, 0, {"val": [(1, "Boolean", [True])]}),
            ("lg", "Length", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("x", "pt", 0), ("y", "pt", 1),
           ("pt", "pl", 0), ("pl", "lg", 0),
           ("lg", "pan", 0), ("lg", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-22 — le boss de fin de chapitre
# ---------------------------------------------------------------------------
R["G-22"] = dict(
    sujet=[
        ("v", "DATA:Number", 0, 0,
         {"nick": u"DEUX_CENT_QUARANTE_VALEURS", "data": _f(S.D_G22)}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Phase 1 — huit branches PAR PAS DE HUIT, et non huit tranches "
         u"consécutives. `Partition List` par 8 puis `Flip Matrix` : la "
         u"première branche prend les valeurs 0, 8, 16… Les deux découpages "
         u"donnent bien huit branches de trente, et les comptes filtrés "
         u"n'ont plus rien à voir", [
            ("pa", "Partition List", 1, 0,
             {"val": [(1, "Integer", [S.D_G22_BRANCHES])]}),
            ("fl", "Flip Matrix", 2, 0, {}),
        ]),
        (u"Phase 2 — deux conditions combinées : au-dessus de 400 ET "
         u"multiple de 3", [
            ("gt", "Larger Than", 3, 0, {"val": [(1, "Number", [400])]}),
            ("mo", "Modulus", 3, 3, {"val": [(1, "Number", [3])]}),
            ("eq", "Equality", 4, 3, {"val": [(1, "Number", [0])]}),
            ("et", "Gate And", 5, 0, {}),
            ("cu", "Cull Pattern", 6, 0, {}),
        ]),
        (u"Phase 3 — le tableau : huit comptes, puis huit sommes. Les "
         u"comptes vont de 4 à 10, les sommes de 3 150 à 7 818 : aucune "
         u"colonne ne peut se confondre avec une autre", [
            ("nb", "List Length", 7, 0, {}),
            ("so", "Mass Addition", 7, 3, {}),
            ("fn", "Flatten Tree", 8, 0, {}),
            ("fs", "Flatten Tree", 8, 3, {}),
            ("me", "Merge", 9, 0, {}),
            ("pan", "PANEL", 9, 4, {}),
        ]),
    ],
    wires=[("v", "pa", 0), ("pa", "fl", 0),
           ("fl", "gt", 0), ("fl", "mo", 0), ("mo", "eq", 0),
           ("gt", 0, "et", 0), ("eq", 0, "et", 1),
           ("fl", "cu", 0), ("et", "cu", 1),
           ("cu", "nb", 0), ("cu", "so", 0),
           ("nb", "fn", 0), ("so", "fs", 0),
           ("fn", "me", 0), ("fs", "me", 1),
           ("me", "pan", 0), ("me", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-23 — le duel
# ---------------------------------------------------------------------------
R["G-23"] = dict(
    sujet=[
        ("q", "DATA:Number", 0, 0,
         {"nick": u"QUANTITES", "data": _f([q for _n, q in S.D_G23])}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Trier par QUANTITÉ, puis inverser. Trier par désignation — ce que "
         u"`Sort List` fait sur des textes — donne 6, 18, 9, 14, 31, 44, 27, "
         u"22 : huit lignes parfaitement présentables, et un classement faux", [
            ("tri", "Sort List", 1, 0, {}),
            ("rv", "Reverse List", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("q", "tri", 0), ("tri", "rv", 0),
           ("rv", "pan", 0), ("rv", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-24 — le retour sonore
# ---------------------------------------------------------------------------
R["G-24"] = dict(
    sujet=[
        ("v", "DATA:Number", 0, 0,
         {"nick": u"QUATRE_VINGTS_VALEURS", "data": _f(S.D_G24)}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Condition 1 — multiple de 4. Condition 2 — au-dessus de 120", [
            ("m4", "Modulus", 1, 0, {"val": [(1, "Number", [4])]}),
            ("e4", "Equality", 2, 0, {"val": [(1, "Number", [0])]}),
            ("gt", "Larger Than", 1, 3, {"val": [(1, "Number", [120])]}),
        ]),
        (u"Condition 3 — le dernier chiffre vaut 0, 4 ou 8 : le reste "
         u"modulo 10. Tout multiple de 4 finit par 0, 2, 4, 6 ou 8 — cette "
         u"condition écarte les deux derniers cas", [
            ("m10", "Modulus", 1, 5, {"val": [(1, "Number", [10])]}),
            ("z0", "Equality", 2, 5, {"val": [(1, "Number", [0])]}),
            ("z4", "Equality", 2, 7, {"val": [(1, "Number", [4])]}),
            ("z8", "Equality", 2, 9, {"val": [(1, "Number", [8])]}),
            ("ou1", "Gate Or", 3, 5, {}),
            ("ou2", "Gate Or", 4, 5, {}),
        ]),
        (u"Les trois par un ET, jamais par un OU. Un OU retiendrait 71 "
         u"valeurs sur 80 : le son de victoire retentirait presque toujours, "
         u"et deviendrait inaudible", [
            ("et1", "Gate And", 5, 0, {}),
            ("et2", "Gate And", 6, 0, {}),
            ("cu", "Cull Pattern", 7, 0, {}),
            ("nb", "List Length", 8, 0, {}),
            ("pan", "PANEL", 8, 4, {}),
        ]),
    ],
    wires=[("v", "m4", 0), ("m4", "e4", 0),
           ("v", "gt", 0),
           ("v", "m10", 0), ("m10", "z0", 0), ("m10", "z4", 0), ("m10", "z8", 0),
           ("z0", 0, "ou1", 0), ("z4", 0, "ou1", 1),
           ("ou1", "ou2", 0), ("z8", 0, "ou2", 1),
           ("e4", 0, "et1", 0), ("gt", 0, "et1", 1),
           ("et1", "et2", 0), ("ou2", "et2", 1),
           ("v", "cu", 0), ("et2", "cu", 1),
           ("cu", "nb", 0),
           ("nb", "pan", 0), ("nb", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-25 — l'animation de la solution
# ---------------------------------------------------------------------------
R["G-25"] = dict(
    sujet=[
        ("v", "DATA:Number", 0, 0,
         {"nick": u"LONGUEUR_DES_QUARANTE_BARRES", "data": _f(S.D_G25)}),
        ("t", "SLIDER", 0, 4,
         {"slider": (0, 1, S.D_G25_T, 3), "nick": u"Avancement de l'animation"}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Les barres apparaissent de la plus courte à la plus longue : on "
         u"trie d'abord", [
            ("tri", "Sort List", 1, 0, {}),
        ]),
        (u"Le nombre visible à t : quinze barres sur quarante", [
            ("nt", "Multiplication", 1, 4,
             {"val": [(1, "Number", [float(len(S.D_G25))])]}),
            ("rd", "Round", 2, 4, {}),
            ("m1", "Subtraction", 3, 4, {"val": [(1, "Number", [1])]}),
            ("dm", "Construct Domain", 4, 4, {"val": [(0, "Number", [0])]}),
        ]),
        (u"8 508 mm cumulés, soit 19 % de la longueur pour 37,5 % des "
         u"barres. Un cumul proportionnel au temps — 16 510 mm — signalerait "
         u"une révélation dans le désordre. C'est l'état INTERMÉDIAIRE qui "
         u"prouve le pilotage : à t = 1, toute animation affiche les quarante", [
            ("sl", "Sub List", 5, 0, {}),
            ("so", "Mass Addition", 6, 0, {}),
            ("pan", "PANEL", 6, 4, {}),
        ]),
    ],
    wires=[("v", "tri", 0),
           ("t", "nt", 0), ("nt", "rd", 0), ("rd", 2, "m1", 0),
           ("m1", "dm", 1),
           ("tri", "sl", 0), ("dm", "sl", 1),
           ("sl", "so", 0),
           ("so", "pan", 0), ("so", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-26 — le retour visuel immédiat
# ---------------------------------------------------------------------------
_B26, _H26 = S.D_G26_BORNES
R["G-26"] = dict(
    sujet=[
        ("v", "DATA:Number", 0, 0,
         {"nick": u"LONGUEUR_DES_VINGT_PIECES", "data": _f(S.D_G26)}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Une tolérance a DEUX bornes. Ne tester que les pièces trop "
         u"courtes en compte 5 au lieu de 8 : trois pièces dépassent 900 mm "
         u"et passeraient en vert", [
            ("pe", "Smaller Than", 1, 0, {"val": [(1, "Number", [_B26])]}),
            ("gr", "Larger Than", 1, 3, {"val": [(1, "Number", [_H26])]}),
        ]),
        (u"8 pièces non conformes", [
            ("ou", "Gate Or", 2, 0, {}),
            ("cu", "Cull Pattern", 3, 0, {}),
            ("nb", "List Length", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("v", "pe", 0), ("v", "gr", 0),
           ("pe", 0, "ou", 0), ("gr", 0, "ou", 1),
           ("v", "cu", 0), ("ou", "cu", 1),
           ("cu", "nb", 0),
           ("nb", "pan", 0), ("nb", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-27 — la savane paramétrique
# ---------------------------------------------------------------------------
_D27 = S.D_G27
R["G-27"] = dict(
    sujet=[
        ("r", "SLIDER", 0, 0,
         {"slider": (200, 4000, _D27["rayon_abreuvoir"], 0),
          "nick": u"Rayon de l'abreuvoir"}),
        ("e", "SLIDER", 0, 1,
         {"slider": (100, 3000, _D27["ecart"], 0), "nick": u"Ecart au bord"}),
        ("n", "SLIDER", 0, 2,
         {"slider": (3, 24, _D27["animaux"], 0), "nick": u"Animaux de la harde"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Les animaux se tiennent à 950 mm DU BORD, pas du centre : leur "
         u"cercle a pour rayon 1 800 + 950 = 2 750. Les poser sur le cercle "
         u"de l'abreuvoir donnerait 11 180,98 mm — et douze animaux les pieds "
         u"dans l'eau", [
            ("rh", "Addition", 1, 0, {}),
        ]),
        (u"Le côté d'un polygone régulier à n sommets : 2R·sin(π/n)", [
            ("pi", "Pi", 1, 3, {"val": [(0, "Number", [1])]}),
            ("an", "Division", 2, 3, {}),
            ("si", "Sine", 3, 3, {}),
            ("d2", "Multiplication", 2, 0, {"val": [(1, "Number", [2])]}),
            ("co", "Multiplication", 4, 0, {}),
        ]),
        (u"17 082,06 mm — le périmètre de la harde", [
            ("pe", "Multiplication", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("r", "rh", 0), ("e", "rh", 1),
           ("pi", "an", 0), ("n", "an", 1), ("an", "si", 0),
           ("rh", "d2", 0),
           ("d2", "co", 0), ("si", "co", 1),
           ("co", "pe", 0), ("n", "pe", 1),
           ("pe", "pan", 0), ("pe", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-28 — l'avatar paramétrique
# ---------------------------------------------------------------------------
_D28 = S.D_G28
R["G-28"] = dict(
    sujet=[
        ("f", "SLIDER", 0, 0,
         {"slider": (1, 10, _D28["formes"], 0), "nick": u"Formes de corps"}),
        ("m", "SLIDER", 0, 1,
         {"slider": (1, 10, _D28["motifs"], 0), "nick": u"Motifs"}),
        ("c", "SLIDER", 0, 2,
         {"slider": (1, 12, _D28["couleurs"], 0), "nick": u"Couleurs"}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le code vaut forme×100 + motif×10 + couleur. Sur les 72 "
         u"combinaisons, chaque forme revient 4 × 6 = 24 fois, chaque motif "
         u"3 × 6 = 18 fois, chaque couleur 3 × 4 = 12 fois", [
            ("mc", "Multiplication", 1, 0, {}),
            ("fc", "Multiplication", 1, 3, {}),
            ("fm", "Multiplication", 1, 6, {}),
        ]),
        (u"La somme des rangs de 1 à n vaut n(n+1)/2 : 6 pour les formes, 10 "
         u"pour les motifs, 21 pour les couleurs", [
            ("f1", "Addition", 2, 0, {"val": [(1, "Number", [1])]}),
            ("sf", "Multiplication", 3, 0, {}),
            ("df", "Division", 4, 0, {"val": [(1, "Number", [2])]}),
            ("m1", "Addition", 2, 3, {"val": [(1, "Number", [1])]}),
            ("sm", "Multiplication", 3, 3, {}),
            ("dm", "Division", 4, 3, {"val": [(1, "Number", [2])]}),
            ("c1", "Addition", 2, 6, {"val": [(1, "Number", [1])]}),
            ("sc", "Multiplication", 3, 6, {}),
            ("dc", "Division", 4, 6, {"val": [(1, "Number", [2])]}),
        ]),
        (u"16 452. Vérifier son avatar sur la seule combinaison choisie ne "
         u"prouve rien : un codage qui casse sur 3-4-6 passe tous les "
         u"contrôles visuels", [
            ("pf", "Multiplication", 5, 0, {}),
            ("cf", "Multiplication", 6, 0, {"val": [(1, "Number", [100])]}),
            ("pm", "Multiplication", 5, 3, {}),
            ("cm", "Multiplication", 6, 3, {"val": [(1, "Number", [10])]}),
            ("pc", "Multiplication", 5, 6, {}),
            ("t1", "Addition", 7, 0, {}),
            ("t2", "Addition", 8, 0, {}),
            ("pan", "PANEL", 8, 4, {}),
        ]),
    ],
    wires=[("m", "mc", 0), ("c", "mc", 1),
           ("f", "fc", 0), ("c", "fc", 1),
           ("f", "fm", 0), ("m", "fm", 1),
           ("f", "f1", 0), ("f", "sf", 0), ("f1", "sf", 1), ("sf", "df", 0),
           ("m", "m1", 0), ("m", "sm", 0), ("m1", "sm", 1), ("sm", "dm", 0),
           ("c", "c1", 0), ("c", "sc", 0), ("c1", "sc", 1), ("sc", "dc", 0),
           ("df", "pf", 0), ("mc", "pf", 1), ("pf", "cf", 0),
           ("dm", "pm", 0), ("fc", "pm", 1), ("pm", "cm", 0),
           ("dc", "pc", 0), ("fm", "pc", 1),
           ("cf", "t1", 0), ("cm", "t1", 1),
           ("t1", "t2", 0), ("pc", "t2", 1),
           ("t2", "pan", 0), ("t2", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-29 — le défi du jour
# ---------------------------------------------------------------------------
R["G-29"] = dict(
    sujet=[
        ("v", "DATA:Number", 0, 0,
         {"nick": u"PIECES_DU_JOUR", "data": _f(S.D_G29)}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Quarante-et-une pièces : un nombre IMPAIR, donc la médiane est "
         u"une valeur réellement présente dans la liste — celle de rang 20 "
         u"après tri", [
            ("tri", "Sort List", 1, 0, {}),
            ("it", "List Item", 2, 0,
             {"val": [(1, "Integer", [len(S.D_G29) // 2])]}),
        ]),
        (u"1 119 mm. La moyenne, 1 203 mm, répond à la même question et "
         u"diffère de 84 mm : assez pour fausser un débit, pas assez pour "
         u"alerter", [
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("v", "tri", 0), ("tri", "it", 0),
           ("it", "pan", 0), ("it", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-30 — le relais à deux
# ---------------------------------------------------------------------------
_PAR30 = len(S.D_G30) // S.D_G30_BRANCHES
R["G-30"] = dict(
    sujet=[
        ("v", "DATA:Number", 0, 0,
         {"nick": u"QUATRE_VINGT_SEIZE_VALEURS", "data": _f(S.D_G30)}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Première moitié — six branches de seize. C'est le point de "
         u"passage : ce que le binôme reprend", [
            ("pa", "Partition List", 1, 0,
             {"val": [(1, "Integer", [_PAR30])]}),
        ]),
        (u"Seconde moitié — dans CHAQUE branche, on trie puis on écarte deux "
         u"valeurs hautes et deux basses. Les écarter sur l'ensemble des 96 "
         u"avant de répartir est l'autre lecture, défendable à l'oral et "
         u"fausse ici : c'est exactement l'ambiguïté qu'un relais révèle", [
            ("tri", "Sort List", 2, 0, {}),
            ("dm", "Construct Domain", 2, 4,
             {"val": [(0, "Number", [S.D_G30_ECARTES]),
                      (1, "Number", [_PAR30 - S.D_G30_ECARTES - 1])]}),
            ("sl", "Sub List", 3, 0, {}),
            ("mo", "Average", 4, 0, {}),
        ]),
        (u"2 904,3333 — la somme des six moyennes. Sans `Flatten Tree`, "
         u"`Mass Addition` rendrait SIX sommes, une par branche : il somme "
         u"ce que chaque branche contient, et chacune n'en contient qu'une", [
            ("fl", "Flatten Tree", 5, 0, {}),
            ("so", "Mass Addition", 6, 0, {}),
            ("pan", "PANEL", 7, 0, {}),
        ]),
    ],
    wires=[("v", "pa", 0), ("pa", "tri", 0),
           ("tri", "sl", 0), ("dm", "sl", 1),
           ("sl", "mo", 0), ("mo", "fl", 0), ("fl", "so", 0),
           ("so", "pan", 0), ("so", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-31 — l'arbre de compétences
# ---------------------------------------------------------------------------
R["G-31"] = dict(
    sujet=[
        ("p", "DATA:Number", 0, 0,
         {"nick": u"EXERCICES_PORTES", "data": _f(S.D_G31_PORTE)}),
        ("q", "DATA:Number", 0, 3,
         {"nick": u"EXERCICES_VALIDES", "data": _f(S.D_G31_VALIDE)}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Une notion est COMPLÈTE quand les validés atteignent les portés — "
         u"« au moins », et non « exactement » : une notion peut avoir plus "
         u"de validés que d'exercices portés, cas réel d'un exercice retiré "
         u"du référentiel", [
            ("ge", "Larger Than", 1, 0, {}),
        ]),
        (u"21 notions sur 48, soit 44 %. Compter les notions ENTAMÉES — au "
         u"moins un exercice validé — en donnerait 37, et l'arbre paraîtrait "
         u"aux trois quarts vert", [
            ("cu", "Cull Pattern", 2, 0, {}),
            ("nb", "List Length", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("q", "ge", 0), ("p", "ge", 1),
           ("q", "cu", 0), ("ge", 1, "cu", 1),
           ("cu", "nb", 0),
           ("nb", "pan", 0), ("nb", "rep", 0)],
)


# ---------------------------------------------------------------------------
# G-32 — les indices payants
# ---------------------------------------------------------------------------
_PAR32 = len(S.D_G32) // S.D_G32_BRANCHES
R["G-32"] = dict(
    sujet=[
        ("v", "DATA:Number", 0, 0,
         {"nick": u"ARBRE_SOURCE", "data": _f(S.D_G32)}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Neuf branches de huit, puis les multiples de 5 de chacune", [
            ("pa", "Partition List", 1, 0,
             {"val": [(1, "Integer", [_PAR32])]}),
            ("mo", "Modulus", 2, 0, {"val": [(1, "Number", [5])]}),
            ("eq", "Equality", 3, 0, {"val": [(1, "Number", [0])]}),
            ("cu", "Cull Pattern", 4, 0, {}),
        ]),
        (u"La structure se décrit par les EFFECTIFS de ses branches, pas par "
         u"les valeurs retenues : 4, 1, 0, 3, 2, 2, 3, 2, 2. Une branche est "
         u"vide — c'est elle qui vérifie qu'on ne supprime pas les branches "
         u"sans contenu", [
            ("nb", "List Length", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("v", "pa", 0), ("pa", "mo", 0), ("mo", "eq", 0),
           ("pa", "cu", 0), ("eq", 0, "cu", 1),
           ("cu", "nb", 0),
           ("nb", "pan", 0), ("nb", "rep", 0)],
)
