# -*- coding: utf-8 -*-
"""Vague 2, seconde partie : lots PL, DV et IA.

UN AVERTISSEMENT SUR LE LOT PL
------------------------------
La categorie « Ecosysteme de plugins » compte onze notions, dont sept nomment
un plugin precis. Ecrire des exercices qui affirment ce que fait chacun serait
risque : je ne les ai pas tous sous la main, et un exercice qui se trompe sur
le comportement d'un outil est pire qu'un exercice absent.

Les huit exercices portent donc sur ce qui se verifie et se mesure : la
FERMETURE des dependances, la portabilite d'une definition qui en depend, le
choix entre un plugin et une chaine native, la compatibilite des versions, et
la lisibilite d'une definition. Les notions qui nomment un plugin leur sont
rattachees : la fiche invite a les essayer, l'exercice ne prejuge pas de leur
interface. Les noms de paquets des exercices PL-05 et PL-06 sont neutres et
donnes comme tels — ce qui est evalue est le raisonnement sur un graphe de
dependances, pas la memoire d'un catalogue.

TOUTES LES VALEURS SONT CALCULEES par `verifier_vague2.py`.
"""

# ---------------------------------------------------------------------------
# Jeux de donnees
# ---------------------------------------------------------------------------

#: PL-05 — un graphe de dependances, tel que le gestionnaire de paquets le
#: declare. Noms neutres a dessein.
D_PL05_DEPENDANCES = {
    u"Nid": [u"Trame", u"Aiguille"],
    u"Trame": [u"Noyau"],
    u"Aiguille": [u"Noyau", u"Sillage"],
    u"Sillage": [u"Fontaine"],
    u"Fontaine": [],
    u"Noyau": [],
    u"Cadran": [u"Noyau"],
}
D_PL05_CIBLE = u"Nid"

#: PL-06 — qui pourra ouvrir la definition livree
D_PL06_REQUIS = [u"Trame", u"Sillage", u"Cadran"]
D_PL06_POSTES = [
    (u"Bureau A", [u"Trame", u"Sillage", u"Cadran", u"Nid"]),
    (u"Bureau B", [u"Trame", u"Cadran"]),
    (u"Atelier", [u"Trame", u"Sillage", u"Cadran"]),
    (u"Client 1", []),
    (u"Client 2", [u"Sillage", u"Cadran", u"Fontaine"]),
    (u"Sous-traitant", [u"Trame", u"Sillage", u"Cadran", u"Fontaine"]),
    (u"Chantier", [u"Trame"]),
]

#: PL-07 — cinq taches, en natif et avec le plugin qui va bien
D_PL07_TACHES = [
    (u"Imbrication 2D", 34, 1), (u"Relaxation", 41, 2),
    (u"Lecture d'un tableur", 12, 1), (u"Maillage adaptatif", 27, 3),
    (u"Export d'une nomenclature", 9, 1),
]

#: PL-08 — les surnoms releves sur une definition. True = le surnom dit ce
#: que le composant fait ; False = il faut remonter le cable pour le savoir.
D_PL08_SURNOMS = [
    (u"Largeur du caisson", True), (u"A", False), (u"Hauteur libre", True),
    (u"Srf", False), (u"Nombre de tablettes", True), (u"D", False),
    (u"Epaisseur du panneau", True), (u"Mult", False), (u"Jeu de pose", True),
    (u"X", False), (u"Volume de bois", True), (u"Div", False),
    (u"Prix au metre cube", True), (u"N", False), (u"Cout matiere", True),
    (u"Rot", False), (u"Angle de chant", True), (u"Pt", False),
    (u"Longueur de chant", True), (u"Vec", False),
    (u"Surface de placage", True), (u"Nombre de percages", True),
    (u"Entraxe des percages", True), (u"Diametre de percage", True),
]

#: PL-09 — la version de Rhino que chaque plugin exige
D_PL09_PLUGINS = [
    (u"Trame", 7), (u"Aiguille", 8), (u"Sillage", 6), (u"Cadran", 8),
    (u"Fontaine", 5), (u"Noyau", 7), (u"Nid", 8), (u"Meridien", 9),
    (u"Vasque", 9),
]
D_PL09_CIBLE = 8

#: DV-08 — un arbre a deux niveaux de chemin
D_DV08 = dict(niveau_a=3, niveau_b=4)

#: DV-09 — les valeurs a diviser, et le diviseur
D_DV09_VALEURS = [7, 13, 22, 5, 18, 31, 9, 26, 14, 3]
D_DV09_DIVISEUR = 4

#: IA-19 — les debits releves, et les deux seuils de regroupement
D_IA19_DEBITS = [412, 88, 1240, 355, 67, 980, 1510, 210, 45, 720, 1330, 168,
                 890, 52, 1105, 298, 640, 1420, 75, 505, 1180, 130, 830, 385]
D_IA19_SEUILS = (300, 900)

#: IA-20 — le budget d'une campagne d'evaluations
D_IA20 = dict(budget_heures=6.0, duree_seconde=42.0, parametres=12, niveaux=5)

#: IA-21 — une file de poteaux
D_IA21 = dict(longueur=18600.0, entraxe_max=2500.0)

#: IA-22 — des demi-unites a arrondir
D_IA22_VALEURS = [12.5, 7.5, 3.5, 18.5, 24.5, 9.5, 15.5, 2.5,
                  21.5, 6.5, 11.5, 30.5]

#: IA-23 — les cas qui passent, tour d'agent apres tour d'agent
D_IA23_TOURS = [(1, 7), (2, 12), (3, 16), (4, 18), (5, 18)]
D_IA23_CIBLE = 18

#: IA-25 — la consommation mensuelle d'un service, et ses tarifs
D_IA25 = dict(requetes=4200, jetons_entree=1850, jetons_sortie=320,
              prix_entree=3.0, prix_sortie=15.0)


# ---------------------------------------------------------------------------
# Lot PL — ecosysteme de plugins
# ---------------------------------------------------------------------------

