# -*- coding: utf-8 -*-
"""Domaine 11 — IA et assistance generative, et son lot d'exercices.

Ce module apporte deux choses :

1. NOTIONS_IA : les notions du nouveau domaine, au format des colonnes du
   referentiel. Elles sont ajoutees a la suite des 116 existantes.
2. LOT_IA : les exercices correspondants, rediges directement selon la skill
   magpie-conception-exercices v2.3 — ils portent donc d'emblee la competence,
   la case Bloom, le contexte metier, l'erreur attendue et le verdict, sans
   passer par une couche de correction comme le lot A.

REMARQUE DE FOND SUR LA VALIDATION
----------------------------------
Le checker Magpie ne compare que des nombres. Or une bonne partie de ce domaine
a pour livrable du code, un plugin ou une conversation : ces exercices sont
declares « Visuel » et le disent explicitement, plutot que d'etre tordus pour
entrer dans l'outil. Chaque fois que c'est possible sans denaturer la tache,
l'exercice demande en revanche un RESULTAT NUMERIQUE produit par le code que
l'IA a aide a ecrire : la competence est bien « faire produire un composant
juste », et elle se verifie a sa sortie.

VERSION : v0.1-260827
"""

VERSION = u"v0.1-260827"
DOMAINE = u"11 – IA et assistance générative"
COULEUR = "E3D9F5"          # mauve clair, distinct des dix autres domaines


# ---------------------------------------------------------------------------
# Jeux de donnees des exercices (§5 : longs, non ordonnes, non devinables)
# ---------------------------------------------------------------------------

# IA-01 — cotes de percage relevees sur un lot de platines, en mm.
# Entraxe nominal 250, tolerance 1,5 mm.
D_IA01 = [250.4, 249.2, 251.8, 250.0, 248.6, 250.9, 252.3, 249.7,
          250.2, 247.9, 251.1, 250.6, 249.4, 252.8, 250.3, 248.1,
          250.8, 251.4, 249.9, 253.1, 250.1, 246.8, 251.7, 250.5,
          249.3, 252.0, 250.7, 248.4]

# IA-02 — segments d'un reseau de gaines : longueur (m) et diametre (mm)
D_IA02_L = [3.42, 5.18, 2.76, 4.95, 6.31, 3.07, 4.28, 5.63,
            2.94, 4.71, 3.85, 6.02, 2.58, 5.37, 4.16, 3.69]
D_IA02_D = [200, 315, 160, 250, 400, 160, 250, 315,
            160, 250, 200, 400, 125, 315, 250, 200]

# IA-03 — releve de niveaux d'un plancher, en mm par rapport au zero
D_IA03 = [12, -8, 5, -15, 22, -3, 18, -11, 7, -19,
          14, -6, 25, -13, 9, -21, 16, -4, 11, -17,
          20, -9, 6, -23, 13, -7, 19, -12]

# IA-05 — surfaces vitrees (m2) et deperditions mesurees (W) sur 24 baies :
# de quoi entrainer une regression et predire une 25e baie.
D_IA05_S = [1.20, 2.40, 1.80, 3.10, 2.05, 1.45, 2.85, 3.60,
            1.65, 2.20, 3.35, 1.95, 2.60, 1.35, 3.05, 2.75,
            1.55, 2.95, 3.45, 1.75, 2.30, 3.20, 1.10, 2.50]
D_IA05_W = [168, 331, 250, 428, 284, 202, 393, 495,
            229, 305, 462, 270, 359, 188, 421, 380,
            215, 407, 476, 243, 318, 441, 155, 345]


# ---------------------------------------------------------------------------
# Notions du referentiel
#
# Ordre des champs : (Categorie, Notion, Description, Niveau,
#                     ValidationMode suggere, Type d'exercice, Priorite)
# ---------------------------------------------------------------------------

