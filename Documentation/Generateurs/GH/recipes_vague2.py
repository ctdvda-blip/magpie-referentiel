# -*- coding: utf-8 -*-
"""Recettes de construction de la vague 2.

Memes conventions que `recipes_vague1.py`.

DEUX FORMES DE CORRIGE
----------------------
1. La CHAINE, quand une suite de composants natifs mene naturellement au
   resultat : c'est le cas de la plupart des exercices de cette vague.

2. L'ETALON, quand la chaine native serait une contorsion sans valeur
   pedagogique : parcours d'un graphe de dependances, inclusion d'ensembles,
   jugement sur un libelle. Le corrige porte alors ce qui a ete RETENU, et un
   panneau dit pourquoi. C'est le parti pris deja adopte pour IA-17 et pour le
   lot RH : le corrige est de quoi verifier sa reponse, pas la methode a
   recopier.

Ne pas confondre l'etalon avec un raccourci : ce qu'il montre — la fermeture
d'un graphe, les postes qui ont les trois plugins, les surnoms muets — est
exactement ce que l'apprenant devait produire, et se lit d'un coup d'oeil.
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

import exercices_vague2 as V2
import exercices_vague2_avance as V2A
from recipes_nouveaux import charniere as recette_charniere

R = {}


def _e(eid):
    for lot in (V2.LOT_RH, V2.LOT_GP, V2.LOT_QT, V2.LOT_MP,
                V2A.LOT_PL, V2A.LOT_DV, V2A.LOT_IA):
        for x in lot:
            if x["id"] == eid:
                return x
    return None


def _compte(nick, donnees, seuil, sens, texte1, texte2, rep_col=6,
            sortie=0):
    """Recette commune : compter les valeurs d'un cote d'un seuil.

    Six exercices de cette vague ont exactement cette forme — parois trop
    minces, faces degenerees, objets au-dessus d'un niveau, details sous une
    resolution, plugins compatibles. Les ecrire six fois a l'identique aurait
    invite a en corriger cinq le jour ou l'on en corrige une.
    """
    # `sortie` choisit entre la comparaison STRICTE (0) et le « ou egal »
    # (1). PL-09 en depend : une version minimale exigee est un plancher,
    # donc un plugin qui demande exactement Rhino 8 s'installe sur Rhino 8.
    # Le prendre strict n'en trouvait que quatre au lieu de sept.
    comparateur = "Smaller Than" if sens == "<" else "Larger Than"
    return dict(
        sujet=[
            ("val", "DATA:Number", 0, 0, {"nick": nick, "data": list(donnees)}),
            ("seuil", "DATA:Number", 0, 3,
             {"nick": u"SEUIL", "data": [seuil]}),
            ("rep", "REPONSE", rep_col, 0, {"type": "Number"}),
        ],
        corrige=[
            (texte1, [
                ("cmp", comparateur, 1, 0, {}),
            ]),
            (texte2, [
                ("cull", "Cull Pattern", 2, 0, {}),
                ("ll", "List Length", 3, 0, {}),
                ("pan", "PANEL", 4, 0, {}),
            ]),
        ],
        wires=[("val", "cmp", 0), ("seuil", "cmp", 1),
               ("val", "cull", 0), ("cmp", sortie, "cull", 1),
               ("cull", "ll", 0), ("ll", "pan", 0), ("ll", "rep", 0)],
    )


def _etalon(nick, donnees, kind, texte, note, rep_col=5):
    """Recette commune : l'etalon porte ce qui a ete retenu, et on le compte."""
    return dict(
        sujet=[
            ("rep", "REPONSE", rep_col, 0, {"type": "Number"}),
        ],
        corrige=[
            (texte, [
                ("ret", "DATA:" + kind, 1, 0,
                 {"nick": nick, "data": list(donnees)}),
            ]),
            (note, [
                ("ll", "List Length", 2, 0, {}),
                ("pan", "PANEL", 3, 0, {}),
            ]),
        ],
        wires=[("ret", "ll", 0), ("ll", "pan", 0), ("ll", "rep", 0)],
    )


# ---------------------------------------------------------------------------
# Lot RH
# ---------------------------------------------------------------------------

_PTS11 = [(x, y, 0.0) for x, y in V2.D_RH11_BATI + V2.D_RH11_EGARES]