LOT_PL = [

dict(id=u"PL-05", titre=u"Ce qu'un plugin traîne derrière lui",
     them=u"PL1 · Écosystème de plugins",
     ref=u"REF-029, REF-030",
     niv=u"Intermédiaire", duree=20, prereq=u"PL-02",
     competence=u"Établir la liste complète des paquets qu'une installation "
                u"suppose, en suivant les dépendances jusqu'au bout.",
     bloom=u"Analyser × procédurale",
     contexte=u"Le poste du chantier n'a pas Internet. Ce qui n'est pas "
              u"emporté sur la clé ne sera pas installé.",
     obj=u"Établir la liste complète des paquets qu'une installation "
         u"suppose, en suivant les dépendances jusqu'au bout.",
     enonce=u"Le tableau des dépendances déclarées vous est fourni. Donnez "
            u"le nombre total de paquets à emporter pour installer Nid, "
            u"celui-ci compris.",
     depart=u"Le tableau des dépendances : pour chaque paquet, ceux qu'il "
            u"exige.",
     att=u"6 paquets — Nid, plus les cinq dont il dépend directement ou "
         u"indirectement.",
     erreur=u"S'arrêter aux dépendances DIRECTES et n'en emporter que trois. "
            u"Trame et Aiguille en exigent d'autres, qui en exigent encore : "
            u"la chaîne fait trois niveaux. Sur un poste sans réseau, "
            u"l'installation s'arrête au premier maillon manquant, et le "
            u"message ne nomme que celui-là.",
     donnees_note=u"Le graphe fait trois niveaux de profondeur et comporte "
                  u"un paquet exigé par DEUX autres — Noyau — qu'il ne faut "
                  u"compter qu'une fois. Les réponses fausses plausibles "
                  u"sont 3 (les directes) et 7 (Noyau compté deux fois) : "
                  u"toutes deux distinctes de 6. Les noms sont neutres à "
                  u"dessein — ce qui est évalué est le parcours du graphe, "
                  u"pas la mémoire d'un catalogue.",
     limite=u"Six paquets, c'est ce que déclare le graphe de dépendances. "
            u"Un plugin peut en exiger d'autres au premier lancement — "
            u"licence, runtime, redistribuable — que sa déclaration ne "
            u"mentionne pas. Le compte est un minorant.",
     mode=u"SingleValue", tol=u"0", nb=7,
     comp=u"Texte, Member Index, Create Set, List Length, Panel",
     etapes=[u"Relever les dépendances directes du paquet visé.",
             u"Relever celles de chacune, et ainsi de suite.",
             u"Écarter les doublons.",
             u"Ajouter le paquet lui-même."],
     pieges=[u"S'arrêter au premier niveau.",
             u"Compter deux fois un paquet exigé par deux autres."],
     var=[u"Faire la même liste pour Cadran, et mesurer ce que les deux "
          u"installations partagent.",
          u"Repérer les paquets dont plus rien ne dépend."],
     gamif=u"G-06 Valise de chantier",
     bareme=u"1 point si le compte total est juste.",
     verdict=u"competence"),

dict(id=u"PL-06", titre=u"Qui pourra ouvrir votre définition",
     them=u"PL1 · Écosystème de plugins",
     ref=u"REF-038, REF-039",
     niv=u"Intermédiaire", duree=20, prereq=u"PL-05",
     competence=u"Mesurer ce qu'une dépendance à des plugins coûte en "
                u"portabilité, avant de livrer.",
     bloom=u"Évaluer × procédurale",
     contexte=u"La définition part chez sept destinataires. Chez ceux qui "
              u"n'ont pas les plugins, elle s'ouvrira — avec des composants "
              u"rouges à la place du calcul.",
     obj=u"Mesurer ce qu'une dépendance à des plugins coûte en portabilité, "
         u"avant de livrer.",
     enonce=u"Votre définition exige trois plugins. L'inventaire des sept "
            u"postes destinataires vous est fourni. Donnez le nombre de "
            u"postes qui pourront l'exécuter.",
     depart=u"Les trois plugins requis, et pour chacun des sept postes la "
            u"liste de ceux qu'il possède.",
     att=u"3 postes sur 7 pourront l'exécuter.",
     erreur=u"Compter les postes qui possèdent AU MOINS UN des trois "
            u"plugins : six sur sept, et la livraison paraît sans risque. "
            u"Il les faut TOUS LES TROIS — un composant manquant suffit à "
            u"rompre la chaîne, et la définition ne rend alors rien.",
     donnees_note=u"Sept postes, dont un qui n'a rien, un qui a tout et "
                  u"plus, et quatre qui ont une partie : la différence entre "
                  u"« au moins un » (6) et « tous » (3) est du simple au "
                  u"double, et c'est exactement l'écart entre l'impression "
                  u"que la livraison passera et la réalité.",
     limite=u"Le compte suppose que posséder le plugin suffit. Une version "
            u"incompatible se compte comme une absence — c'est l'objet de "
            u"PL-09.",
     mode=u"SingleValue", tol=u"0", nb=8,
     comp=u"Texte, Member Index, Equality, Cull Pattern, List Length, Panel",
     etapes=[u"Pour chaque poste, vérifier la présence des TROIS plugins.",
             u"Ne retenir que ceux qui les ont tous.",
             u"Compter."],
     pieges=[u"Se contenter d'une intersection non vide.",
             u"Oublier qu'un plugin en trop ne compense pas un plugin "
             u"manquant."],
     var=[u"Trouver le plugin dont l'abandon rendrait la définition "
          u"portable au plus grand nombre.",
          u"Chiffrer ce que coûterait de refaire en natif la part "
          u"dépendante."],
     gamif=u"G-17 Passation",
     bareme=u"1 point si le compte des postes capables est juste.",
     verdict=u"competence"),

dict(id=u"PL-07", titre=u"Ce qu'un plugin vous épargne d'écrire",
     them=u"PL1 · Écosystème de plugins",
     ref=u"REF-038, REF-039",
     niv=u"Intermédiaire", duree=20, prereq=u"PL-04",
     competence=u"Chiffrer ce qu'un plugin fait gagner en construction, pour "
                u"le mettre en regard de ce qu'il coûte en dépendance.",
     bloom=u"Évaluer × procédurale",
     contexte=u"La question n'est jamais « ce plugin est-il bon ». Elle est "
              u"« ce qu'il m'épargne vaut-il ce qu'il m'impose ».",
     obj=u"Chiffrer ce qu'un plugin fait gagner en construction, pour le "
         u"mettre en regard de ce qu'il coûte en dépendance.",
     enonce=u"Cinq tâches vous sont données, avec le nombre de composants "
            u"qu'elles demandent en natif et avec le plugin adapté. Donnez "
            u"le nombre de composants économisés au total.",
     depart=u"Les cinq tâches, et pour chacune le compte natif et le compte "
            u"avec plugin.",
     att=u"115 composants économisés — 123 en natif contre 8 avec plugins.",
     erreur=u"Rendre le compte avec plugins (8) ou le compte natif (123) au "
            u"lieu de l'écart. C'est l'ÉCART qui se met en balance avec le "
            u"coût de la dépendance mesuré en PL-06 : 115 composants "
            u"épargnés contre quatre postes sur sept qui ne pourront plus "
            u"ouvrir le fichier.",
     donnees_note=u"Les rapports vont de 9 contre 1 à 34 contre 1 selon la "
                  u"tâche : le gain n'est pas uniforme, et l'exercice se "
                  u"prolonge naturellement en « lequel des cinq mérite "
                  u"vraiment sa dépendance ».",
     limite=u"Le nombre de composants n'est qu'un indice. Un plugin peut "
            u"épargner peu de composants et beaucoup de justesse — une "
            u"imbrication écrite à la main est fausse avant d'être longue.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Nombre, Mass Addition, Subtraction, Panel",
     etapes=[u"Sommer les comptes natifs.",
             u"Sommer les comptes avec plugins.",
             u"Soustraire."],
     pieges=[u"Rendre l'un des deux totaux.",
             u"Conclure du gain seul, sans regarder ce que la dépendance "
             u"coûte."],
     var=[u"Classer les cinq tâches par rapport gain sur dépendance.",
          u"Reprendre en comptant les heures plutôt que les composants."],
     gamif=u"G-21 Optimisation comparée",
     bareme=u"1 point si l'économie totale est juste.",
     verdict=u"competence"),

dict(id=u"PL-08", titre=u"Les composants qui ne disent pas leur nom",
     them=u"PL1 · Écosystème de plugins",
     ref=u"REF-031, REF-032, REF-033",
     niv=u"Intermédiaire", duree=20, prereq=u"PL-03",
     competence=u"Repérer, dans une définition, ce qu'un relecteur ne "
                u"pourra pas comprendre sans remonter les câbles.",
     bloom=u"Évaluer × conceptuelle",
     contexte=u"Les plugins d'ergonomie affichent les noms, alignent, "
              u"colorent. Ils ne remplacent pas le fait de nommer : ils "
              u"rendent visible qu'on ne l'a pas fait.",
     obj=u"Repérer, dans une définition, ce qu'un relecteur ne pourra pas "
         u"comprendre sans remonter les câbles.",
     enonce=u"Les vingt-quatre surnoms relevés sur la définition vous sont "
            u"fournis. Donnez le nombre de composants dont le surnom ne dit "
            u"pas ce qu'ils font.",
     depart=u"Les vingt-quatre surnoms, tels qu'ils apparaissent sur le "
            u"canevas.",
     att=u"10 surnoms ne disent rien de ce que le composant fait.",
     erreur=u"Compter les surnoms COURTS. « Pt » et « Vec » sont courts et "
            u"muets, mais « Jeu de pose » est court et parlant, tandis "
            u"qu'un surnom long et générique ne vaudrait pas mieux que "
            u"« A ». Ce qui se juge est ce que le surnom APPREND, pas sa "
            u"longueur.",
     donnees_note=u"Dix surnoms muets sur vingt-quatre, soit plus de quatre "
                  u"sur dix — la proportion ordinaire d'une définition "
                  u"écrite sans intention de la faire relire. Les muets se "
                  u"répartissent en deux familles : six abréviations de "
                  u"composants (Srf, Mult, Div, Rot, Pt, Vec) et quatre "
                  u"lettres seules (A, D, X, N). Deux familles, pour qu'un "
                  u"critère de longueur seul ne suffise pas à les trouver.",
     limite=u"L'exercice compte. Il ne renomme pas — et renommer est le "
            u"vrai travail, qui se juge en MP-01.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Texte, Booléen, Cull Pattern, List Length, Panel",
     etapes=[u"Lire chaque surnom en se demandant ce qu'il apprend à qui "
             u"n'a pas écrit la définition.",
             u"Écarter le critère de longueur.",
             u"Compter les muets."],
     pieges=[u"Juger sur la longueur.",
             u"Considérer qu'un nom de composant par défaut est acceptable "
             u"parce qu'il est exact."],
     var=[u"Proposer un surnom parlant pour chacun des dix.",
          u"Installer un plugin d'affichage des noms et refaire la lecture."],
     gamif=u"G-17 Passation",
     bareme=u"1 point si le compte des surnoms muets est juste.",
     verdict=u"competence"),

dict(id=u"PL-09", titre=u"Ce qui s'installera vraiment sur ce poste",
     them=u"PL1 · Écosystème de plugins",
     ref=u"REF-030",
     niv=u"Intermédiaire", duree=15, prereq=u"PL-02",
     competence=u"Confronter les exigences de version d'un ensemble de "
                u"plugins à la version installée, avant de promettre une "
                u"configuration.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le poste tourne sous Rhino 8. La liste des plugins souhaités "
              u"vient d'ailleurs, et chacun annonce la version qu'il exige.",
     obj=u"Confronter les exigences de version d'un ensemble de plugins à la "
         u"version installée, avant de promettre une configuration.",
     enonce=u"Les neuf plugins vous sont fournis avec la version de Rhino "
            u"qu'ils exigent au minimum. Le poste tourne sous Rhino 8. "
            u"Donnez le nombre de plugins installables.",
     depart=u"Les neuf plugins et la version minimale exigée par chacun.",
     att=u"7 plugins sur 9 sont installables sur Rhino 8.",
     erreur=u"Ne retenir que ceux qui annoncent exactement 8 — il y en a "
            u"trois. Une version minimale est un PLANCHER : un plugin écrit "
            u"pour Rhino 6 s'installe sur Rhino 8. Ce sont les deux qui "
            u"exigent Rhino 9 qui ne passeront pas.",
     donnees_note=u"Neuf plugins répartis de Rhino 5 à Rhino 9, dont trois "
                  u"exactement à 8 : la lecture « exactement » donne 3, la "
                  u"lecture « au moins » donne 7, et la lecture « tous sauf "
                  u"le plus récent » donne 8. Trois réponses distinctes pour "
                  u"trois façons de se tromper.",
     limite=u"Une version minimale ne garantit pas la compatibilité vers le "
            u"haut : un plugin écrit pour Rhino 6 peut ne plus fonctionner "
            u"sous Rhino 8. L'exercice traite ce que le catalogue déclare, "
            u"pas ce que l'exécution révèle.",
     mode=u"SingleValue", tol=u"0", nb=5,
     comp=u"Nombre, Smaller Than, Cull Pattern, List Length, Panel",
     etapes=[u"Comprendre que la version déclarée est un minimum.",
             u"Comparer chaque exigence à la version du poste.",
             u"Compter."],
     pieges=[u"Chercher l'égalité exacte.",
             u"Supposer qu'un plugin ancien ne fonctionnera pas."],
     var=[u"Trouver la version de Rhino qui permettrait d'installer les "
          u"neuf.",
          u"Croiser avec les dépendances de PL-05."],
     gamif=u"G-06 Valise de chantier",
     bareme=u"1 point si le compte est juste.",
     verdict=u"competence"),

dict(id=u"PL-10", titre=u"Où chercher un plugin",
     them=u"PL1 · Écosystème de plugins",
     ref=u"REF-029, REF-030",
     niv=u"Intermédiaire", duree=8, prereq=u"PL-02",
     competence=u"—", bloom=u"Comprendre × conceptuelle",
     contexte=u"Un plugin est disponible à la fois sur le site "
              u"communautaire et dans le gestionnaire de paquets intégré.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Un plugin est proposé des deux côtés. Par lequel "
               u"l'installez-vous, et pourquoi ?\n"
               u"a) Le site communautaire : on y trouve la version la plus "
               u"récente.\n"
               u"b) Le gestionnaire de paquets : il gère les dépendances, "
               u"les versions et la désinstallation. ← réponse\n"
               u"c) Peu importe, le fichier installé est le même.\n"
               u"d) Le site communautaire, pour lire les avis avant "
               u"d'installer.\n\n"
               u"Valeur diagnostique : (c) est vrai du seul fichier et faux "
               u"de tout le reste — ce qui distingue les deux voies n'est "
               u"pas le binaire, c'est ce qui l'entoure : les dépendances "
               u"tirées automatiquement, la mise à jour qui remplace "
               u"vraiment, et la désinstallation qui nettoie. (a) et (d) "
               u"décrivent de bonnes raisons de CONSULTER le site, pas d'y "
               u"télécharger."),

dict(id=u"PL-11", titre=u"Deux familles de plugins",
     them=u"PL1 · Écosystème de plugins",
     ref=u"REF-031, REF-034, REF-035, REF-036, REF-037",
     niv=u"Intermédiaire", duree=8, prereq=u"PL-03",
     competence=u"—", bloom=u"Comprendre × conceptuelle",
     contexte=u"Certains plugins ajoutent des composants ; d'autres ne "
              u"changent que la façon dont on travaille.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Qu'est-ce qui sépare un plugin d'ERGONOMIE d'un plugin "
               u"FONCTIONNEL, pour celui qui recevra votre définition ?\n"
               u"a) L'ergonomie est gratuite, le fonctionnel est payant.\n"
               u"b) L'ergonomie ne laisse aucune trace dans le fichier "
               u"livré ; le fonctionnel devient une dépendance. ← "
               u"réponse\n"
               u"c) L'ergonomie est réservée aux débutants.\n"
               u"d) Le fonctionnel est plus lourd à installer.\n\n"
               u"Valeur diagnostique : la question ne porte pas sur ce que "
               u"le plugin fait pour VOUS, mais sur ce qu'il impose à "
               u"l'autre. Un plugin qui aligne, colore ou affiche les noms "
               u"peut être désinstallé sans qu'aucune définition cesse de "
               u"fonctionner. Un plugin qui ajoute un composant est dans le "
               u"fichier, et le suit partout — c'est ce que PL-06 mesure."),

dict(id=u"PL-12", titre=u"Le plugin qui n'est plus maintenu",
     them=u"PL1 · Écosystème de plugins",
     ref=u"REF-039",
     niv=u"Intermédiaire", duree=8, prereq=u"PL-11",
     competence=u"—", bloom=u"Évaluer × conceptuelle",
     contexte=u"Le plugin sur lequel repose une définition de production "
              u"n'a pas été mis à jour depuis trois ans.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Une définition de production dépend d'un plugin abandonné "
               u"depuis trois ans. Que faites-vous en premier ?\n"
               u"a) Chercher un plugin de remplacement équivalent.\n"
               u"b) Repérer ce que ce plugin fait réellement dans la "
               u"définition, et si c'est encore indispensable. ← réponse\n"
               u"c) Figer la version de Rhino pour que rien ne bouge.\n"
               u"d) Réécrire la partie concernée en natif, sans attendre.\n\n"
               u"Valeur diagnostique : (c) est la réaction la plus "
               u"répandue, et c'est un report de décision — figer Rhino "
               u"gèle aussi tout le reste, et le problème revient dans un "
               u"an, aggravé. (a) et (d) sont des solutions, mais on ne "
               u"choisit pas une solution avant de savoir ce qu'on "
               u"remplace : sur une définition ancienne, il est fréquent "
               u"que le plugin ne serve plus qu'à une étape devenue "
               u"inutile."),

]