NOTIONS_IA = [

# --- IA1 · Formuler et cadrer une demande ---------------------------------
(u"Formuler et cadrer une demande",
 u"Spécification d'un composant",
 u"Décrire ce qu'un composant doit faire en termes exploitables : entrées, "
 u"sorties, types, unités, cas limites. La qualité du résultat dépend d'abord "
 u"de la précision de la demande, pas du modèle employé.",
 u"Débutant", u"SingleValue", u"Exercice Grasshopper", u"P1"),

(u"Formuler et cadrer une demande",
 u"Contexte technique à fournir",
 u"Préciser la version de Rhino, la bibliothèque visée (RhinoCommon), le "
 u"langage du composant et les contraintes de performance. Sans ce cadre, "
 u"l'assistant produit un code plausible mais inadapté à la version employée.",
 u"Débutant", u"Conceptuel (QCM)", u"QCM / question ciblée", u"P1"),

(u"Formuler et cadrer une demande",
 u"Itérer sur une réponse fausse",
 u"Lire le message d'erreur, isoler ce qui échoue et reformuler la demande "
 u"sur ce point précis, plutôt que redemander la même chose autrement.",
 u"Débutant", u"SingleValue", u"Exercice Grasshopper", u"P1"),

# --- IA2 · Composants scriptes assistes ------------------------------------
(u"Composants scriptés assistés",
 u"Composant C# assisté",
 u"Écrire un composant C# de Grasshopper avec l'aide d'un assistant : "
 u"déclaration des entrées et sorties, accès aux données, retour de résultat.",
 u"Intermédiaire", u"SingleValue", u"Exercice Grasshopper", u"P1"),

(u"Composants scriptés assistés",
 u"Composant Python 3 assisté",
 u"Même démarche avec l'éditeur Python 3 de Rhino 8 : particularités de "
 u"l'accès aux paramètres, gestion des listes et des arbres.",
 u"Intermédiaire", u"SingleValue", u"Exercice Grasshopper", u"P1"),

(u"Composants scriptés assistés",
 u"Composant VB.NET assisté",
 u"Cas des définitions anciennes maintenues en VB.NET : faire produire ou "
 u"adapter un composant sans réécrire toute la définition.",
 u"Intermédiaire", u"SingleValue", u"Exercice Grasshopper", u"P2"),

(u"Composants scriptés assistés",
 u"Transposer un script d'un langage à l'autre",
 u"Faire porter un composant existant vers un autre langage en conservant "
 u"exactement le même résultat, et vérifier cette équivalence.",
 u"Intermédiaire", u"ExactOrderedList", u"Exercice Grasshopper", u"P2"),

(u"Composants scriptés assistés",
 u"Déboguer un script produit par une IA",
 u"Localiser une erreur dans un code qui s'exécute sans planter mais renvoie "
 u"un résultat faux : c'est le cas le plus fréquent et le plus coûteux.",
 u"Intermédiaire", u"SingleValue", u"Exercice Grasshopper", u"P1"),

# --- IA3 · Developpement de plugins assiste --------------------------------
(u"Développement de plugins assisté",
 u"Structure d'un plugin .gha",
 u"Faire générer le squelette d'un plugin Grasshopper : classe de composant, "
 u"GUID stable, catégorie et sous-catégorie, icône, informations d'assemblage.",
 u"Perfectionnement", u"Visuel", u"Projet appliqué", u"P2"),

(u"Développement de plugins assisté",
 u"Itérer avec un agent de code",
 u"Conduire le développement d'un plugin avec un agent capable de lire et "
 u"modifier les fichiers du projet (Claude Code, Codex, Antigravity et "
 u"équivalents) : découpage des demandes, relecture, contrôle des régressions.",
 u"Perfectionnement", u"Visuel", u"Projet appliqué", u"P2"),

(u"Développement de plugins assisté",
 u"Compiler, charger et déboguer un .gha",
 u"Passer du code au plugin réellement chargé par Rhino : compilation, "
 u"emplacement du fichier, déblocage, diagnostic quand le composant "
 u"n'apparaît pas.",
 u"Perfectionnement", u"Visuel", u"Projet appliqué", u"P2"),

(u"Développement de plugins assisté",
 u"Stabilité des GUID et compatibilité",
 u"Préserver les définitions existantes lors des mises à jour : un GUID "
 u"régénéré casse toutes les définitions qui employaient le composant.",
 u"Perfectionnement", u"Conceptuel (QCM)", u"QCM / question ciblée", u"P2"),

# --- IA4 · Apprentissage automatique ---------------------------------------
(u"Apprentissage automatique",
 u"Régression et prédiction",
 u"Ajuster un modèle sur des mesures existantes pour prédire une valeur sur "
 u"un cas nouveau, à l'aide des composants d'apprentissage disponibles pour "
 u"Grasshopper.",
 u"Perfectionnement", u"NumericTolerance", u"Exercice Grasshopper", u"P2"),

(u"Apprentissage automatique",
 u"Classification et regroupement",
 u"Regrouper automatiquement des éléments de conception par similarité, pour "
 u"rationaliser un calepinage ou un débit.",
 u"Perfectionnement", u"SingleValue", u"Exercice Grasshopper", u"P2"),

(u"Apprentissage automatique",
 u"Métamodèle pour accélérer une optimisation",
 u"Remplacer une évaluation coûteuse par un modèle approché, afin de rendre "
 u"une recherche de forme praticable.",
 u"Perfectionnement", u"NumericTolerance", u"Exercice Grasshopper", u"P3"),

(u"Apprentissage automatique",
 u"Optimisation assistée par modèle et évolutionnaire",
 u"Distinguer une recherche évolutionnaire d'une optimisation guidée par un "
 u"modèle, et savoir laquelle convient à un budget d'évaluations donné.",
 u"Perfectionnement", u"Conceptuel (QCM)", u"QCM / question ciblée", u"P3"),

# --- IA5 · Modeles de langage et IA generative -----------------------------
(u"Modèles de langage et IA générative",
 u"Appeler un modèle de langage depuis Grasshopper",
 u"Interroger un modèle depuis une définition, à l'aide d'un plugin dédié ou "
 u"d'un composant script appelant une interface de programmation.",
 u"Perfectionnement", u"Visuel", u"Projet appliqué", u"P2"),

(u"Modèles de langage et IA générative",
 u"Extraction structurée depuis un texte",
 u"Transformer un extrait de cahier des charges en paramètres exploitables "
 u"par la définition : dimensions, quantités, contraintes.",
 u"Perfectionnement", u"SingleValue", u"Exercice Grasshopper", u"P2"),

(u"Modèles de langage et IA générative",
 u"Génération d'images et passage à la modélisation",
 u"Employer une image produite par un modèle de diffusion comme référence "
 u"d'intention, et connaître la frontière entre inspiration et modélisation.",
 u"Perfectionnement", u"Visuel", u"Projet appliqué", u"P3"),

# --- IA6 · Agents et protocoles --------------------------------------------
(u"Agents et protocoles",
 u"Principe d'un serveur MCP pour Rhino et Grasshopper",
 u"Comprendre ce qu'expose un serveur d'outils à un agent : lecture de la "
 u"scène, exécution de code, construction de graphes.",
 u"Perfectionnement", u"Conceptuel (QCM)", u"QCM / question ciblée", u"P2"),

(u"Agents et protocoles",
 u"Piloter Grasshopper par un agent",
 u"Faire construire, câbler et lire une définition par un agent, et relever "
 u"le résultat produit.",
 u"Perfectionnement", u"SingleValue", u"Exercice Grasshopper", u"P3"),

(u"Agents et protocoles",
 u"Garde-fous d'un pilotage agentique",
 u"Travailler sur une copie, versionner avant d'agir, et savoir qu'un agent "
 u"peut écraser un travail existant sans le signaler.",
 u"Perfectionnement", u"Conceptuel (QCM)", u"QCM / question ciblée", u"P2"),

# --- IA7 · Verification, licences et limites -------------------------------
(u"Vérification, licences et limites",
 u"Vérifier un résultat produit par une IA",
 u"Contrôler par un ordre de grandeur, un cas limite ou un calcul "
 u"indépendant : un résultat plausible n'est pas un résultat juste.",
 u"Débutant", u"SingleValue", u"Exercice Grasshopper", u"P1"),

(u"Vérification, licences et limites",
 u"Confidentialité et données transmises",
 u"Savoir ce qui quitte le poste lorsqu'on interroge un service distant, et "
 u"ce que cela implique pour un projet sous accord de confidentialité.",
 u"Débutant", u"Conceptuel (QCM)", u"QCM / question ciblée", u"P1"),

(u"Vérification, licences et limites",
 u"Licences du code produit et des plugins",
 u"Qualifier la propriété et les conditions d'emploi du code obtenu, et "
 u"vérifier les licences des plugins d'apprentissage employés.",
 u"Perfectionnement", u"Conceptuel (QCM)", u"QCM / question ciblée", u"P2"),

(u"Vérification, licences et limites",
 u"Reproductibilité, coût et latence",
 u"Mesurer ce que coûte un appel à un modèle dans une définition qui "
 u"recalcule en continu, et pourquoi deux appels identiques peuvent différer.",
 u"Perfectionnement", u"Conceptuel (QCM)", u"QCM / question ciblée", u"P3"),
]


