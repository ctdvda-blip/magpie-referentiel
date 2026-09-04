# -*- coding: utf-8 -*-
"""Couche pedagogique du LOT C, superposee aux fiches d'origine.

Meme montage que `skill_b.py` : `exos_b.py` (qui porte LOT_B et LOT_C) n'est
pas touche.

LE CAS PARTICULIER DU LOT C
---------------------------
Ce sont des PROJETS : quarante a cinquante composants, plusieurs livrables,
parfois un plugin. Leur livrable ne se reduit pas a un nombre, et il ne doit
pas : une resille relaxee, un devis structure par lot, un plan d'imbrication
avec ses DXF ne sont pas des valeurs.

Mais chacun porte un INDICATEUR que le metier regarde de toute facon, et que
les fiches d'origine annoncaient deja — « deux indicateurs affiches », « un
tableau de controle ». C'est cet indicateur qui est corrige automatiquement ;
le reste se juge sur grille, comme pour tout projet.

Ce n'est donc pas un exercice reduit a son indicateur : c'est un projet dont
UN point se verifie sans le formateur, ce qui permet a l'apprenant de savoir
seul s'il s'est trompe avant de rendre.

TOUTES LES VALEURS SONT CALCULEES par `verifier_lot_c.py`.
"""

import math

# ---------------------------------------------------------------------------
# Jeux de donnees
# ---------------------------------------------------------------------------

#: C-01 — des lames horizontales, et le soleil du 21 juin a 15 h
D_C01 = dict(entraxe=400.0, hauteur_solaire=58.0, lames=180)

#: C-02 — une resille triangulee reguliere
D_C02 = dict(largeur=24000.0, profondeur=16000.0, maille=2000.0)

#: C-03 — des gradins, et la ligne de visee
D_C03 = dict(rangs=18, profondeur=850.0, degagement=90.0, foyer=4200.0)

#: C-04 — le devis, lot par lot : (designation, quantite, unite, prix unitaire)
D_C04_LOTS = [
    (u"Gros œuvre", [(u"Béton", 18.4, u"m³", 185.0),
                     (u"Acier", 1.35, u"t", 1420.0),
                     (u"Coffrage", 96.0, u"m²", 42.0)]),
    (u"Menuiserie", [(u"Fenêtres", 12.0, u"u", 680.0),
                     (u"Portes", 7.0, u"u", 410.0),
                     (u"Bardage", 145.0, u"m²", 88.0)]),
    (u"Second œuvre", [(u"Isolation", 210.0, u"m²", 34.0),
                       (u"Cloisons", 168.0, u"m²", 52.0),
                       (u"Peinture", 320.0, u"m²", 19.0)]),
]

#: C-05 — une bibliotheque a montants regulierement espaces
D_C05 = dict(largeur=3200.0, hauteur=2400.0, profondeur=320.0,
             epaisseur=19.0, entraxe_max=800.0, tablettes_par_travee=5)

#: C-06 — la directrice de l'assise, et la lamelle
D_C06 = dict(corde=420.0, fleche=65.0, epaisseur=8.0, rapport_mini=25.0,
             lamelles=22)

#: C-07 — le configurateur, et son bareme
D_C07_PIEDS = {u"tourné": 96.0, u"fuseau": 128.0, u"compas": 154.0,
               u"caisson": 72.0}
D_C07_MATIERE = {u"chêne": 1.0, u"noyer": 1.42}
D_C07 = dict(base=310.0, par_tiroir=88.0,
             choix=(u"compas", 3, u"noyer"))

#: C-08 — la bague, et l'or 750
D_C08 = dict(taille=54.0, largeur=2.0, epaisseur=1.30, densite=15.6,
             chaton=42.0, limite=3.2)

#: C-09 — le pavage de pierres
D_C09 = dict(surface=260.0, diametre=1.85, metal=0.3)

#: C-10 — le motif Voronoi
D_C10 = dict(surface=168.0, aire_cellule=1.5, filet=0.25)

