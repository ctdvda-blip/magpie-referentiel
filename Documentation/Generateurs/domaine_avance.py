# -*- coding: utf-8 -*-
"""Domaines 2, 6, 7, 8 et 9 — plugins, methode, algorithmique, developpement, web.

Cinq lots pour les 33 notions restantes :

    PL  ecosysteme de plugins et principes de la conception parametrique
    MP  methode, organisation, performance et evenements
    AV  algorithmique avancee : boucles, simulation, design generatif
    DV  developpement, scripting et API
    WB  interfaces, publication web et interoperabilite

PARTI PRIS
----------
C'est le bloc ou la skill elimine le plus. Installer un plugin, connaitre
l'outil qui fait telle chose, savoir ce qu'est Rhino.Compute : ce sont des
CONNAISSANCES. Les monter en exercice mesurerait la memoire, pas la pratique.
Elles deviennent donc des questions charnieres, dont chaque mauvaise reponse
dit quelque chose d'utile au formateur.

Restent quelques vraies competences, et elles sont chiffrables : une boucle
converge sur une valeur, une simulation se stabilise sur une longueur, une
recherche de forme rend un optimum, un script rend un nombre.

VERSION : v0.1-260828
"""

VERSION = u"v0.1-260828"


# ---------------------------------------------------------------------------
# Jeux de donnees
# ---------------------------------------------------------------------------

# MP-02 — releve de temps de recalcul, en millisecondes, avant optimisation
D_MP02 = [1840, 12, 8, 26, 15, 9, 2260, 11, 7, 19,
          14, 6, 22, 13, 10, 2150, 9, 8, 17, 12]

# AV-01 — suite convergente : cotes successives d'un ajustement par bissection
D_AV01_CIBLE = 2450.0     # portee visee, en mm
D_AV01_DEBUT = (1000.0, 4000.0)