# ---------------------------------------------------------------------------
# Lot DV — developpement, scripting et API
# ---------------------------------------------------------------------------

LOT_DV = [

dict(id=u"DV-08", titre=u"Ce que le remappage fait aux branches",
     them=u"DV2 · API et librairies",
     ref=u"REF-105",
     niv=u"Expert", duree=25, prereq=u"DV-03",
     competence=u"Prévoir la structure d'un arbre après un remappage de "
                u"chemins, en raisonnant sur les chemins plutôt que sur les "
                u"données.",
     bloom=u"Analyser × conceptuelle",
     contexte=u"Le composant scripté reçoit un arbre à deux niveaux et doit "
              u"rendre un résultat par valeur du second niveau, toutes "
              u"origines confondues.",
     obj=u"Prévoir la structure d'un arbre après un remappage de chemins, en "
         u"raisonnant sur les chemins plutôt que sur les données.",
     enonce=u"L'arbre porte trois valeurs au premier niveau de chemin et "
            u"quatre au second, soit une branche par combinaison. Le "
            u"remappage ne conserve que le second niveau. Donnez le nombre "
            u"de branches obtenues.",
     depart=u"La structure de l'arbre de départ et la règle de remappage.",
     att=u"4 branches — une par valeur du second niveau.",
     erreur=u"Répondre 3, en conservant le mauvais maillon, ou 12 en "
            u"supposant que le remappage ne change rien. Un remappage qui "
            u"laisse tomber un niveau FUSIONNE les branches qui ne "
            u"différaient que par lui : douze branches deviennent quatre, et "
            u"chacune porte désormais trois fois plus de données.",
     donnees_note=u"Trois et quatre sont premiers entre eux, de sorte que "
                  u"les trois réponses — 3, 4 et 12 — sont toutes "
                  u"distinctes et qu'aucune n'est un multiple trompeur des "
                  u"autres.",
     limite=u"Le compte des branches ne dit rien de leur CONTENU ni de "
            u"l'ordre dans lequel les données s'y retrouvent — qui dépend de "
            u"l'ordre de parcours, et se relève plutôt qu'il ne se devine.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Series, Cross Reference, Path Mapper, Tree Statistics, Panel",
     etapes=[u"Compter les branches de départ : le produit des deux "
             u"niveaux.",
             u"Comprendre que le remappage retire un niveau du chemin.",
             u"Compter les chemins distincts qui subsistent."],
     pieges=[u"Conserver le mauvais niveau.",
             u"Croire qu'un remappage ne change que l'étiquette."],
     var=[u"Donner le nombre d'éléments par branche après remappage.",
          u"Reprendre avec un aplatissement complet."],
     gamif=u"G-09 Arbre relu",
     bareme=u"1 point si le nombre de branches est juste.",
     verdict=u"competence"),

dict(id=u"DV-09", titre=u"La division qui n'est pas celle qu'on croit",
     them=u"DV1 · Scripting dans Grasshopper",
     ref=u"REF-100, REF-102",
     niv=u"Expert", duree=25, prereq=u"DV-01",
     competence=u"Anticiper le comportement d'un opérateur selon le TYPE de "
                u"ses opérandes, dans un composant scripté.",
     bloom=u"Analyser × procédurale",
     contexte=u"Le script calcule combien de panneaux entiers chaque pièce "
              u"consomme. Les quantités sont des entiers, et l'opérateur de "
              u"division aussi.",
     obj=u"Anticiper le comportement d'un opérateur selon le type de ses "
         u"opérandes, dans un composant scripté.",
     enonce=u"Le script divise chacune des dix quantités par 4 et somme les "
            u"résultats. Les quantités et le diviseur sont déclarés comme "
            u"des ENTIERS. Donnez la somme rendue par le script.",
     depart=u"Les dix quantités, le diviseur, et le type déclaré des "
            u"variables.",
     att=u"32 — la somme des quotients entiers.",
     erreur=u"Calculer en réel et rendre 37. Sur des entiers, la division "
            u"tronque : 7 ÷ 4 donne 1 et non 1,75. L'écart de 5 est ici "
            u"visible, mais le même script rendrait un résultat plausible "
            u"sur d'autres données — et c'est ce qui rend l'erreur "
            u"durable.",
     donnees_note=u"Dix quantités dont aucune n'est multiple de 4 : la "
                  u"troncature agit à chaque terme, et l'écart s'accumule "
                  u"au lieu de se compenser. Les deux réponses, 32 et 37, "
                  u"sont assez proches pour paraître toutes deux "
                  u"crédibles — c'est exactement le danger.",
     limite=u"Ce que le script doit rendre dépend du métier : pour des "
            u"panneaux entiers, la troncature est peut-être juste, ou "
            u"peut-être faut-il arrondir au supérieur. L'exercice porte sur "
            u"ce que le langage FAIT, pas sur ce qu'il faudrait vouloir.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Nombre, Division, Round, Mass Addition, Panel",
     etapes=[u"Diviser chaque quantité en respectant le type entier.",
             u"Sommer.",
             u"Comparer au résultat qu'aurait donné une division réelle."],
     pieges=[u"Diviser en réel.",
             u"Arrondir au lieu de tronquer : sur ces données les deux "
             u"diffèrent."],
     var=[u"Reprendre en déclarant les variables en réel et mesurer "
          u"l'écart.",
          u"Rendre le nombre de panneaux réellement nécessaires, arrondi au "
          u"supérieur."],
     gamif=u"G-15 Relecture de code",
     bareme=u"1 point si la somme des quotients entiers est juste.",
     verdict=u"competence"),

]


