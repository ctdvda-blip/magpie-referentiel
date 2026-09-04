# -*- coding: utf-8 -*-
"""Vague 3 : un exercice pour chacune des dix-huit notions ajoutees.

Les notions viennent de `notions_complement.py`, qui a porte les quatorze
categories les plus maigres du referentiel a trois notions. Chaque notion
ajoutee recoit ici son exercice, de sorte que la couverture reste entiere et
que le compte par categorie suive.

Quatre de ces items sont des CONNAISSANCES et deviennent des questions
charnieres : choisir une representation geometrique, formuler un objectif
d'optimisation, savoir ce qu'une simulation ne dit pas, reconnaitre une
surface developpable. Ce sont des jugements, pas des calculs, et la skill
interdit d'en faire de faux exercices.

TOUTES LES VALEURS SONT CALCULEES par `verifier_vague3.py`.
"""

# ---------------------------------------------------------------------------
# Jeux de donnees
# ---------------------------------------------------------------------------

#: RH-23 — le releve, calque et type par objet
D_RH23_OBJETS = [
    (u"10-Porteurs", u"Courbe"), (u"10-Porteurs", u"Surface"),
    (u"11-Cloisons", u"Courbe"), (u"10-Porteurs", u"Courbe"),
    (u"20-Menuiseries", u"Bloc"), (u"11-Cloisons", u"Surface"),
    (u"10-Porteurs", u"Courbe"), (u"10-Porteurs", u"Bloc"),
    (u"11-Cloisons", u"Courbe"), (u"20-Menuiseries", u"Bloc"),
    (u"10-Porteurs", u"Surface"), (u"11-Cloisons", u"Courbe"),
    (u"10-Porteurs", u"Courbe"), (u"20-Menuiseries", u"Surface"),
    (u"11-Cloisons", u"Bloc"), (u"10-Porteurs", u"Courbe"),
    (u"20-Menuiseries", u"Bloc"), (u"11-Cloisons", u"Courbe"),
    (u"10-Porteurs", u"Surface"), (u"10-Porteurs", u"Courbe"),
    (u"20-Menuiseries", u"Courbe"), (u"11-Cloisons", u"Surface"),
    (u"10-Porteurs", u"Bloc"), (u"20-Menuiseries", u"Bloc"),
]
D_RH23_CIBLE = (u"10-Porteurs", u"Courbe")

#: A-50 — les libelles tels que l'atelier les a saisis
D_A50_LIBELLES = [u" MEL-19 ", u"mel-19", u"MEL-19", u"CP-18", u" cp-18",
                  u"CP-18 ", u"MDF-22", u"mdf-22 ", u" MDF-22", u"MAS-27",
                  u"mas-27", u"MAS-27 ", u"CP-12", u" cp-12 ", u"MEL-19",
                  u"mdf-16", u"MDF-16 ", u"CP-18", u"mas-27", u"MEL-19 "]

#: A-51 — des reperes de pieces, saisis comme du texte
D_A51_REPERES = [u"2", u"10", u"7", u"21", u"3", u"15", u"9", u"100",
                 u"12", u"5", u"30", u"8"]

#: GP-09 — un trapeze rectangle : base, hauteur, angle du fuyant
D_GP09 = dict(base=2400.0, hauteur=1800.0, angle=68.0)

#: GP-11 — un contour a conger et a decaler
D_GP11 = dict(longueur=1800.0, hauteur=900.0, rayon=120.0, decalage=40.0)

#: GP-12 — un point, une rotation, une translation
D_GP12 = dict(point=(1200.0, 0.0), angle=35.0, translation=(800.0, 300.0))

#: MP-05 — le profil de temps, releve composant par composant
D_MP05_TEMPS = [
    (u"Lecture du modele", 210), (u"Nettoyage des courbes", 95),
    (u"Maillage adaptatif", 4820), (u"Calcul des aires", 140),
    (u"Tri des pieces", 60), (u"Imbrication", 1310),
    (u"Cotation", 180), (u"Nomenclature", 75),
    (u"Rendu d'apercu", 640), (u"Export", 120),
    (u"Verification", 210), (u"Journalisation", 40),
]

