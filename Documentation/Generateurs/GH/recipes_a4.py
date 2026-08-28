# -*- coding: utf-8 -*-
"""Recettes de construction - LOT A, exercices A-39 a A-49."""

import math

R = {}

DEUX_PI = 2.0 * math.pi

# quatre percages traversants dans un bloc de 300 x 200 x 60
PERCAGES = [((60, 50, -20), 10, 100), ((240, 50, -20), 10, 100),
            ((60, 150, -20), 10, 100), ((240, 150, -20), 10, 100)]

# quinze blocs disposes en trame, dont certains empietent sur le gabarit
QUINZE_BLOCS = []
for _i in range(5):
    for _j in range(3):
        QUINZE_BLOCS.append(((_i * 130.0, _j * 110.0, 0), 90, 70, 40))

SIX_PIECES = [((0, 0, 0), 120, 80, 40), ((200, 0, 0), 90, 90, 60),
              ((360, 0, 0), 150, 60, 30), ((0, 160, 0), 70, 70, 100),
              ((200, 160, 0), 110, 130, 25), ((400, 160, 0), 60, 60, 80)]

COURBE_LIBRE = [(0, 0, 0), (100, 120, 0), (250, 60, 0),
                (340, -80, 0), (480, 20, 0), (600, 140, 0)]

R["A-39"] = dict(
    sujet=[
        ("mod", "GEO:Curve", 0, 0, {"nick": "MODULE", "geo": ("rect", (0, 0, 0), 400, 300)}),
        ("rep", "REPONSE", 5, 0, {"type": "Curve"}),
    ],
    corrige=[
        (u"La cellule du réseau est une boîte : 600 x 400 correspond à des demi-cotes de 300 et 200", [
            ("cb", "Center Box", 1, 2, {"val": [(1, "Number", [300]), (2, "Number", [200]),
                                                (3, "Number", [0.5])]}),
        ]),
        (u"Réseau rectangulaire 5 x 4 : la sortie est un arbre, pas une liste plate", [
            ("ra", "Rectangular Array", 2, 0, {"val": [(2, "Integer", [5]),
                                                       (3, "Integer", [4])]}),
            ("pv", "Param Viewer", 3, 0, {}),
        ]),
        (u"Réseau polaire : 12 copies sur 2 pi radians", [
            ("pa", "Polar Array", 2, 2, {"val": [(2, "Integer", [12]),
                                                 (3, "Number", [DEUX_PI])]}),
        ]),
    ],
    wires=[("mod", "ra", 0), ("cb", "ra", 1), ("ra", 0, "pv", 0),
           ("mod", "pa", 0), ("ra", 0, "rep", 0)],
)

R["A-40"] = dict(
    sujet=[
        ("prof", "GEO:Curve", 0, 0, {"nick": "PROFIL",
                                     "geo": ("polygon", (0, 0, 0), 80, 6)}),
        ("rep", "REPONSE", 4, 0, {"type": "Curve"}),
    ],
    corrige=[
        (u"Area fournit le centroïde : Scale utiliserait sinon l'origine du repère", [
            ("ar", "Area", 1, 1, {}),
        ]),
        (u"Échelle uniforme à 60 %, centrée sur le centre de gravité", [
            ("sc", "Transform/Affine/Scale", 2, 0, {"val": [(2, "Number", [0.6])]}),
        ]),
        (u"Échelle non uniforme : deux fois plus haut, largeur inchangée", [
            ("xy", "XY Plane", 2, 2, {}),
            ("snu", "Scale NU", 3, 2, {"val": [(2, "Number", [1]), (3, "Number", [2]),
                                               (4, "Number", [1])]}),
        ]),
    ],
    wires=[("prof", "ar", 0), ("prof", "sc", 0), ("ar", 1, "sc", 1),
           ("prof", "snu", 0), ("xy", "snu", 1), ("sc", 0, "rep", 0)],
)