#: C-11 — la tole a cinq plis, cotes EXTERIEURES
D_C11 = dict(epaisseur=2.0, rayon=3.0, k=0.44,
             cotes=[70.0, 120.0, 95.0, 120.0, 70.0, 45.0])

#: C-12 — quarante-six pieces a imbriquer
D_C12_PLAQUE = (3000.0, 1500.0)
D_C12 = dict(espacement=8.0, bord=15.0)
D_C12_PIECES = [
    (800, 520), (820, 445), (885, 720), (460, 270), (885, 470), (445, 220),
    (625, 395), (750, 570), (320, 200), (915, 645), (520, 310), (685, 490),
    (250, 165), (855, 615), (405, 260), (730, 425), (580, 355), (790, 540),
    (290, 185), (875, 685), (490, 300), (665, 470), (365, 230), (830, 595),
    (540, 335), (705, 510), (270, 175), (895, 665), (425, 280), (645, 445),
    (345, 210), (810, 560), (510, 320), (730, 480), (310, 200), (905, 635),
    (470, 290), (675, 460), (385, 240), (840, 580), (550, 345), (720, 500),
    (260, 170), (925, 655), (435, 275), (635, 435),
]


# ---------------------------------------------------------------------------
# La couche
# ---------------------------------------------------------------------------

