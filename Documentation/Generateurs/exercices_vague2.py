# -*- coding: utf-8 -*-
"""Vague 2 de l'equilibrage, premiere partie : lots RH, GP, QT et MP.

Meme cible que la vague 1 — un exercice par notion, en gros — et memes regles
de la skill. Les treize categories encore en deficit apres la vague 1 y
passent ; celle-ci en traite huit, la suite (`exercices_vague2_avance.py`) en
traite cinq.

Le gros morceau est le SOCLE RHINO : trois categories, douze exercices. Il
avait ete servi en dernier parce qu'il est le plus eloigne de Grasshopper —
mais c'est le prerequis de tout le reste, et une categorie de neuf notions ne
peut pas tenir sur quatre exercices.

TOUTES LES VALEURS SONT CALCULEES par `verifier_vague2.py`, jamais posees.
"""

# ---------------------------------------------------------------------------
# Jeux de donnees
# ---------------------------------------------------------------------------

#: RH-11 — cinquante objets, dont deux tres loin. Le batiment tient dans
#: 8,4 m ; l'etendue du fichier fait 6 km.
D_RH11_BATI = [(x * 1200.0, y * 900.0) for y in range(6) for x in range(8)]
D_RH11_EGARES = [(4850000.0, 12000.0), (-1200000.0, -3000.0)]

#: RH-12 — les altitudes de trente objets. L'une vaut exactement le niveau
#: cherche : c'est elle qui separe « au-dessus » de « au niveau ».
D_RH12_ALTITUDES = [180, 2650, 2810, 940, 3120, 2795, 4400, 2800, 1220, 3980,
                    2799, 5100, 2801, 760, 3450, 2790, 6200, 2820, 1580, 2808,
                    4720, 2788, 3300, 2812, 990, 5600, 2802, 3900, 2796, 2830]
D_RH12_NIVEAU = 2800

#: RH-13 — huit calques, quatre allumes. (nom, allume, nombre d'objets)
D_RH13_CALQUES = [
    (u"00-Reference", False, 12), (u"10-Porteurs", True, 34),
    (u"11-Cloisons", True, 58), (u"20-Menuiseries", True, 21),
    (u"30-Reseaux", False, 47), (u"40-Mobilier", True, 63),
    (u"90-Traces", False, 9), (u"91-Anciens releves", False, 26),
]

#: RH-14 — une trame de plots, percee d'une tremie
D_RH14 = dict(nx=8, ny=6, tremie=(3, 2), pas=1200)

#: RH-15 — le trace d'un cheminement, en plan
D_RH15_PTS = [(0, 0), (2400, 0), (2400, 1800), (5600, 1800),
              (5600, 4300), (9100, 4300)]

#: RH-16 — un bardage rampant
D_RH16 = dict(base=8400.0, profondeur=3200.0, denivele=1500.0)

#: RH-17 — deux volumes qui se recouvrent
D_RH17 = dict(a=(400.0, 300.0, 200.0), b=(250.0, 350.0, 180.0),
              intersection=(150.0, 200.0, 180.0))

#: RH-18 — les epaisseurs de paroi relevees sur une piece. L'une vaut
#: exactement le minimum imprimable.
D_RH18_PAROIS = [2.4, 1.8, 0.9, 3.2, 1.1, 2.0, 0.75, 1.6, 2.8, 1.2,
                 0.95, 4.1, 1.15, 2.2]
D_RH18_MINI = 1.2

#: RH-19 — des details de maquette, et ce que la mise a l'echelle leur fait
D_RH19_DETAILS = [0.031, 0.006, 0.018, 0.009, 0.024, 0.011, 0.038, 0.004,
                  0.015, 0.021, 0.007, 0.028]
D_RH19 = dict(facteur=25.0, resolution=0.4)

#: RH-20 — un maillage triangule : faces et aretes
D_RH20 = dict(faces=2960, aretes=4434)

#: RH-21 — les aires des faces d'un maillage a reparer
D_RH21_AIRES = [12.4, 0.0008, 8.7, 22.1, 0.0003, 5.6, 14.9, 0.0009, 31.2,
                7.3, 0.0012, 19.8, 4.5, 26.7, 0.0006]
D_RH21_TOL = 0.001

#: RH-22 — un cylindre a exporter, et la fleche admise
D_RH22 = dict(rayon=30.0, fleche=0.05)

#: GP-06 et GP-07 — une nappe maillee en quadrangles
D_GP06 = dict(u=48, v=30)

#: GP-08 — une cage de subdivision
D_GP08 = dict(faces=26, passes=3)

#: QT-06 — les postes d'un devis
D_QT06 = dict(materiaux=4820.50, heures=22.5, taux=48.0, marge=0.12, tva=0.10)

#: MP-04 — un graphe, et ce qui se recalcule quand une entree bouge
D_MP04_GRAPHE = {
    u"Largeur": [u"Rectangle"], u"Hauteur": [u"Rectangle"],
    u"Rectangle": [u"Aire", u"Extrusion"],
    u"Aire": [u"Ratio"], u"Extrusion": [u"Volume", u"Enveloppe"],
    u"Volume": [u"Masse"], u"Masse": [u"Cout"], u"Enveloppe": [u"Surface"],
    u"Surface": [u"Isolant"], u"Ratio": [], u"Cout": [], u"Isolant": [],
    u"Essence": [u"Masse"], u"Prix unitaire": [u"Cout"],
}


# ---------------------------------------------------------------------------
# Lot RH — socle Rhino
# ---------------------------------------------------------------------------

