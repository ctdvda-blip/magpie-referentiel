# -*- coding: utf-8 -*-
"""Recettes de construction des exercices de la vague d'equilibrage.

Memes conventions que les autres recettes : bandeau, ZONE_SUJET, separateur,
ZONE_CORRIGE en groupes d'etapes, corrige masque par un interrupteur.

Les DONNEES sont posees dans la zone sujet et lues par le corrige : c'est deja
le parti pris de GP-02 et des autres exercices a donnees pures. Ce qui ne
traverse jamais, c'est le RESULTAT — REPONSE reste libre de toute source, et
c'est ce que verifient les recettes 3 et 6.

Les quatre questions charnieres de la vague passent par le meme helper que les
autres : leurs propositions sont derivees de la fiche, jamais recopiees, de
sorte que l'ordre affiche dans la definition et celui de la fiche ne puissent
pas diverger.

DV-07 n'a pas de definition : son livrable est un plugin installe sur un poste
tiers, note sur grille. Lui en fabriquer une reviendrait a livrer le travail.
"""
import os
import sys

_ICI = os.path.dirname(os.path.abspath(__file__)) if "__file__" in dir() \
    else r"C:\Users\charl\.claude\projects\MAGPIE\Documentation\Generateurs\GH"
_GEN = os.path.abspath(os.path.join(_ICI, ".."))
for _p in (_ICI, _GEN):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import exercices_vague1 as V1
import exercices_vague1_avance as V1A
# Renomme a l'import : `charniere` est aussi le nom du CHAMP qui porte le
# texte de la question dans les fiches, et IronPython s'y perdait.
from recipes_nouveaux import charniere as recette_charniere

R = {}


def _e(eid):
    for lot in (V1.LOT_GP, V1.LOT_QT, V1.LOT_FA,
                V1A.LOT_DV, V1A.LOT_WB, V1A.LOT_IA):
        for x in lot:
            if x["id"] == eid:
                return x
    return None


# ---------------------------------------------------------------------------
# GP-05 — la chaine de cotes
# ---------------------------------------------------------------------------

