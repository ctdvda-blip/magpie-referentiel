# -*- coding: utf-8 -*-
"""Notions ajoutees pour amener chaque categorie a trois notions au moins.

POURQUOI
--------
Le referentiel comptait 41 categories de 1 a 11 notions, mediane 3. Quatorze
n'en portaient qu'une ou deux — et trois categories entieres du domaine
« Algorithmique avancee » tenaient sur une seule notion chacune. Une categorie
d'une notion n'est pas une categorie : c'est une notion qu'on a rangee seule.

Le plancher retenu est TROIS, la mediane existante. Il ne s'agit pas de gonfler
le referentiel : chaque notion ajoutee comble un manque reel, reperable au fait
qu'elle etait deja supposee par les exercices existants sans jamais avoir ete
ecrite.

CE QUI A GUIDE LE CHOIX
-----------------------
Trois criteres, dans cet ordre.

1. La notion doit MANQUER, pas completer. Test employe : un formateur qui
   couvre la categorie sans elle laisse-t-il un trou que l'atelier revele ?
   « Reperer un objet par ses proprietes » manque a l'organisation du document ;
   « connaitre le nom des calques » n'aurait rien ajoute.

2. Elle doit se traiter par une COMPETENCE mesurable quand c'est possible.
   Trois d'entre elles sont des connaissances assumees et le disent : leur
   ValidationMode est « Conceptuel (QCM) », et l'exercice correspondant est une
   question charniere.

3. Elle doit tenir dans le niveau de sa categorie. Ajouter une notion experte a
   une categorie debutante deplacerait la categorie entiere.

IDENTIFIANTS
------------
Les nouvelles notions prennent REF-143 et suivants. Elles ne s'inserent PAS
dans la numerotation existante : REF-065 doit rester REF-065, sans quoi toutes
les fiches d'exercice deja ecrites designeraient autre chose. Le classeur les
range a leur place par le tri des lignes ; c'est la colonne N° qui porte la
position, l'ID qui porte l'identite.
"""

