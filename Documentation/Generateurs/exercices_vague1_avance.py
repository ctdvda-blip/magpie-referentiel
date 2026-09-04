# -*- coding: utf-8 -*-
"""Vague 1 de l'equilibrage, suite : lots DV, WB et IA.

Meme demarche et memes regles que `exercices_vague1.py`, qui porte les lots
GP, QT et FA. Le fichier est separe parce que le premier atteignait deja
quatre cents lignes, non parce que la logique differe.

UN POINT DE FOND SUR LA CATEGORIE « COMPILATION ET IDE »
--------------------------------------------------------
Elle compte quatre notions et n'avait qu'un exercice. Mais compiler un plugin
n'est pas une competence qui se mesure par un nombre : c'est pour l'essentiel
une CONNAISSANCE (ce que la compilation change) et un GESTE DE DEPLOIEMENT
(le faire charger ailleurs). La skill interdit d'en faire de faux exercices a
reponse numerique. D'ou la forme retenue : deux questions charnieres et un
livrable note sur grille. C'est la juste forme, pas un pis-aller.

Meme raisonnement pour deux items du lot IA : les garde-fous d'un pilotage
agentique et ce qu'une image generee peut donner a la modelisation sont des
jugements, pas des calculs.
"""

# ---------------------------------------------------------------------------
# Jeux de donnees
# ---------------------------------------------------------------------------

#: WB-04 — les quatorze entrees d'une definition a interfacer.
#: (nom, nature) ou nature vaut "choix" (a exposer), "derive" ou "interne".
D_WB04_ENTREES = [
    (u"Largeur du meuble", u"choix"),
    (u"Hauteur du meuble", u"choix"),
    (u"Profondeur du meuble", u"choix"),
    (u"Nombre de tiroirs", u"choix"),
    (u"Essence du placage", u"choix"),
    (u"Type de poignee", u"choix"),
    (u"Epaisseur du panneau", u"derive"),        # suit l'essence
    (u"Jeu de tiroir", u"derive"),               # suit le type de poignee
    (u"Hauteur d'un tiroir", u"derive"),         # hauteur / nombre de tiroirs
    (u"Tolerance de couture", u"interne"),
    (u"Densite du maillage d'apercu", u"interne"),
    (u"Graine aleatoire du placage", u"interne"),
    (u"Rayon de conge d'usinage", u"interne"),
    (u"Origine du plan de construction", u"interne"),
]

#: WB-05 — la frequentation d'un configurateur en ligne
D_WB05 = dict(visites=12000, part_pointe=0.18, recalculs=6, duree=1.2)

#: WB-06 — un maillage d'apercu, en QUADRANGLES. Le STL ne connait que le
#: triangle : c'est la tout le piege.
D_WB06 = dict(quads=24310, entete=84, par_facette=50)

#: WB-07 — la piece a mettre au plan, et la feuille
D_WB07 = dict(longueur=2380.0, hauteur=1640.0, feuille=(420.0, 297.0),
              marge=15.0, echelles=(1, 2, 5, 10, 20, 50, 100))

#: IA-15 — ce qui etait demande a l'agent, et ce qu'il a produit.
#: (source, cible, entree_demandee, entree_produite)
D_IA15_GRAPHE = [
    (u"Largeur", u"Rectangle", 1, 1),
    (u"Hauteur", u"Rectangle", 2, 0),          # divergence
    (u"Rayon de conge", u"Rectangle", 3, 3),
    (u"Rectangle", u"Extrusion", 0, 0),
    (u"Vecteur de montee", u"Extrusion", 1, 0),  # divergence
    (u"Extrusion", u"Fermeture", 0, 0),
    (u"Fermeture", u"Volume", 0, 0),
    (u"Volume", u"Division", 0, 0),
    (u"Un million", u"Division", 1, 0),        # divergence
]

#: IA-17 — le courriel du conducteur de travaux, tel qu'il arrive.
#: (article, quantite_retenue, ce_qui_pique)
D_IA17_COMMANDE = [
    (u"paumelles", 24, None),
    (u"vis a tete fraisee", 48, u"quantite ecrite en toutes lettres"),
    (u"poignees", 18, u"annoncee a 12 puis corrigee a 18 plus bas"),
    (u"cremones", 0, u"demande de prix, pas une commande"),
    (u"serrures", 6, None),
]


