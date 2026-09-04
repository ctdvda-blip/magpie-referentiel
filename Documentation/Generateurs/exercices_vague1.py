# -*- coding: utf-8 -*-
"""Vague 1 de l'equilibrage : les dix categories qui n'avaient qu'un exercice.

POURQUOI CETTE VAGUE
--------------------
Le referentiel compte 41 categories, de 1 a 9 exercices chacune. La cible
retenue est PROPORTIONNELLE AU NOMBRE DE NOTIONS : une categorie de trois
notions merite trois exercices, une categorie d'une notion en merite un. Ni les
domaines ni les categories ne sont alors egaux entre eux — et c'est voulu : un
domaine de 26 notions n'a pas a recevoir autant qu'un domaine de trois.

Cette premiere vague traite les dix categories les plus pauvres, celles qui
n'avaient qu'UN seul exercice pour deux ou trois notions. Elles portaient
toutes le meme defaut : un exercice-parapluie qui couvrait la categorie
entiere, donc aucune n'etait traitee en propre.

CE QUI A GUIDE LA REDACTION
---------------------------
La skill magpie-conception-exercices v2.3, et en particulier :

- §1 une competence, jamais une connaissance. Quatre items de cette vague sont
  des CONNAISSANCES : ils deviennent des questions charnieres, pas de faux
  exercices. Un cinquieme livre un plugin installe : il se note sur grille.
- §5 des donnees non devinables et une reponse qu'on ne trouve pas de tete.
- §6 une erreur attendue qui produit un resultat DIFFERENT, donc lisible.
- Contraintes du checker : entiers en SingleValue, NumericTolerance des que la
  valeur attendue est decimale, jamais de booleen ni de texte sur REPONSE.

TOUTES LES VALEURS ATTENDUES ONT ETE CALCULEES, pas posees de tete. Le script
de verification est `verifier_vague1.py`, a cote de ce fichier : il recalcule
chaque reponse depuis les donnees et signale tout desaccord avec la fiche.
"""

# ---------------------------------------------------------------------------
# Jeux de donnees, partages entre la fiche, la definition et la verification
# ---------------------------------------------------------------------------

#: GP-05 — une facade de sept percements, cotes en chaine depuis l'origine
D_GP05_ORIGINE = 420
D_GP05_ENTRAXES = [1240, 980, 1615, 1105, 1430, 875, 1290]

#: QT-04 et QT-05 — un debit de vingt-quatre lignes pour huit references.
#: Les references se repetent dans le desordre : c'est ce qui oblige a
#: regrouper plutot qu'a lire.
D_QT04_DEBIT = [
    (u"MEL-19-CHENE", 4), (u"MEL-19-BLANC", 6), (u"CP-18-BOUL", 2),
    (u"MEL-19-CHENE", 3), (u"MAS-27-HETRE", 5), (u"CP-18-BOUL", 7),
    (u"MEL-19-BLANC", 2), (u"MDF-22-BRUT", 8), (u"MEL-19-CHENE", 6),
    (u"MAS-27-HETRE", 1), (u"CP-12-PEUPL", 4), (u"MDF-22-BRUT", 3),
    (u"MEL-19-BLANC", 5), (u"CP-18-BOUL", 1), (u"MAS-40-CHENE", 2),
    (u"MEL-19-CHENE", 2), (u"CP-12-PEUPL", 6), (u"MDF-16-BRUT", 4),
    (u"MAS-27-HETRE", 3), (u"MEL-19-BLANC", 4), (u"CP-18-BOUL", 5),
    (u"MDF-22-BRUT", 2), (u"MAS-40-CHENE", 6), (u"MDF-16-BRUT", 3),
]

#: FA-03 — un profil en U plie dans la tole, cotes EXTERIEURES comme sur un
#: plan de tolerie. Le facteur K place la fibre neutre : c'est la seule fibre
#: qui garde sa longueur au pliage, et elle n'est pas au milieu de
#: l'epaisseur.
D_FA03 = dict(aile=120.0, ame=300.0, epaisseur=3.0, rayon=5.0, k=0.42)

#: FA-04 — le volume de construction de la machine, l'encombrement de la
#: piece, et l'ecart a respecter entre deux pieces comme entre une piece et
#: une paroi.
D_FA04 = dict(plateau=(250.0, 210.0, 210.0), piece=(62.0, 38.0, 95.0),
              ecart=4.0)