#: (categorie, notion, description, niveau, validation, type, priorite)
NOTIONS = [

# --- 1 · Organisation du document Rhino -----------------------------------
(u"Organisation du document Rhino",
 u"Sélection par propriétés",
 u"Retrouver des objets sur ce qu'ils SONT — calque, couleur, type, nom — "
 u"plutôt que sur ce qu'on voit à l'écran. Une sélection faite à la souris "
 u"cesse d'être juste dès la livraison suivante ; une sélection faite sur une "
 u"propriété se rejoue.",
 u"Débutant", u"SingleValue", u"Exercice Grasshopper", u"P1"),

# --- 3 · Outils de texte ---------------------------------------------------
(u"Outils de texte",
 u"Nettoyage d'une chaîne",
 u"Retirer les espaces de bord, uniformiser la casse et les séparateurs avant "
 u"toute comparaison. Deux libellés qui désignent la même référence mais ne "
 u"s'écrivent pas pareil ne se regroupent pas, et le regroupement échoue sans "
 u"message.",
 u"Intermédiaire", u"SingleValue", u"Exercice Grasshopper", u"P1"),

# --- 3 · Types et conversion implicite -------------------------------------
(u"Types et conversion implicite",
 u"Texte et nombre",
 u"Ce qui distingue « 12 » de 12, et ce que Grasshopper fait quand il attend "
 u"l'un et reçoit l'autre. Un tri de textes place 10 avant 9 : la conversion "
 u"n'est pas une formalité, elle change le résultat.",
 u"Débutant", u"ExactOrderedList", u"Exercice Grasshopper", u"P1"),

# --- 4 · Plan paramétrique -------------------------------------------------
(u"Plan paramétrique",
 u"Contraintes d'un tracé",
 u"Poser les dimensions qui pilotent un tracé et celles qui s'en déduisent, "
 u"de sorte qu'aucune ne puisse contredire une autre. Un tracé sur-contraint "
 u"ne se recalcule pas ; un tracé sous-contraint se recalcule n'importe "
 u"comment.",
 u"Intermédiaire", u"NumericTolerance", u"Exercice Grasshopper", u"P2"),

# --- 4 · Synthèse géométrie ------------------------------------------------
(u"Synthèse géométrie",
 u"Choisir la représentation",
 u"Décider si une pièce se traite en courbe, en surface, en solide ou en "
 u"maillage — chacune répondant à des questions différentes et coûtant un "
 u"prix différent. Le choix se fait sur ce qu'on veut MESURER, pas sur ce "
 u"qu'on veut voir.",
 u"Perfectionnement", u"SingleValue", u"QCM / question ciblée", u"P2"),

(u"Synthèse géométrie",
 u"Enchaîner les opérations",
 u"Ordonner une suite d'opérations géométriques de sorte que chacune reçoive "
 u"ce dont elle a besoin. Un congé posé avant une booléenne et le même posé "
 u"après ne donnent pas la même pièce.",
 u"Perfectionnement", u"GeometryTolerance", u"Exercice Grasshopper", u"P2"),

# --- 4 · Transformations et réseaux ----------------------------------------
(u"Transformations et réseaux",
 u"Composer des transformations",
 u"Enchaîner rotation, translation et échelle en sachant que l'ordre compte : "
 u"tourner puis déplacer ne place pas la pièce où déplacer puis tourner la "
 u"place. Le repère de chaque opération est ce qui décide.",
 u"Intermédiaire", u"GeometryTolerance", u"Exercice Grasshopper", u"P1"),

# --- 6 · Organisation et performance ---------------------------------------
(u"Organisation et performance",
 u"Mesurer avant d'optimiser",
 u"Relever le temps réellement passé par chaque composant avant de toucher au "
 u"graphe. L'intuition désigne presque toujours le mauvais coupable, et une "
 u"optimisation faite au jugé coûte du temps sans en rendre.",
 u"Perfectionnement", u"SingleValue", u"Exercice Grasshopper", u"P1"),

# --- 7 · Boucles et itération ----------------------------------------------
(u"Boucles et itération",
 u"Critère d'arrêt d'une boucle",
 u"Décider ce qui met fin à l'itération : un écart sous un seuil, un nombre "
 u"maximal de passages, ou les deux. Une boucle sans garde-fou ne s'arrête "
 u"pas quand elle ne converge pas — et rien ne dit qu'elle converge.",
 u"Perfectionnement", u"SingleValue", u"Exercice Grasshopper", u"P1"),

(u"Boucles et itération",
 u"Accumuler un état d'un passage à l'autre",
 u"Transporter une valeur d'une itération à la suivante — un cumul, un "
 u"meilleur résultat, une liste qui s'allonge. C'est ce qui distingue une "
 u"boucle d'une simple répétition, et ce que le graphe seul ne sait pas "
 u"faire.",
 u"Perfectionnement", u"NumericTolerance", u"Exercice Grasshopper", u"P2"),

# --- 7 · Design génératif --------------------------------------------------
(u"Design génératif",
 u"Formuler un objectif et ses contraintes",
 u"Traduire une intention de projet en une grandeur à minimiser ou maximiser, "
 u"et en contraintes qui bornent l'espace des solutions. Un objectif mal posé "
 u"produit une solution optimale à un problème que personne n'avait.",
 u"Perfectionnement", u"SingleValue", u"QCM / question ciblée", u"P1"),

(u"Design génératif",
 u"Lire un front de solutions",
 u"Comparer des solutions qui ne se classent pas entre elles — meilleures sur "
 u"un critère, moins bonnes sur un autre — et choisir en connaissance de "
 u"cause. L'optimisation ne décide pas à la place du projeteur : elle lui "
 u"montre le compromis.",
 u"Perfectionnement", u"SingleValue", u"Exercice Grasshopper", u"P2"),

# --- 7 · Simulation physique -----------------------------------------------
(u"Simulation physique",
 u"Convergence et stabilité d'une relaxation",
 u"Reconnaître une simulation qui s'est stabilisée d'une qui oscille encore, "
 u"et savoir que l'aperçu ne le dit pas. Une forme qui paraît figée à l'écran "
 u"peut encore bouger sous la tolérance d'affichage.",
 u"Perfectionnement", u"NumericTolerance", u"Exercice Grasshopper", u"P1"),

(u"Simulation physique",
 u"Ce qu'une simulation ne dit pas",
 u"Situer ce qu'un moteur de relaxation calcule — une forme d'équilibre — et "
 u"ce qu'il ne calcule pas : ni contraintes admissibles, ni sections, ni "
 u"dimensionnement. Confondre les deux fait prendre une maquette pour une "
 u"note de calcul.",
 u"Perfectionnement", u"Conceptuel (QCM)", u"QCM / question ciblée", u"P1"),

# --- 9 · Interfaces utilisateur --------------------------------------------
(u"Interfaces utilisateur",
 u"Bornes et valeurs par défaut",
 u"Donner à chaque paramètre exposé une plage admissible et une valeur de "
 u"départ qui tienne. Un curseur sans bornes laisse produire une pièce "
 u"infabricable, et l'interface n'aura rien signalé.",
 u"Perfectionnement", u"SingleValue", u"Exercice Grasshopper", u"P1"),

# --- 9 · Interopérabilité --------------------------------------------------
(u"Interopérabilité",
 u"Ce qu'un format d'échange transporte",
 u"Savoir, pour chaque format, ce qui survit au passage : géométrie, unités, "
 u"calques, matières, métadonnées. Un échange réussi se juge sur ce qui "
 u"arrive, pas sur le fait que le fichier s'ouvre.",
 u"Perfectionnement", u"SingleValue", u"Exercice Grasshopper", u"P1"),

# --- 10 · Déroulé et mise à plat -------------------------------------------
(u"Déroulé et mise à plat",
 u"Surfaces développables ou non",
 u"Reconnaître ce qui se met à plat sans déformer — cylindre, cône — de ce "
 u"qui ne s'y met pas — sphère, surface à double courbure. Dans le second "
 u"cas, tout déroulé est une approximation, et son écart se chiffre.",
 u"Perfectionnement", u"Conceptuel (QCM)", u"QCM / question ciblée", u"P1"),

# --- 10 · Imbrication ------------------------------------------------------
(u"Imbrication",
 u"Trait de scie et chutes",
 u"Tenir compte de la largeur d'outil entre deux pièces et du bord de "
 u"panneau inutilisable. Une imbrication calculée sans trait de scie tombe "
 u"juste sur le plan et ne tombe pas juste sur la machine.",
 u"Perfectionnement", u"NumericTolerance", u"Exercice Grasshopper", u"P1"),

]