# ---------------------------------------------------------------------------
# Lot DV — developpement, scripting et API
# ---------------------------------------------------------------------------

LOT_DV = [

dict(id=u"DV-05", titre=u"Ce que la compilation change vraiment",
     them=u"DV3 · Compilation et IDE",
     ref=u"REF-096",
     niv=u"Expert", duree=8, prereq=u"DV-02",
     competence=u"—", bloom=u"Comprendre × conceptuelle",
     contexte=u"Un composant scripté rend le service attendu depuis six "
              u"mois, dans une trentaine de définitions. La question de le "
              u"compiler se pose.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Votre composant scripté fonctionne. Que vous apporte "
               u"d'abord sa compilation en .gha ?\n"
               u"a) Il ira plus vite : le code n'est plus interprété.\n"
               u"b) Il se distribue et se corrige en un seul endroit, sans "
               u"que personne n'ouvre les définitions. ← réponse\n"
               u"c) Le code source devient illisible pour l'utilisateur.\n"
               u"d) Il pourra enfin appeler RhinoCommon.\n\n"
               u"Valeur diagnostique : (a) et (d) révèlent qu'on n'a pas "
               u"situé ce qu'un composant scripté sait déjà faire — il "
               u"appelle RhinoCommon, et sa lenteur vient presque toujours "
               u"de l'algorithme, pas de l'interprétation. (c) est "
               u"accessoire, et faux au sens strict : un .gha se décompile. "
               u"Le vrai gain est de DISTRIBUTION : trente définitions qui "
               u"embarquaient chacune leur copie du script deviennent trente "
               u"définitions qui pointent vers une version unique."),

dict(id=u"DV-06", titre=u"Le plugin qui parle aussi à Rhino",
     them=u"DV3 · Compilation et IDE",
     ref=u"REF-097, REF-099",
     niv=u"Expert", duree=8, prereq=u"DV-05",
     competence=u"—", bloom=u"Comprendre × conceptuelle",
     contexte=u"Le composant compilé rend service dans Grasshopper. On "
              u"voudrait le même service depuis la ligne de commande Rhino.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Vous avez un .gha qui marche. Que faut-il pour offrir le "
               u"même service en commande Rhino ?\n"
               u"a) Rien : un .gha est déjà chargé par Rhino, la commande "
               u"suit.\n"
               u"b) Un plugin .rhp qui déclare la commande, les deux "
               u"partageant la même bibliothèque de calcul. ← réponse\n"
               u"c) Réécrire le calcul en RhinoScript.\n"
               u"d) Publier le .gha sur le gestionnaire de paquets.\n\n"
               u"Valeur diagnostique : (a) confond « chargé par Rhino » et "
               u"« exposé dans Rhino » — un .gha vit dans Grasshopper, et la "
               u"ligne de commande ne connaît pas ses composants. La bonne "
               u"réponse vaut surtout pour ce qu'elle implique : le calcul "
               u"ne se duplique pas, il se met dans une bibliothèque que les "
               u"deux plugins référencent. Sans quoi la commande et le "
               u"composant divergeront à la première correction."),

dict(id=u"DV-07", titre=u"Un plugin qui s'installe chez quelqu'un d'autre",
     them=u"DV3 · Compilation et IDE",
     ref=u"REF-098",
     niv=u"Expert", duree=50, prereq=u"DV-06",
     competence=u"Livrer un plugin qui se charge sur un poste qui n'est pas "
                u"celui du développeur, et le prouver.",
     bloom=u"Créer × procédurale",
     contexte=u"Le plugin marche sur votre poste. C'est la situation la "
              u"moins informative qui soit : votre poste porte le SDK, les "
              u"dépendances et les chemins de développement.",
     obj=u"Livrer un plugin qui se charge sur un poste qui n'est pas celui "
         u"du développeur, et le prouver.",
     enonce=u"Reprenez le plugin de DV-04 et rendez-le installable : "
            u"manifeste renseigné, dépendances embarquées ou déclarées, "
            u"version visible. Faites-le installer par quelqu'un d'autre, "
            u"sur un poste où l'environnement de développement n'est pas "
            u"présent, et faites-lui exécuter le composant sans un mot "
            u"d'explication.",
     depart=u"Le plugin de DV-04, et un poste qui n'est pas le vôtre.",
     att=u"Un plugin installé et fonctionnel sur un poste tiers, dont le "
         u"composant apparaît dans l'onglet visé et rend le résultat "
         u"attendu.",
     erreur=u"Livrer le seul fichier compilé. Il se chargera chez vous et "
            u"nulle part ailleurs : les dépendances qu'il trouve dans votre "
            u"dossier de compilation n'existent pas sur le poste d'arrivée. "
            u"Et l'échec ne dit rien — le composant est simplement absent de "
            u"l'onglet, sans message.",
     donnees_note=u"—",
     limite=u"Le livrable se juge sur grille : il n'y a pas de définition "
            u"Grasshopper à corriger, et c'est le propre de cet exercice. "
            u"C'est aussi pourquoi la vérification passe par un TIERS — la "
            u"seule qui distingue « ça marche » de « ça marche chez moi ».",
     mode=u"Visuel", tol=u"—", nb=0,
     comp=u"Environnement de développement, gabarit de plugin Grasshopper, "
          u"gestionnaire de paquets",
     etapes=[u"Renseigner le manifeste : nom, version, auteur, description, "
             u"icône.",
             u"Lister les dépendances et décider, pour chacune, entre "
             u"l'embarquer et l'exiger.",
             u"Produire le paquet d'installation.",
             u"Installer sur un poste tiers, sans environnement de "
             u"développement.",
             u"Faire exécuter le composant par son utilisateur, sans "
             u"assistance."],
     pieges=[u"Livrer le binaire seul.",
             u"Oublier de faire croître le numéro de version : la mise à "
             u"jour ne remplace alors rien.",
             u"Tester sur son propre poste et conclure."],
     var=[u"Publier sur le gestionnaire de paquets et faire installer par la "
          u"voie normale.",
          u"Livrer une version 2 et vérifier qu'elle remplace bien la "
          u"première."],
     gamif=u"G-23 Livraison à l'aveugle",
     bareme=u"Grille : manifeste complet (1), dépendances traitées (1), "
            u"installation réussie sur un poste tiers (2), composant exécuté "
            u"sans assistance (1).",
     verdict=u"competence"),

]