R["A-41"] = dict(
    sujet=[
        ("prof", "GEO:Curve", 0, 0,
         {"nick": "PROFILS", "geo": ("circles", [((0, 0, 0), 80), ((0, 0, 300), 50)])}),
        ("rep", "REPONSE", 5, 0, {"type": "Brep"}),
    ],
    corrige=[
        (u"Loft relie les deux profils : l'ordre de branchement compte", [
            ("lo", "Loft", 1, 0, {}),
        ]),
        (u"Extrude attend un vecteur, pas une distance", [
            ("li", "List Item", 1, 2, {"val": [(1, "Integer", [0])]}),
            ("sl", "SLIDER", 2, 3, {"slider": (0, 500, 200, 0), "nick": "Hauteur (mm)"}),
            ("uz", "Unit Z", 3, 3, {}),
        ]),
        (u"Loft suit les deux profils, Extrude conserve la section constante", [
            ("ex", "Extrude", 4, 2, {}),
        ]),
    ],
    wires=[("prof", "lo", 0), ("prof", "li", 0), ("sl", "uz", 0),
           ("li", "ex", 0), ("uz", "ex", 1), ("lo", 0, "rep", 0)],
)

R["A-42"] = dict(
    sujet=[
        ("rail", "GEO:Curve", 0, 0,
         {"nick": "COURBE_GUIDE", "geo": ("interp", [(0, 0, 0), (150, 100, 50),
                                                     (320, -40, 120), (480, 60, 200)])}),
        ("sect", "GEO:Curve", 0, 1, {"nick": "PROFIL_CIRCULAIRE",
                                     "geo": ("circle", (0, 0, 0), 20)}),
        ("gene", "GEO:Curve", 0, 2,
         {"nick": "PROFIL_VASE", "geo": ("poly", [(20, 0, 0), (60, 0, 20), (70, 0, 120),
                                                  (45, 0, 200), (55, 0, 260)], False)}),
        ("rep", "REPONSE", 4, 0, {"type": "Brep"}),
    ],
    corrige=[
        (u"Balayage : le profil doit être perpendiculaire au rail", [
            ("pf", "Perp Frames", 1, 0, {"val": [(1, "Integer", [1])]}),
            ("xyo", "XY Plane", 1, 2, {}),
            ("or1", "Transform/Euclidean/Orient", 2, 0, {}),
        ]),
        (u"Sweep1 le long de la courbe guide", [
            ("sw", "Sweep1", 3, 0, {}),
        ]),
        (u"Révolution du profil plan : le domaine complet ferme le vase", [
            ("axe", "GEO:Curve", 1, 2, {"nick": "AXE_Z",
                                       "geo": ("poly", [(0, 0, 0), (0, 0, 300)], False)}),
            ("cd", "Construct Domain", 2, 2, {"val": [(0, "Number", [0]),
                                                      (1, "Number", [6.283185307179586])]}),
            ("rv", "Revolution", 3, 2, {}),
        ]),
    ],
    manuel=[
    ],
    wires=[("rail", "pf", 0), ("sect", "or1", 0), ("xyo", "or1", 1), ("pf", 0, "or1", 2),
           ("rail", "sw", 0), ("or1", 0, "sw", 1),
           ("gene", "rv", 0), ("axe", "rv", 1), ("cd", "rv", 2),
           ("sw", 0, "rep", 0)],
)

