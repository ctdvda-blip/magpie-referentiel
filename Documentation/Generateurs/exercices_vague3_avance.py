# -*- coding: utf-8 -*-
"""Vague 3, suite : lots AV, WB et FA.

Le domaine « Algorithmique avancée » est celui qui change le plus : ses trois
categories tenaient chacune sur UNE notion et UN exercice. Elles en portent
desormais trois et trois — et le lot AV passe de 3 a 9 exercices.
"""

# Les jeux de donnees vivent dans `exercices_vague3`, avec les autres.
from exercices_vague3 import (D_AV04, D_AV05_LONGUEURS, D_AV05_CAPACITE,
                              D_AV07_SOLUTIONS, D_AV08_RESIDUS,
                              D_AV08_TOLERANCE, D_WB08_CAS, D_WB08_LIBRE,
                              D_WB09_FORMATS, D_WB09_BESOIN, D_FA06)


# ---------------------------------------------------------------------------
# Lot AV — algorithmique avancee
# ---------------------------------------------------------------------------

LOT_AV = [

dict(id=u"AV-04", titre=u"Ce qui met fin à la boucle",
     them=u"AV1 · Boucles et itération",
     ref=u"REF-151",
     niv=u"Perfectionnement", duree=25, prereq=u"AV-01",
     competence=u"Déterminer le nombre de passages qu'exige un critère "
                u"d'arrêt, et savoir que c'est LUI qui commande la sortie.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le tassement du remblai décroît de 15 % à chaque passe de "
              u"compactage. On s'arrête quand il descend sous 5 mm.",
     obj=u"Déterminer le nombre de passages qu'exige un critère d'arrêt, et "
         u"savoir que c'est lui qui commande la sortie.",
     enonce=u"Le tassement initial vaut 48 mm et chaque passe le réduit de "
            u"15 %. Donnez le nombre de passes nécessaires pour descendre "
            u"sous 5 mm.",
     depart=u"Le tassement initial, le facteur de décroissance et le seuil.",
     att=u"14 passes — la treizième laisse encore 5,80 mm.",
     erreur=u"Fixer un nombre de passes à l'avance, dix par exemple, parce "
            u"que « ça devrait suffire ». Il en reste alors 9,45 mm, soit "
            u"près du double du toléré — et la boucle s'est arrêtée sur un "
            u"compte, pas sur un état.",
     donnees_note=u"48 mm ramenés sous 5 par un facteur 0,85 demandent "
                  u"exactement 14 passes : la treizième laisse 5,80 et la "
                  u"quatorzième 4,93. La frontière tombe donc entre deux "
                  u"entiers, et un arrondi au plus proche donnerait 14 — juste "
                  u"par hasard, ce que la variante d'énoncé permet de vérifier.",
     limite=u"La décroissance géométrique est une hypothèse commode. Un "
            u"tassement réel ralentit autrement, et c'est le relevé qui le "
            u"dit — l'exercice porte sur le critère d'arrêt, pas sur la "
            u"géotechnique.",
     mode=u"SingleValue", tol=u"0", nb=8,
     comp=u"Division, Log N, Round, Panel",
     etapes=[u"Écrire le tassement après n passes comme un produit de "
             u"facteurs.",
             u"En déduire n par le logarithme du rapport des seuils.",
             u"Arrondir au SUPÉRIEUR : une passe entamée ne compte pas à "
             u"moitié.",
             u"Vérifier la valeur atteinte à n et à n − 1."],
     pieges=[u"Fixer le nombre de passes d'avance.",
             u"Arrondir à l'inférieur, ce qui laisse le tassement au-dessus "
             u"du seuil."],
     var=[u"Trouver le facteur qui atteindrait le seuil en dix passes.",
          u"Ajouter un nombre maximal de passes, et dire ce qui se produit "
          u"si le critère n'est jamais atteint."],
     gamif=u"G-13 Chronomètre",
     bareme=u"1 point si le nombre de passes est juste et arrondi au "
            u"supérieur.",
     verdict=u"competence"),

dict(id=u"AV-05", titre=u"Charger jusqu'à la limite",
     them=u"AV1 · Boucles et itération",
     ref=u"REF-152",
     niv=u"Perfectionnement", duree=25, prereq=u"AV-04",
     competence=u"Transporter un cumul d'un passage au suivant, et repérer le "
                u"rang où il franchit une limite.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Les pièces se chargent dans l'ordre du montage, pas dans "
              u"celui qui remplirait le mieux. Le camion accepte 4 000 mm de "
              u"longueur cumulée.",
     obj=u"Transporter un cumul d'un passage au suivant, et repérer le rang "
         u"où il franchit une limite.",
     enonce=u"Les vingt longueurs vous sont fournies dans l'ordre de "
            u"chargement. La capacité est de 4 000 mm cumulés. Donnez le rang "
            u"de la première pièce qui fait dépasser la capacité.",
     depart=u"Les vingt longueurs, dans l'ordre, et la capacité.",
     att=u"8 — c'est la huitième pièce qui fait passer le cumul au-delà de "
         u"4 000 mm.",
     erreur=u"Rendre le rang de la dernière pièce qui TIENT, soit 7. Les deux "
            u"réponses ne diffèrent que d'une unité, et la consigne tranche : "
            u"c'est celle qui fait dépasser qui est demandée. Sur le quai, "
            u"c'est la pièce qu'on repose.",
     donnees_note=u"Le cumul atteint 3 150 mm à la septième pièce et "
                  u"4 068 mm à la huitième : le franchissement est net, mais "
                  u"le rang ne se devine pas — il faut cumuler. Vingt "
                  u"longueurs pour que le calcul de tête soit exclu.",
     limite=u"L'exercice suit l'ordre imposé. Choisir l'ordre qui remplit le "
            u"mieux est un tout autre problème, et il n'a pas de solution "
            u"simple.",
     mode=u"SingleValue", tol=u"0", nb=9,
     comp=u"Mass Addition, Larger Than, Cull Pattern, List Item, Panel",
     etapes=[u"Cumuler les longueurs dans l'ordre — la somme partielle, pas "
             u"le total.",
             u"Comparer chaque cumul à la capacité.",
             u"Prendre le rang du premier qui dépasse."],
     pieges=[u"Rendre le rang de la dernière pièce qui tient.",
             u"Sommer d'abord et chercher ensuite : le cumul PARTIEL est ce "
             u"qui porte l'information."],
     var=[u"Donner le nombre de camions nécessaires pour les vingt pièces.",
          u"Rendre la longueur inutilisée du premier camion."],
     gamif=u"G-11 Commande à passer",
     bareme=u"1 point si le rang est juste.",
     verdict=u"competence"),

dict(id=u"AV-06", titre=u"Ce qu'on demande à l'optimisation",
     them=u"AV2 · Design génératif",
     ref=u"REF-153",
     niv=u"Perfectionnement", duree=8, prereq=u"AV-03",
     competence=u"—", bloom=u"Évaluer × conceptuelle",
     contexte=u"On veut « la meilleure façade ». L'outil, lui, veut une "
              u"grandeur à minimiser et des bornes.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Le client veut « la meilleure façade ». Que posez-vous "
               u"d'abord ?\n"
               u"a) Les contraintes : ce que la façade ne doit en aucun cas "
               u"faire.\n"
               u"b) La grandeur à optimiser, ET les contraintes qui bornent "
               u"les solutions admissibles. ← réponse\n"
               u"c) Les paramètres à faire varier : c'est eux qui définissent "
               u"l'espace.\n"
               u"d) Le nombre de générations, pour cadrer le temps de "
               u"calcul.\n\n"
               u"Valeur diagnostique : (c) est le réflexe de celui qui pense "
               u"en graphe plutôt qu'en projet — les paramètres viennent "
               u"après, et mal choisis ils ne font qu'agrandir un espace "
               u"vide. (a) est à moitié juste, et c'est ce qui la rend "
               u"dangereuse : des contraintes sans objectif rendent un "
               u"ensemble de solutions admissibles, dont aucune n'est "
               u"meilleure. Un objectif mal posé produit une solution "
               u"optimale à un problème que personne n'avait."),

dict(id=u"AV-07", titre=u"Les solutions qu'on ne peut pas départager",
     them=u"AV2 · Design génératif",
     ref=u"REF-154",
     niv=u"Perfectionnement", duree=30, prereq=u"AV-06",
     competence=u"Distinguer, parmi des solutions, celles qu'aucune autre ne "
                u"surpasse sur tous les critères à la fois.",
     bloom=u"Analyser × procédurale",
     contexte=u"L'optimisation a rendu huit variantes. Aucune n'est la "
              u"meilleure partout : c'est le principe, et c'est ce qui reste "
              u"à arbitrer.",
     obj=u"Distinguer, parmi des solutions, celles qu'aucune autre ne "
         u"surpasse sur tous les critères à la fois.",
     enonce=u"Les huit solutions vous sont fournies avec leur coût, à "
            u"minimiser, et leur performance, à maximiser. Donnez le nombre "
            u"de solutions qu'aucune autre ne surpasse sur les deux critères "
            u"à la fois.",
     depart=u"Les huit solutions, leur coût et leur performance.",
     att=u"5 solutions ne sont surpassées par aucune autre.",
     erreur=u"Chercher LA meilleure et n'en garder qu'une — la moins chère, "
            u"ou la plus performante. Les deux existent, elles ne sont pas la "
            u"même, et trois autres solutions restent défendables. Réduire un "
            u"arbitrage à un classement, c'est décider à la place du "
            u"projeteur sans le lui dire.",
     donnees_note=u"Huit solutions dont trois sont réellement surpassées : "
                  u"pour chacune, il existe une autre à la fois moins chère "
                  u"ET plus performante. Les cinq restantes forment le front, "
                  u"et le fait qu'elles soient majoritaires est le message — "
                  u"une optimisation ne réduit pas le choix, elle l'éclaire.",
     limite=u"L'exercice porte sur deux critères. À trois ou plus, le front "
            u"grossit vite et cesse d'être lisible : c'est le moment où il "
            u"faut hiérarchiser les critères, et cela ne se calcule pas.",
     mode=u"SingleValue", tol=u"0", nb=10,
     comp=u"Nombre, Cross Reference, Smaller Than, Larger Than, Gate And, "
          u"Cull Pattern, List Length, Panel",
     etapes=[u"Pour chaque solution, chercher s'il en existe une autre au "
             u"moins aussi bonne partout et strictement meilleure quelque "
             u"part.",
             u"Si oui, elle est surpassée.",
             u"Compter celles qui ne le sont pas."],
     pieges=[u"Ne garder que l'extrême d'un critère.",
             u"Oublier qu'une solution ne se surpasse pas elle-même.",
             u"Traiter « au moins aussi bon » comme « meilleur »."],
     var=[u"Nommer les trois solutions écartées et dire par laquelle.",
          u"Ajouter un troisième critère et observer le front grossir."],
     gamif=u"G-21 Optimisation comparée",
     bareme=u"1 point si le nombre de solutions non surpassées est juste.",
     verdict=u"competence"),

dict(id=u"AV-08", titre=u"Quand la relaxation a-t-elle convergé",
     them=u"AV3 · Simulation physique",
     ref=u"REF-155",
     niv=u"Perfectionnement", duree=25, prereq=u"AV-02",
     competence=u"Établir qu'une simulation s'est stabilisée, en distinguant "
                u"un passage sous la tolérance d'une stabilisation durable.",
     bloom=u"Analyser × procédurale",
     contexte=u"La forme relâchée ne bouge plus à l'écran depuis quelques "
              u"passes. Le relevé de résidu, lui, raconte autre chose.",
     obj=u"Établir qu'une simulation s'est stabilisée, en distinguant un "
         u"passage sous la tolérance d'une stabilisation durable.",
     enonce=u"Le résidu de chacune des dix passes vous est fourni. La "
            u"tolérance vaut 0,1. Donnez le numéro de la première passe à "
            u"partir de laquelle le résidu RESTE sous la tolérance.",
     depart=u"Le résidu de chaque passe, et la tolérance.",
     att=u"8 — c'est à partir de la huitième passe que le résidu ne remonte "
         u"plus.",
     erreur=u"Répondre 6, la première passe sous la tolérance. Le résidu y "
            u"descend à 0,09, puis REMONTE à 0,13 à la septième : la "
            u"simulation n'était pas stabilisée, elle passait. S'arrêter là "
            u"fige une forme qui bougeait encore, et rien à l'écran ne le "
            u"distingue d'une forme convergée.",
     donnees_note=u"Le résidu descend, franchit la tolérance, la refranchit "
                  u"en sens inverse d'un cheveu — 0,09 puis 0,13 — puis "
                  u"redescend pour de bon. Cette remontée est le cœur de "
                  u"l'exercice, et elle est réaliste : une relaxation "
                  u"oscille avant de se poser. Les deux réponses possibles, "
                  u"6 et 8, sont toutes deux plausibles à la lecture.",
     limite=u"Rester sous la tolérance sur trois passes n'est pas une preuve "
            u"de convergence, c'est un faisceau. Une simulation mal "
            u"contrainte peut se stabiliser sur une forme fausse — le "
            u"résidu ne dit rien de la justesse du modèle.",
     mode=u"SingleValue", tol=u"0", nb=9,
     comp=u"Nombre, Smaller Than, Cull Pattern, List Item, Panel",
     etapes=[u"Comparer chaque résidu à la tolérance.",
             u"Chercher le premier rang à partir duquel TOUTES les "
             u"comparaisons suivantes sont vraies.",
             u"Ne pas s'arrêter au premier passage sous le seuil."],
     pieges=[u"Prendre la première passe sous la tolérance.",
             u"Prendre la dernière passe du relevé.",
             u"Se fier à l'aperçu, qui ne bouge plus depuis longtemps."],
     var=[u"Dire ce qu'il faudrait relever de plus pour être sûr.",
          u"Reprendre avec une tolérance de 0,05."],
     gamif=u"G-20 Contre-expertise",
     bareme=u"1 point si le rang de stabilisation durable est juste.",
     verdict=u"competence"),

dict(id=u"AV-09", titre=u"Ce qu'une simulation ne dit pas",
     them=u"AV3 · Simulation physique",
     ref=u"REF-156",
     niv=u"Perfectionnement", duree=8, prereq=u"AV-08",
     competence=u"—", bloom=u"Évaluer × conceptuelle",
     contexte=u"La forme relâchée est belle, stable, et le client la trouve "
              u"convaincante. Reste à savoir ce qu'elle établit.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Votre relaxation a convergé sur une forme de couverture "
               u"tendue. Qu'avez-vous établi ?\n"
               u"a) Que la structure tient : la forme est en équilibre.\n"
               u"b) Une géométrie d'équilibre sous les hypothèses posées — ni "
               u"sections, ni contraintes admissibles, ni "
               u"dimensionnement. ← réponse\n"
               u"c) Rien d'utilisable : il faut un logiciel de calcul.\n"
               u"d) Que la forme est optimale.\n\n"
               u"Valeur diagnostique : (a) est l'erreur coûteuse, et elle est "
               u"facile — « équilibre » est le mot qu'emploie le moteur, et "
               u"ce n'est pas celui de l'ingénieur. Une forme d'équilibre dit "
               u"où va l'effort, pas s'il passe. (d) confond équilibre et "
               u"optimum : la relaxation ne compare rien. (c) jette ce qui a "
               u"le plus de valeur — la forme obtenue est précisément ce "
               u"qu'un logiciel de calcul demandera en entrée."),

]