# ---------------------------------------------------------------------------
# Lot WB — interfaces, web et interoperabilite
# ---------------------------------------------------------------------------

LOT_WB = [

dict(id=u"WB-04", titre=u"Ce qu'on expose, et ce qu'on cache",
     them=u"WB1 · Interfaces utilisateur",
     ref=u"REF-107",
     niv=u"Perfectionnement", duree=25, prereq=u"WB-01",
     competence=u"Distinguer, parmi les entrées d'une définition, celles qui "
                u"relèvent d'un choix de l'utilisateur de celles qui se "
                u"déduisent ou qui règlent l'outil.",
     bloom=u"Analyser × conceptuelle",
     contexte=u"La définition va être pilotée depuis Rhino par quelqu'un qui "
              u"n'ouvrira jamais le graphe. Tout ce qu'on expose, il faudra "
              u"le lui expliquer ; tout ce qu'on cache, il ne pourra plus le "
              u"régler.",
     obj=u"Distinguer, parmi les entrées d'une définition, celles qui "
         u"relèvent d'un choix de l'utilisateur de celles qui se déduisent "
         u"ou qui règlent l'outil.",
     enonce=u"La définition du meuble compte quatorze entrées, décrites une "
            u"à une avec ce qu'elles commandent et ce dont elles dépendent. "
            u"Donnez le nombre d'entrées à exposer dans l'interface.",
     depart=u"La liste des quatorze entrées et leur description.",
     att=u"6 — les six entrées qui relèvent d'un choix du client.",
     erreur=u"Exposer les quatorze. L'utilisateur peut alors régler la "
            u"tolérance de couture et la graine aléatoire du placage, et "
            u"surtout saisir une hauteur de tiroir incompatible avec la "
            u"hauteur du meuble : trois entrées se DÉDUISENT des autres, et "
            u"les exposer revient à autoriser deux vérités contradictoires "
            u"dans la même définition.",
     donnees_note=u"Quatorze entrées : six choix, trois grandeurs dérivées, "
                  u"cinq réglages internes. Les trois familles donnent trois "
                  u"réponses distinctes — 6, 9 et 14 — donc trois erreurs "
                  u"lisibles. Les dérivées sont le vrai discriminant : les "
                  u"repérer demande de lire les dépendances, pas seulement "
                  u"les intitulés.",
     limite=u"L'exercice valide un compte, pas une interface. Une interface "
            u"à six champs mal nommés est aussi inutilisable qu'une "
            u"interface à quatorze : le nommage se juge en WB-01.",
     mode=u"SingleValue", tol=u"0", nb=5,
     comp=u"Texte, Member Index, Cull Pattern, List Length, Panel",
     etapes=[u"Classer chaque entrée : choix, grandeur dérivée, ou réglage "
             u"interne.",
             u"Écarter les réglages internes : ils appartiennent à l'auteur "
             u"de la définition.",
             u"Écarter les grandeurs dérivées : les exposer autoriserait des "
             u"saisies contradictoires.",
             u"Compter ce qui reste."],
     pieges=[u"Exposer tout ce qui est un curseur.",
             u"Exposer une grandeur dérivée « pour laisser le choix », et "
             u"créer une incohérence silencieuse.",
             u"Cacher un vrai choix parce qu'il a une valeur par défaut "
             u"raisonnable."],
     var=[u"Nommer les six entrées en langage client et poser leurs bornes.",
          u"Faire piloter la définition par quelqu'un qui ne connaît pas "
          u"Grasshopper, et relever ce qu'il demande."],
     gamif=u"G-17 Passation",
     bareme=u"1 point si le compte est juste.",
     verdict=u"competence"),

dict(id=u"WB-05", titre=u"Dimensionner le calcul d'un configurateur",
     them=u"WB3 · Interopérabilité",
     ref=u"REF-112",
     niv=u"Expert", duree=30, prereq=u"WB-03",
     competence=u"Dimensionner une capacité de calcul distante à partir de "
                u"la fréquentation attendue, en raisonnant sur la pointe et "
                u"non sur la moyenne.",
     bloom=u"Analyser × procédurale",
     contexte=u"Le configurateur en ligne délègue ses recalculs à un service "
              u"distant, facturé à l'instance et à l'heure. Sous-dimensionné, "
              u"il fait attendre ; sur-dimensionné, il coûte pour rien.",
     obj=u"Dimensionner une capacité de calcul distante à partir de la "
         u"fréquentation attendue, en raisonnant sur la pointe et non sur la "
         u"moyenne.",
     enonce=u"Le configurateur reçoit 12 000 visites par jour, dont 18 % se "
            u"concentrent sur l'heure de pointe. Chaque visite déclenche "
            u"6 recalculs, et un recalcul occupe une instance pendant "
            u"1,2 seconde. Donnez le nombre d'instances nécessaires pour "
            u"tenir la pointe sans faire attendre.",
     depart=u"La fréquentation quotidienne, la part de l'heure de pointe, le "
            u"nombre de recalculs par visite et la durée d'un recalcul.",
     att=u"5 instances — la pointe demande 15 552 secondes de calcul pour "
         u"3 600 secondes d'horloge.",
     erreur=u"Lisser la charge sur les vingt-quatre heures : 12 000 × 6 × "
            u"1,2 ÷ 86 400 donne 1 instance. Le service tiendra la nuit et "
            u"s'effondrera à l'heure où il y a du monde, c'est-à-dire au "
            u"seul moment qui compte. Un dimensionnement à la moyenne est un "
            u"dimensionnement pour personne.",
     donnees_note=u"Une pointe à 18 % de la journée correspond à ce "
                  u"qu'observent les configurateurs grand public, dont le "
                  u"trafic se concentre en soirée. Le rapport entre le "
                  u"dimensionnement à la pointe (5) et à la moyenne (1) vaut "
                  u"cinq : l'erreur ne se rattrape pas par une marge de "
                  u"sécurité.",
     limite=u"Le calcul suppose des recalculs indépendants et de durée "
            u"constante. Une mise en cache des configurations les plus "
            u"demandées change tout — et c'est le premier levier à actionner "
            u"avant d'acheter des instances.",
     mode=u"SingleValue", tol=u"0", nb=8,
     comp=u"Multiplication, Division, Round, Panel",
     etapes=[u"Ramener la fréquentation à l'heure de pointe.",
             u"En déduire le nombre de recalculs à absorber dans l'heure.",
             u"Convertir en secondes de calcul demandées.",
             u"Rapporter aux 3 600 secondes que rend une instance en une "
             u"heure.",
             u"Arrondir au SUPÉRIEUR : une instance ne se loue pas par "
             u"quart."],
     pieges=[u"Dimensionner sur la moyenne quotidienne.",
             u"Arrondir au plus proche : 4,32 devient 4, et la pointe "
             u"déborde.",
             u"Oublier les six recalculs par visite et compter une visite "
             u"pour un calcul."],
     var=[u"Ajouter un cache qui absorbe 40 % des recalculs et refaire le "
          u"dimensionnement.",
          u"Chiffrer le coût mensuel des deux hypothèses, et le comparer au "
          u"coût d'une seconde d'attente pour un visiteur."],
     gamif=u"G-22 Mise en charge",
     bareme=u"1 point si le nombre d'instances est juste et arrondi au "
            u"supérieur.",
     verdict=u"competence"),

dict(id=u"WB-06", titre=u"Le poids du modèle que l'on télécharge",
     them=u"WB2 · Publication web",
     ref=u"REF-109",
     niv=u"Perfectionnement", duree=25, prereq=u"WB-02",
     competence=u"Prévoir le poids d'un fichier d'échange à partir de la "
                u"structure du maillage exporté, avant de le proposer au "
                u"téléchargement.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le configurateur propose le téléchargement du modèle. Le "
              u"fichier part souvent sur une connexion mobile : son poids se "
              u"prévoit avant de le produire, pas après.",
     obj=u"Prévoir le poids d'un fichier d'échange à partir de la structure "
         u"du maillage exporté, avant de le proposer au téléchargement.",
     enonce=u"Le maillage d'aperçu compte 24 310 faces quadrangulaires. Vous "
            u"l'exportez dans un format binaire qui ne stocke que des "
            u"triangles, avec un en-tête de 84 octets et 50 octets par "
            u"facette. Donnez le poids du fichier, en octets.",
     depart=u"Le nombre de faces du maillage, leur nature, et la structure "
            u"du format d'export.",
     att=u"2 431 084 octets — soit 2,32 Mio.",
     erreur=u"Compter 50 octets par face du maillage : 1 215 584 octets, la "
            u"moitié. Le format ne connaît que le TRIANGLE ; un maillage "
            u"quadrangulaire est triangulé à l'export, et chaque quadrangle "
            u"devient deux facettes. L'erreur ne se voit pas au calcul — "
            u"elle se voit quand le fichier arrive deux fois plus lourd que "
            u"promis à l'utilisateur.",
     donnees_note=u"24 310 quadrangles est l'ordre de grandeur d'un aperçu "
                  u"de meuble correctement maillé. Les deux réponses "
                  u"possibles sont dans un rapport de deux exactement, ce "
                  u"qui rend l'erreur immédiatement identifiable ; et "
                  u"l'en-tête de 84 octets est assez petit pour qu'on "
                  u"l'oublie sans que le résultat change d'ordre de "
                  u"grandeur — donc assez discret pour départager une "
                  u"réponse construite d'une réponse approchée.",
     limite=u"Ce format ne porte ni matière, ni couleur, ni unité. Le poids "
            u"n'est qu'un critère : la fiche invite à le comparer au 3DM et "
            u"au glTF, qui portent davantage pour un poids voisin.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Multiplication, Addition, Panel",
     etapes=[u"Convertir les faces quadrangulaires en triangles.",
             u"Multiplier par le poids d'une facette.",
             u"Ajouter l'en-tête.",
             u"Convertir en mébioctets pour l'annoncer à l'utilisateur."],
     pieges=[u"Compter une facette par face du maillage.",
             u"Oublier l'en-tête.",
             u"Confondre mébioctet et mégaoctet en annonçant le poids."],
     var=[u"Refaire le calcul pour la variante texte du même format et "
          u"mesurer le rapport.",
          u"Réduire le maillage de moitié et juger ce que l'aperçu y perd."],
     gamif=u"G-16 Livrable pesé",
     bareme=u"1 point si le poids en octets est juste.",
     verdict=u"competence"),

dict(id=u"WB-07", titre=u"Le plan qui tient sur la feuille",
     them=u"WB2 · Publication web",
     ref=u"REF-110",
     niv=u"Perfectionnement", duree=25, prereq=u"WB-02",
     competence=u"Choisir l'échelle normalisée qui fait tenir une pièce sur "
                u"un format donné, marges comprises.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le configurateur produit le plan en PDF, que le client "
              u"imprime lui-même. Une échelle non normalisée rend le plan "
              u"inutilisable : personne ne mesure au 1:6,1.",
     obj=u"Choisir l'échelle normalisée qui fait tenir une pièce sur un "
         u"format donné, marges comprises.",
     enonce=u"La pièce mesure 2 380 mm de long et 1 640 mm de haut. Le plan "
            u"sort sur une feuille de 420 × 297 mm, avec 15 mm de marge sur "
            u"chaque bord. Les échelles disponibles sont 1:1, 1:2, 1:5, "
            u"1:10, 1:20, 1:50 et 1:100. Donnez le dénominateur de la plus "
            u"grande échelle qui convient.",
     depart=u"Les dimensions de la pièce, le format de la feuille, la marge, "
            u"et la liste des échelles normalisées.",
     att=u"10 — l'échelle 1:10, qui donne 238 × 164 mm dans une zone utile "
         u"de 390 × 267 mm.",
     erreur=u"Calculer le rapport exact — 6,10 en longueur — et retenir 1:5 "
            u"en arrondissant vers l'échelle voisine. Au 1:5, la pièce fait "
            u"476 mm et déborde de 86 mm : le PDF s'imprime quand même, "
            u"tronqué. Une échelle se choisit DANS la liste, et toujours "
            u"vers la plus petite.",
     donnees_note=u"Le rapport nécessaire vaut 6,10 en longueur et 6,14 en "
                  u"hauteur : les deux dépassent 5 et aucun n'atteint 10, de "
                  u"sorte que ni la longueur seule ni la hauteur seule ne "
                  u"suffisent à trancher — il faut vérifier les deux. Une "
                  u"pièce plus étroite aurait laissé passer le réflexe de ne "
                  u"regarder que la plus grande dimension.",
     limite=u"L'exercice choisit l'échelle, pas la mise en page : cartouche, "
            u"cotation et nomenclature occupent aussi la feuille, et se "
            u"traitent au format supérieur ou en plusieurs vues.",
     mode=u"SingleValue", tol=u"0", nb=8,
     comp=u"Subtraction, Division, Larger Than, Cull Pattern, List Item, "
          u"Panel",
     etapes=[u"Retrancher les marges pour obtenir la zone utile.",
             u"Calculer le rapport nécessaire sur chacune des deux "
             u"dimensions.",
             u"Retenir le plus grand des deux.",
             u"Choisir dans la liste la première échelle dont le "
             u"dénominateur l'atteint ou le dépasse."],
     pieges=[u"Ne vérifier que la longueur.",
             u"Oublier les marges.",
             u"Retenir une échelle non normalisée parce qu'elle « tient "
             u"mieux »."],
     var=[u"Passer au format inférieur et reprendre le choix.",
          u"Réserver 60 mm de cartouche en bas de feuille et recommencer."],
     gamif=u"G-16 Livrable pesé",
     bareme=u"1 point si le dénominateur est juste.",
     verdict=u"competence"),

]