LOT_RH = [

dict(id=u"RH-11", titre=u"Ce que le zoom étendue vous apprend",
     them=u"RH1 · Interface et navigation Rhino",
     ref=u"REF-001, REF-002, REF-003",
     niv=u"Débutant", duree=15, prereq=u"RH-01",
     competence=u"Diagnostiquer l'étendue réelle d'un fichier au lieu de "
                u"juger sur ce que l'écran montre.",
     bloom=u"Analyser × procédurale",
     contexte=u"Le fichier arrive du géomètre. Un zoom étendue et l'on ne "
              u"voit plus rien : le bâtiment est devenu un point.",
     obj=u"Diagnostiquer l'étendue réelle d'un fichier au lieu de juger sur "
         u"ce que l'écran montre.",
     enonce=u"Le fichier contient cinquante objets, dont les coordonnées "
            u"vous sont fournies. Donnez l'étendue du fichier selon X, en "
            u"mètres.",
     depart=u"Les coordonnées en plan des cinquante objets, en millimètres.",
     att=u"6 050 m — l'étendue selon X de tout ce que le fichier contient.",
     erreur=u"Répondre 8,4 m, l'étendue du bâtiment. C'est ce que l'on VOIT "
            u"une fois zoomé dessus, et c'est précisément ce que le zoom "
            u"étendue ne montre pas : deux objets égarés à 4,8 km et à "
            u"1,2 km étirent la vue sur six kilomètres, et le bâtiment "
            u"n'occupe plus qu'un cinq-centième de l'écran.",
     donnees_note=u"Quarante-huit objets tiennent dans 8,4 m ; deux sont à "
                  u"des kilomètres, l'un dans chaque sens. Le rapport entre "
                  u"l'étendue vue (8,4 m) et l'étendue réelle (6 050 m) vaut "
                  u"720 : aucune confusion possible entre les deux réponses, "
                  u"et le chiffre dit à lui seul pourquoi l'écran est vide.",
     limite=u"L'exercice mesure l'étendue. Il ne dit pas quoi faire ensuite — "
            u"supprimer les égarés, ou comprendre d'où ils viennent, ce qui "
            u"est souvent plus utile.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Point, Deconstruct, Bounds, Deconstruct Domain, Subtraction, "
          u"Division, Panel",
     etapes=[u"Extraire l'abscisse de chaque objet.",
             u"En prendre les bornes.",
             u"Soustraire, puis convertir en mètres.",
             u"Comparer à l'étendue de ce que l'on croyait voir."],
     pieges=[u"Juger sur l'écran.",
             u"Ne regarder que les objets sélectionnés.",
             u"Confondre étendue et distance à l'origine."],
     var=[u"Donner aussi l'étendue en Y et en Z.",
          u"Trouver les deux objets égarés et dire de quel calque ils "
          u"viennent."],
     gamif=u"G-02 Diagnostic éclair",
     bareme=u"1 point si l'étendue est juste, en mètres.",
     verdict=u"competence"),

dict(id=u"RH-12", titre=u"Ce qui dépasse le niveau",
     them=u"RH1 · Interface et navigation Rhino",
     ref=u"REF-002",
     niv=u"Débutant", duree=15, prereq=u"RH-11",
     competence=u"Compter ce qui franchit un niveau donné, en tranchant "
                u"explicitement le cas de ce qui s'y trouve exactement.",
     bloom=u"Appliquer × procédurale",
     contexte=u"On cherche ce qui dépasse le niveau du faux plafond, posé à "
              u"2 800 mm, pour savoir ce qui devra être repris.",
     obj=u"Compter ce qui franchit un niveau donné, en tranchant "
         u"explicitement le cas de ce qui s'y trouve exactement.",
     enonce=u"Les altitudes des trente objets vous sont fournies. Donnez le "
            u"nombre d'objets qui dépassent strictement le niveau de "
            u"2 800 mm.",
     depart=u"Les trente altitudes, en millimètres, et le niveau du faux "
            u"plafond.",
     att=u"17 objets dépassent strictement 2 800 mm.",
     erreur=u"Compter 18 en incluant l'objet posé exactement à 2 800. La "
            u"consigne dit STRICTEMENT, et sur un chantier la différence "
            u"n'est pas rhétorique : ce qui affleure le plafond passe, ce "
            u"qui le dépasse se reprend.",
     donnees_note=u"Un objet exactement à 2 800, douze autres entre 2 788 et "
                  u"2 820 : la frontière est peuplée, de sorte qu'un "
                  u"comptage à l'œil se trompe, et que le choix entre "
                  u"strict et large change la réponse d'exactement un.",
     limite=u"Dix-sept objets dépassent STRICTEMENT. Un objet posé "
            u"exactement à 2 800 mm ne compte pas ici — c'est une "
            u"convention, et sur un relevé réel, entaché de tolérance, "
            u"cette convention doit être écrite avant de compter.",
     mode=u"SingleValue", tol=u"0", nb=5,
     comp=u"Nombre, Larger Than, Cull Pattern, List Length, Panel",
     etapes=[u"Poser le niveau à comparer.",
             u"Comparer chaque altitude, en choisissant sciemment entre "
             u"strict et large.",
             u"Compter."],
     pieges=[u"Prendre « supérieur ou égal » par défaut.",
             u"Compter à l'œil sur une liste où la frontière est peuplée."],
     var=[u"Donner aussi le compte de ce qui affleure, à 5 mm près.",
          u"Reprendre avec un plafond relevé à 2 850 mm."],
     gamif=u"G-02 Diagnostic éclair",
     bareme=u"1 point si le compte est juste et strict.",
     verdict=u"competence"),

dict(id=u"RH-13", titre=u"Ce que le fichier contient vraiment",
     them=u"RH1 · Interface et navigation Rhino",
     ref=u"REF-006, REF-004",
     niv=u"Débutant", duree=15, prereq=u"RH-02",
     competence=u"Distinguer ce qu'un fichier contient de ce qu'il affiche, "
                u"et compter sur la structure plutôt que sur l'écran.",
     bloom=u"Analyser × conceptuelle",
     contexte=u"Avant d'envoyer le fichier, on veut savoir ce qu'il "
              u"transporte : un calque éteint part quand même, avec tout ce "
              u"qu'il contient.",
     obj=u"Distinguer ce qu'un fichier contient de ce qu'il affiche, et "
         u"compter sur la structure plutôt que sur l'écran.",
     enonce=u"Les huit calques vous sont fournis avec leur état et le nombre "
            u"d'objets de chacun. Donnez le nombre d'objets actuellement "
            u"VISIBLES.",
     depart=u"Les huit calques : nom, allumé ou éteint, nombre d'objets.",
     att=u"176 objets visibles, sur les 270 que contient le fichier.",
     erreur=u"Répondre 270, le contenu du fichier. C'est la bonne réponse à "
            u"une autre question — et c'est justement l'écart entre les deux "
            u"qui compte : 94 objets, dont d'anciens relevés, partiront chez "
            u"le destinataire sans que personne les ait vus.",
     donnees_note=u"Quatre calques allumés sur huit, et les éteints portent "
                  u"un tiers des objets. Les deux réponses — 176 et 270 — "
                  u"sont assez éloignées pour qu'aucune approximation ne les "
                  u"confonde.",
     limite=u"Le compte des objets visibles ne dit rien de leur poids ni de "
            u"ce qu'ils révèlent. Un calque éteint nommé « anciens relevés » "
            u"est un problème de confidentialité avant d'être un problème de "
            u"comptage.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Booléen, Nombre, Cull Pattern, Mass Addition, Panel",
     etapes=[u"Retenir les seuls calques allumés.",
             u"Sommer leurs objets.",
             u"Comparer au total du fichier."],
     pieges=[u"Sommer tous les calques.",
             u"Oublier qu'un calque éteint voyage avec le fichier."],
     var=[u"Donner ce que le fichier transporterait après purge des calques "
          u"éteints.",
          u"Repérer les calques dont le nom seul pose un problème."],
     gamif=u"G-17 Passation",
     bareme=u"1 point si le compte des objets visibles est juste.",
     verdict=u"competence"),

dict(id=u"RH-14", titre=u"La trame percée d'une trémie",
     them=u"RH2 · Modélisation Rhino",
     ref=u"REF-013, REF-008",
     niv=u"Débutant", duree=20, prereq=u"RH-03",
     competence=u"Compter les éléments d'un réseau régulier dont une zone a "
                u"été retirée.",
     bloom=u"Appliquer × procédurale",
     contexte=u"La dalle repose sur une trame de plots, sauf à l'aplomb de "
              u"la trémie d'escalier, où ils sont supprimés.",
     obj=u"Compter les éléments d'un réseau régulier dont une zone a été "
         u"retirée.",
     enonce=u"La trame compte huit plots en longueur et six en largeur, au "
            u"pas de 1 200 mm. La trémie en supprime trois en longueur et "
            u"deux en largeur. Donnez le nombre de plots.",
     depart=u"Les dimensions de la trame, son pas, et l'emprise de la "
            u"trémie en nombre de plots.",
     att=u"42 plots — 48 moins les 6 de la trémie.",
     erreur=u"Retrancher 3 + 2 = 5 au lieu de 3 × 2 = 6. La trémie retire un "
            u"RECTANGLE de plots, pas une ligne et une colonne : l'erreur ne "
            u"se voit pas sur le compte, mais le plot qu'on a oublié de "
            u"retirer se retrouve au milieu de l'escalier.",
     donnees_note=u"Huit par six donne un total, 48, qui ne se confond avec "
                  u"aucune des réponses fausses ; et 3 × 2 = 6 se distingue "
                  u"nettement de 3 + 2 = 5, donc 42 de 43.",
     limite=u"42 plots suppose la trémie ALIGNÉE sur la trame. Une trémie "
            u"quelconque coupe des plots en deux : le compte devient une "
            u"question de calepinage — on décale, on recoupe ou on renonce "
            u"— et non plus une soustraction.",
     mode=u"SingleValue", tol=u"0", nb=5,
     comp=u"Multiplication, Subtraction, Panel",
     etapes=[u"Compter la trame complète.",
             u"Compter l'emprise de la trémie comme un rectangle.",
             u"Soustraire."],
     pieges=[u"Additionner les deux dimensions de la trémie.",
             u"Compter les intervalles au lieu des plots."],
     var=[u"Donner la position du dernier plot depuis l'origine.",
          u"Ajouter une seconde trémie, qui chevauche la première d'un plot."],
     gamif=u"G-04 Comptage réfléchi",
     bareme=u"1 point si le compte est juste.",
     verdict=u"competence"),

dict(id=u"RH-15", titre=u"Le développé d'un cheminement",
     them=u"RH2 · Modélisation Rhino",
     ref=u"REF-009",
     niv=u"Débutant", duree=20, prereq=u"RH-14",
     competence=u"Mesurer la longueur réellement parcourue par une "
                u"polyligne, et non la distance entre ses extrémités.",
     bloom=u"Appliquer × procédurale",
     contexte=u"On chiffre un linéaire de garde-corps le long d'un "
              u"cheminement qui tourne quatre fois.",
     obj=u"Mesurer la longueur réellement parcourue par une polyligne, et "
         u"non la distance entre ses extrémités.",
     enonce=u"Les six sommets du cheminement vous sont fournis. Donnez sa "
            u"longueur développée, en millimètres.",
     depart=u"Les coordonnées en plan des six sommets.",
     att=u"13 400 mm — la somme des cinq segments.",
     erreur=u"Mesurer la distance du premier au dernier point : 10 065 mm. "
            u"C'est la corde, pas le parcours — et 3,3 m de garde-corps "
            u"manqueraient à la livraison.",
     donnees_note=u"Cinq segments orthogonaux de longueurs différentes, et "
                  u"un écart de 25 % entre la corde et le développé : assez "
                  u"grand pour que l'erreur se voie au chiffrage, assez "
                  u"petit pour qu'elle ne saute pas aux yeux sur le plan.",
     limite=u"13 400 mm est la longueur du cheminement PROJETÉ. Un "
            u"cheminement qui monte est plus long que sa projection : sur "
            u"une pente à 5 %, l'écart est de 0,1 %, sur une rampe à 30 %, "
            u"de 4 %. L'exercice traite le cas plan.",
     mode=u"SingleValue", tol=u"0", nb=5,
     comp=u"Point, Polyline, Length, Panel",
     etapes=[u"Relier les sommets dans l'ordre.",
             u"Mesurer la courbe obtenue, et non la distance entre ses "
             u"extrémités."],
     pieges=[u"Mesurer la corde.",
             u"Fermer la polyligne sans que la consigne le demande."],
     var=[u"Donner la longueur de chaque segment, pour le débit.",
          u"Ajouter un congé de 300 mm à chaque angle et reprendre la "
          u"mesure."],
     gamif=u"G-04 Comptage réfléchi",
     bareme=u"1 point si le développé est juste.",
     verdict=u"competence"),

dict(id=u"RH-16", titre=u"La surface d'un rampant",
     them=u"RH2 · Modélisation Rhino",
     ref=u"REF-010, REF-011",
     niv=u"Débutant", duree=20, prereq=u"RH-15",
     competence=u"Mesurer une surface inclinée dans son plan, et non dans sa "
                u"projection horizontale.",
     bloom=u"Appliquer × procédurale",
     contexte=u"On commande la couverture d'un appentis : le couvreur pose "
              u"sur le rampant, le plan le montre en projection.",
     obj=u"Mesurer une surface inclinée dans son plan, et non dans sa "
         u"projection horizontale.",
     enonce=u"L'appentis mesure 8 400 mm de long, 3 200 mm de profondeur en "
            u"projection, pour un dénivelé de 1 500 mm. Donnez la surface de "
            u"couverture à commander, en mètres carrés.",
     depart=u"La longueur, la profondeur en projection et le dénivelé.",
     att=u"29,69 m² — la surface du rampant, à 0,01 près.",
     erreur=u"Multiplier la longueur par la profondeur en projection : "
            u"26,88 m². Il manque 2,81 m², soit près de 10 % — de quoi "
            u"arrêter le chantier à trois rangs de la faîtière.",
     donnees_note=u"Un dénivelé de 1 500 pour 3 200 de projection fait une "
                  u"pente de 25°, courante en appentis. L'écart de 10 % "
                  u"entre les deux réponses est trop petit pour se voir sur "
                  u"un plan, trop grand pour se rattraper sur une commande.",
     limite=u"29,69 m² est la surface du RAMPANT NU. Une couverture se "
            u"commande avec ses recouvrements, ses rives et son faîtage : "
            u"la surface achetée dépasse celle-ci de 10 à 15 % selon le "
            u"matériau.",
     mode=u"NumericTolerance", tol=u"0.01", nb=7,
     comp=u"Multiplication, Addition, Square Root, Division, Panel",
     etapes=[u"Calculer la longueur du rampant par le théorème de "
             u"Pythagore.",
             u"Multiplier par la longueur de l'appentis.",
             u"Convertir en mètres carrés."],
     pieges=[u"Prendre la profondeur en projection pour le rampant.",
             u"Oublier la conversion en mètres carrés."],
     var=[u"Ajouter un débord de 400 mm et reprendre.",
          u"Donner le nombre de plaques de 2 000 × 1 050 mm nécessaires."],
     gamif=u"G-04 Comptage réfléchi",
     bareme=u"1 point si la surface du rampant est juste à 0,01 m² près.",
     verdict=u"competence"),

dict(id=u"RH-17", titre=u"Le volume de deux blocs qui se recouvrent",
     them=u"RH2 · Modélisation Rhino",
     ref=u"REF-012",
     niv=u"Débutant", duree=20, prereq=u"RH-05",
     competence=u"Calculer le volume d'une réunion de solides sans compter "
                u"deux fois la matière commune.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Deux massifs de béton se recoupent en angle. On commande le "
              u"béton au volume.",
     obj=u"Calculer le volume d'une réunion de solides sans compter deux "
         u"fois la matière commune.",
     enonce=u"Le premier massif mesure 400 × 300 × 200 mm, le second "
            u"250 × 350 × 180 mm, et leur recouvrement 150 × 200 × 180 mm. "
            u"Donnez le volume de béton, en décimètres cubes.",
     depart=u"Les dimensions des deux massifs et celles de leur "
            u"recouvrement.",
     att=u"34,35 dm³ — la réunion des deux massifs.",
     erreur=u"Additionner les deux volumes : 39,75 dm³. La zone commune est "
            u"alors comptée deux fois — 5,4 dm³ de béton commandés pour "
            u"rien, et l'erreur se répète à chaque massif de la série.",
     donnees_note=u"Le recouvrement représente 14 % de la réunion : assez "
                  u"pour que l'écart se voie sur une commande, assez peu "
                  u"pour qu'on l'oublie. Les trois volumes sont donnés, de "
                  u"sorte que l'exercice porte sur le raisonnement et non "
                  u"sur la construction géométrique.",
     limite=u"La réunion suppose UN SEUL recouvrement, entièrement contenu "
            u"dans les deux massifs. Trois volumes qui se recoupent deux à "
            u"deux demandent l'inclusion-exclusion complète — retrancher "
            u"les paires puis rajouter le triple — et la formule de "
            u"l'exercice ne s'y étend pas.",
     mode=u"NumericTolerance", tol=u"0.01", nb=8,
     comp=u"Multiplication, Addition, Subtraction, Division, Panel",
     etapes=[u"Calculer chaque volume.",
             u"Additionner les deux massifs.",
             u"Retrancher une fois le recouvrement.",
             u"Convertir en décimètres cubes."],
     pieges=[u"Additionner sans retrancher.",
             u"Retrancher deux fois le recouvrement."],
     var=[u"Traiter trois massifs dont deux recouvrements.",
          u"Donner le volume de la seule zone commune."],
     gamif=u"G-04 Comptage réfléchi",
     bareme=u"1 point si le volume de la réunion est juste.",
     verdict=u"competence"),

dict(id=u"RH-18", titre=u"Les parois que la machine ne saura pas faire",
     them=u"RH3 · Préparation à l'impression 3D",
     ref=u"REF-016",
     niv=u"Débutant", duree=20, prereq=u"RH-08",
     competence=u"Confronter une pièce aux contraintes de la machine avant "
                u"de lancer une impression.",
     bloom=u"Analyser × procédurale",
     contexte=u"La machine ne descend pas sous 1,2 mm de paroi. En deçà, "
              u"elle imprime quelque chose — qui casse à la première "
              u"manipulation.",
     obj=u"Confronter une pièce aux contraintes de la machine avant de "
         u"lancer une impression.",
     enonce=u"Les quatorze épaisseurs de paroi relevées sur la pièce vous "
            u"sont fournies. Donnez le nombre de parois strictement "
            u"inférieures au minimum imprimable de 1,2 mm.",
     depart=u"Les quatorze épaisseurs relevées, en millimètres, et le "
            u"minimum imprimable.",
     att=u"5 parois passent sous le minimum.",
     erreur=u"Compter 6 en incluant la paroi qui vaut exactement 1,2 mm. Le "
            u"minimum est atteignable : c'est un minimum, pas une borne "
            u"exclue. Se tromper de sens conduit à reprendre une paroi qui "
            u"n'en avait pas besoin — ou, dans l'autre sens, à en laisser "
            u"passer une.",
     donnees_note=u"Quatorze relevés, dont un exactement au minimum et trois "
                  u"entre 1,1 et 1,25 : la frontière est peuplée, et le sens "
                  u"de la comparaison change la réponse d'exactement un.",
     limite=u"L'exercice compte les parois trop minces. Il ne dit pas "
            u"comment les épaissir — ce qui suppose de savoir laquelle est "
            u"structurelle et laquelle est décorative.",
     mode=u"SingleValue", tol=u"0", nb=5,
     comp=u"Nombre, Smaller Than, Cull Pattern, List Length, Panel",
     etapes=[u"Comparer chaque épaisseur au minimum.",
             u"Choisir sciemment entre strict et large.",
             u"Compter."],
     pieges=[u"Inclure la paroi qui vaut exactement le minimum.",
             u"Juger sur l'aperçu plutôt que sur les relevés."],
     var=[u"Donner l'épaisseur minimale relevée.",
          u"Reprendre avec une machine descendant à 0,8 mm."],
     gamif=u"G-19 Pièce d'essai",
     bareme=u"1 point si le compte est juste et strict.",
     verdict=u"competence"),

dict(id=u"RH-19", titre=u"Ce que la mise à l'échelle fait aux détails",
     them=u"RH3 · Préparation à l'impression 3D",
     ref=u"REF-017, REF-018",
     niv=u"Débutant", duree=25, prereq=u"RH-07",
     competence=u"Juger la finesse d'un modèle À L'ÉCHELLE OÙ IL SERA "
                u"IMPRIMÉ, et non à celle où il a été dessiné.",
     bloom=u"Analyser × procédurale",
     contexte=u"La maquette d'étude est dessinée au 1:25 et sera imprimée à "
              u"l'échelle 1. La machine ne distingue rien sous 0,4 mm.",
     obj=u"Juger la finesse d'un modèle à l'échelle où il sera imprimé, et "
         u"non à celle où il a été dessiné.",
     enonce=u"Les douze détails les plus fins du modèle vous sont fournis, "
            u"mesurés sur la maquette. Le modèle sera agrandi 25 fois. "
            u"Donnez le nombre de détails qui resteront sous la résolution "
            u"de 0,4 mm APRÈS agrandissement.",
     depart=u"Les douze dimensions relevées sur la maquette, le facteur "
            u"d'agrandissement et la résolution de la machine.",
     att=u"6 détails restent sous la résolution après agrandissement.",
     erreur=u"Juger avant l'agrandissement : les douze détails sont alors "
            u"sous 0,4 mm, et l'on conclut que rien n'est imprimable. "
            u"L'agrandissement en sauve la moitié — refaire toute la "
            u"maquette pour rien est une décision coûteuse fondée sur une "
            u"comparaison faite à la mauvaise échelle.",
     donnees_note=u"Les douze détails sont tous sous la résolution avant "
                  u"agrandissement et six seulement après : les deux "
                  u"réponses, 12 et 6, sont dans un rapport de deux, et la "
                  u"première est aussi le nombre total de détails — ce qui "
                  u"la rend immédiatement suspecte à qui la relit.",
     limite=u"Six détails passent sous la résolution APRÈS agrandissement. "
            u"Le compte est géométrique : il ne dit pas si ces détails "
            u"comptent. Un congé perdu est sans conséquence, un jeu "
            u"fonctionnel perdu bloque l'assemblage, et c'est le concepteur "
            u"qui fait la différence.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Multiplication, Smaller Than, Cull Pattern, List Length, Panel",
     etapes=[u"Appliquer le facteur d'échelle à chaque détail.",
             u"Comparer ensuite à la résolution de la machine.",
             u"Compter."],
     pieges=[u"Comparer avant d'agrandir.",
             u"Oublier que la tolérance du document, elle aussi, suit "
             u"l'échelle."],
     var=[u"Trouver le facteur minimal qui sauve tous les détails.",
          u"Reprendre avec une machine à 0,2 mm de résolution."],
     gamif=u"G-19 Pièce d'essai",
     bareme=u"1 point si le compte après agrandissement est juste.",
     verdict=u"competence"),

dict(id=u"RH-20", titre=u"Un maillage est-il fermé",
     them=u"RH3 · Préparation à l'impression 3D",
     ref=u"REF-019, REF-020, REF-021",
     niv=u"Débutant", duree=25, prereq=u"RH-08",
     competence=u"Établir par le calcul qu'un maillage est ouvert, et de "
                u"combien, sans se fier à son apparence.",
     bloom=u"Analyser × conceptuelle",
     contexte=u"Le maillage part à l'impression. À l'écran, il paraît "
              u"parfaitement fermé — c'est toujours le cas.",
     obj=u"Établir par le calcul qu'un maillage est ouvert, et de combien, "
         u"sans se fier à son apparence.",
     enonce=u"Le maillage compte 2 960 faces triangulaires et 4 434 arêtes. "
            u"Donnez le nombre d'arêtes nues.",
     depart=u"Le nombre de faces triangulaires et le nombre d'arêtes.",
     att=u"12 arêtes nues.",
     erreur=u"Conclure que le maillage est fermé parce que rien ne se voit. "
            u"Un maillage fermé de 2 960 triangles aurait exactement "
            u"4 440 arêtes : chaque arête y est partagée par deux faces. "
            u"Il en manque six, donc douze arêtes ne sont bordées que d'une "
            u"seule face — et la pièce sortira de la machine avec un trou.",
     donnees_note=u"Le raisonnement tient en une ligne : trois arêtes par "
                  u"triangle, deux triangles par arête intérieure, donc "
                  u"3F − 2E arêtes nues. Douze arêtes nues sur 4 434, c'est "
                  u"0,3 % — invisible à l'œil, rédhibitoire à la machine.",
     limite=u"Le compte dit qu'il y a des trous, pas où ils sont. Les "
            u"localiser demande les outils d'analyse, que RH-21 aborde.",
     mode=u"SingleValue", tol=u"0", nb=5,
     comp=u"Multiplication, Subtraction, Panel",
     etapes=[u"Compter les arêtes qu'exigent les faces : trois par "
             u"triangle.",
             u"Compter celles qu'offrent les arêtes réelles : deux usages "
             u"chacune si elles sont intérieures.",
             u"La différence est le nombre d'arêtes nues."],
     pieges=[u"Se fier à l'aperçu.",
             u"Confondre arêtes nues et faces manquantes."],
     var=[u"Retrouver le nombre d'arêtes d'un maillage fermé de même "
          u"nombre de faces.",
          u"Refaire le calcul pour un maillage quadrangulaire."],
     gamif=u"G-19 Pièce d'essai",
     bareme=u"1 point si le nombre d'arêtes nues est juste.",
     verdict=u"competence"),

dict(id=u"RH-21", titre=u"Les faces qui ne mesurent rien",
     them=u"RH3 · Préparation à l'impression 3D",
     ref=u"REF-022, REF-023",
     niv=u"Débutant", duree=20, prereq=u"RH-20",
     competence=u"Repérer les faces dégénérées d'un maillage avant de le "
                u"réparer, en s'appuyant sur la tolérance du document.",
     bloom=u"Analyser × procédurale",
     contexte=u"Le maillage vient d'une conversion. Certaines faces sont "
              u"réduites à un fil : elles ne se voient pas, et font échouer "
              u"la réparation automatique.",
     obj=u"Repérer les faces dégénérées d'un maillage avant de le réparer, "
         u"en s'appuyant sur la tolérance du document.",
     enonce=u"Les aires des quinze faces suspectes vous sont fournies, en "
            u"millimètres carrés. La tolérance du document vaut 0,001 mm². "
            u"Donnez le nombre de faces dégénérées.",
     depart=u"Les quinze aires relevées et la tolérance du document.",
     att=u"4 faces dégénérées.",
     erreur=u"Comparer à zéro. Aucune face n'a une aire exactement nulle : "
            u"elles valent 0,0003 à 0,0012 mm², ce qui n'est pas zéro mais "
            u"n'est rien à l'échelle du document. Une comparaison à zéro "
            u"n'en trouve aucune, et la réparation échoue sans dire "
            u"pourquoi.",
     donnees_note=u"Cinq faces sous le millième de millimètre carré, dont "
                  u"une à 0,0012 qui passe JUSTE au-dessus de la "
                  u"tolérance : la réponse est 4, et non 5. C'est la "
                  u"tolérance qui tranche, pas l'intuition.",
     limite=u"Quatre faces sont dégénérées AU REGARD de la tolérance du "
            u"document. Changer cette tolérance change le compte : c'est "
            u"une propriété du fichier, pas de la géométrie, et deux "
            u"ouvertures du même modèle peuvent ne pas s'accorder.",
     mode=u"SingleValue", tol=u"0", nb=5,
     comp=u"Nombre, Smaller Than, Cull Pattern, List Length, Panel",
     etapes=[u"Comparer chaque aire à la tolérance, et non à zéro.",
             u"Compter.",
             u"Retenir que la face à 0,0012 n'est pas dégénérée au sens du "
             u"document."],
     pieges=[u"Comparer à zéro.",
             u"Prendre une tolérance choisie au jugé plutôt que celle du "
             u"document."],
     var=[u"Reprendre avec une tolérance de 0,01 mm².",
          u"Donner l'aire totale perdue par la suppression de ces faces."],
     gamif=u"G-19 Pièce d'essai",
     bareme=u"1 point si le compte est juste.",
     verdict=u"competence"),

dict(id=u"RH-22", titre=u"La finesse du maillage à l'export",
     them=u"RH3 · Préparation à l'impression 3D",
     ref=u"REF-024",
     niv=u"Débutant", duree=25, prereq=u"RH-10",
     competence=u"Régler la finesse d'un maillage d'export à partir de "
                u"l'écart admissible à la surface, et non au jugé.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le cylindre part en fabrication. Le maillage d'export "
              u"remplace le cercle par un polygone : la question est de "
              u"savoir de combien il s'en écarte.",
     obj=u"Régler la finesse d'un maillage d'export à partir de l'écart "
         u"admissible à la surface, et non au jugé.",
     enonce=u"Le cylindre a 30 mm de rayon. L'écart entre le maillage et la "
            u"surface réelle ne doit pas dépasser 0,05 mm. Donnez le nombre "
            u"minimal de facettes sur un demi-tour.",
     depart=u"Le rayon du cylindre et l'écart maximal admis.",
     att=u"55 facettes sur un demi-tour.",
     erreur=u"Régler la finesse sur un curseur, au jugé, jusqu'à ce que "
            u"l'aperçu paraisse lisse. L'aperçu paraît lisse bien avant que "
            u"l'écart soit tenu — à 54 facettes il vaut déjà 0,0508 mm, "
            u"au-delà du toléré, et rien à l'écran ne le signale.",
     donnees_note=u"L'écart d'une corde à son arc vaut r(1 − cos(π/n)). "
                  u"Avec r = 30 et 0,05 mm admis, n vaut 54,41 : la "
                  u"frontière tombe entre deux entiers, de sorte qu'un "
                  u"arrondi au plus proche donnerait 54 — qui ne tient pas "
                  u"l'écart. C'est un arrondi au SUPÉRIEUR.",
     limite=u"Le calcul porte sur la circonférence. La finesse selon "
            u"l'axe, elle, ne dépend pas de l'écart mais du procédé.",
     mode=u"SingleValue", tol=u"0", nb=8,
     comp=u"Division, Subtraction, ArcCos, Pi, Round, Panel",
     etapes=[u"Écrire l'écart entre la corde et l'arc en fonction du "
             u"nombre de facettes.",
             u"Inverser la relation pour obtenir le nombre de facettes.",
             u"Arrondir au SUPÉRIEUR.",
             u"Vérifier l'écart obtenu, et celui d'une facette de moins."],
     pieges=[u"Arrondir au plus proche.",
             u"Régler au jugé sur l'aperçu.",
             u"Confondre l'écart à la surface et la longueur de la corde."],
     var=[u"Refaire pour un rayon de 5 mm : le nombre de facettes change "
          u"peu, le poids du fichier beaucoup.",
          u"Chiffrer le poids du fichier obtenu."],
     gamif=u"G-19 Pièce d'essai",
     bareme=u"1 point si le nombre de facettes est juste et arrondi au "
            u"supérieur.",
     verdict=u"competence"),

]


