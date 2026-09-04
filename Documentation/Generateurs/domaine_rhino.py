# -*- coding: utf-8 -*-
"""Domaine 1 — Socle Rhino : lot RH.

Couvre les 24 notions du socle, REF-001 a REF-024.

PARTI PRIS
----------
Ces notions decrivent des gestes RHINO, pas des graphes Grasshopper. Le checker
Magpie, lui, ne sait comparer que ce qui sort d'une definition. Deux reponses,
selon la nature de la notion :

1. Ce qui produit une GEOMETRIE se valide en la referencant dans Grasshopper et
   en la mesurant — c'est deja le principe de A-04. L'apprenant modelise dans
   Rhino, la definition mesure, le checker compare un nombre. La competence
   evaluee reste bien le geste Rhino.

2. Ce qui releve de l'INTERFACE — navigation, selection, visibilite, blocs —
   ne produit rien de mesurable. Ce sont des connaissances : elles deviennent
   des questions charnieres, non notees, dont chaque mauvaise reponse est
   diagnostique. Les forcer en exercice mesurerait la memoire, pas la pratique.

VERSION : v0.1-260828
"""

VERSION = u"v0.1-260828"
LOT = u"RH"
TITRE_LOT = u"RH — Socle Rhino"


# ---------------------------------------------------------------------------
# Jeux de donnees
# ---------------------------------------------------------------------------

# RH-02 — implantation de poteaux livree par le geometre, repartie sur trois
# calques dont un seul est a reprendre.
D_RH02_PORTEURS = [(0, 0), (5400, 0), (10800, 0), (16200, 0),
                   (0, 6200), (5400, 6200), (10800, 6200), (16200, 6200),
                   (0, 12400), (5400, 12400), (10800, 12400), (16200, 12400)]
D_RH02_CLOISONS = [(2700, 3100), (8100, 3100), (13500, 3100),
                   (2700, 9300), (8100, 9300), (13500, 9300)]

# RH-08 — cotes d'un caisson a rendre etanche, en mm
D_RH08 = (420.0, 260.0, 180.0, 12.0)     # longueur, largeur, hauteur, epaisseur


NOTIONS_COUVERTES = {
    u"RH-01": u"REF-001, REF-002, REF-003",
    u"RH-02": u"REF-004, REF-006, REF-014",
    u"RH-03": u"REF-007, REF-008, REF-013",
    u"RH-04": u"REF-009, REF-010, REF-011",
    u"RH-05": u"REF-012",
    u"RH-06": u"REF-005",
    u"RH-07": u"REF-015, REF-017",
    u"RH-08": u"REF-019, REF-020, REF-021, REF-022, REF-023",
    u"RH-09": u"REF-016, REF-018",
    u"RH-10": u"REF-024",
}