#: AV-04 — un tassement qui decroit d'un facteur constant
D_AV04 = dict(depart=48.0, facteur=0.85, seuil=5.0)

#: AV-05 — les longueurs a charger, dans l'ordre du montage
D_AV05_LONGUEURS = [340, 512, 198, 760, 425, 630, 285, 918, 372, 540,
                    205, 688, 455, 310, 795, 240, 610, 380, 725, 165]
D_AV05_CAPACITE = 4000

#: AV-07 — huit solutions : (nom, cout, performance)
D_AV07_SOLUTIONS = [(u"S1", 1200, 82), (u"S2", 980, 74), (u"S3", 1450, 91),
                    (u"S4", 1100, 79), (u"S5", 1320, 86), (u"S6", 890, 68),
                    (u"S7", 1510, 88), (u"S8", 1050, 83)]

#: AV-08 — le residu passe apres passe. Il repasse AU-DESSUS de la
#: tolerance a la septieme : c'est tout l'objet de l'exercice.
D_AV08_RESIDUS = [(1, 42.0), (2, 18.5), (3, 6.2), (4, 1.8), (5, 0.42),
                  (6, 0.09), (7, 0.13), (8, 0.06), (9, 0.04), (10, 0.03)]
D_AV08_TOLERANCE = 0.1

#: WB-08 — douze reglages soumis a l'interface : (hauteur, tablettes,
#: epaisseur). Une tablette demande 180 mm de hauteur libre plus son
#: epaisseur.
D_WB08_CAS = [(2200, 6, 30), (1200, 6, 30), (900, 4, 22), (1800, 6, 18),
              (600, 3, 16), (2000, 5, 25), (450, 2, 30), (1500, 4, 30),
              (1000, 5, 22), (1600, 8, 18), (2100, 4, 16), (750, 4, 25)]
D_WB08_LIBRE = 180

#: WB-09 — ce que chaque format transporte
#: (format, geometrie, unites, calques, matieres, metadonnees, courbes)
D_WB09_FORMATS = [
    (u"STL",  1, 0, 0, 0, 0, 0),
    (u"OBJ",  1, 0, 1, 1, 0, 0),
    (u"3DM",  1, 1, 1, 1, 1, 1),
    (u"IGES", 1, 1, 1, 0, 0, 1),
    (u"STEP", 1, 1, 1, 1, 0, 1),
    (u"glTF", 1, 1, 0, 1, 1, 0),
]
D_WB09_BESOIN = (u"geometrie", u"unites", u"calques", u"courbes")

#: FA-06 — le debit lineaire d'un panneau
D_FA06 = dict(panneau=2500.0, piece=352.0, trait=4.0, rive=12.0)


# ---------------------------------------------------------------------------
# Lot RH
# ---------------------------------------------------------------------------