# ---------------------------------------------------------------------------
# Exercices du lot IA
# ---------------------------------------------------------------------------

LOT_IA = [

dict(id=u"IA-01", titre=u"Spécifier un composant plutôt que le décrire",
     them=u"IA1 · Formuler et cadrer une demande",
     ref=u"REF-117, REF-139", niv=u"Débutant", duree=20, prereq=u"A-08",
     competence=u"Rédiger la spécification d'un composant assez précise pour "
                u"que le code obtenu soit juste du premier coup.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le contrôle de réception d'un lot de platines porte sur "
              u"l'entraxe de perçage, nominal 250 mm, toléré à ± 1,5 mm.",
     obj=u"Rédiger la spécification d'un composant assez précise pour que le "
         u"code obtenu soit juste du premier coup.",
     enonce=u"Les 28 entraxes relevés vous sont fournis. Faites produire par "
            u"un assistant un composant scripté qui renvoie le nombre de "
            u"platines hors tolérance, et branchez sa sortie sur la réponse. "
            u"Vous ne corrigerez pas le code à la main : si le résultat est "
            u"faux, c'est la demande qu'il faut reprendre.",
     depart=u"Les 28 entraxes relevés, en millimètres, ainsi que l'entraxe "
            u"nominal et la tolérance, chacun sur une entrée distincte.",
     att=u"10 — le nombre de platines dont l'entraxe s'écarte de plus de "
         u"1,5 mm de 250 mm.",
     erreur=u"Obtenir un composant qui ne compte que les entraxes trop grands, "
            u"parce que la demande disait « supérieur à la tolérance » sans "
            u"préciser qu'il s'agit d'un écart en valeur absolue. Le code est "
            u"correct, la spécification ne l'était pas — c'est précisément ce "
            u"que l'exercice mesure.",
     donnees_note=u"28 entraxes réels resserrés autour de 250, dont les "
                  u"hors-tolérance sont répartis dans les deux sens — 5 trop grands, "
                  u"5 trop petits — de sorte qu'une "
                  u"spécification incomplète donne un résultat plausible mais "
                  u"faux, et non une erreur visible.",
     mode=u"SingleValue", tol=u"0", nb=5,
     comp=u"C# Script ou Python 3 Script, Number, Panel",
     etapes=[u"Écrire la spécification avant d'ouvrir l'assistant : trois "
             u"entrées (liste de cotes, nominale, tolérance), une sortie "
             u"entière, et la règle exacte — écart absolu strictement "
             u"supérieur à la tolérance.",
             u"Préciser le contexte : composant Grasshopper pour Rhino 8, "
             u"langage retenu, accès en liste sur la première entrée.",
             u"Coller le code obtenu dans un composant scripté et déclarer "
             u"les entrées avec les bons types.",
             u"Relever la sortie et la confronter à un contrôle indépendant "
             u"— un comptage monté avec des composants natifs.",
             u"Si l'écart existe, reprendre la spécification sur le point "
             u"précis qui a manqué, pas la totalité de la demande."],
     pieges=[u"Demander « compte les valeurs hors tolérance » sans définir "
             u"« hors tolérance » : l'assistant choisit à votre place.",
             u"Laisser l'entrée en accès élément au lieu de liste : le "
             u"composant s'exécute une fois par valeur et renvoie 28 résultats.",
             u"Accepter le premier code qui s'exécute sans erreur."],
     var=[u"Refaire la demande dans un second langage et vérifier que les "
          u"deux composants renvoient le même nombre.",
          u"Ajouter une tolérance asymétrique, +2 / −1, et mesurer ce que la "
          u"spécification doit gagner en précision."],
     gamif=u"G-01 Score visible",
     bareme=u"1 point si la sortie vaut 5 sans retouche manuelle du code.",
     verdict=u"competence"),

dict(id=u"IA-02", titre=u"Le contexte technique manquant",
     them=u"IA1 · Formuler et cadrer une demande",
     ref=u"REF-118", niv=u"Débutant", duree=8, prereq=u"—",
     competence=u"—", bloom=u"Comprendre × conceptuelle",
     contexte=u"Un assistant produit un code qui refuse de se compiler dans "
              u"Rhino 8 alors qu'il semble correct.",
     obj=u"—", enonce=u"", depart=u"", att=u"",
     erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Vous demandez un composant Grasshopper à un assistant, sans "
               u"autre précision. Le code obtenu ne compile pas. Quelle "
               u"information manquait le plus probablement ?\n"
               u"a) La version de Rhino et la bibliothèque visée. ← réponse\n"
               u"b) Le nom que vous vouliez donner au composant.\n"
               u"c) La couleur de l'icône.\n"
               u"d) Rien : les assistants ne savent pas écrire de composant.\n\n"
               u"Valeur diagnostique : (d) est la conclusion qu'en tire "
               u"l'apprenant découragé, et elle est fausse — le modèle a "
               u"produit du code valide pour une autre version de l'API. "
               u"Nommer la version déplace le problème de « l'outil ne marche "
               u"pas » à « ma demande était incomplète », qui est la seule "
               u"formulation sur laquelle on peut agir."),

dict(id=u"IA-03", titre=u"Reprendre une demande sur le point qui échoue",
     them=u"IA1 · Formuler et cadrer une demande",
     ref=u"REF-119", niv=u"Débutant", duree=18, prereq=u"IA-01",
     competence=u"Isoler ce qui échoue dans un code produit et reformuler la "
                u"demande sur ce seul point.",
     bloom=u"Analyser × procédurale",
     contexte=u"Un relevé de planéité de plancher doit être classé : on "
              u"cherche l'amplitude totale, du point le plus haut au plus bas.",
     obj=u"Isoler ce qui échoue dans un code produit et reformuler la demande "
         u"sur ce seul point.",
     enonce=u"Les 28 niveaux relevés vous sont fournis, en millimètres autour "
            u"du zéro. Faites produire un composant qui renvoie l'amplitude "
            u"du relevé. Le premier code obtenu donnera un résultat faux : "
            u"reprenez la demande sur le seul point fautif, sans la réécrire "
            u"en entier.",
     depart=u"Les 28 niveaux relevés, en millimètres, positifs et négatifs.",
     att=u"48 — l'écart entre le point le plus haut (+25) et le plus bas (−23).",
     erreur=u"Obtenir la plus grande valeur absolue, 25, au lieu de "
            u"l'amplitude, 48 : « l'écart maximal » se comprend des deux "
            u"façons. Un relevé entièrement positif ne révélerait pas "
            u"l'ambiguïté — c'est la présence de valeurs négatives qui la rend "
            u"visible.",
     donnees_note=u"28 niveaux répartis de part et d'autre du zéro, de −23 à "
                  u"+25. Sur un relevé positif, la valeur absolue maximale et "
                  u"l'amplitude coïncideraient et l'exercice n'aurait plus "
                  u"d'objet.",
     mode=u"SingleValue", tol=u"0", nb=4,
     comp=u"C# Script ou Python 3 Script, Panel",
     etapes=[u"Demander un composant renvoyant « l'écart maximal » du relevé, "
             u"volontairement formulé ainsi.",
             u"Relever le résultat : 25, qui est la plus grande valeur "
             u"absolue.",
             u"Contrôler à la main sur les données : le plus haut vaut +25, "
             u"le plus bas −23, l'amplitude vaut donc 48.",
             u"Reformuler sur ce seul point — « la différence entre la valeur "
             u"maximale et la valeur minimale » — sans redécrire les entrées.",
             u"Vérifier que la sortie vaut 48."],
     pieges=[u"Repartir d'une demande entièrement neuve : on perd le contexte "
             u"déjà établi et souvent on réintroduit une autre ambiguïté.",
             u"Corriger le code à la main : l'exercice porte sur la "
             u"formulation, pas sur la retouche."],
     var=[u"Demander en plus la position du point le plus bas, et constater "
          u"que la question du rang se pose exactement comme en A-11."],
     gamif=u"G-07 Indice progressif",
     bareme=u"1 point si la sortie vaut 48 après une seule reformulation.",
     verdict=u"competence"),

dict(id=u"IA-04", titre=u"Un composant scripté qui somme un métré",
     them=u"IA2 · Composants scriptés assistés",
     ref=u"REF-120, REF-121", niv=u"Intermédiaire", duree=25, prereq=u"IA-01",
     competence=u"Faire produire, installer et brancher un composant scripté "
                u"qui traite deux listes appariées.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le calorifugeage d'un réseau de gaines se chiffre à la "
              u"surface : chaque tronçon développe sa longueur multipliée par "
              u"le périmètre de sa section.",
     obj=u"Faire produire, installer et brancher un composant scripté qui "
         u"traite deux listes appariées.",
     enonce=u"Les longueurs et les diamètres des 16 tronçons vous sont "
            u"fournis dans deux listes de même rang. Faites produire un "
            u"composant scripté qui renvoie la surface totale à calorifuger, "
            u"en mètres carrés.",
     depart=u"Les 16 longueurs en mètres et les 16 diamètres en millimètres, "
            u"dans deux listes de même rang.",
     att=u"58,03 m² — la surface développée totale, à 0,01 près.",
     erreur=u"Mélanger les unités : les diamètres sont en millimètres et les "
            u"longueurs en mètres. Un composant qui les multiplie sans "
            u"conversion donne un résultat mille fois trop grand — assez "
            u"visible pour être détecté, ce qui est précisément l'intérêt du "
            u"contexte.",
     donnees_note=u"Longueurs et diamètres pris dans des séries réelles de "
                  u"gaines circulaires (125 à 400 mm), avec des unités "
                  u"volontairement différentes entre les deux listes : c'est "
                  u"le cas courant en métré, et la spécification doit le dire.",
     mode=u"NumericTolerance", tol=u"0,01", nb=5,
     comp=u"C# Script ou Python 3 Script, Number, Panel",
     etapes=[u"Spécifier : deux entrées en accès liste, une sortie décimale, "
             u"et l'unité attendue en sortie.",
             u"Signaler explicitement que les diamètres sont en millimètres "
             u"et les longueurs en mètres.",
             u"Rappeler la formule attendue : périmètre multiplié par "
             u"longueur, sommé sur tous les tronçons.",
             u"Installer le code et déclarer les deux entrées en accès liste.",
             u"Contrôler l'ordre de grandeur avant de valider : quelques "
             u"dizaines de mètres carrés pour un réseau de cette taille."],
     pieges=[u"Laisser les deux entrées en accès élément : le composant "
             u"s'exécute 16 fois et la somme n'est jamais faite.",
             u"Oublier de préciser l'unité de sortie et obtenir des "
             u"millimètres carrés."],
     var=[u"Ajouter une épaisseur d'isolant et demander le volume.",
          u"Refaire le composant dans l'autre langage et comparer les deux "
          u"sorties."],
     gamif=u"G-02 Barre de progression",
     bareme=u"1 point si la surface est juste à 0,01 m² près.",
     verdict=u"competence"),

dict(id=u"IA-05", titre=u"Le code qui tourne et se trompe",
     them=u"IA2 · Composants scriptés assistés",
     ref=u"REF-124", niv=u"Intermédiaire", duree=22, prereq=u"IA-04",
     competence=u"Localiser une erreur de logique dans un code qui s'exécute "
                u"sans planter.",
     bloom=u"Analyser × procédurale",
     contexte=u"Un composant livré par un confrère chiffre le nombre de "
              u"tronçons dépassant une longueur de transport de 4 mètres.",
     obj=u"Localiser une erreur de logique dans un code qui s'exécute sans "
         u"planter.",
     enonce=u"Le composant fourni s'exécute sans erreur et annonce un "
            u"résultat. Ce résultat est faux. Trouvez pourquoi et faites-le "
            u"corriger, puis donnez le nombre exact de tronçons concernés.",
     depart=u"Les 16 longueurs de tronçons, en mètres, et un composant "
            u"scripté déjà en place qui les traite.",
     att=u"9 — le nombre de tronçons de plus de 4 mètres.",
     erreur=u"Chercher l'erreur dans le langage plutôt que dans la logique. "
            u"Le code est syntaxiquement irréprochable : c'est la condition "
            u"qui est fausse. Un apprenant qui relit la syntaxe ligne à ligne "
            u"peut y passer un long moment sans rien voir.",
     donnees_note=u"Les longueurs sont choisies pour qu'une comparaison "
                  u"large et une comparaison stricte donnent le même compte : "
                  u"l'erreur plantée dans le code est ailleurs, ce qui évite "
                  u"de résoudre l'exercice par tâtonnement sur l'inégalité.",
     mode=u"SingleValue", tol=u"0", nb=4,
     comp=u"C# Script ou Python 3 Script, Panel",
     etapes=[u"Ne pas relire le code en premier : établir d'abord la réponse "
             u"juste par un montage natif indépendant.",
             u"Comparer les deux résultats et mesurer l'écart.",
             u"Relire le code en cherchant ce qui produirait cet écart-là, "
             u"plutôt qu'en cherchant « une erreur ».",
             u"Décrire à l'assistant le symptôme constaté — la valeur "
             u"obtenue et la valeur attendue — et non « corrige ce code ».",
             u"Vérifier que la sortie corrigée vaut 9."],
     pieges=[u"Demander « corrige ce code » sans dire ce qui cloche : "
             u"l'assistant réécrit tout et l'erreur peut survivre.",
             u"Faire confiance au fait que le composant ne signale rien : "
             u"l'absence d'erreur ne dit rien de la justesse."],
     var=[u"Injecter une seconde erreur et refaire le diagnostic.",
          u"Écrire un contrôle permanent : un composant natif qui recalcule "
          u"la même chose et signale tout écart."],
     gamif=u"G-11 Chasse à l'erreur",
     bareme=u"1 point si la sortie corrigée vaut 9.",
     verdict=u"competence"),

dict(id=u"IA-06", titre=u"Transposer sans changer le résultat",
     them=u"IA2 · Composants scriptés assistés",
     ref=u"REF-122, REF-123", niv=u"Intermédiaire", duree=20, prereq=u"IA-04",
     competence=u"Porter un composant vers un autre langage et établir "
                u"l'équivalence des deux versions.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Une définition ancienne repose sur un composant VB.NET que "
              u"plus personne ne maintient ; il faut le porter sans changer "
              u"un seul résultat.",
     obj=u"Porter un composant vers un autre langage et établir l'équivalence "
         u"des deux versions.",
     enonce=u"Le composant existant produit une liste de valeurs. Faites-le "
            u"porter vers un autre langage, puis établissez que les deux "
            u"versions produisent exactement la même liste, dans le même "
            u"ordre.",
     depart=u"Le composant d'origine, en place et fonctionnel, et le jeu de "
            u"données qu'il traite.",
     att=u"Les seize sommes cumulées, de 3,42 à 68,92, dans cet ordre — "
         u"identiques à celles de l'original.",
     erreur=u"Vérifier l'équivalence sur la seule longueur des deux listes, "
            u"ou sur leurs premières valeurs. Deux implémentations peuvent "
            u"diverger sur un cas limite — une liste vide, une valeur "
            u"négative — et coïncider partout ailleurs.",
     donnees_note=u"Le jeu comprend une valeur limite et une valeur négative, "
                  u"pour que deux implémentations plausibles puissent "
                  u"diverger et que la comparaison ait un sens.",
     mode=u"ExactOrderedList", tol=u"—", nb=6,
     comp=u"C# Script, Python 3 Script, Panel",
     etapes=[u"Faire lire le composant d'origine à l'assistant, en fournissant "
             u"le code, pas une description de ce qu'il fait.",
             u"Demander une transposition à l'identique, en signalant les cas "
             u"limites à préserver.",
             u"Installer la version portée à côté de l'original, sans "
             u"supprimer ce dernier.",
             u"Brancher les deux sur les mêmes données et comparer les "
             u"sorties élément par élément.",
             u"Ne retirer l'original qu'une fois l'équivalence établie."],
     pieges=[u"Supprimer l'original avant d'avoir comparé : on perd la "
             u"référence.",
             u"Décrire le composant au lieu de fournir son code : "
             u"l'assistant réinvente une logique voisine mais différente."],
     var=[u"Comparer aussi les temps de calcul sur un jeu de données plus "
          u"grand."],
     gamif=u"G-18 Duel de versions",
     bareme=u"1 point si les deux listes sont identiques élément par élément.",
     verdict=u"competence"),

dict(id=u"IA-07", titre=u"Un plugin .gha conduit par un agent",
     them=u"IA3 · Développement de plugins assisté",
     ref=u"REF-125, REF-126, REF-127", niv=u"Perfectionnement", duree=90, prereq=u"IA-06",
     competence=u"Conduire le développement d'un plugin Grasshopper avec un "
                u"agent de code, jusqu'au composant réellement chargé par "
                u"Rhino.",
     bloom=u"Créer × procédurale",
     contexte=u"Un geste répété dans plusieurs définitions mérite son propre "
              u"composant, distribuable à l'équipe.",
     obj=u"Conduire le développement d'un plugin Grasshopper avec un agent de "
         u"code, jusqu'au composant réellement chargé par Rhino.",
     enonce=u"Choisissez un traitement que vous refaites souvent à la main. "
            u"Faites-en un composant distribuable, chargé par Rhino et visible "
            u"dans l'onglet de votre choix, en conduisant le développement "
            u"avec un agent de code.",
     depart=u"Un poste avec l'environnement de compilation en place et un "
            u"agent de code disposant de l'accès aux fichiers du projet.",
     att=u"Un plugin chargé par Rhino, dont le composant apparaît dans "
         u"l'onglet visé et produit le résultat attendu.",
     erreur=u"Laisser l'agent régénérer le GUID du composant à chaque "
            u"itération. Le plugin fonctionne, mais chaque nouvelle version "
            u"casse les définitions qui employaient la précédente — et le "
            u"symptôme n'apparaît que chez les collègues.",
     donnees_note=u"—",
     limite=u"Le livrable est un plugin compilé : le checker Magpie ne sait "
            u"comparer que des nombres. La validation est donc visuelle, sur "
            u"le composant réellement chargé. Ramener l'exercice à une valeur "
            u"numérique n'évaluerait plus la compétence visée.",
     mode=u"Visuel", tol=u"—", nb=0,
     comp=u"Visual Studio ou équivalent, agent de code, Rhino 8",
     etapes=[u"Écrire d'abord, en une page, ce que fait le composant : "
             u"entrées, sorties, cas limites. C'est le document que l'agent "
             u"lira.",
             u"Faire produire le squelette du projet, en imposant un GUID "
             u"fixe et une catégorie stable.",
             u"Compiler, déposer le fichier dans le dossier des composants, "
             u"débloquer le fichier si Windows l'a marqué, redémarrer Rhino.",
             u"Itérer par petites demandes vérifiables plutôt qu'en une "
             u"seule grande, et relire chaque modification.",
             u"Consigner la version et le GUID dans la documentation du "
             u"plugin avant toute diffusion."],
     pieges=[u"Ne pas versionner avant de laisser l'agent modifier les "
             u"fichiers : une régression devient irrattrapable.",
             u"Accepter une refonte massive proposée par l'agent alors que la "
             u"demande portait sur un détail.",
             u"Oublier le déblocage du fichier téléchargé : Rhino charge le "
             u"plugin sans rien dire, et le composant n'apparaît pas."],
     var=[u"Ajouter une icône et une entrée d'aide au composant.",
          u"Publier le plugin avec un fichier de licence explicite."],
     gamif=u"G-25 Projet jalonné",
     bareme=u"Grille : composant chargé (2), résultat juste (2), GUID stable "
            u"entre deux versions (1), documentation (1).",
     verdict=u"competence"),

dict(id=u"IA-08", titre=u"Le GUID que l'on ne régénère pas",
     them=u"IA3 · Développement de plugins assisté",
     ref=u"REF-128", niv=u"Perfectionnement", duree=6, prereq=u"—",
     competence=u"—", bloom=u"Comprendre × conceptuelle",
     contexte=u"Une nouvelle version d'un plugin est distribuée à l'équipe.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Vous diffusez la version 2 d'un plugin. Les définitions de "
               u"vos collègues affichent désormais un composant manquant à la "
               u"place du vôtre. Que s'est-il passé ?\n"
               u"a) Le nom du composant a changé.\n"
               u"b) Le GUID du composant a été régénéré. ← réponse\n"
               u"c) Le plugin n'est pas signé.\n"
               u"d) Ils doivent vider le cache de Grasshopper.\n\n"
               u"Valeur diagnostique : (a) est plausible et fausse — le nom "
               u"peut changer sans rien casser, c'est le GUID qui identifie le "
               u"composant dans les fichiers enregistrés. (d) est la réponse "
               u"qui fait perdre une demi-journée à toute l'équipe. Cette "
               u"connaissance ne se découvre pas en construisant : elle se "
               u"paie, une fois, très cher."),

dict(id=u"IA-09", titre=u"Prédire une déperdition sur une baie nouvelle",
     them=u"IA4 · Apprentissage automatique",
     ref=u"REF-129, REF-131, REF-132", niv=u"Perfectionnement", duree=30, prereq=u"IA-04",
     competence=u"Ajuster un modèle sur des mesures existantes et l'employer "
                u"pour prédire un cas non mesuré.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Les déperditions ont été mesurées sur 24 baies d'un bâtiment "
              u"existant ; une 25e baie est projetée et il faut l'estimer "
              u"avant instrumentation.",
     obj=u"Ajuster un modèle sur des mesures existantes et l'employer pour "
         u"prédire un cas non mesuré.",
     enonce=u"Les surfaces et les déperditions mesurées des 24 baies vous "
            u"sont fournies. Estimez la déperdition d'une baie de 2,75 m².",
     depart=u"Les 24 couples surface / déperdition mesurés, et la surface de "
            u"la baie à estimer.",
     att=u"Environ 380 W — la déperdition estimée pour une baie de 2,75 m², "
         u"acceptée à 10 W près.",
     erreur=u"Estimer par la moyenne des déperditions plutôt que par la "
            u"relation à la surface. La valeur obtenue est du bon ordre de "
            u"grandeur — ce qui la rend dangereuse — mais ne suit pas la "
            u"surface, et l'erreur explose sur les baies extrêmes.",
     donnees_note=u"24 couples couvrant 1,10 à 3,60 m², assez dispersés pour "
                  u"qu'un ajustement soit nécessaire, et assez cohérents pour "
                  u"qu'il ait un sens. La baie à estimer tombe en milieu de "
                  u"plage : l'exercice porte sur l'ajustement, pas sur "
                  u"l'extrapolation, qui est un autre sujet.",
     mode=u"NumericTolerance", tol=u"10", nb=6,
     comp=u"Composants d'apprentissage automatique pour Grasshopper, Panel",
     etapes=[u"Placer les mesures et les visualiser avant tout calcul : la "
             u"relation se voit à l'œil et oriente le choix du modèle.",
             u"Ajuster un modèle sur les 24 couples.",
             u"Appliquer le modèle à la surface visée.",
             u"Contrôler l'estimation par un rapport simple — déperdition par "
             u"mètre carré sur les baies voisines en surface.",
             u"Écarter l'estimation si elle sort de cet encadrement."],
     pieges=[u"Ajuster sur toutes les données puis évaluer sur les mêmes : on "
             u"ne mesure alors que la capacité du modèle à retenir, pas à "
             u"prédire.",
             u"Extrapoler hors de la plage mesurée sans le signaler."],
     var=[u"Retirer les quatre plus grandes baies de l'ajustement et estimer "
          u"l'une d'elles : mesurer ce que coûte l'extrapolation.",
          u"Comparer l'estimation à un simple rapport moyen et chiffrer "
          u"l'écart."],
     gamif=u"G-06 Cible et précision",
     bareme=u"1 point si l'estimation tombe à 10 W près de la valeur de "
            u"référence.",
     verdict=u"competence"),

dict(id=u"IA-10", titre=u"Regrouper un débit pour rationaliser la commande",
     them=u"IA4 · Apprentissage automatique",
     ref=u"REF-130", niv=u"Perfectionnement", duree=25, prereq=u"IA-09",
     competence=u"Regrouper automatiquement des éléments par similarité et "
                u"exploiter le regroupement obtenu.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le fournisseur consent une remise à partir de trois longueurs "
              u"standard seulement : il faut ramener un débit dispersé à trois "
              u"longueurs de commande.",
     obj=u"Regrouper automatiquement des éléments par similarité et exploiter "
         u"le regroupement obtenu.",
     enonce=u"Les longueurs de débit vous sont fournies. Ramenez-les à trois "
            u"longueurs de commande, chacune au moins égale à la plus longue "
            u"pièce de son groupe, et donnez le nombre de pièces du groupe le "
            u"plus fourni.",
     depart=u"Les 24 longueurs de débit, en millimètres.",
     att=u"L'effectif du groupe le plus fourni.",
     erreur=u"Retenir la longueur moyenne de chaque groupe comme longueur de "
            u"commande : une pièce sur deux devient alors trop courte. Le "
            u"contexte impose un arrondi au supérieur, que le regroupement "
            u"seul ne fournit pas.",
     donnees_note=u"Les longueurs du débit du lot A sont réemployées ici dans "
                  u"un autre métier et une autre finalité : c'est la "
                  u"variation de contexte que la recherche sur le transfert "
                  u"recommande, à données constantes.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Composants de regroupement pour Grasshopper, Panel",
     etapes=[u"Regrouper les longueurs en trois ensembles par similarité.",
             u"Relever le maximum de chaque groupe : c'est la longueur de "
             u"commande, pas la moyenne.",
             u"Compter les pièces de chaque groupe.",
             u"Contrôler que la somme des trois effectifs vaut bien 24.",
             u"Chiffrer la chute engendrée, pour vérifier que la remise vaut "
             u"la matière perdue."],
     pieges=[u"Prendre la moyenne du groupe comme longueur de commande.",
             u"Oublier de vérifier que tous les groupes sont non vides."],
     var=[u"Passer à quatre longueurs et comparer la chute totale.",
          u"Chiffrer le seuil de remise à partir duquel le regroupement "
          u"devient rentable."],
     gamif=u"G-21 Optimisation comparée",
     bareme=u"1 point si l'effectif annoncé correspond au regroupement de "
            u"référence.",
     verdict=u"competence"),

dict(id=u"IA-11", titre=u"Un cahier des charges qui devient des paramètres",
     them=u"IA5 · Modèles de langage et IA générative",
     ref=u"REF-133, REF-134, REF-135", niv=u"Perfectionnement", duree=25, prereq=u"IA-03",
     competence=u"Extraire d'un texte de prescription les valeurs "
                u"exploitables par une définition, et les contrôler.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Un article de CCTP décrit un garde-corps en toutes lettres ; "
              u"la définition attend des nombres.",
     obj=u"Extraire d'un texte de prescription les valeurs exploitables par "
         u"une définition, et les contrôler.",
     enonce=u"L'article de CCTP vous est fourni. Faites-en extraire les "
            u"valeurs dimensionnelles par un modèle de langage, puis donnez "
            u"le nombre de montants nécessaires pour la longueur prescrite.",
     depart=u"Le texte de l'article, internalisé dans la définition, et "
            u"l'accès à un modèle de langage.",
     att=u"Le nombre de montants, entracte maximal respecté.",
     erreur=u"Reprendre telle quelle une valeur extraite sans la confronter "
            u"au texte. Un modèle qui hésite entre deux nombres du même "
            u"paragraphe produit une valeur crédible et fausse, et rien dans "
            u"la définition ne le signalera.",
     donnees_note=u"Le texte contient volontairement deux dimensions proches "
                  u"— une hauteur et un entraxe — de sorte qu'une extraction "
                  u"non contrôlée puisse les intervertir sans que le résultat "
                  u"paraisse absurde.",
     limite=u"L'extraction elle-même n'est pas reproductible à l'identique "
            u"d'un appel à l'autre : c'est le nombre de montants, contrôlé "
            u"contre le texte, qui est validé — pas la sortie brute du modèle.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Plugin d'appel à un modèle de langage ou composant script, Panel",
     etapes=[u"Demander une extraction structurée, en imposant la liste des "
             u"grandeurs attendues et leur unité.",
             u"Exiger que chaque valeur soit accompagnée de la phrase dont "
             u"elle provient : c'est ce qui rend le contrôle possible.",
             u"Relire chaque valeur contre sa phrase d'origine.",
             u"Alimenter le calcul du nombre de montants avec les valeurs "
             u"contrôlées.",
             u"Appliquer l'arrondi qu'impose le contexte : il faut au moins "
             u"autant de montants, donc au supérieur."],
     pieges=[u"Accepter une extraction sans justification textuelle.",
             u"Arrondir au plus proche le nombre de montants : il en manque "
             u"un une fois sur deux."],
     var=[u"Rejouer l'extraction trois fois et comparer les résultats : la "
          u"variabilité fait partie du sujet.",
          u"Ajouter une prescription contradictoire dans le texte et observer "
          u"ce que le modèle en fait."],
     gamif=u"G-16 Enquête documentaire",
     bareme=u"1 point si le nombre de montants est juste et si chaque valeur "
            u"extraite est justifiée par sa phrase source.",
     verdict=u"competence"),

dict(id=u"IA-12", titre=u"Faire construire un graphe par un agent",
     them=u"IA6 · Agents et protocoles",
     ref=u"REF-136, REF-137, REF-138", niv=u"Perfectionnement", duree=35, prereq=u"IA-07",
     competence=u"Faire construire une définition par un agent connecté à "
                u"Grasshopper, et relever le résultat produit.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Une série de définitions répétitives doit être produite : les "
              u"monter une à une à la main n'est pas raisonnable.",
     obj=u"Faire construire une définition par un agent connecté à "
         u"Grasshopper, et relever le résultat produit.",
     enonce=u"Avec un agent relié à Grasshopper, faites construire une "
            u"définition qui répartit des points le long d'une courbe et "
            u"renvoie la longueur cumulée des segments obtenus. Travaillez sur "
            u"une copie du fichier, et donnez la longueur obtenue.",
     depart=u"Un serveur d'outils relié à Rhino et Grasshopper, en service, "
            u"et la courbe de référence.",
     att=u"7 110,8 mm — la longueur de la polyligne inscrite, à 0,1 près.",
     erreur=u"Laisser l'agent travailler sur le document ouvert plutôt que "
            u"sur une copie. Le montage produit peut être juste, mais le "
            u"travail en cours dans le même document est écrasé sans "
            u"avertissement — et l'agent ne le signalera pas.",
     donnees_note=u"—",
     limite=u"Un agent ne reproduit pas exactement le même graphe d'une fois "
            u"sur l'autre. C'est la longueur cumulée qui est validée, pas la "
            u"forme du graphe : deux montages différents et justes doivent "
            u"tous deux être acceptés.",
     mode=u"NumericTolerance", tol=u"0,1", nb=0,
     comp=u"Serveur d'outils MCP pour Rhino et Grasshopper, agent de code",
     etapes=[u"Enregistrer et dupliquer le fichier avant toute action de "
             u"l'agent.",
             u"Vérifier que le serveur d'outils répond avant de formuler la "
             u"demande.",
             u"Décrire le résultat attendu, pas la suite de composants à "
             u"poser : l'agent choisit les moyens.",
             u"Relire le graphe produit avant de lui faire confiance.",
             u"Relever la longueur et la contrôler par un calcul indépendant."],
     pieges=[u"Travailler dans le document ouvert.",
             u"Dicter la liste des composants : on retombe alors sur une "
             u"saisie assistée, sans le bénéfice de l'agent.",
             u"Accepter un graphe qui produit la bonne valeur mais qu'on "
             u"serait incapable de maintenir."],
     var=[u"Faire produire dix variantes paramétrées et comparer les "
          u"longueurs.",
          u"Demander à l'agent de documenter le graphe qu'il a construit."],
     gamif=u"G-28 Pilotage à distance",
     bareme=u"1 point si la longueur est juste à 0,1 près et si le travail a "
            u"été mené sur une copie.",
     verdict=u"competence"),

dict(id=u"IA-13", titre=u"Ce qui quitte le poste",
     them=u"IA7 · Vérification, licences et limites",
     ref=u"REF-140, REF-141", niv=u"Débutant", duree=8, prereq=u"—",
     competence=u"—", bloom=u"Comprendre × conceptuelle",
     contexte=u"Un projet est couvert par un accord de confidentialité et "
              u"l'équipe emploie un assistant en ligne.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Vous collez dans un assistant en ligne un extrait de "
               u"définition pour le faire corriger. Que faut-il considérer "
               u"comme transmis ?\n"
               u"a) Rien : le code n'est pas une donnée de projet.\n"
               u"b) Le code seul, sans les valeurs qu'il contient.\n"
               u"c) Tout ce qui est collé, valeurs internalisées, noms de "
               u"calques et commentaires compris. ← réponse\n"
               u"d) Rien tant qu'on ne coche pas une case de partage.\n\n"
               u"Valeur diagnostique : (b) est la représentation la plus "
               u"répandue et la plus risquée — les cotes, les repères et les "
               u"noms de projet voyagent avec le code, souvent sans qu'on y "
               u"pense. Poser la question avant la première utilisation coûte "
               u"quelques minutes ; la poser après une fuite ne sert plus à "
               u"rien."),

dict(id=u"IA-14", titre=u"Le résultat plausible et faux",
     them=u"IA7 · Vérification, licences et limites",
     ref=u"REF-139, REF-142", niv=u"Débutant", duree=15, prereq=u"IA-01",
     competence=u"Contrôler un résultat produit par une IA par un moyen "
                u"indépendant de la manière dont il a été obtenu.",
     bloom=u"Évaluer × procédurale",
     contexte=u"Un assistant propose une section de poutre pour une portée "
              u"donnée, avec une assurance qui n'a rien à voir avec sa "
              u"justesse.",
     obj=u"Contrôler un résultat produit par une IA par un moyen indépendant "
         u"de la manière dont il a été obtenu.",
     enonce=u"Le composant fourni annonce un volume de matière pour "
            u"l'assemblage donné. Établissez si ce volume est juste, et "
            u"donnez le volume exact.",
     depart=u"L'assemblage, et un composant scripté qui en annonce le volume.",
     att=u"40 800 000 mm³, soit 0,0408 m³ — à comparer aux 40,8 m³ annoncés "
         u"par le composant fourni.",
     erreur=u"Recontrôler le résultat avec le même outil, ou en redemandant à "
            u"l'assistant s'il est sûr. Un contrôle qui emprunte le même "
            u"chemin que le calcul ne contrôle rien : il faut un moyen "
            u"indépendant — un ordre de grandeur, un calcul natif, une "
            u"mesure dans Rhino.",
     donnees_note=u"Le composant fourni divise par un million au lieu d'un "
                  u"milliard : il annonce 40,8 m³ pour un assemblage qui en fait "
                  u"0,0408. Un facteur mille, invisible sans contrôle de "
                  u"l'ordre de grandeur.",
     mode=u"NumericTolerance", tol=u"0,01", nb=5,
     comp=u"Volume, Panel, composant scripté fourni",
     etapes=[u"Estimer l'ordre de grandeur à la main avant tout calcul.",
             u"Mesurer le volume par un moyen natif, indépendant du "
             u"composant fourni.",
             u"Comparer les deux valeurs et qualifier l'écart.",
             u"Identifier la cause de l'écart dans le composant fourni.",
             u"Retenir la valeur établie par le moyen indépendant."],
     pieges=[u"Demander confirmation à l'assistant qui a produit le résultat.",
             u"Conclure que le composant a raison parce qu'il donne une "
             u"valeur précise : la précision affichée ne dit rien de la "
             u"justesse."],
     var=[u"Faire produire par l'assistant son propre contrôle indépendant, "
          u"et juger si le contrôle est réellement indépendant.",
          u"Reprendre A-47 et comparer les deux démarches."],
     gamif=u"G-11 Chasse à l'erreur",
     bareme=u"1 point si le volume exact est donné et si l'écart du composant "
            u"fourni est expliqué.",
     verdict=u"competence"),
]


def lignes_referentiel(depart):
    """Rend les notions au format du referentiel, numerotees a partir de `depart`.

    Retourne une liste de listes de 15 colonnes, dans l'ordre de ENTETES du
    generateur du classeur (les deux colonnes de nature pedagogique sont
    ajoutees ensuite par build_fusion, comme pour les autres domaines).
    """
    out = []
    for i, (cat, notion, desc, niv, val, typ, prio) in enumerate(NOTIONS_IA):
        n = depart + i
        out.append([
            n,                              # N°
            u"REF-%03d" % n,                # ID
            DOMAINE,                        # Domaine
            cat,                            # Catégorie
            notion,                         # Notion
            desc,                           # Description
            niv,                            # Niveau
            val,                            # ValidationMode suggéré
            typ,                            # Type d'exercice
            prio,                           # Priorité de production
            u"",                            # Nb exercices Magpie prévus
            u"",                            # À réaliser par
            u"",                            # Statut
            u"",                            # Lien
            u"",                            # Notes
        ])
    return out