# ---------------------------------------------------------------------------
# Lot IA — IA et assistance generative
# ---------------------------------------------------------------------------

LOT_IA = [

dict(id=u"IA-19", titre=u"Regrouper un débit en trois familles",
     them=u"IA5 · Apprentissage automatique",
     ref=u"REF-130",
     niv=u"Perfectionnement", duree=25, prereq=u"IA-10",
     competence=u"Regrouper des pièces en familles de fabrication et "
                u"identifier celle qui pèse le plus dans l'organisation de "
                u"l'atelier.",
     bloom=u"Analyser × procédurale",
     contexte=u"L'atelier organise ses postes par famille de format. Le "
              u"débit arrive en vrac, et c'est la famille la plus fournie "
              u"qui dimensionne le poste.",
     obj=u"Regrouper des pièces en familles de fabrication et identifier "
         u"celle qui pèse le plus dans l'organisation de l'atelier.",
     enonce=u"Les vingt-quatre longueurs du débit vous sont fournies. Les "
            u"familles sont : petit sous 300 mm, moyen jusqu'à 900 mm exclus, "
            u"grand au-delà. Donnez l'effectif de la famille la plus "
            u"fournie.",
     depart=u"Les vingt-quatre longueurs, en millimètres, et les deux "
            u"seuils.",
     att=u"9 pièces — l'effectif de la famille des petits.",
     erreur=u"Rendre le nombre de familles (3), ou l'effectif de la famille "
            u"des grands, qu'on suppose la plus nombreuse parce qu'elle "
            u"occupe le plus de place. Les grands sont sept, les moyens "
            u"huit : c'est la famille des PETITS qui est la plus fournie, et "
            u"c'est contre-intuitif — la place occupée n'est pas l'effectif.",
     donnees_note=u"Neuf, huit et sept : les trois effectifs sont proches, "
                  u"de sorte que la réponse ne se devine pas d'un coup "
                  u"d'œil et qu'un comptage approximatif se trompe de "
                  u"famille. Les longueurs vont de 45 à 1 510 mm, l'étendue "
                  u"ordinaire d'un débit de mobilier.",
     limite=u"Les seuils sont donnés. Les TROUVER — c'est-à-dire laisser un "
            u"regroupement automatique les proposer — est l'étape suivante, "
            u"et elle demande de juger si les familles obtenues ont un sens "
            u"pour l'atelier.",
     mode=u"SingleValue", tol=u"0", nb=8,
     comp=u"Nombre, Smaller Than, Cull Pattern, List Length, Sort List, "
          u"Panel",
     etapes=[u"Classer chaque pièce selon les deux seuils.",
             u"Compter chaque famille.",
             u"Prendre le plus grand effectif."],
     pieges=[u"Rendre le nombre de familles.",
             u"Placer mal la borne : « jusqu'à 900 exclus » n'est pas "
             u"« jusqu'à 900 ».",
             u"Supposer la réponse au lieu de compter."],
     var=[u"Donner les trois effectifs.",
          u"Chercher les seuils qui équilibreraient les trois familles."],
     gamif=u"G-04 Comptage réfléchi",
     bareme=u"1 point si l'effectif de la famille la plus fournie est "
            u"juste.",
     verdict=u"competence"),

dict(id=u"IA-20", titre=u"Ce qu'un budget de calcul permet d'essayer",
     them=u"IA5 · Apprentissage automatique",
     ref=u"REF-131, REF-132",
     niv=u"Perfectionnement", duree=30, prereq=u"IA-09",
     competence=u"Dimensionner une campagne d'évaluations à partir du temps "
                u"disponible, et mesurer l'écart avec ce qu'exigerait "
                u"l'exploration exhaustive.",
     bloom=u"Analyser × procédurale",
     contexte=u"Chaque évaluation demande un calcul thermique complet. On "
              u"dispose d'une nuit de machine.",
     obj=u"Dimensionner une campagne d'évaluations à partir du temps "
         u"disponible, et mesurer l'écart avec ce qu'exigerait "
         u"l'exploration exhaustive.",
     enonce=u"Le budget est de 6 heures et chaque évaluation prend "
            u"42 secondes. Donnez le nombre d'évaluations réalisables.",
     depart=u"Le budget en heures, la durée d'une évaluation, et le nombre "
            u"de paramètres et de niveaux du problème.",
     att=u"514 évaluations tiennent dans le budget.",
     erreur=u"Vouloir explorer toutes les combinaisons. Douze paramètres à "
            u"cinq niveaux font 244 millions d'évaluations, soit trois cent "
            u"vingt-cinq ans de machine. Ce n'est pas une question de "
            u"patience : c'est ce qui rend le métamodèle nécessaire plutôt "
            u"que confortable.",
     donnees_note=u"514 évaluations pour un espace de 244 millions de "
                  u"points : le budget couvre deux millionièmes de "
                  u"pour cent de l'espace. Le chiffre n'est pas là pour "
                  u"impressionner — il dit que le plan d'expériences ne "
                  u"peut pas être régulier, et qu'il faut le choisir.",
     limite=u"Le nombre d'évaluations tenables ne dit pas LESQUELLES faire. "
            u"C'est tout l'objet d'un plan d'expériences, et la qualité du "
            u"métamodèle en dépend plus que leur nombre.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Multiplication, Division, Round, Panel",
     etapes=[u"Convertir le budget en secondes.",
             u"Diviser par la durée d'une évaluation.",
             u"Arrondir à l'entier INFÉRIEUR : une évaluation entamée ne "
             u"compte pas.",
             u"Calculer, pour comparaison, la taille du plan complet."],
     pieges=[u"Arrondir au supérieur.",
             u"Oublier de convertir les heures en secondes.",
             u"Croire qu'on peut approcher l'exhaustif en optimisant le "
             u"calcul."],
     var=[u"Trouver la durée d'évaluation qui permettrait mille essais.",
          u"Comparer un plan aléatoire et un plan en hypercube latin à "
          u"budget égal."],
     gamif=u"G-13 Chronomètre",
     bareme=u"1 point si le nombre d'évaluations est juste et arrondi à "
            u"l'inférieur.",
     verdict=u"competence"),

dict(id=u"IA-21", titre=u"Le script qui compte les intervalles",
     them=u"IA2 · Composants scriptés assistés",
     ref=u"REF-121",
     niv=u"Intermédiaire", duree=25, prereq=u"IA-04",
     competence=u"Relire un script produit par un assistant en confrontant "
                u"ce qu'il compte à ce que la tâche demande.",
     bloom=u"Évaluer × procédurale",
     contexte=u"La clôture fait 18,60 m et les poteaux ne doivent pas être "
              u"espacés de plus de 2,50 m. Le script généré rend un nombre, "
              u"et il paraît raisonnable.",
     obj=u"Relire un script produit par un assistant en confrontant ce qu'il "
         u"compte à ce que la tâche demande.",
     enonce=u"La file mesure 18 600 mm et l'entraxe ne doit pas dépasser "
            u"2 500 mm. Donnez le nombre de poteaux.",
     depart=u"La longueur de la file et l'entraxe maximal admis.",
     att=u"9 poteaux — huit travées de 2 325 mm.",
     erreur=u"Rendre 8, le nombre de TRAVÉES. C'est ce que rend un script "
            u"qui divise et arrondit sans se demander ce qu'il compte. "
            u"Le résultat est plausible, l'ordre de grandeur est juste, et "
            u"il manque un poteau — celui du bout, qui est aussi celui qui "
            u"tient la clôture.",
     donnees_note=u"18 600 ÷ 2 500 vaut 7,44 : l'arrondi au supérieur donne "
                  u"8 travées, donc 9 poteaux, et l'entraxe réel tombe à "
                  u"2 325 mm. Les deux réponses possibles diffèrent d'une "
                  u"unité — l'erreur la plus fréquente en programmation, et "
                  u"celle qui passe le mieux la relecture.",
     limite=u"L'exercice suppose les deux extrémités équipées d'un poteau. "
            u"Une clôture qui vient buter contre un mur n'en a qu'un — et "
            u"c'est le genre de précision que la consigne doit porter, pas "
            u"le script.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Division, Round, Addition, Panel",
     etapes=[u"Diviser la longueur par l'entraxe maximal.",
             u"Arrondir au supérieur : c'est le nombre de TRAVÉES.",
             u"Ajouter un : les poteaux sont un de plus que les travées.",
             u"Vérifier l'entraxe réel obtenu."],
     pieges=[u"Rendre le nombre de travées.",
             u"Arrondir au plus proche, ce qui donnerait 7 travées et un "
             u"entraxe de 2 657 mm, au-delà du maximum."],
     var=[u"Reprendre pour une clôture butant sur un mur à chaque bout.",
          u"Donner la position de chaque poteau depuis l'origine."],
     gamif=u"G-15 Relecture de code",
     bareme=u"1 point si le nombre de poteaux est juste.",
     verdict=u"competence"),

dict(id=u"IA-22", titre=u"L'arrondi qui change avec le langage",
     them=u"IA2 · Composants scriptés assistés",
     ref=u"REF-123",
     niv=u"Intermédiaire", duree=25, prereq=u"IA-06",
     competence=u"Vérifier qu'un script transposé rend le même résultat que "
                u"l'original, en se méfiant des comportements par défaut.",
     bloom=u"Évaluer × procédurale",
     contexte=u"Le script de chiffrage est transposé d'un langage à un "
              u"autre. Il compile, il tourne, et le total a bougé de six "
              u"unités.",
     obj=u"Vérifier qu'un script transposé rend le même résultat que "
         u"l'original, en se méfiant des comportements par défaut.",
     enonce=u"Les douze quantités à arrondir vous sont fournies ; toutes "
            u"tombent sur une demi-unité. Le métier arrondit la demie vers "
            u"le haut. Donnez la somme des quantités arrondies selon la "
            u"règle du métier.",
     depart=u"Les douze quantités et la règle d'arrondi du métier.",
     att=u"170 — la somme des arrondis commerciaux.",
     erreur=u"Laisser l'arrondi par défaut du langage faire son office : il "
            u"rend 164. La plupart des langages arrondissent la demie vers "
            u"le nombre PAIR, pour ne pas biaiser les sommes — 2,5 donne 2 "
            u"et 3,5 donne 4. C'est statistiquement vertueux et "
            u"commercialement faux : sur douze lignes, six unités "
            u"s'évaporent, et le devis ne tombe plus juste.",
     donnees_note=u"Douze valeurs tombant toutes exactement sur la demie, "
                  u"dont six paires et six impaires : l'arrondi au pair "
                  u"descend une valeur sur deux, d'où un écart de six "
                  u"exactement. Sur des données ordinaires, l'écart serait "
                  u"nul la plupart du temps — et le défaut resterait "
                  u"invisible jusqu'au jour où il ne l'est plus.",
     limite=u"Aucune des deux règles n'est « la bonne » dans l'absolu. Ce "
            u"qui est fautif est de ne pas savoir laquelle le langage "
            u"applique, et de découvrir l'écart sur une facture.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Nombre, Addition, Round, Mass Addition, Panel",
     etapes=[u"Arrondir chaque valeur selon la règle du métier.",
             u"Sommer.",
             u"Refaire la somme avec l'arrondi par défaut du langage et "
             u"mesurer l'écart."],
     pieges=[u"Se fier à l'arrondi par défaut.",
             u"Supposer que deux langages arrondissent pareil."],
     var=[u"Retrouver l'écart sur un jeu où une valeur sur dix seulement "
          u"tombe sur la demie.",
          u"Écrire la règle du métier explicitement, sans dépendre du "
          u"langage."],
     gamif=u"G-15 Relecture de code",
     bareme=u"1 point si la somme selon la règle du métier est juste.",
     verdict=u"competence"),

dict(id=u"IA-23", titre=u"Combien de tours avant que tout passe",
     them=u"IA3 · Développement de plugins assisté",
     ref=u"REF-126",
     niv=u"Perfectionnement", duree=25, prereq=u"IA-07",
     competence=u"Piloter une itération avec un agent de code en s'appuyant "
                u"sur une batterie de cas, et savoir quand elle est finie.",
     bloom=u"Évaluer × procédurale",
     contexte=u"L'agent corrige le composant tour après tour. Sans "
              u"batterie de cas, on s'arrête quand on est fatigué.",
     obj=u"Piloter une itération avec un agent de code en s'appuyant sur une "
         u"batterie de cas, et savoir quand elle est finie.",
     enonce=u"Dix-huit cas d'essai doivent passer. Le relevé des cinq tours "
            u"d'itération vous est fourni. Donnez le numéro du premier tour "
            u"où tous les cas passent.",
     depart=u"Le nombre de cas à satisfaire, et le nombre de cas qui "
            u"passent à chaque tour.",
     att=u"4 — c'est au quatrième tour que les dix-huit cas passent.",
     erreur=u"Rendre 5, le dernier tour du relevé. Le cinquième n'a rien "
            u"amélioré : il a coûté un aller-retour pour confirmer que le "
            u"quatrième suffisait. Savoir s'arrêter fait partie de la "
            u"compétence — une itération sans critère d'arrêt ne s'arrête "
            u"pas, elle s'épuise.",
     donnees_note=u"Les cas passent 7, 12, 16, 18, 18 : la progression "
                  u"ralentit, ce qui est le profil habituel, et le palier "
                  u"final rend visible le tour de trop. Le relevé compte "
                  u"cinq tours pour que la réponse ne soit ni le premier ni "
                  u"le dernier.",
     limite=u"Dix-huit cas qui passent ne font pas un composant juste : ils "
            u"font un composant juste SUR CES CAS. La compétence suivante "
            u"est d'écrire les cas qui manquent.",
     mode=u"SingleValue", tol=u"0", nb=7,
     comp=u"Nombre, Equality, Cull Pattern, List Item, Panel",
     etapes=[u"Comparer, tour par tour, le nombre de cas qui passent à la "
             u"cible.",
             u"Retenir le PREMIER tour qui l'atteint.",
             u"Constater que les tours suivants n'apportent rien."],
     pieges=[u"Rendre le dernier tour du relevé.",
             u"Conclure qu'un composant qui passe tous les cas est juste."],
     var=[u"Estimer le coût des tours inutiles sur une série de dix "
          u"composants.",
          u"Écrire trois cas supplémentaires qui feraient échouer le "
          u"composant du quatrième tour."],
     gamif=u"G-20 Contre-expertise",
     bareme=u"1 point si le numéro du premier tour suffisant est juste.",
     verdict=u"competence"),

dict(id=u"IA-24", titre=u"Le composant qui n'apparaît pas",
     them=u"IA3 · Développement de plugins assisté",
     ref=u"REF-127",
     niv=u"Perfectionnement", duree=8, prereq=u"IA-23",
     competence=u"—", bloom=u"Analyser × conceptuelle",
     contexte=u"L'agent annonce que la compilation a réussi. Grasshopper "
              u"n'affiche aucun nouveau composant, et ne dit rien.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Compilation réussie, aucun composant dans l'onglet, aucun "
               u"message. Que regardez-vous en premier ?\n"
               u"a) Le code du composant : il manque sans doute une "
               u"méthode.\n"
               u"b) Où le fichier compilé a été déposé, et si Rhino "
               u"regarde ce dossier. ← réponse\n"
               u"c) La version du SDK utilisée pour compiler.\n"
               u"d) Le journal de Grasshopper, qui doit contenir "
               u"l'erreur.\n\n"
               u"Valeur diagnostique : l'absence de MESSAGE est "
               u"l'information. Un composant mal écrit produit une erreur ; "
               u"un composant que Rhino n'a jamais chargé ne produit rien. "
               u"(a) et (c) supposent que le fichier a été lu, ce que rien "
               u"n'établit. (d) est un bon réflexe, mais un journal vide "
               u"dit la même chose que le silence : personne n'a essayé de "
               u"charger quoi que ce soit."),

dict(id=u"IA-25", titre=u"Ce que le service coûte par mois",
     them=u"IA4 · Vérification, licences et limites",
     ref=u"REF-142",
     niv=u"Perfectionnement", duree=25, prereq=u"IA-13",
     competence=u"Chiffrer le coût d'usage d'un service d'IA à partir de sa "
                u"consommation réelle, en distinguant ce qui entre de ce qui "
                u"sort.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le composant appelle un service distant à chaque "
              u"recalcul. La facture arrive à la fin du mois, et personne "
              u"n'a chiffré avant.",
     obj=u"Chiffrer le coût d'usage d'un service d'IA à partir de sa "
         u"consommation réelle, en distinguant ce qui entre de ce qui sort.",
     enonce=u"Le service traite 4 200 requêtes par mois. Chacune envoie "
            u"1 850 jetons et en reçoit 320. L'entrée est facturée 3 € le "
            u"million de jetons, la sortie 15 €. Donnez le coût mensuel, en "
            u"euros.",
     depart=u"Le nombre de requêtes, les jetons échangés par requête, et les "
            u"deux tarifs.",
     att=u"43,47 € par mois.",
     erreur=u"Appliquer le même tarif à l'entrée et à la sortie : 27,34 €. "
            u"La sortie coûte cinq fois l'entrée, et c'est structurel — "
            u"elle se produit jeton par jeton. Un service qui répond peu "
            u"mais lit beaucoup ne coûte pas comme un service qui lit peu "
            u"et rédige longuement.",
     donnees_note=u"1 850 jetons en entrée pour 320 en sortie est le profil "
                  u"d'un composant qui envoie un contexte et reçoit une "
                  u"réponse courte. Malgré ce rapport de six contre un en "
                  u"volume, la sortie pèse 36 % de la facture : c'est ce "
                  u"renversement que le calcul doit faire apparaître.",
     limite=u"Le coût n'est qu'une des trois limites de la fiche. La "
            u"latence, elle, se paie à chaque recalcul et se mesure en "
            u"secondes d'attente ; la reproductibilité ne se paie pas, elle "
            u"s'établit — ou pas.",
     mode=u"NumericTolerance", tol=u"0.01", nb=8,
     comp=u"Multiplication, Addition, Division, Panel",
     etapes=[u"Chiffrer les jetons d'entrée du mois, et ceux de sortie.",
             u"Appliquer à chacun SON tarif.",
             u"Additionner, et ramener au million de jetons."],
     pieges=[u"Appliquer un tarif unique.",
             u"Oublier que les tarifs sont donnés au million.",
             u"Compter la sortie comme négligeable parce qu'elle est courte."],
     var=[u"Chiffrer la part de la sortie dans la facture.",
          u"Reprendre avec une mise en cache qui évite 40 % des requêtes."],
     gamif=u"G-16 Livrable pesé",
     bareme=u"1 point si le coût mensuel est juste au centime.",
     verdict=u"competence"),

]
