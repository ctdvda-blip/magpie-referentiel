# -*- coding: utf-8 -*-
"""Recette d'AV-01 — convergence par bissection.

PARTI PRIS
----------
L'exercice se monte avec un plugin de boucle : c'est bien la construction de
l'iteration qui est evaluee. Mais le RESULTAT, lui, se calcule sans boucle —
une bissection divise l'intervalle par deux a chaque passage, et le nombre de
passages necessaires pour descendre sous un critere vaut le logarithme en
base 2 du rapport, arrondi au superieur.

La zone corrige porte donc cet ETALON natif, pas une reproduction de la boucle.
C'est le meme choix que pour le lot RH : le corrige n'est pas la solution a
recopier, c'est de quoi verifier la sienne. Et il porte ici un enseignement en
plus — savoir qu'un calcul direct existe evite de faire tourner une boucle pour
repondre a une question qui n'en demandait pas.
"""
import os
import sys

_ICI = os.path.dirname(os.path.abspath(__file__))
_GEN = os.path.abspath(os.path.join(_ICI, ".."))
for _p in (_ICI, _GEN):
    if _p not in sys.path:
        sys.path.insert(0, _p)

R = {}

R["AV-01"] = dict(
    sujet=[
        ("bas", "SLIDER", 0, 0,
         {"slider": (0, 3000, 1000, 0), "nick": u"Borne basse"}),
        ("haut", "SLIDER", 0, 1,
         {"slider": (1000, 8000, 4000, 0), "nick": u"Borne haute"}),
        ("crit", "SLIDER", 0, 2,
         {"slider": (0.1, 10, 1, 1), "nick": u"Critere d'arret"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon ne reproduit pas la boucle : il calcule directement ce "
         u"qu'elle doit trouver. L'intervalle de départ mesure 3 000 mm", [
            ("etendue", "Subtraction", 1, 0, {}),
        ]),
        (u"Chaque bissection le divise par deux. Le nombre de passages "
         u"nécessaires pour descendre sous le critère est donc le logarithme "
         u"en base 2 du rapport : log₂(3 000 ÷ 1) vaut 11,55", [
            ("rap", "Division", 2, 0, {}),
            ("lg", "Log N", 3, 0, {"val": [(1, "Number", [2])]}),
        ]),
        (u"Arrondi au SUPÉRIEUR : onze bissections laissent encore 1,46 mm, "
         u"douze descendent à 0,73. Il en faut donc 12 — et c'est le CRITÈRE "
         u"qui doit commander la sortie de boucle, jamais un compte fixé "
         u"d'avance", [
            ("rd", "Round", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
        (u"Ce que l'étalon enseigne en passant : quand un calcul direct "
         u"existe, faire tourner une boucle pour l'obtenir est un détour. "
         u"Savoir le reconnaître fait partie de la compétence", [
            ("note", "PANEL", 5, 2,
             {"text": u"11 bissections -> 1.46 mm\n"
                      u"12 bissections -> 0.73 mm\n\n"
                      u"Sortir sur le CRITERE, non sur un compte.",
              "h": 86, "w": 280}),
        ]),
    ],
    wires=[("haut", "etendue", 0), ("bas", "etendue", 1),
           ("etendue", "rap", 0), ("crit", "rap", 1),
           ("rap", "lg", 0),
           ("lg", "rd", 0),
           ("rd", 2, "pan", 0), ("rd", 2, "rep", 0)],
)


# ---------------------------------------------------------------------------
# AV-02 — la chainette qui se stabilise
# ---------------------------------------------------------------------------
#
# Meme parti pris qu'AV-01. Le sujet demande une RELAXATION : c'est la
# construction de la simulation qui est evaluee. Mais la forme d'equilibre
# d'un fil pesant porte un nom depuis Huygens — c'est une chainette — et
# Grasshopper sait la tracer d'un composant. L'etalon la trace donc, et sert
# de reference a la forme relachee.
#
# L'enseignement en passant est le meme, et il est le vrai sujet de ce lot :
# une simulation n'est pas une reponse, c'est une methode. Quand la forme
# cherchee a une expression connue, la simulation sert a la retrouver, pas a
# la decouvrir — et elle doit tomber dessus.

R["AV-02"] = dict(
    sujet=[
        ("lo", "SLIDER", 0, 0,
         {"slider": (4000, 8000, 6000, 0), "nick": u"Longueur du cable"}),
        ("po", "SLIDER", 0, 1,
         {"slider": (2000, 6000, 4800, 0), "nick": u"Portee entre ancrages"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Les deux ancrages, à 4 800 mm l'un de l'autre et à la même "
         u"altitude", [
            ("a", "GEO:Point", 1, 0,
             {"nick": u"ANCRAGE_A", "geo": ("pts", [(0.0, 0.0, 0.0)])}),
            ("b", "GEO:Point", 1, 2,
             {"nick": u"ANCRAGE_B", "geo": ("pts", [(4800.0, 0.0, 0.0)])}),
        ]),
        (u"6 000 mm de câble pour 4 800 mm de portée : un quart de mou. "
         u"La pesanteur descend, et c'est elle qui donne la forme — un câble "
         u"sans poids resterait tendu en ligne droite", [
            ("lg", "DATA:Number", 1, 4,
             {"nick": u"LONGUEUR_DU_CABLE", "data": [6000]}),
            ("g", "Unit Z", 1, 6, {"val": [(0, "Number", [-1])]}),
            ("cat", "Catenary", 2, 0, {}),
        ]),
        (u"Échantillonner la courbe, puis n'en garder que les altitudes", [
            ("n", "DATA:Integer", 2, 4,
             {"nick": u"NOMBRE_DE_POINTS", "data": [2000]}),
            ("dc", "Divide Curve", 3, 0, {}),
            ("dec", "Deconstruct", 4, 0, {}),
        ]),
        (u"La flèche est l'écart entre les ancrages et le point bas : "
         u"l'altitude la plus basse, prise au signe près. Mesurer la corde "
         u"du câble au lieu de sa flèche donnerait 4 800 mm — la portée, "
         u"que l'on connaissait déjà", [
            ("bd", "Bounds", 5, 0, {}),
            ("dd", "Deconstruct Domain", 6, 0, {}),
            ("ab", "Absolute", 7, 0, {}),
            ("pan", "PANEL", 7, 2, {}),
        ]),
    ],
    wires=[("a", "cat", 0), ("b", "cat", 1), ("lg", "cat", 2), ("g", "cat", 3),
           ("cat", "dc", 0), ("n", "dc", 1),
           ("dc", "dec", 0),
           ("dec", 2, "bd", 0),
           ("bd", "dd", 0),
           ("dd", "ab", 0),
           ("ab", "pan", 0), ("ab", "rep", 0)],
)