R["GP-05"] = dict(
    sujet=[
        ("ori", "DATA:Number", 0, 0,
         {"nick": u"ECART_A_L_ORIGINE", "data": [V1.D_GP05_ORIGINE]}),
        ("ent", "DATA:Number", 0, 2,
         {"nick": u"ENTRAXES", "data": list(V1.D_GP05_ENTRAXES)}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Les entraxes sont des distances RELATIVES : chacun se mesure "
         u"depuis le percement précédent. Les cumuler donne la distance "
         u"parcourue depuis le premier percement — 8 535 mm — et non la cote "
         u"de pose", [
            ("ma", "Mass Addition", 1, 0, {}),
        ]),
        (u"La cote de pose se compte depuis le point de RÉFÉRENCE. Il reste "
         u"donc à ajouter l'écart entre ce point et le premier percement : "
         u"8 955 mm. Oublier ces 420 mm décale toute la façade d'un tableau "
         u"de baie — assez peu pour ne se voir qu'à la livraison", [
            ("add", "Addition", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
        (u"Ce que l'exercice vaut au-delà du chiffre : sur le plan de pose, "
         u"on cote TOUJOURS depuis une origine unique. Coter de proche en "
         u"proche fait cumuler les erreurs de report, et le dernier "
         u"percement porte la somme de toutes les précédentes", [
            ("note", "PANEL", 3, 2,
             {"text": u"Entraxe  = distance au voisin.\n"
                      u"Cote     = distance a l'origine.\n\n"
                      u"Le plan de pose ne porte que\n"
                      u"des cotes.",
              "h": 90, "w": 250}),
        ]),
    ],
    wires=[("ent", "ma", 0), ("ma", "add", 0), ("ori", "add", 1),
           ("add", "pan", 0), ("add", "rep", 0)],
)


# ---------------------------------------------------------------------------
# QT-04 et QT-05 — le debit qui devient une commande
# ---------------------------------------------------------------------------

_REFS = [r for r, _q in V1.D_QT04_DEBIT]
_QTES = [q for _r, q in V1.D_QT04_DEBIT]

R["QT-04"] = dict(
    sujet=[
        ("refs", "DATA:Text", 0, 0,
         {"nick": u"REFERENCES", "data": _REFS}),
        ("qtes", "DATA:Number", 0, 3,
         {"nick": u"QUANTITES", "data": _QTES}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Établir la liste des références DISTINCTES : vingt-quatre lignes "
         u"pour huit références", [
            ("set", "Create Set", 1, 0, {}),
        ]),
        (u"Pour chaque référence, relever à quelles lignes du débit elle "
         u"apparaît. C'est ce relevé qui fait le regroupement — sans lui, on "
         u"ne peut que trier", [
            ("mi", "Member Index", 2, 0, {}),
        ]),
        (u"Aller chercher les quantités à ces lignes, puis les cumuler "
         u"référence par référence", [
            ("li", "List Item", 3, 0, {}),
            ("ma", "Mass Addition", 4, 0, {}),
        ]),
        (u"Les huit cumuls arrivent en huit BRANCHES distinctes — une par "
         u"référence — et non en une liste. Les aplatir avant de chercher "
         u"le plus grand : trier huit branches d'un élément chacune ne trie "
         u"rien du tout, et rend les huit cumuls dans leur ordre d'origine", [
            ("plat", "Flatten Tree", 5, 0, {}),
        ]),
        (u"Le plus grand cumul vaut 17. La plus grosse LIGNE unitaire vaut "
         u"8, et la référence la plus FRÉQUENTE n'est pas celle qui porte le "
         u"plus gros cumul : trois lectures possibles, trois réponses "
         u"différentes", [
            ("bor", "Bounds", 6, 0, {}),
            ("dd", "Deconstruct Domain", 7, 0, {}),
            ("pan", "PANEL", 8, 2, {}),
        ]),
    ],
    wires=[("refs", "set", 0),
           ("refs", "mi", 0), ("set", "mi", 1),
           ("qtes", "li", 0), ("mi", "li", 1),
           ("li", "ma", 0),
           ("ma", "plat", 0),
           ("plat", "bor", 0),
           ("bor", "dd", 0),
           ("dd", 1, "pan", 0), ("dd", 1, "rep", 0)],
)

R["QT-05"] = dict(
    sujet=[
        ("refs", "DATA:Text", 0, 0,
         {"nick": u"REFERENCES", "data": _REFS}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le fichier ne porte pas les lignes du débit, mais les références "
         u"distinctes : une ligne par référence", [
            ("set", "Create Set", 1, 0, {}),
            ("ll", "List Length", 2, 0, {}),
        ]),
        (u"Plus la ligne d'en-tête, qui nomme les colonnes. Neuf lignes en "
         u"tout. L'oublier fait lire la première référence comme un nom de "
         u"colonne : elle disparaît de la commande, sans erreur ni message", [
            ("add", "Addition", 3, 0, {"val": [(1, "Number", [1])]}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("refs", "set", 0), ("set", "ll", 0), ("ll", "add", 0),
           ("add", "pan", 0), ("add", "rep", 0)],
)


# ---------------------------------------------------------------------------
# FA-03 — le developpe d'un profil plie
# ---------------------------------------------------------------------------

_F3 = V1.D_FA03

R["FA-03"] = dict(
    sujet=[
        ("aile", "SLIDER", 0, 0,
         {"slider": (50, 300, _F3["aile"], 0), "nick": u"Aile exterieure"}),
        ("ame", "SLIDER", 0, 1,
         {"slider": (100, 600, _F3["ame"], 0), "nick": u"Ame exterieure"}),
        ("ep", "SLIDER", 0, 2,
         {"slider": (1, 10, _F3["epaisseur"], 1), "nick": u"Epaisseur"}),
        ("ray", "SLIDER", 0, 3,
         {"slider": (1, 20, _F3["rayon"], 1), "nick": u"Rayon interieur"}),
        ("k", "SLIDER", 0, 4,
         {"slider": (0.3, 0.5, _F3["k"], 2), "nick": u"Facteur K"}),
        ("rep", "REPONSE", 9, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"La partie réellement PLATE d'une paroi n'est pas sa cote "
         u"extérieure : le pli lui prend le rayon et l'épaisseur. Une aile, "
         u"qui ne porte qu'un pli, en perd une fois ; l'âme, qui en porte "
         u"deux, en perd deux fois", [
            ("re", "Addition", 1, 0, {}),
            ("pa", "Subtraction", 2, 0, {}),
            ("re2", "Multiplication", 2, 3, {"val": [(1, "Number", [2])]}),
            ("pm", "Subtraction", 3, 3, {}),
        ]),
        (u"L'allongement d'un pli à 90° : un quart de cercle décrit par la "
         u"FIBRE NEUTRE, la seule fibre qui garde sa longueur au pliage. "
         u"Elle se situe à r + K·e du centre de courbure — le facteur K dit "
         u"où exactement, et il ne vaut pas 0,5", [
            ("ke", "Multiplication", 1, 6, {}),
            ("rn", "Addition", 2, 6, {}),
            ("q", "Pi", 3, 6, {"val": [(0, "Number", [0.5])]}),
            ("ba", "Multiplication", 4, 6, {}),
        ]),
        (u"Le développé est la somme des parties plates et des deux "
         u"allongements : 527,67 mm. Additionner les cotes extérieures "
         u"donnerait 540 mm — 12,3 mm de trop, invisibles au plan, et "
         u"répétés sur chaque pièce de la série", [
            ("2a", "Multiplication", 4, 0, {"val": [(1, "Number", [2])]}),
            ("sp", "Addition", 5, 0, {}),
            ("2b", "Multiplication", 5, 6, {"val": [(1, "Number", [2])]}),
            ("tot", "Addition", 6, 0, {}),
            ("pan", "PANEL", 7, 0, {}),
        ]),
    ],
    wires=[("ray", "re", 0), ("ep", "re", 1),
           ("aile", "pa", 0), ("re", "pa", 1),
           ("re", "re2", 0),
           ("ame", "pm", 0), ("re2", "pm", 1),
           ("k", "ke", 0), ("ep", "ke", 1),
           ("ray", "rn", 0), ("ke", "rn", 1),
           ("rn", "ba", 0), ("q", "ba", 1),
           ("pa", "2a", 0),
           ("2a", "sp", 0), ("pm", "sp", 1),
           ("ba", "2b", 0),
           ("sp", "tot", 0), ("2b", "tot", 1),
           ("tot", "pan", 0), ("tot", "rep", 0)],
)


# ---------------------------------------------------------------------------
# FA-04 — la fournee
# ---------------------------------------------------------------------------

_F4 = V1.D_FA04


def _axe(nom, col, ligne, plateau, piece):
    """Combien de pieces tiennent sur un axe, ecarts compris."""
    return [
        ("u" + nom, "Subtraction", col, ligne,
         {"val": [(0, "Number", [plateau]), (1, "Number", [2 * _F4["ecart"]])]}),
        ("d" + nom, "Addition", col + 1, ligne,
         {"val": [(1, "Number", [_F4["ecart"]])]}),
        ("p" + nom, "Addition", col + 1, ligne + 1,
         {"val": [(0, "Number", [piece]), (1, "Number", [_F4["ecart"]])]}),
        ("r" + nom, "Division", col + 2, ligne, {}),
        ("n" + nom, "Round", col + 3, ligne, {}),
    ]


R["FA-04"] = dict(
    sujet=[
        ("px", "SLIDER", 0, 0,
         {"slider": (100, 400, _F4["plateau"][0], 0), "nick": u"Plateau X"}),
        ("py", "SLIDER", 0, 1,
         {"slider": (100, 400, _F4["plateau"][1], 0), "nick": u"Plateau Y"}),
        ("pz", "SLIDER", 0, 2,
         {"slider": (100, 400, _F4["plateau"][2], 0), "nick": u"Plateau Z"}),
        ("ec", "SLIDER", 0, 3,
         {"slider": (0, 20, _F4["ecart"], 0), "nick": u"Ecart"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Sur chaque axe : retrancher les deux écarts de paroi, puis "
         u"chercher combien de pièces séparées d'un écart tiennent dans ce "
         u"qui reste. Entre n pièces il y a n − 1 intervalles, d'où le "
         u"+ écart au numérateur", [
            ("ux", "Subtraction", 1, 0,
             {"val": [(0, "Number", [_F4["plateau"][0]]),
                      (1, "Number", [2 * _F4["ecart"]])]}),
            ("dx", "Addition", 2, 0, {"val": [(1, "Number", [_F4["ecart"]])]}),
            ("px2", "Addition", 2, 1,
             {"val": [(0, "Number", [_F4["piece"][0]]),
                      (1, "Number", [_F4["ecart"]])]}),
            ("rx", "Division", 3, 0, {}),
            ("nx", "Round", 4, 0, {}),
        ]),
        (u"L'arrondi se fait à l'entier INFÉRIEUR : une pièce qui dépasse ne "
         u"se produit pas. Les trois divisions tombent sur 3,72, 4,90 et "
         u"2,08 — au plus proche, elles donneraient 4, 5 et 2, soit "
         u"quarante pièces qui ne rentrent pas", [
            ("uy", "Subtraction", 1, 3,
             {"val": [(0, "Number", [_F4["plateau"][1]]),
                      (1, "Number", [2 * _F4["ecart"]])]}),
            ("dy", "Addition", 2, 3, {"val": [(1, "Number", [_F4["ecart"]])]}),
            ("py2", "Addition", 2, 4,
             {"val": [(0, "Number", [_F4["piece"][1]]),
                      (1, "Number", [_F4["ecart"]])]}),
            ("ry", "Division", 3, 3, {}),
            ("ny", "Round", 4, 3, {}),
        ]),
        (u"Le même compte sur la hauteur", [
            ("uz", "Subtraction", 1, 6,
             {"val": [(0, "Number", [_F4["plateau"][2]]),
                      (1, "Number", [2 * _F4["ecart"]])]}),
            ("dz", "Addition", 2, 6, {"val": [(1, "Number", [_F4["ecart"]])]}),
            ("pz2", "Addition", 2, 7,
             {"val": [(0, "Number", [_F4["piece"][2]]),
                      (1, "Number", [_F4["ecart"]])]}),
            ("rz", "Division", 3, 6, {}),
            ("nz", "Round", 4, 6, {}),
        ]),
        (u"3 × 4 × 2 font 24 pièces. Le rapport des volumes en annonçait 49 "
         u"— le double. Les pièces ne se déforment pas pour combler les "
         u"creux, et c'est ce que le rapport des volumes oublie", [
            ("m1", "Multiplication", 5, 0, {}),
            ("m2", "Multiplication", 6, 0, {}),
            ("pan", "PANEL", 7, 3, {}),
        ]),
    ],
    wires=[("ux", "dx", 0), ("dx", "rx", 0), ("px2", "rx", 1), ("rx", "nx", 0),
           ("uy", "dy", 0), ("dy", "ry", 0), ("py2", "ry", 1), ("ry", "ny", 0),
           ("uz", "dz", 0), ("dz", "rz", 0), ("pz2", "rz", 1), ("rz", "nz", 0),
           ("nx", 1, "m1", 0), ("ny", 1, "m1", 1),
           ("m1", "m2", 0), ("nz", 1, "m2", 1),
           ("m2", "pan", 0), ("m2", "rep", 0)],
)


# ---------------------------------------------------------------------------
# WB-04 — ce qu'on expose
# ---------------------------------------------------------------------------

R["WB-04"] = dict(
    sujet=[
        ("nat", "DATA:Text", 0, 0,
         {"nick": u"NATURE_DE_CHAQUE_ENTREE",
          # IronPython 2.7 fait FUITER la variable de boucle d'une
          # comprehension dans la portee englobante. Nommer celle-ci
          # `_e` ecrasait la fonction `_e` definie plus haut, qui
          # devenait le dernier libelle lu — et les quatre charnieres
          # de la fin du fichier echouaient sur « str is not callable ».
          "data": [nature for _libelle, nature in V1A.D_WB04_ENTREES]}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Trois familles, et une seule s'expose. Les réglages internes "
         u"appartiennent à l'auteur de la définition ; les grandeurs "
         u"dérivées se déduisent d'autres entrées, et les exposer "
         u"autoriserait deux vérités contradictoires — une hauteur de "
         u"tiroir incompatible avec la hauteur du meuble", [
            ("cible", "DATA:Text", 1, 0,
             {"nick": u"CE_QUI_S_EXPOSE", "data": [u"choix"]}),
        ]),
        (u"Compter les entrées de cette seule famille : six sur quatorze. "
         u"Tout exposer en donnerait quatorze, s'arrêter aux non-internes "
         u"en donnerait neuf", [
            ("mi", "Member Index", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("nat", "mi", 0), ("cible", "mi", 1),
           ("mi", 1, "pan", 0), ("mi", 1, "rep", 0)],
)


# ---------------------------------------------------------------------------
# WB-05 — dimensionner le calcul distant
# ---------------------------------------------------------------------------

_W5 = V1A.D_WB05

R["WB-05"] = dict(
    sujet=[
        ("vis", "SLIDER", 0, 0,
         {"slider": (1000, 40000, _W5["visites"], 0), "nick": u"Visites par jour"}),
        ("part", "SLIDER", 0, 1,
         {"slider": (0.05, 0.5, _W5["part_pointe"], 2), "nick": u"Part de la pointe"}),
        ("rec", "SLIDER", 0, 2,
         {"slider": (1, 20, _W5["recalculs"], 0), "nick": u"Recalculs par visite"}),
        ("dur", "SLIDER", 0, 3,
         {"slider": (0.1, 10, _W5["duree"], 1), "nick": u"Duree d'un recalcul"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Ramener la fréquentation à l'heure de pointe : 2 160 visites, et "
         u"non les 500 d'une moyenne horaire. C'est la seule heure qui "
         u"décide du dimensionnement", [
            ("pointe", "Multiplication", 1, 0, {}),
        ]),
        (u"Chaque visite déclenche six recalculs, chacun d'1,2 seconde : "
         u"15 552 secondes de calcul à absorber", [
            ("nrec", "Multiplication", 2, 0, {}),
            ("sec", "Multiplication", 3, 0, {}),
        ]),
        (u"Une instance rend 3 600 secondes en une heure. Il en faut 4,32, "
         u"donc 5 : on ne loue pas un quart d'instance. Lisser la charge sur "
         u"les vingt-quatre heures aurait donné 1 — le service aurait tenu "
         u"la nuit et cédé le soir", [
            ("inst", "Division", 4, 0, {"val": [(1, "Number", [3600])]}),
            ("rd", "Round", 5, 0, {}),
            ("pan", "PANEL", 6, 0, {}),
        ]),
    ],
    wires=[("vis", "pointe", 0), ("part", "pointe", 1),
           ("pointe", "nrec", 0), ("rec", "nrec", 1),
           ("nrec", "sec", 0), ("dur", "sec", 1),
           ("sec", "inst", 0),
           ("inst", "rd", 0),
           ("rd", 2, "pan", 0), ("rd", 2, "rep", 0)],
)


# ---------------------------------------------------------------------------
# WB-06 — le poids du fichier
# ---------------------------------------------------------------------------

_W6 = V1A.D_WB06

R["WB-06"] = dict(
    sujet=[
        ("q", "SLIDER", 0, 0,
         {"slider": (1000, 60000, _W6["quads"], 0), "nick": u"Faces quadrangulaires"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Le format ne connaît que le TRIANGLE. Chaque quadrangle en donne "
         u"deux : 48 620 facettes, et non 24 310. C'est là que se joue "
         u"l'exercice — le reste n'est qu'une multiplication", [
            ("tri", "Multiplication", 1, 0, {"val": [(1, "Number", [2])]}),
        ]),
        (u"Cinquante octets par facette, plus les 84 octets d'en-tête : "
         u"2 431 084 octets, soit 2,32 Mio. Compter une facette par face "
         u"aurait annoncé 1,16 Mio — la moitié, et l'utilisateur reçoit le "
         u"double de ce qu'on lui a promis", [
            ("po", "Multiplication", 2, 0,
             {"val": [(1, "Number", [_W6["par_facette"]])]}),
            ("tot", "Addition", 3, 0,
             {"val": [(1, "Number", [_W6["entete"]])]}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("q", "tri", 0), ("tri", "po", 0), ("po", "tot", 0),
           ("tot", "pan", 0), ("tot", "rep", 0)],
)


# ---------------------------------------------------------------------------
# WB-07 — l'echelle qui fait tenir la piece
# ---------------------------------------------------------------------------

_W7 = V1A.D_WB07

R["WB-07"] = dict(
    sujet=[
        ("lg", "SLIDER", 0, 0,
         {"slider": (200, 6000, _W7["longueur"], 0), "nick": u"Longueur de la piece"}),
        ("ht", "SLIDER", 0, 1,
         {"slider": (200, 6000, _W7["hauteur"], 0), "nick": u"Hauteur de la piece"}),
        ("ech", "DATA:Number", 0, 3,
         {"nick": u"ECHELLES_NORMALISEES", "data": list(_W7["echelles"])}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"La zone utile est la feuille moins deux marges sur chaque "
         u"dimension : 390 × 267 mm", [
            ("zl", "Subtraction", 1, 0,
             {"val": [(0, "Number", [_W7["feuille"][0]]),
                      (1, "Number", [2 * _W7["marge"]])]}),
            ("zh", "Subtraction", 1, 2,
             {"val": [(0, "Number", [_W7["feuille"][1]]),
                      (1, "Number", [2 * _W7["marge"]])]}),
        ]),
        (u"La pièce réduite doit tenir dans les DEUX dimensions. Ici 6,10 en "
         u"longueur et 6,14 en hauteur : ni l'une ni l'autre ne tranche "
         u"seule, il faut vérifier les deux", [
            ("dl", "Division", 2, 0, {}),
            ("dh", "Division", 2, 2, {}),
            ("okl", "Smaller Than", 3, 0, {}),
            ("okh", "Smaller Than", 3, 2, {}),
        ]),
        (u"Retenir les échelles qui satisfont les deux conditions, et "
         u"prendre la première : 1:10. Le rapport exact vaut 6,10, mais "
         u"1:6,1 n'existe pas, et 1:5 déborde de 86 mm — une échelle se "
         u"choisit DANS la liste, et toujours vers la plus petite", [
            ("et", "Gate And", 4, 0, {}),
            ("cull", "Cull Pattern", 5, 0, {}),
            ("prem", "List Item", 6, 0, {"val": [(1, "Integer", [0])]}),
            ("pan", "PANEL", 7, 0, {}),
        ]),
    ],
    wires=[("lg", "dl", 0), ("ech", "dl", 1),
           ("ht", "dh", 0), ("ech", "dh", 1),
           ("dl", "okl", 0), ("zl", "okl", 1),
           ("dh", "okh", 0), ("zh", "okh", 1),
           ("okl", 1, "et", 0), ("okh", 1, "et", 1),
           ("ech", "cull", 0), ("et", "cull", 1),
           ("cull", "prem", 0),
           ("prem", "pan", 0), ("prem", "rep", 0)],
)


# ---------------------------------------------------------------------------
# IA-15 — relire le graphe d'un agent
# ---------------------------------------------------------------------------

R["IA-15"] = dict(
    sujet=[
        ("dem", "DATA:Number", 0, 0,
         {"nick": u"ENTREES_DEMANDEES",
          "data": [d for _s, _c, d, _p in V1A.D_IA15_GRAPHE]}),
        ("pro", "DATA:Number", 0, 3,
         {"nick": u"ENTREES_PRODUITES",
          "data": [p for _s, _c, _d, p in V1A.D_IA15_GRAPHE]}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Comparer liaison par liaison l'entrée DEMANDÉE et l'entrée "
         u"réellement atteinte. Les neuf liaisons existent des deux côtés : "
         u"ce n'est pas leur nombre qui diffère, c'est leur point d'arrivée", [
            ("eq", "Equality", 1, 0, {}),
        ]),
        (u"Trois désaccords, et tous les trois aboutissent sur l'entrée "
         u"d'indice 0. C'est la panne réelle des ponts agentiques : beaucoup "
         u"ignorent silencieusement l'indice demandé et écrivent sur la "
         u"première entrée. Le graphe se construit, ne signale rien, et "
         u"calcule autre chose", [
            ("cull", "Cull Pattern", 2, 0, {}),
            ("ll", "List Length", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
        (u"L'aperçu, lui, était plausible. C'est tout le sujet de "
         u"l'exercice : un graphe complet peut être entièrement faux, et il "
         u"produit alors un résultat parfaitement crédible", [
            ("note", "PANEL", 4, 2,
             {"text": u"Complet n'est pas conforme.\n\n"
                      u"Verifier les INDICES d'entree,\n"
                      u"pas seulement les composants.",
              "h": 80, "w": 260}),
        ]),
    ],
    wires=[("dem", "eq", 0), ("pro", "eq", 1),
           ("dem", "cull", 0), ("eq", 1, "cull", 1),
           ("cull", "ll", 0),
           ("ll", "pan", 0), ("ll", "rep", 0)],
)


# ---------------------------------------------------------------------------
# IA-17 — la commande cachee dans un courriel
# ---------------------------------------------------------------------------

R["IA-17"] = dict(
    sujet=[
        ("art", "DATA:Text", 0, 0,
         {"nick": u"ARTICLES_CITES",
          "data": [a for a, _q, _p in V1A.D_IA17_COMMANDE]}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Les quantités RETENUES, article par article. Elles ne se lisent "
         u"pas : elles se décident. Les vis sont écrites en toutes lettres, "
         u"les poignées sont annoncées à 12 puis corrigées à 18 plus bas "
         u"dans le message, et les crémones font l'objet d'une demande de "
         u"PRIX — elles ne sont pas commandées", [
            ("qte", "DATA:Number", 1, 0,
             {"nick": u"QUANTITES_RETENUES",
              "data": [q for _a, q, _p in V1A.D_IA17_COMMANDE]}),
        ]),
        (u"96 pièces. Additionner tout ce qui ressemble à une quantité "
         u"donnerait 138 : les crémones comptées, et les poignées comptées "
         u"deux fois. Ignorer la quantité écrite en lettres donnerait 48. "
         u"Trois erreurs, trois valeurs distinctes", [
            ("ma", "Mass Addition", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
        (u"Ce que l'exercice enseigne : une extraction automatique produit "
         u"une commande, et personne ne relit une commande produite "
         u"automatiquement. La vérification se pose AVANT, dans ce qu'on "
         u"demande d'extraire — l'intention, pas seulement le chiffre", [
            ("note", "PANEL", 3, 2,
             {"text": u"Un chiffre dans un texte n'est\n"
                      u"pas une quantite commandee.\n\n"
                      u"Extraire l'INTENTION.",
              "h": 80, "w": 260}),
        ]),
    ],
    wires=[("qte", "ma", 0), ("ma", "pan", 0), ("ma", "rep", 0)],
)


# ---------------------------------------------------------------------------
# Les quatre questions charnieres de la vague
# ---------------------------------------------------------------------------

R["DV-05"] = recette_charniere(_e("DV-05"),
    u"Composant scripte : une copie par definition.\n"
    u"Plugin compile  : une version, N definitions.\n\n"
    u"Le gain est de DISTRIBUTION,\n"
    u"pas de vitesse.")

R["DV-06"] = recette_charniere(_e("DV-06"),
    u".gha -> vit dans Grasshopper.\n"
    u".rhp -> declare des commandes Rhino.\n\n"
    u"Le calcul va dans une bibliotheque\n"
    u"que les deux referencent. Sinon ils\n"
    u"divergent des la premiere correction.")

R["IA-16"] = recette_charniere(_e("IA-16"),
    u"Un garde-fou ne vaut que s'il tient\n"
    u"quand on cesse de regarder.\n\n"
    u"Borner ce qui est reversible,\n"
    u"faire confirmer le reste.")

R["IA-18"] = recette_charniere(_e("IA-18"),
    u"Une image generee porte une INTENTION.\n\n"
    u"Elle ne porte ni cotes, ni epaisseurs,\n"
    u"ni assemblages — ni la question de\n"
    u"savoir si cela tient debout.")
