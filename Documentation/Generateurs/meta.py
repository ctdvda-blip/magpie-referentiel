# -*- coding: utf-8 -*-
# Classification des 97 items distincts issus des programmes de formation
# index -> (domaine, categorie, notion, niveau, validation, type exercice)

D0 = "0 – Socle Rhino (prérequis)"
D1 = "1 – Environnement et principes Grasshopper"
D2 = "2 – Données et logique"
D3 = "3 – Géométrie paramétrique"
D4 = "4 – Mesures, quantitatifs et export"
D5 = "5 – Méthode, performance et évènements"
D6 = "6 – Algorithmique avancée"
D7 = "7 – Développement, scripting et API"
D8 = "8 – Interfaces, web et interopérabilité"
D9 = "9 – Aide à la fabrication"

DOMAINES = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9]

DEB = "Débutant"
INT = "Intermédiaire"
PER = "Perfectionnement"
EXP = "Expert"
NIVEAUX = [DEB, INT, PER, EXP]

EOL = "ExactOrderedList"
SEQ = "SetEquality"
SV = "SingleValue"
NT = "NumericTolerance"
GT = "GeometryTolerance"
CO = "Conceptuel (QCM)"
MODES = [EOL, SEQ, SV, NT, GT, CO]

EX = "Exercice Grasshopper"
SY = "Exercice de synthèse"
QC = "QCM / question ciblée"
DM = "Démonstration formateur"
TYPES = [EX, SY, QC, DM]

