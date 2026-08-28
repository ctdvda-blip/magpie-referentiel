# -*- coding: utf-8 -*-
"""Recettes de construction - LOT A, exercices A-01 a A-13.

Format d'un objet : (cle, LABEL, colonne, ligne, options)
  LABEL special : SLIDER, PANEL, TOGGLE, VALUELIST, REPONSE,
                  DATA:<type>, PARAM:<type>, GEO:<type>
  sinon : nom du composant Grasshopper, resolu au moment de la construction.
Format d'un cablage : (source, cible, entree)  ou  (source, sortie, cible, entree)
La cle "rep" designe toujours le parametre REPONSE.
"""

R = {}

LETTRES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
DOUZE = [14, 7, 23, 3, 19, 11, 30, 2, 26, 8, 17, 5]
QUINZE = [42, 8, 91, 17, 63, 4, 78, 25, 56, 12, 39, 70, 31, 87, 49]
VINGT = [12, 68, 34, 91, 7, 55, 80, 23, 46, 99, 15, 72, 38, 61, 4, 87, 29, 53, 76, 41]

R["A-01"] = dict(
    sujet=[
        ("slA", "SLIDER", 0, 0, {"slider": (0, 100, 17, 0), "nick": "Valeur A"}),
        ("rep", "REPONSE", 3, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Poser un second Number Slider de 0 à 100", [
            ("slB", "SLIDER", 0, 0, {"slider": (0, 100, 25, 0), "nick": "Valeur B"}),
        ]),
        (u"Additionner les deux valeurs", [
            ("add", "Addition", 1, 0, {}),
        ]),
        (u"Afficher le résultat et régler les curseurs sur 42", [
            ("pan", "PANEL", 2, 0, {}),
        ]),
    ],
    wires=[("slA", "add", 0), ("slB", "add", 1), ("add", "pan", 0), ("add", "rep", 0)],
)

R["A-02"] = dict(
    sujet=[
        ("rep", "REPONSE", 3, 1, {"type": "Point"}),
    ],
    corrige=[
        (u"Trois curseurs, en veillant aux bornes négatives pour Y", [
            ("slX", "SLIDER", 0, 0, {"slider": (-100, 100, 30, 0), "nick": "X"}),
            ("slY", "SLIDER", 0, 1, {"slider": (-50, 50, -15, 0), "nick": "Y"}),
            ("slZ", "SLIDER", 0, 2, {"slider": (-50, 50, 8, 0), "nick": "Z"}),
        ]),
        (u"Assembler les trois nombres en un point", [
            ("cp", "Construct Point", 1, 1, {}),
        ]),
    ],
    wires=[("slX", "cp", 0), ("slY", "cp", 1), ("slZ", "cp", 2), ("cp", "rep", 0)],
)

R["A-03"] = dict(
    sujet=[
        ("slX", "SLIDER", 0, 0, {"slider": (-100, 100, 30, 0), "nick": "X"}),
        ("slY", "SLIDER", 0, 1, {"slider": (-50, 50, -15, 0), "nick": "Y"}),
        ("slZ", "SLIDER", 0, 2, {"slider": (-50, 50, 8, 0), "nick": "Z"}),
        ("cp", "Construct Point", 1, 1, {}),
        ("rep", "REPONSE", 4, 1, {"type": "Point"}),
    ],
    corrige=[
        (u"Poser un paramètre Point autonome et y internaliser la donnée", [
            ("ptf", "DATA:Point", 0, 0, {"nick": "POINT_FIGE", "data": [(30, -15, 8)]}),
        ]),
        (u"La chaîne amont peut alors être supprimée : le point subsiste", [
            ("pv", "Param Viewer", 1, 0, {}),
        ]),
    ],
    wires=[("slX", "cp", 0), ("slY", "cp", 1), ("slZ", "cp", 2),
           ("ptf", "pv", 0), ("ptf", "rep", 0)],
)