R["A-43"] = dict(
    sujet=[
        ("brp", "GEO:Brep", 0, 0,
         {"nick": "POLYSURFACE_OUVERTE",
          "geo": ("tube", (0, 0, 0), 200, 150, 100)}),
        ("rep", "REPONSE", 5, 0, {"type": "Boolean"}),
    ],
    corrige=[
        (u"Cap Holes ferme les ouvertures planes", [
            ("cap", "Cap Holes", 1, 0, {}),
        ]),
        (u"Un volume non nul prouve la fermeture", [
            ("vo", "Volume", 2, 0, {}),
            ("pan", "PANEL", 3, 1, {}),
        ]),
        (u"Traduire la preuve en booléen", [
            ("lt", "Larger Than", 3, 0, {"val": [(1, "Number", [0])]}),
            ("pan2", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("brp", "cap", 0), ("cap", "vo", 0), ("vo", 0, "pan", 0),
           ("vo", 0, "lt", 0), ("lt", 0, "pan2", 0), ("lt", 0, "rep", 0)],
)

R["A-44"] = dict(
    sujet=[
        ("bloc", "GEO:Brep", 0, 0, {"nick": "BLOC", "geo": ("box", (0, 0, 0), 300, 200, 60)}),
        ("cyl", "GEO:Brep", 0, 2, {"nick": "CYLINDRES", "geo": ("cyls", PERCAGES)}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Solid Difference : le bloc sur A, les cylindres sur B", [
            ("sd", "Solid Difference", 1, 0, {}),
        ]),
        (u"Mesurer le volume avant et après perçage", [
            ("v1", "Volume", 2, 2, {}),
            ("v2", "Volume", 2, 0, {}),
        ]),
        (u"La différence donne le volume de matière retirée", [
            ("sub", "Subtraction", 3, 1, {}),
            ("pan", "PANEL", 4, 1, {}),
        ]),
    ],
    wires=[("bloc", "sd", 0), ("cyl", "sd", 1),
           ("bloc", "v1", 0), ("sd", "v2", 0),
           ("v1", 0, "sub", 0), ("v2", 0, "sub", 1),
           ("sub", "pan", 0), ("sub", "rep", 0)],
)

R["A-45"] = dict(
    sujet=[
        ("sol", "GEO:Brep", 0, 0, {"nick": "SOLIDE",
                                   "geo": ("box", (0, 0, 0), 200, 150, 100)}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le centroïde donne directement la mi-hauteur", [
            ("vo", "Volume", 1, 2, {}),
            ("xy", "XY Plane", 2, 2, {}),
        ]),
        (u"Couper le solide par ce plan et récupérer les courbes de coupe", [
            ("bp", "Brep | Plane", 3, 0, {}),
        ]),
        (u"Additionner les longueurs de tous les contours obtenus", [
            ("ln", "Length", 4, 0, {}),
            ("ma", "Mass Addition", 5, 2, {}),
            ("pan", "PANEL", 4, 2, {}),
        ]),
    ],
    wires=[("sol", "vo", 0), ("vo", 1, "xy", 0),
           ("sol", "bp", 0), ("xy", "bp", 1),
           ("bp", 0, "ln", 0), ("ln", "ma", 0), ("ma", 0, "pan", 0),
           ("ma", 0, "rep", 0)],
)

R["A-46"] = dict(
    sujet=[
        ("blocs", "GEO:Brep", 0, 0, {"nick": "BLOCS", "geo": ("boxes", QUINZE_BLOCS)}),
        ("gab", "GEO:Brep", 0, 2, {"nick": "GABARIT",
                                   "geo": ("box", (150, 60, -10), 260, 200, 80)}),
        ("rep", "REPONSE", 5, 0, {"type": "Brep"}),
    ],
    corrige=[
        (u"Inverser les rôles : les blocs sur Collider, le gabarit sur Obstacles", [
            ("col", "Collision One|Many", 1, 1, {"graft": 0}),
        ]),
        (u"Grafter l'entrée Collider : chaque bloc, seul dans sa branche, obtient "
         u"son propre booléen. Sans graft on n'aurait qu'un booléen global.", [
            ("fl", "Flatten Tree", 2, 1, {}),
            ("disp", "Dispatch", 3, 0, {}),
        ]),
        (u"Afficher les blocs en collision dans une couleur distincte", [
            ("sw", "Colour Swatch", 3, 2, {}),
            ("cp", "Custom Preview", 4, 0, {}),
        ]),
    ],
    manuel=[
        u"Colour Swatch : régler la couleur sur rouge par double-clic.",
    ],
    wires=[("blocs", "col", 0), ("gab", "col", 1),
           ("col", 0, "fl", 0),
           ("blocs", "disp", 0), ("fl", "disp", 1),
           ("disp", 0, "cp", 0), ("sw", "cp", 1),
           ("disp", 0, "rep", 0)],
)

R["A-47"] = dict(
    sujet=[
        ("sol", "GEO:Brep", 0, 0, {"nick": "ASSEMBLAGE",
                                   "geo": ("box", (0, 0, 0), 240, 180, 90)}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Deconstruct Brep sépare faces, arêtes et sommets", [
            ("db", "Deconstruct Brep", 1, 0, {}),
        ]),
        (u"Développé des arêtes : mesurer puis sommer", [
            ("ln", "Length", 2, 0, {}),
            ("ma", "Mass Addition", 3, 0, {}),
        ]),
        (u"Sur un Brep fermé, Area renvoie déjà la surface totale", [
            ("ar", "Area", 2, 2, {}),
            ("vo", "Volume", 2, 3, {}),
        ]),
        (u"Assembler les trois valeurs dans l'ordre demandé", [
            ("mg1", "Merge", 4, 1, {}),
            ("mg2", "Merge", 5, 1, {}),
            ("pan", "PANEL", 5, 3, {}),
        ]),
    ],
    wires=[("sol", "db", 0), ("db", 1, "ln", 0), ("ln", "ma", 0),
           ("sol", "ar", 0), ("sol", "vo", 0),
           ("ma", 0, "mg1", 0), ("ar", 0, "mg1", 1),
           ("mg1", "mg2", 0), ("vo", 0, "mg2", 1),
           ("mg2", "pan", 0), ("mg2", "rep", 0)],
)