SKILL_C = {

"C-01": dict(
  competence=u"Dimensionner un dispositif d'ombrage à partir de la course "
             u"solaire, en distinguant ce qui se divise de ce qui se "
             u"multiplie.",
  bloom=u"Analyser × procédurale",
  contexte=u"Le brise-soleil doit occulter à l'heure la plus chaude sans "
           u"assombrir le reste de l'année. Sa profondeur est ce qui coûte "
           u"et ce qui se voit.",
  att=u"249,95 mm — la profondeur minimale de lame, à 0,01 près.",
  erreur=u"Multiplier l'entraxe par la tangente au lieu de le diviser : "
         u"640 mm, soit deux fois et demie trop. Une lame de 640 mm sur un "
         u"entraxe de 400 se recouvre elle-même — la façade devient un mur, "
         u"et le calcul reste plausible tant qu'on ne le dessine pas.",
  donnees_note=u"Un soleil à 58° correspond au 21 juin en milieu "
               u"d'après-midi sous nos latitudes. Les deux réponses, 250 et "
               u"640 mm, sont dans un rapport de 2,56 — soit exactement le "
               u"carré de la tangente, ce qui est la signature de l'erreur.",
  limite=u"Le calcul assure l'occultation à CET instant. Une lame "
         u"dimensionnée pour le 21 juin à 15 h laisse passer le soleil "
         u"rasant de septembre — c'est la limite de tout brise-soleil fixe, "
         u"et l'exercice ne la traite pas.",
  mode=u"NumericTolerance", tol=u"0.01"),

"C-02": dict(
  competence=u"Chiffrer le linéaire d'une structure triangulée en n'oubliant "
             u"aucune des trois familles de barres.",
  bloom=u"Appliquer × procédurale",
  contexte=u"La résille se chiffre au mètre de barre avant d'être relaxée. "
           u"C'est ce chiffre qui décide si le projet passe le budget.",
  att=u"695,53 m de barres, à 0,01 près.",
  erreur=u"Oublier les diagonales : 424 m. Or ce sont elles qui TRIANGULENT "
         u"— sans elles la résille n'est pas une structure, c'est une "
         u"grille articulée. Elles pèsent 271 m, soit 39 % du total, et leur "
         u"oubli fait passer le projet pour deux fois moins cher qu'il "
         u"n'est.",
  donnees_note=u"Une maille de 2 000 mm sur 24 × 16 m donne 12 × 8 panneaux. "
               u"La diagonale d'une maille carrée vaut √2 fois son côté : "
               u"les diagonales pèsent donc plus que les horizontales, ce qui "
               u"est contre-intuitif et rend leur oubli d'autant plus "
               u"coûteux.",
  limite=u"Le linéaire est celui de la résille PLANE. La relaxation la "
         u"déforme, et les barres s'allongent — de quelques pour cent selon "
         u"la flèche obtenue. Le chiffrage se refait après relaxation.",
  mode=u"NumericTolerance", tol=u"0.01"),

"C-03": dict(
  competence=u"Construire une progression dont chaque terme dépend du "
             u"précédent ET de sa position, et en tirer une cote de projet.",
  bloom=u"Analyser × procédurale",
  contexte=u"Le dégagement visuel est une règle de sécurité et de confort. "
           u"Il se vérifie rang par rang, et la hauteur du dernier décide de "
           u"tout le volume construit.",
  att=u"3 105,01 mm — la hauteur du dernier rang, à 0,01 près.",
  erreur=u"Ajouter 90 mm à chaque rang : 1 530 mm au dernier, soit la moitié. "
         u"Le dégagement ne s'ajoute pas — il se PROPAGE : chaque rang doit "
         u"dépasser la ligne de visée du précédent, et cette ligne s'élève "
         u"d'autant plus qu'on s'éloigne du foyer. La salle construite sur "
         u"le calcul faux ne voit rien depuis le fond.",
  donnees_note=u"Dix-huit rangs de 850 mm, foyer à 4 200 mm : la hauteur "
               u"croît de 108 mm au deuxième rang à plus de 200 au dernier. "
               u"C'est cette accélération que la somme constante ignore, et "
               u"elle donne un facteur deux sur la hauteur totale.",
  limite=u"Le calcul suppose un foyer ponctuel et des spectateurs alignés. "
         u"Une salle réelle a une scène étendue et des rangs décalés, ce qui "
         u"adoucit la progression — mais jamais au point de la rendre "
         u"linéaire.",
  mode=u"NumericTolerance", tol=u"0.01"),

"C-04": dict(
  competence=u"Structurer un devis par lot avec sous-totaux, et le rendre "
             u"exact au centime.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le devis part au maître d'ouvrage. Un sous-total faux ne se "
           u"voit pas ; un total faux se voit toujours, et trop tard.",
  att=u"55 099,00 € de total général.",
  erreur=u"Additionner les quantités au lieu des montants, ou sommer les "
         u"sous-totaux d'un lot en oubliant une ligne. Un devis à trois lots "
         u"et neuf lignes se vérifie de deux façons — par les lots et par "
         u"les lignes — et les deux doivent tomber sur le même chiffre.",
  donnees_note=u"Neuf lignes en trois lots, avec des unités différentes — m³, "
               u"tonne, unité, m² — pour que la somme des quantités n'ait "
               u"aucun sens et que l'erreur se voie. Les trois sous-totaux "
               u"sont de tailles très différentes : 9 353, 23 790, 21 956.",
  limite=u"Le total est un montant de TRAVAUX, hors taxes et hors aléas. "
         u"Un devis remis au client y ajoute la TVA, les frais généraux et "
         u"une provision d'imprévus — de 5 à 10 % selon la maturité du "
         u"projet. Le chiffre juste n'est pas encore le prix.",
  mode=u"NumericTolerance", tol=u"0.01"),

"C-05": dict(
  competence=u"Déduire le nombre d'éléments d'un meuble d'une contrainte "
             u"d'entraxe maximal, et en tirer la nomenclature.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Une tablette de plus de 800 mm de portée flèche sous la charge. "
           u"C'est cette règle qui fixe le nombre de montants, pas "
           u"l'esthétique.",
  att=u"28 panneaux à débiter.",
  erreur=u"Compter quatre montants pour quatre travées. Il en faut CINQ — un "
         u"de plus que les intervalles, comme toujours. Le meuble monté sur "
         u"le calcul faux n'a pas de joue à une extrémité.",
  donnees_note=u"3 200 mm de largeur pour 800 mm d'entraxe maximal donnent "
               u"exactement quatre travées : le cas limite, où l'arrondi au "
               u"supérieur ne change rien et où seul le « n + 1 » compte. "
               u"Cinq montants, vingt tablettes, deux traverses et un fond.",
  limite=u"L'exercice compte les panneaux. Leur DÉBIT — comment ils se "
         u"placent dans les plaques — est l'objet de C-12, et n'a pas la "
         u"même réponse.",
  mode=u"SingleValue", tol=u"0"),

"C-06": dict(
  competence=u"Vérifier qu'une forme voulue respecte une contrainte de "
             u"matière, en comparant un rayon obtenu à un rayon admissible.",
  bloom=u"Évaluer × procédurale",
  contexte=u"Une lamelle de contreplaqué cintrée trop serré casse au "
           u"pressage. Le rapport rayon sur épaisseur est ce que l'atelier "
           u"regarde.",
  att=u"371,73 mm — le rayon de la directrice, à 0,01 près, à comparer aux "
      u"200 mm admissibles.",
  erreur=u"Prendre la flèche pour le rayon, ou la demi-corde. Le rayon d'un "
         u"arc se retrouve de sa corde ET de sa flèche : (c²/4 + f²) ÷ 2f. "
         u"Ni 65 ni 210 ne sont le rayon, et les deux sont sous la limite "
         u"admissible — l'assise serait déclarée infaisable alors qu'elle "
         u"passe avec 86 % de marge.",
  donnees_note=u"Corde de 420 et flèche de 65 donnent 371,7 mm de rayon, "
               u"contre 200 admissibles pour une lamelle de 8 mm au rapport "
               u"25. La marge est confortable, à dessein : l'exercice porte "
               u"sur la façon de CONCLURE, pas sur un cas limite.",
  limite=u"Le rayon vérifie la faisabilité du CINTRAGE. Il ne dit rien du "
         u"retour élastique : une lamelle relâchée s'ouvre de quelques "
         u"degrés, et le gabarit se creuse en conséquence. C'est un réglage "
         u"d'atelier, pas un calcul.",
  mode=u"NumericTolerance", tol=u"0.01"),

"C-07": dict(
  competence=u"Établir un prix par composition, en appliquant chaque "
             u"coefficient sur son assiette.",
  bloom=u"Appliquer × procédurale",
  contexte=u"Le configurateur affiche un prix à chaque changement. Un "
           u"coefficient mal appliqué se voit sur des milliers de "
           u"configurations, jamais sur celle qu'on a testée.",
  att=u"1 033,76 € pour la combinaison compas, trois tiroirs, noyer.",
  erreur=u"N'appliquer la majoration de matière qu'au prix de base : "
         u"858,20 €. Le noyer coûte plus cher pour TOUT le meuble — pieds et "
         u"tiroirs compris. L'écart de 175 € est un sixième du prix, et il "
         u"est toujours dans le même sens : à la perte.",
  donnees_note=u"Quatre types de pieds, un à trois tiroirs, deux matières : "
               u"vingt-quatre combinaisons. Celle qui est demandée cumule le "
               u"pied le plus cher, le maximum de tiroirs et la matière "
               u"majorée — c'est là que l'erreur de coefficient coûte le "
               u"plus, donc là qu'il faut la chercher.",
  limite=u"Le barème est linéaire. Un vrai configurateur applique des "
         u"remises par quantité et des suppléments non linéaires, mais la "
         u"question de l'assiette du coefficient reste la même.",
  mode=u"NumericTolerance", tol=u"0.01"),

"C-08": dict(
  competence=u"Chiffrer la masse d'une pièce à partir de sa fibre moyenne, "
           u"et la confronter à une limite de projet.",
  bloom=u"Évaluer × procédurale",
  contexte=u"L'or se pèse avant d'être coulé. Un gramme de trop sur un "
           u"solitaire, c'est cinquante euros et un anneau qui paraît lourd "
           u"au doigt.",
  att=u"3,011 g d'or 750, à 0,05 près — sous la limite de 3,2 g.",
  erreur=u"Calculer le volume sur la circonférence NOMINALE, celle du doigt : "
         u"2,845 g. L'anneau a une épaisseur ; sa fibre moyenne court à "
         u"mi-épaisseur, donc sur une circonférence plus grande de π fois "
         u"l'épaisseur. L'écart de 0,17 g dépasse quatre fois la tolérance, "
         u"et il sous-estime toujours — c'est de l'or qu'on croit économiser "
         u"et qu'il faudra ajouter.",
  donnees_note=u"Taille 54, section 2,0 × 1,3 mm, or 750 à 15,6 g/cm³ : la "
               u"masse tombe à 3,011 g pour une limite de 3,2. La marge est "
               u"de 6 % — assez serrée pour que l'erreur de fibre moyenne "
               u"compte, assez large pour que la pièce reste faisable.",
  limite=u"3,011 g est la masse de MATIÈRE finie. La fonte à cire perdue "
         u"consomme davantage — tiges d'alimentation, masselottes, pertes "
         u"de récupération — couramment 20 à 30 % de plus, que le devis "
         u"joaillier compte séparément.",
  mode=u"NumericTolerance", tol=u"0.05"),

"C-09": dict(
  competence=u"Estimer combien d'éléments circulaires tiennent sur une "
             u"surface en tenant compte de l'écart imposé entre eux.",
  bloom=u"Analyser × procédurale",
  contexte=u"Le métal entre deux pierres tient le serti. Sous 0,3 mm il "
           u"cède, et la pierre part.",
  att=u"64 pierres.",
  erreur=u"Diviser la surface par l'aire d'une pierre : 96. Deux erreurs se "
         u"cumulent — l'écart de métal est ignoré, et des disques ne pavent "
         u"pas un plan. La maille hexagonale la plus dense laisse 9 % de "
         u"vide même sans écart ; avec 0,3 mm de métal, chaque pierre occupe "
         u"4,00 mm² au lieu de 2,69.",
  donnees_note=u"Une surface de 260 mm², des pierres de 1,85 mm et 0,3 mm de "
               u"métal : le pas monte à 2,15 mm. Les deux réponses, 64 et 96, "
               u"sont dans un rapport de 1,5 — assez pour que la commande de "
               u"pierres soit franchement fausse.",
  limite=u"64 est le compte d'une maille régulière. La consigne demande une "
         u"répartition « quasi aléatoire », qui en fait toujours tenir un peu "
         u"moins : le chiffre est un plafond, et c'est ce qu'il faut savoir "
         u"en le donnant au client.",
  mode=u"SingleValue", tol=u"0"),

"C-10": dict(
  competence=u"Dimensionner une partition de surface en tenant compte de ce "
             u"que les séparations consomment.",
  bloom=u"Analyser × procédurale",
  contexte=u"Le filet entre cellules doit rester gravable. Trop fin, il "
           u"disparaît au polissage.",
  att=u"77 cellules.",
  erreur=u"Diviser la surface par l'aire visée d'une cellule : 112. Le filet "
         u"de 0,25 mm court AUTOUR de chaque cellule : le pas réel n'est pas "
         u"le côté de la cellule mais le côté plus le filet, ce qui fait "
         u"perdre un tiers des cellules. Le motif calculé sans lui arrive "
         u"trop dense, et le filet disparaît.",
  donnees_note=u"Une cellule de 1,5 mm² fait 1,22 mm de côté ; avec le filet "
               u"le pas monte à 1,47 mm, soit une aire de 2,17 mm² par "
               u"cellule — 45 % de plus. C'est la marge que le filet coûte, "
               u"et elle est loin d'être négligeable à cette échelle.",
  limite=u"77 cellules est un compte de SURFACE. Un Voronoï réel n'a pas "
         u"de cellules égales : les cellules de bord sont plus petites, et "
         u"le nombre effectivement placé varie de quelques unités selon la "
         u"répartition des germes.",
  mode=u"SingleValue", tol=u"0"),

"C-11": dict(
  competence=u"Calculer le développé d'une tôle à plis multiples, en "
             u"comptant le bon nombre de plis par segment.",
  bloom=u"Appliquer × procédurale",
  contexte=u"La bande part au débit avant pliage. Cinq plis, c'est cinq "
           u"occasions de se tromper d'un rayon.",
  att=u"500,47 mm de développé, à 0,1 près.",
  erreur=u"Additionner les cotes extérieures : 520 mm, soit près de 20 mm de "
         u"trop. Mais l'erreur la plus coûteuse est ailleurs : retirer "
         u"rayon et épaisseur UNE fois par segment. Les quatre segments "
         u"intérieurs portent DEUX plis chacun, les deux segments d'extrémité "
         u"un seul — c'est ce décompte qui fait la différence entre une bande "
         u"juste et une bande courte de 20 mm.",
  donnees_note=u"Six segments et cinq plis : deux extrémités à un pli, quatre "
               u"segments intérieurs à deux plis. Le facteur K de 0,44 est "
               u"celui d'un acier doux plié sur un rayon supérieur à "
               u"l'épaisseur. Le développé, 500,47, est inférieur à la somme "
               u"des cotes — contre-intuitif, et c'est bien le cas général.",
  limite=u"Cinq plis à 90° dans le même sens font une pièce qui se referme "
         u"presque. La faisabilité du pliage — l'ordre des plis, la place de "
         u"l'outil — n'est pas jugée ici, et c'est elle qui décide en "
         u"atelier.",
  mode=u"NumericTolerance", tol=u"0.1"),

"C-12": dict(
  competence=u"Chiffrer un débit en tenant compte des espacements et des "
             u"bords perdus, et en tirer un taux de chute défendable.",
  bloom=u"Analyser × procédurale",
  contexte=u"La plaque se commande à l'unité et le taux de chute figure au "
           u"devis. Il engage l'entreprise.",
  att=u"27,36 % de chute, à 0,01 près.",
  erreur=u"Calculer sur les surfaces nues, sans les 8 mm d'espacement ni les "
         u"15 mm de bord perdu : on conclut alors à TROIS plaques et 3 % de "
         u"chute. Chaque pièce occupe en réalité 8 mm de plus dans chaque "
         u"dimension, et la plaque perd 30 mm sur chaque côté — il en faut "
         u"quatre. Une plaque manquante sur le bon de commande arrête la "
         u"découpe en fin de série.",
  donnees_note=u"46 pièces de 255 à 925 mm dans des plaques de 3 × 1,5 m. Le "
               u"jeu est calibré pour que l'espacement CHANGE le compte : "
               u"13,07 m² de pièces nues tiennent en trois plaques, mais "
               u"13,45 m² avec les espacements ne tiennent plus dans les "
               u"13,10 m² utiles de trois plaques. C'est le cas limite, et "
               u"c'est celui où l'oubli se paie.",
  limite=u"Le taux est un MINORANT, comme en B-13 : il ne compte que les "
         u"surfaces. Le plan d'imbrication réel ajoute la chute de placement, "
         u"et c'est lui qui figure au bon de commande.",
  mode=u"NumericTolerance", tol=u"0.01"),

}


def fusionner(exo):
    """Rend la fiche d'origine enrichie de la couche pedagogique."""
    r = dict(exo)
    couche = SKILL_C.get(exo["id"])
    if not couche:
        return r
    for cle, valeur in couche.items():
        r[cle] = valeur
    r.setdefault(u"verdict", u"competence")
    r[u"competence"] = couche.get(u"competence", exo.get("obj", u""))
    # Les fiches d'origine du lot C disent « Experimente », un niveau qui
    # n'existe nulle part ailleurs dans le referentiel : les filtres de
    # l'application en auraient fait une categorie a douze exercices, isolee
    # des quatre autres. Ces projets relevent du perfectionnement.
    if r.get(u"niv") == u"Expérimenté":
        r[u"niv"] = u"Perfectionnement"
    return r