LOT_RH = [

dict(id=u"RH-23", titre=u"Sélectionner sur ce que les objets sont",
     them=u"RH2 · Organisation du document Rhino",
     ref=u"REF-143",
     niv=u"Débutant", duree=20, prereq=u"RH-13",
     competence=u"Retrouver des objets par le croisement de leurs propriétés, "
                u"plutôt que par ce qu'on voit à l'écran.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Il faut isoler les axes de porteurs pour les envoyer au bureau "
              u"d'études. Une sélection à la souris cesse d'être juste dès la "
              u"livraison suivante.",
     obj=u"Retrouver des objets par le croisement de leurs propriétés, plutôt "
         u"que par ce qu'on voit à l'écran.",
     enonce=u"Le relevé des vingt-quatre objets vous est fourni, avec pour "
            u"chacun son calque et son type. Donnez le nombre d'objets qui "
            u"sont À LA FOIS sur le calque des porteurs et de type courbe.",
     depart=u"Les vingt-quatre objets, leur calque et leur type.",
     att=u"6 objets satisfont les deux conditions.",
     erreur=u"Compter sur une seule propriété : onze objets sont sur le calque "
            u"des porteurs, et onze sont des courbes. Les deux comptes sont "
            u"égaux, ce qui donne l'illusion d'une réponse — mais seuls six "
            u"objets vérifient les deux conditions ensemble.",
     donnees_note=u"Les deux comptes partiels valent onze chacun, à dessein : "
                  u"un apprenant qui n'en vérifie qu'un obtient le même chiffre "
                  u"des deux côtés et n'a aucune raison de se méfier. Le "
                  u"croisement, lui, en donne six.",
     limite=u"L'exercice croise deux propriétés. En pratique on en croise "
            u"souvent trois ou quatre, et c'est le même geste — mais aussi le "
            u"moment où une sélection à la souris devient impossible à "
            u"reproduire.",
     mode=u"SingleValue", tol=u"0", nb=7,
     comp=u"Texte, Member Index, Gate And, Cull Pattern, List Length, Panel",
     etapes=[u"Comparer le calque de chaque objet à celui recherché.",
             u"Comparer son type à celui recherché.",
             u"Ne retenir que les objets qui satisfont les DEUX.",
             u"Compter."],
     pieges=[u"Ne vérifier qu'une propriété.",
             u"Additionner les deux comptes partiels.",
             u"Sélectionner à l'écran plutôt que sur la propriété."],
     var=[u"Ajouter une troisième condition sur la couleur.",
          u"Enregistrer la sélection comme un filtre rejouable."],
     gamif=u"G-02 Diagnostic éclair",
     bareme=u"1 point si le croisement est juste.",
     verdict=u"competence"),

]


# ---------------------------------------------------------------------------
# Lot A
# ---------------------------------------------------------------------------

