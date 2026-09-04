# -*- coding: utf-8 -*-
"""Recettes de construction des lots RH, GP, QT, FA, MP, AV, PL, DV et WB.

Meme moteur et memes conventions que les lots A et IA : bandeau, ZONE_SUJET,
separateur, ZONE_CORRIGE en groupes d'etapes, corrige masque par interrupteur,
aucun cable entre les deux zones.

DEUX FAMILLES
-------------
1. Les QUESTIONS CHARNIERES recoivent un menu deroulant et un parametre de
   reponse entier. Leurs propositions ne sont PAS recopiees ici : elles sont
   derivees de la fiche par equilibrer_qcm, de sorte que l'ordre affiche dans
   la definition et celui de la fiche ne puissent pas diverger. C'est le defaut
   qui m'avait oblige a figer quatre charnieres du lot A : ici, il ne peut plus
   se produire.

2. Les EXERCICES A DONNEES PURES recoivent leurs listes et un corrige natif.

CE QUI N'EST PAS ICI
--------------------
Les exercices qui demandent une geometrie Rhino a fabriquer (RH-02 a RH-05,
RH-08, RH-09, GP-03), un plugin d'iteration ou de simulation (AV-01, AV-02),
un composant scripte (DV-02) ou un deroule (FA-02). Ils viendront avec leurs
ressources .3dm et leurs dependances verifiees.
"""
import os
import sys

_GEN = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
if _GEN not in sys.path:
    sys.path.insert(0, _GEN)

import domaine_metier as M
import domaine_avance as A
from equilibrer_qcm import charniere_equilibree, RE_PROP, MARQUE

R = {}


# ---------------------------------------------------------------------------
# Questions charnieres : le menu deroulant suit la fiche
# ---------------------------------------------------------------------------

def _options(e, largeur=58):
    """Propositions et indice de la bonne reponse, tels que la fiche les rend."""
    items, bonne = [], 0
    i = 0
    for ligne in charniere_equilibree(e).split(u"\n"):
        m = RE_PROP.match(ligne.strip())
        if not m:
            continue
        texte = m.group(2).replace(MARQUE, u"").strip()
        if MARQUE in m.group(2):
            bonne = i
        if len(texte) > largeur:
            texte = texte[:largeur].rsplit(u" ", 1)[0] + u"…"
        items.append((u"%d - %s" % (i, texte), str(i)))
        i += 1
    return items, bonne


def charniere(e, note=None):
    """Recette d'une question charniere : menu deroulant, reponse, rappel."""
    items, bonne = _options(e)
    etapes = [
        (u"La bonne réponse est la proposition %d. Le corrigé porte cet "
         u"indice en clair : le menu du sujet, lui, part sur la première "
         u"proposition, quelle qu'elle soit." % bonne, [
            ("bonne", "DATA:Integer", 2, 0,
             {"nick": u"BONNE_REPONSE", "data": [bonne]}),
        ]),
    ]
    if note:
        etapes.append((u"À retenir", [
            ("pan", "PANEL", 1, 2, {"text": note, "h": 130, "w": 300}),
        ]))
    return dict(
        sujet=[
            ("qcm", "VALUELIST", 0, 0,
             {"nick": u"REPONSE_QCM", "items": items}),
            ("rep", "REPONSE", 4, 0, {"type": "Integer"}),
        ],
        corrige=etapes,
        wires=[("bonne", "rep", 0)],
    )


# ---------------------------------------------------------------------------
# Lot RH — socle Rhino
# ---------------------------------------------------------------------------

def _rh(eid):
    for e in __import__("domaine_rhino").LOT_RH:
        if e["id"] == eid:
            return e
    return None


R["RH-01"] = charniere(_rh("RH-01"),
    u"Si le zoom etendue ne montre rien :\n"
    u"- un calque est masque\n"
    u"- les objets sont hors du plan de coupe\n"
    u"- un objet egare tres loin ecrase l'echelle")

R["RH-06"] = charniere(_rh("RH-06"),
    u"Groupe   : rassemble une selection.\n"
    u"           Modifier = reprendre chaque copie.\n\n"
    u"Bloc     : une definition, N instances.\n"
    u"           Modifier la definition met tout a jour.")

R["RH-07"] = charniere(_rh("RH-07"),
    u"Changer l'unite du document ne met PAS\n"
    u"le modele a l'echelle : c'est un choix\n"
    u"explicite, propose separement.\n\n"
    u"La tolerance absolue suit l'unite : la\n"
    u"revoir apres toute mise a l'echelle.")

