# -*- coding: utf-8 -*-
"""Recettes de construction - LOT A, exercices A-27 a A-38."""

R = {}

LONGUEURS_20 = [820, 1450, 380, 1180, 640, 1520, 990, 470, 1340, 720,
                510, 1600, 860, 290, 1120, 750, 430, 1280, 950, 610]

REFS = ["MEUB-A12-CHENE", "MEUB-B07-NOYER", "MEUB-C24-FRENE",
        "MEUB-D03-ERABLE", "MEUB-E18-HETRE", "MEUB-F31-CHENE"]

SIX_PTS = [(0, 0, 0), (120, 90, 0), (260, -50, 0),
           (390, 70, 0), (520, -20, 0), (640, 40, 0)]

R["A-27"] = dict(
    sujet=[
        ("num", "DATA:Integer", 0, 0, {"nick": "NUMEROS", "data": [1, 2, 3, 4, 5]}),
        ("lng", "DATA:Number", 0, 2, {"nick": "LONGUEURS",
                                      "data": [1250, 880, 1640, 730, 1100]}),
        ("rep", "REPONSE", 4, 1, {"type": "Text"}),
    ],
    corrige=[
        (u"Formater le numéro sur deux chiffres avec le masque {0:00}", [
            ("fmt", "Format", 1, 0, {"val": [(0, "Text", ["{0:00}"])]}),
        ]),
        (u"Assembler les cinq fragments, en surveillant les espaces", [
            ("cat", "Concatenate", 2, 1, {"inputs": 5,
                                          "val": [(0, "Text", ["PIECE-"]),
                                                  (2, "Text", [" : "]),
                                                  (4, "Text", [" mm"])]}),
            ("pan", "PANEL", 3, 1, {"w": 220}),
        ]),
    ],
    wires=[("num", "fmt", 2), ("fmt", "cat", 1), ("lng", "cat", 3),
           ("cat", "pan", 0), ("cat", "rep", 0)],
)