LOT_A = [

dict(id=u"A-50", titre=u"Nettoyer avant de regrouper",
     them=u"A7 · Outils de texte",
     ref=u"REF-144",
     niv=u"Intermédiaire", duree=25, prereq=u"A-28",
     competence=u"Ramener des libellés saisis à la main à une forme "
                u"comparable, avant tout regroupement.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Les références du débit ont été saisies par trois personnes, "
              u"sur trois postes. Le fournisseur, lui, attend une ligne par "
              u"référence.",
     obj=u"Ramener des libellés saisis à la main à une forme comparable, avant "
         u"tout regroupement.",
     enonce=u"Les vingt libellés vous sont fournis tels qu'ils ont été saisis. "
            u"Donnez le nombre de références réellement distinctes.",
     depart=u"Les vingt libellés, avec leurs espaces et leurs casses "
            u"d'origine.",
     att=u"6 références distinctes.",
     erreur=u"Regrouper sans nettoyer : on en trouve dix-sept. « MEL-19 », "
            u" « mel-19 » et « MEL-19 » avec une espace de bord sont trois "
            u"chaînes différentes et une seule référence. Le fournisseur "
            u"recevrait dix-sept lignes pour six produits, et le rapprochement "
            u"de facture échouerait sans que rien ne soit signalé.",
     donnees_note=u"Trois écarts de saisie, et un seul de chaque sorte par "
                  u"référence : espace de bord, casse, et les deux à la fois. "
                  u"Dix-sept contre six, soit près du triple : l'erreur ne se "
                  u"rattrape pas au jugé.",
     limite=u"Le nettoyage traite les écarts de FORME. Deux références "
            u"réellement différentes mal orthographiées resteront deux — et "
            u"c'est heureux : aucun nettoyage ne doit deviner l'intention.",
     mode=u"SingleValue", tol=u"0", nb=7,
     comp=u"Texte, Trim, Upper Case, Create Set, List Length, Panel",
     etapes=[u"Retirer les espaces de bord.",
             u"Uniformiser la casse.",
             u"Établir l'ensemble des valeurs distinctes.",
             u"Compter."],
     pieges=[u"Regrouper sur la chaîne brute.",
             u"Retirer TOUS les espaces, y compris ceux de l'intérieur : un "
             u"libellé composé y perdrait son sens."],
     var=[u"Rendre la liste des références nettoyées, triées.",
          u"Repérer les libellés que le nettoyage n'a pas suffi à réconcilier."],
     gamif=u"G-11 Commande à passer",
     bareme=u"1 point si le nombre de références distinctes est juste.",
     verdict=u"competence"),

dict(id=u"A-51", titre=u"Le repère qui arrive en tête",
     them=u"A2 · Types et conversion implicite",
     ref=u"REF-145",
     niv=u"Débutant", duree=20, prereq=u"A-06",
     competence=u"Reconnaître qu'un tri dépend du TYPE des valeurs triées, et "
                u"pas seulement de leur apparence.",
     bloom=u"Comprendre × conceptuelle",
     contexte=u"Les repères de pièces sortent d'un tableur, où ils sont du "
              u"texte. Le bon de débit les veut dans l'ordre.",
     obj=u"Reconnaître qu'un tri dépend du type des valeurs triées, et pas "
         u"seulement de leur apparence.",
     enonce=u"Les douze repères vous sont fournis tels qu'ils arrivent du "
            u"tableur : ce sont des chaînes de caractères. Triés en l'état, "
            u"donnez le repère qui arrive en tête.",
     depart=u"Les douze repères, sous forme de texte.",
     att=u"10 — c'est ce repère qui arrive en tête d'un tri de TEXTE.",
     erreur=u"Répondre 2, le plus petit nombre. Un tri de texte compare "
            u"caractère par caractère : « 1 » vient avant « 2 », donc 10 et "
            u"100 précèdent 2. Sur un bon de débit, les pièces sortent alors "
            u"dans un ordre qui n'est celui de personne.",
     donnees_note=u"Douze repères de 2 à 100, choisis pour que les deux tris "
                  u"donnent des têtes DIFFÉRENTES — 10 contre 2 — et des "
                  u"queues différentes aussi : 9 contre 100. Aucune des deux "
                  u"réponses n'est absurde à l'œil, et c'est précisément "
                  u"pourquoi l'erreur passe.",
     limite=u"L'exercice montre le symptôme. Le remède — convertir avant de "
            u"trier — se pose en amont, au moment de la lecture du tableur, "
            u"et pas au moment du tri.",
     mode=u"SingleValue", tol=u"0", nb=5,
     comp=u"Texte, Sort List, List Item, Panel",
     etapes=[u"Trier les repères tels qu'ils sont, en texte.",
             u"Prendre le premier.",
             u"Refaire le tri après conversion en nombres, et comparer."],
     pieges=[u"Répondre par le plus petit nombre.",
             u"Supposer qu'un tri « comprend » ce que les valeurs "
             u"représentent."],
     var=[u"Donner aussi le repère qui arrive en queue dans chaque tri.",
          u"Compter combien de repères changent de place entre les deux tris."],
     gamif=u"G-14 Question éclair",
     bareme=u"1 point si le repère de tête du tri de texte est juste.",
     verdict=u"competence"),

]


# ---------------------------------------------------------------------------
# Lot GP
# ---------------------------------------------------------------------------

