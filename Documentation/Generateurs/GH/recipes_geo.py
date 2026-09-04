# -*- coding: utf-8 -*-
"""Recettes des exercices a geometrie : le sujet MESURE, le corrige etalonne.

Ces exercices demandent de modeliser dans RHINO. La definition n'a donc rien a
construire — elle mesure. D'ou deux zones de nature differente :

  SUJET   : un parametre de reference vide, la chaine de mesure, et REPONSE.
            Tant que l'apprenant n'a rien modelise, rien ne sort. C'est normal,
            et c'est le principe meme de ces exercices.

  CORRIGE : la geometrie de REFERENCE internalisee, la meme chaine de mesure,
            et donc la valeur attendue. C'est l'etalon contre lequel l'apprenant
            confronte sa propre production.

On emploie un parametre de reference plutot qu'un filtre de calque : le filtre
se regle dans l'interface et ne se transporte pas dans le fichier enregistre.
La fiche demande a l'apprenant de le poser lui-meme — c'est d'ailleurs la
competence evaluee par RH-02.
"""
import os
import sys

_ICI = os.path.dirname(os.path.abspath(__file__))
_GEN = os.path.abspath(os.path.join(_ICI, ".."))
for _p in (_ICI, _GEN):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import domaine_rhino as _RH

R = {}


def _pts(liste, z=0.0):
    return [(float(x), float(y), z) for x, y in liste]


# ---------------------------------------------------------------------------
# RH-02 — compter les porteurs isoles sur leur calque
# ---------------------------------------------------------------------------