R["A-28"] = dict(
    sujet=[
        ("refs", "DATA:Text", 0, 0, {"nick": "REFERENCES", "data": REFS}),
        ("rep", "REPONSE", 5, 0, {"type": "Text"}),
    ],
    corrige=[
        (u"Découper sur le tiret : chaque référence donne une branche de trois fragments", [
            ("sp", "Text Split", 1, 0, {"val": [(1, "Text", ["-"])]}),
            ("pv", "Param Viewer", 2, 2, {}),
        ]),
        (u"Prendre le fragment central de chaque branche", [
            ("li", "List Item", 2, 0, {"val": [(1, "Integer", [1])]}),
        ]),
        (u"Convertir en minuscules : la sortie L de Text Case", [
            ("tc", "Text Case", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("refs", "sp", 0), ("sp", "pv", 0), ("sp", "li", 0), ("li", "tc", 0),
           ("tc", 1, "pan", 0), ("tc", 1, "rep", 0)],
)

R["A-29"] = dict(
    sujet=[
        ("a", "SLIDER", 0, 0, {"slider": (0, 1, 0.1, 1), "nick": "A"}),
        ("b", "SLIDER", 0, 1, {"slider": (0, 1, 0.2, 1), "nick": "B"}),
        ("add", "Addition", 1, 0, {}),
        ("c", "SLIDER", 0, 2, {"slider": (0, 1, 0.3, 1), "nick": "C"}),
        ("eq", "Equality", 2, 0, {}),
        ("rep", "REPONSE", 5, 1, {"type": "Boolean"}),
    ],
    corrige=[
        (u"Equality renvoie False : deux flottants ne sont jamais strictement égaux", [
            ("pan0", "PANEL", 3, 0, {}),
        ]),
        (u"Similarity compare avec une tolérance explicite", [
            ("sim", "Similarity", 3, 2, {"val": [(2, "Number", [0.001])]}),
            ("pan", "PANEL", 4, 2, {}),
        ]),
    ],
    wires=[("a", "add", 0), ("b", "add", 1),
           ("add", "eq", 0), ("c", "eq", 1), ("eq", 0, "pan0", 0),
           ("add", "sim", 0), ("c", "sim", 1),
           ("sim", 0, "pan", 0), ("sim", 0, "rep", 0)],
)

R["A-30"] = dict(
    sujet=[
        ("data", "DATA:Number", 0, 0, {"nick": "LONGUEURS", "data": LONGUEURS_20}),
        ("rep", "REPONSE", 5, 0, {"type": "Boolean"}),
    ],
    corrige=[
        (u"Borne basse : utiliser la sortie >= car 500 est inclus", [
            ("s1", "SLIDER", 1, 1, {"slider": (0, 2000, 500, 0), "nick": "Mini"}),
            ("ge", "Larger Than", 2, 0, {}),
        ]),
        (u"Borne haute : sortie <= car 1500 est inclus", [
            ("s2", "SLIDER", 1, 1, {"slider": (0, 2000, 1500, 0), "nick": "Maxi"}),
            ("le", "Smaller Than", 2, 0, {}),
        ]),
        (u"Gate And : les deux conditions doivent être vraies simultanément", [
            ("ga", "Gate And", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("data", "ge", 0), ("s1", "ge", 1),
           ("data", "le", 0), ("s2", "le", 1),
           ("ge", 1, "ga", 0), ("le", 1, "ga", 1),
           ("ga", "pan", 0), ("ga", "rep", 0)],
)

R["A-31"] = dict(
    sujet=[
        ("cir", "GEO:Curve", 0, 0, {"nick": "CERCLE", "geo": ("circle", (0, 0, 0), 50)}),
        ("rec", "GEO:Curve", 0, 1, {"nick": "CARRE",
                                    "geo": ("rect", (150, 0, 0), 90, 90)}),
        ("tg", "TOGGLE", 0, 2, {"value": False, "nick": "Cercle / Carré"}),
        ("rep", "REPONSE", 4, 0, {"type": "Curve"}),
    ],
    corrige=[
        (u"Stream Filter choisit une entrée : le booléen est converti en 0 ou 1", [
            ("sf", "Stream Filter", 2, 0, {}),
        ]),
        (u"Basculer le toggle et vérifier l'alternance dans la vue", [
            ("pv", "Param Viewer", 3, 1, {}),
        ]),
    ],
    wires=[("tg", "sf", 0), ("cir", "sf", 1), ("rec", "sf", 2),
           ("sf", "pv", 0), ("sf", "rep", 0)],
)

R["A-32"] = dict(
    sujet=[
        ("pa", "DATA:Point", 0, 0, {"nick": "ORIGINE", "data": [(0, 0, 0)]}),
        ("pb", "DATA:Point", 0, 1, {"nick": "EXTREMITE", "data": [(30, 40, 0)]}),
        ("rep", "REPONSE", 5, 0, {"type": "Vector"}),
    ],
    corrige=[
        (u"Le vecteur entre les deux points mesure 50", [
            ("v2", "Vector 2Pt", 1, 0, {}),
            ("vl", "Vector Length", 2, 1, {}),
            ("pan", "PANEL", 3, 1, {}),
        ]),
        (u"Amplitude impose une longueur sans changer la direction", [
            ("amp", "Amplitude", 2, 0, {"val": [(1, "Number", [100])]}),
        ]),
        (u"Afficher les deux vecteurs pour comparer", [
            ("vd", "Vector Display", 3, 0, {}),
        ]),
    ],
    wires=[("pa", "v2", 0), ("pb", "v2", 1),
           ("v2", 0, "vl", 0), ("vl", "pan", 0),
           ("v2", 0, "amp", 0), ("pa", "vd", 0), ("amp", "vd", 1),
           ("amp", "rep", 0)],
)

R["A-33"] = dict(
    sujet=[
        ("rep", "REPONSE", 5, 0, {"type": "Curve"}),
    ],
    corrige=[
        (u"Poser l'origine du plan à (0 ; 0 ; 50)", [
            ("cp", "Construct Point", 0, 0, {"val": [(0, "Number", [0]),
                                                     (1, "Number", [0]),
                                                     (2, "Number", [50])]}),
            ("xy", "XY Plane", 1, 0, {}),
        ]),
        (u"Grasshopper travaille en radians : convertir les 30°", [
            ("deg", "SLIDER", 1, 2, {"slider": (0, 90, 30, 0), "nick": "Angle (°)"}),
            ("rad", "Radians", 2, 2, {}),
        ]),
        (u"Incliner le plan puis y poser le cercle de rayon 20", [
            ("rot", "Rotate Plane", 3, 0, {}),
            ("cir", "Curve/Primitive/Circle", 4, 0, {"val": [(1, "Number", [20])]}),
        ]),
    ],
    wires=[("cp", "xy", 0), ("deg", "rad", 0),
           ("xy", "rot", 0), ("rad", "rot", 1),
           ("rot", "cir", 0), ("cir", "rep", 0)],
)

R["A-34"] = dict(
    sujet=[
        ("rep", "REPONSE", 5, 0, {"type": "Curve"}),
    ],
    corrige=[
        (u"Polygon attend un nombre de côtés, ici 6, et un rayon de 40", [
            ("pg", "Polygon", 1, 0, {"val": [(1, "Number", [40]),
                                             (2, "Integer", [6])]}),
        ]),
        (u"Rectangle attend deux domaines centrés, et non une largeur", [
            ("cd", "Construct Domain", 1, 2, {"val": [(0, "Number", [-40]),
                                                      (1, "Number", [40])]}),
            ("rc", "Curve/Primitive/Rectangle", 2, 2, {}),
        ]),
        (u"Le rectangle est tangent au cercle circonscrit à l'hexagone", [
            ("mg", "Merge", 3, 1, {}),
        ]),
    ],
    wires=[("cd", "rc", 1), ("cd", "rc", 2),
           ("pg", 0, "mg", 0), ("rc", 0, "mg", 1), ("mg", "rep", 0)],
)

R["A-35"] = dict(
    sujet=[
        ("crv", "GEO:Curve", 0, 0,
         {"nick": "COURBE", "geo": ("interp", [(0, 0, 0), (120, 80, 0), (260, -40, 30),
                                               (400, 60, 0), (520, 0, 20)])}),
        ("rep", "REPONSE", 5, 0, {"type": "Curve"}),
    ],
    corrige=[
        (u"Sur une courbe ouverte, 11 divisions donnent 12 points", [
            ("dc", "Divide Curve", 1, 2, {"val": [(1, "Integer", [11])]}),
        ]),
        (u"Perp Frames fournit directement les plans perpendiculaires", [
            ("pf", "Perp Frames", 1, 0, {"val": [(1, "Integer", [11])]}),
        ]),
        (u"Poser un cercle de rayon 5 dans chacun de ces plans", [
            ("cir", "Curve/Primitive/Circle", 3, 0, {"val": [(1, "Number", [5])]}),
        ]),
    ],
    wires=[("crv", "dc", 0), ("crv", "pf", 0),
           ("pf", 0, "cir", 0), ("cir", "rep", 0)],
)

R["A-36"] = dict(
    sujet=[
        ("pts", "DATA:Point", 0, 0, {"nick": "POINTS", "data": SIX_PTS}),
        ("rep", "REPONSE", 4, 0, {"type": "Curve"}),
    ],
    corrige=[
        (u"Interpolate : la courbe passe exactement par les points", [
            ("it", "Interpolate", 1, 0, {}),
        ]),
        (u"Nurbs Curve : les points deviennent des points de contrôle", [
            ("nc", "Nurbs Curve", 1, 2, {}),
        ]),
        (u"Superposer les deux tracés pour comparer", [
            ("mg", "Merge", 2, 1, {}),
        ]),
    ],
    wires=[("pts", "it", 0), ("pts", "nc", 0),
           ("it", 0, "mg", 0), ("nc", 0, "mg", 1),
           ("it", 0, "rep", 0)],
)

R["A-37"] = dict(
    sujet=[
        ("cir", "GEO:Curve", 0, 0, {"nick": "CERCLE", "geo": ("circle", (0, 0, 0), 50)}),
        ("rep", "REPONSE", 4, 0, {"type": "Curve"}),
    ],
    corrige=[
        (u"Une série de six hauteurs, de 0 à 120 par pas de 24", [
            ("ser", "Series", 1, 2, {"val": [(0, "Number", [0]), (1, "Number", [24]),
                                             (2, "Integer", [6])]}),
        ]),
        (u"Unit Z multiplié par chaque hauteur donne une liste de vecteurs", [
            ("uz", "Unit Z", 2, 2, {}),
        ]),
        (u"Une liste de vecteurs sur l'entrée T produit une liste de résultats", [
            ("mv", "Transform/Euclidean/Move", 3, 0, {}),
        ]),
    ],
    wires=[("ser", "uz", 0), ("cir", "mv", 0), ("uz", "mv", 1), ("mv", 0, "rep", 0)],
)

R["A-38"] = dict(
    sujet=[
        ("prof", "GEO:Curve", 0, 0, {"nick": "PROFIL",
                                     "geo": ("polygon", (0, 0, 0), 60, 5)}),
        ("rep", "REPONSE", 5, 0, {"type": "Curve"}),
    ],
    corrige=[
        (u"Convertir 45° en radians avant de tourner", [
            ("deg", "SLIDER", 1, 2, {"slider": (0, 180, 45, 0), "nick": "Angle (°)"}),
            ("rad", "Radians", 2, 2, {}),
        ]),
        (u"Rotation autour de l'axe Z passant par l'origine", [
            ("rot", "Transform/Euclidean/Rotate", 3, 0, {}),
        ]),
        (u"Le plan de symétrie de Mirror est un plan, pas un axe", [
            ("xz", "XZ Plane", 3, 2, {}),
            ("mir", "Transform/Euclidean/Mirror", 4, 0, {}),
        ]),
    ],
    wires=[("deg", "rad", 0), ("prof", "rot", 0), ("rad", "rot", 1),
           ("rot", 0, "mir", 0), ("xz", "mir", 1), ("mir", 0, "rep", 0)],
)