# ---------------------------------------------------------------------------
# Lot WB — interfaces, web et interoperabilite
# ---------------------------------------------------------------------------

LOT_WB = [

dict(id=u"WB-08", titre=u"Les bornes qui empêchent l'infabricable",
     them=u"WB1 · Interfaces utilisateur",
     ref=u"REF-157",
     niv=u"Perfectionnement", duree=25, prereq=u"WB-04",
     competence=u"Éprouver les bornes d'une interface en cherchant les "
                u"combinaisons admises qui produisent une pièce "
                u"infabricable.",
     bloom=u"Évaluer × procédurale",
     contexte=u"Chaque paramètre du configurateur est borné. Pris séparément, "
              u"aucun ne pose problème ; c'est leur COMBINAISON qui décide.",
     obj=u"Éprouver les bornes d'une interface en cherchant les combinaisons "
         u"admises qui produisent une pièce infabricable.",
     enonce=u"Une tablette exige 180 mm de hauteur libre, plus son épaisseur. "
            u"Les douze réglages soumis vous sont fournis : hauteur du "
            u"meuble, nombre de tablettes, épaisseur. Donnez le nombre de "
            u"réglages infabricables.",
     depart=u"Les douze combinaisons, et la règle de hauteur libre.",
     att=u"3 réglages sur douze sont infabricables.",
     erreur=u"Vérifier chaque paramètre contre sa propre borne et conclure "
            u"que tout va bien : pris un à un, les douze réglages sont dans "
            u"les plages admises. C'est leur croisement qui échoue — une "
            u"hauteur permise et un nombre de tablettes permis peuvent être "
            u"incompatibles entre eux.",
     donnees_note=u"Trois combinaisons infaisables sur douze, et trois autres "
                  u"qui passent de justesse — 588 mm exigés pour 600 "
                  u"disponibles, 1 584 pour 1 600. La frontière est peuplée "
                  u"des deux côtés, de sorte qu'un contrôle approximatif se "
                  u"trompe dans les deux sens.",
     limite=u"L'exercice compte les combinaisons fautives d'un lot soumis. "
            u"Une interface robuste ne les compte pas : elle les rend "
            u"impossibles à saisir, en faisant dépendre la borne d'un "
            u"paramètre de la valeur des autres.",
     mode=u"SingleValue", tol=u"0", nb=9,
     comp=u"Multiplication, Addition, Smaller Than, Cull Pattern, "
          u"List Length, Panel",
     etapes=[u"Calculer, pour chaque réglage, la hauteur qu'exigent les "
             u"tablettes : leur nombre multiplié par la hauteur libre plus "
             u"l'épaisseur.",
             u"Comparer à la hauteur du meuble.",
             u"Compter les réglages où l'exigence dépasse le disponible."],
     pieges=[u"Vérifier les paramètres un à un.",
             u"Oublier d'ajouter l'épaisseur de la tablette à la hauteur "
             u"libre."],
     var=[u"Écrire la borne du nombre de tablettes en fonction de la hauteur.",
          u"Trouver la hauteur minimale qui rendrait les douze réglages "
          u"admissibles."],
     gamif=u"G-17 Passation",
     bareme=u"1 point si le compte des réglages infabricables est juste.",
     verdict=u"competence"),

dict(id=u"WB-09", titre=u"Ce que le format transporte, et ce qu'il perd",
     them=u"WB3 · Interopérabilité",
     ref=u"REF-158",
     niv=u"Perfectionnement", duree=25, prereq=u"WB-05",
     competence=u"Choisir un format d'échange sur ce qu'il transporte "
                u"réellement, et non sur le fait que le fichier s'ouvre.",
     bloom=u"Évaluer × procédurale",
     contexte=u"Le modèle part chez le bureau d'études, qui a besoin des "
              u"courbes, des calques et des unités. Un fichier qui s'ouvre "
              u"n'est pas un échange réussi.",
     obj=u"Choisir un format d'échange sur ce qu'il transporte réellement, et "
         u"non sur le fait que le fichier s'ouvre.",
     enonce=u"Le tableau des six formats vous est fourni, avec ce que chacun "
            u"transporte. L'échange exige la géométrie, les unités, les "
            u"calques et les courbes. Donnez le nombre de formats qui "
            u"conviennent.",
     depart=u"Les six formats et, pour chacun, ce qu'il transporte.",
     att=u"3 formats répondent aux quatre exigences.",
     erreur=u"Retenir tout format qui transporte la géométrie : les six "
            u"conviennent alors. Le fichier s'ouvrira, la forme sera là, et "
            u"le bureau d'études redemandera les calques et les unités — "
            u"c'est-à-dire la moitié du travail de mise en ordre.",
     donnees_note=u"Six formats, dont trois répondent aux quatre exigences et "
                  u"deux échouent sur un seul critère. Les réponses fausses "
                  u"plausibles — 6 si l'on ne regarde que la géométrie, 5 si "
                  u"l'on oublie les courbes — sont distinctes de 3.",
     limite=u"Le tableau dit ce que le format PEUT porter. Ce qu'il porte "
            u"effectivement dépend aussi de l'exportateur et de "
            u"l'importateur — deux logiciels qui parlent le même format "
            u"peuvent ne pas s'entendre.",
     mode=u"SingleValue", tol=u"0", nb=9,
     comp=u"Booléen, Gate And, Cull Pattern, List Length, Panel",
     etapes=[u"Ne retenir que les colonnes exigées par l'échange.",
             u"Pour chaque format, exiger qu'elles soient TOUTES vraies.",
             u"Compter."],
     pieges=[u"Se contenter de la géométrie.",
             u"Traiter la liste des exigences comme un « au moins un »."],
     var=[u"Nommer les formats écartés et le critère qui les écarte.",
          u"Refaire le choix pour un échange qui exigerait les matières."],
     gamif=u"G-17 Passation",
     bareme=u"1 point si le compte des formats convenables est juste.",
     verdict=u"competence"),

]