# ---------------------------------------------------------------------------
# Lot GP — geometrie parametrique appliquee
# ---------------------------------------------------------------------------

LOT_GP = [

dict(id=u"GP-06", titre=u"Les sommets d'une nappe maillée",
     them=u"GP4 · Maillages et SubD",
     ref=u"REF-074",
     niv=u"Perfectionnement", duree=20, prereq=u"GP-03",
     competence=u"Distinguer le nombre de faces d'un maillage de son nombre "
                u"de sommets, et savoir lequel commande quoi.",
     bloom=u"Comprendre × conceptuelle",
     contexte=u"La nappe part vers un calcul aux éléments finis, qui se "
              u"dimensionne au nombre de NŒUDS, pas de faces.",
     obj=u"Distinguer le nombre de faces d'un maillage de son nombre de "
         u"sommets, et savoir lequel commande quoi.",
     enonce=u"La nappe est maillée en 48 divisions dans un sens et 30 dans "
            u"l'autre, en quadrangles. Donnez le nombre de sommets.",
     depart=u"Les deux nombres de divisions.",
     att=u"1 519 sommets — 49 × 31.",
     erreur=u"Répondre 1 440, le nombre de faces. Un maillage de n divisions "
            u"a n + 1 rangées de sommets : l'écart de 79 sommets ne se voit "
            u"pas sur l'image, mais il change la taille du système à "
            u"résoudre.",
     donnees_note=u"48 et 30 sont des divisions courantes pour une nappe "
                  u"d'étude. Les deux réponses — 1 440 et 1 519 — sont "
                  u"assez proches pour qu'on ne les distingue pas à vue, "
                  u"assez différentes pour que le calcul ne soit pas le "
                  u"même.",
     limite=u"1 519 sommets vaut pour une nappe OUVERTE. Refermer la nappe "
            u"sur elle-même — un cylindre, un tore — soude une rangée de "
            u"sommets à une autre, et le compte tombe. La formule (n+1)(m+1) "
            u"suppose que rien ne se recolle.",
     mode=u"SingleValue", tol=u"0", nb=5,
     comp=u"Addition, Multiplication, Panel",
     etapes=[u"Compter les rangées de sommets dans chaque sens : une de "
             u"plus que les divisions.",
             u"Multiplier."],
     pieges=[u"Multiplier les divisions entre elles.",
             u"Oublier que le maillage n'est pas fermé sur lui-même."],
     var=[u"Donner le nombre d'arêtes.",
          u"Reprendre pour une nappe refermée dans un sens."],
     gamif=u"G-04 Comptage réfléchi",
     bareme=u"1 point si le nombre de sommets est juste.",
     verdict=u"competence"),

dict(id=u"GP-07", titre=u"Ce que la soudure retire",
     them=u"GP4 · Maillages et SubD",
     ref=u"REF-076",
     niv=u"Perfectionnement", duree=25, prereq=u"GP-06",
     competence=u"Mesurer la redondance d'un maillage construit face par "
                u"face, et ce que la soudure des sommets lui retire.",
     bloom=u"Analyser × procédurale",
     contexte=u"Le maillage a été construit quadrangle par quadrangle. "
              u"Chaque face porte ses quatre sommets, sans savoir que ses "
              u"voisines portent les mêmes.",
     obj=u"Mesurer la redondance d'un maillage construit face par face, et "
         u"ce que la soudure des sommets lui retire.",
     enonce=u"La nappe compte 48 divisions par 30, en quadrangles construits "
            u"un à un. Donnez le nombre de sommets que la soudure "
            u"supprimera.",
     depart=u"Les deux nombres de divisions, et le mode de construction "
            u"face par face.",
     att=u"4 241 sommets supprimés — de 5 760 à 1 519.",
     erreur=u"Répondre 1 519, le nombre de sommets APRÈS soudure, au lieu du "
            u"nombre supprimé. Les deux chiffres racontent la même "
            u"opération, mais seul le second dit ce que le maillage "
            u"transportait pour rien : près des trois quarts de ses "
            u"sommets.",
     donnees_note=u"Quatre sommets par quadrangle non soudé contre 1 519 "
                  u"après soudure : le maillage brut est 3,8 fois plus lourd "
                  u"que nécessaire. C'est l'ordre de grandeur réel d'un "
                  u"maillage produit face par face, et la raison pour "
                  u"laquelle un fichier d'export paraît parfois "
                  u"inexplicablement gros.",
     limite=u"La soudure suppose une tolérance. Trop large, elle referme "
            u"des arêtes qui devaient rester ouvertes — l'exercice ne "
            u"traite pas ce réglage.",
     mode=u"SingleValue", tol=u"0", nb=7,
     comp=u"Multiplication, Addition, Subtraction, Panel",
     etapes=[u"Compter les sommets du maillage non soudé : quatre par "
             u"face.",
             u"Compter ceux du maillage soudé.",
             u"Soustraire."],
     pieges=[u"Rendre le nombre de sommets restants.",
             u"Compter trois sommets par face, comme pour un triangle."],
     var=[u"Chiffrer le gain de poids du fichier exporté.",
          u"Refaire le calcul pour un maillage triangulé."],
     gamif=u"G-16 Livrable pesé",
     bareme=u"1 point si le nombre de sommets supprimés est juste.",
     verdict=u"competence"),

dict(id=u"GP-08", titre=u"Ce que coûte une subdivision de plus",
     them=u"GP4 · Maillages et SubD",
     ref=u"REF-077, REF-078",
     niv=u"Perfectionnement", duree=20, prereq=u"GP-04",
     competence=u"Anticiper la croissance d'une surface de subdivision, et "
                u"choisir le niveau d'affichage en connaissance de cause.",
     bloom=u"Analyser × conceptuelle",
     contexte=u"La cage de subdivision est légère et se manipule bien. "
              u"C'est l'affichage lissé qui fait ramer la machine.",
     obj=u"Anticiper la croissance d'une surface de subdivision, et choisir "
         u"le niveau d'affichage en connaissance de cause.",
     enonce=u"La cage compte 26 faces. Chaque passe de subdivision remplace "
            u"chaque face par quatre. Donnez le nombre de faces après trois "
            u"passes.",
     depart=u"Le nombre de faces de la cage et le nombre de passes.",
     att=u"1 664 faces après trois passes.",
     erreur=u"Multiplier une seule fois par quatre (104), ou multiplier par "
            u"trois (78). La croissance est GÉOMÉTRIQUE : chaque passe "
            u"quadruple ce que la précédente a produit. C'est pour cela "
            u"qu'une passe de plus, décidée sans y penser, fait passer un "
            u"modèle fluide à un modèle inutilisable.",
     donnees_note=u"26 faces est la taille d'une cage de mobilier. Les trois "
                  u"réponses possibles — 78, 104 et 1 664 — sont séparées "
                  u"d'un ordre de grandeur, ce qui rend chaque erreur "
                  u"immédiatement lisible.",
     limite=u"1 664 faces est un compte de TOPOLOGIE, pas de coût. Le poids "
            u"réel d'une subdivision dépend aussi de ce qui est calculé sur "
            u"chaque face — aperçu, matériau, analyse — et deux cages de "
            u"même compte peuvent tenir ou saturer selon ce qui les suit.",
     mode=u"SingleValue", tol=u"0", nb=5,
     comp=u"Multiplication, Panel",
     etapes=[u"Comprendre que la croissance est géométrique.",
             u"Élever quatre à la puissance du nombre de passes.",
             u"Multiplier par le nombre de faces de la cage."],
     pieges=[u"Multiplier par le nombre de passes.",
             u"N'appliquer le facteur qu'une fois."],
     var=[u"Trouver le nombre de passes qui dépasse cent mille faces.",
          u"Comparer au coût d'affichage d'un maillage équivalent."],
     gamif=u"G-04 Comptage réfléchi",
     bareme=u"1 point si le nombre de faces est juste.",
     verdict=u"competence"),

]


