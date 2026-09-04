# -*- coding: utf-8 -*-
"""Recettes de construction - LOT A, exercices A-14 a A-26."""

from recipes_a1 import DOUZE, VINGT

R = {}

# huit points repartis sur un cercle de rayon 100 (octogone)
OCTO = [(100.0, 0.0, 0), (70.711, 70.711, 0), (0.0, 100.0, 0), (-70.711, 70.711, 0),
        (-100.0, 0.0, 0), (-70.711, -70.711, 0), (0.0, -100.0, 0), (70.711, -70.711, 0)]

TRIO_A = [(0, 0, 0), (0, 80, 0), (0, 160, 0)]
TRIO_B = [(200, 0, 0), (200, 80, 0), (200, 160, 0)]

R["A-14"] = dict(
    sujet=[
        ("data", "DATA:Number", 0, 0, {"nick": "VALEURS", "data": DOUZE}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Saisir le motif sur trois lignes distinctes du Panel", [
            ("pat", "PANEL", 1, 1, {"text": "True\nFalse\nFalse", "h": 76}),
        ]),
        (u"Le motif se répète cycliquement sur toute la liste", [
            ("cull", "Cull Pattern", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("data", "cull", 0), ("pat", "cull", 1),
           ("cull", "pan", 0), ("cull", "rep", 0)],
)

R["A-15"] = dict(
    sujet=[
        ("data", "DATA:Number", 0, 0, {"nick": "VALEURS", "data": VINGT}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Comparer au seuil : la sortie >= inclut la valeur 50", [
            ("sl", "SLIDER", 1, 1, {"slider": (0, 100, 50, 0), "nick": "Seuil"}),
            ("lt", "Larger Than", 2, 1, {}),
        ]),
        (u"Répartir : la sortie A reçoit les True, la sortie B les False", [
            ("disp", "Dispatch", 3, 0, {}),
            ("pan1", "PANEL", 4, 0, {}),
            ("pan2", "PANEL", 4, 1, {}),
        ]),
    ],
    wires=[("data", "lt", 0), ("sl", "lt", 1),
           ("data", "disp", 0), ("lt", 1, "disp", 1),
           ("disp", 0, "pan1", 0), ("disp", 1, "pan2", 0),
           ("disp", 0, "rep", 0)],
)

R["A-16"] = dict(
    sujet=[
        ("pts", "DATA:Point", 0, 0, {"nick": "POINTS_OCTOGONE", "data": OCTO}),
        ("rep", "REPONSE", 4, 0, {"type": "Curve"}),
    ],
    corrige=[
        (u"Décaler la liste d'un cran, l'option Wrap ramenant le dernier au début", [
            ("sh", "Shift List", 1, 1, {"val": [(1, "Integer", [1]),
                                                (2, "Boolean", [True])]}),
        ]),
        (u"Un seul composant Line relie chaque point à son suivant", [
            ("ln", "Curve/Primitive/Line", 2, 0, {}),
        ]),
    ],
    wires=[("pts", "sh", 0), ("pts", "ln", 0), ("sh", "ln", 1), ("ln", "rep", 0)],
)

R["A-17"] = dict(
    sujet=[
        ("l1", "DATA:Text", 0, 0, {"nick": "LISTE_1", "data": ["A", "B", "C"]}),
        ("l2", "DATA:Text", 0, 1, {"nick": "LISTE_2", "data": ["1", "2", "3"]}),
        ("rep", "REPONSE", 4, 0, {"type": "Text"}),
    ],
    corrige=[
        (u"Weave alterne les deux flux selon le motif par défaut 0, 1", [
            ("wv", "Weave", 1, 0, {}),
            ("pan1", "PANEL", 2, 0, {}),
        ]),
        (u"Merge, lui, concatènerait bout à bout : A B C 1 2 3", [
            ("mg", "Merge", 1, 2, {}),
            ("pan2", "PANEL", 2, 2, {}),
        ]),
    ],
    wires=[("l1", "wv", 1), ("l2", "wv", 2), ("wv", "pan1", 0), ("wv", "rep", 0),
           ("l1", "mg", 0), ("l2", "mg", 1), ("mg", "pan2", 0)],
)

R["A-18"] = dict(
    sujet=[
        ("data", "DATA:Number", 0, 0, {"nick": "VALEURS", "data": VINGT}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Construire le domaine d'index : les deux bornes sont incluses", [
            ("cd", "Construct Domain", 1, 1, {"val": [(0, "Number", [5]),
                                                      (1, "Number", [12])]}),
        ]),
        (u"Prélever la portion de liste", [
            ("sub", "Sub List", 2, 0, {}),
        ]),
        (u"Vérifier : huit éléments, et non sept", [
            ("ll", "List Length", 3, 1, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("data", "sub", 0), ("cd", "sub", 1), ("sub", "ll", 0),
           ("sub", "pan", 0), ("sub", "rep", 0)],
)

R["A-19"] = dict(
    sujet=[
        ("tree", "DATA:Number", 0, 0,
         {"nick": "ARBRE", "data": [[11, 12, 13], [21, 22, 23], [31, 32, 33], [41, 42, 43]]}),
        ("rep", "REPONSE", 5, 0, {"type": "Text"}),
    ],
    corrige=[
        (u"Tree Statistics : la sortie P donne la liste des chemins", [
            ("ts", "Tree Statistics", 1, 0, {}),
        ]),
        (u"Compter les chemins donne le nombre de branches", [
            ("ll", "List Length", 2, 0, {}),
        ]),
        (u"Le troisième chemin est à l'index 2", [
            ("li", "List Item", 2, 2, {"val": [(1, "Integer", [2])]}),
        ]),
        (u"Assembler les deux réponses", [
            ("mg", "Merge", 3, 1, {}),
            ("pan", "PANEL", 4, 1, {}),
        ]),
    ],
    wires=[("tree", "ts", 0), ("ts", 0, "ll", 0), ("ts", 0, "li", 0),
           ("ll", "mg", 0), ("li", "mg", 1), ("mg", "pan", 0), ("mg", "rep", 0)],
)

R["A-20"] = dict(
    sujet=[
        ("ptsA", "DATA:Point", 0, 0, {"nick": "POINTS_A", "data": TRIO_A}),
        ("ptsB", "DATA:Point", 0, 1, {"nick": "POINTS_B", "data": TRIO_B}),
        ("ln", "Curve/Primitive/Line", 1, 0, {"nick": "3 segments"}),
        ("rep", "REPONSE", 4, 0, {"type": "Curve"}),
    ],
    corrige=[
        (u"Grafter l'entrée A : chaque point part dans sa propre branche", [
            ("ln2", "Curve/Primitive/Line", 1, 0, {"graft": 0, "nick": "9 segments"}),
        ]),
        (u"Chaque branche de A est croisée avec la liste complète de B", [
            ("pv", "Param Viewer", 2, 0, {}),
        ]),
        (u"Un Flatten ramènerait les 9 segments dans une seule liste", [
            ("fl", "Flatten Tree", 2, 2, {}),
            ("ll", "List Length", 3, 2, {}),
            ("pan", "PANEL", 4, 2, {}),
        ]),
    ],
    wires=[("ptsA", "ln", 0), ("ptsB", "ln", 1),
           ("ptsA", "ln2", 0), ("ptsB", "ln2", 1),
           ("ln2", "pv", 0), ("ln2", "fl", 0), ("fl", "ll", 0), ("ll", "pan", 0),
           ("ln2", "rep", 0)],
)

R["A-21"] = dict(
    sujet=[
        ("tree", "DATA:Number", 0, 0,
         {"nick": "ARBRE_PROFOND",
          "data": [("0;0;0;0", [1, 2]), ("0;0;0;1", [3, 4]),
                   ("0;0;0;2", [5, 6]), ("0;0;0;3", [7, 8])]}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Lire les chemins de départ : {0;0;0;n}", [
            ("pv1", "Param Viewer", 1, 1, {}),
        ]),
        (u"Simplify supprime les niveaux communs à toutes les branches", [
            ("si", "Simplify Tree", 2, 0, {}),
            ("pv2", "Param Viewer", 3, 0, {}),
        ]),
        (u"Trim Tree, lui, supprimerait le dernier niveau et fusionnerait les branches", [
            ("tt", "Trim Tree", 2, 2, {}),
            ("pv3", "Param Viewer", 3, 2, {}),
        ]),
    ],
    wires=[("tree", "pv1", 0), ("tree", "si", 0), ("si", "pv2", 0),
           ("tree", "tt", 0), ("tt", "pv3", 0), ("si", "rep", 0)],
)

R["A-22"] = dict(
    sujet=[
        ("l1", "DATA:Number", 0, 0, {"nick": "LISTE_1", "data": [10, 20]}),
        ("l2", "DATA:Number", 0, 1, {"nick": "LISTE_2", "data": [1, 2, 3, 4, 5]}),
        ("l3", "DATA:Number", 0, 2, {"nick": "LISTE_3", "data": [100, 200, 300]}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Entwine assemble les listes en autant de branches", [
            ("ent", "Entwine", 1, 1, {"inputs": 3}),
            ("pv", "Param Viewer", 2, 1, {}),
        ]),
        (u"Explode Tree restitue chaque liste séparément (zoomer pour voir les sorties)", [
            ("ex", "Explode Tree", 3, 1, {"outputs": 3}),
        ]),
    ],
    wires=[("l1", "ent", 0), ("l2", "ent", 1), ("l3", "ent", 2),
           ("ent", "pv", 0), ("ent", "ex", 0), ("ent", "rep", 0)],
)

R["A-23"] = dict(
    sujet=[
        ("tree", "DATA:Number", 0, 0,
         {"nick": "ARBRE_2_NIVEAUX",
          "data": [("0;0", [1]), ("0;1", [2]), ("0;2", [3]), ("0;3", [4]),
                   ("1;0", [5]), ("1;1", [6]), ("1;2", [7]), ("1;3", [8]),
                   ("2;0", [9]), ("2;1", [10]), ("2;2", [11]), ("2;3", [12])]}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Path Mapper : masque source {A;B}, masque cible {B;A}", [
            ("pm", "Path Mapper", 1, 0, {}),
        ]),
        (u"Contrôler la permutation des deux niveaux", [
            ("pv", "Param Viewer", 2, 0, {}),
        ]),
    ],
    manuel=[
        u"Path Mapper : double-cliquer, saisir {A;B} en source et {B;A} en cible.",
        u"Ne pas oublier les accolades, et réutiliser les mêmes lettres de part et d'autre.",
    ],
    wires=[("tree", "pm", 0), ("pm", "pv", 0), ("pm", "rep", 0)],
)

