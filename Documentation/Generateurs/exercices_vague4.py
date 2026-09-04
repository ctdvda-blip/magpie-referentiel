# -*- coding: utf-8 -*-
"""Vague 4 : densifier les quinze categories restees au plancher.

APRES la vague 3, chaque notion du referentiel avait au moins un exercice.
Les lots B, C et G ont ensuite nourri les categories DEJA denses — listes,
transformations, surfaces — et l'ecart s'est creuse : « Transformations et
reseaux » a fini a huit exercices par notion quand quinze categories restaient
a un seul. Le socle Rhino, l'ecosysteme de plugins et le domaine IA etaient au
minimum.

Ces vingt-quatre exercices portent sur des notions DEJA couvertes, mais par un
angle different : la ou le premier fait construire, celui-ci fait choisir,
compter ou verifier. Un second exercice qui redemanderait la meme chose
n'apporterait rien.

Repartition, proportionnelle au nombre de notions :

    ecosysteme de plugins       11 notions -> 4    PL-13 a PL-16
    impression 3D                9         -> 3    RH-24 a RH-26
    modelisation Rhino           7         -> 3    RH-27 a RH-29
    interface et navigation      6         -> 2    RH-30, RH-31
    composants scriptes assistes 5         -> 2    IA-26, IA-27
    huit categories de 3 ou 4    32        -> 12   le reste

TOUTES LES VALEURS SONT CALCULEES par `verifier_vague4.py`.
"""


# ---------------------------------------------------------------------------
# Le generateur des jeux de donnees
# ---------------------------------------------------------------------------

def suite(n, graine, bas, haut, pas=1):
    """Suite deterministe, lue sur les bits de POIDS FORT.

    Le reste modulo l'etendue rendait la parite previsible : sur un
    generateur congruentiel de module 2^31, le bit de poids faible alterne.
    C'est le defaut trouve sur le lot G, et il ne se reproduit pas ici.
    """
    out, x = [], graine
    span = int((haut - bas) / pas) + 1
    for _ in range(n):
        x = (1103515245 * x + 12345) % 2147483648
        out.append(bas + ((x >> 13) % span) * pas)
    return out


# ---------------------------------------------------------------------------
# Jeux de donnees
# ---------------------------------------------------------------------------

#: PL-13 — (nom, present sur le Package Manager, present sur Food4Rhino)
D_PL13 = [(u"Metahopper", True, True), (u"Human", False, True),
          (u"Elefront", True, True), (u"Weaverbird", False, True),
          (u"Pufferfish", True, True), (u"LunchBox", True, True),
          (u"Kangaroo", True, False), (u"Bifocals", False, True),
          (u"SnappingGecko", False, True), (u"Palette", False, True),
          (u"Moonlight", True, True), (u"pOd", False, True),
          (u"AutoGraph", True, True), (u"Dendro", True, True)]

#: PL-14 — (nom, temps de chargement en ms, deja exige par un autre plugin)
D_PL14 = [(u"Bifocals", 210, False), (u"SnappingGecko", 145, False),
          (u"Palette", 95, False), (u"Moonlight", 130, False),
          (u"pOd", 380, False), (u"AutoGraph", 260, False),
          (u"Metahopper", 175, True)]

#: PL-15 — ce que chaque plugin apporte, et ce que la definition reclame
D_PL15_FOURNI = [
    (u"Metahopper", [u"Get Objects", u"Set Nickname", u"Component Info",
                     u"Define Attributes"]),
    (u"Human", [u"Text Tag 3D", u"Get Objects", u"Custom Preview",
                u"Set Nickname"]),
    (u"Elefront", [u"Bake Objects", u"Reference by Layer",
                   u"Define Attributes", u"Text Tag 3D"]),
    (u"Weaverbird", [u"Catmull-Clark", u"Mesh Thicken", u"Picture Frame"]),
    (u"Pufferfish", [u"Tween Curves", u"Mesh Thicken", u"Blend Box",
                     u"Catmull-Clark"]),
    (u"LunchBox", [u"Diamond Panels", u"Hexagon Cells", u"Random Panels",
                   u"Tween Curves"]),
]
D_PL15_BESOIN = [u"Get Objects", u"Set Nickname", u"Define Attributes",
                 u"Bake Objects", u"Reference by Layer", u"Text Tag 3D",
                 u"Catmull-Clark", u"Mesh Thicken", u"Blend Box",
                 u"Diamond Panels", u"Hexagon Cells", u"Tween Curves"]

#: PL-16 — (nom, version de Rhino minimale, version maximale supportee)
D_PL16 = [(u"Metahopper", 6, 8), (u"Human", 5, 7), (u"Elefront", 6, 8),
          (u"Weaverbird", 5, 8), (u"Pufferfish", 6, 8), (u"LunchBox", 6, 8),
          (u"Kangaroo", 6, 8), (u"Bifocals", 5, 6), (u"SnappingGecko", 6, 7),
          (u"Palette", 5, 8), (u"Moonlight", 7, 8), (u"pOd", 6, 7),
          (u"AutoGraph", 7, 8), (u"Dendro", 6, 8)]

#: RH-24 — epaisseurs de paroi relevees, en centiemes de millimetre
D_RH24 = suite(18, 60221, 40, 340, 10)
D_RH24_ECHELLE, D_RH24_MINI = 0.62, 1.20

#: RH-25 — (aretes nues, aretes non-manifold) par polysurface
D_RH25 = [(0, 0), (4, 0), (0, 2), (0, 0), (12, 0), (0, 0), (2, 1), (0, 0),
          (0, 3), (6, 0), (0, 0), (0, 0)]

#: RH-26 — le maillage a exporter
D_RH26_TRIANGLES = 148520

#: RH-27 — socle, cylindre, et la profondeur dont le second entre dans le premier
D_RH27 = dict(longueur=240.0, largeur=160.0, hauteur=40.0,
              rayon=45.0, hauteur_cyl=120.0, enfoncement=15.0)

#: RH-28 — le contour a extruder, et la hauteur
D_RH28 = [(0.0, 0.0), (1800.0, 0.0), (1800.0, 900.0), (1100.0, 1400.0),
          (0.0, 1400.0)]
D_RH28_HAUTEUR = 2600.0

#: RH-29 — la platine et son reseau de percements
D_RH29 = dict(longueur=900.0, largeur=600.0, epaisseur=12.0,
              nx=6, ny=4, diametre=22.0)

#: RH-30 — (type, calque, verrouille)
D_RH30 = [(u"Courbe", u"10-Porteurs", False), (u"Surface", u"10-Porteurs", False),
          (u"Courbe", u"11-Cloisons", True), (u"Bloc", u"10-Porteurs", False),
          (u"Courbe", u"10-Porteurs", True), (u"Surface", u"11-Cloisons", False),
          (u"Courbe", u"20-Menuiseries", False), (u"Courbe", u"10-Porteurs", False),
          (u"Maillage", u"10-Porteurs", False), (u"Courbe", u"11-Cloisons", False),
          (u"Surface", u"20-Menuiseries", True), (u"Courbe", u"10-Porteurs", False),
          (u"Bloc", u"11-Cloisons", False), (u"Courbe", u"10-Porteurs", True),
          (u"Courbe", u"20-Menuiseries", False), (u"Surface", u"10-Porteurs", False)]

#: RH-31 — (groupe, calque visible, objet masque)
D_RH31 = [(u"G1", True, False), (u"G1", True, True), (u"G2", False, False),
          (u"G1", True, False), (u"G3", True, False), (u"G2", False, True),
          (u"G3", True, True), (u"G1", True, False), (u"G2", True, False),
          (u"G3", False, False), (u"G1", True, False), (u"G2", True, True),
          (u"G3", True, False), (u"G1", False, False), (u"G2", True, False),
          (u"G3", True, False), (u"G1", True, True), (u"G2", True, False)]

#: RH-32 — la couleur de chaque objet
D_RH32 = [u"ParCalque", u"Rouge", u"ParCalque", u"ParCalque", u"Bleu",
          u"ParCalque", u"ParCalque", u"Vert", u"ParCalque", u"Rouge",
          u"ParCalque", u"ParCalque", u"Bleu", u"ParCalque", u"ParCalque",
          u"Jaune", u"ParCalque", u"ParCalque", u"ParCalque", u"Rouge"]

#: GP-13 — la plaque congee, percee, puis epaissie
D_GP13 = dict(longueur=420.0, largeur=260.0, conge=35.0, epaisseur=18.0,
              percage=26.0, percements=7)

#: WB-10 — ce que chaque format transporte
D_WB10 = [
    (u"géométrie NURBS", [u"3DM", u"STEP", u"IGES"]),
    (u"unités", [u"3DM", u"STEP"]),
    (u"calques", [u"3DM", u"STEP", u"DWG"]),
    (u"couleurs objet", [u"3DM", u"DWG"]),
    (u"matériaux", [u"3DM"]),
    (u"blocs", [u"3DM", u"DWG"]),
    (u"historique", [u"3DM"]),
    (u"maillages", [u"3DM", u"OBJ", u"STL", u"DWG"]),
]
D_WB10_FORMAT = u"STEP"

#: WB-11 — temps de recalcul local, en millisecondes, et le facteur serveur
D_WB11 = suite(24, 33113, 20, 900)
D_WB11_FACTEUR = 2.4

#: IA-26 — le jeu sur lequel les deux versions doivent s'accorder
D_IA26 = suite(14, 77003, 15, 480)

#: IA-27 — les longueurs sur lesquelles le script se trompe
D_IA27 = suite(30, 51878, 200, 3200)
D_IA27_SEUIL = 1500

#: IA-28 — (longueur, epaisseur) de chaque piece
D_IA28 = list(zip(suite(20, 90031, 200, 1800, 10),
                  suite(20, 41103, 10, 60, 2)))