# ---------------------------------------------------------------------------
# Lot FA — aide a la fabrication
# ---------------------------------------------------------------------------

LOT_FA = [

dict(id=u"FA-05", titre=u"Ce qui se met à plat, et ce qui ne s'y met pas",
     them=u"FA2 · Déroulé et mise à plat",
     ref=u"REF-159",
     niv=u"Perfectionnement", duree=8, prereq=u"FA-03",
     competence=u"—", bloom=u"Comprendre × conceptuelle",
     contexte=u"La commande porte sur une coque à double courbure. Le "
              u"logiciel propose un déroulé, et il le fait sans se plaindre.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Le logiciel a déroulé votre coque à double courbure sans "
               u"message. Qu'en concluez-vous ?\n"
               u"a) Que la surface est développable, sinon il aurait refusé.\n"
               u"b) Qu'il a produit une APPROXIMATION, dont l'écart se "
               u"chiffre et doit être vérifié. ← réponse\n"
               u"c) Que le déroulé est juste aux tolérances près du "
               u"logiciel.\n"
               u"d) Qu'il faut découper la surface en bandes pour être "
               u"tranquille.\n\n"
               u"Valeur diagnostique : (a) prend l'absence de message pour "
               u"une validation — or aucun outil ne refuse de dérouler, ils "
               u"déforment. (c) confond la tolérance de calcul et l'erreur de "
               u"modèle : ici l'écart ne vient pas d'un arrondi, il vient de "
               u"ce que la surface ne se met pas à plat. (d) est le bon "
               u"REMÈDE, proposé avant le diagnostic — et découper en bandes "
               u"ne dispense pas de chiffrer ce qu'on perd."),

dict(id=u"FA-06", titre=u"Le trait de scie mange une pièce",
     them=u"FA1 · Imbrication",
     ref=u"REF-160",
     niv=u"Perfectionnement", duree=25, prereq=u"FA-01",
     competence=u"Compter les pièces d'un débit linéaire en tenant compte du "
                u"trait de scie et des rives inutilisables.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le panneau se refend en lames. La lame de scie prend 4 mm à "
              u"chaque passage, et les 12 mm de rive ne sont pas "
              u"utilisables.",
     obj=u"Compter les pièces d'un débit linéaire en tenant compte du trait "
         u"de scie et des rives inutilisables.",
     enonce=u"Le panneau mesure 2 500 mm. Chaque pièce fait 352 mm, le trait "
            u"de scie 4 mm, et 12 mm de rive sont à écarter de chaque côté. "
            u"Donnez le nombre de pièces par panneau.",
     depart=u"La longueur du panneau, celle de la pièce, le trait de scie et "
            u"la rive.",
     att=u"6 pièces par panneau.",
     erreur=u"Diviser la longueur du panneau par celle de la pièce : "
            u"2 500 ÷ 352 donne 7,1, donc 7 pièces. Il en manque une. Le "
            u"trait de scie et les rives mangent 44 mm à eux tous — moins de "
            u"2 % du panneau, et une pièce sur sept. C'est le genre d'écart "
            u"qui ne se voit qu'au moment où la dernière lame manque.",
     donnees_note=u"352 mm est choisi pour que le compte BASCULE : sans "
                  u"trait ni rives on en tire sept, avec on en tire six. À "
                  u"360 mm les deux calculs donneraient six, et l'exercice ne "
                  u"prouverait rien.",
     limite=u"Le calcul suppose un débit dans un seul sens. Un panneau se "
            u"refend souvent dans les deux, et le compte devient celui de "
            u"FA-04 — une affaire d'encombrement, pas de longueur.",
     mode=u"SingleValue", tol=u"0", nb=8,
     comp=u"Subtraction, Addition, Division, Round, Panel",
     etapes=[u"Retirer les deux rives de la longueur du panneau.",
             u"Chercher combien de pièces séparées d'un trait de scie "
             u"tiennent dans ce qui reste : entre n pièces il y a n − 1 "
             u"traits.",
             u"Arrondir à l'entier INFÉRIEUR."],
     pieges=[u"Diviser sans rien retirer.",
             u"Compter un trait de scie de trop ou de moins.",
             u"Arrondir au plus proche."],
     var=[u"Chiffrer la chute, et sa part du panneau.",
          u"Trouver la longueur de pièce qui ne laisserait aucune chute."],
     gamif=u"G-21 Optimisation comparée",
     bareme=u"1 point si le nombre de pièces est juste.",
     verdict=u"competence"),

]