R["A-48"] = dict(
    sujet=[
        ("crv", "GEO:Curve", 0, 0, {"nick": "COURBE", "geo": ("interp", COURBE_LIBRE)}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Échantillonner finement : 200 divisions", [
            ("dc", "Divide Curve", 1, 0, {"val": [(1, "Integer", [200])]}),
        ]),
        (u"Curvature renvoie le vecteur de courbure en chaque paramètre", [
            ("cu", "Curvature", 2, 0, {}),
            ("vl", "Vector Length", 3, 0, {}),
        ]),
        (u"Prendre la courbure maximale, puis son inverse : le rayon", [
            ("bd", "Bounds", 4, 0, {}),
            ("dd", "Bounds", 4, 2, {}),
            ("dv", "Division", 5, 2, {"val": [(0, "Number", [1])]}),
            ("pan", "PANEL", 5, 3, {}),
        ]),
    ],
    manuel=[
        u"Remplacer le second Bounds par un Deconstruct Domain si le nom diffère : "
        u"on cherche la borne haute du domaine des courbures.",
    ],
    wires=[("crv", "dc", 0), ("crv", "cu", 0), ("dc", 2, "cu", 1),
           ("cu", 1, "vl", 0), ("vl", "bd", 0), ("bd", "dd", 0),
           ("dd", 0, "dv", 1), ("dv", "pan", 0), ("dv", "rep", 0)],
)

R["A-49"] = dict(
    sujet=[
        ("sols", "GEO:Brep", 0, 0, {"nick": "PIECES", "geo": ("boxes", SIX_PIECES)}),
        ("rep", "REPONSE", 5, 0, {"type": "Point"}),
    ],
    corrige=[
        (u"La sortie C de Volume donne le centroïde volumique de chaque pièce", [
            ("vo", "Volume", 1, 0, {}),
        ]),
        (u"Générer les numéros de 1 à 6 et les formater sur deux chiffres", [
            ("ser", "Series", 1, 2, {"val": [(0, "Number", [1]), (1, "Number", [1]),
                                             (2, "Integer", [6])]}),
            ("fmt", "Format", 2, 2, {"val": [(0, "Text", ["{0:00}"])]}),
        ]),
        (u"Poser l'étiquette au centre de gravité de chaque pièce", [
            ("tt", "Text Tag 3D", 3, 0, {"val": [(2, "Number", [12])]}),
        ]),
    ],
    wires=[("sols", "vo", 0), ("ser", "fmt", 2),
           ("vo", 1, "tt", 0), ("fmt", "tt", 1),
           ("vo", 1, "rep", 0)],
)