META = {
1: (D1, "Principes de la conception paramétrique", "Conception paramétrique et programmation visuelle", DEB, CO, QC),
2: (D1, "Interopérabilité Rhino – Grasshopper", "Bake et Geometry Pipeline", DEB, GT, EX),
3: (D1, "Flux de données et câblage", "Curseurs, entrées, panel, sorties, branchement des câbles", DEB, SV, EX),
4: (D1, "Interface et canvas", "Barre d'outils et navigation dans le canvas", DEB, CO, QC),
5: (D3, "Géométrie vectorielle", "Points, vecteurs et plans", DEB, GT, EX),
6: (D3, "Géométrie filaire", "Cercles, carrés, polygones, courbes", DEB, GT, EX),
7: (D3, "Division de courbes", "Outils de division et d'échantillonnage de courbes", DEB, GT, EX),
8: (D3, "Dessin paramétrique 2D", "Exercice d'application – plan paramétrique", DEB, GT, SY),
9: (D3, "Cotation automatique", "Génération automatique des cotations", DEB, SEQ, EX),
10: (D3, "Transformations", "Matrice linéaire, polaire, rotation, symétrie", DEB, GT, EX),
11: (D3, "Matrices rectangulaires et polaires", "Réseaux rectangulaires et polaires", DEB, GT, EX),
12: (D3, "Surfaces", "Balayage, surface par section", DEB, GT, EX),
13: (D3, "Solides fermés", "Fermeture d'une polysurface en solide étanche", DEB, SV, EX),
14: (D3, "Intersections entre solides", "Recherche d'intersection entre géométries", DEB, GT, EX),
15: (D3, "Détection de collisions", "Détection de collisions entre objets", DEB, SEQ, EX),
16: (D3, "Modèle 3D paramétrique", "Exercice d'application – modèle 3D paramétrique", DEB, GT, SY),
17: (D2, "Listes – traitement et tri", "Outils de traitement des listes, tri croissant / décroissant", DEB, EOL, EX),
18: (D2, "Arbres – construction et lecture", "Création, lecture et numérotation des branches", INT, SEQ, EX),
19: (D4, "Mesures dimensionnelles", "Longueurs, aires, volumes", DEB, NT, EX),
20: (D4, "Rayon et courbure", "Mesure de rayon et de courbure", DEB, NT, EX),
21: (D4, "Centre de gravité", "Recherche du centre de gravité", DEB, NT, EX),
22: (D4, "Métrés", "Exercice d'application – calcul de métrés", INT, NT, SY),
23: (D4, "Chiffrage et devis", "Devis généré à partir d'un modèle 3D", INT, NT, SY),
24: (D2, "Arbres – Graft et Flatten", "Approfondissement listes et arbres, Graft / Flatten", INT, SEQ, EX),
25: (D5, "Organisation et lisibilité", "Clusters, nommage, groupes, titres", INT, CO, QC),
26: (D5, "Performance d'exécution", "Multiprocessing et analyse des temps d'exécution", PER, NT, EX),
27: (D5, "Ordre d'exécution des tâches", "Déclencheurs, Timer, chronologie", PER, CO, QC),
28: (D6, "Boucles et itération", "Hoopsnake et Anemone", PER, EOL, EX),
29: (D6, "Simulation physique", "Moteur physique Kangaroo, recherche d'équilibre", PER, GT, EX),
30: (D6, "Design génératif", "Algorithme génétique Galapagos", PER, NT, EX),
31: (D8, "Interfaçage d'une définition", "Remote control panel, interface WPF / C# dans Rhino", PER, CO, DM),
32: (D8, "Intégration dans Rhino", "Lier une définition à un bouton de barre d'outils", PER, CO, DM),
33: (D7, "Composant compilé .gha", "Réaliser un composant *.gha pour Grasshopper", EXP, CO, DM),
34: (D7, "Compilation en plugin .rhp", "Compiler une définition en plugin *.rhp", EXP, CO, DM),
35: (D7, "Scripting dans Grasshopper", "Composant VB / C# / Python personnalisé", EXP, SV, EX),
36: (D4, "Comptage de quantités", "Comptage automatique des quantités de blocs", INT, SV, EX),
37: (D4, "Préparation de données tabulaires", "Préparation des colonnes de données", INT, EOL, EX),
38: (D4, "Export Excel", "Export d'un tableau vers une feuille de calcul", INT, CO, DM),
39: (D4, "Export CSV / nomenclature", "Export d'une nomenclature au format CSV", INT, CO, DM),
40: (D5, "Évènement clavier", "Détection de l'appui sur une touche", PER, CO, DM),
41: (D5, "Évènement souris", "Détection du mouvement de la souris", PER, CO, DM),
42: (D7, "API RhinoCommon", "API RhinoCommon en Python, C#.NET, VB.NET", EXP, CO, QC),
43: (D7, "Librairies opensource Rhino", "openNURBS, Rhino3dm", EXP, CO, QC),
44: (D7, "API Grasshopper", "API Grasshopper", EXP, CO, QC),
45: (D7, "Composant Python", "Écrire un composant Python personnalisé", EXP, SV, EX),
46: (D7, "Composant VB / C#", "Écrire un composant VB / C# personnalisé", EXP, SV, EX),
47: (D7, "IDE Visual Studio – templates", "Templates disponibles sous Visual Studio", EXP, CO, DM),
48: (D7, "Plugin Rhino en C#.NET", "Composant plugin Rhino sous Visual Studio", EXP, CO, DM),
49: (D3, "Maillages – génération", "Générer des maillages avec Weaverbird", PER, GT, EX),
50: (D3, "Maillages – lissage", "Adoucir un maillage", PER, GT, EX),
51: (D3, "Maillages – réparation", "Réparer un maillage avec Mesh+", PER, GT, EX),
52: (D3, "SubD – génération", "Générer une surface SubD depuis un maillage", PER, GT, EX),
53: (D3, "SubD – déformation", "Déformer une SubD à partir d'un squelette", PER, GT, EX),
54: (D8, "Publication web ShapeDiver", "Mise en ligne d'une définition Grasshopper", PER, CO, DM),
55: (D8, "Téléchargement de modèles 3D", "Bouton de téléchargement de modèles 3D", PER, CO, DM),
56: (D8, "Génération de plans PDF", "Bouton de téléchargement de plans PDF", PER, CO, DM),
57: (D8, "Rhino.Inside", "Interopérabilité avec un autre logiciel", EXP, CO, DM),
58: (D8, "Rhino.Compute", "Appel de fonctions Rhino / Grasshopper depuis un site web", EXP, CO, DM),
59: (D9, "Imbrication 2D (OpenNest)", "Imbrication de pièces dans des plaques de matière", PER, GT, EX),
60: (D9, "Imbrication 3D", "Imbrication 3D pour la mise en carton", PER, GT, EX),
61: (D9, "Déroulé de surface", "Fonctions de déroulé de surface", PER, GT, EX),
62: (D9, "Déroulé de tôle", "Déroulé avec épaisseur et retrait", PER, NT, EX),
63: (D1, "Installation de plugins – Food4Rhino", "Installer un plugin depuis un .gha ou .exe", INT, CO, DM),
64: (D1, "Installation de plugins – Package Manager", "Installer un plugin depuis le Package Manager", INT, CO, DM),
65: (D1, "Plugins d'ergonomie – principe", "Customisation de l'interface Grasshopper", INT, CO, QC),
66: (D1, "Plugin Bifocals", "Étiquettes flottantes au-dessus des composants", INT, CO, DM),
67: (D1, "Plugin SnappingGecko", "Aimantation et rangement des composants", INT, CO, DM),
68: (D1, "Plugin Palette", "Couleurs de l'interface Grasshopper", INT, CO, DM),
69: (D1, "Plugin Moonlight", "Mode sombre de l'interface", INT, CO, DM),
70: (D1, "Plugin pOd", "Vue Rhino affichée sur le canvas", INT, CO, DM),
71: (D1, "Plugin AutoGraph", "Rangement automatique de la définition", INT, CO, DM),
72: (D1, "Plugins fonctionnels – principe", "Plugins essentiels ajoutant des fonctions", INT, CO, QC),
73: (D1, "Plugins fonctionnels essentiels", "Metahopper, Human, Elefront, Weaverbird, Pufferfish, LunchBox", INT, CO, QC),
74: (D0, "Interface Rhino", "Barres d'outils, fenêtres, options", DEB, CO, QC),
75: (D0, "Manipulation des vues", "Gestion des fenêtres et des vues", DEB, CO, QC),
76: (D0, "Navigation", "Zoom, panoramique, rotation", DEB, CO, QC),
77: (D0, "Objets de base", "Cubes, sphères, cylindres", DEB, GT, EX),
78: (D0, "Transformations de base", "Déplacer, tourner, échelle, orienter", DEB, GT, EX),
79: (D0, "Sélection d'objets", "Sélection et manipulation d'objets", DEB, CO, QC),
80: (D0, "Groupes et blocs", "Groupes et blocs Rhino", DEB, CO, QC),
81: (D0, "Visibilité des objets", "Verrouillage, masquage, isoler, montrer", DEB, CO, QC),
82: (D0, "Courbes Rhino", "Lignes, cercles, ellipses", DEB, GT, EX),
83: (D0, "Surfaces depuis courbes", "Générer des surfaces à partir de courbes", DEB, GT, EX),
84: (D0, "Extrusion", "Extrusion et création de surfaces", DEB, GT, EX),
85: (D0, "Opérations booléennes Rhino", "Union, intersection, soustraction", DEB, GT, EX),
86: (D0, "Calques", "Gestion des calques", DEB, CO, QC),
87: (D0, "Propriétés d'objet", "Couleurs, matériaux, propriétés", DEB, CO, QC),
88: (D0, "Contraintes d'impression 3D", "Épaisseur minimale, angle de surplomb", DEB, CO, QC),
89: (D0, "Précision et unités", "Modélisation de précision et unités de mesure", DEB, CO, QC),
90: (D0, "Échelle et précision", "Paramétrage des unités, échelle et précision", DEB, CO, QC),
91: (D0, "Solides pour impression 3D", "Création de solides imprimables", DEB, SV, EX),
92: (D0, "Solides étanches", "Construction de solides fermés et étanches", DEB, SV, EX),
93: (D0, "Contrôle des erreurs", "Trous, surfaces ouvertes", DEB, SV, EX),
94: (D0, "Réseaux et répétitions", "Réseaux et répétition de formes", DEB, GT, EX),
95: (D0, "Outils d'analyse", "Détection des erreurs par analyse", DEB, CO, QC),
96: (D0, "Commandes de correction", "Remplissage de trous, jointure", DEB, SV, EX),
97: (D0, "Export STL / OBJ", "Export et optimisation des maillages", DEB, CO, DM),
}