LOT_PL = [

dict(id=u"PL-01", titre=u"Ce qui change quand on passe au paramétrique",
     them=u"PL1 · Principes",
     ref=u"REF-025",
     niv=u"Débutant", duree=8, prereq=u"—",
     competence=u"—", bloom=u"Comprendre × conceptuelle",
     contexte=u"Un client demande de reprendre une façade déjà modélisée en "
              u"changeant la trame.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Qu'est-ce qu'une définition paramétrique apporte qu'un "
               u"modèle dessiné n'apporte pas ?\n"
               u"a) Elle va plus vite à produire la première fois.\n"
               u"b) Elle rend la modification bon marché : on change une "
               u"valeur, tout suit. ← réponse\n"
               u"c) Elle donne un modèle plus précis.\n"
               u"d) Elle évite d'avoir à connaître Rhino.\n\n"
               u"Valeur diagnostique : (a) est faux et c'est important de le "
               u"dire — une définition coûte presque toujours plus cher que "
               u"le dessin équivalent, la première fois. Croire le contraire "
               u"mène à en faire pour des cas uniques, où elle ne se "
               u"rentabilise jamais. Le paramétrique s'amortit sur les "
               u"variantes, pas sur la première livraison."),

dict(id=u"PL-02", titre=u"Où trouver un plugin, et lequel",
     them=u"PL2 · Installation de plugins",
     ref=u"REF-029, REF-030",
     niv=u"Intermédiaire", duree=8, prereq=u"—",
     competence=u"—", bloom=u"Comprendre × procédurale",
     contexte=u"Une définition reçue affiche des composants manquants.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Vous ouvrez une définition et plusieurs composants "
               u"apparaissent en rouge, marqués manquants. Par où "
               u"commencez-vous ?\n"
               u"a) Reconstruire les parties manquantes à la main.\n"
               u"b) Lire le nom du composant manquant, qui porte celui du "
               u"plugin, et l'installer par le gestionnaire de paquets. "
               u"← réponse\n"
               u"c) Demander à l'auteur de refaire la définition sans "
               u"plugin.\n"
               u"d) Réinstaller Rhino.\n\n"
               u"Valeur diagnostique : (a) est le réflexe coûteux — on "
               u"reconstruit parfois des heures ce qu'une installation d'une "
               u"minute aurait résolu. Le point à faire passer : Grasshopper "
               u"dit toujours ce qui manque, et le gestionnaire de paquets "
               u"intégré est à préférer au téléchargement manuel, parce qu'il "
               u"gère les versions et les mises à jour."),

dict(id=u"PL-03", titre=u"Les plugins qui ne servent qu'à travailler mieux",
     them=u"PL3 · Plugins d'ergonomie",
     ref=u"REF-031, REF-032, REF-033, REF-034, REF-035, REF-036, REF-037",
     niv=u"Intermédiaire", duree=20, prereq=u"PL-02",
     competence=u"Installer et régler les plugins d'ergonomie, et juger "
                u"lesquels valent la place qu'ils prennent.",
     bloom=u"Évaluer × procédurale",
     contexte=u"Une définition d'équipe se relit à plusieurs : ce qui la rend "
              u"lisible fait gagner plus de temps que ce qui la rend "
              u"puissante.",
     obj=u"Installer et régler les plugins d'ergonomie, et juger lesquels "
         u"valent la place qu'ils prennent.",
     enonce=u"Installez les plugins d'ergonomie proposés, réglez-les, puis "
            u"reprenez une définition existante et dites, pour chacun, ce "
            u"qu'il vous a réellement fait gagner. Concluez par les deux que "
            u"vous garderiez et les raisons.",
     depart=u"Une définition d'exercice déjà produite, à relire, et l'accès "
            u"au gestionnaire de paquets.",
     att=u"Une définition relue, les plugins réglés, et un jugement motivé "
         u"sur chacun.",
     erreur=u"Tout installer et tout garder. Chaque plugin d'ergonomie ajoute "
            u"un affichage, un raccourci ou une couleur ; empilés sans choix, "
            u"ils encombrent l'écran plus qu'ils n'aident, et la définition "
            u"devient illisible pour qui ne les a pas.",
     donnees_note=u"—",
     limite=u"Le livrable est un jugement argumenté, pas un nombre : la "
            u"validation est visuelle. Ramener cet exercice à une valeur "
            u"chiffrée n'aurait aucun sens.",
     mode=u"Visuel", tol=u"—", nb=0,
     comp=u"Gestionnaire de paquets Rhino, plugins d'ergonomie",
     etapes=[u"Installer les plugins un par un, en relançant Rhino entre "
             u"chacun : installer en bloc empêche de savoir lequel fait quoi.",
             u"Reprendre la même définition après chaque installation.",
             u"Noter ce que le plugin change concrètement : temps gagné, "
             u"erreur évitée, lisibilité.",
             u"Désactiver ceux qui n'ont rien apporté.",
             u"Vérifier que la définition reste lisible pour un collègue qui "
             u"n'a aucun de ces plugins."],
     pieges=[u"Confondre confort personnel et lisibilité partagée : une "
             u"couleur qui vous parle n'existe pas chez le voisin.",
             u"Dépendre d'un plugin d'ergonomie pour comprendre sa propre "
             u"définition : elle devient intransmissible."],
     var=[u"Faire relire votre définition par quelqu'un qui n'a aucun plugin "
          u"installé.",
          u"Chronométrer la même reprise avec et sans."],
     gamif=u"G-18 Duel de versions",
     bareme=u"Grille : plugins installés et réglés (2), jugement motivé sur "
            u"chacun (2), définition lisible sans eux (1).",
     verdict=u"competence"),

dict(id=u"PL-04", titre=u"Choisir un plugin fonctionnel",
     them=u"PL4 · Plugins fonctionnels",
     ref=u"REF-038, REF-039",
     niv=u"Intermédiaire", duree=8, prereq=u"PL-02",
     competence=u"—", bloom=u"Évaluer × conceptuelle",
     contexte=u"Un besoin nouveau — imbriquer des pièces — a sûrement déjà un "
              u"plugin.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Avant d'adopter un plugin fonctionnel dans une définition "
               u"livrée à un client, qu'est-ce qui compte le plus ?\n"
               u"a) Le nombre de composants qu'il apporte.\n"
               u"b) Sa licence, son entretien et ce qui se passe pour le "
               u"client s'il disparaît. ← réponse\n"
               u"c) Sa popularité sur les forums.\n"
               u"d) Qu'il soit gratuit.\n\n"
               u"Valeur diagnostique : (d) est le critère le plus souvent "
               u"appliqué et le plus dangereux — gratuit ne dit rien du droit "
               u"d'usage commercial, ni de la survie du projet. Une "
               u"définition livrée qui dépend d'un plugin abandonné devient "
               u"inexploitable à la première mise à jour de Rhino, et c'est "
               u"le client qui le découvre."),
]