R["A-04"] = dict(
    ressource_3dm=("A-04", "CERCLES", [((0, 0, 0), 40), ((120, 0, 0), 25), ((240, 0, 0), 60)]),
    sujet=[
        ("gp", "Geometry Pipeline", 0, 0, {"nick": "PIPELINE"}),
        ("rep", "REPONSE", 4, 0, {"type": "Curve"}),
    ],
    corrige=[
        (u"Renseigner le calque CERCLES dans le Geometry Pipeline", [
            ("gp2", "Geometry Pipeline", 0, 0, {"layer": "CERCLES", "nick": "PIPELINE"}),
        ]),
        (u"Construire le vecteur de décalage : 50 mm suivant Z", [
            ("sl", "SLIDER", 1, 1, {"slider": (0, 200, 50, 0), "nick": "Décalage (mm)"}),
            ("uz", "Unit Z", 2, 1, {}),
        ]),
        (u"Déplacer, puis cuire le résultat sur le calque COPIES", [
            ("mv", "Transform/Euclidean/Move", 3, 0, {}),
        ]),
    ],
    manuel=[
        u"Geometry Pipeline : saisir CERCLES dans le champ Layer (sensible à la casse).",
        u"Bake du composant Move : choisir le calque COPIES.",
    ],
    wires=[("gp2", "mv", 0), ("sl", "uz", 0), ("uz", "mv", 1), ("mv", "rep", 0)],
)

R["A-05"] = dict(
    sujet=[
        ("flux", "DATA:Number", 0, 0, {"nick": "FLUX", "data": DOUZE}),
        ("rep", "REPONSE", 3, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Inspecter la structure du flux sans le modifier", [
            ("pv", "Param Viewer", 1, 1, {}),
        ]),
        (u"Compter les éléments transportés", [
            ("ll", "List Length", 1, 0, {}),
            ("pan", "PANEL", 2, 0, {}),
        ]),
    ],
    wires=[("flux", "pv", 0), ("flux", "ll", 0), ("ll", "pan", 0), ("ll", "rep", 0)],
)