# Fondamentaux V1 (19 notions) : couverture par les programmes de formation
# ordre V1 -> (couverture, items programme rattaches, domaine, categorie, niveau)
FOND_MAP = {
1:  ("Non couverte", "",   D2, "Types et conversion implicite", DEB),
2:  ("Non couverte", "",   D2, "Types et conversion implicite", INT),
3:  ("Couverte",     "17", D2, "Listes – traitement et tri", DEB),
4:  ("Partielle",    "17", D2, "Listes – séries et longueur", DEB),
5:  ("Non couverte", "",   D2, "Comportements implicites", INT),
6:  ("Non couverte", "",   D2, "Comportements implicites", INT),
7:  ("Couverte",     "17", D2, "Listes – traitement et tri", DEB),
8:  ("Partielle",    "17", D2, "Listes – filtrage et répartition", INT),
9:  ("Partielle",    "17", D2, "Listes – décalage et permutation", INT),
10: ("Non couverte", "",   D2, "Comportements implicites", INT),
11: ("Couverte",     "18", D2, "Arbres – construction et lecture", INT),
12: ("Couverte",     "24", D2, "Arbres – Graft et Flatten", INT),
13: ("Partielle",    "24", D2, "Arbres – nettoyage de structure", INT),
14: ("Partielle",    "27", D2, "Comportements implicites", INT),
15: ("Non couverte", "",   D2, "Outils de texte", DEB),
16: ("Non couverte", "",   D2, "Outils de texte", INT),
17: ("Non couverte", "",   D2, "Logique et conditions", DEB),
18: ("Non couverte", "",   D2, "Logique et conditions", INT),
19: ("Non couverte", "",   D2, "Logique et conditions", INT),
}