LOT_GP = [

dict(id=u"GP-09", titre=u"Ce que les contraintes imposent",
     them=u"GP3 · Plan paramétrique",
     ref=u"REF-146",
     niv=u"Intermédiaire", duree=25, prereq=u"GP-05",
     competence=u"Déduire d'un jeu de contraintes la dimension qui n'est pas "
                u"donnée, plutôt que de la mesurer sur le dessin.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le joue de meuble suit la pente du rampant. Le plan donne la "
              u"base, la hauteur et l'angle ; la petite base, elle, se déduit "
              u"et doit se recalculer si l'angle change.",
     obj=u"Déduire d'un jeu de contraintes la dimension qui n'est pas donnée, "
         u"plutôt que de la mesurer sur le dessin.",
     enonce=u"Le joue est un trapèze rectangle de 2 400 mm de base et "
            u"1 800 mm de hauteur, dont le fuyant fait 68° avec "
            u"l'horizontale. Donnez la longueur de la petite base, en "
            u"millimètres.",
     depart=u"La base, la hauteur et l'angle du fuyant.",
     att=u"1 672,75 mm — la petite base, à 0,01 près.",
     erreur=u"Retrancher la LONGUEUR du fuyant (1 941 mm) au lieu de son "
            u"recul horizontal (727 mm), ce qui donne 459 mm. La valeur reste "
            u"positive et plausible sur un plan ; la pièce, elle, sort de "
            u"l'atelier avec 1,2 m de moins.",
     donnees_note=u"Un angle de 68° donne un recul de 727 mm et un fuyant de "
                  u"1 941 mm : les deux sont du même ordre que les cotes du "
                  u"meuble, donc tous deux crédibles. C'est ce qui rend la "
                  u"confusion durable.",
     limite=u"La petite base se déduit d'un fuyant RECTILIGNE. Un fuyant "
            u"courbe, cas fréquent en menuiserie de comble, ne se traite pas "
            u"par un recul horizontal : il demande une intersection, et "
            u"l'exercice ne l'aborde pas.",
     mode=u"NumericTolerance", tol=u"0.01", nb=7,
     comp=u"Radians, Tangent, Division, Subtraction, Panel",
     etapes=[u"Convertir l'angle en radians.",
             u"Calculer le RECUL horizontal du fuyant : hauteur divisée par la "
             u"tangente de l'angle.",
             u"Le retrancher à la base."],
     pieges=[u"Prendre la longueur du fuyant pour son recul.",
             u"Multiplier par la tangente au lieu de diviser.",
             u"Oublier la conversion en radians."],
     var=[u"Faire varier l'angle et vérifier que la petite base suit.",
          u"Trouver l'angle qui annule la petite base."],
     gamif=u"G-08 Relevé contradictoire",
     bareme=u"1 point si la petite base est juste à 0,01 mm près.",
     verdict=u"competence"),

dict(id=u"GP-10", titre=u"Courbe, surface, solide ou maillage",
     them=u"GP5 · Synthèse géométrie",
     ref=u"REF-147",
     niv=u"Perfectionnement", duree=8, prereq=u"GP-03",
     competence=u"—", bloom=u"Évaluer × conceptuelle",
     contexte=u"La même pièce peut se traiter de quatre façons. Chacune répond "
              u"à des questions différentes, et coûte un prix différent.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Vous devez chiffrer le VOLUME de matière d'une pièce "
               u"moulurée. Sur quelle représentation travaillez-vous ?\n"
               u"a) Le maillage : c'est le plus rapide à obtenir.\n"
               u"b) Un solide fermé : seul un volume étanche a un volume. ← "
               u"réponse\n"
               u"c) Les courbes de profil : elles suffisent, le volume s'en "
               u"déduit.\n"
               u"d) Peu importe : Grasshopper convertit tout seul.\n\n"
               u"Valeur diagnostique : (a) est la réponse la plus fréquente et "
               u"elle n'est pas absurde — un maillage fermé a bien un volume, "
               u"mais approché, et sa finesse décide de l'erreur. (c) confond "
               u"ce qui ENGENDRE la forme et ce qui la mesure. (d) est le "
               u"vrai piège : Grasshopper convertit en effet, silencieusement, "
               u"et le résultat dépend alors d'une conversion que personne "
               u"n'a choisie. Le choix se fait sur ce qu'on veut MESURER."),

dict(id=u"GP-11", titre=u"L'ordre des opérations",
     them=u"GP5 · Synthèse géométrie",
     ref=u"REF-148",
     niv=u"Perfectionnement", duree=30, prereq=u"GP-10",
     competence=u"Établir qu'une suite d'opérations géométriques ne commute "
                u"pas, et chiffrer ce que l'ordre change.",
     bloom=u"Analyser × procédurale",
     contexte=u"Le contour part à la découpe. Il doit être congé de 120 mm et "
              u"décalé de 40 mm vers l'extérieur pour la surcote d'usinage.",
     obj=u"Établir qu'une suite d'opérations géométriques ne commute pas, et "
         u"chiffrer ce que l'ordre change.",
     enonce=u"Le contour est un rectangle de 1 800 × 900 mm. Il faut le "
            u"congéer d'un rayon de 120 mm et le décaler de 40 mm vers "
            u"l'extérieur. Donnez l'écart de périmètre entre les deux ordres "
            u"possibles, en millimètres.",
     depart=u"Les dimensions du rectangle, le rayon de congé et la valeur du "
            u"décalage.",
     att=u"68,67 mm d'écart entre les deux ordres, à 0,01 près.",
     erreur=u"Supposer que l'ordre est indifférent et n'en calculer qu'un. "
            u"Congéer puis décaler donne des congés de 160 mm ; décaler puis "
            u"congéer les laisse à 120 mm sur un contour plus grand. Les deux "
            u"pièces sortent différentes, et rien sur le plan ne dit laquelle "
            u"était voulue.",
     donnees_note=u"Un écart de 68,67 mm sur un périmètre de 5 445 mm, soit "
                  u"1,3 % : trop peu pour se voir à l'écran, assez pour que "
                  u"deux ateliers travaillant chacun dans son ordre livrent "
                  u"des pièces qui ne s'assemblent pas.",
     limite=u"L'exercice chiffre l'écart de PÉRIMÈTRE. L'écart de forme est "
            u"ailleurs : les rayons ne sont pas les mêmes, et c'est cela que "
            u"le plan doit préciser.",
     mode=u"NumericTolerance", tol=u"0.01", nb=10,
     comp=u"Multiplication, Addition, Subtraction, Pi, Absolute, Panel",
     etapes=[u"Calculer le périmètre pour l'ordre congé puis décalage : les "
             u"rayons valent alors rayon + décalage.",
             u"Calculer celui de l'ordre inverse : le contour grandit de deux "
             u"décalages dans chaque dimension, les rayons restent.",
             u"Prendre la valeur absolue de la différence."],
     pieges=[u"Supposer la commutativité.",
             u"Oublier que le décalage agit des DEUX côtés de chaque "
             u"dimension."],
     var=[u"Faire tendre le rayon vers zéro et vérifier que l'écart "
          u"disparaît.",
          u"Reprendre avec un décalage vers l'intérieur."],
     gamif=u"G-21 Optimisation comparée",
     bareme=u"1 point si l'écart est juste à 0,01 mm près.",
     verdict=u"competence"),

dict(id=u"GP-12", titre=u"Tourner puis déplacer, ou l'inverse",
     them=u"GP2 · Transformations et réseaux",
     ref=u"REF-149",
     niv=u"Intermédiaire", duree=25, prereq=u"GP-11",
     competence=u"Composer deux transformations en sachant que leur ordre "
                u"décide du résultat.",
     bloom=u"Analyser × procédurale",
     contexte=u"Le bras de la potence est décrit par une rotation et une "
              u"translation. Selon l'ordre où on les applique, son extrémité "
              u"ne tombe pas au même endroit.",
     obj=u"Composer deux transformations en sachant que leur ordre décide du "
         u"résultat.",
     enonce=u"Le point est à 1 200 mm de l'origine sur l'axe des abscisses. "
            u"On lui applique une rotation de 35° autour de l'origine et une "
            u"translation de 800 mm en X et 300 mm en Y. Donnez la distance "
            u"entre les deux positions finales possibles, en millimètres.",
     depart=u"La position du point, l'angle de rotation et le vecteur de "
            u"translation.",
     att=u"513,85 mm séparent les deux résultats, à 0,01 près.",
     erreur=u"Croire que la composition commute et n'appliquer qu'un ordre. "
            u"Une rotation autour de l'ORIGINE emporte la translation déjà "
            u"faite ; appliquée après, elle ne la touche pas. 514 mm d'écart "
            u"sur un bras de 1,2 m, c'est un point d'ancrage qui tombe à côté "
            u"du poteau.",
     donnees_note=u"Un angle de 35° et une translation du même ordre de "
                  u"grandeur que le bras : les deux résultats sont tous deux "
                  u"plausibles, et 514 mm d'écart ne se voit pas sur un "
                  u"aperçu à l'échelle du bâtiment.",
     limite=u"L'exercice mesure l'écart entre deux ordres. Lequel est le bon "
            u"dépend de ce que décrit le mécanisme — et c'est au plan de le "
            u"dire, pas au calcul de le deviner.",
     mode=u"NumericTolerance", tol=u"0.01", nb=12,
     comp=u"Rotate, Move, Distance, Panel",
     etapes=[u"Appliquer la rotation puis la translation.",
             u"Appliquer la translation puis la rotation.",
             u"Mesurer la distance entre les deux points obtenus."],
     pieges=[u"N'appliquer qu'un ordre.",
             u"Tourner autour du point plutôt qu'autour de l'origine."],
     var=[u"Chercher la translation qui rendrait les deux ordres "
          u"équivalents.",
          u"Reprendre avec une rotation autour du point lui-même."],
     gamif=u"G-08 Relevé contradictoire",
     bareme=u"1 point si la distance est juste à 0,01 mm près.",
     verdict=u"competence"),

]