# ---------------------------------------------------------------------------
# Lot QT — quantitatifs, chiffrage et export
# ---------------------------------------------------------------------------

LOT_QT = [

dict(id=u"QT-06", titre=u"Du métré au devis",
     them=u"QT2 · Quantitatifs et chiffrage",
     ref=u"REF-083",
     niv=u"Intermédiaire", duree=30, prereq=u"QT-02",
     competence=u"Enchaîner les coefficients d'un devis dans le bon ordre, "
                u"en sachant sur quelle assiette chacun s'applique.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le métré est fait. Reste à en faire un devis : main "
              u"d'œuvre, marge, puis taxe — et pas dans un autre ordre.",
     obj=u"Enchaîner les coefficients d'un devis dans le bon ordre, en "
         u"sachant sur quelle assiette chacun s'applique.",
     enonce=u"Les matériaux reviennent à 4 820,50 €. La pose demande "
            u"22,5 heures à 48 € l'heure. La marge est de 12 %, la taxe de "
            u"10 %. Donnez le montant toutes taxes comprises, en euros.",
     depart=u"Le coût des matériaux, les heures et leur taux, le taux de "
            u"marge et celui de la taxe.",
     att=u"7 269,42 € toutes taxes comprises.",
     erreur=u"Oublier la marge et facturer 6 490,55 €. L'écart, 778,87 €, "
            u"est exactement ce que l'entreprise gagnait sur le chantier : "
            u"le devis reste plausible, il est simplement à prix coûtant.",
     donnees_note=u"Les taux — 12 % de marge, 10 % de taxe — sont ceux du "
                  u"bâtiment en rénovation. Marge et taxe étant toutes deux "
                  u"multiplicatives, leur ORDRE ne change pas le total : "
                  u"c'est l'oubli de l'une qui se voit, pas leur "
                  u"permutation, et l'exercice porte donc sur ce qui compte "
                  u"vraiment.",
     limite=u"Le calcul suppose une marge sur le déboursé sec. Beaucoup "
            u"d'entreprises appliquent des coefficients distincts aux "
            u"matériaux et à la main d'œuvre — la structure du calcul reste "
            u"la même.",
     mode=u"NumericTolerance", tol=u"0.01", nb=8,
     comp=u"Multiplication, Addition, Panel",
     etapes=[u"Chiffrer la main d'œuvre.",
             u"Ajouter les matériaux : c'est le déboursé sec.",
             u"Appliquer la marge.",
             u"Appliquer la taxe."],
     pieges=[u"Oublier la marge.",
             u"Appliquer la marge aux seuls matériaux.",
             u"Confondre marge et taux de marque."],
     var=[u"Séparer les coefficients matériaux et main d'œuvre.",
          u"Retrouver le prix de vente qui atteint une marge visée."],
     gamif=u"G-11 Commande à passer",
     bareme=u"1 point si le montant TTC est juste au centime.",
     verdict=u"competence"),

]