#: le domaine de chaque categorie, pour retrouver sa place au classement
DOMAINES = {
    u"Organisation du document Rhino": u"1 – Socle Rhino (prérequis)",
    u"Outils de texte": u"3 – Données et logique",
    u"Types et conversion implicite": u"3 – Données et logique",
    u"Plan paramétrique": u"4 – Géométrie paramétrique",
    u"Synthèse géométrie": u"4 – Géométrie paramétrique",
    u"Transformations et réseaux": u"4 – Géométrie paramétrique",
    u"Organisation et performance": u"6 – Méthode, performance et évènements",
    u"Boucles et itération": u"7 – Algorithmique avancée",
    u"Design génératif": u"7 – Algorithmique avancée",
    u"Simulation physique": u"7 – Algorithmique avancée",
    u"Interfaces utilisateur": u"9 – Interfaces, web et interopérabilité",
    u"Interopérabilité": u"9 – Interfaces, web et interopérabilité",
    u"Déroulé et mise à plat": u"10 – Aide à la fabrication",
    u"Imbrication": u"10 – Aide à la fabrication",
}


def lignes_referentiel(depart):
    """Rend les notions au format du referentiel, numerotees a partir de
    `depart`. Meme contrat que `domaine_ia.lignes_referentiel`."""
    out = []
    for i, (cat, notion, desc, niv, val, typ, prio) in enumerate(NOTIONS):
        n = depart + i
        out.append([
            n,                              # N°
            u"REF-%03d" % n,                # ID
            DOMAINES[cat],                  # Domaine
            cat,                            # Catégorie
            notion,                         # Notion
            desc,                           # Description
            niv,                            # Niveau
            val,                            # ValidationMode suggéré
            typ,                            # Type d'exercice
            prio,                           # Priorité de production
            u"",                            # Nb exercices Magpie prévus
            u"",                            # À réaliser par
            u"",                            # Statut
            u"",                            # Lien
            u"",                            # Notes
        ])
    return out


if __name__ == "__main__":
    import collections
    import io as _io
    import sys as _sys
    _sys.stdout = _io.TextIOWrapper(_sys.stdout.buffer, encoding="utf-8",
                                    errors="replace")
    c = collections.Counter(n[0] for n in NOTIONS)
    print(u"%d notions, %d catégories complétées" % (len(NOTIONS), len(c)))
    for cat, k in sorted(c.items()):
        print(u"   %-40s +%d" % (cat, k))