LOT_MP = [

dict(id=u"MP-01", titre=u"Une définition qu'un autre peut reprendre",
     them=u"MP1 · Organisation et lisibilité",
     ref=u"REF-088",
     niv=u"Intermédiaire", duree=30, prereq=u"A-31",
     competence=u"Organiser une définition pour qu'un tiers la reprenne sans "
                u"explication orale.",
     bloom=u"Créer × procédurale",
     contexte=u"Vous partez en congés et la définition doit vivre sans vous.",
     obj=u"Organiser une définition pour qu'un tiers la reprenne sans "
         u"explication orale.",
     enonce=u"Reprenez une de vos définitions et rendez-la reprenable : "
            u"entrées rassemblées et nommées, étapes groupées et titrées, "
            u"sorties identifiées. Faites-la relire par quelqu'un qui ne l'a "
            u"pas écrite, sans un mot d'explication.",
     depart=u"Une définition existante, fonctionnelle mais non organisée.",
     att=u"Une définition dont un tiers retrouve seul les entrées, la "
         u"logique et les sorties.",
     erreur=u"Ajouter des commentaires partout au lieu de structurer. Un "
            u"scribble sur chaque composant n'est pas de la lisibilité, c'est "
            u"du bruit : ce qui se lit, c'est un groupe titré par ce qu'il "
            u"fait, pas par le composant qu'il contient.",
     donnees_note=u"—",
     limite=u"La lisibilité ne se mesure pas par un nombre. Le seul contrôle "
            u"honnête est celui que l'énoncé prescrit : quelqu'un d'autre "
            u"reprend la définition, ou n'y arrive pas.",
     mode=u"Visuel", tol=u"—", nb=0,
     comp=u"Groupes, scribbles, paramètres nommés",
     etapes=[u"Rassembler toutes les entrées réglables au même endroit, à "
             u"gauche, et les nommer par ce qu'elles représentent.",
             u"Grouper les étapes par intention — « répartir les montants » — "
             u"et non par famille de composant.",
             u"Titrer chaque groupe d'une phrase, pas d'un mot.",
             u"Identifier les sorties et les isoler.",
             u"Faire l'essai de reprise par un tiers, en silence."],
     pieges=[u"Titrer les groupes du nom des composants qu'ils contiennent : "
             u"cela n'apprend rien à qui lit.",
             u"Laisser des composants orphelins hors de tout groupe : ils "
             u"font douter de ce qui est actif."],
     var=[u"Reprendre une définition d'un collègue et mesurer le temps qu'il "
          u"vous faut pour la comprendre.",
          u"Rédiger la notice d'une page qui l'accompagne."],
     gamif=u"G-18 Duel de versions",
     bareme=u"Grille : entrées rassemblées (1), groupes titrés par intention "
            u"(2), reprise réussie par un tiers (2).",
     verdict=u"competence"),

dict(id=u"MP-02", titre=u"Trouver ce qui coûte le temps de calcul",
     them=u"MP2 · Performance d'exécution",
     ref=u"REF-089",
     niv=u"Perfectionnement", duree=25, prereq=u"MP-01",
     competence=u"Localiser le composant qui coûte le temps de recalcul, "
                u"plutôt que d'optimiser au hasard.",
     bloom=u"Analyser × procédurale",
     contexte=u"Une définition met plusieurs secondes à se recalculer à "
              u"chaque mouvement de curseur, et le client attend devant "
              u"l'écran.",
     obj=u"Localiser le composant qui coûte le temps de recalcul, plutôt que "
         u"d'optimiser au hasard.",
     enonce=u"Les temps de recalcul des 20 composants d'une définition vous "
            u"sont fournis, en millisecondes. Donnez la part du temps total "
            u"que représentent les trois composants les plus coûteux, en "
            u"pourcentage arrondi à l'entier.",
     depart=u"Les 20 temps mesurés, en millisecondes, dans l'ordre du profil "
            u"affiché par Grasshopper.",
     att=u"97 — la part des trois composants les plus coûteux, en "
         u"pourcentage entier.",
     erreur=u"Optimiser les composants nombreux plutôt que les composants "
            u"lents. Dix-sept composants du relevé coûtent moins de 15 ms "
            u"chacun : les régler tous ne fera rien gagner. Trois en coûtent "
            u"presque tout — et c'est contre-intuitif tant qu'on n'a pas "
            u"mesuré.",
     donnees_note=u"Le relevé est volontairement très déséquilibré : trois "
                  u"composants au-dessus de 1 800 ms, dix-sept sous 30 ms. "
                  u"C'est la répartition réelle d'une définition lente, et "
                  u"c'est ce qui rend la mesure indispensable.",
     limite=u"97 % dit OÙ est le temps, pas ce qu'on peut en récupérer. Un "
            u"composant lent peut l'être irréductiblement — un maillage, "
            u"une intersection — et le profilage désigne la cible sans "
            u"promettre le gain.",
     mode=u"SingleValue", tol=u"0", nb=7,
     comp=u"Sort List, Reverse List, Sub List, Mass Addition, Division, Panel",
     etapes=[u"Sommer les vingt temps pour obtenir le total.",
             u"Trier les temps par ordre décroissant.",
             u"Prélever les trois premiers et les sommer.",
             u"Rapporter au total et convertir en pourcentage.",
             u"Arrondir à l'entier, et en tirer la conclusion : c'est là, et "
             u"seulement là, qu'il faut travailler."],
     pieges=[u"Trier sans inverser : on prend les trois plus rapides.",
             u"Conclure que la définition est « globalement lente » : elle "
             u"ne l'est pas, trois composants le sont."],
     var=[u"Chiffrer le gain si l'un des trois passait à 100 ms.",
          u"Mesurer le profil réel d'une de vos définitions et refaire "
          u"l'analyse."],
     gamif=u"G-01 Score visible",
     bareme=u"1 point si la part est juste à l'entier près.",
     verdict=u"competence"),

dict(id=u"MP-03", titre=u"Une définition qui réagit",
     them=u"MP3 · Chronologie et évènements",
     ref=u"REF-091, REF-092",
     niv=u"Perfectionnement", duree=8, prereq=u"MP-02",
     competence=u"—", bloom=u"Comprendre × conceptuelle",
     contexte=u"On voudrait qu'une définition réagisse à une touche ou à un "
              u"clic dans la vue.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Grasshopper recalcule quand une donnée change. Comment lui "
               u"faire prendre en compte un évènement clavier ou souris ?\n"
               u"a) C'est impossible, Grasshopper n'écoute rien.\n"
               u"b) Par un composant qui expose l'évènement comme une donnée, "
               u"laquelle déclenche alors le recalcul habituel. ← réponse\n"
               u"c) En relançant la définition à la main.\n"
               u"d) En écrivant un plugin, il n'y a pas d'autre voie.\n\n"
               u"Valeur diagnostique : (a) et (d) sont deux façons de "
               u"renoncer trop tôt. Le point à faire passer est conceptuel : "
               u"le modèle de Grasshopper reste le même — une donnée change, "
               u"l'aval se recalcule. L'évènement n'est pas une exception au "
               u"modèle, c'est une donnée de plus."),
]