D_IA28_SEUILS = (900, 34)

#: IA-29 — (composant, GUID conserve, definitions qui l'emploient)
D_IA29 = [(u"C01", True, 4), (u"C02", False, 7), (u"C03", True, 2),
          (u"C04", False, 3), (u"C05", True, 9), (u"C06", False, 5),
          (u"C07", True, 6), (u"C08", False, 1)]

#: IA-30 — le coût d'un appel dans une definition qui recalcule
D_IA30 = dict(appels_par_recalcul=3, recalculs=240, latence=1.8, prix=0.004)

#: IA-31 — le journal des operations de l'agent
D_IA31 = [u"lire", u"lire", u"ajouter", u"lire", u"cabler", u"lire",
          u"lire", u"supprimer", u"lire", u"ajouter", u"deplacer",
          u"lire", u"cabler", u"lire", u"renommer", u"lire", u"lire",
          u"ajouter", u"lire", u"supprimer", u"lire", u"cabler"]
D_IA31_ECRITURE = [u"ajouter", u"supprimer", u"cabler", u"deplacer",
                   u"renommer"]

#: IA-32 — le jeu sur lequel quatre lectures d'une meme demande divergent
D_IA32 = suite(16, 22091, 100, 999)
D_IA32[5] = 500
D_IA32_SEUIL = 500

#: IA-33 — la verriere decrite en toutes lettres
D_IA33 = dict(largeur=3200.0, hauteur=2450.0, travees=6, montant=60.0,
              imposte=380.0)


# ---------------------------------------------------------------------------
# Les exercices
# ---------------------------------------------------------------------------