R["A-06"] = dict(
    sujet=[
        ("sl", "SLIDER", 0, 0, {"slider": (0, 10, 4.6, 1), "nick": "Count"}),
        ("ser", "Series", 1, 0, {}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Compter les éléments réellement produits par la série", [
            ("ll", "List Length", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
        (u"Faire varier le curseur entre 4,4 et 4,6 : Grasshopper arrondit au plus proche", [
            ("pv", "Param Viewer", 2, 1, {}),
        ]),
    ],
    wires=[("sl", "ser", 2), ("ser", "ll", 0), ("ll", "pan", 0), ("ll", "rep", 0),
           ("ser", "pv", 0)],
)

R["A-07"] = dict(
    sujet=[
        ("txt", "PANEL", 0, 0, {"text": "douze"}),
        ("sl", "SLIDER", 0, 1, {"slider": (0, 10, 3, 0), "nick": "Valeur B"}),
        ("add", "Addition", 1, 0, {}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le texte non numérique produit une valeur nulle, pas un zéro", [
            ("pv", "Param Viewer", 2, 1, {}),
        ]),
        (u"Remplacer le contenu du Panel par une valeur numérique", [
            ("txtok", "PANEL", 0, 2, {"text": "12"}),
        ]),
        (u"L'addition redevient valide et renvoie 15", [
            ("add2", "Addition", 1, 2, {}),
            ("pan", "PANEL", 2, 2, {}),
        ]),
    ],
    wires=[("txt", "add", 0), ("sl", "add", 1), ("add", "pv", 0),
           ("txtok", "add2", 0), ("sl", "add2", 1), ("add2", "pan", 0),
           ("add2", "rep", 0)],
)

R["A-08"] = dict(
    sujet=[
        ("data", "DATA:Number", 0, 0, {"nick": "VALEURS", "data": DOUZE[:10]}),
        ("sl", "SLIDER", 0, 1, {"slider": (0, 30, 5, 0), "nick": "Seuil"}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Comparer chaque valeur au seuil : on obtient une liste de booléens", [
            ("lt", "Larger Than", 1, 0, {}),
        ]),
        (u"Sommer les booléens : True vaut 1, False vaut 0", [
            ("ma", "Mass Addition", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("data", "lt", 0), ("sl", "lt", 1), ("lt", "ma", 0),
           ("ma", "pan", 0), ("ma", "rep", 0)],
)

R["A-09"] = dict(
    sujet=[
        ("data", "DATA:Number", 0, 0,
         {"nick": "LISTE_AVEC_NULLES", "data": [1, 2, None, 4, 5, None, 7, 8]}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Localiser les valeurs nulles", [
            ("ni", "Null Item", 1, 1, {}),
        ]),
        (u"Nettoyer la liste en supprimant les nulles", [
            ("ct", "Clean Tree", 1, 0, {"val": [(0, "Boolean", [True])]}),
        ]),
        (u"Compter les éléments valides restants", [
            ("ll", "List Length", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("data", "ni", 0), ("data", "ct", 3), ("ct", "ll", 0),
           ("ll", "pan", 0), ("ll", "rep", 0)],
)

R["A-10"] = dict(
    sujet=[
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Series raisonne en pas et nombre d'éléments", [
            ("ser", "Series", 0, 0, {"val": [(0, "Number", [10]), (1, "Number", [5]),
                                             (2, "Integer", [5])]}),
            ("pan1", "PANEL", 1, 0, {}),
        ]),
        (u"Range raisonne en domaine et nombre de subdivisions", [
            ("cd", "Construct Domain", 0, 0, {"val": [(0, "Number", [10]),
                                                      (1, "Number", [30])]}),
            ("rng", "Range", 1, 0, {"val": [(1, "Integer", [4])]}),
            ("pan2", "PANEL", 2, 0, {}),
        ]),
    ],
    wires=[("ser", "pan1", 0), ("ser", "rep", 0), ("cd", "rng", 0), ("rng", "pan2", 0)],
)

R["A-11"] = dict(
    sujet=[
        ("data", "DATA:Text", 0, 0, {"nick": "LETTRES", "data": LETTRES}),
        ("rep", "REPONSE", 5, 0, {"type": "Text"}),
    ],
    corrige=[
        (u"Le premier élément porte l'index 0 : la lettre D est à l'index 3", [
            ("li1", "List Item", 1, 0, {"val": [(1, "Integer", [3])]}),
            ("pan1", "PANEL", 2, 0, {}),
        ]),
        (u"Pour le dernier élément, calculer l'index plutôt que le coder en dur", [
            ("ll", "List Length", 1, 2, {}),
            ("sub", "Subtraction", 2, 2, {"val": [(1, "Number", [1])]}),
        ]),
        (u"Extraire à cet index calculé", [
            ("li2", "List Item", 3, 1, {}),
            ("pan2", "PANEL", 4, 1, {}),
        ]),
    ],
    wires=[("data", "li1", 0), ("li1", "pan1", 0),
           ("data", "ll", 0), ("ll", "sub", 0),
           ("data", "li2", 0), ("sub", "li2", 1),
           ("li2", "pan2", 0), ("li2", "rep", 0)],
)

R["A-12"] = dict(
    sujet=[
        ("data", "DATA:Number", 0, 0, {"nick": "VALEURS", "data": QUINZE}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Mesurer l'effectif", [
            ("ll", "List Length", 1, 0, {}),
        ]),
        (u"Obtenir le domaine des valeurs puis ses deux bornes", [
            ("bd", "Bounds", 1, 1, {}),
            ("dd", "Deconstruct Domain", 2, 1, {}),
        ]),
        (u"Assembler effectif, minimum et maximum dans cet ordre", [
            ("mg1", "Merge", 3, 0, {}),
            ("mg2", "Merge", 4, 0, {}),
            ("pan", "PANEL", 4, 2, {}),
        ]),
    ],
    wires=[("data", "ll", 0), ("data", "bd", 0), ("bd", "dd", 0),
           ("ll", "mg1", 0), ("dd", 0, "mg1", 1),
           ("mg1", "mg2", 0), ("dd", 1, "mg2", 1),
           ("mg2", "pan", 0), ("mg2", "rep", 0)],
)

R["A-13"] = dict(
    sujet=[
        ("noms", "DATA:Text", 0, 0,
         {"nick": "NOMS", "data": ["Montant", "Traverse", "Panneau",
                                   "Tablette", "Socle", "Chant"]}),
        ("lg", "DATA:Number", 0, 1,
         {"nick": "LONGUEURS", "data": [2100, 850, 1800, 760, 1200, 2400]}),
        ("rep", "REPONSE", 4, 0, {"type": "Text"}),
    ],
    corrige=[
        (u"Trier : les longueurs sont les clés, les noms les valeurs", [
            ("sl", "Sort List", 1, 0, {}),
        ]),
        (u"Sort List trie par ordre croissant : inverser pour obtenir le décroissant", [
            ("rv", "Reverse List", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("lg", "sl", 0), ("noms", "sl", 1), ("sl", 1, "rv", 0),
           ("rv", "pan", 0), ("rv", "rep", 0)],
)