LOT_RH = [

dict(id=u"RH-01", titre=u"Retrouver un objet perdu de vue",
     them=u"RH1 · Interface et navigation Rhino",
     ref=NOTIONS_COUVERTES[u"RH-01"],
     niv=u"Débutant", duree=6, prereq=u"—",
     competence=u"—", bloom=u"Comprendre × procédurale",
     contexte=u"Un fichier reçu d'un confrère s'ouvre sur une vue où l'on ne "
              u"voit rien : le modèle est quelque part, mais hors champ.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Vous ouvrez un fichier et la vue est vide, alors que le "
               u"modèle existe. Quel réflexe vous remet devant la géométrie "
               u"en une action ?\n"
               u"a) Zoomer arrière longuement jusqu'à voir quelque chose.\n"
               u"b) Zoom Étendue — la vue se cadre sur tout ce qui est "
               u"visible. ← réponse\n"
               u"c) Recréer une vue depuis le menu.\n"
               u"d) Fermer et rouvrir le fichier.\n\n"
               u"Valeur diagnostique : (a) est ce que fait spontanément un "
               u"débutant, et cela peut durer longtemps — un objet égaré à "
               u"10 km de l'origine ne se rattrape pas à la molette. Cette "
               u"question vaut surtout pour son prolongement : si le zoom "
               u"étendue ne montre toujours rien, c'est que les objets sont "
               u"sur un calque masqué ou hors du plan de coupe — et l'on "
               u"cherche alors du bon côté."),

dict(id=u"RH-02", titre=u"Reprendre une implantation par son calque",
     them=u"RH2 · Organisation du document",
     ref=NOTIONS_COUVERTES[u"RH-02"],
     niv=u"Débutant", duree=15, prereq=u"A-04",
     competence=u"Organiser un document Rhino par calques de sorte qu'une "
                u"définition puisse en reprendre une partie sans sélection "
                u"manuelle.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le géomètre livre l'implantation d'un plancher : poteaux "
              u"porteurs et cloisons sont mélangés sur un même calque, alors "
              u"que seuls les porteurs entrent dans la descente de charges.",
     obj=u"Organiser un document Rhino par calques de sorte qu'une définition "
         u"puisse en reprendre une partie sans sélection manuelle.",
     enonce=u"Le fichier fourni contient 18 points d'implantation sur un "
            u"calque unique. Séparez les 12 porteurs des 6 cloisons sur deux "
            u"calques distincts, puis faites compter les porteurs par la "
            u"définition — sans les désigner un par un.",
     depart=u"Un fichier Rhino contenant les 18 points sur le calque "
            u"« IMPLANTATION », et une définition prête à référencer un calque.",
     att=u"12 — le nombre de points sur le calque des porteurs.",
     erreur=u"Sélectionner les porteurs à la main dans la vue plutôt que de "
            u"les isoler sur un calque. Le compte est juste aujourd'hui, et "
            u"faux dès que le géomètre livre une mise à jour — ce que "
            u"l'exercice ne montre qu'à la seconde livraison.",
     donnees_note=u"Les porteurs forment une trame régulière de 5 400 × "
                  u"6 200 mm, les cloisons sont décalées à mi-portée. La "
                  u"distinction est lisible à l'œil dans la vue, ce qui rend "
                  u"le tri manuel tentant — et c'est justement le piège.",
     limite=u"Douze prouve que la SÉPARATION est faite. Que les calques "
            u"portent des noms utilisables par un tiers, et non « calque 01 "
            u"» et « calque 02 », ne se vérifie pas par un nombre — c'est "
            u"pourtant ce qui rend le fichier transmissible.",
     mode=u"SingleValue", tol=u"0", nb=4,
     comp=u"Geometry Pipeline, List Length, Panel",
     etapes=[u"Créer les deux calques, « PORTEURS » et « CLOISONS », avant "
             u"toute sélection.",
             u"Isoler les porteurs par leur régularité — un réseau de "
             u"sélection ou une fenêtre suffit — et les déplacer sur leur "
             u"calque.",
             u"Vérifier qu'il ne reste rien sur le calque d'origine.",
             u"Faire pointer la définition sur le calque des porteurs, pas "
             u"sur une sélection.",
             u"Contrôler que le compte tombe à 12."],
     pieges=[u"Masquer les cloisons au lieu de les déplacer : elles restent "
             u"sur le calque et la définition les reprend quand même.",
             u"Nommer les calques après coup : le lien de la définition se "
             u"fait sur le nom, un renommage le casse."],
     var=[u"Ajouter deux porteurs dans Rhino et vérifier que le compte suit "
          u"tout seul.",
          u"Reprendre les porteurs par un filtre sur la couleur plutôt que "
          u"sur le calque, et juger ce qui est le plus robuste."],
     gamif=u"G-02 Barre de progression",
     bareme=u"1 point si le compte vaut 12 et si aucun point n'a été désigné "
            u"individuellement.",
     verdict=u"competence"),

dict(id=u"RH-03", titre=u"Une trame de plots posée dans Rhino",
     them=u"RH3 · Modélisation Rhino",
     ref=NOTIONS_COUVERTES[u"RH-03"],
     niv=u"Débutant", duree=20, prereq=u"RH-02",
     competence=u"Produire dans Rhino une répétition régulière d'objets à "
                u"partir d'un original et d'un pas, et la faire mesurer.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Une terrasse sur plots demande un plot tous les 600 mm dans "
              u"les deux sens, sur une emprise donnée.",
     obj=u"Produire dans Rhino une répétition régulière d'objets à partir "
         u"d'un original et d'un pas, et la faire mesurer.",
     enonce=u"L'emprise de la terrasse mesure 4 200 mm sur 3 000 mm. Posez un "
            u"plot cylindrique de 100 mm de diamètre à chaque nœud d'une "
            u"trame de 600 mm, le premier au coin d'origine. Donnez le nombre "
            u"de plots.",
            depart=u"Un fichier Rhino avec l'emprise tracée et un plot "
                   u"modèle à l'origine.",
     att=u"48 — huit rangées de six plots.",
     erreur=u"Compter 4 200 ÷ 600 = 7 plots dans la longueur au lieu de 8. "
            u"C'est la confusion entre le nombre d'intervalles et le nombre "
            u"de nœuds, déjà vue en A-10 : ici elle laisse un angle de "
            u"terrasse sans appui.",
     donnees_note=u"L'emprise tombe juste sur la trame dans les deux sens, "
                  u"pour que l'exercice porte sur le décompte et non sur le "
                  u"traitement des rives incomplètes.",
     limite=u"48 plots suppose la trame COMPLÈTE dans l'emprise. Une "
            u"terrasse réelle a des rives : le dernier rang tombe rarement "
            u"juste, et le calepinage décide de le décaler ou de le "
            u"recouper. L'exercice pose le cas où la trame tombe juste.",
     mode=u"SingleValue", tol=u"0", nb=4,
     comp=u"Geometry Pipeline, List Length, Panel",
     etapes=[u"Poser le plot modèle au coin d'origine de l'emprise.",
             u"Établir le nombre de nœuds avant de lancer le réseau : "
             u"4 200 ÷ 600 = 7 intervalles, donc 8 positions.",
             u"Lancer le réseau rectangulaire avec 8 et 6 éléments, pas 7 "
             u"et 5.",
             u"Vérifier visuellement que les quatre angles portent un plot.",
             u"Faire compter les plots par la définition, par leur calque."],
     pieges=[u"Compter les intervalles au lieu des nœuds.",
             u"Réseau lancé depuis le centre du plot modèle sans vérifier que "
             u"le premier tombe bien sur l'angle."],
     var=[u"Porter l'emprise à 4 500 mm et traiter la rive incomplète.",
          u"Passer la trame en quinconce et recompter."],
     gamif=u"G-01 Score visible",
     bareme=u"1 point si le compte vaut 48 et si les quatre angles sont "
            u"appuyés.",
     verdict=u"competence"),

dict(id=u"RH-04", titre=u"Du profil à la surface",
     them=u"RH3 · Modélisation Rhino",
     ref=NOTIONS_COUVERTES[u"RH-04"],
     niv=u"Débutant", duree=20, prereq=u"RH-03",
     competence=u"Passer d'une courbe tracée dans Rhino à une surface, et "
                u"contrôler la grandeur obtenue.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Un bardage courbe se chiffre à la surface développée ; le "
              u"tracé vient d'un relevé, la surface doit en découler.",
     obj=u"Passer d'une courbe tracée dans Rhino à une surface, et contrôler "
         u"la grandeur obtenue.",
     enonce=u"Le relevé fournit la ligne au sol du bardage. Produisez la "
            u"surface du bardage en la montant de 2 800 mm à la verticale, "
            u"puis donnez sa surface en mètres carrés.",
     depart=u"Un fichier Rhino contenant la courbe de relevé au sol.",
     att=u"La surface du bardage, en mètres carrés, à 0,01 près.",
     erreur=u"Monter la surface en suivant la normale de la courbe plutôt "
            u"qu'à la verticale : sur une ligne au sol non plane, la hauteur "
            u"cesse d'être constante et la surface obtenue n'est plus celle "
            u"d'un bardage.",
     donnees_note=u"La ligne au sol présente une courbure variable : une "
                   u"extrusion suivant la normale donnerait un résultat "
                   u"visuellement proche et numériquement différent.",
     limite=u"La surface est celle du BARDAGE DÉVELOPPÉ. Elle ne déduit ni "
            u"les baies ni les recouvrements de lames : la commande se fait "
            u"sur une surface majorée, typiquement de 5 à 10 %.",
     mode=u"NumericTolerance", tol=u"0,01", nb=5,
     comp=u"Geometry Pipeline, Area, Division, Panel",
     etapes=[u"Vérifier que la courbe de relevé est bien une seule courbe, "
             u"non une suite de segments disjoints.",
             u"Monter la surface à la verticale, pas selon la normale.",
             u"Référencer la surface dans la définition par son calque.",
             u"Mesurer l'aire, en millimètres carrés.",
             u"Convertir en mètres carrés : diviser par un million, pas par "
             u"mille."],
     pieges=[u"Une courbe en plusieurs morceaux produit autant de surfaces, "
             u"et l'aire mesurée n'est plus celle d'un seul objet.",
             u"Conversion d'unités : un mètre carré vaut un million de "
             u"millimètres carrés."],
     var=[u"Incliner le bardage de 10° et mesurer l'écart de surface.",
          u"Découper la surface en lés de 1 200 mm et compter les lés."],
     gamif=u"G-06 Cible et précision",
     bareme=u"1 point si la surface est juste à 0,01 m² près.",
     verdict=u"competence"),

dict(id=u"RH-05", titre=u"Percer une platine dans Rhino",
     them=u"RH3 · Modélisation Rhino",
     ref=NOTIONS_COUVERTES[u"RH-05"],
     niv=u"Débutant", duree=15, prereq=u"RH-04",
     competence=u"Combiner des solides par soustraction dans Rhino et "
                u"quantifier la matière retirée.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Une platine d'assemblage reçoit quatre boulons ; la matière "
              u"retirée entre dans le bilan de poids.",
     obj=u"Combiner des solides par soustraction dans Rhino et quantifier la "
         u"matière retirée.",
     enonce=u"La platine mesure 300 × 200 × 15 mm. Percez-la de quatre trous "
            u"traversants de 18 mm de diamètre, centrés à 40 mm de chaque "
            u"bord. Donnez le volume de matière retirée, en millimètres cubes.",
     depart=u"Un fichier Rhino contenant la platine pleine.",
     att=u"15 268 mm³ environ — quatre cylindres de 18 mm de diamètre sur "
         u"15 mm d'épaisseur.",
     erreur=u"Percer avec des cylindres exactement à fleur des faces : "
            u"l'opération booléenne échoue ou laisse une face résiduelle, "
            u"parce que deux surfaces coplanaires ne se coupent pas "
            u"proprement. Il faut faire dépasser les cylindres.",
     donnees_note=u"L'épaisseur de 15 mm et le diamètre de 18 mm sont ceux "
                  u"d'une platine courante pour boulons M16 : les valeurs "
                  u"parlent à qui connaît le métier.",
     limite=u"Le volume retiré est GÉOMÉTRIQUE. Le perçage réel enlève un "
            u"peu plus — ébavurage et jeu du foret — et surtout ne dit rien "
            u"de la tenue de la platine : quatre trous à 40 mm des bords "
            u"affaiblissent une pièce de 15 mm, ce qui est un calcul de "
            u"résistance.",
     mode=u"NumericTolerance", tol=u"1", nb=5,
     comp=u"Geometry Pipeline, Volume, Subtraction, Panel",
     etapes=[u"Poser les quatre cylindres, plus longs que l'épaisseur de la "
             u"platine et débordant des deux côtés.",
             u"Mesurer le volume de la platine pleine avant le perçage.",
             u"Réaliser la soustraction booléenne.",
             u"Mesurer le volume après perçage.",
             u"La différence des deux volumes est la matière retirée — et "
             u"non le volume des cylindres, qui dépassent."],
     pieges=[u"Cylindres à fleur : la booléenne échoue silencieusement ou "
             u"laisse un objet non fermé.",
             u"Prendre le volume des cylindres entiers comme réponse : ils "
             u"dépassent de la platine."],
     var=[u"Passer les trous en oblongs et refaire le calcul.",
          u"Chiffrer le poids retiré, en acier à 7 850 kg/m³."],
     gamif=u"G-11 Chasse à l'erreur",
     bareme=u"1 point si le volume retiré est juste à 1 mm³ près.",
     verdict=u"competence"),

dict(id=u"RH-06", titre=u"Groupe ou bloc ?",
     them=u"RH2 · Organisation du document",
     ref=NOTIONS_COUVERTES[u"RH-06"],
     niv=u"Débutant", duree=6, prereq=u"—",
     competence=u"—", bloom=u"Comprendre × conceptuelle",
     contexte=u"Un même module de façade est répété quarante fois ; le "
              u"client demande d'en changer la meneau.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Un module se répète quarante fois et devra être modifié "
               u"d'un coup. Groupe ou bloc ?\n"
               u"a) Un groupe : il rassemble les objets, c'est fait pour ça.\n"
               u"b) Un bloc : modifier sa définition met à jour les quarante "
               u"instances. ← réponse\n"
               u"c) Les deux se valent, c'est une affaire d'habitude.\n"
               u"d) Ni l'un ni l'autre, il faut un calque par module.\n\n"
               u"Valeur diagnostique : (a) et (c) sont la représentation la "
               u"plus coûteuse du lot. Un groupe ne fait que rassembler une "
               u"sélection ; il faut alors reprendre les quarante copies une "
               u"à une. Le bloc porte une définition unique. La différence "
               u"ne se voit pas au moment où l'on modélise — elle se paie au "
               u"moment où l'on modifie."),

dict(id=u"RH-07", titre=u"Le fichier au mauvais millimètre",
     them=u"RH4 · Précision et unités",
     ref=NOTIONS_COUVERTES[u"RH-07"],
     niv=u"Débutant", duree=7, prereq=u"—",
     competence=u"—", bloom=u"Comprendre × conceptuelle",
     contexte=u"Un modèle reçu d'un partenaire arrive mille fois trop petit.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Un fichier reçu s'affiche mille fois trop petit. Que "
               u"faites-vous ?\n"
               u"a) Mettre le modèle à l'échelle 1000.\n"
               u"b) Vérifier d'abord l'unité du document : il a sans doute "
               u"été modélisé en mètres et ouvert en millimètres. ← réponse\n"
               u"c) Changer l'unité du document, ce qui remet tout d'aplomb "
               u"sans toucher au modèle.\n"
               u"d) Redemander le fichier.\n\n"
               u"Valeur diagnostique : (a) « marche » et laisse une "
               u"tolérance absolue devenue mille fois trop grossière — les "
               u"jonctions cesseront de se fermer sans qu'on comprenne "
               u"pourquoi. (c) est presque juste : changer l'unité ne met "
               u"pas le modèle à l'échelle, il faut choisir explicitement de "
               u"le faire. C'est la nuance que la question sert à révéler."),

dict(id=u"RH-08", titre=u"Un caisson vraiment fermé",
     them=u"RH5 · Préparation à l'impression 3D",
     ref=NOTIONS_COUVERTES[u"RH-08"],
     niv=u"Débutant", duree=25, prereq=u"RH-05",
     competence=u"Établir qu'un solide est réellement étanche, et le "
                u"réparer quand il ne l'est pas.",
     bloom=u"Analyser × procédurale",
     contexte=u"Une pièce partant en impression 3D doit être un volume "
              u"fermé : une enveloppe ouverte n'a pas d'intérieur, et le "
              u"trancheur la refuse ou la remplit n'importe comment.",
     obj=u"Établir qu'un solide est réellement étanche, et le réparer quand "
         u"il ne l'est pas.",
     enonce=u"Le caisson fourni paraît fermé mais ne l'est pas. Trouvez ce "
            u"qui l'empêche, réparez-le, et donnez son volume une fois "
            u"étanche, en millimètres cubes.",
     depart=u"Un fichier Rhino contenant le caisson, 420 × 260 × 180 mm, "
            u"auquel il manque deux faces.",
     att=u"19 656 000 mm³ — le volume du caisson une fois refermé. Une "
         u"enveloppe ouverte n'en a aucun : c'est là toute la preuve.",
     erreur=u"Se fier à l'aspect. Un caisson non fermé s'affiche exactement "
            u"comme un caisson fermé : rien à l'écran ne distingue les deux. "
            u"Seul le contrôle des arêtes nues tranche, et il faut le faire "
            u"avant de mesurer, pas après.",
     donnees_note=u"Le caisson s'affiche exactement comme s'il était fermé : "
                  u"rien à l'écran ne distingue une enveloppe ouverte d'un "
                  u"solide. C'est ce qui rend le contrôle numérique "
                  u"indispensable, et non facultatif.",
     limite=u"Un volume non nul prouve que l'enveloppe est FERMÉE, pas "
            u"qu'elle est propre : des faces retournées, des arêtes "
            u"dupliquées ou une auto-intersection peuvent subsister sans "
            u"empêcher le calcul. Les commandes de vérification les "
            u"diraient ; le volume seul, non.",
     mode=u"NumericTolerance", tol=u"1", nb=6,
     comp=u"Geometry Pipeline, Is Solid, Volume, Panel",
     etapes=[u"Ne pas mesurer d'abord : contrôler d'abord l'étanchéité.",
             u"Afficher les arêtes nues — ce sont elles qui nomment les "
             u"jonctions défaillantes.",
             u"Réparer par jonction des faces adjacentes, en resserrant la "
             u"tolérance si nécessaire.",
             u"Revérifier qu'il ne reste aucune arête nue.",
             u"Mesurer alors le volume : sur une enveloppe ouverte, il "
             u"n'aurait aucun sens."],
     pieges=[u"Mesurer le volume d'un objet non fermé : la valeur sort quand "
             u"même, et elle est fausse.",
             u"Élargir la tolérance jusqu'à ce que ça ferme : les faces "
             u"finissent par se joindre au mauvais endroit."],
     var=[u"Mesurer le volume avant réparation et chiffrer l'écart.",
          u"Ajouter un congé intérieur et refaire le contrôle."],
     gamif=u"G-11 Chasse à l'erreur",
     bareme=u"1 point si l'objet est déclaré solide et si le volume est juste.",
     verdict=u"competence"),

dict(id=u"RH-09", titre=u"Une pièce imprimable",
     them=u"RH5 · Préparation à l'impression 3D",
     ref=NOTIONS_COUVERTES[u"RH-09"],
     niv=u"Débutant", duree=20, prereq=u"RH-08",
     competence=u"Vérifier qu'une pièce respecte les contraintes "
                u"dimensionnelles d'une machine avant de la lancer.",
     bloom=u"Évaluer × procédurale",
     contexte=u"L'imprimante du bureau accepte 220 × 220 × 250 mm et ne tient "
              u"pas une paroi sous 1,2 mm.",
     obj=u"Vérifier qu'une pièce respecte les contraintes dimensionnelles "
         u"d'une machine avant de la lancer.",
     enonce=u"La pièce fournie doit passer sur cette machine. Établissez le "
            u"facteur d'échelle maximal qui la fait tenir dans le volume "
            u"d'impression, arrondi au centième inférieur, et donnez-le.",
     depart=u"Un fichier Rhino contenant la pièce — 380 × 260 × 195 mm hors "
            u"tout — et les cotes du volume d'impression.",
     att=u"0,57 — le facteur limitant vient de la longueur : 220 ÷ 380 "
         u"vaut 0,5789, arrondi vers le bas au centième.",
     erreur=u"Arrondir le facteur au plus proche plutôt qu'au inférieur. À "
            u"0,005 près, la pièce dépasse — et la machine s'en aperçoit "
            u"après trois heures d'impression, pas avant. Le contexte impose "
            u"le sens de l'arrondi, comme en A-06.",
     donnees_note=u"Les trois rapports valent 0,579, 0,846 et 1,282 : le "
                  u"troisième axe passerait sans réduction, et prendre la "
                  u"moyenne des trois donnerait 0,90 — une pièce qui ne "
                  u"rentre pas. C'est le plus petit qui commande.",
     limite=u"0,57 est le facteur GÉOMÉTRIQUE. Une impression réelle "
            u"réserve en plus la place des supports et du bord de plateau, "
            u"et une pièce à 0,57 exactement touche les parois : on descend "
            u"en pratique un ou deux centièmes plus bas.",
     mode=u"NumericTolerance", tol=u"0,01", nb=7,
     comp=u"Geometry Pipeline, Bounding Box, Deconstruct Brep, Division, Panel",
     etapes=[u"Encadrer la pièce pour obtenir ses trois dimensions hors tout.",
             u"Calculer le rapport disponible sur chacun des trois axes.",
             u"Retenir le plus petit des trois : c'est lui qui limite.",
             u"Arrondir vers le bas, jamais au plus proche.",
             u"Contrôler, après mise à l'échelle, que la paroi la plus fine "
             u"reste au-dessus de 1,2 mm."],
     pieges=[u"Prendre la moyenne des trois rapports.",
             u"Oublier que la mise à l'échelle réduit aussi les parois : une "
             u"pièce qui rentre peut devenir non imprimable."],
     var=[u"Faire pivoter la pièce de 90° et voir si le facteur s'améliore.",
          u"Ajouter une marge de 2 mm sur chaque axe et refaire le calcul."],
     gamif=u"G-06 Cible et précision",
     bareme=u"1 point si le facteur est juste et arrondi vers le bas.",
     verdict=u"competence"),

dict(id=u"RH-10", titre=u"Ce que l'export STL perd",
     them=u"RH5 · Préparation à l'impression 3D",
     ref=NOTIONS_COUVERTES[u"RH-10"],
     niv=u"Débutant", duree=7, prereq=u"RH-08",
     competence=u"—", bloom=u"Comprendre × conceptuelle",
     contexte=u"Une pièce parfaitement lisse dans Rhino ressort facettée de "
              u"l'imprimante.",
     obj=u"—", enonce=u"", depart=u"", att=u"", erreur=u"",
     mode=u"—", tol=u"—", nb=0, comp=u"—",
     etapes=[], pieges=[], var=[],
     gamif=u"G-14 Question éclair",
     bareme=u"—",
     verdict=u"connaissance",
     charniere=u"Votre cylindre est parfait dans Rhino, et il sort facetté "
               u"de l'imprimante. Pourquoi ?\n"
               u"a) L'imprimante n'est pas assez précise.\n"
               u"b) Le format STL ne connaît que des triangles : la "
               u"conversion a échantillonné la surface, et la finesse de cet "
               u"échantillonnage est un réglage. ← réponse\n"
               u"c) Le fichier a été enregistré en basse résolution.\n"
               u"d) Il fallait exporter en OBJ.\n\n"
               u"Valeur diagnostique : (a) fait accuser la machine et "
               u"acheter du matériel qui ne changera rien. (d) est faux pour "
               u"la même raison — l'OBJ maille aussi. La bonne réponse "
               u"déplace l'attention vers le seul endroit où l'on peut agir : "
               u"les réglages de maillage au moment de l'export."),
]