# ---------------------------------------------------------------------------
# Lot GP — geometrie parametrique appliquee
# ---------------------------------------------------------------------------

LOT_GP = [

dict(id=u"GP-05", titre=u"La chaîne de cotes d'une façade",
     them=u"GP3 · Plan paramétrique",
     ref=u"REF-065, REF-066",
     niv=u"Intermédiaire", duree=25, prereq=u"GP-01",
     competence=u"Produire une cotation en chaîne qui se recalcule avec le "
                u"modèle, en distinguant ce qui se mesure d'un voisin à "
                u"l'autre de ce qui se repère depuis une origine unique.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le poseur implante les percements d'une façade au décamètre, "
              u"depuis un unique point de référence : c'est la seule manière "
              u"de ne pas cumuler les erreurs de report.",
     obj=u"Produire une cotation en chaîne qui se recalcule avec le modèle, "
         u"en distinguant ce qui se mesure d'un voisin à l'autre de ce qui "
         u"se repère depuis une origine unique.",
     enonce=u"Le bureau d'études fournit les entraxes des sept percements, "
            u"mesurés chacun depuis le précédent, et la distance du premier "
            u"au point de référence. Donnez la cote du dernier percement "
            u"telle qu'elle doit figurer au plan de pose, en millimètres.",
     depart=u"La distance du premier percement au point de référence, et les "
            u"sept entraxes successifs, en millimètres.",
     att=u"8 955 mm — la position du dernier percement, comptée depuis le "
         u"point de référence.",
     erreur=u"Reporter le dernier entraxe (1 290 mm) ou la somme des seuls "
            u"entraxes (8 535 mm). Le premier oublie que l'entraxe est une "
            u"distance relative ; le second oublie l'écart d'origine. Sur le "
            u"chantier, les deux se traduisent par un percement au mauvais "
            u"endroit — et l'un des deux le met à 420 mm près, un écart "
            u"assez petit pour n'être vu qu'une fois la menuiserie livrée.",
     donnees_note=u"Sept entraxes irréguliers, aucun multiple d'un pas "
                  u"commun : la cote finale ne se retrouve pas de tête. "
                  u"L'écart d'origine de 420 mm est du même ordre qu'un "
                  u"tableau de baie, donc plausible et facile à oublier.",
     limite=u"L'exercice valide la cote finale, pas la cotation entière. "
            u"Une chaîne juste sur son dernier maillon peut être fausse au "
            u"milieu : le formateur regarde le graphe, pas seulement la "
            u"réponse.",
     mode=u"SingleValue", tol=u"0", nb=5,
     comp=u"Nombre, Mass Addition, Addition, Panel",
     etapes=[u"Distinguer la donnée relative (l'entraxe) de la donnée "
             u"absolue (la position depuis l'origine).",
             u"Cumuler les entraxes.",
             u"Ajouter l'écart d'origine.",
             u"Vérifier que la première cote vaut bien l'écart d'origine, et "
             u"non zéro."],
     pieges=[u"Confondre entraxe et cote cumulée.",
             u"Oublier l'écart entre le point de référence et le premier "
             u"percement.",
             u"Coter chaque percement depuis son voisin sur le plan de "
             u"pose : les erreurs de report s'additionnent alors."],
     var=[u"Produire la chaîne complète des huit cotes, et non la seule "
          u"dernière.",
          u"Ajouter un percement au milieu et vérifier que toutes les cotes "
          u"suivantes se recalculent seules."],
     gamif=u"G-08 Relevé contradictoire",
     bareme=u"1 point si la cote finale est juste.",
     verdict=u"competence"),

]


# ---------------------------------------------------------------------------
# Lot QT — quantitatifs, chiffrage et export
# ---------------------------------------------------------------------------