# --- Regroupement en categories pedagogiques (niveau intermediaire de la hierarchie)
GROUPES = [
 (D0, "Interface et navigation Rhino",        [74,75,76,79,80,81]),
 (D0, "Modélisation Rhino",                   [77,78,82,83,84,85,94]),
 (D0, "Organisation du document Rhino",       [86,87]),
 (D0, "Préparation à l'impression 3D",        [88,89,90,91,92,93,95,96,97]),
 (D1, "Principes et interface Grasshopper",   [1,2,3,4]),
 (D1, "Écosystème de plugins",                [63,64,65,66,67,68,69,70,71,72,73]),
 (D2, "Types et conversion implicite",        []),
 (D2, "Listes",                               [17]),
 (D2, "Arbres de données",                    [18,24]),
 (D2, "Comportements implicites",             []),
 (D2, "Outils de texte",                      []),
 (D2, "Portes logiques",                      []),
 (D3, "Géométrie vectorielle et filaire",     [5,6,7]),
 (D3, "Plan paramétrique",                    [8,9]),
 (D3, "Transformations et réseaux",           [10,11]),
 (D3, "Surfaces et solides",                  [12,13,14,15]),
 (D3, "Maillages et SubD",                    [49,50,51,52,53]),
 (D3, "Synthèse géométrie",                   [16]),
 (D4, "Mesures géométriques",                 [19,20,21]),
 (D4, "Quantitatifs et chiffrage",            [22,23,36]),
 (D4, "Export de données",                    [37,38,39]),
 (D5, "Organisation et performance",          [25,26]),
 (D5, "Chronologie et évènements",            [27,40,41]),
 (D6, "Boucles et itération",                 [28]),
 (D6, "Simulation physique",                  [29]),
 (D6, "Design génératif",                     [30]),
 (D7, "Scripting dans Grasshopper",           [35,45,46]),
 (D7, "API et librairies",                    [42,43,44]),
 (D7, "Compilation et IDE",                   [33,34,47,48]),
 (D8, "Interfaces utilisateur",               [31,32]),
 (D8, "Publication web",                      [54,55,56]),
 (D8, "Interopérabilité",                     [57,58]),
 (D9, "Imbrication",                          [59,60]),
 (D9, "Déroulé et mise à plat",               [61,62]),
]

_GRP = {}
for _d, _c, _ids in GROUPES:
    for _i in _ids:
        _GRP[_i] = _c

# Reconstruction : categorie = groupe pedagogique, notion = libelle court
_NEW = {}
for _i, _t in META.items():
    _NEW[_i] = (_t[0], _GRP[_i], _t[1], _t[3], _t[4], _t[5])
META = _NEW

# Categories des fondamentaux V1 alignees sur les groupes
_FCAT = {
 1:"Types et conversion implicite", 2:"Types et conversion implicite",
 3:"Listes", 4:"Listes", 7:"Listes", 8:"Listes", 9:"Listes",
 5:"Comportements implicites", 6:"Comportements implicites",
 10:"Comportements implicites", 14:"Comportements implicites",
 11:"Arbres de données", 12:"Arbres de données", 13:"Arbres de données",
 15:"Outils de texte", 16:"Outils de texte",
 17:"Portes logiques", 18:"Portes logiques", 19:"Portes logiques",
}
FOND_MAP = dict((k, (v[0], v[1], v[2], _FCAT[k], v[4])) for k, v in FOND_MAP.items())

CAT_ORDER_D2 = ["Types et conversion implicite", "Listes", "Arbres de données",
                "Comportements implicites", "Outils de texte", "Portes logiques"]


# Anomalies relevees lors de la production des exercices : ajoutees en Notes du
# referentiel, sans modifier l'intitule d'origine des notions.
ALERTES = {
 5: u"⚠ VERIFIE DANS RHINO 8 LE 26/08/2026 : l'intitule est inexact. La "
    u"correspondance PAR DEFAUT de Grasshopper n'est pas la troncature sur la liste "
    u"la plus courte, mais la correspondance sur la liste la plus LONGUE, la liste "
    u"courte etant prolongee par repetition de son dernier element. Le mode "
    u"Shortest List existe mais doit etre demande explicitement par clic droit. "
    u"A corriger dans le tableau des fondamentaux V1. Cf. exercice A-24.",
}