LOT_AV = [

dict(id=u"AV-01", titre=u"Converger vers une portée",
     them=u"AV1 · Boucles et itération",
     ref=u"REF-093",
     niv=u"Perfectionnement", duree=35, prereq=u"A-30",
     competence=u"Faire converger un calcul par itérations successives "
                u"jusqu'à un critère d'arrêt.",
     bloom=u"Appliquer × procédurale",
     contexte=u"La flèche d'une poutre dépend de sa portée d'une façon qui ne "
              u"s'inverse pas simplement : on cherche la portée qui donne la "
              u"flèche admissible.",
     obj=u"Faire converger un calcul par itérations successives jusqu'à un "
         u"critère d'arrêt.",
     enonce=u"La flèche admissible est atteinte pour une portée comprise "
            u"entre 1 000 et 4 000 mm. Approchez cette portée par bissection "
            u"jusqu'à ce que l'intervalle passe sous 1 mm, et donnez le "
            u"nombre d'itérations nécessaires.",
     depart=u"La fonction de flèche, l'intervalle de départ et le critère "
            u"d'arrêt.",
     att=u"12 — le nombre de bissections pour ramener 3 000 mm sous 1 mm.",
     erreur=u"Fixer le nombre d'itérations à l'avance plutôt que de sortir "
            u"sur un critère. Une boucle à compte fixe s'arrête trop tôt ou "
            u"tourne pour rien ; c'est le critère qui doit commander, et "
            u"c'est là toute la différence entre répéter et converger.",
     donnees_note=u"L'intervalle de départ vaut 3 000 mm : chaque bissection "
                  u"le divise par deux, il faut donc douze passages pour "
                  u"descendre sous 1 mm. Le compte est vérifiable à la main, "
                  u"ce qui permet de contrôler la boucle sans la croire sur "
                  u"parole.",
     limite=u"L'itération demande un plugin de boucle : ce n'est pas natif. "
            u"C'est le nombre d'itérations qui est validé, pas le montage.",
     mode=u"SingleValue", tol=u"0", nb=8,
     comp=u"Plugin de boucle, Larger Than, Addition, Division, Panel",
     etapes=[u"Poser l'intervalle de départ et le critère d'arrêt avant "
             u"d'écrire la boucle.",
             u"À chaque passage, couper l'intervalle en deux et garder la "
             u"moitié qui encadre la solution.",
             u"Compter les passages.",
             u"Sortir dès que la largeur de l'intervalle passe sous 1 mm.",
             u"Contrôler : 3 000 divisé douze fois par deux vaut 0,73 mm, "
             u"onze fois seulement 1,46."],
     pieges=[u"Boucle sans critère de sortie : elle tourne indéfiniment.",
             u"Garder la mauvaise moitié de l'intervalle : la boucle "
             u"converge, mais ailleurs."],
     var=[u"Passer le critère à 0,1 mm et prévoir le nombre d'itérations "
          u"avant de le mesurer.",
          u"Comparer à une recherche par pas constant et chiffrer l'écart."],
     gamif=u"G-02 Barre de progression",
     bareme=u"1 point si le nombre d'itérations vaut 12 et si la sortie se "
            u"fait sur le critère, non sur un compte.",
     verdict=u"competence"),

dict(id=u"AV-02", titre=u"Une chaînette qui se stabilise",
     them=u"AV2 · Simulation physique",
     ref=u"REF-094",
     niv=u"Perfectionnement", duree=35, prereq=u"AV-01",
     competence=u"Conduire une simulation jusqu'à l'équilibre et relever une "
                u"grandeur sur l'état stabilisé.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Un câble de suspension prend, sous son propre poids, une "
              u"forme qu'on ne dessine pas : on la laisse s'établir.",
     obj=u"Conduire une simulation jusqu'à l'équilibre et relever une "
         u"grandeur sur l'état stabilisé.",
     enonce=u"Le câble mesure 6 000 mm et ses deux ancrages sont distants de "
            u"4 800 mm. Laissez la forme s'établir sous son poids propre, et "
            u"donnez la flèche au point bas, en millimètres.",
     depart=u"Les deux ancrages, la longueur de câble et le moteur de "
            u"simulation.",
     att=u"La flèche au point bas, à 5 mm près.",
     erreur=u"Relever la valeur avant stabilisation. Une simulation affiche "
            u"un résultat dès la première itération, et il change encore. "
            u"Lire trop tôt donne une valeur plausible et fausse — le seul "
            u"contrôle est que la valeur cesse de bouger.",
     donnees_note=u"6 000 mm de câble pour 4 800 mm de portée : le mou est "
                  u"assez important pour que la flèche soit franche, et la "
                  u"forme obtenue reste une chaînette, dont la flèche se "
                  u"vérifie par le calcul.",
     limite=u"La simulation demande un moteur dédié, non natif. La tolérance "
            u"de 5 mm tient compte de la convergence, qui n'est jamais "
            u"exactement reproductible.",
     mode=u"NumericTolerance", tol=u"5", nb=7,
     comp=u"Moteur de simulation physique, Divide Curve, Bounds, Panel",
     etapes=[u"Discrétiser le câble en segments réguliers.",
             u"Ancrer les deux extrémités, laisser le reste libre.",
             u"Appliquer le poids propre et lancer la simulation.",
             u"Attendre que la valeur relevée cesse d'évoluer — c'est le "
             u"seul critère d'arrêt honnête.",
             u"Mesurer l'écart vertical entre les ancrages et le point bas."],
     pieges=[u"Trop peu de segments : la forme est anguleuse et la flèche "
             u"sous-évaluée.",
             u"Lire la valeur en cours de convergence."],
     var=[u"Rallonger le câble de 10 % et prévoir l'effet sur la flèche "
          u"avant de le mesurer.",
          u"Comparer à la formule de la chaînette."],
     gamif=u"G-06 Cible et précision",
     bareme=u"1 point si la flèche est juste à 5 mm près sur un état "
            u"stabilisé.",
     verdict=u"competence"),

dict(id=u"AV-03", titre=u"Chercher la meilleure trame",
     them=u"AV3 · Design génératif",
     ref=u"REF-095",
     niv=u"Perfectionnement", duree=40, prereq=u"AV-02",
     competence=u"Poser un problème de recherche de forme — variables, "
                u"objectif, contraintes — et juger l'optimum obtenu.",
     bloom=u"Créer × procédurale",
     contexte=u"Une façade doit être calepinée : moins de panneaux coûte "
              u"moins cher, mais aucun panneau ne peut dépasser 2 400 mm.",
     obj=u"Poser un problème de recherche de forme — variables, objectif, "
         u"contraintes — et juger l'optimum obtenu.",
     enonce=u"La façade mesure 18 600 mm de long. Cherchez le calepinage qui "
            u"minimise le nombre de panneaux sans qu'aucun dépasse "
            u"2 400 mm, et donnez ce nombre.",
     depart=u"La longueur de façade, la largeur maximale de panneau, et un "
            u"moteur de recherche.",
     att=u"8 — le nombre minimal de panneaux.",
     erreur=u"Laisser le moteur chercher sans contrainte et retenir son "
            u"meilleur résultat. Sans la contrainte des 2 400 mm exprimée "
            u"dans la fonction évaluée, l'optimum est un panneau unique de "
            u"18 600 mm : mathématiquement parfait, physiquement absurde. "
            u"Une recherche de forme ne vaut que ce que vaut ce qu'on lui "
            u"demande d'optimiser.",
     donnees_note=u"18 600 divisé par 2 400 vaut 7,75 : la réponse est 8, et "
                  u"l'exercice ne se résout pas en arrondissant au plus "
                  u"proche. C'est aussi un cas où le moteur de recherche est "
                  u"un détour — le calcul direct suffit, et c'est un "
                  u"enseignement en soi.",
     limite=u"La recherche demande un moteur d'optimisation. Ce qui est "
            u"validé est le nombre de panneaux ; l'exercice vaut surtout "
            u"pour la formulation du problème, que le formateur relit.",
     mode=u"SingleValue", tol=u"0", nb=8,
     comp=u"Moteur d'optimisation, Division, Round, Panel",
     etapes=[u"Écrire d'abord ce qu'on minimise et sous quelle contrainte.",
             u"Exprimer la contrainte DANS la fonction évaluée, non à côté.",
             u"Lancer la recherche.",
             u"Contrôler l'optimum par le calcul direct : 18 600 ÷ 2 400 "
             u"arrondi au supérieur.",
             u"Conclure : quand le calcul direct suffit, le moteur de "
             u"recherche est un luxe — savoir le reconnaître fait partie de "
             u"la compétence."],
     pieges=[u"Contrainte laissée hors de la fonction évaluée.",
             u"Employer un moteur de recherche là où une division suffit, et "
             u"ne pas s'en apercevoir."],
     var=[u"Ajouter une contrainte de panneaux tous égaux et refaire la "
          u"recherche.",
          u"Introduire un coût par joint et voir l'optimum se déplacer."],
     gamif=u"G-21 Optimisation comparée",
     bareme=u"1 point si le nombre vaut 8 et si la contrainte figure dans la "
            u"fonction évaluée.",
     verdict=u"competence"),
]