R["RH-02"] = dict(
    sujet=[
        ("ref", "PARAM:Point", 0, 0, {"nick": u"POINTS_DU_CALQUE_PORTEURS"}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon : les douze porteurs, tels qu'ils doivent rester une fois "
         u"les six cloisons écartées sur leur propre calque", [
            ("geo", "GEO:Point", 1, 0,
             {"nick": u"PORTEURS_DE_REFERENCE",
              "geo": ("pts", _pts(_RH.D_RH02_PORTEURS))}),
        ]),
        (u"Compter ne demande qu'un composant. Toute la difficulté est en "
         u"amont, dans Rhino : ce qui est compté doit venir d'un CALQUE et non "
         u"d'une sélection, sans quoi le compte cesse de suivre dès la "
         u"prochaine livraison du géomètre", [
            ("ll", "List Length", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("geo", "ll", 0), ("ll", "pan", 0), ("ll", "rep", 0)],
)


# ---------------------------------------------------------------------------
# RH-03 — compter les plots de la trame
# ---------------------------------------------------------------------------

_PLOTS = [(x * 600.0, y * 600.0) for y in range(6) for x in range(8)]

R["RH-03"] = dict(
    sujet=[
        ("ref", "PARAM:Point", 0, 0, {"nick": u"CENTRES_DES_PLOTS"}),
        ("rep", "REPONSE", 4, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon : huit positions en longueur, six en largeur. 4 200 ÷ 600 "
         u"vaut 7 intervalles, donc 8 nœuds. C'est là que se joue l'exercice — "
         u"et un angle de terrasse sans appui avec", [
            ("geo", "GEO:Point", 1, 0,
             {"nick": u"PLOTS_DE_REFERENCE", "geo": ("pts", _pts(_PLOTS))}),
        ]),
        (u"48 plots : six rangées de huit", [
            ("ll", "List Length", 2, 0, {}),
            ("pan", "PANEL", 3, 0, {}),
        ]),
    ],
    wires=[("geo", "ll", 0), ("ll", "pan", 0), ("ll", "rep", 0)],
)


# ---------------------------------------------------------------------------
# RH-05 — volume de matiere retiree d'une platine
# ---------------------------------------------------------------------------

R["RH-05"] = dict(
    sujet=[
        ("ref", "PARAM:Brep", 0, 0, {"nick": u"PLATINE_PERCEE"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon : la platine pleine, 300 × 200 × 15 mm", [
            ("pleine", "GEO:Brep", 1, 0,
             {"nick": u"PLATINE_PLEINE",
              "geo": ("box", (0, 0, 0), 300, 200, 15)}),
        ]),
        (u"Les quatre perçages, Ø 18 mm. Ils DÉPASSENT de la platine, de part "
         u"et d'autre : deux faces coplanaires ne se coupent pas proprement, "
         u"et la booléenne échouerait sur des cylindres posés à fleur", [
            ("trous", "GEO:Brep", 1, 2,
             {"nick": u"PERCAGES",
              "geo": ("cyls", [((40, 40, -5), 9, 25), ((260, 40, -5), 9, 25),
                               ((40, 160, -5), 9, 25),
                               ((260, 160, -5), 9, 25)])}),
        ]),
        (u"Percer, puis mesurer les deux volumes", [
            ("dif", "Solid Difference", 2, 0, {}),
            ("v2", "Volume", 3, 2, {}),
            ("v1", "Volume", 3, 0, {}),
        ]),
        (u"La matière retirée est la DIFFÉRENCE des deux volumes, non le "
         u"volume des cylindres : ceux-ci dépassent, et les compter entiers "
         u"donnerait 25 447 mm³ au lieu de 15 268", [
            ("sub", "Subtraction", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("pleine", "dif", 0), ("trous", "dif", 1),
           ("pleine", "v2", 0), ("dif", "v1", 0),
           ("v2", "sub", 0), ("v1", "sub", 1),
           ("sub", "pan", 0), ("sub", "rep", 0)],
)


# ---------------------------------------------------------------------------
# RH-08 — refermer un caisson, et le prouver
# ---------------------------------------------------------------------------

R["RH-08"] = dict(
    sujet=[
        ("ref", "PARAM:Brep", 0, 0, {"nick": u"CAISSON_A_REFERMER"}),
        ("rep", "REPONSE", 5, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon : le caisson tel qu'il est livré, deux faces manquantes. "
         u"À l'écran, rien ne le distingue d'un solide", [
            ("geo", "GEO:Brep", 1, 0,
             {"nick": u"CAISSON_OUVERT",
              # Le dernier argument est la LISTE des faces a retirer.
              # Essayees dans Rhino : seule la paire [4, 5] laisse des
              # ouvertures que CapPlanarHoles sait refermer ; [0,1], [2,3]
              # et [3,5] rendent un brep non solide, volume nul.
              "geo": ("boxouvert", (0, 0, 0), 420, 260, 180, [4, 5])}),
        ]),
        (u"Refermer les ouvertures planes", [
            ("cap", "Cap Holes", 2, 0, {}),
        ]),
        (u"Le volume EST la preuve : une enveloppe ouverte n'en a pas. "
         u"19 656 000 mm³ une fois fermée. Mesurer avant de refermer rend "
         u"bien une valeur — et elle ne veut rien dire", [
            ("vo", "Volume", 3, 0, {}),
            ("pan", "PANEL", 4, 0, {}),
        ]),
    ],
    wires=[("geo", "cap", 0), ("cap", "vo", 0),
           ("vo", "pan", 0), ("vo", "rep", 0)],
)


# ---------------------------------------------------------------------------
# RH-09 — facteur d'echelle maximal pour le plateau d'impression
# ---------------------------------------------------------------------------

R["RH-09"] = dict(
    sujet=[
        ("ref", "PARAM:Brep", 0, 0, {"nick": u"PIECE_A_IMPRIMER"}),
        ("px", "SLIDER", 0, 2,
         {"slider": (100, 400, 220, 0), "nick": u"Plateau X"}),
        ("rep", "REPONSE", 11, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon : la pièce, 380 × 260 × 195 mm hors tout", [
            ("geo", "GEO:Brep", 1, 0,
             {"nick": u"PIECE_DE_REFERENCE",
              "geo": ("box", (0, 0, 0), 380, 260, 195)}),
        ]),
        (u"Encadrer la pièce, puis en extraire la LONGUEUR selon X. "
         u"L'encadrement rend des intervalles, non des nombres : il faut les "
         u"décomposer, sinon on divise une cote par un domaine et le résultat "
         u"n'a pas de sens", [
            ("bb", "Bounding Box", 2, 0, {}),
            ("db", "Deconstruct Box", 3, 0, {}),
            ("dd", "Deconstruct Domain", 4, 0, {}),
            ("lx", "Subtraction", 5, 0, {}),
        ]),
        (u"Un rapport par axe : 220÷380 = 0,579, 220÷260 = 0,846, "
         u"250÷195 = 1,282. Le troisième passerait sans réduction ; prendre "
         u"la moyenne donnerait 0,90 et la pièce ne rentrerait pas. C'est le "
         u"plus PETIT qui commande", [
            ("note", "PANEL", 5, 4,
             {"text": u"0.579  /  0.846  /  1.282" + chr(10) + u"le plus PETIT commande",
              "h": 56, "w": 240}),
        ]),
        (u"Arrondi VERS LE BAS au centième : 0,57. Au plus proche on "
         u"obtiendrait 0,58, et la pièce dépasserait — ce que la machine "
         u"découvre après trois heures d'impression, pas avant", [
            ("dv", "Division", 6, 0, {}),
            ("mu", "Multiplication", 7, 0, {"val": [(1, "Number", [100])]}),
            ("rd", "Round", 8, 0, {}),
            ("dv2", "Division", 9, 0, {"val": [(1, "Number", [100])]}),
            ("pan", "PANEL", 10, 0, {}),
        ]),
    ],
    wires=[("geo", "bb", 0), ("bb", "db", 0),
           ("db", 1, "dd", 0),
           ("dd", 1, "lx", 0), ("dd", 0, "lx", 1),
           ("px", "dv", 0), ("lx", "dv", 1),
           ("dv", "mu", 0), ("mu", "rd", 0),
           ("rd", 1, "dv2", 0),
           ("dv2", "pan", 0), ("dv2", "rep", 0)],
)


# ---------------------------------------------------------------------------
# GP-03 — mailler une surface sous un ecart impose
# ---------------------------------------------------------------------------

R["GP-03"] = dict(
    sujet=[
        ("ref", "PARAM:Brep", 0, 0, {"nick": u"SURFACE_A_MAILLER"}),
        ("rep", "REPONSE", 6, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon : une nappe présentant une zone de forte courbure et une "
         u"zone presque plane. Un maillage à densité uniforme y est toujours "
         u"mauvais quelque part — c'est ce qui oblige à raisonner en écart", [
            ("geo", "GEO:Surface", 1, 0,
             {"nick": u"NAPPE_DE_REFERENCE",
              "geo": ("srf", [(0, 0, 0), (200, 0, 40), (400, 0, 0),
                              (0, 200, 30), (200, 200, 160), (400, 200, 30),
                              (0, 400, 0), (200, 400, 40), (400, 400, 0)],
                      3, 3)}),
        ]),
        (u"Mailler en fixant l'ÉCART, non la densité : régler la densité à "
         u"l'œil produit soit un maillage grossier qui paraît lisse à l'écran, "
         u"soit un maillage inutilement lourd", [
            ("mb", "Mesh Brep", 2, 0, {}),
        ]),
        (u"Compter les faces obtenues. C'est la contrepartie directe de la "
         u"finesse, et du poids du fichier exporté", [
            ("dm", "Deconstruct Mesh", 3, 0, {}),
            ("ll", "List Length", 4, 0, {}),
            ("pan", "PANEL", 5, 0, {}),
        ]),
    ],
    wires=[("geo", "mb", 0), ("mb", "dm", 0),
           ("dm", 1, "ll", 0), ("ll", "pan", 0), ("ll", "rep", 0)],
)


# ---------------------------------------------------------------------------
# FA-02 — developpe d'une virole conique
# ---------------------------------------------------------------------------

R["FA-02"] = dict(
    sujet=[
        ("rg", "SLIDER", 0, 0,
         {"slider": (50, 400, 180, 0), "nick": u"Grand rayon"}),
        ("rp", "SLIDER", 0, 1,
         {"slider": (20, 300, 95, 0), "nick": u"Petit rayon"}),
        ("ht", "SLIDER", 0, 2,
         {"slider": (100, 800, 340, 0), "nick": u"Hauteur"}),
        ("rep", "REPONSE", 8, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"Contrôle par le calcul, indépendant du déroulé. La génératrice "
         u"n'est PAS la hauteur : elle vaut la racine de la hauteur au carré "
         u"plus l'écart des rayons au carré — 350,46 mm ici, contre 340 de "
         u"hauteur. Deux pour cent d'écart, et la virole ne se referme pas", [
            ("dr", "Subtraction", 1, 0, {}),
            ("dr2", "Multiplication", 2, 0, {}),
            ("h2", "Multiplication", 2, 2, {}),
            ("som", "Addition", 3, 0, {}),
            ("gen", "Square Root", 4, 0, {}),
        ]),
        (u"Surface développée : π multiplié par la somme des rayons, "
         u"multiplié par la génératrice", [
            ("sr", "Addition", 3, 4, {}),
            ("pi", "Pi", 4, 4, {"val": [(0, "Number", [1])]}),
            ("m1", "Multiplication", 5, 3, {}),
            ("m2", "Multiplication", 6, 0, {}),
        ]),
        (u"En mètres carrés : 0,3028. Prendre la hauteur pour la génératrice "
         u"donnerait 0,2938 — moins de trois pour cent d'écart, invisible sur "
         u"un devis, fatal à l'atelier", [
            ("cv", "Division", 7, 0, {"val": [(1, "Number", [1000000])]}),
            ("pan", "PANEL", 8, 2, {}),
        ]),
    ],
    wires=[("rg", "dr", 0), ("rp", "dr", 1),
           ("dr", "dr2", 0), ("dr", "dr2", 1),
           ("ht", "h2", 0), ("ht", "h2", 1),
           ("h2", "som", 0), ("dr2", "som", 1), ("som", "gen", 0),
           ("rg", "sr", 0), ("rp", "sr", 1),
           ("sr", "m1", 0), ("pi", "m1", 1),
           ("m1", "m2", 0), ("gen", "m2", 1),
           ("m2", "cv", 0), ("cv", "pan", 0), ("cv", "rep", 0)],
)


# ---------------------------------------------------------------------------
# RH-04 — la surface du bardage, montee a la verticale
# ---------------------------------------------------------------------------

#: ligne au sol du releve : sa courbure varie d'un bout a l'autre, ce qui est
#: precisement ce qui separe une extrusion VERTICALE d'une extrusion suivant
#: la normale. Les deux se ressemblent a l'ecran ; elles ne donnent pas la
#: meme aire.
_SOL_RH04 = [(0, 0), (2400, 900), (5200, 700), (7800, 2100), (10500, 1800)]

R["RH-04"] = dict(
    sujet=[
        ("ref", "PARAM:Curve", 0, 0, {"nick": u"LIGNE_AU_SOL"}),
        ("rep", "REPONSE", 7, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon : la ligne au sol du relevé, telle que le géomètre la "
         u"livre — une courbe dont le rayon change tout au long du tracé", [
            ("geo", "GEO:Curve", 1, 0,
             {"nick": u"LIGNE_DE_REFERENCE",
              "geo": ("interp", _pts(_SOL_RH04))}),
        ]),
        (u"La direction de montée est VERTICALE, et vaut 2 800 mm. C'est un "
         u"vecteur explicite, non la normale de la courbe : sur un tracé "
         u"dont la courbure varie, suivre la normale donnerait une nappe "
         u"gauche, voisine à l'œil et fausse au métré", [
            ("h", "DATA:Number", 1, 2,
             {"nick": u"HAUTEUR_DE_BARDAGE", "data": [2800]}),
            ("uz", "Unit Z", 2, 2, {}),
            ("ex", "Extrude", 3, 0, {}),
        ]),
        (u"L'aire vient en millimètres carrés : la ramener au mètre carré "
         u"est le dernier geste, et le plus souvent oublié. 31,24 m²", [
            ("ar", "Area", 4, 0, {}),
            ("cv", "Division", 5, 0, {"val": [(1, "Number", [1000000])]}),
            ("pan", "PANEL", 6, 2, {}),
        ]),
    ],
    wires=[("geo", "ex", 0), ("h", "uz", 0), ("uz", "ex", 1),
           ("ex", "ar", 0), ("ar", "cv", 0),
           ("cv", "pan", 0), ("cv", "rep", 0)],
)


# ---------------------------------------------------------------------------
# DV-02 — les portions trop cintrees pour la machine
# ---------------------------------------------------------------------------

#: trace a cintrer : un long parcours calme, et un coude ou le rayon tombe a
#: 155 mm. La zone sous 250 mm mesure quelque 106 mm sur pres de six metres
#: de developpe — invisible a qui echantillonne tous les 200 mm.
#:
#: ATTENTION : le decoupage se fait a LONGUEUR D'ARC constante, ce que fait
#: Divide Curve. Echantillonner a pas de PARAMETRE constant donne 406 mm au
#: lieu de 106 : les parametres d'une NURBS se resserrent dans les courbes,
#: et la zone cintree se retrouve comptee quatre fois. C'est l'erreur que
#: j'ai faite en calibrant cet exercice, et elle ne se voit pas.
_TRACE_DV02 = [(0, 0), (1800, 0), (2800, 300), (2940, 608),
               (3700, 1150), (5500, 1250)]

R["DV-02"] = dict(
    sujet=[
        ("ref", "PARAM:Curve", 0, 0, {"nick": u"TRACE_A_CINTRER"}),
        ("rc", "SLIDER", 0, 2,
         {"slider": (100, 500, 250, 0), "nick": u"Rayon de cintrage mini"}),
        ("rep", "REPONSE", 10, 0, {"type": "Number"}),
    ],
    corrige=[
        (u"L'étalon : le tracé livré par le bureau d'études", [
            ("geo", "GEO:Curve", 1, 0,
             {"nick": u"TRACE_DE_REFERENCE",
              "geo": ("interp", _pts(_TRACE_DV02))}),
        ]),
        (u"Le pas d'échantillonnage EST la réponse à l'exercice : 3 000 pas "
         u"sur 5 988 mm font un point tous les 2 mm. À 200 mm, la zone "
         u"entière passe entre deux échantillons et la pièce est déclarée "
         u"fabricable. Le découpage se fait à LONGUEUR d'arc constante : "
         u"un pas de paramètre constant resserrerait les points dans les "
         u"courbes et compterait la zone quatre fois", [
            ("n", "DATA:Integer", 1, 2,
             {"nick": u"NOMBRE_DE_PAS", "data": [3000]}),
            ("dc", "Divide Curve", 2, 0, {}),
            ("cv", "Curvature", 3, 0, {}),
        ]),
        (u"Le rayon de courbure est l'INVERSE de la courbure. Comparer "
         u"directement les courbures reviendrait à inverser le sens du "
         u"critère : la zone dangereuse est celle où la courbure est GRANDE", [
            ("vl", "Vector Length", 4, 0, {}),
            ("inv", "Division", 5, 0, {"val": [(0, "Number", [1])]}),
        ]),
        (u"Retenir les échantillons dont le rayon descend sous 250 mm, puis "
         u"les compter", [
            ("st", "Smaller Than", 6, 0, {"val": [(1, "Number", [250])]}),
            ("cull", "Cull Pattern", 7, 0, {}),
            ("ll", "List Length", 8, 0, {}),
        ]),
        (u"La longueur cumulée est le nombre d'échantillons retenus "
         u"multiplié par le pas. 106 mm, sur un développé de 5 988 mm", [
            ("lg", "Length", 2, 4, {}),
            ("pas", "Division", 6, 4, {}),
            ("cum", "Multiplication", 9, 0, {}),
            ("pan", "PANEL", 9, 3, {}),
        ]),
    ],
    wires=[("geo", "dc", 0), ("n", "dc", 1),
           ("geo", "cv", 0), ("dc", 2, "cv", 1),
           ("cv", 1, "vl", 0), ("vl", "inv", 1),
           ("inv", "st", 0),
           ("inv", "cull", 0), ("st", "cull", 1), ("cull", "ll", 0),
           ("geo", "lg", 0), ("lg", "pas", 0), ("n", "pas", 1),
           ("ll", "cum", 0), ("pas", "cum", 1),
           ("cum", "pan", 0), ("cum", "rep", 0)],
)