# ---------------------------------------------------------------------------
# Lot IA — IA et assistance generative
# ---------------------------------------------------------------------------

LOT_IA = [

dict(id=u"IA-15", titre=u"Relire le graphe qu'un agent a construit",
     them=u"IA7 · Agents et protocoles",
     ref=u"REF-137",
     niv=u"Perfectionnement", duree=30, prereq=u"IA-12",
     competence=u"Confronter le graphe produit par un agent à la "
                u"spécification qu'on lui avait donnée, et compter ce qui "
                u"diverge — plutôt que de juger sur l'aperçu.",
     bloom=u"Évaluer × procédurale",
     contexte=u"L'agent a construit la définition en trente secondes. "
              u"L'aperçu montre un volume plausible. C'est précisément le "
              u"moment où l'on ne vérifie pas.",
     obj=u"Confronter le graphe produit par un agent à la spécification "
         u"qu'on lui avait donnée, et compter ce qui diverge.",
     enonce=u"Vous aviez spécifié neuf liaisons, chacune avec son entrée de "
            u"destination. Le relevé du graphe produit vous est fourni en "
            u"regard. Donnez le nombre de liaisons qui ne sont pas "
            u"conformes à la spécification.",
     depart=u"Les neuf liaisons demandées et les neuf liaisons produites, "
            u"chacune avec l'indice de l'entrée de destination.",
     att=u"3 — trois liaisons aboutissent sur une autre entrée que celle "
         u"demandée.",
     erreur=u"Compter les liaisons manquantes, et n'en trouver aucune : les "
            u"neuf liaisons existent bien, et le graphe est complet. Ce qui "
            u"diffère est leur POINT D'ARRIVÉE. Un graphe complet peut être "
            u"entièrement faux, et il produit alors un résultat — donc un "
            u"aperçu — parfaitement crédible.",
     donnees_note=u"Les trois divergences aboutissent toutes sur l'entrée "
                  u"d'indice 0, et c'est la panne réelle des ponts "
                  u"agentiques : beaucoup d'implémentations ignorent "
                  u"silencieusement l'indice demandé et écrivent sur la "
                  u"première entrée. Le graphe se construit, ne signale "
                  u"rien, et calcule autre chose. Neuf liaisons est un "
                  u"format assez court pour se vérifier à la main, assez "
                  u"long pour qu'on ne le fasse pas.",
     limite=u"L'exercice compte les écarts de câblage. Il ne dit rien des "
            u"valeurs, des types ni des composants choisis — un graphe "
            u"conforme au câblage près peut encore être faux. Compter est "
            u"la première vérification, pas la seule.",
     mode=u"SingleValue", tol=u"0", nb=7,
     comp=u"Nombre, Equality, Cull Pattern, List Length, Panel",
     etapes=[u"Mettre les deux relevés en regard, liaison par liaison.",
             u"Comparer les indices d'entrée, et non les seuls noms.",
             u"Compter les désaccords.",
             u"Ne conclure à la conformité qu'après avoir aussi vérifié "
             u"qu'aucune liaison ne manque."],
     pieges=[u"Comparer les noms des composants et s'arrêter là.",
             u"Se fier à l'aperçu, qui est plausible.",
             u"Conclure de « neuf liaisons des deux côtés » à « graphe "
             u"conforme »."],
     var=[u"Reprendre la spécification et faire corriger l'agent, puis "
          u"recompter.",
          u"Écrire la vérification comme une étape automatique du pont, "
          u"exécutée après chaque construction."],
     gamif=u"G-20 Contre-expertise",
     bareme=u"1 point si le nombre de divergences est juste.",
     verdict=u"competence"),

dict(id=u"IA-16", titre=u"Ce qu'un agent ne fait pas sans vous",
     them=u"IA7 · Agents et protocoles",
     ref=u"REF-138",
     niv=u"Perfectionnement", duree=8, prereq=u"IA-15",
     competence=u"—", bloom=u"Évaluer × conceptuelle",
     contexte=u"L'agent pilote Grasshopper et Rhino par un pont ouvert sur "
              u"votre poste. Il a accès au document, aux fichiers, et à ce "
              u"que vous lui laissez.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Vous ouvrez un pont agentique sur votre poste de travail. "
               u"Quel garde-fou pose-t-on en premier ?\n"
               u"a) Relire chaque commande avant de la laisser passer.\n"
               u"b) Travailler sur une copie du document, et exiger une "
               u"confirmation pour tout ce qui écrit hors de cette "
               u"copie. ← réponse\n"
               u"c) Limiter l'agent aux composants natifs.\n"
               u"d) Journaliser les appels pour pouvoir les rejouer.\n\n"
               u"Valeur diagnostique : (a) est le réflexe naturel et il ne "
               u"tient pas — un agent émet des dizaines d'appels par minute, "
               u"personne ne les relit. (d) est utile mais ne protège de "
               u"rien : un journal se lit après. (c) confond la puissance de "
               u"l'agent et son droit d'écriture. Le seul garde-fou qui "
               u"tienne est celui qui reste efficace quand on cesse de "
               u"regarder : borner ce qui est réversible, et faire "
               u"confirmer le reste."),

dict(id=u"IA-17", titre=u"Une commande cachée dans un courriel",
     them=u"IA6 · Modèles de langage et IA générative",
     ref=u"REF-134",
     niv=u"Perfectionnement", duree=30, prereq=u"IA-11",
     competence=u"Extraire d'un texte libre les données chiffrées qui "
                u"engagent, en distinguant ce qui est commandé de ce qui est "
                u"seulement évoqué.",
     bloom=u"Analyser × procédurale",
     contexte=u"Le conducteur de travaux commande sa quincaillerie par "
              u"courriel, en une phrase par ligne et sans tableau. La "
              u"commande doit en sortir chiffrée.",
     obj=u"Extraire d'un texte libre les données chiffrées qui engagent, en "
         u"distinguant ce qui est commandé de ce qui est seulement évoqué.",
     enonce=u"Le courriel vous est fourni tel qu'il a été reçu. Donnez le "
            u"nombre total de pièces réellement commandées.",
     depart=u"Le courriel du conducteur de travaux, en texte libre.",
     att=u"96 pièces — 24 paumelles, 48 vis, 18 poignées et 6 serrures.",
     erreur=u"Additionner tout ce qui ressemble à une quantité. On obtient "
            u"alors 138 : les 30 crémones d'une demande de PRIX y sont "
            u"comptées comme commandées, et les poignées le sont deux fois, "
            u"à leur valeur annoncée puis à leur valeur corrigée. Une "
            u"extraction qui ne distingue pas l'intention du chiffre "
            u"produit une commande fausse — et personne ne relit une "
            u"commande produite automatiquement.",
     donnees_note=u"Le courriel porte trois pièges distincts, et un seul de "
                  u"chaque sorte : une quantité écrite en toutes lettres "
                  u"(que la lecture naïve ignore, donnant 48), une "
                  u"correction plus bas dans le message (qui invite au "
                  u"double comptage), et une demande de prix (qui invite à "
                  u"commander). Les quatre résultats possibles — 96, 48, "
                  u"108 et 138 — sont tous distincts, donc chaque erreur se "
                  u"lit sans ambiguïté.",
     limite=u"L'exercice valide un total, pas la structure extraite. Une "
            u"extraction juste au total peut avoir mal attribué les "
            u"quantités : le formateur regarde la table, pas seulement la "
            u"somme.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Texte, Nombre, Mass Addition, Panel",
     etapes=[u"Repérer chaque article cité et la quantité qui l'accompagne.",
             u"Convertir les quantités écrites en lettres.",
             u"Repérer les corrections : la dernière valeur annoncée "
             u"remplace la précédente, elle ne s'y ajoute pas.",
             u"Écarter ce qui n'est pas une commande.",
             u"Sommer."],
     pieges=[u"Ignorer la quantité écrite en toutes lettres.",
             u"Additionner la valeur annoncée et sa correction.",
             u"Commander ce qui faisait l'objet d'une demande de prix."],
     var=[u"Rendre la table structurée article par article, et non le seul "
          u"total.",
          u"Reprendre le même courriel avec deux corrections successives "
          u"sur le même article."],
     gamif=u"G-18 Dictée technique",
     bareme=u"1 point si le total est juste.",
     verdict=u"competence"),

dict(id=u"IA-18", titre=u"Ce qu'une image générée ne vous donne pas",
     them=u"IA6 · Modèles de langage et IA générative",
     ref=u"REF-135",
     niv=u"Perfectionnement", duree=8, prereq=u"IA-17",
     competence=u"—", bloom=u"Évaluer × conceptuelle",
     contexte=u"Le client a apporté une image générée qui lui plaît "
              u"beaucoup, et demande « le même » en trois dimensions.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Un client apporte une image générée et demande le modèle "
               u"correspondant. Qu'en tirez-vous réellement ?\n"
               u"a) Une intention de forme et de matière, à traduire en "
               u"cotes et en constructibilité. ← réponse\n"
               u"b) Une géométrie, qu'un outil de reconstruction saura "
               u"extraire.\n"
               u"c) Rien d'exploitable : mieux vaut repartir d'un croquis.\n"
               u"d) Une référence de style, à condition d'en avoir les "
               u"droits.\n\n"
               u"Valeur diagnostique : (b) est l'erreur coûteuse — les "
               u"outils de reconstruction rendent une surface, jamais des "
               u"cotes, et une image générée n'a aucune raison d'être "
               u"cohérente d'une vue à l'autre. (c) jette ce qui a de la "
               u"valeur : l'image dit une intention, et c'est beaucoup. "
               u"(d) est un vrai sujet, mais il vient après. Ce que "
               u"l'image ne porte pas est ce qui fait le projet : "
               u"dimensions, épaisseurs, assemblages, et la question de "
               u"savoir si cela tient debout."),

]