# ---------------------------------------------------------------------------
# Lot MP
# ---------------------------------------------------------------------------

LOT_MP = [

dict(id=u"MP-05", titre=u"Mesurer avant d'optimiser",
     them=u"MP2 · Organisation et performance",
     ref=u"REF-150",
     niv=u"Perfectionnement", duree=25, prereq=u"MP-04",
     competence=u"Fonder une optimisation sur un relevé de temps, et non sur "
                u"l'intuition de ce qui coûte cher.",
     bloom=u"Analyser × procédurale",
     contexte=u"La définition met huit secondes à répondre. On a une "
              u"après-midi pour la rendre utilisable, et douze composants "
              u"candidats.",
     obj=u"Fonder une optimisation sur un relevé de temps, et non sur "
         u"l'intuition de ce qui coûte cher.",
     enonce=u"Le relevé de temps des douze composants vous est fourni, en "
            u"millisecondes. Donnez la part du composant le plus lourd dans "
            u"le temps total, en pour cent, arrondie à l'entier.",
     depart=u"Les douze composants et le temps mesuré pour chacun.",
     att=u"61 % — la part du maillage adaptatif.",
     erreur=u"Répartir l'effort sur les composants qu'on soupçonne. Un seul "
            u"composant pèse 61 % du temps : le diviser par dix ferait gagner "
            u"55 % à lui seul, quand optimiser les onze autres jusqu'à les "
            u"annuler n'en ferait gagner que 39.",
     donnees_note=u"Douze composants dont un à 4 820 ms et le suivant à "
                   u"1 310 : le profil réel d'une définition, où le temps se "
                   u"concentre au lieu de se répartir. Les neuf plus légers "
                   u"cumulés pèsent moins d'un quart du plus lourd.",
     limite=u"Le relevé dit où le temps passe, pas comment le réduire. Un "
            u"maillage adaptatif se règle avant de se réécrire — et parfois "
            u"il ne se réduit pas.",
     mode=u"SingleValue", tol=u"0", nb=8,
     comp=u"Nombre, Mass Addition, Bounds, Deconstruct Domain, Division, "
          u"Multiplication, Round, Panel",
     etapes=[u"Sommer les temps.",
             u"Trouver le plus grand.",
             u"En faire le rapport au total, puis un pourcentage.",
             u"Arrondir à l'entier."],
     pieges=[u"Optimiser sans mesurer.",
             u"Prendre la moyenne pour la part du plus lourd.",
             u"Confondre le plus lourd et le plus fréquent."],
     var=[u"Chiffrer le gain total si le plus lourd était divisé par dix.",
          u"Trouver combien de composants il faut cumuler pour atteindre la "
          u"moitié du temps."],
     gamif=u"G-13 Chronomètre",
     bareme=u"1 point si la part est juste à l'entier près.",
     verdict=u"competence"),

]
