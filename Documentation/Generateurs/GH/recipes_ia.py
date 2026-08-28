# -*- coding: utf-8 -*-
"""Recettes de construction des definitions Grasshopper du lot IA.

Meme moteur et memes conventions que le lot A : bandeau, ZONE_SUJET,
separateur, ZONE_CORRIGE en groupes d'etapes, corrige masque par un
interrupteur et sans aucun cable vers la zone sujet.

PARTI PRIS
----------
Une partie de ce lot se joue HORS de Grasshopper : un assistant ecrit le code,
un agent conduit un projet de plugin, un modele de langage lit un texte. La
definition ne peut donc pas contenir la solution.

Ce que la zone corrige apporte alors, c'est le CONTROLE INDEPENDANT : le meme
resultat obtenu avec des composants natifs, sans assistance. C'est exactement
ce que les enonces demandent — verifier ce que l'outil renvoie par un moyen qui
n'emprunte pas le meme chemin. Le corrige n'est donc pas la reponse a recopier,
c'est l'etalon.

IA-07 (developpement d'un plugin .gha) ne recoit pas de definition : il n'y a
rien a monter dans Grasshopper, et fabriquer un fichier vide pour la forme
serait trompeur.
"""
import os
import sys

_GEN = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
if _GEN not in sys.path:
    sys.path.insert(0, _GEN)

import domaine_ia as D
import skill_a as S

R = {}

# ===========================================================================
# IA1 · Formuler et cadrer une demande
# ===========================================================================