R["A-24"] = dict(
    sujet=[
        ("l10", "DATA:Number", 0, 0, {"nick": "DIX_VALEURS", "data": VINGT[:10]}),
        ("l4", "DATA:Number", 0, 1, {"nick": "QUATRE_VALEURS", "data": [1, 2, 3, 4]}),
        ("add", "Addition", 1, 0, {}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Compter les résultats réellement produits", [
            ("ll", "List Length", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
        (u"Aucun avertissement n'est émis : la troncature est silencieuse (Shortest List)", [
            ("pv", "Param Viewer", 2, 2, {}),
        ]),
    ],
    wires=[("l10", "add", 0), ("l4", "add", 1), ("add", "ll", 0),
           ("ll", "pan", 0), ("add", "pv", 0), ("ll", "rep", 0)],
)

R["A-25"] = dict(
    sujet=[
        ("l10", "DATA:Number", 0, 0, {"nick": "DIX_VALEURS", "data": VINGT[:10]}),
        ("l4", "DATA:Number", 0, 1, {"nick": "QUATRE_VALEURS", "data": [1, 2, 3, 4]}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Longest List complète la liste courte par répétition de son dernier élément", [
            ("lg", "Longest List", 1, 0, {}),
            ("add1", "Addition", 2, 0, {}),
            ("ll1", "List Length", 3, 0, {}),
            ("pan1", "PANEL", 4, 0, {}),
        ]),
        (u"Cross Reference croise chaque élément de A avec chaque élément de B", [
            ("cr", "Cross Reference", 1, 0, {}),
            ("add2", "Addition", 2, 0, {}),
            ("ll2", "List Length", 3, 0, {}),
            ("pan2", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("l10", "lg", 0), ("l4", "lg", 1),
           ("lg", 0, "add1", 0), ("lg", 1, "add1", 1),
           ("add1", "ll1", 0), ("ll1", "pan1", 0), ("ll1", "rep", 0),
           ("l10", "cr", 0), ("l4", "cr", 1),
           ("cr", 0, "add2", 0), ("cr", 1, "add2", 1),
           ("add2", "ll2", 0), ("ll2", "pan2", 0)],
)

R["A-26"] = dict(
    sujet=[
        ("sl", "SLIDER", 0, 0, {"slider": (0, 100, 20, 0), "nick": "Entrée branche 1"}),
        ("m1", "Multiplication", 1, 0, {"val": [(1, "Number", [2])]}),
        ("pan1", "PANEL", 2, 0, {}),
        ("data", "DATA:Number", 0, 2, {"nick": "Entrée branche 2", "data": [7, 8, 9]}),
        ("m2", "Multiplication", 1, 2, {"val": [(1, "Number", [3])]}),
        ("pan2", "PANEL", 2, 2, {}),
        ("qcm", "VALUELIST", 4, 1,
         {"nick": "REPONSE_QCM",
          "items": [(u"0 - de gauche a droite sur le canvas", "0"),
                    (u"1 - selon les dependances de donnees", "1"),
                    (u"2 - dans l'ordre de creation des composants", "2"),
                    (u"3 - de haut en bas sur le canvas", "3")]}),
        ("rep", "REPONSE", 6, 1, {"type": "Integer"}),
    ],
    corrige=[
        (u"Modifier un curseur : seule la branche qui en dépend se recalcule", [
            ("pv", "Param Viewer", 3, 0, {}),
        ]),
        (u"Déplacer un composant ne change rien : l'ordre suit le graphe de dépendances", [
            ("pv2", "Param Viewer", 3, 2, {}),
        ]),
    ],
    manuel=[
        u"Activer le widget Profiler (menu Display) pour lire les temps par composant.",
        u"Réponse attendue : 1 — l'ordre suit les dépendances de données.",
    ],
    wires=[("sl", "m1", 0), ("m1", "pan1", 0),
           ("data", "m2", 0), ("m2", "pan2", 0),
           ("m1", "pv", 0), ("m2", "pv2", 0), ("qcm", "rep", 0)],
)