LOT_DV = [

dict(id=u"DV-01", titre=u"Quand écrire du script plutôt que câbler",
     them=u"DV1 · Scripting dans Grasshopper",
     ref=u"REF-100",
     niv=u"Expert", duree=8, prereq=u"IA-04",
     competence=u"—", bloom=u"Évaluer × conceptuelle",
     contexte=u"Une partie de définition compte quarante composants pour une "
              u"opération qui s'écrirait en cinq lignes.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Quand vaut-il mieux écrire un composant scripté que câbler "
               u"des composants natifs ?\n"
               u"a) Dès qu'on sait programmer : c'est toujours plus rapide.\n"
               u"b) Quand la logique est itérative ou conditionnelle, et que "
               u"le câblage la rendrait illisible. ← réponse\n"
               u"c) Jamais : une définition doit rester lisible par des "
               u"non-programmeurs.\n"
               u"d) Uniquement pour les performances.\n\n"
               u"Valeur diagnostique : (a) et (c) sont deux dogmes "
               u"symétriques et également coûteux. Le premier produit des "
               u"définitions que personne d'autre ne maintient ; le second "
               u"fait câbler des boucles sur cinquante composants. Le critère "
               u"utile est la lisibilité du résultat, pas la préférence de "
               u"celui qui écrit."),

dict(id=u"DV-02", titre=u"Un composant scripté qui parle à RhinoCommon",
     them=u"DV2 · API et librairies",
     ref=u"REF-101, REF-102, REF-103",
     niv=u"Expert", duree=35, prereq=u"IA-04",
     competence=u"Employer l'interface de programmation de Rhino depuis un "
                u"composant scripté pour obtenir ce qu'aucun composant natif "
                u"ne donne.",
     bloom=u"Appliquer × procédurale",
     contexte=u"On cherche, sur une courbe, le point où le rayon de courbure "
              u"passe sous le rayon de cintrage de la machine — information "
              u"qu'aucun composant natif ne rend directement.",
     obj=u"Employer l'interface de programmation de Rhino depuis un composant "
         u"scripté pour obtenir ce qu'aucun composant natif ne donne.",
     enonce=u"Le rayon de cintrage minimal de la machine est de 250 mm. Sur "
            u"la courbe fournie, donnez la longueur cumulée des portions où "
            u"le rayon de courbure descend sous cette valeur, en millimètres.",
     depart=u"La courbe de tracé et le rayon de cintrage minimal.",
     att=u"La longueur cumulée des portions trop cintrées, à 5 mm près.",
     erreur=u"Échantillonner la courbe trop grossièrement. La courbure varie "
            u"continûment : sur un développé de près de six mètres, un "
            u"échantillon tous les 200 mm peut enjamber entièrement la zone "
            u"trop cintrée et conclure que la pièce est fabricable. Le pas "
            u"d'échantillonnage est un choix, et il doit être justifié — "
            u"seconde erreur, plus discrète : échantillonner à pas de "
            u"PARAMÈTRE constant et non à pas de LONGUEUR constante. Les "
            u"paramètres se resserrent dans les courbes, et la zone trop "
            u"cintrée ressort quatre fois trop longue.",
     donnees_note=u"Le tracé mesure 5 988 mm et son rayon tombe à 155 mm sur "
                  u"un coude unique : quelque 106 mm passent sous les 250 mm "
                  u"admis, soit moins de deux pour cent du développé. Assez "
                  u"large pour être trouvé avec un pas raisonnable, assez "
                  u"étroit pour être manqué avec un pas négligent. La "
                  u"tolérance de 5 mm sanctionne la détection, non la "
                  u"finesse du pas : un point tous les 10 mm suffit à "
                  u"passer, un point tous les 20 mm ne suffit plus.",
     limite=u"La longueur cumulée dépend du PAS d'échantillonnage : plus il "
            u"est fin, plus les extrémités des portions se précisent. La "
            u"tolérance de 5 mm en tient compte. Une mesure exacte "
            u"demanderait de résoudre l'égalité rayon = 250, ce que "
            u"l'exercice ne demande pas.",
     mode=u"NumericTolerance", tol=u"5", nb=7,
     comp=u"C# Script ou Python 3 Script, Curve, Panel",
     etapes=[u"Choisir un pas d'échantillonnage et le justifier par rapport à "
             u"la taille de la zone recherchée.",
             u"Parcourir la courbe et relever la courbure en chaque point, "
             u"via l'interface de programmation.",
             u"Convertir la courbure en rayon — l'un est l'inverse de "
             u"l'autre.",
             u"Repérer les intervalles où le rayon passe sous le seuil.",
             u"Sommer leurs longueurs, et contrôler en divisant le pas par "
             u"deux : le résultat doit peu bouger."],
     pieges=[u"Confondre courbure et rayon : ils varient en sens inverse.",
             u"Pas d'échantillonnage choisi au hasard, sans contrôle de "
             u"convergence."],
     var=[u"Rendre le pas adaptatif : plus fin là où la courbure varie vite.",
          u"Sortir aussi la position du point le plus cintré."],
     gamif=u"G-06 Cible et précision",
     bareme=u"1 point si la longueur est juste à 1 mm près et si le pas a été "
            u"contrôlé par convergence.",
     verdict=u"competence"),

dict(id=u"DV-03", titre=u"Ce que les librairies évitent d'écrire",
     them=u"DV2 · API et librairies",
     ref=u"REF-104, REF-105",
     niv=u"Expert", duree=8, prereq=u"DV-02",
     competence=u"—", bloom=u"Comprendre × conceptuelle",
     contexte=u"Un besoin de géométrie de calcul — enveloppe convexe, "
              u"triangulation — se présente dans un composant scripté.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Vous avez besoin d'une triangulation dans un composant "
               u"scripté. Par où commencez-vous ?\n"
               u"a) L'écrire : c'est un bon exercice.\n"
               u"b) Chercher si RhinoCommon la fournit déjà, puis une "
               u"librairie éprouvée. ← réponse\n"
               u"c) La demander à un assistant, qui l'écrira vite.\n"
               u"d) Changer d'approche pour éviter d'en avoir besoin.\n\n"
               u"Valeur diagnostique : (c) est devenu le réflexe majoritaire "
               u"et c'est le plus trompeur — un assistant produit vite une "
               u"triangulation qui marche sur le cas d'essai et échoue sur "
               u"les cas dégénérés, que trente ans de bibliothèque ont, eux, "
               u"déjà rencontrés. La question ne porte pas sur la difficulté "
               u"d'écrire, mais sur le coût de valider."),

dict(id=u"DV-04", titre=u"Du composant scripté au plugin installé",
     them=u"DV3 · Compilation et IDE",
     ref=u"REF-096, REF-097, REF-098, REF-099",
     niv=u"Expert", duree=120, prereq=u"IA-07, DV-02",
     competence=u"Passer d'un composant scripté à un plugin compilé et "
                u"installé, côté Grasshopper et côté Rhino.",
     bloom=u"Créer × procédurale",
     contexte=u"Un composant scripté qui a fait ses preuves doit être "
              u"distribué à l'équipe, sans que chacun recolle du code.",
     obj=u"Passer d'un composant scripté à un plugin compilé et installé, "
         u"côté Grasshopper et côté Rhino.",
     enonce=u"Reprenez le composant scripté de DV-02 et faites-en un plugin "
            u"compilé, installé et visible dans Grasshopper. Ajoutez-y une "
            u"commande Rhino qui rend le même service depuis la ligne de "
            u"commande.",
     depart=u"Le composant scripté de DV-02, un environnement de compilation "
            u"et les modèles de projet Rhino.",
     att=u"Un plugin chargé par Rhino, dont le composant apparaît dans "
         u"Grasshopper et dont la commande répond en ligne de commande.",
     erreur=u"Compiler pour la mauvaise cible. Un plugin construit pour une "
            u"version majeure de Rhino ne se charge pas dans l'autre, et le "
            u"symptôme est silencieux : le composant n'apparaît simplement "
            u"pas, sans message d'erreur.",
     donnees_note=u"—",
     limite=u"Le livrable est un plugin compilé : la validation est visuelle, "
            u"sur le composant et la commande réellement disponibles.",
     mode=u"Visuel", tol=u"—", nb=0,
     comp=u"Environnement de compilation, modèles de projet Rhino, RhinoCommon",
     etapes=[u"Partir du modèle de projet fourni par Rhino, plutôt que d'un "
             u"projet vide.",
             u"Reporter le code du composant scripté, en déclarant "
             u"explicitement entrées et sorties.",
             u"Figer le GUID du composant dès la première version.",
             u"Compiler pour la version de Rhino visée, déposer le fichier, "
             u"le débloquer si Windows l'a marqué, relancer Rhino.",
             u"Ajouter la commande Rhino, en respectant la convention de "
             u"nommage du plugin."],
     pieges=[u"Cible de compilation qui ne correspond pas à la version "
             u"installée : rien ne se charge, rien ne le dit.",
             u"Fichier téléchargé non débloqué : même symptôme.",
             u"GUID régénéré entre deux versions : les définitions des "
             u"collègues cassent."],
     var=[u"Ajouter une icône et une entrée d'aide.",
          u"Publier le plugin avec une licence explicite et un numéro de "
          u"version."],
     gamif=u"G-25 Projet jalonné",
     bareme=u"Grille : composant visible dans Grasshopper (2), commande Rhino "
            u"opérante (2), GUID stable et version documentée (1).",
     verdict=u"competence"),
]