R["RH-11"] = dict(
    sujet=[
        ("pts", "DATA:Point", 0, 0,
         {"nick": u"OBJETS_DU_FICHIER", "data": _PTS11}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Ne garder que l'abscisse de chaque objet : c'est selon X que "
         u"l'étendue est demandée", [
            ("dec", "Deconstruct", 1, 0, {}),
        ]),
        (u"Les bornes de la liste — et non celles de ce que l'écran "
         u"montre. Deux objets suffisent à les fixer", [
            ("bor", "Bounds", 2, 0, {}),
            ("dd", "Deconstruct Domain", 3, 0, {}),
        ]),
        (u"L'étendue est la différence des bornes : 6 050 000 mm, soit "
         u"6 050 m. Le bâtiment, lui, tient dans 8,4 m — un sept-centième "
         u"de ce que le zoom étendue doit cadrer", [
            ("sub", "Subtraction", 4, 0, {}),
            ("m", "Division", 5, 0, {"val": [(1, "Number", [1000])]}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("pts", "dec", 0), ("dec", "bor", 0), ("bor", "dd", 0),
           ("dd", 1, "sub", 0), ("dd", "sub", 1),
           ("sub", "m", 0), ("m", "pan", 0), ("m", "rep", 0)],
)

R["RH-12"] = _compte(
    u"ALTITUDES", V2.D_RH12_ALTITUDES, V2.D_RH12_NIVEAU, ">",
    u"Comparer chaque altitude au niveau. La sortie retenue est la "
    u"comparaison STRICTE : c'est ce que la consigne demande, et l'objet "
    u"posé exactement à 2 800 en dépend",
    u"Retenir les objets qui dépassent, puis les compter : 17. En comptant "
    u"« supérieur ou égal », on en trouverait 18")

R["RH-13"] = dict(
    sujet=[
        ("etat", "DATA:Boolean", 0, 0,
         {"nick": u"CALQUE_ALLUME",
          "data": [a for _n, a, _q in V2.D_RH13_CALQUES]}),
        ("qte", "DATA:Number", 0, 3,
         {"nick": u"OBJETS_PAR_CALQUE",
          "data": [q for _n, _a, q in V2.D_RH13_CALQUES]}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Ne retenir que les calques allumés", [
            ("cull", "Cull Pattern", 1, 0, {}),
        ]),
        (u"Sommer leurs objets : 176 visibles. Le fichier en contient 270 — "
         u"les 94 autres partiront chez le destinataire sans que personne "
         u"les ait vus, dont d'anciens relevés", [
            ("ma", "Mass Addition", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("qte", "cull", 0), ("etat", "cull", 1),
           ("cull", "ma", 0), ("ma", "pan", 0), ("ma", "rep", 0)],
)

R["RH-14"] = dict(
    sujet=[
        ("nx", "SLIDER", 0, 0,
         {"slider": (2, 20, V2.D_RH14["nx"], 0), "nick": u"Plots en longueur"}),
        ("ny", "SLIDER", 0, 1,
         {"slider": (2, 20, V2.D_RH14["ny"], 0), "nick": u"Plots en largeur"}),
        ("tx", "SLIDER", 0, 2,
         {"slider": (0, 10, V2.D_RH14["tremie"][0], 0), "nick": u"Tremie en longueur"}),
        ("ty", "SLIDER", 0, 3,
         {"slider": (0, 10, V2.D_RH14["tremie"][1], 0), "nick": u"Tremie en largeur"}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"La trame complète : 8 × 6 = 48 plots", [
            ("tot", "Multiplication", 1, 0, {}),
        ]),
        (u"La trémie retire un RECTANGLE de plots : 3 × 2 = 6, et non "
         u"3 + 2 = 5. Le plot qu'on aurait oublié de retirer se retrouve au "
         u"milieu de l'escalier", [
            ("tre", "Multiplication", 1, 3, {}),
        ]),
        (u"42 plots", [
            ("sub", "Subtraction", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("nx", "tot", 0), ("ny", "tot", 1),
           ("tx", "tre", 0), ("ty", "tre", 1),
           ("tot", "sub", 0), ("tre", "sub", 1),
           ("sub", "pan", 0), ("sub", "rep", 0)],
)

R["RH-15"] = dict(
    sujet=[
        ("pts", "DATA:Point", 0, 0,
         {"nick": u"SOMMETS_DU_CHEMINEMENT",
          "data": [(x, y, 0.0) for x, y in V2.D_RH15_PTS]}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Relier les sommets dans l'ordre, sans refermer : la consigne ne "
         u"le demande pas, et refermer ajouterait la corde de retour", [
            ("pl", "PolyLine", 1, 0, {}),
        ]),
        (u"Mesurer la COURBE, et non la distance entre ses extrémités. "
         u"13 400 mm développés contre 10 065 mm de corde : 3,3 m de "
         u"garde-corps qui manqueraient à la livraison", [
            ("lg", "Length", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("pts", "pl", 0), ("pl", "lg", 0),
           ("lg", "pan", 0), ("lg", "rep", 0)],
)

R["RH-16"] = dict(
    sujet=[
        ("base", "SLIDER", 0, 0,
         {"slider": (1000, 20000, V2.D_RH16["base"], 0), "nick": u"Longueur"}),
        ("prof", "SLIDER", 0, 1,
         {"slider": (500, 10000, V2.D_RH16["profondeur"], 0),
          "nick": u"Profondeur en projection"}),
        ("den", "SLIDER", 0, 2,
         {"slider": (0, 5000, V2.D_RH16["denivele"], 0), "nick": u"Denivele"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le rampant est l'hypoténuse : la projection et le dénivelé en "
         u"sont les côtés. 3 534 mm pour 3 200 de projection", [
            ("p2", "Multiplication", 1, 0, {}),
            ("d2", "Multiplication", 1, 2, {}),
            ("som", "Addition", 2, 0, {}),
            ("ram", "Square Root", 3, 0, {}),
        ]),
        (u"L'aire se mesure DANS le plan du rampant : 29,69 m². Prendre la "
         u"projection donnerait 26,88 m², soit 10 % de moins — de quoi "
         u"arrêter le chantier à trois rangs de la faîtière", [
            ("air", "Multiplication", 4, 0, {}),
            ("m2", "Division", 5, 0, {"val": [(1, "Number", [1000000])]}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("prof", "p2", 0), ("prof", "p2", 1),
           ("den", "d2", 0), ("den", "d2", 1),
           ("p2", "som", 0), ("d2", "som", 1), ("som", "ram", 0),
           ("base", "air", 0), ("ram", "air", 1),
           ("air", "m2", 0), ("m2", "pan", 0), ("m2", "rep", 0)],
)

_A17, _B17, _I17 = V2.D_RH17["a"], V2.D_RH17["b"], V2.D_RH17["intersection"]

R["RH-17"] = dict(
    sujet=[
        ("va", "DATA:Number", 0, 0,
         {"nick": u"MASSIF_A", "data": list(_A17)}),
        ("vb", "DATA:Number", 0, 2,
         {"nick": u"MASSIF_B", "data": list(_B17)}),
        ("vi", "DATA:Number", 0, 4,
         {"nick": u"RECOUVREMENT", "data": list(_I17)}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le volume de chaque parallélépipède est le produit de ses trois "
         u"dimensions — un produit cumulé sur la liste", [
            ("pa", "Mass Multiplication", 1, 0, {}),
            ("pb", "Mass Multiplication", 1, 2, {}),
            ("pi", "Mass Multiplication", 1, 4, {}),
        ]),
        (u"La réunion additionne les deux massifs puis retranche UNE FOIS "
         u"leur partie commune. L'additionner sans retrancher la compterait "
         u"deux fois : 5,4 dm³ de béton commandés pour rien", [
            ("som", "Addition", 2, 0, {}),
            ("uni", "Subtraction", 3, 0, {}),
        ]),
        (u"34,35 dm³, contre 39,75 si l'on additionne", [
            ("dm3", "Division", 4, 0, {"val": [(1, "Number", [1000000])]}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("va", "pa", 0), ("vb", "pb", 0), ("vi", "pi", 0),
           ("pa", "som", 0), ("pb", "som", 1),
           ("som", "uni", 0), ("pi", "uni", 1),
           ("uni", "dm3", 0), ("dm3", "pan", 0), ("dm3", "rep", 0)],
)

R["RH-18"] = _compte(
    u"EPAISSEURS_DE_PAROI", V2.D_RH18_PAROIS, V2.D_RH18_MINI, "<",
    u"Comparer chaque épaisseur au minimum imprimable. La comparaison est "
    u"STRICTE : le minimum est atteignable, c'est un minimum et non une "
    u"borne exclue",
    u"Compter les parois qui passent dessous : 5. En incluant celle qui vaut "
    u"exactement 1,2 mm, on en reprendrait une pour rien")

R["RH-19"] = dict(
    sujet=[
        ("det", "DATA:Number", 0, 0,
         {"nick": u"DETAILS_SUR_LA_MAQUETTE",
          "data": list(V2.D_RH19_DETAILS)}),
        ("fac", "SLIDER", 0, 3,
         {"slider": (1, 100, V2.D_RH19["facteur"], 0), "nick": u"Facteur d'echelle"}),
        ("res", "SLIDER", 0, 4,
         {"slider": (0.1, 2, V2.D_RH19["resolution"], 1), "nick": u"Resolution machine"}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Agrandir D'ABORD. C'est tout l'exercice : juger la finesse à "
         u"l'échelle où la pièce sera imprimée, et non à celle où elle a "
         u"été dessinée", [
            ("mul", "Multiplication", 1, 0, {}),
        ]),
        (u"Comparer ensuite à la résolution de la machine, et compter : 6 "
         u"détails restent trop fins. Avant agrandissement, les douze "
         u"l'étaient — et l'on aurait refait toute la maquette", [
            ("cmp", "Smaller Than", 2, 0, {}),
            ("cull", "Cull Pattern", 3, 0, {}),
            ("ll", "List Length", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("det", "mul", 0), ("fac", "mul", 1),
           ("mul", "cmp", 0), ("res", "cmp", 1),
           ("mul", "cull", 0), ("cmp", "cull", 1),
           ("cull", "ll", 0), ("ll", "pan", 0), ("ll", "rep", 0)],
)

R["RH-20"] = dict(
    sujet=[
        ("f", "SLIDER", 0, 0,
         {"slider": (100, 10000, V2.D_RH20["faces"], 0), "nick": u"Faces triangulaires"}),
        ("e", "SLIDER", 0, 1,
         {"slider": (100, 15000, V2.D_RH20["aretes"], 0), "nick": u"Aretes"}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Chaque triangle réclame trois arêtes : 8 880 usages d'arête au "
         u"total", [
            ("f3", "Multiplication", 1, 0, {"val": [(1, "Number", [3])]}),
        ]),
        (u"Chaque arête INTÉRIEURE en sert deux : 8 868 usages offerts. "
         u"Un maillage fermé de 2 960 triangles aurait exactement "
         u"4 440 arêtes", [
            ("e2", "Multiplication", 1, 2, {"val": [(1, "Number", [2])]}),
        ]),
        (u"La différence est le nombre d'arêtes qui ne bordent qu'une seule "
         u"face : 12 arêtes nues, soit 0,3 % du maillage. Invisible à "
         u"l'œil, rédhibitoire à la machine", [
            ("sub", "Subtraction", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("f", "f3", 0), ("e", "e2", 0),
           ("f3", "sub", 0), ("e2", "sub", 1),
           ("sub", "pan", 0), ("sub", "rep", 0)],
)

R["RH-21"] = _compte(
    u"AIRES_DES_FACES", V2.D_RH21_AIRES, V2.D_RH21_TOL, "<",
    u"Comparer chaque aire à la TOLÉRANCE du document, et non à zéro. "
    u"Aucune face n'a une aire nulle : elles valent quelques dix-millièmes, "
    u"ce qui n'est pas zéro et n'est rien",
    u"Compter les faces dégénérées : 4. Celle qui vaut 0,0012 passe juste "
    u"au-dessus de la tolérance et n'en est pas une")

R["RH-22"] = dict(
    sujet=[
        ("r", "SLIDER", 0, 0,
         {"slider": (1, 200, V2.D_RH22["rayon"], 0), "nick": u"Rayon"}),
        ("f", "SLIDER", 0, 1,
         {"slider": (0.01, 1, V2.D_RH22["fleche"], 2), "nick": u"Fleche admise"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'écart entre la corde et l'arc vaut r × (1 − cos(π/n)). On "
         u"inverse : cos de l'angle au sommet vaut 1 − flèche ÷ rayon", [
            ("rap", "Division", 1, 0, {}),
            ("un", "Subtraction", 2, 0, {"val": [(0, "Number", [1])]}),
            ("ang", "ArcCosine", 3, 0, {}),
        ]),
        (u"Le demi-tour vaut π : le nombre de facettes est π divisé par cet "
         u"angle, soit 54,41", [
            ("n", "Division", 4, 0, {"val": [(0, "Number", [3.14159265358979])]}),
        ]),
        (u"Arrondi au SUPÉRIEUR : 55 facettes. À 54, la flèche vaut déjà "
         u"0,0508 mm — au-delà du toléré, et rien à l'écran ne le signale", [
            ("rd", "Round", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("f", "rap", 0), ("r", "rap", 1),
           ("rap", "un", 1), ("un", "ang", 0),
           ("ang", "n", 1),
           ("n", "rd", 0),
           ("rd", 2, "pan", 0), ("rd", 2, "rep", 0)],
)


# ---------------------------------------------------------------------------
# Lot GP
# ---------------------------------------------------------------------------

R["GP-06"] = dict(
    sujet=[
        ("u", "SLIDER", 0, 0,
         {"slider": (1, 200, V2.D_GP06["u"], 0), "nick": u"Divisions en U"}),
        ("v", "SLIDER", 0, 1,
         {"slider": (1, 200, V2.D_GP06["v"], 0), "nick": u"Divisions en V"}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Une nappe de n divisions porte n + 1 rangées de sommets : c'est "
         u"le même écart qu'entre les intervalles et les piquets d'une "
         u"clôture", [
            ("u1", "Addition", 1, 0, {"val": [(1, "Number", [1])]}),
            ("v1", "Addition", 1, 2, {"val": [(1, "Number", [1])]}),
        ]),
        (u"49 × 31 = 1 519 sommets. Le nombre de FACES, lui, vaut 1 440 — "
         u"79 de moins, ce qui ne se voit pas sur l'image mais change la "
         u"taille du système à résoudre", [
            ("mul", "Multiplication", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("u", "u1", 0), ("v", "v1", 0),
           ("u1", "mul", 0), ("v1", "mul", 1),
           ("mul", "pan", 0), ("mul", "rep", 0)],
)

R["GP-07"] = dict(
    sujet=[
        ("u", "SLIDER", 0, 0,
         {"slider": (1, 200, V2.D_GP06["u"], 0), "nick": u"Divisions en U"}),
        ("v", "SLIDER", 0, 1,
         {"slider": (1, 200, V2.D_GP06["v"], 0), "nick": u"Divisions en V"}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Non soudé, chaque quadrangle porte ses quatre sommets sans savoir "
         u"que ses voisins portent les mêmes : 1 440 × 4 = 5 760", [
            ("f", "Multiplication", 1, 0, {}),
            ("brut", "Multiplication", 2, 0, {"val": [(1, "Number", [4])]}),
        ]),
        (u"Soudé, il n'en reste que 1 519", [
            ("u1", "Addition", 1, 3, {"val": [(1, "Number", [1])]}),
            ("v1", "Addition", 1, 5, {"val": [(1, "Number", [1])]}),
            ("net", "Multiplication", 2, 3, {}),
        ]),
        (u"4 241 sommets supprimés : le maillage brut était 3,8 fois plus "
         u"lourd que nécessaire. C'est la raison ordinaire d'un fichier "
         u"d'export inexplicablement gros", [
            ("sub", "Subtraction", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("u", "f", 0), ("v", "f", 1), ("f", "brut", 0),
           ("u", "u1", 0), ("v", "v1", 0),
           ("u1", "net", 0), ("v1", "net", 1),
           ("brut", "sub", 0), ("net", "sub", 1),
           ("sub", "pan", 0), ("sub", "rep", 0)],
)

R["GP-08"] = dict(
    sujet=[
        ("f", "SLIDER", 0, 0,
         {"slider": (1, 500, V2.D_GP08["faces"], 0), "nick": u"Faces de la cage"}),
        ("n", "SLIDER", 0, 1,
         {"slider": (0, 8, V2.D_GP08["passes"], 0), "nick": u"Passes de subdivision"}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Chaque passe quadruple ce que la précédente a produit : la "
         u"croissance est GÉOMÉTRIQUE, quatre à la puissance du nombre de "
         u"passes", [
            ("pow", "Power", 1, 0, {"val": [(0, "Number", [4])]}),
        ]),
        (u"26 × 4³ = 1 664 faces. Multiplier par trois passes en donnerait "
         u"78, une seule passe 104 : trois ordres de grandeur différents, "
         u"et c'est pourquoi une passe de plus, décidée sans y penser, rend "
         u"un modèle inutilisable", [
            ("mul", "Multiplication", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("n", "pow", 1), ("f", "mul", 0), ("pow", "mul", 1),
           ("mul", "pan", 0), ("mul", "rep", 0)],
)


# ---------------------------------------------------------------------------
# Lots QT et MP
# ---------------------------------------------------------------------------

_Q6 = V2.D_QT06

R["QT-06"] = dict(
    sujet=[
        ("mat", "SLIDER", 0, 0,
         {"slider": (0, 20000, _Q6["materiaux"], 2), "nick": u"Materiaux"}),
        ("h", "SLIDER", 0, 1,
         {"slider": (0, 200, _Q6["heures"], 1), "nick": u"Heures"}),
        ("t", "SLIDER", 0, 2,
         {"slider": (20, 120, _Q6["taux"], 0), "nick": u"Taux horaire"}),
        ("mg", "SLIDER", 0, 3,
         {"slider": (0, 0.5, _Q6["marge"], 2), "nick": u"Marge"}),
        ("tv", "SLIDER", 0, 4,
         {"slider": (0, 0.3, _Q6["tva"], 2), "nick": u"Taxe"}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"La main d'œuvre, puis le déboursé sec : matériaux et pose", [
            ("mo", "Multiplication", 1, 0, {}),
            ("sec", "Addition", 2, 0, {}),
        ]),
        (u"La marge s'applique au déboursé sec. L'oublier facturerait "
         u"6 490,55 € — un devis parfaitement plausible, et à prix "
         u"coûtant : 778,87 € qui ne rentreront pas", [
            ("cm", "Addition", 3, 2, {"val": [(1, "Number", [1])]}),
            ("ht", "Multiplication", 4, 0, {}),
        ]),
        (u"La taxe s'applique ensuite. Marge et taxe étant toutes deux "
         u"multiplicatives, leur ordre ne change rien — c'est l'oubli de "
         u"l'une qui se voit. 7 269,42 €", [
            ("ct", "Addition", 3, 5, {"val": [(1, "Number", [1])]}),
            ("ttc", "Multiplication", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("h", "mo", 0), ("t", "mo", 1),
           ("mat", "sec", 0), ("mo", "sec", 1),
           ("mg", "cm", 0), ("sec", "ht", 0), ("cm", "ht", 1),
           ("tv", "ct", 0), ("ht", "ttc", 0), ("ct", "ttc", 1),
           ("ttc", "pan", 0), ("ttc", "rep", 0)],
)


def _aval_mp04():
    g = V2.D_MP04_GRAPHE
    vus, pile = set(), [u"Largeur"]
    while pile:
        for s in g.get(pile.pop(), []):
            if s not in vus:
                vus.add(s)
                pile.append(s)
    return sorted(vus)


R["MP-04"] = _etalon(
    u"RECALCULES_EN_AVAL", _aval_mp04(), "Text",
    u"L'étalon porte ce que le parcours des liaisons désigne : les "
    u"composants situés EN AVAL de Largeur, atteints directement ou par une "
    u"chaîne. Hauteur, Essence et Prix unitaire n'en font pas partie — ils "
    u"alimentent le graphe sans dépendre de Largeur",
    u"Dix composants sur quatorze. Croire que tout repasse en ferait "
    u"treize, et conduirait à optimiser au mauvais endroit")


# ---------------------------------------------------------------------------
# Lot PL
# ---------------------------------------------------------------------------

def _fermeture_pl05():
    dep = V2A.D_PL05_DEPENDANCES
    vus, pile = set(), list(dep.get(V2A.D_PL05_CIBLE, []))
    while pile:
        n = pile.pop()
        if n in vus:
            continue
        vus.add(n)
        pile.extend(dep.get(n, []))
    return [V2A.D_PL05_CIBLE] + sorted(vus)


R["PL-05"] = _etalon(
    u"PAQUETS_A_EMPORTER", _fermeture_pl05(), "Text",
    u"L'étalon porte la fermeture du graphe : le paquet visé, et tout ce "
    u"dont il dépend de proche en proche. Noyau y figure UNE FOIS bien que "
    u"deux paquets l'exigent",
    u"Six paquets. S'arrêter aux dépendances directes en emporterait trois, "
    u"et l'installation s'arrêterait au premier maillon manquant")

R["PL-06"] = _etalon(
    u"POSTES_CAPABLES",
    [p for p, d in V2A.D_PL06_POSTES if set(V2A.D_PL06_REQUIS) <= set(d)],
    "Text",
    u"L'étalon nomme les postes qui possèdent les TROIS plugins requis. Il "
    u"en faut trois sur trois : un composant manquant suffit à rompre la "
    u"chaîne, et la définition ne rend alors rien",
    u"Trois postes sur sept. Compter ceux qui ont au moins un des trois en "
    u"donnerait six — et la livraison paraîtrait sans risque")

R["PL-07"] = dict(
    sujet=[
        ("nat", "DATA:Number", 0, 0,
         {"nick": u"COMPOSANTS_EN_NATIF",
          "data": [a for _n, a, _b in V2A.D_PL07_TACHES]}),
        ("plu", "DATA:Number", 0, 3,
         {"nick": u"COMPOSANTS_AVEC_PLUGIN",
          "data": [b for _n, _a, b in V2A.D_PL07_TACHES]}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Sommer les deux colonnes : 123 composants en natif, 8 avec les "
         u"plugins", [
            ("sn", "Mass Addition", 1, 0, {}),
            ("sp", "Mass Addition", 1, 3, {}),
        ]),
        (u"C'est l'ÉCART qui se met en balance avec le coût de la "
         u"dépendance : 115 composants épargnés, contre quatre postes sur "
         u"sept qui ne pourront plus ouvrir le fichier — c'est ce que PL-06 "
         u"mesure", [
            ("sub", "Subtraction", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("nat", "sn", 0), ("plu", "sp", 0),
           ("sn", "sub", 0), ("sp", "sub", 1),
           ("sub", "pan", 0), ("sub", "rep", 0)],
)

R["PL-08"] = _etalon(
    u"SURNOMS_MUETS",
    [s for s, parlant in V2A.D_PL08_SURNOMS if not parlant], "Text",
    u"L'étalon nomme les surnoms qui n'apprennent rien : six abréviations de "
    u"composants et quatre lettres seules. Le critère n'est pas la longueur "
    u"— « Jeu de pose » est court et parlant",
    u"Dix sur vingt-quatre, soit plus de quatre sur dix. La proportion "
    u"ordinaire d'une définition écrite sans intention de la faire relire")

R["PL-09"] = _compte(
    u"VERSION_EXIGEE", [v for _n, v in V2A.D_PL09_PLUGINS],
    V2A.D_PL09_CIBLE, "<",
    u"La version déclarée est un PLANCHER : un plugin écrit pour Rhino 6 "
    u"s'installe sur Rhino 8. La comparaison retenue est donc « au plus la "
    u"version du poste », sortie « ou égal à » comprise",
    u"Sept plugins sur neuf. Chercher l'égalité exacte n'en trouverait que "
    u"trois ; ce sont les deux qui exigent Rhino 9 qui ne passeront pas",
    sortie=1)


# ---------------------------------------------------------------------------
# Lot DV
# ---------------------------------------------------------------------------

R["DV-08"] = dict(
    sujet=[
        ("a", "SLIDER", 0, 0,
         {"slider": (1, 10, V2A.D_DV08["niveau_a"], 0), "nick": u"Valeurs du niveau A"}),
        ("b", "SLIDER", 0, 1,
         {"slider": (1, 10, V2A.D_DV08["niveau_b"], 0), "nick": u"Valeurs du niveau B"}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'arbre de départ porte une branche par combinaison : 3 × 4 = 12 "
         u"chemins {A;B}", [
            ("dep", "Multiplication", 1, 0, {}),
            ("pan0", "PANEL", 2, 0, {}),
        ]),
        (u"Le remappage laisse tomber le premier maillon. Les branches qui "
         u"ne différaient QUE par lui fusionnent : il reste autant de "
         u"chemins que le second niveau a de valeurs, soit 4 — et chacune "
         u"porte désormais trois fois plus de données", [
            ("res", "Addition", 3, 0, {"val": [(1, "Number", [0])]}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("a", "dep", 0), ("b", "dep", 1), ("dep", "pan0", 0),
           ("b", "res", 0), ("res", "pan", 0), ("res", "rep", 0)],
)

R["DV-09"] = dict(
    sujet=[
        ("val", "DATA:Number", 0, 0,
         {"nick": u"QUANTITES", "data": list(V2A.D_DV09_VALEURS)}),
        ("div", "DATA:Number", 0, 3,
         {"nick": u"DIVISEUR", "data": [V2A.D_DV09_DIVISEUR]}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"La division réelle donne 1,75 pour 7 ÷ 4. Ce n'est pas ce que "
         u"fait le langage sur deux ENTIERS", [
            ("dv", "Division", 1, 0, {}),
        ]),
        (u"Sur des entiers, la division TRONQUE : elle prend la partie "
         u"entière inférieure, elle n'arrondit pas. La sortie retenue est "
         u"donc le plancher, pas le plus proche", [
            ("rd", "Round", 2, 0, {}),
        ]),
        (u"32, contre 37 en réel. Aucune des dix quantités n'est multiple "
         u"de 4 : la troncature agit à chaque terme et l'écart s'accumule. "
         u"Les deux valeurs sont assez proches pour paraître toutes deux "
         u"crédibles — c'est exactement le danger", [
            ("ma", "Mass Addition", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("val", "dv", 0), ("div", "dv", 1),
           ("dv", "rd", 0),
           ("rd", 1, "ma", 0),
           ("ma", "pan", 0), ("ma", "rep", 0)],
)


# ---------------------------------------------------------------------------
# Lot IA
# ---------------------------------------------------------------------------

def _effectifs_ia19():
    bas, haut = V2A.D_IA19_SEUILS
    d = V2A.D_IA19_DEBITS
    return [sum(1 for x in d if x < bas),
            sum(1 for x in d if bas <= x < haut),
            sum(1 for x in d if x >= haut)]


R["IA-19"] = dict(
    sujet=[
        ("deb", "DATA:Number", 0, 0,
         {"nick": u"LONGUEURS_DU_DEBIT", "data": list(V2A.D_IA19_DEBITS)}),
        ("s", "DATA:Number", 0, 3,
         {"nick": u"SEUILS", "data": list(V2A.D_IA19_SEUILS)}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Les trois effectifs, relevés famille par famille : 9 petits, "
         u"8 moyens, 7 grands. La borne haute est EXCLUE du moyen — « jusqu'à "
         u"900 exclus » n'est pas « jusqu'à 900 »", [
            ("eff", "DATA:Number", 1, 0,
             {"nick": u"EFFECTIFS", "data": _effectifs_ia19()}),
        ]),
        (u"Le plus grand des trois : 9. C'est la famille des PETITS, ce qui "
         u"est contre-intuitif — les grands occupent plus de place, ils ne "
         u"sont pas plus nombreux. Les trois effectifs sont assez proches "
         u"pour qu'un comptage à l'œil se trompe de famille", [
            ("bor", "Bounds", 2, 0, {}),
            ("dd", "Deconstruct Domain", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("eff", "bor", 0), ("bor", "dd", 0),
           ("dd", 1, "pan", 0), ("dd", 1, "rep", 0)],
)

R["IA-20"] = dict(
    sujet=[
        ("b", "SLIDER", 0, 0,
         {"slider": (1, 48, V2A.D_IA20["budget_heures"], 1), "nick": u"Budget en heures"}),
        ("d", "SLIDER", 0, 1,
         {"slider": (1, 300, V2A.D_IA20["duree_seconde"], 0),
          "nick": u"Duree d'une evaluation"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le budget en secondes : 6 heures font 21 600 secondes", [
            ("sec", "Multiplication", 1, 0, {"val": [(1, "Number", [3600])]}),
        ]),
        (u"Divisé par la durée d'une évaluation, puis arrondi à l'entier "
         u"INFÉRIEUR : une évaluation entamée ne compte pas. 514 essais", [
            ("dv", "Division", 2, 0, {}),
            ("rd", "Round", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
        (u"À comparer aux 244 millions d'évaluations qu'exigerait "
         u"l'exploration complète de douze paramètres à cinq niveaux — "
         u"trois cent vingt-cinq ans de machine. Ce n'est pas une question "
         u"de patience : c'est ce qui rend le métamodèle nécessaire", [
            ("note", "PANEL", 4, 2,
             {"text": u"514 essais tenables.\n"
                      u"244 140 625 essais pour l'exhaustif.\n\n"
                      u"Le plan d'experiences se CHOISIT.",
              "h": 80, "w": 280}),
        ]),
    ],
    wires=[("b", "sec", 0), ("sec", "dv", 0), ("d", "dv", 1),
           ("dv", "rd", 0),
           ("rd", 1, "pan", 0), ("rd", 1, "rep", 0)],
)

R["IA-21"] = dict(
    sujet=[
        ("l", "SLIDER", 0, 0,
         {"slider": (1000, 50000, V2A.D_IA21["longueur"], 0), "nick": u"Longueur de la file"}),
        ("e", "SLIDER", 0, 1,
         {"slider": (500, 5000, V2A.D_IA21["entraxe_max"], 0), "nick": u"Entraxe maximal"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"18 600 ÷ 2 500 vaut 7,44. Arrondi au SUPÉRIEUR : huit travées, "
         u"d'où un entraxe réel de 2 325 mm. Arrondir au plus proche "
         u"donnerait sept travées et 2 657 mm — au-delà du maximum", [
            ("dv", "Division", 1, 0, {}),
            ("rd", "Round", 2, 0, {}),
        ]),
        (u"Les poteaux sont un de plus que les travées : 9. Un script qui "
         u"divise et arrondit sans se demander ce qu'il compte rend 8 — "
         u"plausible, du bon ordre de grandeur, et il manque le poteau du "
         u"bout, celui qui tient la clôture", [
            ("add", "Addition", 3, 0, {"val": [(1, "Number", [1])]}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("l", "dv", 0), ("e", "dv", 1),
           ("dv", "rd", 0), ("rd", 2, "add", 0),
           ("add", "pan", 0), ("add", "rep", 0)],
)

R["IA-22"] = dict(
    sujet=[
        ("val", "DATA:Number", 0, 0,
         {"nick": u"QUANTITES", "data": list(V2A.D_IA22_VALEURS)}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"La règle du métier — la demie monte — s'écrit explicitement : "
         u"ajouter un demi, puis prendre le plancher. Elle ne dépend alors "
         u"plus du langage", [
            ("add", "Addition", 1, 0, {"val": [(1, "Number", [0.5])]}),
            ("rd", "Round", 2, 0, {}),
        ]),
        (u"170. L'arrondi par défaut de la plupart des langages envoie la "
         u"demie vers le nombre PAIR — 2,5 donne 2, 3,5 donne 4 — pour ne "
         u"pas biaiser les sommes. C'est statistiquement vertueux et "
         u"commercialement faux : six unités s'évaporent sur douze lignes", [
            ("ma", "Mass Addition", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("val", "add", 0), ("add", "rd", 0),
           ("rd", 1, "ma", 0),
           ("ma", "pan", 0), ("ma", "rep", 0)],
)

R["IA-23"] = dict(
    sujet=[
        ("tour", "DATA:Number", 0, 0,
         {"nick": u"NUMERO_DE_TOUR",
          "data": [t for t, _p in V2A.D_IA23_TOURS]}),
        ("pass", "DATA:Number", 0, 3,
         {"nick": u"CAS_QUI_PASSENT",
          "data": [p for _t, p in V2A.D_IA23_TOURS]}),
        ("cible", "DATA:Number", 0, 5,
         {"nick": u"CAS_A_SATISFAIRE", "data": [V2A.D_IA23_CIBLE]}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Comparer, tour par tour, les cas qui passent à la cible. La "
         u"sortie retenue est « ou égal » : atteindre la cible suffit", [
            ("ge", "Larger Than", 1, 0, {}),
        ]),
        (u"Ne garder que les tours qui l'atteignent, et prendre le PREMIER. "
         u"Le cinquième n'a rien amélioré : il a coûté un aller-retour pour "
         u"confirmer que le quatrième suffisait", [
            ("cull", "Cull Pattern", 2, 0, {}),
            ("prem", "List Item", 3, 0, {"val": [(1, "Integer", [0])]}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
        (u"Ce que l'exercice ne dit pas, et qui suit : dix-huit cas qui "
         u"passent ne font pas un composant juste. Ils font un composant "
         u"juste SUR CES CAS", [
            ("note", "PANEL", 4, 2,
             {"text": u"Une iteration sans critere d'arret\n"
                      u"ne s'arrete pas : elle s'epuise.\n\n"
                      u"La suite est d'ecrire les cas\n"
                      u"qui manquent.",
              "h": 86, "w": 270}),
        ]),
    ],
    wires=[("pass", "ge", 0), ("cible", "ge", 1),
           ("tour", "cull", 0), ("ge", 1, "cull", 1),
           ("cull", "prem", 0),
           ("prem", "pan", 0), ("prem", "rep", 0)],
)

_I25 = V2A.D_IA25

R["IA-25"] = dict(
    sujet=[
        ("req", "SLIDER", 0, 0,
         {"slider": (100, 50000, _I25["requetes"], 0), "nick": u"Requetes par mois"}),
        ("je", "SLIDER", 0, 1,
         {"slider": (100, 10000, _I25["jetons_entree"], 0), "nick": u"Jetons en entree"}),
        ("js", "SLIDER", 0, 2,
         {"slider": (10, 5000, _I25["jetons_sortie"], 0), "nick": u"Jetons en sortie"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Les jetons du mois, séparément : l'entrée et la sortie ne "
         u"coûtent pas le même prix", [
            ("te", "Multiplication", 1, 0, {}),
            ("ts", "Multiplication", 1, 3, {}),
        ]),
        (u"Chacun à SON tarif : 3 € le million en entrée, 15 € en sortie. "
         u"La sortie coûte cinq fois l'entrée, et c'est structurel — elle se "
         u"produit jeton par jeton", [
            ("ce", "Multiplication", 2, 0,
             {"val": [(1, "Number", [_I25["prix_entree"]])]}),
            ("cs", "Multiplication", 2, 3,
             {"val": [(1, "Number", [_I25["prix_sortie"]])]}),
        ]),
        (u"43,47 € par mois. Un tarif unique aurait annoncé 27,34 €. "
         u"Malgré un rapport de six contre un en VOLUME, la sortie pèse "
         u"36 % de la facture : c'est ce renversement que le calcul fait "
         u"apparaître", [
            ("som", "Addition", 3, 0, {}),
            ("eur", "Division", 4, 0, {"val": [(1, "Number", [1000000])]}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("req", "te", 0), ("je", "te", 1),
           ("req", "ts", 0), ("js", "ts", 1),
           ("te", "ce", 0), ("ts", "cs", 0),
           ("ce", "som", 0), ("cs", "som", 1),
           ("som", "eur", 0), ("eur", "pan", 0), ("eur", "rep", 0)],
)


# ---------------------------------------------------------------------------
# Les quatre questions charnieres de la vague 2
# ---------------------------------------------------------------------------

R["PL-10"] = recette_charniere(_e("PL-10"),
    u"Le binaire est le meme.\n"
    u"Ce qui l'entoure ne l'est pas :\n"
    u"dependances, mise a jour,\n"
    u"desinstallation.")

R["PL-11"] = recette_charniere(_e("PL-11"),
    u"Ergonomie   : rien dans le fichier livre.\n"
    u"Fonctionnel : une dependance qui suit\n"
    u"              le fichier partout.\n\n"
    u"C'est ce que PL-06 mesure.")

R["PL-12"] = recette_charniere(_e("PL-12"),
    u"Figer Rhino gele aussi tout le reste,\n"
    u"et le probleme revient dans un an.\n\n"
    u"Savoir CE QUE le plugin fait encore\n"
    u"precede le choix d'un remplacant.")

R["IA-24"] = recette_charniere(_e("IA-24"),
    u"L'absence de message EST l'information.\n\n"
    u"Un composant mal ecrit leve une erreur.\n"
    u"Un composant jamais charge ne dit rien.")