VAGUE4 = [

dict(id=u"PL-13", titre=u"Où trouver chaque plugin",
     them=u"PL2 · Installation de plugins",
     ref=u"REF-029, REF-030",
     niv=u"Intermédiaire", duree=12, prereq=u"PL-02",
     verdict=u"competence",
     competence=u"Distinguer les deux canaux de distribution d'un plugin, et "
                u"savoir lesquels imposent une installation manuelle.",
     bloom=u"Analyser × factuelle",
     contexte=u"Préparer un poste de formation, c'est savoir ce qui "
              u"s'installe en une commande et ce qui demande un "
              u"téléchargement, un déblocage de fichier et un redémarrage.",
     obj=u"Distinguer les deux canaux de distribution d'un plugin, et savoir "
         u"lesquels imposent une installation manuelle.",
     enonce=u"Le tableau vous donne, pour quatorze plugins, leur présence sur "
            u"le gestionnaire de paquets et sur Food4Rhino. Donnez le nombre "
            u"de plugins qui ne sont disponibles QUE sur Food4Rhino.",
     depart=u"Le tableau des quatorze plugins et de leurs deux canaux.",
     att=u"6 plugins ne sont disponibles que sur Food4Rhino.",
     erreur=u"Compter les plugins PRÉSENTS sur Food4Rhino — treize sur "
            u"quatorze. La question porte sur l'exclusivité : ce sont les six "
            u"absents du gestionnaire qui imposeront un téléchargement, un "
            u"déblocage du fichier et un redémarrage sur chaque poste.",
     donnees_note=u"Treize plugins sur quatorze sont sur Food4Rhino et huit "
                  u"sur le gestionnaire : les deux comptes sont proches, et "
                  u"seul le croisement donne six. Un seul plugin — Kangaroo — "
                  u"n'est que sur le gestionnaire, ce qui empêche de "
                  u"raisonner par symétrie.",
     limite=u"Le tableau décrit une situation DATÉE. Les canaux changent : un "
            u"plugin publié sur le gestionnaire six mois plus tard fait "
            u"tomber le compte, et c'est pourquoi une liste d'installation se "
            u"revérifie à chaque session de formation.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Data, Gate Not, Gate And, Cull Pattern, List Length, Panel",
     etapes=[u"Isoler la colonne « présent sur le gestionnaire ».",
             u"En prendre la négation.",
             u"La croiser par un ET avec la colonne Food4Rhino.",
             u"Compter les vrais."],
     pieges=[u"Compter la colonne Food4Rhino seule.",
             u"Oublier la négation et compter les plugins présents partout."],
     var=[u"Compter ceux qui ne sont sur aucun des deux canaux.",
          u"Donner la liste des noms plutôt que le compte."],
     gamif=u"G-06 Le déblocage progressif",
     bareme=u"1 point si le compte est exact."),

dict(id=u"PL-14", titre=u"Ce que l'ergonomie coûte au démarrage",
     them=u"PL3 · Plugins d'ergonomie",
     ref=u"REF-031, REF-032, REF-033, REF-034, REF-035, REF-036, REF-037",
     niv=u"Intermédiaire", duree=14, prereq=u"PL-06",
     verdict=u"competence",
     competence=u"Chiffrer le coût d'une panoplie d'ergonomie sans compter "
                u"deux fois ce qui est déjà installé.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Chaque plugin allonge le démarrage de Rhino. Sur un poste de "
              u"formation ouvert et fermé dix fois par jour, la panoplie "
              u"d'ergonomie se paie en secondes d'attente.",
     obj=u"Chiffrer le coût d'une panoplie d'ergonomie sans compter deux fois "
         u"ce qui est déjà installé.",
     enonce=u"Le relevé donne le temps de chargement de sept plugins, et "
            u"signale ceux qu'un autre plugin déjà installé exige de toute "
            u"façon. Donnez le temps AJOUTÉ par la panoplie d'ergonomie, en "
            u"millisecondes.",
     depart=u"Le relevé des sept temps de chargement, et la colonne des "
            u"dépendances déjà satisfaites.",
     att=u"1 220 ms ajoutés au démarrage.",
     erreur=u"Tout additionner, Metahopper compris : 1 395 ms. Metahopper est "
            u"déjà exigé par un plugin fonctionnel installé sur le poste — "
            u"son chargement n'est pas imputable à l'ergonomie, et le compter "
            u"revient à facturer deux fois la même seconde.",
     donnees_note=u"Sept plugins de 95 à 380 ms. L'écart entre les deux "
                  u"réponses est de 175 ms, soit 14 % : assez pour fausser "
                  u"une décision d'équipement, trop peu pour sauter aux yeux.",
     limite=u"Les temps sont des MESURES sur un poste. Ils dépendent du "
            u"disque, de la version de Rhino et de ce qui est déjà chargé — "
            u"le classement des plugins entre eux est stable, les valeurs "
            u"absolues non.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Data, Gate Not, Cull Pattern, Mass Addition, Panel",
     etapes=[u"Isoler la colonne des dépendances déjà satisfaites.",
             u"En prendre la négation.",
             u"Écarter les temps correspondants.",
             u"Sommer ce qui reste."],
     pieges=[u"Sommer les sept temps sans filtrer.",
             u"Écarter les mauvais, en oubliant la négation."],
     var=[u"Chiffrer le coût sur dix démarrages quotidiens.",
          u"Chercher le plugin dont le retrait gagne le plus."],
     gamif=u"G-05 La collection de badges",
     bareme=u"1 point si le total est exact."),

dict(id=u"PL-15", titre=u"Combien de plugins pour douze composants",
     them=u"PL4 · Plugins fonctionnels",
     ref=u"REF-038, REF-039",
     niv=u"Perfectionnement", duree=22, prereq=u"PL-07",
     verdict=u"competence",
     competence=u"Couvrir un besoin en composants par le plus petit nombre "
                u"de plugins, en exploitant leurs recouvrements.",
     bloom=u"Analyser × procédurale",
     contexte=u"Chaque plugin installé est une dépendance de plus à "
              u"maintenir, à faire installer par l'apprenant et à revérifier "
              u"à chaque version de Rhino. On en installe le moins possible.",
     obj=u"Couvrir un besoin en composants par le plus petit nombre de "
         u"plugins, en exploitant leurs recouvrements.",
     enonce=u"La définition à reprendre emploie douze composants non natifs. "
            u"Le tableau donne ce qu'apporte chacun des six plugins "
            u"candidats. Donnez le nombre MINIMAL de plugins à installer pour "
            u"couvrir les douze.",
     depart=u"La liste des douze composants requis et le tableau des six "
            u"plugins avec leurs apports.",
     att=u"4 plugins suffisent à couvrir les douze composants.",
     erreur=u"Installer un plugin par composant manquant — douze, ou les six "
            u"disponibles « pour être tranquille ». Les plugins se "
            u"RECOUVRENT : `Mesh Thicken` vient de deux d'entre eux, "
            u"`Catmull-Clark` aussi, et c'est ce recouvrement qui fait "
            u"descendre le compte de six à quatre.",
     donnees_note=u"Six plugins, douze composants, quatre suffisent — et deux "
                  u"quartets différents y parviennent. C'est le NOMBRE qui "
                  u"est demandé, précisément parce qu'il est unique là où la "
                  u"solution ne l'est pas. Aucun trio ne couvre le besoin : "
                  u"la réponse ne s'obtient pas au jugé.",
     limite=u"Le minimum porte sur les COMPOSANTS. Il ignore le poids des "
            u"plugins, leur stabilité et leur licence : quatre plugins "
            u"abandonnés valent moins que cinq maintenus, et cet arbitrage-là "
            u"ne se calcule pas.",
     mode=u"SingleValue", tol=u"0", nb=9,
     comp=u"Data, Create Set, Set Union, Set Difference, List Length, Panel",
     etapes=[u"Poser les six ensembles d'apports.",
             u"Écarter d'emblée les plugins dont l'apport est déjà couvert.",
             u"Chercher la plus petite réunion qui contienne les douze.",
             u"Vérifier qu'aucun trio n'y parvient."],
     pieges=[u"Compter un plugin par composant.",
             u"Croire la solution unique et rendre une liste de noms."],
     var=[u"Donner le quartet le plus léger en temps de chargement.",
          u"Refaire le calcul en retirant LunchBox du catalogue."],
     gamif=u"G-21 Le golf de composants",
     bareme=u"1 point si le minimum est exact."),

dict(id=u"PL-16", titre=u"Ce qui tourne encore sous Rhino 8",
     them=u"PL1 · Écosystème de plugins",
     ref=u"REF-029, REF-038, REF-039",
     niv=u"Intermédiaire", duree=12, prereq=u"PL-09",
     verdict=u"competence",
     competence=u"Vérifier la compatibilité d'un parc de plugins avec une "
                u"version cible, en tenant les DEUX bornes.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Migrer une salle de formation vers une nouvelle version de "
              u"Rhino se prépare : un plugin abandonné à la version 7 ne "
              u"chargera pas, et la définition qui l'emploie s'ouvrira en "
              u"rouge devant les apprenants.",
     obj=u"Vérifier la compatibilité d'un parc de plugins avec une version "
         u"cible, en tenant les DEUX bornes.",
     enonce=u"Le tableau donne, pour quatorze plugins, la version de Rhino "
            u"minimale et la version maximale supportée. Donnez le nombre de "
            u"plugins compatibles avec Rhino 8.",
     depart=u"Le tableau des quatorze plugins et de leurs deux bornes.",
     att=u"10 plugins sur 14 sont compatibles avec Rhino 8.",
     erreur=u"Ne regarder que la version MINIMALE : quatorze sur quatorze, "
            u"puisque aucun n'exige mieux que Rhino 8. Un intervalle a deux "
            u"bornes, et ce sont les quatre plugins abandonnés en 6 ou en 7 "
            u"qui feront échouer la migration.",
     donnees_note=u"Quatorze plugins, dont quatre s'arrêtent avant la "
                  u"version 8. La borne minimale ne rejette personne : le "
                  u"test naïf donne donc le score parfait, ce qui est "
                  u"exactement ce qui le rend crédible.",
     limite=u"La compatibilité DÉCLARÉE n'est pas la compatibilité observée. "
            u"Un plugin annoncé pour Rhino 8 peut échouer sur une fonction "
            u"précise, et un plugin annoncé pour Rhino 7 fonctionner "
            u"parfaitement. Le tableau donne une présomption, pas un test.",
     mode=u"SingleValue", tol=u"0", nb=8,
     comp=u"Data, Smaller Than, Larger Than, Gate And, Cull Pattern, "
          u"List Length, Panel",
     etapes=[u"Tester la borne minimale : au plus 8.",
             u"Tester la borne maximale : au moins 8.",
             u"Combiner les deux par un ET.",
             u"Compter les vrais."],
     pieges=[u"N'appliquer qu'une des deux bornes.",
             u"Employer une comparaison stricte là où la version 8 est "
             u"elle-même admise."],
     var=[u"Refaire le compte pour Rhino 9.",
          u"Donner la liste des plugins qui bloquent la migration."],
     gamif=u"G-18 Vrai ou faux à élimination",
     bareme=u"1 point si le compte est exact."),

dict(id=u"RH-24", titre=u"Les parois trop minces après mise à l'échelle",
     them=u"RH5 · Préparation à l'impression 3D",
     ref=u"REF-016, REF-017, REF-018",
     niv=u"Débutant", duree=15, prereq=u"RH-10",
     verdict=u"competence",
     competence=u"Confronter un relevé d'épaisseurs à la contrainte "
                u"machine APRÈS mise à l'échelle, et non avant.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Une maquette se réduit pour tenir dans le volume "
              u"d'impression. Les parois se réduisent avec elle, et celles "
              u"qui passaient au 1/1 ne passent plus.",
     obj=u"Confronter un relevé d'épaisseurs à la contrainte machine APRÈS "
         u"mise à l'échelle, et non avant.",
     enonce=u"Le relevé donne dix-huit épaisseurs de paroi, en centièmes de "
            u"millimètre. La pièce sera imprimée à 62 % de sa taille, et la "
            u"machine ne tient pas sous 1,20 mm. Donnez le nombre de parois "
            u"qui ne passeront pas.",
     depart=u"Les dix-huit épaisseurs relevées, le facteur d'échelle et le "
            u"minimum machine.",
     att=u"12 parois passent sous le minimum après réduction.",
     erreur=u"Juger les épaisseurs AVANT la mise à l'échelle : cinq "
            u"seulement. Sept parois franchissent le seuil pendant la "
            u"réduction — elles sortiront de la machine en dentelle, et rien "
            u"dans le modèle au 1/1 ne le laissait voir.",
     donnees_note=u"Dix-huit épaisseurs de 0,40 à 3,40 mm. Le facteur 0,62 "
                  u"place le seuil effectif à 1,94 mm au 1/1 : sept parois "
                  u"tombent entre 1,20 et 1,94, et ce sont elles qui font "
                  u"toute la différence entre les deux réponses.",
     limite=u"Le compte suppose une réduction UNIFORME. Une mise à l'échelle "
            u"non uniforme — pour tenir dans un plateau étroit — réduit "
            u"différemment selon l'axe, et l'épaisseur d'une paroi dépend "
            u"alors de son orientation.",
     mode=u"SingleValue", tol=u"0", nb=8,
     comp=u"Data, Division, Multiplication, Smaller Than, Cull Pattern, "
          u"List Length, Panel",
     etapes=[u"Ramener les centièmes en millimètres.",
             u"Appliquer le facteur d'échelle.",
             u"Comparer au minimum machine.",
             u"Compter les parois retenues."],
     pieges=[u"Comparer avant la mise à l'échelle.",
             u"Oublier la conversion des centièmes."],
     var=[u"Chercher le facteur maximal qui ne sacrifie aucune paroi.",
          u"Refaire le compte pour une machine à 0,8 mm."],
     gamif=u"G-26 Le retour visuel immédiat",
     bareme=u"1 point si le compte est exact."),

dict(id=u"RH-25", titre=u"Les volumes réellement étanches",
     them=u"RH3 · Préparation à l'impression 3D",
     ref=u"REF-019, REF-020, REF-021",
     niv=u"Débutant", duree=14, prereq=u"RH-08",
     verdict=u"competence",
     competence=u"Établir l'étanchéité d'une polysurface en tenant compte "
                u"des arêtes non-manifold autant que des arêtes nues.",
     bloom=u"Analyser × conceptuelle",
     contexte=u"Un solide qui n'est pas étanche ne s'imprime pas. Le "
              u"diagnostic se lit sur deux compteurs, et le second est "
              u"régulièrement ignoré.",
     obj=u"Établir l'étanchéité d'une polysurface en tenant compte des arêtes "
         u"non-manifold autant que des arêtes nues.",
     enonce=u"Le rapport d'analyse donne, pour douze polysurfaces, le nombre "
            u"d'arêtes nues et le nombre d'arêtes non-manifold. Donnez le "
            u"nombre de polysurfaces réellement étanches.",
     depart=u"Le rapport des douze polysurfaces et de leurs deux compteurs.",
     att=u"6 polysurfaces sur 12 sont réellement étanches.",
     erreur=u"Ne regarder que les arêtes nues : huit. Deux polysurfaces sans "
            u"aucune arête nue portent des arêtes NON-MANIFOLD — trois faces "
            u"partagent la même arête. Elles sont fermées et invalides : "
            u"aucun trancheur n'en tirera un parcours d'outil.",
     donnees_note=u"Douze polysurfaces, dont deux à zéro arête nue mais avec "
                  u"des non-manifold, et une qui cumule les deux défauts. "
                  u"L'écart entre les deux réponses tient à ces deux cas — "
                  u"les seuls que le compteur d'arêtes nues déclare bons.",
     limite=u"Les deux compteurs à zéro rendent une polysurface FERMÉE. Ils "
            u"ne disent rien des faces retournées ni des "
            u"auto-intersections : un solide étanche peut encore être "
            u"impossible à imprimer, et c'est l'objet de RH-08.",
     mode=u"SingleValue", tol=u"0", nb=8,
     comp=u"Data, Equality, Gate And, Cull Pattern, List Length, Panel",
     etapes=[u"Tester l'égalité à zéro sur les arêtes nues.",
             u"Faire de même sur les arêtes non-manifold.",
             u"Combiner par un ET.",
             u"Compter les vrais."],
     pieges=[u"Ne tester qu'un des deux compteurs.",
             u"Employer un OU au lieu d'un ET."],
     var=[u"Donner le nombre de polysurfaces à corriger en priorité.",
          u"Distinguer les défauts réparables des autres."],
     gamif=u"G-20 La chasse aux bugs",
     bareme=u"1 point si le compte est exact."),

dict(id=u"RH-26", titre=u"Le poids du fichier à envoyer",
     them=u"RH5 · Préparation à l'impression 3D",
     ref=u"REF-022, REF-023, REF-024",
     niv=u"Débutant", duree=12, prereq=u"RH-22",
     verdict=u"competence",
     competence=u"Prévoir le poids d'un export maillé à partir du nombre de "
                u"triangles et du format retenu.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Un STL s'envoie à un prestataire. Savoir avant l'export s'il "
              u"fera sept mégaoctets ou trente-cinq décide du format et du "
              u"moyen de transmission.",
     obj=u"Prévoir le poids d'un export maillé à partir du nombre de "
         u"triangles et du format retenu.",
     enonce=u"Le maillage compte 148 520 triangles. Un STL binaire pèse "
            u"84 octets d'en-tête plus 50 octets par triangle. Donnez le "
            u"poids du fichier, en octets.",
     depart=u"Le nombre de triangles du maillage et la structure du format.",
     att=u"7 426 084 octets, soit 7,08 Mo.",
     erreur=u"Exporter en STL ASCII sans y penser : environ 35 Mo pour le "
            u"même maillage, cinq fois plus lourd, pour une géométrie "
            u"strictement identique. Le format par défaut de la boîte de "
            u"dialogue n'est pas toujours le binaire.",
     donnees_note=u"148 520 triangles est un maillage de pièce courante, ni "
                  u"trivial ni monstrueux. La structure du binaire est "
                  u"FIXE — 84 + 50 n —, ce qui rend le calcul exact et "
                  u"vérifiable à l'octet près, là où l'ASCII ne peut "
                  u"s'estimer.",
     limite=u"La formule vaut pour le STL BINAIRE, dont chaque triangle "
            u"occupe exactement cinquante octets. L'OBJ, le 3MF et le PLY ont "
            u"des structures différentes, et le 3MF est compressé : son "
            u"poids dépend de la géométrie elle-même.",
     mode=u"SingleValue", tol=u"0", nb=5,
     comp=u"Slider, Multiplication, Addition, Panel",
     etapes=[u"Multiplier le nombre de triangles par cinquante.",
             u"Ajouter les quatre-vingt-quatre octets d'en-tête."],
     pieges=[u"Oublier l'en-tête.",
             u"Confondre octets et bits, ou mégaoctets et mébioctets."],
     var=[u"Donner le nombre de triangles tenant dans une pièce jointe "
          u"de 10 Mo.",
          u"Comparer au poids du même maillage en 3MF."],
     gamif=u"G-05 La collection de badges",
     bareme=u"1 point si le poids est exact à l'octet."),

dict(id=u"RH-27", titre=u"Le volume d'un assemblage de primitives",
     them=u"RH2 · Modélisation Rhino",
     ref=u"REF-007, REF-008",
     niv=u"Débutant", duree=16, prereq=u"RH-05",
     verdict=u"competence",
     competence=u"Chiffrer la matière d'un assemblage de primitives en "
                u"déduisant ce qu'elles ont en commun.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Un socle et son fût se commandent au volume de matière. Les "
              u"deux se recouvrent là où le second s'encastre dans le "
              u"premier, et cette matière-là n'existe qu'une fois.",
     obj=u"Chiffrer la matière d'un assemblage de primitives en déduisant ce "
         u"qu'elles ont en commun.",
     enonce=u"Le socle mesure 240 × 160 × 40 mm. Le fût cylindrique fait "
            u"45 mm de rayon et 120 mm de haut, et s'encastre de 15 mm dans "
            u"le socle. Donnez le volume de matière, en décimètres cubes.",
     depart=u"Les cotes du socle, celles du fût et la profondeur "
            u"d'encastrement.",
     att=u"2,2040 dm³ de matière, à 0,0001 près.",
     erreur=u"Additionner les deux volumes : 2,2994 dm³. Les 15 mm "
            u"d'encastrement sont comptés deux fois — une fois dans le "
            u"socle, une fois dans le fût. L'écart est de 4 %, assez pour "
            u"fausser un devis de fonderie, trop peu pour se voir.",
     donnees_note=u"Le recouvrement vaut 95 426 mm³, soit 4,3 % du total. "
                  u"C'est l'ordre de grandeur d'une erreur qui passe : "
                  u"au-delà de 20 % on la cherche, en dessous de 1 % elle ne "
                  u"coûte rien.",
     limite=u"Le volume est celui de la GÉOMÉTRIE. Une pièce fondue y ajoute "
            u"les dépouilles, les congés de raccordement et la surépaisseur "
            u"d'usinage, que ce calcul ignore.",
     mode=u"NumericTolerance", tol=u"0.0001", nb=9,
     comp=u"Slider, Multiplication, Pi, Subtraction, Division, Panel",
     etapes=[u"Calculer le volume du socle.",
             u"Calculer celui du fût entier.",
             u"Calculer le volume encastré : le disque du fût sur 15 mm.",
             u"Additionner les deux premiers et retrancher le troisième."],
     pieges=[u"Additionner sans déduire.",
             u"Retrancher le volume du fût entier au lieu de la seule partie "
             u"encastrée."],
     var=[u"Faire varier l'encastrement et suivre le volume.",
          u"Chercher l'encastrement qui ramène le volume à 2,15 dm³."],
     gamif=u"G-14 Le puzzle de câblage",
     bareme=u"1 point si le volume est juste à 0,0001 dm³."),

dict(id=u"RH-28", titre=u"La surface d'une extrusion",
     them=u"RH2 · Modélisation Rhino",
     ref=u"REF-009, REF-010, REF-011",
     niv=u"Débutant", duree=14, prereq=u"RH-04",
     verdict=u"competence",
     competence=u"Établir la surface développée d'une extrusion à partir du "
                u"périmètre de son contour, refermé.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Le bardage d'un local technique se commande au mètre carré. "
              u"Sa surface est celle du contour au sol, développé sur la "
              u"hauteur.",
     obj=u"Établir la surface développée d'une extrusion à partir du "
         u"périmètre de son contour, refermé.",
     enonce=u"Le contour au sol vous est donné par ses cinq sommets, en "
            u"millimètres. Le bardage monte à 2 600 mm. Donnez sa surface, en "
            u"mètres carrés.",
     depart=u"Les cinq sommets du contour et la hauteur de bardage.",
     att=u"15,7566 m² de bardage, à 0,0001 près.",
     erreur=u"Laisser le contour OUVERT : 12,1166 m², soit 3,64 m² de moins. "
            u"Le segment de fermeture mesure 1 400 mm — c'est un mur entier, "
            u"et l'aperçu d'une polyligne ouverte ressemble à celui d'une "
            u"polyligne fermée.",
     donnees_note=u"Cinq sommets, dont un pan coupé oblique qui interdit de "
                  u"retrouver le périmètre par une somme de cotes lues sur "
                  u"le plan. Le segment de fermeture pèse 23 % du total : "
                  u"l'oubli ne se rattrape pas au jugé.",
     limite=u"La surface est celle de l'ENVELOPPE. Elle ne déduit ni les "
            u"portes ni les grilles de ventilation, et n'ajoute pas les "
            u"recouvrements de lames : la commande se fait sur une surface "
            u"majorée.",
     mode=u"NumericTolerance", tol=u"0.0001", nb=8,
     comp=u"Data, Construct Point, PolyLine, Length, Multiplication, "
          u"Division, Panel",
     etapes=[u"Construire les cinq points depuis leurs coordonnées.",
             u"Tracer la polyligne en la refermant.",
             u"Mesurer sa longueur.",
             u"Multiplier par la hauteur, puis convertir en mètres carrés."],
     pieges=[u"Laisser la polyligne ouverte.",
             u"Convertir une seule fois au lieu de deux : les millimètres "
             u"carrés font un million par mètre carré."],
     var=[u"Déduire une porte de 900 × 2 100.",
          u"Refaire le calcul pour une hauteur variable."],
     gamif=u"G-14 Le puzzle de câblage",
     bareme=u"1 point si la surface est juste à 0,0001 m²."),

dict(id=u"RH-29", titre=u"La platine percée en réseau",
     them=u"RH3 · Modélisation Rhino",
     ref=u"REF-012, REF-013",
     niv=u"Débutant", duree=14, prereq=u"RH-05",
     verdict=u"competence",
     competence=u"Chiffrer la matière restante après un réseau de "
                u"percements, en distinguant rayon et diamètre.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Une platine percée se pèse pour le transport et se chiffre "
              u"au kilo. Vingt-quatre trous enlèvent une matière qui compte.",
     obj=u"Chiffrer la matière restante après un réseau de percements, en "
         u"distinguant rayon et diamètre.",
     enonce=u"La platine mesure 900 × 600 × 12 mm. Elle reçoit un réseau de "
            u"6 par 4 trous traversants de 22 mm de diamètre. Donnez le "
            u"volume de matière restante, en décimètres cubes.",
     depart=u"Les cotes de la platine, la trame et le diamètre des trous.",
     att=u"6,3705 dm³ de matière restante, à 0,0001 près.",
     erreur=u"Prendre le diamètre pour le rayon dans l'aire du disque : "
            u"6,0421 dm³. L'aire va comme le CARRÉ du rayon — l'erreur "
            u"quadruple le volume percé, et la platine est annoncée 5 % plus "
            u"légère qu'elle n'est.",
     donnees_note=u"Vingt-quatre trous de 22 mm dans 12 mm d'épaisseur "
                  u"retirent 109 500 mm³, soit 1,7 % de la platine. L'erreur "
                  u"de rayon en retire quatre fois plus : 6,8 %. Les deux "
                  u"réponses restent plausibles pour une platine d'acier.",
     limite=u"Le volume suppose des trous CYLINDRIQUES et traversants. Un "
            u"perçage fraisé ou taraudé enlève davantage, et la tolérance de "
            u"perçage — un dixième sur le diamètre — pèse plus que la "
            u"précision affichée ici.",
     mode=u"NumericTolerance", tol=u"0.0001", nb=10,
     comp=u"Slider, Multiplication, Division, Pi, Subtraction, Panel",
     etapes=[u"Calculer le volume plein de la platine.",
             u"Diviser le diamètre par deux pour obtenir le rayon.",
             u"Calculer le volume d'un trou, puis des vingt-quatre.",
             u"Retrancher."],
     pieges=[u"Employer le diamètre comme rayon.",
             u"Oublier de multiplier par le nombre de trous."],
     var=[u"Donner la masse en acier à 7,85 g/cm³.",
          u"Chercher le diamètre qui allège la platine de 10 %."],
     gamif=u"G-20 La chasse aux bugs",
     bareme=u"1 point si le volume est juste à 0,0001 dm³."),

dict(id=u"RH-30", titre=u"Ce que le filtre de sélection retient",
     them=u"RH1 · Interface et navigation Rhino",
     ref=u"REF-003, REF-004",
     niv=u"Débutant", duree=12, prereq=u"RH-01",
     verdict=u"competence",
     competence=u"Prévoir le résultat d'une sélection filtrée en tenant "
                u"compte de ce qui est verrouillé.",
     bloom=u"Analyser × conceptuelle",
     contexte=u"Sélectionner par type et par calque est le geste de base "
              u"d'un fichier bien rangé. Ce qui est verrouillé n'entre pas "
              u"dans la sélection, et l'oublier fait croire à un fichier "
              u"incomplet.",
     obj=u"Prévoir le résultat d'une sélection filtrée en tenant compte de ce "
         u"qui est verrouillé.",
     enonce=u"L'inventaire donne, pour seize objets, leur type, leur calque "
            u"et leur état de verrouillage. Donnez le nombre d'objets que "
            u"retient une sélection des courbes du calque 10-Porteurs.",
     depart=u"L'inventaire des seize objets et de leurs trois attributs.",
     att=u"3 objets sont retenus par la sélection.",
     erreur=u"Ignorer le verrouillage : cinq. Deux courbes du bon calque sont "
            u"verrouillées et n'entreront jamais dans la sélection — "
            u"l'apprenant cherche alors pourquoi son compte ne tombe pas, "
            u"sans penser au cadenas.",
     donnees_note=u"Seize objets répartis sur trois calques et quatre types. "
                  u"Cinq courbes sont sur 10-Porteurs, dont deux "
                  u"verrouillées : les deux réponses sont proches et toutes "
                  u"deux crédibles devant un fichier qu'on découvre.",
     limite=u"Le compte suppose que le verrouillage vient de l'OBJET. Un "
            u"objet peut aussi être inaccessible parce que son calque est "
            u"verrouillé, ce que l'inventaire ne distingue pas ici et qui "
            u"produit le même symptôme.",
     mode=u"SingleValue", tol=u"0", nb=9,
     comp=u"Data, Equality, Gate Not, Gate And, Cull Pattern, List Length, "
          u"Panel",
     etapes=[u"Tester l'égalité du type à « Courbe ».",
             u"Tester l'égalité du calque à « 10-Porteurs ».",
             u"Prendre la négation du verrouillage.",
             u"Combiner les trois par des ET, puis compter."],
     pieges=[u"Oublier la troisième condition.",
             u"Employer un OU entre le type et le calque."],
     var=[u"Compter ce que retiendrait le même filtre après déverrouillage.",
          u"Donner le calque le mieux fourni en courbes."],
     gamif=u"G-16 La chasse au trésor",
     bareme=u"1 point si le compte est exact."),

dict(id=u"RH-31", titre=u"Ce qui reste visible",
     them=u"RH1 · Interface et navigation Rhino",
     ref=u"REF-005, REF-006",
     niv=u"Débutant", duree=12, prereq=u"RH-06",
     verdict=u"competence",
     competence=u"Distinguer la visibilité d'un objet de celle de son "
                u"calque, deux mécanismes qui produisent le même symptôme.",
     bloom=u"Analyser × conceptuelle",
     contexte=u"Un objet qui n'apparaît pas peut être masqué, ou reposer sur "
              u"un calque éteint. Le remède n'est pas le même, et « Montrer "
              u"tout » ne règle que le premier cas.",
     obj=u"Distinguer la visibilité d'un objet de celle de son calque, deux "
         u"mécanismes qui produisent le même symptôme.",
     enonce=u"L'inventaire donne, pour dix-huit objets, leur groupe, la "
            u"visibilité de leur calque et leur propre état de masquage. "
            u"Donnez le nombre d'objets réellement visibles à l'écran.",
     depart=u"L'inventaire des dix-huit objets et de leurs trois attributs.",
     att=u"10 objets sont réellement visibles.",
     erreur=u"Ne regarder que le masquage d'objet : treize. Trois objets "
            u"non masqués reposent sur un calque éteint — « Montrer tout » "
            u"ne les fera pas revenir, et c'est le motif d'appel le plus "
            u"fréquent en formation.",
     donnees_note=u"Dix-huit objets, dont cinq masqués individuellement et "
                  u"quatre sur calque éteint, avec un recouvrement d'un "
                  u"objet cumulant les deux. Les deux causes se distinguent "
                  u"donc, et le total ne s'obtient par aucune soustraction "
                  u"simple.",
     limite=u"L'inventaire ignore l'ISOLATION, troisième mécanisme : isoler "
            u"une sélection masque tout le reste sans toucher aux calques ni "
            u"aux objets, et se défait par une commande encore différente.",
     mode=u"SingleValue", tol=u"0", nb=8,
     comp=u"Data, Gate Not, Gate And, Cull Pattern, List Length, Panel",
     etapes=[u"Prendre la colonne de visibilité de calque.",
             u"Prendre la négation du masquage d'objet.",
             u"Combiner par un ET, puis compter."],
     pieges=[u"Ne tester qu'un des deux mécanismes.",
             u"Additionner les deux causes en croyant qu'elles s'excluent."],
     var=[u"Compter les objets qu'un « Montrer tout » ferait réapparaître.",
          u"Donner le groupe le plus affecté."],
     gamif=u"G-26 Le retour visuel immédiat",
     bareme=u"1 point si le compte est exact."),

dict(id=u"RH-32", titre=u"Ce qui suivra le calque",
     them=u"RH2 · Organisation du document Rhino",
     ref=u"REF-014, REF-015, REF-143",
     niv=u"Débutant", duree=12, prereq=u"RH-07",
     verdict=u"competence",
     competence=u"Prévoir quels objets suivront un changement de calque, "
                u"selon que leur couleur est héritée ou forcée.",
     bloom=u"Analyser × conceptuelle",
     contexte=u"Changer la couleur d'un calque doit changer celle de ses "
              u"objets. Ceux dont la couleur a été forcée à la main ne "
              u"bougeront pas, et le plan ressort en deux teintes.",
     obj=u"Prévoir quels objets suivront un changement de calque, selon que "
         u"leur couleur est héritée ou forcée.",
     enonce=u"L'inventaire donne la couleur de vingt objets : « ParCalque » "
            u"ou une couleur propre. Le calque va changer de couleur. Donnez "
            u"le nombre d'objets qui suivront.",
     depart=u"L'inventaire des couleurs des vingt objets.",
     att=u"13 objets suivront le calque.",
     erreur=u"Compter les couleurs PROPRES — sept — en croyant répondre à la "
            u"question. Ce sont justement celles qui ne suivront pas : "
            u"l'inventaire se lit dans le sens de la question, et les deux "
            u"comptes se complètent à vingt.",
     donnees_note=u"Vingt objets, treize hérités et sept forcés en quatre "
                  u"couleurs différentes. Ni la majorité écrasante ni la "
                  u"moitié : les deux réponses sont distinctes, et aucune ne "
                  u"se devine.",
     limite=u"La couleur n'est qu'une des propriétés héritées. Type de "
            u"ligne, épaisseur d'impression et matériau suivent la même "
            u"logique et peuvent être forcés séparément : un objet peut "
            u"suivre son calque en couleur et pas en matériau.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Data, Equality, Cull Pattern, List Length, Panel",
     etapes=[u"Tester l'égalité de la couleur à « ParCalque ».",
             u"Compter les vrais."],
     pieges=[u"Compter les couleurs forcées.",
             u"Confondre la couleur d'affichage et la couleur d'impression."],
     var=[u"Donner le nombre d'objets à repasser en ParCalque.",
          u"Compter les couleurs propres distinctes."],
     gamif=u"G-01 Le tableau des scores",
     bareme=u"1 point si le compte est exact."),

dict(id=u"GP-13", titre=u"La pièce qui enchaîne trois opérations",
     them=u"GP5 · Synthèse géométrie",
     ref=u"REF-073, REF-147, REF-148",
     niv=u"Intermédiaire", duree=22, prereq=u"GP-11",
     verdict=u"competence",
     competence=u"Ordonner congé, perçage et épaississement de sorte que "
                u"chaque opération reçoive ce dont elle a besoin.",
     bloom=u"Créer × procédurale",
     contexte=u"Une platine de fixation se dessine à plat, se congé, se "
              u"perce, puis s'épaissit. L'ordre n'est pas indifférent : "
              u"épaissir d'abord oblige à percer un solide.",
     obj=u"Ordonner congé, perçage et épaississement de sorte que chaque "
         u"opération reçoive ce dont elle a besoin.",
     enonce=u"La platine mesure 420 × 260 mm, ses quatre angles portent un "
            u"congé de 35 mm de rayon, et elle reçoit sept perçages de 26 mm "
            u"de diamètre. Elle fait 18 mm d'épaisseur. Donnez son volume, en "
            u"décimètres cubes.",
     depart=u"Les cotes de la platine, le rayon de congé, le diamètre et le "
            u"nombre de perçages, l'épaisseur.",
     att=u"1,8798 dm³, à 0,0001 près.",
     erreur=u"Oublier les congés : 1,8987 dm³. Un congé de rayon r retire à "
            u"chaque angle la différence entre le carré de côté r et le "
            u"quart de disque, soit (4 − π)r² pour les quatre — ici "
            u"1 052 mm², un demi-pour-cent du volume. C'est peu, et c'est "
            u"précisément pourquoi on ne le voit pas.",
     donnees_note=u"Les congés retirent 1 052 mm² et les perçages "
                  u"3 717 mm² : les seconds pèsent trois fois plus, ce qui "
                  u"rend l'oubli des premiers d'autant plus facile. Sept "
                  u"perçages, nombre impair, interdisent de retrouver l'aire "
                  u"par symétrie.",
     limite=u"Le volume suppose que les perçages ne rencontrent PAS les "
            u"congés. Un huitième perçage placé dans un angle recouperait la "
            u"matière déjà retirée, et la soustraction cesserait d'être une "
            u"simple somme.",
     mode=u"NumericTolerance", tol=u"0.0001", nb=11,
     comp=u"Slider, Multiplication, Pi, Subtraction, Division, Panel",
     etapes=[u"Calculer l'aire du rectangle plein.",
             u"Retrancher ce que les quatre congés enlèvent : (4 − π) r².",
             u"Retrancher l'aire des sept perçages.",
             u"Multiplier par l'épaisseur, puis convertir."],
     pieges=[u"Oublier les congés.",
             u"Retrancher quatre quarts de disque au lieu de la différence."],
     var=[u"Faire varier le rayon de congé jusqu'à ce qu'il rencontre un "
          u"perçage.",
          u"Chercher l'épaisseur qui donne exactement 2 dm³."],
     gamif=u"G-21 Le golf de composants",
     bareme=u"1 point si le volume est juste à 0,0001 dm³."),

dict(id=u"WB-10", titre=u"Ce qu'un format d'échange laisse en route",
     them=u"WB3 · Interopérabilité",
     ref=u"REF-111, REF-112, REF-158",
     niv=u"Perfectionnement", duree=15, prereq=u"WB-09",
     verdict=u"competence",
     competence=u"Savoir, avant d'exporter, quelles propriétés du modèle le "
                u"format retenu ne transportera pas.",
     bloom=u"Analyser × factuelle",
     contexte=u"Transmettre un modèle à un bureau d'études, c'est choisir ce "
              u"qu'on accepte de perdre. Le choix se fait avant l'export, "
              u"pas quand le destinataire signale que les calques ont "
              u"disparu.",
     obj=u"Savoir, avant d'exporter, quelles propriétés du modèle le format "
         u"retenu ne transportera pas.",
     enonce=u"Le tableau donne, pour huit propriétés du modèle, les formats "
            u"qui les transportent. Donnez le nombre de propriétés perdues "
            u"par un export au format STEP.",
     depart=u"Le tableau des huit propriétés et des formats qui les portent.",
     att=u"5 propriétés sur 8 sont perdues par un export STEP.",
     erreur=u"Compter ce que STEP CONSERVE — trois — en croyant répondre. La "
            u"question porte sur la perte, et c'est elle qui décide : un "
            u"modèle exporté en STEP arrive sans matériaux, sans blocs, sans "
            u"historique, sans couleurs d'objet et sans maillages.",
     donnees_note=u"Huit propriétés et cinq formats. Le 3DM les porte toutes, "
                  u"ce qui donne au tableau son point de comparaison ; aucun "
                  u"autre format n'en porte plus de quatre, et les pertes "
                  u"diffèrent d'un format à l'autre — DWG en perd quatre, "
                  u"mais pas les mêmes.",
     limite=u"Le tableau raisonne par PROPRIÉTÉ, pas par fidélité. Un STEP "
            u"transporte la géométrie NURBS, mais un échange réel dégrade "
            u"aussi les tolérances et peut casser des surfaces trimées : la "
            u"propriété survit, sa qualité pas toujours.",
     mode=u"SingleValue", tol=u"0", nb=7,
     comp=u"Data, Member Index, Gate Not, Cull Pattern, List Length, Panel",
     etapes=[u"Pour chaque propriété, chercher si STEP figure dans sa liste.",
             u"Prendre la négation.",
             u"Compter les propriétés retenues."],
     pieges=[u"Compter les propriétés conservées.",
             u"Oublier qu'une propriété peut être portée par plusieurs "
             u"formats."],
     var=[u"Refaire le compte pour DWG, puis pour OBJ.",
          u"Chercher le format qui préserve le plus de propriétés après "
          u"le 3DM."],
     gamif=u"G-18 Vrai ou faux à élimination",
     bareme=u"1 point si le compte est exact."),

dict(id=u"WB-11", titre=u"Le temps de calcul, une fois en ligne",
     them=u"WB2 · Publication web",
     ref=u"REF-108, REF-109, REF-110",
     niv=u"Perfectionnement", duree=16, prereq=u"WB-06",
     verdict=u"competence",
     competence=u"Estimer le temps de réponse d'une définition publiée en "
                u"ligne, en tenant compte de l'écart entre le poste et le "
                u"serveur.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Un configurateur publié doit répondre en quelques secondes. "
              u"Ce qui tourne en dix secondes sur le poste du concepteur "
              u"peut dépasser la limite du service une fois en ligne.",
     obj=u"Estimer le temps de réponse d'une définition publiée en ligne, en "
         u"tenant compte de l'écart entre le poste et le serveur.",
     enonce=u"Le profilage donne le temps de recalcul des vingt-quatre "
            u"composants sur votre poste, en millisecondes. Le serveur est "
            u"2,4 fois plus lent. Donnez le temps de réponse en ligne, en "
            u"secondes.",
     depart=u"Le relevé des vingt-quatre temps et le facteur serveur.",
     att=u"25,1736 s de temps de réponse en ligne, à 0,0001 près.",
     erreur=u"Oublier le facteur serveur : 10,489 s, sous la limite de vingt "
            u"secondes. La définition est alors publiée, et c'est le premier "
            u"visiteur qui découvre qu'elle dépasse — le profilage local "
            u"donne toujours le résultat rassurant.",
     donnees_note=u"Vingt-quatre composants de 20 à 900 ms. Le total local "
                  u"passe sous la limite, le total en ligne la dépasse de "
                  u"cinq secondes : c'est le cas qui décide, et il est "
                  u"invisible tant qu'on ne multiplie pas.",
     limite=u"Le facteur 2,4 est une MOYENNE mesurée. Il varie avec le type "
            u"d'opération — un maillage et une intersection ne se dégradent "
            u"pas dans le même rapport — et ne dit rien de la latence "
            u"réseau, qui s'ajoute au temps de calcul.",
     mode=u"NumericTolerance", tol=u"0.0001", nb=6,
     comp=u"Data, Mass Addition, Multiplication, Division, Panel",
     etapes=[u"Sommer les vingt-quatre temps locaux.",
             u"Multiplier par le facteur serveur.",
             u"Convertir en secondes."],
     pieges=[u"Oublier le facteur.",
             u"Multiplier chaque temps puis re-multiplier la somme."],
     var=[u"Chercher les composants à retirer pour tenir sous vingt "
          u"secondes.",
          u"Refaire le calcul avec un facteur de 1,8."],
     gamif=u"G-03 Contre la montre",
     bareme=u"1 point si le temps est juste à 0,0001 s."),

dict(id=u"IA-26", titre=u"Transposer, et le prouver sur un second jeu",
     them=u"IA2 · Composants scriptés assistés",
     ref=u"REF-122, REF-123",
     niv=u"Intermédiaire", duree=18, prereq=u"IA-06",
     verdict=u"competence",
     competence=u"Établir qu'un script porté vers un autre langage produit "
                u"exactement la même chose, sur un jeu qu'il n'a pas servi à "
                u"écrire.",
     bloom=u"Analyser × procédurale",
     contexte=u"Reprendre une définition ancienne maintenue en VB.NET, c'est "
              u"la porter sans changer un résultat dont personne ne se "
              u"souvient de la règle exacte.",
     obj=u"Établir qu'un script porté vers un autre langage produit "
         u"exactement la même chose, sur un jeu qu'il n'a pas servi à "
         u"écrire.",
     enonce=u"Le composant existant produit les sommes cumulées d'une liste. "
            u"Faites-le porter vers un autre langage, puis appliquez les deux "
            u"versions au jeu de preuve fourni et donnez les quatorze valeurs "
            u"obtenues.",
     depart=u"Le composant d'origine et le jeu de preuve de quatorze valeurs.",
     att=u"Les quatorze cumuls : 213, 230, 656, 1 011, 1 306, 1 560, 1 711, "
         u"1 801, 2 150, 2 234, 2 390, 2 524, 2 989, 3 141.",
     erreur=u"Vérifier le portage sur le jeu qui a servi à l'écrire. Les deux "
            u"versions s'y accordent forcément — c'est ce jeu-là que "
            u"l'assistant avait sous les yeux. La preuve n'a de valeur que "
            u"sur des données qu'il n'a pas vues.",
     donnees_note=u"Quatorze valeurs de 15 à 480, sans ordre. Le cumul est "
                  u"strictement croissant : un décalage d'un rang se voit "
                  u"immédiatement, et une somme oubliée décale tout ce qui "
                  u"suit. C'est ce qui rend la comparaison sévère.",
     limite=u"L'égalité sur quatorze valeurs établit que les deux versions "
            u"s'accordent SUR CE JEU. Un cas limite absent — liste vide, "
            u"valeur négative, dépassement de capacité — peut encore les "
            u"séparer, et c'est le défaut classique du portage.",
     mode=u"ExactOrderedList", tol=u"0", nb=5,
     comp=u"Data, Mass Addition, Partial Results, Panel",
     etapes=[u"Lire ce que fait le composant d'origine sur un petit jeu.",
             u"Faire produire la version dans l'autre langage.",
             u"Appliquer les deux au jeu de preuve.",
             u"Comparer élément par élément, dans l'ordre."],
     pieges=[u"Comparer des ensembles au lieu de listes ordonnées.",
             u"Prouver le portage sur le jeu d'origine."],
     var=[u"Ajouter une valeur négative au jeu et voir si l'accord tient.",
          u"Porter vers un troisième langage."],
     gamif=u"G-19 Le composant mystère",
     bareme=u"1 point si les quatorze valeurs concordent dans l'ordre."),

dict(id=u"IA-27", titre=u"Le script qui tourne et compte mal",
     them=u"IA2 · Composants scriptés assistés",
     ref=u"REF-124",
     niv=u"Intermédiaire", duree=16, prereq=u"IA-05",
     verdict=u"competence",
     competence=u"Localiser une erreur de bornes dans un code qui s'exécute "
                u"sans planter et rend un résultat crédible.",
     bloom=u"Analyser × procédurale",
     contexte=u"Un script qui plante se répare. Un script qui rend "
              u"quatorze au lieu de quinze se livre, et l'écart se découvre "
              u"trois semaines plus tard sur un autre jeu.",
     obj=u"Localiser une erreur de bornes dans un code qui s'exécute sans "
         u"planter et rend un résultat crédible.",
     enonce=u"Le composant fourni doit compter les longueurs qui dépassent "
            u"1 500 mm parmi les trente relevées. Il rend un résultat faux. "
            u"Corrigez-le et donnez le compte exact.",
     depart=u"Le composant fautif et les trente longueurs relevées.",
     att=u"15 longueurs dépassent 1 500 mm.",
     erreur=u"Accepter le quatorze que rend le composant. Sa boucle s'arrête "
            u"un cran trop tôt et ne teste jamais le dernier élément — qui "
            u"vaut ici 2 592 mm et dépasse largement. L'erreur ne se voit "
            u"que si la dernière valeur est justement concernée.",
     donnees_note=u"Trente longueurs de 200 à 3 200 mm, et la DERNIÈRE "
                  u"dépasse le seuil : le jeu est choisi pour que le défaut "
                  u"de bornes se manifeste. Sur les deux tiers des jeux "
                  u"possibles, le même code faux rendrait la bonne réponse.",
     limite=u"Le compte exact prouve que le défaut est corrigé, pas qu'il "
            u"est COMPRIS. Remplacer la boucle par un composant natif donne "
            u"la bonne valeur sans avoir jamais vu l'erreur — l'exercice "
            u"demande de la nommer, et cela se lit sur le canvas.",
     mode=u"SingleValue", tol=u"0", nb=6,
     comp=u"Data, Larger Than, Cull Pattern, List Length, Panel",
     etapes=[u"Comparer le résultat du composant à un comptage natif.",
             u"Chercher où les deux divergent : la dernière valeur.",
             u"Corriger la borne de la boucle.",
             u"Vérifier que les deux comptes coïncident."],
     pieges=[u"Corriger le seuil au lieu de la borne.",
             u"Conclure que le composant est juste parce qu'il ne plante "
             u"pas."],
     var=[u"Chercher un jeu sur lequel le code faux rend la bonne réponse.",
          u"Faire produire un test qui attrape ce défaut."],
     gamif=u"G-20 La chasse aux bugs",
     bareme=u"1 point si le compte corrigé est exact."),

dict(id=u"IA-28", titre=u"Regrouper des pièces par similarité",
     them=u"IA5 · Apprentissage automatique",
     ref=u"REF-130",
     niv=u"Perfectionnement", duree=20, prereq=u"IA-10",
     verdict=u"competence",
     competence=u"Regrouper des éléments sur plusieurs critères à la fois et "
                u"lire l'effectif du groupe dominant.",
     bloom=u"Analyser × procédurale",
     contexte=u"Rationaliser un débit, c'est ramener des pièces toutes "
              u"différentes à quelques familles. La famille la plus fournie "
              u"décide du réglage de la machine.",
     obj=u"Regrouper des éléments sur plusieurs critères à la fois et lire "
         u"l'effectif du groupe dominant.",
     enonce=u"Les vingt pièces vous sont données par leur longueur et leur "
            u"épaisseur. Regroupez-les selon qu'elles dépassent ou non "
            u"900 mm de long et 34 mm d'épaisseur. Donnez l'effectif du "
            u"groupe le plus fourni.",
     depart=u"Les vingt couples longueur-épaisseur et les deux seuils.",
     att=u"10 pièces dans le groupe le plus fourni.",
     erreur=u"Regrouper sur un seul critère. La longueur seule donne deux "
            u"groupes de dix ; c'est le CROISEMENT des deux critères qui "
            u"produit quatre familles d'effectifs 10, 4, 4 et 2 — et seul le "
            u"croisement dit quoi régler sur la machine.",
     donnees_note=u"Vingt pièces, quatre familles d'effectifs 10, 4, 4 et 2. "
                  u"Deux familles sont à égalité : le maximum, lui, est "
                  u"unique. Le groupe dominant rassemble la moitié des "
                  u"pièces, ce qui rend le regroupement utile plutôt que "
                  u"décoratif.",
     limite=u"Les seuils sont DONNÉS. Un vrai regroupement les cherche — "
            u"c'est ce que fait un algorithme de partitionnement — et le "
            u"nombre de familles devient lui-même un résultat, pas une "
            u"hypothèse.",
     mode=u"SingleValue", tol=u"0", nb=10,
     comp=u"Data, Larger Than, Gate And, Gate Not, Cull Pattern, "
          u"List Length, Bounds, Panel",
     etapes=[u"Tester chaque pièce sur les deux seuils.",
             u"Former les quatre combinaisons de vrai et de faux.",
             u"Compter chaque famille.",
             u"Prendre le plus grand des quatre effectifs."],
     pieges=[u"Ne croiser qu'un critère.",
             u"Rendre le nombre de familles au lieu de l'effectif."],
     var=[u"Faire varier le seuil de longueur et suivre le groupe dominant.",
          u"Chercher les seuils qui équilibrent les quatre familles."],
     gamif=u"G-12 Le memory des composants",
     bareme=u"1 point si l'effectif est exact."),

dict(id=u"IA-29", titre=u"Les GUID qui cassent les définitions",
     them=u"IA3 · Développement de plugins assisté",
     ref=u"REF-128",
     niv=u"Perfectionnement", duree=18, prereq=u"IA-08",
     verdict=u"competence",
     competence=u"Mesurer l'effet d'un GUID régénéré sur le parc de "
                u"définitions existantes.",
     bloom=u"Analyser × conceptuelle",
     contexte=u"Publier la version suivante d'un plugin ne doit pas casser "
              u"les définitions déjà écrites. Un GUID régénéré rend un "
              u"composant introuvable, et la définition s'ouvre avec un trou.",
     obj=u"Mesurer l'effet d'un GUID régénéré sur le parc de définitions "
         u"existantes.",
     enonce=u"Le tableau donne, pour huit composants du plugin, si leur GUID "
            u"a été conservé d'une version à l'autre et combien de "
            u"définitions les emploient. Donnez le nombre de définitions "
            u"cassées par la mise à jour.",
     depart=u"Le tableau des huit composants, de leurs GUID et de leur usage.",
     att=u"16 définitions sont cassées par la mise à jour.",
     erreur=u"Compter les COMPOSANTS dont le GUID a changé — quatre — au lieu "
            u"des définitions qui les emploient. Un composant régénéré casse "
            u"autant de définitions qu'il en sert : le préjudice se mesure "
            u"chez les utilisateurs, pas dans le code.",
     donnees_note=u"Huit composants, quatre GUID régénérés, et des usages de "
                  u"1 à 9 définitions. Les composants les plus employés ne "
                  u"sont pas ceux dont le GUID a changé : le total, 16, ne "
                  u"se déduit ni du nombre de composants ni de l'usage moyen.",
     limite=u"Le compte suppose qu'une définition cassée l'est ENTIÈREMENT. "
            u"En pratique elle s'ouvre, le composant manquant apparaît en "
            u"substitut rouge, et le reste continue de fonctionner — le "
            u"préjudice est réel mais gradué, ce que ce chiffre n'exprime "
            u"pas.",
     mode=u"SingleValue", tol=u"0", nb=7,
     comp=u"Data, Gate Not, Cull Pattern, Mass Addition, Panel",
     etapes=[u"Isoler les composants dont le GUID a changé.",
             u"Récupérer le nombre de définitions correspondantes.",
             u"En faire la somme."],
     pieges=[u"Compter les composants au lieu des définitions.",
             u"Sommer tout le parc sans filtrer."],
     var=[u"Chercher le composant dont la régénération coûte le plus cher.",
          u"Estimer le gain d'une table de correspondance des anciens GUID."],
     gamif=u"G-29 Le défi du jour",
     bareme=u"1 point si le compte est exact."),

dict(id=u"IA-30", titre=u"Ce qu'un appel coûte dans une définition qui recalcule",
     them=u"IA7 · Vérification, licences et limites",
     ref=u"REF-142",
     niv=u"Perfectionnement", duree=15, prereq=u"IA-13",
     verdict=u"competence",
     competence=u"Chiffrer le coût d'un service distant appelé depuis une "
                u"définition qui recalcule à chaque manipulation.",
     bloom=u"Appliquer × procédurale",
     contexte=u"Un composant qui interroge un modèle de langage se paie à "
              u"l'appel. Dans une définition qui recalcule à chaque "
              u"déplacement de curseur, la facture ne suit pas le nombre de "
              u"réponses utiles.",
     obj=u"Chiffrer le coût d'un service distant appelé depuis une définition "
         u"qui recalcule à chaque manipulation.",
     enonce=u"La définition émet trois appels par recalcul, et la séance en "
            u"a compté 240. Chaque appel coûte 0,004 € et prend 1,8 s. "
            u"Donnez le coût de la séance, en euros.",
     depart=u"Le nombre d'appels par recalcul, le nombre de recalculs, le "
            u"prix et la latence unitaires.",
     att=u"2,88 € pour la séance.",
     erreur=u"Compter un appel par recalcul : 0,96 €, trois fois moins. La "
            u"définition en émet trois — un par branche du graphe — et c'est "
            u"le genre de multiplication qu'on ne découvre qu'à la facture.",
     donnees_note=u"720 appels pour une séance de travail ordinaire, et "
                  u"1 296 s d'attente cumulée, soit vingt-deux minutes. Les "
                  u"deux nombres disent la même chose de deux façons : le "
                  u"coût se voit sur la facture, la latence se subit tout de "
                  u"suite.",
     limite=u"Le calcul suppose le prix et la latence CONSTANTS. Les deux "
            u"varient avec la taille de la demande et la charge du service, "
            u"et un modèle plus grand peut coûter dix fois plus pour la même "
            u"question.",
     mode=u"NumericTolerance", tol=u"0.01", nb=5,
     comp=u"Slider, Multiplication, Panel",
     etapes=[u"Multiplier les recalculs par les appels de chacun.",
             u"Multiplier par le prix unitaire."],
     pieges=[u"Oublier les trois appels par recalcul.",
             u"Confondre le coût et la latence."],
     var=[u"Donner l'attente cumulée en minutes.",
          u"Chercher le nombre de recalculs qui tient dans un budget de 1 €."],
     gamif=u"G-03 Contre la montre",
     bareme=u"1 point si le coût est juste au centime."),

dict(id=u"IA-31", titre=u"Ce que l'agent a modifié",
     them=u"IA6 · Agents et protocoles",
     ref=u"REF-136, REF-137, REF-138",
     niv=u"Perfectionnement", duree=16, prereq=u"IA-12",
     verdict=u"competence",
     competence=u"Distinguer, dans le journal d'un agent, les opérations qui "
                u"ont modifié le document de celles qui l'ont seulement lu.",
     bloom=u"Analyser × conceptuelle",
     contexte=u"Avant de laisser un agent travailler sur une définition, on "
              u"veut savoir ce qu'il a touché. Le journal le dit, à "
              u"condition de trier les lectures des écritures.",
     obj=u"Distinguer, dans le journal d'un agent, les opérations qui ont "
         u"modifié le document de celles qui l'ont seulement lu.",
     enonce=u"Le journal donne les vingt-deux opérations menées par l'agent. "
            u"Donnez le nombre d'opérations qui ont MODIFIÉ le document.",
     depart=u"Le journal des vingt-deux opérations.",
     att=u"10 opérations ont modifié le document.",
     erreur=u"Ne compter que les ajouts et les suppressions — cinq. Câbler, "
            u"déplacer et renommer modifient le document tout autant : un "
            u"fil rebranché change le résultat sans que rien n'apparaisse ni "
            u"ne disparaisse, et c'est la modification la plus difficile à "
            u"retrouver après coup.",
     donnees_note=u"Vingt-deux opérations dont douze lectures. Les cinq "
                  u"verbes d'écriture se répartissent en trois familles — "
                  u"création, destruction, altération — et seule la "
                  u"troisième est oubliée par le compte naïf.",
     limite=u"Le journal dit ce que l'agent a FAIT, pas ce qu'il a cassé. "
            u"Dix modifications peuvent être toutes justes, ou une seule "
            u"peut avoir rompu la chaîne : c'est la raison pour laquelle on "
            u"travaille sur une copie et qu'on versionne avant d'agir.",
     mode=u"SingleValue", tol=u"0", nb=7,
     comp=u"Data, Member Index, Larger Than, Cull Pattern, List Length, "
          u"Panel",
     etapes=[u"Poser la liste des verbes d'écriture.",
             u"Pour chaque opération du journal, chercher si son verbe y "
             u"figure.",
             u"Compter les correspondances."],
     pieges=[u"Réduire l'écriture à l'ajout et à la suppression.",
             u"Compter les lectures."],
     var=[u"Donner le nombre d'opérations irréversibles.",
          u"Reconstituer l'état du document après les dix modifications."],
     gamif=u"G-16 La chasse au trésor",
     bareme=u"1 point si le compte est exact."),

dict(id=u"IA-32", titre=u"Ce qu'une demande floue laisse passer",
     them=u"IA1 · Formuler et cadrer une demande",
     ref=u"REF-117, REF-119",
     niv=u"Débutant", duree=15, prereq=u"IA-01",
     verdict=u"competence",
     competence=u"Mesurer l'écart entre plusieurs lectures défendables d'une "
                u"même consigne, pour comprendre ce qu'une spécification "
                u"doit trancher.",
     bloom=u"Analyser × conceptuelle",
     contexte=u"« Compte les grandes valeurs » se lit de quatre façons. "
              u"L'assistant en choisit une, silencieusement, et le résultat "
              u"est juste au regard de sa lecture.",
     obj=u"Mesurer l'écart entre plusieurs lectures défendables d'une même "
         u"consigne, pour comprendre ce qu'une spécification doit trancher.",
     enonce=u"La consigne dit « compte les grandes valeurs » sur les seize "
            u"relevés fournis. Appliquez-lui quatre lectures : strictement "
            u"au-dessus de 500, au moins 500, au-dessus de la moyenne, "
            u"au-dessus de la médiane. Donnez les quatre comptes, dans cet "
            u"ordre.",
     depart=u"Les seize relevés et les quatre lectures à appliquer.",
     att=u"Les quatre comptes, dans l'ordre : 7, 8, 9, 8.",
     erreur=u"Croire que la question du seuil strict est théorique. Un relevé "
            u"vaut EXACTEMENT 500 : c'est lui qui sépare les deux premières "
            u"lectures, et c'est le cas limite qu'une spécification doit "
            u"nommer explicitement.",
     donnees_note=u"Seize relevés de 100 à 999, dont un posé exactement au "
                  u"seuil. La moyenne, 472,81, et la médiane, 491,50, "
                  u"encadrent le seuil de 500 sans coïncider avec lui : les "
                  u"quatre lectures donnent trois comptes différents, et "
                  u"aucune n'est plus légitime que les autres.",
     limite=u"Quatre lectures ne sont pas toutes les lectures. « Grande » "
            u"peut aussi vouloir dire au-dessus du troisième quartile, ou "
            u"au-dessus d'un seuil métier absent des données : l'exercice "
            u"montre le problème, il n'en épuise pas les cas.",
     mode=u"ExactOrderedList", tol=u"0", nb=12,
     comp=u"Data, Larger Than, Average, Sort List, List Item, Cull Pattern, "
          u"List Length, Merge, Panel",
     etapes=[u"Compter les valeurs strictement au-dessus de 500.",
             u"Recommencer avec la comparaison large.",
             u"Calculer la moyenne, puis compter au-dessus.",
             u"Trier pour obtenir la médiane, puis compter au-dessus.",
             u"Assembler les quatre comptes dans l'ordre."],
     pieges=[u"Confondre moyenne et médiane.",
             u"Employer la même comparaison pour les deux premières "
             u"lectures."],
     var=[u"Ajouter un second relevé à 500 et refaire les quatre comptes.",
          u"Rédiger la spécification qui lèverait l'ambiguïté."],
     gamif=u"G-17 Le quiz éclair",
     bareme=u"1 point si les quatre comptes concordent dans l'ordre."),

dict(id=u"IA-33", titre=u"Du texte aux paramètres",
     them=u"IA5 · Modèles de langage et IA générative",
     ref=u"REF-134",
     niv=u"Perfectionnement", duree=18, prereq=u"IA-11",
     verdict=u"competence",
     competence=u"Tirer d'un texte de programme les paramètres qui pilotent "
                u"une définition, en distinguant ce qui est donné de ce qui "
                u"se déduit.",
     bloom=u"Analyser × procédurale",
     contexte=u"Un cahier des charges décrit une verrière en toutes lettres. "
              u"La définition, elle, a besoin d'une largeur de travée et "
              u"d'une hauteur vitrée, qu'aucune phrase ne donne directement.",
     obj=u"Tirer d'un texte de programme les paramètres qui pilotent une "
         u"définition, en distinguant ce qui est donné de ce qui se déduit.",
     enonce=u"L'extrait décrit une verrière de 3 200 mm de large et 2 450 mm "
            u"de haut, à 6 travées égales séparées par des montants de "
            u"60 mm, avec une imposte de 380 mm en partie haute. Donnez la "
            u"largeur d'une travée puis la hauteur vitrée, en millimètres.",
     depart=u"L'extrait de programme, en toutes lettres.",
     att=u"483,3333 mm de largeur de travée, puis 2 070 mm de hauteur vitrée.",
     erreur=u"Diviser la largeur par le nombre de travées : 533,33 mm. Les "
            u"cinq montants intérieurs occupent 300 mm qu'aucune travée ne "
            u"reçoit — la verrière posée sur ce chiffre déborde de 300 mm, "
            u"et l'erreur ne se voit qu'au montage.",
     donnees_note=u"Six travées et cinq montants : c'est l'écart d'une unité "
                  u"qui fait tout le piège, et il est le même que celui des "
                  u"barreaux de garde-corps en B-02. La largeur obtenue "
                  u"n'est pas ronde, ce qui interdit de la deviner.",
     limite=u"Les deux paramètres se déduisent du TEXTE. Ils ne disent pas "
            u"si la verrière est constructible : une travée de 483 mm en "
            u"simple vitrage tient, en double vitrage sur 2 070 mm de haut "
            u"elle demande un calcul de raidissement que le texte ignore.",
     mode=u"NumericTolerance", tol=u"0.0001", nb=8,
     comp=u"Slider, Subtraction, Multiplication, Division, Merge, Panel",
     etapes=[u"Compter les montants : un de moins que les travées.",
             u"Retrancher leur largeur cumulée à la largeur totale.",
             u"Diviser par le nombre de travées.",
             u"Retrancher l'imposte à la hauteur totale."],
     pieges=[u"Compter autant de montants que de travées.",
             u"Diviser avant de retrancher."],
     var=[u"Refaire le calcul pour sept travées.",
          u"Chercher le nombre de travées qui donne une largeur ronde."],
     gamif=u"G-19 Le composant mystère",
     bareme=u"1 point si les deux valeurs sont justes à 0,0001 mm."),

]