R["IA-01"] = dict(
    sujet=[
        ("data", "DATA:Number", 0, 0,
         {"nick": u"ENTRAXES_RELEVES", "data": list(D.D_IA01)}),
        ("nom", "SLIDER", 0, 2,
         {"slider": (200, 300, 250, 0), "nick": u"Nominale"}),
        ("tol", "SLIDER", 0, 3,
         {"slider": (0, 5, 1.5, 1), "nick": u"Tolerance"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le corrigé n'est pas la solution : c'est le contrôle indépendant. "
         u"On monte ici, avec des composants natifs, le comptage que le "
         u"composant produit par l'assistant devra retrouver.", [
            ("sub", "Subtraction", 1, 0, {}),
        ]),
        (u"Valeur absolue de l'écart : une platine trop courte est aussi hors "
         u"tolérance qu'une platine trop longue", [
            ("abs", "Absolute", 2, 0, {}),
        ]),
        (u"Comparer l'écart à la tolérance", [
            ("lt", "Larger Than", 3, 0, {}),
        ]),
        (u"Sommer les booléens : 6 platines trop grandes et 4 trop petites, "
         u"soit 10", [
            ("ma", "Mass Addition", 4, 0, {}),
            ("pan", "PANEL", 5, 1, {}),
        ]),
    ],
    wires=[("data", "sub", 0), ("nom", "sub", 1),
           ("sub", "abs", 0), ("abs", "lt", 0), ("tol", "lt", 1),
           ("lt", "ma", 0), ("ma", "pan", 0), ("ma", "rep", 0)],
)

R["IA-02"] = dict(
    sujet=[
        ("qcm", "VALUELIST", 0, 0,
         {"nick": u"REPONSE_QCM",
          "items": [(u"0 - la version de Rhino et la bibliotheque visee", "0"),
                    (u"1 - le nom du composant", "1"),
                    (u"2 - la couleur de l'icone", "2"),
                    (u"3 - rien, les assistants n'ecrivent pas de composant", "3")]}),
        ("rep", "REPONSE", 3, 0, {"type": "Integer"}),
    ],
    corrige=[
        (u"La réponse est 0. Le modèle a produit du code valide — pour une "
         u"autre version de l'interface de programmation. Nommer la version "
         u"déplace le problème de « l'outil ne marche pas » à « ma demande "
         u"était incomplète », qui est la seule formulation sur laquelle on "
         u"peut agir.", [
            ("pan", "PANEL", 1, 2,
             {"text": u"Contexte minimal a fournir :\n"
                      u"- Rhino 8, Grasshopper 1.0\n"
                      u"- RhinoCommon, cible .NET du composant script\n"
                      u"- langage : C# / Python 3 / VB.NET\n"
                      u"- acces aux parametres : element, liste ou arbre",
              "h": 120, "w": 260}),
            ("bonne", "DATA:Integer", 2, 0,
             {"nick": u"BONNE_REPONSE", "data": [0]}),
        ]),
    ],
    wires=[("bonne", "rep", 0)],
)

R["IA-03"] = dict(
    sujet=[
        ("data", "DATA:Number", 0, 0,
         {"nick": u"NIVEAUX_RELEVES", "data": list(D.D_IA03)}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Encadrer le relevé : on obtient l'intervalle du plus bas au plus "
         u"haut", [
            ("bd", "Bounds", 1, 0, {}),
        ]),
        (u"Séparer les deux bornes de l'intervalle", [
            ("dd", "Deconstruct Domain", 2, 0, {}),
        ]),
        (u"L'amplitude est la différence des deux bornes : 25 − (−23) = 48. "
         u"La plus grande valeur absolue vaudrait 25 : c'est la réponse que "
         u"donne une demande mal formulée.", [
            ("sub", "Subtraction", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("data", "bd", 0), ("bd", "dd", 0),
           ("dd", 1, "sub", 0), ("dd", 0, "sub", 1),
           ("sub", "pan", 0), ("sub", "rep", 0)],
)

# ===========================================================================
# IA2 · Composants scriptes assistes
# ===========================================================================

R["IA-04"] = dict(
    sujet=[
        ("lg", "DATA:Number", 0, 0,
         {"nick": u"LONGUEURS_M", "data": list(D.D_IA02_L)}),
        ("di", "DATA:Number", 0, 2,
         {"nick": u"DIAMETRES_MM", "data": [float(x) for x in D.D_IA02_D]}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Ramener les diamètres en mètres : les deux listes doivent parler "
         u"la même unité avant toute multiplication", [
            ("div", "Division", 1, 2, {"val": [(1, "Number", [1000])]}),
        ]),
        (u"Périmètre de chaque section : π × diamètre", [
            ("pi", "Pi", 1, 4, {"val": [(0, "Number", [1])]}),
            ("mul1", "Multiplication", 2, 2, {}),
        ]),
        (u"Surface développée de chaque tronçon : périmètre × longueur", [
            ("mul2", "Multiplication", 3, 0, {}),
        ]),
        (u"Somme des seize tronçons : 58,03 m²", [
            ("ma", "Mass Addition", 4, 0, {}),
            ("pan", "PANEL", 5, 1, {}),
        ]),
    ],
    wires=[("di", "div", 0), ("div", "mul1", 0), ("pi", "mul1", 1),
           ("mul1", "mul2", 0), ("lg", "mul2", 1),
           ("mul2", "ma", 0), ("ma", "pan", 0), ("ma", "rep", 0)],
)

R["IA-05"] = dict(
    sujet=[
        ("data", "DATA:Number", 0, 0,
         {"nick": u"LONGUEURS_TRONCONS_M", "data": list(D.D_IA02_L)}),
        ("seuil", "SLIDER", 0, 2,
         {"slider": (0, 10, 4, 0), "nick": u"Longueur de transport"}),
        ("faux", "PANEL", 0, 3,
         {"text": u"COMPOSANT FOURNI\nannonce : 7 troncons",
          "h": 60, "w": 200}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Établir d'abord la réponse juste, sans regarder le code : "
         u"comparer chaque longueur au seuil de transport", [
            ("lt", "Larger Than", 1, 0, {}),
        ]),
        (u"Compter les tronçons concernés : 9, et non 7. L'écart vaut 2 — "
         u"c'est cet écart-là qu'il faut aller chercher dans le code, "
         u"pas « une erreur » en général.", [
            ("ma", "Mass Addition", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
        (u"Le code fourni s'exécute sans rien signaler : l'absence d'erreur "
         u"ne dit rien de la justesse.", [
            ("note", "PANEL", 3, 2,
             {"text": u"Un composant qui ne plante pas\n"
                      u"n'est pas un composant juste.",
              "h": 60, "w": 200}),
        ]),
    ],
    wires=[("data", "lt", 0), ("seuil", "lt", 1),
           ("lt", "ma", 0), ("ma", "pan", 0), ("ma", "rep", 0)],
)

R["IA-06"] = dict(
    sujet=[
        ("data", "DATA:Number", 0, 0,
         {"nick": u"LONGUEURS_M", "data": list(D.D_IA02_L)}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le composant d'origine produit les sommes cumulées. L'étalon natif "
         u"les fournit sans écrire une ligne de code : c'est contre cette "
         u"liste que la version portée doit être comparée, élément par "
         u"élément.", [
            ("ma", "Mass Addition", 1, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
        (u"Comparer les longueurs de liste ne suffit pas : deux "
         u"implémentations peuvent diverger sur un seul rang et coïncider "
         u"partout ailleurs.", [
            ("ll", "List Length", 2, 2, {}),
            ("pan2", "PANEL", 3, 2, {}),
        ]),
    ],
    wires=[("data", "ma", 0), ("ma", 1, "pan", 0), ("ma", 1, "rep", 0),
           ("ma", 1, "ll", 0), ("ll", "pan2", 0)],
)

# ===========================================================================
# IA3 · Developpement de plugins assiste
# IA-07 n'a pas de definition : le livrable est un plugin compile.
# ===========================================================================

R["IA-08"] = dict(
    sujet=[
        ("qcm", "VALUELIST", 0, 0,
         {"nick": u"REPONSE_QCM",
          "items": [(u"0 - le nom du composant a change", "0"),
                    (u"1 - le GUID du composant a ete regenere", "1"),
                    (u"2 - le plugin n'est pas signe", "2"),
                    (u"3 - il faut vider le cache de Grasshopper", "3")]}),
        ("rep", "REPONSE", 3, 0, {"type": "Integer"}),
    ],
    corrige=[
        (u"La réponse est 1. Le nom peut changer sans rien casser : c'est le "
         u"GUID qui identifie le composant dans les fichiers enregistrés. "
         u"Un GUID régénéré transforme chaque composant posé en composant "
         u"manquant, et le symptôme n'apparaît que chez les collègues.", [
            ("pan", "PANEL", 1, 2,
             {"text": u"A figer des la premiere version :\n"
                      u"- le GUID de chaque composant\n"
                      u"- le nom de la categorie et de l'onglet\n"
                      u"- le nom des entrees et sorties\n\n"
                      u"Peut changer librement :\n"
                      u"- le libelle affiche, l'icone, l'aide",
              "h": 140, "w": 280}),
            ("bonne", "DATA:Integer", 2, 0,
             {"nick": u"BONNE_REPONSE", "data": [1]}),
        ]),
    ],
    wires=[("bonne", "rep", 0)],
)

# ===========================================================================
# IA4 · Apprentissage automatique
# ===========================================================================

R["IA-09"] = dict(
    sujet=[
        ("sx", "DATA:Number", 0, 0,
         {"nick": u"SURFACES_M2", "data": list(D.D_IA05_S)}),
        ("wy", "DATA:Number", 0, 2,
         {"nick": u"DEPERDITIONS_W", "data": [float(v) for v in D.D_IA05_W]}),
        ("cible", "SLIDER", 0, 4,
         {"slider": (0, 5, 2.75, 2), "nick": u"Surface a estimer"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon natif d'un ajustement affine : on n'appelle aucun plugin, "
         u"on calcule les quatre sommes dont la droite des moindres carrés a "
         u"besoin. Σx, Σy, Σxy et Σx².", [
            ("sumx", "Mass Addition", 1, 0, {}),
            ("sumy", "Mass Addition", 1, 2, {}),
            ("mxy", "Multiplication", 1, 4, {}),
            ("sumxy", "Mass Addition", 2, 4, {}),
            ("mxx", "Multiplication", 1, 6, {}),
            ("sumxx", "Mass Addition", 2, 6, {}),
        ]),
        (u"Pente de la droite : a = (n·Σxy − Σx·Σy) / (n·Σx² − Σx·Σx), "
         u"avec n = 24", [
            ("n1", "Multiplication", 3, 4, {"val": [(1, "Number", [24])]}),
            ("pxy", "Multiplication", 3, 2, {}),
            ("num", "Subtraction", 4, 3, {}),
            ("n2", "Multiplication", 3, 6, {"val": [(1, "Number", [24])]}),
            ("pxx", "Multiplication", 3, 8, {}),
            ("den", "Subtraction", 4, 7, {}),
            ("a", "Division", 5, 5, {}),
        ]),
        (u"Ordonnée à l'origine : b = (Σy − a·Σx) / n", [
            ("asx", "Multiplication", 6, 1, {}),
            ("dif", "Subtraction", 7, 1, {}),
            ("b", "Division", 8, 1, {"val": [(1, "Number", [24])]}),
        ]),
        (u"Prédiction pour la surface visée : environ 380 W. Un apprenant qui "
         u"répond par la moyenne des déperditions obtient un ordre de grandeur "
         u"voisin — et une erreur qui explose sur les baies extrêmes.", [
            ("acx", "Multiplication", 6, 9, {}),
            ("pred", "Addition", 7, 9, {}),
            ("pan", "PANEL", 8, 9, {}),
        ]),
    ],
    wires=[("sx", "sumx", 0), ("wy", "sumy", 0),
           ("sx", "mxy", 0), ("wy", "mxy", 1), ("mxy", "sumxy", 0),
           ("sx", "mxx", 0), ("sx", "mxx", 1), ("mxx", "sumxx", 0),
           ("sumxy", "n1", 0),
           ("sumx", "pxy", 0), ("sumy", "pxy", 1),
           ("n1", "num", 0), ("pxy", "num", 1),
           ("sumxx", "n2", 0),
           ("sumx", "pxx", 0), ("sumx", "pxx", 1),
           ("n2", "den", 0), ("pxx", "den", 1),
           ("num", "a", 0), ("den", "a", 1),
           ("a", "asx", 0), ("sumx", "asx", 1),
           ("sumy", "dif", 0), ("asx", "dif", 1),
           ("dif", "b", 0),
           ("a", "acx", 0), ("cible", "acx", 1),
           ("acx", "pred", 0), ("b", "pred", 1),
           ("pred", "pan", 0), ("pred", "rep", 0)],
)

R["IA-10"] = dict(
    sujet=[
        ("data", "DATA:Number", 0, 0,
         {"nick": u"LONGUEURS_DEBIT", "data": list(S.D_A11)}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Étalon natif du regroupement : à défaut d'un composant "
         u"d'apprentissage, on découpe la plage en trois tranches de largeur "
         u"égale. C'est la ligne de base contre laquelle le regroupement du "
         u"plugin devra faire mieux.", [
            ("bd", "Bounds", 1, 0, {}),
            ("dd", "Deconstruct Domain", 2, 0, {}),
        ]),
        (u"Première borne : minimum + un tiers de l'étendue", [
            ("etendue", "Subtraction", 3, 0, {}),
            ("tiers", "Division", 4, 0, {"val": [(1, "Number", [3])]}),
            ("b1", "Addition", 5, 0, {}),
        ]),
        (u"Le groupe le plus fourni est celui des courtes : 9 pièces sur 24, "
         u"commandées à 2 075 mm. Prendre la moyenne du groupe au lieu de son "
         u"maximum rendrait une pièce sur deux trop courte.", [
            ("lt", "Smaller Than", 6, 2, {}),
            ("ma", "Mass Addition", 7, 2, {}),
            ("pan", "PANEL", 8, 2, {}),
        ]),
    ],
    wires=[("data", "bd", 0), ("bd", "dd", 0),
           ("dd", 1, "etendue", 0), ("dd", 0, "etendue", 1),
           ("etendue", "tiers", 0),
           ("dd", 0, "b1", 0), ("tiers", "b1", 1),
           ("data", "lt", 0), ("b1", "lt", 1),
           ("lt", "ma", 0), ("ma", "pan", 0), ("ma", "rep", 0)],
)

# ===========================================================================
# IA5 · Modeles de langage et IA generative
# ===========================================================================

R["IA-11"] = dict(
    sujet=[
        ("texte", "PANEL", 0, 0,
         {"text": u"ARTICLE 4.2 - GARDE-CORPS\n\n"
                  u"Le garde-corps du niveau R+1 sera realise en acier\n"
                  u"thermolaque. Il presentera une hauteur de 1 000 mm\n"
                  u"mesuree depuis le nu du sol fini. Les montants seront\n"
                  u"espaces d'un entraxe maximal de 1 100 mm. La longueur\n"
                  u"totale a equiper est de 14 800 mm. Le remplissage sera\n"
                  u"constitue de barreaudage vertical.",
          "h": 190, "w": 380}),
        ("lg", "SLIDER", 0, 5,
         {"slider": (0, 30000, 14800, 0), "nick": u"Longueur totale"}),
        ("ent", "SLIDER", 0, 6,
         {"slider": (0, 2000, 1100, 0), "nick": u"Entraxe maximal"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Deux valeurs seulement servent au calcul : la longueur et "
         u"l'entraxe. Le texte contient aussi une hauteur de 1 000 mm, du même "
         u"ordre de grandeur que l'entraxe — une extraction non contrôlée peut "
         u"les intervertir sans que le résultat paraisse absurde.", [
            ("div", "Division", 1, 0, {}),
        ]),
        (u"Le nombre d'intervalles s'arrondit au SUPÉRIEUR : l'entraxe est un "
         u"maximum, il faut donc au moins autant d'intervalles. Un arrondi au "
         u"plus proche donnerait 13 et l'entraxe dépasserait la prescription.", [
            ("rnd", "Round", 2, 0, {}),
        ]),
        (u"Les montants sont les intervalles plus un : 14 intervalles, "
         u"15 montants.", [
            ("add", "Addition", 3, 0, {"val": [(1, "Number", [1])]}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("lg", "div", 0), ("ent", "div", 1),
           ("div", "rnd", 0), ("rnd", 2, "add", 0),
           ("add", "pan", 0), ("add", "rep", 0)],
)

# ===========================================================================
# IA6 · Agents et protocoles
# ===========================================================================

R["IA-12"] = dict(
    sujet=[
        ("crb", "GEO:Curve", 0, 0,
         {"nick": u"COURBE_DE_REFERENCE",
          "geo": ("interp", [(0, 0, 0), (1200, 800, 0), (2600, -400, 0),
                             (4100, 900, 0), (5400, 0, 0)], 3)}),
        ("n", "SLIDER", 0, 3, {"slider": (2, 60, 24, 0), "nick": u"Divisions"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Étalon natif du résultat que l'agent doit retrouver. L'agent est "
         u"libre de ses moyens : c'est la longueur cumulée qui est validée, "
         u"pas la forme du graphe qu'il a produit.", [
            ("dc", "Divide Curve", 1, 0, {}),
        ]),
        (u"Relier les points dans l'ordre donne la polyligne inscrite", [
            ("pl", "PolyLine", 2, 0, {}),
        ]),
        (u"Sa longueur est légèrement inférieure à celle de la courbe : "
         u"c'est normal, une polyligne coupe les arcs.", [
            ("lng", "Length", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("crb", "dc", 0), ("n", "dc", 1),
           ("dc", "pl", 0), ("pl", "lng", 0),
           ("lng", "pan", 0), ("lng", "rep", 0)],
)

# ===========================================================================
# IA7 · Verification, licences et limites
# ===========================================================================

R["IA-13"] = dict(
    sujet=[
        ("qcm", "VALUELIST", 0, 0,
         {"nick": u"REPONSE_QCM",
          "items": [(u"0 - rien, le code n'est pas une donnee de projet", "0"),
                    (u"1 - le code seul, sans les valeurs", "1"),
                    (u"2 - tout ce qui est colle, valeurs et noms compris", "2"),
                    (u"3 - rien tant qu'on ne coche pas une case de partage", "3")]}),
        ("rep", "REPONSE", 3, 0, {"type": "Integer"}),
    ],
    corrige=[
        (u"La réponse est 2. Les cotes internalisées, les noms de calques, "
         u"les repères de projet et les commentaires voyagent avec le code, "
         u"souvent sans qu'on y pense.", [
            ("pan", "PANEL", 1, 2,
             {"text": u"Voyagent avec un extrait colle :\n"
                      u"- valeurs internalisees dans les parametres\n"
                      u"- noms de calques et de blocs\n"
                      u"- commentaires et scribbles\n"
                      u"- chemins de fichiers\n"
                      u"- reperes et numeros d'affaire",
              "h": 130, "w": 300}),
            ("bonne", "DATA:Integer", 2, 0,
             {"nick": u"BONNE_REPONSE", "data": [2]}),
        ]),
    ],
    wires=[("bonne", "rep", 0)],
)

R["IA-14"] = dict(
    sujet=[
        ("geo", "GEO:Brep", 0, 0,
         {"nick": u"ASSEMBLAGE",
          "geo": ("boxes", [((0, 0, 0), 600, 200, 40),
                            ((0, 0, 40), 200, 200, 300),
                            ((400, 0, 40), 200, 200, 300),
                            ((0, 0, 340), 600, 200, 40),
                            ((250, 60, 40), 100, 80, 300),
                            ((0, 0, -40), 600, 200, 40)])}),
        ("faux", "PANEL", 0, 4,
         {"text": u"COMPOSANT FOURNI\nannonce : 0,0684 m3",
          "h": 60, "w": 220}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Contrôle indépendant : mesurer le volume par un moyen natif, qui "
         u"n'emprunte pas le chemin du composant fourni. Redemander à "
         u"l'assistant s'il est sûr ne contrôle rien.", [
            ("vol", "Volume", 1, 0, {}),
        ]),
        (u"Somme des six blocs, en millimètres cubes. Le composant fourni "
         u"annonce 40,8 m³ : il a divisé par un million au lieu d'un "
         u"milliard. Le vrai volume est 40 800 000 mm³, soit 0,0408 m³. Un "
         u"facteur mille — invisible pour qui ne contrôle pas l'ordre de "
         u"grandeur, et parfaitement visible pour qui le fait.", [
            ("ma", "Mass Addition", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("geo", "vol", 0), ("vol", "ma", 0),
           ("ma", "pan", 0), ("ma", "rep", 0)],
)