LOT_QT = [

dict(id=u"QT-04", titre=u"Un débit qui devient une commande",
     them=u"QT3 · Export de données",
     ref=u"REF-085",
     niv=u"Intermédiaire", duree=30, prereq=u"QT-01",
     competence=u"Regrouper un relevé ligne à ligne en une table par "
                u"référence, de sorte que chaque référence n'apparaisse "
                u"qu'une fois avec sa quantité cumulée.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le débit sort de l'atelier ligne par ligne, dans l'ordre du "
              u"montage. Le fournisseur, lui, veut une commande : une ligne "
              u"par référence, et la quantité totale.",
     obj=u"Regrouper un relevé ligne à ligne en une table par référence, de "
         u"sorte que chaque référence n'apparaisse qu'une fois avec sa "
         u"quantité cumulée.",
     enonce=u"Le débit vous est fourni tel qu'il sort de l'atelier : "
            u"vingt-quatre lignes, dans le désordre, où la même référence "
            u"revient plusieurs fois. Donnez la quantité totale de la "
            u"référence la plus commandée.",
     depart=u"Les vingt-quatre lignes du débit : une référence de panneau et "
            u"une quantité par ligne.",
     att=u"17 — la quantité cumulée de la référence la plus commandée.",
     erreur=u"Prendre la plus grande quantité d'une seule ligne (8) au lieu "
            u"du cumul par référence. La table n'est alors pas regroupée : "
            u"elle est seulement triée, et le fournisseur recevra "
            u"vingt-quatre lignes dont huit références en double.",
     donnees_note=u"Vingt-quatre lignes pour huit références, réparties de "
                  u"façon que la référence la plus FRÉQUENTE (quatre lignes) "
                  u"ne soit pas celle qui porte la plus grosse ligne "
                  u"unitaire : compter les occurrences donne une autre "
                  u"réponse que cumuler les quantités. Les deux suivantes "
                  u"sont à 15, assez proches pour qu'un cumul approximatif "
                  u"se trompe de référence.",
     limite=u"Le cumul dit ce qu'il faut COMMANDER, pas ce qu'il faut "
            u"payer : les fournisseurs vendent par conditionnement, et "
            u"dix-sept pièces se commandent souvent par vingt. Le passage "
            u"du besoin au bon de commande n'est pas traité ici.",
     mode=u"SingleValue", tol=u"0", nb=7,
     comp=u"Texte, Nombre, Create Set, Member Index, Mass Addition, Sort "
          u"List, Panel",
     etapes=[u"Établir la liste des références distinctes.",
             u"Rattacher chaque ligne du débit à sa référence.",
             u"Cumuler les quantités par référence.",
             u"Prendre le plus grand cumul."],
     pieges=[u"Confondre le nombre de lignes et la quantité.",
             u"Regrouper sur un libellé approchant : les références se "
             u"ressemblent, deux d'entre elles ne diffèrent que par leur "
             u"épaisseur."],
     var=[u"Rendre la table complète, une ligne par référence, triée par "
          u"quantité décroissante.",
          u"Ajouter une colonne de prix unitaire et sortir le montant."],
     gamif=u"G-11 Commande à passer",
     bareme=u"1 point si la quantité cumulée est juste.",
     verdict=u"competence"),

dict(id=u"QT-05", titre=u"Le fichier que le fournisseur va lire",
     them=u"QT3 · Export de données",
     ref=u"REF-086, REF-087",
     niv=u"Intermédiaire", duree=25, prereq=u"QT-04",
     competence=u"Produire un fichier d'échange dont la structure est celle "
                u"qu'attend le destinataire, en-tête comprise, et savoir "
                u"combien de lignes il doit contenir avant de l'ouvrir.",
     bloom=u"Appliquer × procédurale",
     contexte=u"La commande part en CSV vers le fournisseur, qui l'importe "
              u"automatiquement. Un fichier mal structuré n'est pas rejeté : "
              u"il est importé de travers.",
     obj=u"Produire un fichier d'échange dont la structure est celle "
         u"qu'attend le destinataire, en-tête comprise, et savoir combien de "
         u"lignes il doit contenir avant de l'ouvrir.",
     enonce=u"Vous exportez la commande regroupée de l'exercice précédent au "
            u"format CSV, avec une ligne d'en-tête nommant les colonnes. "
            u"Donnez le nombre de lignes que le fichier doit contenir.",
     depart=u"Le débit de vingt-quatre lignes, et la commande regroupée qui "
            u"en découle.",
     att=u"9 — huit références, plus la ligne d'en-tête.",
     erreur=u"Exporter les vingt-quatre lignes du débit (25 avec l'en-tête) "
            u"ou oublier l'en-tête (8). Le premier fait commander huit "
            u"références en double ; le second fait lire la première "
            u"référence comme un nom de colonne, et elle disparaît de la "
            u"commande.",
     donnees_note=u"Le compte attendu — 9 — ne ressemble ni au nombre de "
                  u"lignes du débit (24) ni au nombre de références (8) : "
                  u"les trois erreurs possibles donnent trois valeurs "
                  u"distinctes, donc lisibles.",
     limite=u"Le compte des lignes ne dit rien du séparateur ni de "
            u"l'encodage, qui font échouer autant d'imports. La fiche les "
            u"signale ; l'exercice ne les valide pas.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Create Set, List Length, Addition, Concatenate, Panel",
     etapes=[u"Reprendre la commande regroupée par référence.",
             u"Compter les références distinctes.",
             u"Ajouter la ligne d'en-tête.",
             u"Écrire le fichier, et le rouvrir pour vérifier le compte."],
     pieges=[u"Oublier l'en-tête.",
             u"Exporter le débit au lieu de la commande.",
             u"Employer la virgule comme séparateur alors que les quantités "
             u"peuvent être décimales."],
     var=[u"Ajouter une colonne d'unité et vérifier que le compte des lignes "
          u"ne change pas.",
          u"Exporter la même commande en XLSX et comparer ce que chaque "
          u"format garantit."],
     gamif=u"G-11 Commande à passer",
     bareme=u"1 point si le nombre de lignes est juste.",
     verdict=u"competence"),

]