LOT_WB = [

dict(id=u"WB-01", titre=u"Une définition utilisable par quelqu'un d'autre",
     them=u"WB1 · Interfaces utilisateur",
     ref=u"REF-106, REF-107",
     niv=u"Perfectionnement", duree=40, prereq=u"MP-01",
     competence=u"Donner à une définition une interface qui permette de "
                u"s'en servir sans l'ouvrir.",
     bloom=u"Créer × procédurale",
     contexte=u"Le commercial doit pouvoir configurer un produit devant le "
              u"client, sans voir un seul composant.",
     obj=u"Donner à une définition une interface qui permette de s'en servir "
         u"sans l'ouvrir.",
     enonce=u"Reprenez une de vos définitions et donnez-lui une interface : "
            u"seuls les paramètres utiles sont exposés, nommés en langage "
            u"métier, avec leurs bornes. Faites-la utiliser par quelqu'un qui "
            u"ne connaît pas Grasshopper.",
     depart=u"Une définition fonctionnelle et organisée.",
     att=u"Une définition pilotable par un tiers, sans ouverture du graphe.",
     erreur=u"Exposer tous les paramètres. Une interface qui montre trente "
            u"curseurs n'est pas une interface : le travail consiste "
            u"justement à choisir les cinq qui comptent et à cacher le reste.",
     donnees_note=u"—",
     limite=u"L'utilisabilité ne se mesure pas par un nombre. Le contrôle est "
            u"celui que l'énoncé prescrit : un tiers s'en sert, ou n'y arrive "
            u"pas.",
     mode=u"Visuel", tol=u"—", nb=0,
     comp=u"Paramètres nommés, bornes, groupes, intégration Rhino",
     etapes=[u"Lister les paramètres et distinguer ceux que l'utilisateur "
             u"doit régler de ceux qui relèvent du concepteur.",
             u"Renommer les premiers en langage métier — « hauteur "
             u"d'allège », non « slider 3 ».",
             u"Poser des bornes qui interdisent les valeurs absurdes.",
             u"Rassembler l'interface au même endroit et masquer le reste.",
             u"Faire l'essai avec quelqu'un qui ne connaît pas l'outil."],
     pieges=[u"Bornes trop larges : l'utilisateur produit une géométrie "
             u"impossible et croit s'être trompé.",
             u"Noms techniques conservés : l'interface reste illisible."],
     var=[u"Ajouter un jeu de valeurs par défaut correspondant au produit "
          u"courant.",
          u"Intégrer la définition dans Rhino pour qu'elle se lance comme une "
          u"commande."],
     gamif=u"G-25 Projet jalonné",
     bareme=u"Grille : paramètres choisis et nommés (2), bornes posées (1), "
            u"usage réussi par un tiers (2).",
     verdict=u"competence"),

dict(id=u"WB-02", titre=u"Publier un configurateur",
     them=u"WB2 · Publication web",
     ref=u"REF-108, REF-109, REF-110",
     niv=u"Perfectionnement", duree=90, prereq=u"WB-01",
     competence=u"Publier une définition sur le web et en faire sortir les "
                u"livrables attendus par un client.",
     bloom=u"Créer × procédurale",
     contexte=u"Le client veut configurer son produit depuis son navigateur "
              u"et repartir avec un plan et un modèle 3D.",
     obj=u"Publier une définition sur le web et en faire sortir les "
         u"livrables attendus par un client.",
     enonce=u"Publiez la définition interfacée en WB-01 sur une plateforme "
            u"web. Le configurateur doit permettre de régler les paramètres, "
            u"de télécharger le modèle 3D et d'obtenir un plan au format PDF.",
     depart=u"La définition interfacée de WB-01 et un compte sur une "
            u"plateforme de publication.",
     att=u"Un configurateur en ligne qui rend les trois livrables.",
     erreur=u"Publier sans borner les paramètres. En ligne, personne ne "
            u"surveille : une valeur hors domaine produit une géométrie "
            u"absurde, ou fait échouer le calcul côté serveur, et c'est le "
            u"client qui le voit en premier.",
     donnees_note=u"—",
     limite=u"Le livrable est un service en ligne : validation visuelle. "
            u"Dépend d'une plateforme tierce et d'un compte.",
     mode=u"Visuel", tol=u"—", nb=0,
     comp=u"Plateforme de publication web, export 3D, mise en plan",
     etapes=[u"Vérifier que la définition ne dépend d'aucun plugin absent de "
             u"la plateforme.",
             u"Contrôler les temps de calcul : ce qui prend cinq secondes en "
             u"local est insupportable en ligne.",
             u"Publier, puis régler l'interface exposée.",
             u"Brancher l'export du modèle 3D.",
             u"Produire le plan PDF et vérifier qu'il reste juste pour toutes "
             u"les valeurs autorisées."],
     pieges=[u"Plugin non disponible côté serveur : la définition ne calcule "
             u"pas.",
             u"Paramètres non bornés.",
             u"Plan PDF correct pour la valeur par défaut seulement."],
     var=[u"Ajouter un chiffrage automatique au configurateur.",
          u"Mesurer le temps de réponse et l'optimiser."],
     gamif=u"G-25 Projet jalonné",
     bareme=u"Grille : configurateur en ligne (2), export 3D (1), plan PDF "
            u"juste sur toute la plage (2).",
     verdict=u"competence"),

dict(id=u"WB-03", titre=u"Rhino sans Rhino",
     them=u"WB3 · Interopérabilité",
     ref=u"REF-111, REF-112",
     niv=u"Expert", duree=8, prereq=u"WB-02",
     competence=u"—", bloom=u"Comprendre × conceptuelle",
     contexte=u"Une application métier doit exploiter la géométrie de Rhino "
              u"sans que l'utilisateur ouvre Rhino.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Vous voulez faire tourner une définition Grasshopper depuis "
               u"une application web, sans interface Rhino. Que "
               u"cherchez-vous ?\n"
               u"a) Rhino.Inside, qui charge Rhino dans un autre logiciel "
               u"hôte.\n"
               u"b) Rhino.Compute, qui expose le moteur de calcul comme un "
               u"service appelable à distance. ← réponse\n"
               u"c) Un export en maillage, qui suffit toujours.\n"
               u"d) Les deux font la même chose.\n\n"
               u"Valeur diagnostique : (a) et (d) confondent deux réponses à "
               u"deux besoins différents — Rhino.Inside fait cohabiter Rhino "
               u"avec Revit ou AutoCAD sur le même poste ; Rhino.Compute met "
               u"le moteur au bout d'un appel réseau. Se tromper de l'un pour "
               u"l'autre fait partir sur une architecture entière qu'il "
               u"faudra défaire."),
]


LOTS = [(u"PL", LOT_PL), (u"MP", LOT_MP), (u"AV", LOT_AV),
        (u"DV", LOT_DV), (u"WB", LOT_WB)]
TOUS = LOT_PL + LOT_MP + LOT_AV + LOT_DV + LOT_WB