R["RH-10"] = charniere(_rh("RH-10"),
    u"STL et OBJ ne connaissent que des\n"
    u"triangles. La finesse du maillage est un\n"
    u"reglage de l'export, pas une propriete\n"
    u"de la machine.")


# ---------------------------------------------------------------------------
# Lot GP — geometrie parametrique
# ---------------------------------------------------------------------------

R["GP-01"] = dict(
    sujet=[
        ("l", "SLIDER", 0, 0,
         {"slider": (200, 3000, 1400, 0), "nick": u"Largeur"}),
        ("h", "SLIDER", 0, 1,
         {"slider": (200, 3000, 850, 0), "nick": u"Hauteur"}),
        ("r", "SLIDER", 0, 2,
         {"slider": (0, 200, 60, 0), "nick": u"Rayon de conge"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le rectangle se construit dans le plan de base, à partir des deux "
         u"dimensions réglables", [
            ("rc", "Rectangle", 1, 0, {}),
        ]),
        (u"Le congé est un paramètre du tracé, non un raccord posé après "
         u"coup : le contour reste ainsi une courbe unique, et sa mesure a "
         u"un sens", [
            ("pan0", "PANEL", 2, 2,
             {"text": u"Le conge est l'entree R\ndu composant de trace.",
              "h": 56, "w": 210}),
        ]),
        (u"Mesurer le contour. Le retranchement des côtés droits est déjà "
         u"fait : y ajouter les quarts de cercle donnerait 4 × (2r − πr/2) "
         u"de trop", [
            ("lg", "Length", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("l", "rc", 1), ("h", "rc", 2), ("r", "rc", 3),
           ("rc", "lg", 0), ("lg", "pan", 0), ("lg", "rep", 0)],
)

R["GP-02"] = dict(
    sujet=[
        ("he", "SLIDER", 0, 0,
         {"slider": (2000, 4000, 2700, 0), "nick": u"Hauteur d'etage"}),
        ("hv", "SLIDER", 0, 1,
         {"slider": (140, 200, 175, 0), "nick": u"Hauteur de marche visee"}),
        ("gi", "SLIDER", 0, 2,
         {"slider": (200, 350, 280, 0), "nick": u"Giron"}),
        ("la", "SLIDER", 0, 3,
         {"slider": (600, 1600, 1100, 0), "nick": u"Largeur"}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le nombre de contremarches est un ENTIER : c'est lui qu'on "
         u"arrondit, au plus proche. 2 700 ÷ 175 vaut 15,43, donc 15", [
            ("dv1", "Division", 1, 0, {}),
            ("rd", "Round", 2, 0, {}),
        ]),
        (u"La hauteur réelle se recale alors sur ce nombre : 2 700 ÷ 15 vaut "
         u"180 mm, et non les 175 visés. Garder 175 donnerait un escalier de "
         u"2 625 mm, qui n'atteint pas l'étage", [
            ("dv2", "Division", 3, 0, {}),
            ("pan1", "PANEL", 4, 3, {}),
        ]),
        (u"Chaque marche cumule les précédentes : la première monte d'une "
         u"hauteur, la quinzième de quinze. La somme 1 + 2 + … + n vaut "
         u"n(n+1)/2, soit 120 pour quinze marches — inutile de construire les "
         u"quinze blocs pour la connaître", [
            ("n1", "Addition", 3, 5, {"val": [(1, "Number", [1])]}),
            ("nn", "Multiplication", 4, 5, {}),
            ("dm", "Division", 5, 5, {"val": [(1, "Number", [2])]}),
        ]),
        (u"Volume d'une assise unitaire : giron × largeur × hauteur réelle", [
            ("ug", "Multiplication", 5, 0, {}),
            ("ul", "Multiplication", 6, 0, {}),
        ]),
        (u"Volume total, converti en mètres cubes : 6,653 m³", [
            ("vt", "Multiplication", 7, 0, {}),
            ("cv", "Division", 8, 0, {"val": [(1, "Number", [1000000000])]}),
            ("pan", "PANEL", 9, 2, {}),
        ]),
    ],
    wires=[("he", "dv1", 0), ("hv", "dv1", 1), ("dv1", "rd", 0),
           ("he", "dv2", 0), ("rd", 0, "dv2", 1), ("dv2", "pan1", 0),
           ("rd", 0, "n1", 0),
           ("rd", 0, "nn", 0), ("n1", "nn", 1), ("nn", "dm", 0),
           ("dv2", "ug", 0), ("gi", "ug", 1),
           ("ug", "ul", 0), ("la", "ul", 1),
           ("ul", "vt", 0), ("dm", "vt", 1),
           ("vt", "cv", 0), ("cv", "pan", 0), ("cv", "rep", 0)],
)


def _gp(eid):
    for e in M.LOT_GP:
        if e["id"] == eid:
            return e
    return None


R["GP-04"] = charniere(_gp("GP-04"),
    u"SubD  : recherche de forme, deformation\n"
    u"        souple, peu de points de controle.\n\n"
    u"NURBS : exactitude, usinage, cotation.\n\n"
    u"La conversion SubD vers NURBS est prevue :\n"
    u"les deux ne s'opposent pas.")


# ---------------------------------------------------------------------------
# Lot QT — quantitatifs, chiffrage, export
# ---------------------------------------------------------------------------

_QT_B = [float(b) for _a, b in M.D_QT01_SECT]
_QT_A = [float(a) for a, _b in M.D_QT01_SECT]

R["QT-01"] = dict(
    sujet=[
        ("a", "DATA:Number", 0, 0,
         {"nick": u"SECTION_LARGEUR_MM", "data": _QT_A}),
        ("b", "DATA:Number", 0, 2,
         {"nick": u"SECTION_HAUTEUR_MM", "data": _QT_B}),
        ("lg", "DATA:Number", 0, 4,
         {"nick": u"LONGUEURS_MM", "data": [float(x) for x in M.D_QT01_LONG]}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Aire de chaque section, en millimètres carrés", [
            ("ai", "Multiplication", 1, 0, {}),
        ]),
        (u"Volume de chaque solive : son aire par SA longueur, terme à terme. "
         u"Prendre la section moyenne pour la longueur totale donnerait une "
         u"valeur voisine et fausse — les sections ne sont pas indépendantes "
         u"des longueurs", [
            ("vo", "Multiplication", 2, 0, {}),
        ]),
        (u"Somme des vingt volumes, puis conversion : un mètre cube vaut un "
         u"MILLIARD de millimètres cubes, non un million", [
            ("ma", "Mass Addition", 3, 0, {}),
            ("dv", "Division", 4, 0, {"val": [(1, "Number", [1000000000])]}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("a", "ai", 0), ("b", "ai", 1),
           ("ai", "vo", 0), ("lg", "vo", 1),
           ("vo", "ma", 0), ("ma", "dv", 0),
           ("dv", "pan", 0), ("dv", "rep", 0)],
)

# QT-02 : le prix de chaque solive, deja apparie a sa section. Le montage
# natif de l'appariement par section est l'objet de l'exercice ; la zone
# corrige fournit l'etalon.
_QT_PRIX = [M.D_QT02_PRIX[s] for s in M.D_QT01_SECT]

R["QT-02"] = dict(
    sujet=[
        ("lg", "DATA:Number", 0, 0,
         {"nick": u"LONGUEURS_MM", "data": [float(x) for x in M.D_QT01_LONG]}),
        ("px", "DATA:Number", 0, 2,
         {"nick": u"PRIX_AU_METRE", "data": _QT_PRIX}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le prix est au mètre linéaire : convertir les longueurs avant "
         u"toute multiplication", [
            ("dv", "Division", 1, 0, {"val": [(1, "Number", [1000])]}),
        ]),
        (u"Prix par solive. L'appariement doit se faire par SECTION, non par "
         u"rang : vingt solives pour cinq prix, un appariement par rang "
         u"produirait silencieusement un résultat calculé sur le mauvais prix", [
            ("mu", "Multiplication", 2, 0, {}),
        ]),
        (u"Montant total : 814,92 €", [
            ("ma", "Mass Addition", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("lg", "dv", 0), ("dv", "mu", 0), ("px", "mu", 1),
           ("mu", "ma", 0), ("ma", "pan", 0), ("ma", "rep", 0)],
)

R["QT-03"] = dict(
    sujet=[
        ("rp", "DATA:Text", 0, 0,
         {"nick": u"REPERES", "data": list(M.D_QT03_REP)}),
        ("l", "DATA:Number", 0, 2,
         {"nick": u"LARGEURS_MM", "data": [float(x) for x in M.D_QT03_L]}),
        ("h", "DATA:Number", 0, 4,
         {"nick": u"HAUTEURS_MM", "data": [float(x) for x in M.D_QT03_H]}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Surface de chaque menuiserie, en mètres carrés", [
            ("mu", "Multiplication", 1, 0, {}),
            ("dv", "Division", 2, 0, {"val": [(1, "Number", [1000000])]}),
        ]),
        (u"Le tableau se construit COLONNE par colonne, jointes par un "
         u"séparateur. En contexte francophone, le point-virgule s'impose : "
         u"la virgule sert déjà de séparateur décimal, et chaque nombre "
         u"casserait une ligne en deux colonnes", [
            ("sep", "PANEL", 3, 2,
             {"text": u"Repere;Largeur;Hauteur;Surface", "h": 46, "w": 240}),
        ]),
        (u"Surface totale : 53,04 m²", [
            ("ma", "Mass Addition", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("l", "mu", 0), ("h", "mu", 1), ("mu", "dv", 0),
           ("dv", "ma", 0), ("ma", "pan", 0), ("ma", "rep", 0)],
)


# ---------------------------------------------------------------------------
# Lot FA — aide a la fabrication
# ---------------------------------------------------------------------------

R["FA-01"] = dict(
    sujet=[
        ("l", "DATA:Number", 0, 0,
         {"nick": u"LONGUEURS_MM", "data": [float(x) for x in M.D_FA01_L]}),
        ("h", "DATA:Number", 0, 2,
         {"nick": u"HAUTEURS_MM", "data": [float(x) for x in M.D_FA01_H]}),
        ("pl", "SLIDER", 0, 4,
         {"slider": (1000, 3000, 2500, 0), "nick": u"Panneau - longueur"}),
        ("ph", "SLIDER", 0, 5,
         {"slider": (600, 2000, 1250, 0), "nick": u"Panneau - largeur"}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Surface de chaque pièce, puis surface totale du débit", [
            ("mu", "Multiplication", 1, 0, {}),
            ("ma", "Mass Addition", 2, 0, {}),
        ]),
        (u"Surface d'un panneau brut", [
            ("sp", "Multiplication", 2, 4, {}),
        ]),
        (u"Le rapport vaut 3,10 panneaux. Un panneau se commande entier : "
         u"c'est un approvisionnement, donc un arrondi au SUPÉRIEUR. "
         u"L'arrondi au plus proche donnerait 3, et il manquerait de quoi "
         u"débiter un dixième du lot", [
            ("dv", "Division", 3, 0, {}),
            ("rd", "Round", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
        (u"Ce nombre est un MINORANT : aucune imbrication ne peut faire "
         u"mieux, et toutes feront moins bien — la chute de placement "
         u"s'ajoute à la chute de surface", [
            ("note", "PANEL", 5, 2,
             {"text": u"3,10 panneaux exiges -> 4 commandes.\n"
                      u"Le nombre reel sera superieur.",
              "h": 56, "w": 240}),
        ]),
    ],
    wires=[("l", "mu", 0), ("h", "mu", 1), ("mu", "ma", 0),
           ("pl", "sp", 0), ("ph", "sp", 1),
           ("ma", "dv", 0), ("sp", "dv", 1),
           ("dv", "rd", 0), ("rd", 2, "pan", 0), ("rd", 2, "rep", 0)],
)


# ---------------------------------------------------------------------------
# Lot MP — methode et performance
# ---------------------------------------------------------------------------

R["MP-02"] = dict(
    sujet=[
        ("t", "DATA:Number", 0, 0,
         {"nick": u"TEMPS_MS", "data": [float(x) for x in A.D_MP02]}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Temps total de recalcul", [
            ("tot", "Mass Addition", 1, 0, {}),
        ]),
        (u"Trier, puis INVERSER : sans l'inversion on prélève les trois plus "
         u"rapides, et la conclusion s'inverse avec", [
            ("sl", "Sort List", 1, 2, {}),
            ("rv", "Reverse List", 2, 2, {}),
        ]),
        (u"Prélever les trois premiers et les sommer", [
            ("cd", "Construct Domain", 3, 4, {"val": [(0, "Number", [0]),
                                                      (1, "Number", [2])]}),
            ("sb", "Sub List", 4, 2, {}),
            ("s3", "Mass Addition", 5, 2, {}),
        ]),
        (u"Part du total : 97 %. Dix-sept composants coûtent moins de 30 ms "
         u"chacun — les régler tous ne ferait rien gagner", [
            ("dv", "Division", 6, 0, {}),
            ("mu", "Multiplication", 7, 2, {"val": [(1, "Number", [100])]}),
            ("rd", "Round", 8, 0, {}),
            ("pan", "PANEL", 9, 0, {}),
        ]),
    ],
    wires=[("t", "tot", 0), ("t", "sl", 0), ("sl", "rv", 0),
           ("rv", "sb", 0), ("cd", "sb", 1), ("sb", "s3", 0),
           ("s3", "dv", 0), ("tot", "dv", 1),
           ("dv", "mu", 0), ("mu", "rd", 0),
           ("rd", 0, "pan", 0), ("rd", 0, "rep", 0)],
)


def _av(eid):
    for e in A.LOT_AV + A.LOT_MP + A.LOT_PL + A.LOT_DV + A.LOT_WB:
        if e["id"] == eid:
            return e
    return None


R["MP-03"] = charniere(_av("MP-03"),
    u"Le modele ne change pas : une donnee\n"
    u"change, l'aval se recalcule.\n\n"
    u"Un evenement clavier ou souris est une\n"
    u"donnee de plus, exposee par un composant.\n"
    u"Ce n'est pas une exception au modele.")


# ---------------------------------------------------------------------------
# Lot AV — algorithmique avancee
# ---------------------------------------------------------------------------

R["AV-03"] = dict(
    sujet=[
        ("lg", "SLIDER", 0, 0,
         {"slider": (5000, 30000, 18600, 0), "nick": u"Longueur de facade"}),
        ("mx", "SLIDER", 0, 1,
         {"slider": (1000, 3000, 2400, 0), "nick": u"Largeur maxi de panneau"}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"18 600 ÷ 2 400 vaut 7,75 panneaux", [
            ("dv", "Division", 1, 0, {}),
        ]),
        (u"La largeur maximale est un plafond : il faut donc au moins autant "
         u"de panneaux, arrondi au SUPÉRIEUR. Sept panneaux feraient 2 657 mm "
         u"chacun et dépasseraient la prescription", [
            ("rd", "Round", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
        (u"Et voici la leçon de l'exercice : un moteur de recherche laissé "
         u"sans contrainte proposerait UN panneau de 18 600 mm — optimum "
         u"parfait, calepinage absurde. Une recherche de forme ne vaut que ce "
         u"que vaut ce qu'on lui demande d'optimiser. Ici, une division "
         u"suffisait", [
            ("note", "PANEL", 3, 2,
             {"text": u"Contrainte HORS de la fonction evaluee\n"
                      u"-> optimum : 1 panneau de 18 600 mm.\n\n"
                      u"Savoir qu'un calcul direct suffit fait\n"
                      u"partie de la competence.",
              "h": 96, "w": 300}),
        ]),
    ],
    wires=[("lg", "dv", 0), ("mx", "dv", 1),
           ("dv", "rd", 0), ("rd", 2, "pan", 0), ("rd", 2, "rep", 0)],
)


# ---------------------------------------------------------------------------
# Lots PL, DV, WB — questions charnieres
# ---------------------------------------------------------------------------

R["PL-01"] = charniere(_av("PL-01"),
    u"Une definition coute presque toujours\n"
    u"plus cher que le dessin equivalent,\n"
    u"la PREMIERE fois.\n\n"
    u"Elle s'amortit sur les variantes.\n"
    u"Pour un cas unique, elle ne se\n"
    u"rentabilise jamais.")

R["PL-02"] = charniere(_av("PL-02"),
    u"Grasshopper NOMME toujours ce qui manque :\n"
    u"le composant rouge porte le nom du plugin.\n\n"
    u"Preferer le gestionnaire de paquets au\n"
    u"telechargement manuel : il gere versions\n"
    u"et mises a jour.")

R["PL-04"] = charniere(_av("PL-04"),
    u"Avant d'adopter un plugin dans une\n"
    u"definition LIVREE :\n"
    u"- licence, et droit d'usage commercial\n"
    u"- entretien : derniere mise a jour ?\n"
    u"- que devient le client s'il disparait ?\n\n"
    u"Gratuit ne dit rien de tout cela.")

R["DV-01"] = charniere(_av("DV-01"),
    u"Le critere n'est pas la preference de\n"
    u"celui qui ecrit, mais la lisibilite du\n"
    u"resultat.\n\n"
    u"Scripter quand la logique est iterative\n"
    u"ou conditionnelle et que le cablage la\n"
    u"rendrait illisible.")

R["DV-03"] = charniere(_av("DV-03"),
    u"La question n'est pas la difficulte\n"
    u"d'ECRIRE, mais le cout de VALIDER.\n\n"
    u"Une librairie eprouvee a deja rencontre\n"
    u"les cas degeneres qu'un code neuf\n"
    u"decouvrira en production.")

R["WB-03"] = charniere(_av("WB-03"),
    u"Rhino.Inside  : Rhino cohabite avec un\n"
    u"                logiciel hote, sur le poste.\n\n"
    u"Rhino.Compute : le moteur de calcul au\n"
    u"                bout d'un appel reseau.\n\n"
    u"Deux reponses a deux besoins differents.")


# --- exercices a geometrie : le sujet mesure, le corrige etalonne ---------
import recipes_geo as _GEO
R.update(_GEO.R)

import recipes_av as _AV
R.update(_AV.R)