# ---------------------------------------------------------------------------
# Lot FA — aide a la fabrication
# ---------------------------------------------------------------------------

LOT_FA = [

dict(id=u"FA-03", titre=u"Le développé d'un profil plié",
     them=u"FA2 · Déroulé et mise à plat",
     ref=u"REF-116",
     niv=u"Perfectionnement", duree=35, prereq=u"FA-02",
     competence=u"Calculer la longueur développée d'une tôle pliée en tenant "
                u"compte de l'allongement de la matière au droit des plis.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le profil en U part au débit avant pliage : la bande découpée "
              u"doit avoir exactement la longueur qui, une fois pliée, donnera "
              u"les cotes du plan.",
     obj=u"Calculer la longueur développée d'une tôle pliée en tenant compte "
         u"de l'allongement de la matière au droit des plis.",
     enonce=u"Le profil en U mesure 120 mm d'aile, 300 mm d'âme, cotes "
            u"extérieures, dans une tôle de 3 mm. Les deux plis à 90° se font "
            u"sur un rayon intérieur de 5 mm, avec un facteur K de 0,42. "
            u"Donnez la longueur de la bande à débiter, en millimètres.",
     depart=u"Les cotes extérieures du profil, l'épaisseur de la tôle, le "
            u"rayon intérieur de pliage et le facteur K.",
     att=u"527,67 mm — la longueur développée, à 0,1 mm près.",
     erreur=u"Additionner les cotes extérieures : 120 + 300 + 120 = 540 mm. "
            u"La matière s'allonge à l'extérieur du pli et se comprime à "
            u"l'intérieur ; seule la fibre neutre garde sa longueur, et elle "
            u"ne passe pas au milieu de l'épaisseur — c'est ce que dit le "
            u"facteur K. L'écart fait 12,3 mm : invisible sur le plan, fatal "
            u"à l'atelier, et il se répète sur chaque pièce de la série.",
     donnees_note=u"Un facteur K de 0,42 est la valeur courante pour un acier "
                  u"doux plié sur un rayon voisin de l'épaisseur. Les cotes "
                  u"sont extérieures, comme sur un plan de tôlerie — c'est "
                  u"précisément ce qui oblige à retrancher rayon et épaisseur "
                  u"avant de calculer les parties plates.",
     limite=u"Le facteur K dépend de la nuance, du rayon et de l'outil : "
            u"celui de l'exercice est donné. En atelier, il se relève sur une "
            u"pièce d'essai, et c'est le vrai geste métier.",
     mode=u"NumericTolerance", tol=u"0.1", nb=9,
     comp=u"Subtraction, Multiplication, Addition, Pi, Division, Panel",
     etapes=[u"Retrancher rayon et épaisseur des cotes extérieures pour "
             u"obtenir les parties réellement plates.",
             u"Calculer l'allongement d'un pli à 90° : un quart de cercle sur "
             u"le rayon de la fibre neutre.",
             u"La fibre neutre est à r + K·e du centre de courbure.",
             u"Sommer les parties plates et les deux allongements."],
     pieges=[u"Sommer les cotes extérieures.",
             u"Placer la fibre neutre au milieu de l'épaisseur, ce qui "
             u"revient à prendre K = 0,5.",
             u"Oublier que l'âme perd rayon et épaisseur DEUX fois, une par "
             u"pli."],
     var=[u"Refaire le calcul avec un facteur K de 0,5 et chiffrer l'écart "
          u"sur une série de 200 pièces.",
          u"Traiter un profil à trois plis, dont un à 135°."],
     gamif=u"G-19 Pièce d'essai",
     bareme=u"1 point si le développé est juste à 0,1 mm près.",
     verdict=u"competence"),

dict(id=u"FA-04", titre=u"Combien de pièces par fournée",
     them=u"FA1 · Imbrication",
     ref=u"REF-114",
     niv=u"Perfectionnement", duree=30, prereq=u"FA-01",
     competence=u"Estimer le remplissage d'un volume de fabrication en "
                u"raisonnant par encombrement, et non par volume de matière.",
     bloom=u"Analyser × procédurale",
     contexte=u"La machine de fabrication additive facture à la fournée, pas "
              u"à la pièce : le prix unitaire dépend entièrement du nombre de "
              u"pièces qu'on fait tenir dans le volume de construction.",
     obj=u"Estimer le remplissage d'un volume de fabrication en raisonnant "
         u"par encombrement, et non par volume de matière.",
     enonce=u"Le volume de construction mesure 250 × 210 × 210 mm. La pièce "
            u"tient dans un encombrement de 62 × 38 × 95 mm et ne peut pas "
            u"être réorientée. Il faut 4 mm entre deux pièces et 4 mm entre "
            u"une pièce et chaque paroi. Donnez le nombre de pièces par "
            u"fournée.",
     depart=u"Les dimensions du volume de construction, l'encombrement de la "
            u"pièce et l'écart minimal à respecter.",
     att=u"24 — soit 3 pièces en longueur, 4 en largeur et 2 en hauteur.",
     erreur=u"Diviser le volume du plateau par le volume de la pièce : "
            u"11 025 000 ÷ 223 820 donne 49 pièces, soit le double. Le "
            u"rapport des volumes ignore que les pièces ne se déforment pas "
            u"pour combler les creux — c'est la même erreur que le rapport "
            u"des surfaces en FA-01, et elle se paie ici au prix de la "
            u"fournée.",
     donnees_note=u"Les trois divisions tombent chacune sur une valeur "
                  u"franchement non entière — 3,72, 4,90 et 2,08 — de sorte "
                  u"qu'un arrondi au plus proche donnerait 4, 5 et 2, soit "
                  u"40 pièces qui ne rentrent pas. L'écart entre le rapport "
                  u"des volumes (49) et le compte réel (24) est du simple au "
                  u"double : impossible de confondre les deux méthodes.",
     limite=u"Le compte suppose une orientation fixe et une grille "
            u"régulière. Un imbriquement réel, qui autorise la rotation et "
            u"l'entrelacement, fait mieux — mais jamais autant que le rapport "
            u"des volumes.",
     mode=u"SingleValue", tol=u"0", nb=10,
     comp=u"Subtraction, Addition, Division, Round, Multiplication, Panel",
     etapes=[u"Retrancher les deux écarts de paroi de chaque dimension du "
             u"plateau.",
             u"Sur chaque axe, chercher combien de pièces séparées d'un écart "
             u"tiennent dans la longueur utile.",
             u"Arrondir chaque compte à l'entier INFÉRIEUR : une pièce qui "
             u"dépasse ne se produit pas.",
             u"Multiplier les trois comptes."],
     pieges=[u"Diviser les volumes.",
             u"Arrondir au plus proche au lieu de l'inférieur.",
             u"Compter un écart de trop ou de moins : entre n pièces il y a "
             u"n − 1 intervalles, plus les deux écarts de paroi."],
     var=[u"Autoriser la rotation à 90° autour de l'axe vertical et "
          u"recompter.",
          u"Chiffrer le prix unitaire pour une fournée facturée 380 € et le "
          u"comparer à celui qu'aurait donné le rapport des volumes."],
     gamif=u"G-21 Optimisation comparée",
     bareme=u"1 point si le nombre de pièces est juste.",
     verdict=u"competence"),

]