# ---------------------------------------------------------------------------
# Lot MP — methode, performance et evenements
# ---------------------------------------------------------------------------

LOT_MP = [

dict(id=u"MP-04", titre=u"Ce qu'un curseur fait recalculer",
     them=u"MP1 · Chronologie et évènements",
     ref=u"REF-090",
     niv=u"Perfectionnement", duree=25, prereq=u"MP-02",
     competence=u"Déterminer ce qu'une modification fait recalculer, en "
                u"suivant les dépendances plutôt qu'en supposant que tout "
                u"repasse.",
     bloom=u"Analyser × conceptuelle",
     contexte=u"La définition met trois secondes à répondre au moindre "
              u"mouvement de curseur. Avant d'optimiser quoi que ce soit, "
              u"il faut savoir ce qui repasse réellement.",
     obj=u"Déterminer ce qu'une modification fait recalculer, en suivant les "
         u"dépendances plutôt qu'en supposant que tout repasse.",
     enonce=u"Les liaisons du graphe vous sont fournies. Donnez le nombre de "
            u"composants qui se recalculent lorsque le curseur Largeur est "
            u"déplacé.",
     depart=u"Les quatorze composants du graphe et leurs liaisons.",
     att=u"10 composants se recalculent.",
     erreur=u"Répondre 13, tout le graphe moins le curseur. Grasshopper ne "
            u"recalcule que ce qui DÉPEND de ce qui a changé : Hauteur, "
            u"Essence et Prix unitaire ne dépendent pas de Largeur, et "
            u"restent intacts. Croire que tout repasse conduit à optimiser "
            u"au mauvais endroit.",
     donnees_note=u"Quatorze composants, dont trois entrées indépendantes et "
                  u"un graphe à deux branches qui se rejoignent : suivre les "
                  u"dépendances à la main est faisable mais fastidieux, et "
                  u"c'est exactement le genre de comptage qu'on préfère "
                  u"supposer plutôt que faire.",
     limite=u"Le compte des composants n'est pas le compte des secondes : "
            u"un seul composant lourd pèse plus que neuf légers. C'est le "
            u"profileur qui le dit, et MP-02 qui l'aborde.",
     mode=u"SingleValue", tol=u"0", nb=7,
     comp=u"Texte, Member Index, Cull Pattern, List Length, Panel",
     etapes=[u"Partir du composant modifié.",
             u"Suivre les liaisons vers l'aval, de proche en proche.",
             u"Compter ce qui a été atteint, sans compter deux fois ce que "
             u"deux branches atteignent."],
     pieges=[u"Compter tout le graphe.",
             u"Compter deux fois un composant atteint par deux chemins.",
             u"Remonter vers l'amont : ce qui alimente un composant ne se "
             u"recalcule pas parce qu'il change."],
     var=[u"Refaire le compte pour le curseur Essence.",
          u"Trouver l'entrée dont la modification recalcule le moins."],
     gamif=u"G-13 Chronomètre",
     bareme=u"1 point si le compte des composants recalculés est juste.",
     verdict=u"competence"),

]
