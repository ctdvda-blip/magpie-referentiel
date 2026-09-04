# REPRISE DE SESSION

## Projet
MAGPIE — outil d'exercices Grasshopper autocorrigés pour Rhino 8 (éditeur RhinoForYou, auteur du prototype : Jérémy CAROLUS).
Contribution de Charles THIERRY DE VILLE D'AVRAY, enveloppe initiale de 10 h décidée en réunion du 11/08/2026.

## Objectif global
Transformer la liste de notions Grasshopper en une bibliothèque d'exercices de qualité, alignée sur les programmes de formation RhinoForYou, testable auprès de profils débutants et intermédiaires.

## Répertoire de travail
`C:\Users\charl\.claude\projects\MAGPIE`

## Branche Git
`main`, dans le dépôt **propre au projet** créé le 02/09/2026 à la racine de
`MAGPIE` — 4,4 Mo, arbre de travail propre.

Il suit ce qui ne se régénère pas : les 84 modules de la chaîne, la
documentation, les 458 fiches Markdown, les 222 descripteurs et les 444
définitions `.gh`. Il ignore les 250 Mo de Word, PDF et images de canevas,
tous refabriqués par `finaliser.py`.

**Ne pas confondre avec le dépôt englobant** (`C:\Users\charl`, branche
`feat/android-app`), qui voit toujours `MAGPIE/` comme un simple dossier non
suivi — la création du dépôt imbriqué n'a rien changé pour lui, et rien ne
doit y être commité sans arbitrage.

Deux pièges vérifiés au clonage :

- **la limite de chemin de Windows** : les lots A et IA nomment leurs dossiers
  par le titre complet de l'exercice, et un clone posé trop bas échoue avec
  « Filename too long ». `core.longpaths` est activé dans le dépôt ; il doit
  l'être aussi côté client, ou le clone doit rester près de la racine ;
- **la conversion de fin de ligne** : `.gitattributes` déclare `.gh`, `.3dm`,
  `.xlsx`, `.docx` et les images comme binaires. Un clone de contrôle a
  confirmé que les définitions en ressortent au bit près.

## Version actuelle
**`v0.5-260902` – Ind. C**, le 02/09/2026. Le fichier `VERSION`, à la racine,
porte le numéro logique : `0.5`.

La montée se propage par **cinq constantes** — `gen_application.py`,
`gen_cdc.py`, `gen_fiches.py`, `gen_fiches_docx.py`, `GH/gh_engine.py` — plus
le fichier `VERSION`. **Ne pas y ajouter `skill_a.py`** : son marqueur est
celui du module, pas celui du produit, et le toucher a invalidé les 98
définitions du lot A une fois déjà.

Les descripteurs `.json` déjà produits sont repris par `propager_version.py`,
qui réécrit le seul champ `version` : les propager par une reconstruction
réattribuerait les GUID des 444 définitions, et republierait une centaine de
mégaoctets pour un champ de texte. Le bandeau des `.gh` porte donc la version
à laquelle chacun a été construit, ce qui est délibéré.

Les livrables de la v0.4 sont archivés dans `Anciens fichiers0.4-260901\`.

- Référentiel de notions : **Ind. C – 01-09-2026** (unifié). Les 160 notions
  n'ont pas bougé : c'est la bibliothèque d'exercices qui a grandi, d'où un
  indice de référentiel inchangé et une version de produit qui monte.
  L'indice A est archivé dans `Anciens fichiers\`.
- Cahier des charges des exercices : **v0.5-260902 – Ind. C**
- Application HTML de consultation : **v0.5-260902 – Ind. C**
  (`MAGPIE - Application.html`, à la racine — doit rester à côté du dossier `EXERCICES`,
  tous les liens y étant relatifs). Accueil à trois niveaux : domaines → catégories →
  notions et exercices rattachés.

## Indice B du référentiel — ce qui change
Fusion complète : plus aucune trace de la partition entre les 19 notions du tableau
d'origine et les 97 issues des programmes.
- onglet `Fondamentaux V1` supprimé ;
- colonnes supprimées : Origine / couverture, D3, P3, P6, P6b, P6A, RG8, Nb prog.,
  Ordre V1, Réf. croisée — il reste **15 colonnes** ;
- identifiants renumérotés **REF-001 à REF-116**, sans préfixe de provenance ;
- colonne Notes purgée de toute mention d'origine, l'avertissement factuel sur la
  correspondance par défaut étant conservé et reformulé ;
- onglet Synthèse recalculé, sans le bloc d'écarts V1 / programmes.
Table de correspondance ancien → nouveau : `EXPORTS\Correspondance_identifiants_IndA_vers_IndB.csv`.

**Propagation faite le 26/08/2026.** Les nouveaux identifiants ont été portés partout :
- `exos_a.py`, `exos_b.py`, `exos_g.py` : **236 références remplacées**, aucun identifiant
  non reconnu. Les originaux sont dans `Anciens fichiers\Generateurs_identifiants_IndA\`.
- Toute la chaîne a été régénérée : cahier des charges, 98 `.gh`, 196 illustrations,
  98 fiches Markdown, 98 fiches Word, 49 PDF, 49 descripteurs JSON, application HTML.
- Contrôle : **0 ancien identifiant** subsistant dans les livrables ; 530 occurrences
  `REF-` dans le cahier des charges, 180 dans les fiches et descripteurs, 60 dans les
  bandeaux des `.gh`.
- Versions portées à **v0.2-260826 / Ind. B** pour le cahier des charges, les fiches et
  les définitions Grasshopper.

## Refonte pédagogique du 26/08/2026 — skill de conception

Le lot A a été repris au regard de la skill **magpie-conception-exercices v2.3**
(`SKILL.md`, à la racine). Un audit mécanisé chiffre l'écart avant / après :

| | Avant | Après |
|---|---|---|
| Écarts relevés | 124 | 7 |
| Exercices à refondre | 18 | 7 |

Les 7 écarts résiduels sont tous du même type — solution de référence trop
courte (§1 : « un seul composant suffit ») — et sont **assumés et documentés** :
chacun porte désormais une *note au formateur* expliquant pourquoi il devrait,
à terme, être absorbé dans un exercice composite ou posé en question charnière.
Ils concernent A-09, A-14, A-16, A-17, A-20, A-22 et A-23.

### Architecture retenue

`exos_a.py` n'est **pas** modifié. Une couche se superpose à lui :

```text
exos_a.py          contenu d'origine, intact, traçable
  └─ skill_a.py    couche pédagogique + correctifs checker + réponses relevées
       └─ fusionner(exo)  utilisé par TOUS les générateurs
GH/recettes_skill.py       correctifs des recettes de construction .gh
```

### Ce que la skill a changé sur le fond

1. **7 items requalifiés en connaissance** — A-03, A-05, A-06, A-07, A-24, A-26,
   A-29. Ils demandaient de *constater un comportement* : la réponse s'obtenait
   en sachant, pas en construisant. Ils ne sont plus notés et portent une
   **question charnière** dont chaque mauvaise réponse est diagnostique. Les
   `.gh` sont conservés comme support de démonstration.
2. **Aucun nom de composant dans les consignes** (§3). La liste des composants
   a quitté la fiche apprenant et ne figure plus que côté corrigé.
3. **Un contexte métier en une phrase** pour les 49 items (§4), varié entre
   exercices : réception de lot, calepinage de bardage, débit d'atelier,
   implantation topographique, haubanage, platine d'assemblage…
4. **10 jeux de données refondus** (§5) : listes de 24 à 36 valeurs, non
   ordonnées, non devinables, à la place des listes de 5 à 20 lisibles à l'œil.
   Source unique dans `skill_a.py`, consommée à la fois par les `.gh` et par
   les fiches — elles ne peuvent plus diverger.
5. **Une erreur attendue par exercice** (§6), choisie pour être *diagnostique*.
6. **Contraintes du checker respectées** : A-13 et A-17 renvoyaient du texte,
   A-15 et A-30 des booléens — le checker n'accepte que des nombres. Ramenés à
   une réponse numérique sans perdre la compétence visée. A-27 et A-28 sont
   déclarés **hors correction automatique** (le livrable EST un texte) plutôt
   que tordus pour entrer dans l'outil.

### Deux défauts de fond trouvés à cette occasion

- **A-30** : les bornes étaient annoncées incluses mais le corrigé employait des
  comparaisons strictes → 14 au lieu de 16. Corrigé en câblant les sorties
  « ou égal ». Le jeu de données contient maintenant une valeur exactement sur
  chaque borne, sans quoi les deux montages seraient indiscernables.
- **A-11** : la réponse ne portait qu'une valeur sur les deux demandées, le
  checker comparant une liste unique. Les deux longueurs sont désormais réunies.

### Contrôles automatiques ajoutés

| Script | Rôle |
|---|---|
| `Generateurs/audit_skill.py` | audit des 49 exercices ; `--fusion` audite la version refondue |
| `Generateurs/controle_reponses.py` | recalcule les réponses attendues et échoue en cas d'écart |
| `GH/recette_2_valeurs.py` | rebranché sur `skill_a` ; bascule l'interrupteur et lit `REPONSE_CORRIGE` |

## Domaine 11 — IA, et renumérotation des domaines (27/08/2026)

### Renumérotation
Les domaines commencent désormais à **1** et non à 0 : un domaine « 0 » se lit
comme un hors-série alors que le socle Rhino est bien la première étape du
parcours. L'ancien 0 devient 1, l'ancien 9 devient 10, et le nouveau domaine IA
prend le 11. La table `RENUM` de `build_fusion.py` porte la correspondance.

**Les identifiants `REF-` n'ont pas bougé** : seuls les libellés de domaine
changent, la traçabilité des 116 notions d'origine est donc intacte, et aucune
fiche d'exercice n'a eu à être retouchée.

### Domaine 11 — IA et assistance générative
Nouveau module `Documentation/Generateurs/domaine_ia.py`, qui porte à la fois
les notions et les exercices — ces derniers sont rédigés **directement** selon
la skill, sans passer par une couche de correction comme le lot A.

**26 notions**, `REF-117` à `REF-142`, en 7 sous-catégories :

| Sous-catégorie | Notions |
|---|---|
| Formuler et cadrer une demande | 3 |
| Composants scriptés assistés (C#, Python 3, VB.NET) | 5 |
| Développement de plugins assisté (vibe coding, agents de code) | 4 |
| Apprentissage automatique | 4 |
| Modèles de langage et IA générative | 3 |
| Agents et protocoles (MCP) | 3 |
| Vérification, licences et limites | 4 |

**14 exercices**, `IA-01` à `IA-14`, dont 2 requalifiés d'emblée en question
charnière (IA-02 contexte technique, IA-08 stabilité des GUID, IA-13
confidentialité).

### Un parti pris de validation, assumé
Le checker Magpie ne compare que des nombres. Une partie de ce domaine a pour
livrable du code, un plugin ou une conversation. Plutôt que de tordre ces
exercices pour les faire entrer dans l'outil, ils sont **déclarés « Visuel » et
le disent explicitement** (IA-07, plugin .gha). Partout où c'était possible sans
dénaturer la tâche, l'exercice demande en revanche un **résultat numérique
produit par le code que l'IA a aidé à écrire** : la compétence est bien « faire
produire un composant juste », et elle se vérifie à sa sortie.

### Livrables du lot IA — produits
**13 exercices sur 14 ont leur définition Grasshopper**, construites par le même
moteur et le même pont Rhino que le lot A :

```text
Documentation/Generateurs/GH/recipes_ia.py     recettes des 13 definitions
Documentation/Generateurs/GH/build_lot_ia.py   lanceur, a executer dans Rhino
EXERCICES/LOT IA - IA et assistance generative/
```

**IA-07 n'a volontairement pas de définition** : son livrable est un plugin
`.gha` compilé, il n'y a rien à monter dans Grasshopper, et fabriquer un fichier
vide pour la forme serait trompeur. Le contrôle de fraîcheur connaît cette
exception et ne la signale pas comme un manque.

#### Ce que contient la zone corrigé de ce lot
Une partie du lot se joue **hors** de Grasshopper : un assistant écrit le code,
un agent conduit un projet, un modèle lit un texte. La définition ne peut donc
pas contenir la solution. Ce que la zone corrigé apporte, c'est le **contrôle
indépendant** : le même résultat obtenu avec des composants natifs, sans
assistance. C'est exactement ce que les énoncés demandent — vérifier ce que
l'outil renvoie par un moyen qui n'emprunte pas le même chemin. Le corrigé n'est
pas la réponse à recopier, c'est l'étalon.

#### Valeurs relevées dans Rhino, pas déduites
| | | | | |
|---|---|---|---|---|
| IA-01 → 10 | IA-02 → 0 | IA-03 → 48 | IA-04 → 58,03 | IA-05 → 9 |
| IA-06 → sommes cumulées | IA-08 → 1 | IA-09 → 379,6 | IA-10 → 9 | IA-11 → 15 |
| IA-12 → 7 110,8 | IA-13 → 2 | IA-14 → 40 800 000 mm³ | | |

Deux réponses que j'avais écrites de tête étaient fausses — IA-01 donnait 10 et
non 5, IA-05 donnait 9 et non 8 — et le calcul les a corrigées avant livraison.

Les fiches Markdown et Word, les illustrations et les vignettes sont produites
pour les 14 exercices. L'application sonde le disque et n'affiche que les
fichiers réellement présents : aucun lien mort.

### Chaîne étendue aux deux lots
`gen_fiches.py`, `gen_fiches_docx.py`, `gen_vignettes.py`, `gen_pdf.py`,
`gen_images.py` et `verifier_fraicheur.py` parcourent désormais les deux
dossiers de lot. L'application résout les chemins **par exercice** : le lot A et
le lot IA ne vivent pas dans le même dossier, et supposer une racine unique
donnait des liens morts.

### Nouvelles colonnes du référentiel
`Nature pédagogique` et `Exercices Magpie`, alimentées par les exercices
réellement produits — jamais devinées d'après le libellé de la notion.

## Couverture complète du référentiel (28/08/2026)

Le référentiel passe de **44 % à 100 %** de couverture : 142 notions, aucune
catégorie sans exercice. `Documentation/Generateurs/couverture.py` le mesure et
produit `COUVERTURE.md`.

### Onze lots, 99 exercices

| Lot | Domaine | Items | dont charnières |
|---|---|---:|---:|
| A | Découverte des composants natifs | 49 | 7 |
| RH | Socle Rhino | 10 | 4 |
| PL | Écosystème de plugins | 4 | 3 |
| GP | Géométrie paramétrique appliquée | 4 | 1 |
| DV | Développement, scripting et API | 4 | 2 |
| QT | Quantitatifs, chiffrage et export | 3 | 0 |
| MP | Méthode, performance et évènements | 3 | 1 |
| AV | Algorithmique avancée | 3 | 0 |
| WB | Interfaces, web et interopérabilité | 3 | 1 |
| FA | Aide à la fabrication | 2 | 0 |
| IA | IA et assistance générative | 14 | 3 |

**77 exercices notés, 22 questions charnières.** La proportion de charnières est
volontairement élevée dans PL et DV : installer un plugin ou savoir ce qu'est
Rhino.Compute sont des connaissances, et la skill interdit de les monter en
exercice.

### Le socle Rhino, cas particulier
Ces notions décrivent des gestes **Rhino**, que le checker ne sait pas comparer.
Réponse retenue : ce qui produit une géométrie se valide **en la référençant
dans Grasshopper et en la mesurant** — c'est déjà le principe d'A-04. Le reste
devient question charnière.

---

## `lots.py` — registre unique

Toute la chaîne s'y adresse : fiches, cahier des charges, application, classeur,
couverture, contrôle de fraîcheur. Un lot ajouté apparaît partout sans autre
intervention. Auparavant chaque générateur importait les lots à sa façon, et il
a fallu les rattraper un par un.

---

## Trois défauts de conception corrigés

### 1. Les fiches apprenant donnaient la réponse
**22 fiches sur 77** annonçaient la valeur — « 11, le nombre de traverses hors
tolérance » — dans la rubrique remise à l'apprenant. `attendus_sujet.py` sépare
les deux lectures : la **nature** du résultat dans le sujet, identique sur les
deux fiches ; la **valeur** dans le corrigé seulement.

### 2. La bonne réponse était toujours en b
**18 charnières sur 22.** Un apprenant cochant systématiquement b obtenait 82 %
— variance non pertinente au construit. `equilibrer_qcm.py` permute les
propositions à l'exécution et **réécrit les renvois de lettres** du commentaire
diagnostique, sans quoi celui-ci désignerait les mauvaises options.

Quatre charnières sont figées : A-26, IA-02, IA-08 et IA-13 portent déjà un menu
déroulant dans leur `.gh`, dont l'indice est fixé. Répartition finale :
a=7, b=6, c=3, d=6.

Les menus des lots récents, eux, sont **dérivés de la fiche** : ils ne peuvent
plus diverger.

### 3. Deux réponses non numériques
A-19 renvoyait un chemin de branche (texte), A-43 un booléen — que le checker
refuse. L'audit ne contrôlait que les couples mode/tolérance, pas la nature de
la réponse. Il interroge désormais **le type déclaré du paramètre REPONSE dans
les recettes**, source qui fait autorité et ne produit pas les faux positifs
d'une lecture du texte.

---

## Définitions Grasshopper

**93 exercices sur 99** ont leur `.gh` : les 49 du lot A, les 13 du lot IA, et
31 des nouveaux lots. Les six restants sont exactement les six exercices dont
le mode de validation est **Visuel** : leur livrable est un plugin, un site ou
une définition remaniée par l'apprenant, jugés sur grille. Tout ce que le
correcteur automatique peut noter a désormais sa définition.

### Les exercices à géométrie — un principe différent
RH-02, RH-03, RH-05, RH-08, RH-09, GP-03 et FA-02 demandent de modéliser dans
**Rhino**. La définition n'a donc rien à construire : elle **mesure**.

  - **Sujet** : un paramètre de référence vide, la chaîne de mesure, `REPONSE`.
    Tant que l'apprenant n'a rien modélisé, rien ne sort — c'est le principe.
  - **Corrigé** : la géométrie de référence internalisée et la même chaîne, donc
    la valeur attendue. C'est l'étalon, pas la solution à recopier.

Le filtre de calque a été écarté au profit d'un paramètre de référence : le
filtre se règle dans l'interface et **ne se transporte pas dans le fichier
enregistré**. La fiche demande à l'apprenant de le poser — c'est justement la
compétence évaluée par RH-02.

### Deux erreurs que seul Rhino a révélées
- **RH-08** ne rendait rien. Sur cinq combinaisons de faces à retirer du
  caisson, **seule la paire [4, 5]** laisse des ouvertures que
  `CapPlanarHoles` sait refermer ; [0,1], [2,3] et [3,5] rendent un brep non
  solide, volume nul. Non déductible — il fallait l'essayer.
- **RH-09** donnait 1 au lieu de 0,57 : `Deconstruct Box` rend des
  **intervalles**, pas des longueurs. Le corrigé les décompose désormais.

### AV-01 : l'étalon plutôt que la reproduction
L'exercice se monte avec un plugin de boucle, mais son résultat se calcule sans
boucle — log₂ du rapport, arrondi au supérieur. Le corrigé porte ce calcul
direct, et y gagne un enseignement : savoir qu'un calcul direct existe évite de
faire tourner une boucle pour rien.

### AV-02, RH-04 et DV-02 : les trois dernières mesurables
- **RH-04** monte la ligne au sol du bardage de 2 800 mm **à la verticale**,
  et rend 31,24 m². Le piège est l'extrusion suivant la normale : sur un
  tracé dont la courbure varie, elle donne une nappe voisine à l'œil et
  fausse au métré.
- **AV-02** suit AV-01 : le sujet demande une relaxation, l'étalon trace la
  **chaînette** directement — `Catenary` existe en natif. Flèche 1 592,03 mm,
  contre 1 592,63 mm pour la chaînette théorique : le composant rend une
  polyligne, dont le sommet bas ne tombe pas exactement au point bas. L'écart
  de 0,6 mm tient largement dans la tolérance de 5 mm.
- **DV-02** échantillonne la courbe et cumule les portions dont le rayon
  descend sous 250 mm : **105,8 mm** sur 5 988 mm de développé.

  **L'erreur que j'ai faite en calibrant DV-02, et qui ne se voit pas.**
  Ma première mesure donnait 406 mm — quatre fois trop. J'échantillonnais à
  pas de **paramètre** constant ; `Divide Curve` échantillonne à pas de
  **longueur d'arc** constante. Les paramètres d'une NURBS se resserrent dans
  les courbes : la zone cintrée, qui est précisément l'endroit où ils se
  resserrent, se retrouvait comptée quatre fois. Les deux valeurs sont
  également stables et convergent proprement, chacune vers la sienne — rien
  dans le résultat ne signale l'erreur. Seule la confrontation à la chaîne
  Grasshopper l'a montrée. Les textes de l'exercice ont été repris en
  conséquence, et la tolérance portée de 1 mm à 5 mm : elle sanctionne la
  détection de la zone, non la finesse du pas, qui ne peut pas mesurer plus
  fin que lui-même.

### Restent 6 exercices sans définition, et ils n'en veulent pas
IA-07, PL-03, MP-01, DV-04, WB-01, WB-02. Livrables : un plugin compilé, des
plugins installés et jugés, une définition rendue reprenable, un plugin plus
sa commande Rhino, une définition interfacée, un configurateur en ligne.
Aucun ne se note par un nombre ; tous portent déjà une grille. Leur fournir
un `.gh` reviendrait à livrer le travail demandé.

### Un comportement non expliqué
GP-02 rendait 1,996 m³ au lieu de 6,653. `Mass Addition` ne sommait que huit
des quinze valeurs de son entrée, de façon reproductible, alors que le même
composant fonctionne sur vingt valeurs en QT-01 et MP-02. Contourné par la
formule de la série arithmétique — n(n+1)/2 — qui supprime la liste. **La cause
reste inconnue.**

---

## Conversion PDF — le gel COM, et sa cause enfin trouvée (01/09/2026)

Un appel COM qui gèle ne lève aucune exception : il ne rend jamais la main, et
aucune protection interne n'est possible. `gen_pdf.py` note donc le document en
cours dans un témoin ; si l'exécution suivante trouve ce témoin, elle écarte le
document fautif et poursuit. La conversion est en outre **reprenable** : elle
saute ce qui est déjà à jour, donc chaque relance progresse.

C'est ce mécanisme qui avait identifié A-13, puis A-38.

### La cause : Word tient une liste noire, indexée par chemin
Pendant trois sessions j'ai cherché dans le contenu : la fiche sujet passait en
trois secondes, la fiche complète gelait ; structure, taille et images étaient
comparables à celles des voisines qui passaient. J'avais conclu au bloc corrigé.
**C'était faux.**

Un dernier essai a montré que Word gelait sur `Documents.Open` — donc **avant**
toute conversion. Et que le même fichier, copié dans un dossier temporaire,
s'ouvrait en 0,4 seconde. Le document n'y était pour rien : c'est le CHEMIN qui
était refusé.

```
HKCU\Software\Microsoft\Office.0\Word\Resiliency\DisabledItems
```

Word y inscrit tout document qui l'a fait planter ou geler une fois, et ne l'en
retire jamais. Il refuse ensuite de l'ouvrir — par une boîte de dialogue, qui
avec `Visible = False` n'a nulle part où s'afficher : l'appel ne revient pas.
Le premier gel, quelle qu'en ait été la cause, condamnait donc définitivement le
document **à sa place**. Les deux valeurs de la clé nommaient très exactement
`a-13_fiche.docx` et `a-38_fiche.docx`.

### Ce qui a été fait
`gen_pdf.py` ne les abandonne plus : il les reprend en fin de série depuis une
**copie temporaire**, et ramène le PDF à sa place (`pdf_un.py`, fonction
`convertir_par_copie`). Les deux PDF sont produits et publiés.

Vider la liste demanderait de toucher au registre de l'utilisateur, ce que la
chaîne ne fait pas. Charles peut le faire lui-même : **Word > Fichier >
Options > Compléments > Gérer : Éléments désactivés**.

## Publication — `publier.py` et la dérive du dépôt (01/09/2026)

La copie de publication était montée à la main. Elle a maintenant son script,
`Documentation\Generateurs\publier.py`, qui aplatit les noms de dossiers,
recopie les annexes et régénère l'index avec `--plat --livrables --protege`.

Il fallait surtout arrêter une dérive : **une republication complète ajoutait
une centaine de mégaoctets à l'historique Git** pour trois exercices modifiés.
Trois causes, toutes réglées.

1. **Les `.gh` ne sont pas déterministes** : Grasshopper réattribue les GUID à
   chaque écriture. Deux constructions du même exercice donnent deux fichiers
   différents.
2. **Les `.docx` et les `.pdf` non plus** : python-docx et Word horodatent
   l'intérieur du fichier.
3. **Les `.json` l'étaient encore moins**, et pour rien : `json.dumps` sans
   `sort_keys` rend les clefs dans un ordre qui varie d'une exécution à
   l'autre. Les 93 descripteurs différaient à chaque reconstruction sans qu'un
   caractère de contenu ait bougé. Corrigé dans les trois constructeurs, et
   `normaliser_json.py` a remis les fichiers existants en forme.

`publier.py` calcule donc une **empreinte de contenu logique** par exercice —
fiches Markdown, descripteur relu clefs triées, inventaire des illustrations —
et ne recopie les fichiers volatils que si elle a changé. La dernière
publication est passée de **416 fichiers modifiés à 214** : 26 `.docx` et
14 `.pdf`, ceux des treize exercices réellement touchés, au lieu de 198 et 99.
Les 93 `.json` du commit sont le tri unique des clefs.

L'inventaire des illustrations compte dans l'empreinte pour une raison précise :
un exercice qui reçoit sa définition reçoit ses canvas **sans que sa fiche
Markdown change d'un caractère**. La fiche Word, elle, les incorpore. Sans cette
ligne, RH-04 et AV-02 seraient restés publiés dans leur version sans images —
l'erreur avait déjà été commise, elle est maintenant impossible.

`verifier_liens.py` relit l'objet `dispo` de la page publiée et confronte chaque
téléchargement promis au disque : **576 promis, 0 absent**.

## État actuel

**Quatorze lots, 253 exercices, 160 notions couvertes à 100 %.**
246 exercices ont leur définition Grasshopper ; les sept autres se notent
sur grille. 1 497 téléchargements proposés par le site, aucun absent.

**Plus aucune catégorie n'est au plancher** : la moins servie compte 1,25
exercice par notion, contre 1,00 avant la vague 4.
Tout est publié et poussé sur `ctdvda-blip/magpie-referentiel`.

**Les quatorze lots du cahier des charges sont produits.** Il n'en reste
aucun à écrire.

**Référentiel Ind. C** : aucune catégorie ne porte moins de trois notions,
aucune n'a moins d'exercices qu'elle n'a de notions.

### L'équilibrage (01/09/2026) — deux vagues, cinquante exercices
Le référentiel comptait 41 catégories de 1 à 9 exercices, médiane 2. Dix
n'en avaient qu'un pour deux ou trois notions.

**Les deux équilibres demandés étaient incompatibles** : les domaines n'ont
pas le même nombre de catégories, de 2 à 7. Équilibrer les catégories
déséquilibre les domaines, et réciproquement. Cible retenue avec Charles :
**proportionnelle au nombre de notions** — une catégorie de trois notions
mérite trois exercices.

| | Vague 1 | Vague 2 |
|---|---|---|
| Exercices | 16 | 34 |
| Catégories servies | 10 | 13 |
| Compétences / charnières / grille | 11 / 4 / 1 | 30 / 4 / 0 |

**Cible atteinte : zéro catégorie en déficit.** Médiane par catégorie :
3 contre 2. Le socle Rhino passe de 10 à 22 exercices, l'écosystème de
plugins de 4 à 12.

Les 41 réponses numériques sont recalculées depuis leurs données par
`verifier_vague1.py` et `verifier_vague2.py`, puis relevées dans
Grasshopper. Les deux concordent. Ces scripts ont attrapé deux défauts que
la relecture n'avait pas vus — un compte de 9 pour une donnée de 10, et une
comparaison stricte là où une version minimale est un plancher.

| Livrable | État |
|---|---|
| Définitions `.gh` | 320 fichiers, 160 exercices — les 7 sans définition se notent sur grille |
| Fiches Markdown | 334 (sujet seul et sujet + corrigé) |
| Fiches Word | 334 |
| Fiches PDF | 167, **A-13 et A-38 comprises** |
| Illustrations | 320 canvas + vignettes web |
| Classeur | `Fondamentaux Grasshopper - IndC - 01-09-2026.xlsx` |
| Application | `MAGPIE - Application.html`, 651 Ko |
| Publication | <https://ctdvda-blip.github.io/magpie-referentiel/> — 981 téléchargements, 0 lien mort |

Contrôles au vert : `verifier_fraicheur.py` (tous les livrables à jour),
`couverture.py` (142/142), `recette_6_tous_lots.py` (93 exercices : fichiers
lisibles, sujets étanches, corrigés masqués, `REPONSE_CORRIGE` alimentée, aucun
avertissement inattendu), **`recette_7_valeurs.py` (93 valeurs figées puis
recomparées, conformes)**, `verifier_liens.py` (576/576).

### `recette_7_valeurs.py` — la non-régression qui manquait
La recette 6 vérifie qu'un corrigé produit *quelque chose*, pas qu'il produit
toujours **le même** chose. Une recette de construction se modifie, et la valeur
attendue par le correcteur bouge sans que rien ne le signale : c'est ce qui
était arrivé à RH-09 (1 au lieu de 0,57). Les 93 valeurs sont figées dans
`GH/valeurs_attendues.json` et recomparées à 1e-6 près en relatif.

Refiger est un geste délibéré : `--figer`. Si cela devient une habitude, la
recette ne sert plus à rien.

Piège rencontré : `str()` d'une géométrie RhinoCommon contient son **adresse
mémoire**, qui change à chaque ouverture — 14 faux écarts au premier essai. Les
18 exercices qui rendent de la géométrie sont désormais décrits par leur type et
leur mesure (`LineCurve L=76.536861`).

Bénéfice inattendu : les quinze charnières à menu déroulant rendent toutes
l'indice visé par `equilibrer_qcm.CIBLES`. Le rééquilibrage est donc cohérent
entre fiches et définitions — ce que rien ne vérifiait.

### Accès à Rhino — à relire à chaque session
Le serveur MCP `rhino_mcp` du bureau vise le port **9876**, ouvert par un script
qui doit tourner DANS Rhino ; la commande `MCPStart` que tape Charles ouvre le
plugin `rhinomcp` sur le port **1999**. Les deux ne se rencontrent pas : l'outil
MCP répond « connexion refusée » alors que Rhino est bien là.

**Contournement retenu, et il fonctionne** : dialoguer directement avec le socket
TCP `127.0.0.1:1999`, en JSON `{"type": ..., "params": {...}}`. Le client est
`Documentation\Generateurs\GH\client_pont_rhino.py` ; la commande utile est
`execute_rhinoscript_python_code`, et la sortie se récupère par `print`, pas par
`result`. L'interpréteur est **IronPython 2.7.12**, et il n'y définit pas
`__file__` — les scripts doivent prévoir la retombée sur un chemin en dur.

## Travail terminé
1. **Dépouillement des 6 programmes de formation** (`EXEMPLES PROGRAMMES DE FORMATION`) : 234 items relevés, 97 items distincts après dédoublonnage.
2. **`Fondamentaux Grasshopper - IndA - 25-08-2026.xlsx`** — 6 feuilles :
   - `Lisez-moi` (version, sources, méthode, légendes, journal des indices)
   - `Référentiel` — 116 lignes : 97 notions issues des programmes + 19 fondamentaux V1, classées en 10 domaines et ~30 catégories, avec matrice de couverture par programme (colonnes D3, P3, P6, P6b, P6A, RG8)
   - `Fondamentaux V1` — reprise à l'identique du tableau d'origine
   - `Contenu programmes` — 234 lignes verbatim, tracées vers le référentiel
   - `Synthèse` — comptages par domaine / niveau / mode de validation / programme + analyse des écarts
   - `Listes` — listes de valeurs des menus déroulants
3. **`Documentation\CAHIER_DES_CHARGES_EXERCICES_MAGPIE - IndA - 25-08-2026.md`** — 111 exercices décrits selon une trame identique en 10 rubriques, répartis en 4 lots et 27 thématiques (~6 400 lignes) :
   - Lot A — 49 exercices de découverte des composants natifs (Débutant)
   - Lot B — 18 exercices d'algorithmes combinés (Intermédiaire)
   - Lot C — 12 projets appliqués (architecture, mobilier, joaillerie, fabrication)
   - Lot G — 32 exercices gamifiés, une technique de gamification par exercice
4. **`Documentation\Generateurs\`** — scripts Python sources des deux livrables (reproductibles).
5. **`Documentation\Generateurs\GH\`** — générateur des fichiers Grasshopper du lot A :
   - `gh_engine.py` — moteur : instancie les composants **par leur nom** auprès du ComponentServer
     (aucun GUID en dur), fabrique la géométrie à internaliser, pose scribbles, groupes, câblage,
     puis enregistre `_complet.gh` et en dérive `_sujet.gh`.
   - `recipes_a1..a4.py` — les 49 recettes de construction (objets, étapes du corrigé, câblage).
   - `build_lot_a.py` — lanceur : contrôle à blanc du catalogue, puis production des `.gh`,
     du 3DM de A-04 et des descripteurs JSON.
   - `verifier_noms.py` — contrôle hors ligne des noms de composants par lecture des assemblages
     Rhino 8 (`Grasshopper.dll` + `Components\*.gha`).
   - `client_pont_rhino.py` — client TCP direct du plugin `rhinomcp` (port 1999).
   - `recette_1_resolution.py`, `recette_2_valeurs.py`, `recette_3_etancheite.py`,
     `lister_ports.py` — scripts de recette, à rejouer après toute modification.
6. **`Documentation\Generateurs\gen_fiches.py`** — génère, dans le dossier de chaque exercice,
   `<ID>_fiche.md` (sujet **et** corrigé, pour le formateur) et `<ID>_fiche_sujet.md`
   (sujet seul, à remettre à l'apprenant).
7. **`Documentation\Generateurs\GH\gen_images.py`** — rend chaque canvas en PNG
   (`GH_Canvas.GenerateHiResImage`, qui renvoie des tuiles à recoller).
8. **`Documentation\Generateurs\gen_fiches_docx.py`** — génère les fiches Word illustrées
   (python-docx + Pillow).
9. **`EXERCICES\LOT A - Composants natifs\`** — le livrable : 49 dossiers contenant chacun
   `<ID>_sujet.gh`, `<ID>_complet.gh`, `<ID>.json`, `<ID>_fiche.md`, `<ID>_fiche_sujet.md`,
   `<ID>_fiche.docx`, `<ID>_fiche_sujet.docx`, `Illustrations\<ID>_canvas_sujet.png` et
   `<ID>_canvas_corrige.png`, plus `Ressources\A-04_ressources.3dm` pour A-04.

## Documentation du projet
`Documentation/` porte désormais les trois documents que les règles du projet
demandent :

- `CAHIER_DES_CHARGES_EXERCICES_MAGPIE - IndB - 26-08-2026.md`
- `GUIDE_UTILISATEUR - IndB - 01-09-2026.md` — objectif, prérequis, installation,
  démarrage, workflow, paramètres, limitations, dépannage, version
- `PLANNING - IndB - 01-09-2026.md` — jalons datés, état par lot, couverture,
  durées cibles, tableau des contrôles, reste à faire

Le planning **n'invente pas de durées de travail** : l'environnement ne les
mesure pas, il écrit « non mesurée » et donne les jalons réellement datés.

Et `Journal des modifications/2026-09-01.md` pour la journée.

## Travail en cours
Aucun. La chaîne est complète, documentée et publiée.

### Décisions qui appartiennent à Charles
1. **Contribuer les neuf nouveaux lots en amont.** La PR #2 sur
   `Magpie-Project/Magpie` a été **fusionnée** le 28/08 : le lot A et le lot IA
   y sont. Les neuf lots ajoutés depuis (RH, GP, QT, FA, PL, MP, AV, DV, WB) ne
   sont **pas** remontés. Ouvrir une nouvelle PR sur le dépôt de Jérémy est un
   geste vers un tiers : il attend son accord.
2. **Nettoyer la liste noire de Word.** Word > Fichier > Options > Compléments >
   Gérer : Éléments désactivés. Sans ce nettoyage, A-13 et A-38 continueront de
   passer par la copie temporaire — ce qui fonctionne, mais reste un détour.
3. **Le poids du dépôt de publication.** `.git` pèse 108 Mo pour quatre
   publications. La dérive est stoppée (voir plus haut), mais l'historique
   accumulé reste. Si le dépôt devient gênant, deux voies : le republier à
   partir d'un commit unique, ou ne plus publier les `.docx` et les `.pdf`, que
   l'application peut reconstruire.

## Décisions prises
- Le fichier d'origine `Fondamentaux Grasshopper.xlsx` **n'est pas modifié** : le nouveau classeur est indicé `Ind. A`.
- Convention d'indice reprise des programmes RhinoForYou (`- IndA - JJ-MM-AAAA`).
- Identifiants du référentiel : `FND-nn` (fondamentaux V1), `PRG-nnn` (items de programme). Ils sont la clé de traçabilité citée par toutes les fiches d'exercice.
- Structure imposée des fichiers `.gh` : bandeau, `ZONE_SUJET` (Scribble d'énoncé + `REPONSE`), séparateur, `ZONE_CORRIGE` (un sous-groupe par étape). Deux fichiers par exercice : `<ID>_sujet.gh` et `<ID>_complet.gh`.
- **Aucun câble ne relie la zone sujet à la zone corrigé** : les composants du sujet dont le
  corrigé a besoin y sont recopiés (groupe `DONNÉES FOURNIES (copie)`), et le câblage interne
  du sujet est rejoué entre ces copies.
- **Le corrigé ne produit rien par défaut** : son résultat traverse un `Stream Gate` piloté par
  un `Boolean Toggle` nommé `AFFICHER LE CORRIGÉ`, à faux au départ ; l'aperçu est coupé sur
  tous les composants du corrigé sauf `REPONSE_CORRIGE`, placé en aval de la porte.
- Fiches d'exercice en Markdown **et** en Word illustré, chacune en version complète
  (formateur) et en version sujet seul (apprenant).
- Lot A : composants natifs exclusivement, aucun plugin tiers.

## Fichiers importants
| Fichier | Rôle |
|---|---|
| `Fondamentaux Grasshopper - IndA - 25-08-2026.xlsx` | Référentiel de notions (livrable) |
| `Fondamentaux Grasshopper.xlsx` | Source V1 de Jérémy CAROLUS — ne pas écraser |
| `Documentation\CAHIER_DES_CHARGES_EXERCICES_MAGPIE - IndA - 25-08-2026.md` | Cahier des charges des exercices (livrable) |
| `Documentation\Generateurs\build.py` + `meta.py` | Génèrent le classeur Excel |
| `Documentation\Generateurs\gen_cdc.py` + `exos_a/b/g.py` | Génèrent le cahier des charges |
| `Trame de suivie projet Magpie.xlsx` | Suivi de projet partagé (Jérémy CAROLUS) |
| `Compte_rendu_session_developpement_Magpie_2026-08-11 (1).docx` | Compte rendu de cadrage |

## Commandes importantes

**Trois interpréteurs, et ce n'est pas un choix mais un état de fait du poste :**
`openpyxl` n'est installé que sur Python 3.7, `python-docx` et `Pillow` que sur
3.14, `pywin32` que sur 3.11. Chaque script va donc avec le sien.

| Étape | Commande |
|---|---|
| Classeur du référentiel | `python "Documentation/Generateurs/build_fusion.py"` (3.7) |
| Couverture des notions | `python "Documentation/Generateurs/couverture.py"` (3.7) |
| Application | `python "Documentation/Generateurs/gen_application.py"` (3.7) |
| Cahier des charges | `py -3.14 "Documentation/Generateurs/gen_cdc.py"` |
| Fiches Markdown | `py -3.14 "Documentation/Generateurs/gen_fiches.py"` |
| Fiches Word | `py -3.14 "Documentation/Generateurs/gen_fiches_docx.py"` |
| Vignettes web | `py -3.14 "Documentation/Generateurs/gen_vignettes.py"` |
| PDF | `py -3.11 "Documentation/Generateurs/gen_pdf.py"` |
| Un seul PDF récalcitrant | `py -3.11 "Documentation/Generateurs/pdf_un.py" --copie "<fiche.docx>"` |
| Fraîcheur des livrables | `python "Documentation/Generateurs/verifier_fraicheur.py"` |

Dans Rhino (par le pont TCP, depuis `Documentation/Generateurs/GH`) :

```bash
python client_pont_rhino.py build_lots_nouveaux.py
```

Les relances **ciblées** évitent de tout reconstruire : `gen_images.py` et
`gen_fiches_docx.py` exposent tous deux un ensemble `SEULEMENT` à poser avant
d'appeler `main()`. Une fiche corrigée après coup ne doit pas rendre les 197
autres périmées — le convertisseur PDF se fie aux dates.

Publier :

```bash
python "Documentation/Generateurs/publier.py" <dossier> --protege "LOGIN:MOTDEPASSE"
```

Le mot de passe se donne **en argument, jamais dans un fichier** : la page ne
porte qu'une empreinte PBKDF2.

## Problèmes connus
- `openpyxl` n'est installé que pour Python 3.7 sur ce poste ; `python-docx` n'est installé nulle part (extracteur maison `docx2txt.py` utilisé à la place).
- Les programmes « perfectionnement 6 jours » et « perfectionnement 6 jours (1) » ont un contenu strictement identique ; l'indice A du 27/02/2025 ajoute la rubrique « Utilisation des plugins » (11 items).
- **ERREUR DE CONTENU DANS LE TABLEAU DES FONDAMENTAUX V1, notion FND-05.** Elle s'intitule
  « Data Matching par défaut (shortest list) ». C'est inexact, et cela a été vérifié dans Rhino 8
  le 26/08/2026 : la correspondance par défaut de Grasshopper est la correspondance sur la liste la
  plus **longue**, la liste courte étant prolongée par répétition de son dernier élément. Une liste
  de 10 et une liste de 4 dans une Addition produisent **10** résultats, pas 4. Le mode Shortest
  List existe mais doit être demandé explicitement par clic droit. À faire corriger par
  Jérémy CAROLUS dans le tableau d'origine. L'alerte est portée en colonne Notes du référentiel
  (via `ALERTES` dans `meta.py`) et l'exercice A-24 a été réécrit en conséquence.
- **Piège de `Collision One|Many`** : le composant ne renvoie qu'un booléen global et l'index du
  PREMIER obstacle touché, pas un booléen par obstacle. Pour obtenir un résultat par élément il
  faut inverser les rôles et grafter l'entrée Collider. `Collision Many|Many` ne convient pas :
  il n'a qu'une entrée et teste un ensemble contre lui-même. Corrigé dans l'exercice A-46.
- Le document Rhino courant est en **mètres** ; les cotes des exercices sont raisonnées en
  millimètres. Sans incidence sur la géométrie internalisée, mais à vérifier avant diffusion.
- **Positionnement des GH_Scribble** : seul `Attributes.Pivot` est conservé à l'enregistrement.
  Passer par `Attributes.Bounds` ou par les `Corners` fonctionne à l'écran mais est perdu au
  premier aller-retour : tous les scribbles se retrouvent empilés à l'origine. Vérifié par
  aller-retour le 26/08/2026. Par ailleurs `GH_Scribble` ne fait aucun retour à la ligne :
  les textes longs sont repliés par le moteur (`_replier`).
- **Panels source de données** : laisser `Properties.Multiline` à False, sinon tout le contenu
  ne forme qu'un seul élément et les conversions en aval échouent.
- **Limite de l'interrupteur de corrigé** : Grasshopper ne sait pas faire disparaître des
  composants du canvas selon un booléen. L'interrupteur commande le *résultat* (rien ne
  s'affiche dans Rhino tant qu'il est sur faux), pas la visibilité des composants sur le
  canvas. Le fichier sans corrigé reste `_sujet.gh`.
- **Conversion Word → PDF** : pas de LibreOffice sur ce poste ; passer par Word en COM.
  Vérifier d'abord si WINWORD tourne déjà et, dans ce cas, NE PAS appeler `Quit()`, sous peine
  de fermer la session Word de l'utilisateur.
- Rendu de canvas : `GH_Canvas.GenerateHiResImage(rect, settings)` renvoie une LISTE DE TUILES
  nommées `colonne;ligne.png`, à recoller soi-même.
- **Ne jamais se contenter de compter les erreurs** : sur ce lot, les trois seuls vrais défauts
  fonctionnels restants ne se manifestaient que par des AVERTISSEMENTS. Rejouer
  `avertissements.py` après toute modification.
- Les étiquettes de groupe Grasshopper sont dessinées AU-DESSUS du bord haut du groupe :
  prévoir un dégagement vertical, sinon elles recouvrent le texte qui précède.

## Tests réalisés
- Relecture du classeur généré : 116 lignes de référentiel, hiérarchie domaine → catégorie → notion vérifiée par extraction.
- Comptage de couverture vérifié : 4 fondamentaux V1 couverts, 5 partiellement, 10 absents des programmes.
- Cahier des charges : 111 fiches complètes, chacune comportant les 10 rubriques (vérifié par comptage de la rubrique 10).
- Générateur lot A — validation structurelle hors ligne : 49 recettes pour 49 fiches, aucune clé de
  câblage orpheline, aucune clé dupliquée, un paramètre `REPONSE` par exercice. **0 erreur.**
- Générateur lot A — validation des noms de composants par lecture des assemblages Rhino 8 :
  **86 / 86 noms confirmés** (une seule correction nécessaire : `Sweep 1` → `Sweep1`).
- **Recette complète dans Rhino 8 (26/08/2026), les trois passes au vert :**
  1. Ouverture et résolution des 49 `_complet.gh` : **49 / 49 sans aucune erreur de composant**,
     et le paramètre `REPONSE` est alimenté dans les 49 cas.
  2. Valeurs produites par le corrigé comparées à celles annoncées par les fiches :
     **28 / 28 conformes** (valeur exacte pour 17 exercices, cardinal pour 11).
  3. Étanchéité des 49 `_sujet.gh` : aucun objet ni groupe du corrigé ne subsiste, et
     `REPONSE` n'a **aucune source** dans les 49 fichiers.
  - Accentuation des scribbles contrôlée : correcte (IronPython 2.7 imposait un décodage explicite).
- Scripts de recette conservés : `recette_1_resolution.py`, `recette_2_valeurs.py`,
  `recette_3_etancheite.py`, `lister_ports.py` dans `Documentation\Generateurs\GH`.
- **Audit de mise en page** : après correction du positionnement des scribbles,
  **0 chevauchement d'objets sur les 49 canvas** (49 fichiers en comportaient auparavant).
- **Recette des deux règles du corrigé** (`recette_4_corrige_masque.py`) : **49 / 49 conformes**.
  Aucun câble ne traverse les deux zones ; interrupteur sur faux → sortie vide dans les 49 cas ;
  interrupteur sur vrai → résultat produit dans les 49 cas.
- Fiches Word contrôlées visuellement : conversion en PDF par Word (COM) puis rendu des pages
  en images. Mise en page, tableau d'en-tête, encadrés et illustrations conformes.
- **Audit des AVERTISSEMENTS** (`avertissements.py`), qui n'avait jamais été fait : il ne
  comptait auparavant que les erreurs. Il a révélé trois défauts réels, tous corrigés :
  A-42 l'axe de `Revolution` n'était pas alimenté (la révolution ne produisait rien) ;
  A-22 `Explode Tree` n'avait que 2 sorties pour 3 branches ; A-26 un paramètre
  `BONNE_REPONSE` orphelin. Ne subsiste que l'avertissement voulu sur `REPONSE`, non
  connecté par construction dans la zone sujet.
- **Revue visuelle des canvas** par planches-contact (9 vignettes par planche) : 4 planches
  lues en détail, soit 36 canvas sur 98, les autres étant structurellement identiques.
  Elle a révélé un défaut systématique sur les 49 sujets — l'étiquette du groupe
  `ZONE_SUJET` recouvrait la ligne de métadonnées du bandeau — et des câbles en diagonale
  dus aux copies de rappel laissées à leur position d'origine. Les deux sont corrigés.

## Tests restant à faire
- Régénérer le classeur une fois Excel fermé, puis contrôler mise en forme et formules `COUNTIF`.
- Ouverture visuelle de quelques `.gh` dans Grasshopper : l'absence de chevauchement est
  désormais contrôlée automatiquement, mais l'esthétique d'ensemble reste à juger à l'œil.
- Test des 6 exercices à réglage manuel après réglage : A-04, A-23, A-26, A-42, A-46, A-48.
- Test des exercices par une personne réellement débutante.
- Relecture technique du cahier des charges par Jérémy CAROLUS.

## Prochaines actions prioritaires
## Prochaines actions prioritaires
1. Fermer Excel et relancer `build.py` pour régénérer le classeur avec l'alerte FND-05.
2. Faire trancher par Jérémy CAROLUS la correction de FND-05 dans le tableau d'origine.
3. Soumettre le format du descripteur JSON à Jérémy CAROLUS : celui produit est une **proposition**,
   le format réellement attendu par le plugin Magpie n'est pas connu.
4. Tester quelques exercices dans le plugin Magpie lui-même (chargement, validation, métriques).
5. Régler à la main les 6 exercices concernés (A-04, A-23, A-26, A-42, A-46, A-48) et les retester.
6. Contribuer les neuf lots récents en amont sur `Magpie-Project/Magpie` : la
   PR #2 fusionnée ne couvre que les lots A et IA. Décision à prendre avec
   Jérémy CAROLUS.
7. Faire arbitrer les 8 points ouverts du chapitre 12 du cahier des charges.
8. Reporter les lignes de travail correspondantes dans `Trame de suivie projet Magpie.xlsx`.

## Interdictions / points de vigilance
- Ne jamais écraser `Fondamentaux Grasshopper.xlsx` ni `Trame de suivie projet Magpie.xlsx` (fichiers de Jérémy CAROLUS).
- Ne pas commiter sur la branche `feat/android-app` sans arbitrage : le dépôt couvre l'ensemble du dossier `.claude`.
- Toute production assistée par IA doit faire l'objet d'une vérification humaine avant intégration (règle actée en réunion).
- Ne jamais toucher `exos_a.py`, `exos_b.py` ni `exos_g.py` : ce sont les
  fiches d'origine de Jérémy CAROLUS. Les couches pédagogiques (`skill_a.py`,
  `skill_b.py`, `skill_c.py`) se superposent, elles ne remplacent pas.
- `GeometryTolerance` ne compare **qu'un seul élément**, et le checker Magpie
  ne compare **que des nombres** : un booléen ou un texte branché sur
  `REPONSE` échoue. C'est ce qui rendait huit exercices du lot B
  incorrigibles tels qu'écrits.
- Un nom d'objet ne doit désigner qu'une chose dans une recette : le second
  écrase le premier et déplace des fils sans rien signaler.
  `recette_8_noms_uniques.py` le contrôle.
- **Toute liste écrite à la main finit par décrocher.** SEPT fois dans ce
  projet : `AVEC_DEFINITIONS`, les sources de `verifier_fraicheur`, ses
  préfixes, les modules de `recette_7`, le corpus d'`audit_skill`, les
  pilotes de construction par lot, et le chargeur des vagues de `lots.py`.
  Toute nouvelle liste de modules ou d'exercices doit être DÉCOUVERTE.
- **Ne jamais nommer une fonction utilitaire `_f`, `_b`, `_e`.** En
  IronPython 2, la variable de boucle d'une compréhension fuit dans la
  portée englobante et l'écrase. Le piège s'est refermé trois fois :
  « str is not callable », « int is not callable », « bool is not
  callable ». Les noms courts sont réservés aux variables de boucle.
- `audit_skill.py --tous` audite les 229 exercices ; sans `--tous`, il ne
  voit que le lot A.
- **Reconstruire par `GH/build_tout.py`**, jamais par un pilote de lot : il
  découvre les recettes et rejoint le dossier EXISTANT de chaque exercice.
  Les lots A et IA ont des dossiers à TITRE LONG ; un constructeur qui
  écrit dans un dossier court les duplique silencieusement.
- Les 229 exercices portent les huit champs de la skill. L'audit compte
  11 écarts, tous §1 et tous documentés.

## Commande de production du lot A
À exécuter **dans Rhino 8** (Outils > Éditeur de scripts, Python 3), Grasshopper ayant été ouvert
au moins une fois dans la session :
```
C:\Users\charl\.claude\projects\MAGPIE\Documentation\Generateurs\GH\build_lot_a.py
```
Sortie attendue : `EXERCICES\LOT A - Composants natifs\<ID> <titre>\` contenant
`<ID>_sujet.gh`, `<ID>_complet.gh`, `<ID>.json`, plus `Ressources\A-04_ressources.3dm`.

## Dernière demande utilisateur
« Fais les lots B, C et G. » Puis « continue avec le lot C ».

- **Lot B — fait** (02/09) : 18 exercices, `skill_b.py`, huit modes de
  validation corrigés, 36 définitions.
- **Lot C — fait** (02/09) : 12 projets appliqués, `skill_c.py`, un indicateur
  vérifiable par projet, 24 définitions. Publié et poussé.
- **Lot G — fait** (02/09) : 32 exercices gamifiés, `skill_g.py`, quatorze
  modes de validation corrigés, six corrigés par étalon, 64 définitions.
  Publié et poussé.

**Le cahier des charges est entièrement produit.**

## Le lot C, et ce qu'il a demandé de trancher
Un projet ne se réduit pas à un nombre : une résille relaxée, un devis
structuré par lot, un plan d'imbrication et ses DXF ne sont pas des valeurs.
Mais chaque fiche d'origine annonçait déjà « deux indicateurs affichés ».
**Chaque projet porte donc un indicateur corrigé automatiquement, le reste
étant jugé sur grille** — l'apprenant sait seul s'il s'est trompé avant de
rendre, sans que le projet soit dénaturé.

Deux corrigés passent par l'étalon plutôt que par une chaîne de composants :
**C-03**, dont la progression des gradins est récursive, et **C-11**, dont le
décompte des plis par segment est une condition, pas un calcul.

Deux défauts trouvés et corrigés à cette occasion :

- **C-12 ne discriminait pas.** Avec ou sans les espacements, il fallait trois
  plaques — le piège de l'exercice n'existait pas — et 10,46 % de chute
  suppose 95 % de remplissage, ce qu'aucune découpe n'atteint. Pièces grossies
  de 4 % : 13,07 m² nus tiennent en trois plaques, 13,45 m² espacés n'y
  tiennent plus.
- **C-02 répondait 0,0034 m au lieu de 695,53.** La recette appelait « m » le
  curseur *maille* du sujet et la division finale du corrigé ; la seconde a
  écrasé le premier dans la table nom → objet. D'où `recette_8_noms_uniques.py`.

Le niveau « Expérimenté » des fiches d'origine, inconnu du reste du
référentiel, est ramené à « Perfectionnement » par `skill_c.fusionner`.

## La vague 4 — densifier plutôt qu'étendre
Quinze catégories restaient à un exercice par notion après les lots B, C et G,
qui avaient nourri les catégories déjà denses. Vingt-quatre exercices les
relèvent, sur des notions DÉJÀ couvertes mais par un angle différent : là où
le premier fait construire, celui-ci fait choisir, compter ou vérifier.

Leurs tableaux sont des inventaires — types, calques, canaux de distribution,
verbes d'opération. Le checker ne compare que des nombres : chaque colonne est
fournie CODÉE, la légende dans le sujet. Le raisonnement logique reste entier,
seule la comparaison de chaînes disparaît.

Un seul étalon, PL-15 : la couverture d'ensemble ne se résout pas avec des
composants natifs, et le nombre minimal est unique là où la solution ne l'est
pas.

## Le lot G, et ses deux pièges de conception
Le lot G portait le défaut du lot B en pire : **six exercices en
`GeometryTolerance`** — qui ne compare qu'un seul élément — tout en produisant
cinq formes ou une harde de douze, et **huit en `SetEquality`** sur des choses
qui ne sont pas des ensembles de nombres.

Principe retenu : **l'indicateur vérifiable est la métrique du jeu lui-même**.
Le score d'un tableau des scores, l'index trouvé d'une chasse au trésor, la
longueur cumulée d'une animation à mi-parcours.

Six corrigés passent par l'étalon — mots croisés, memory, machine à sous,
quiz, vrai/faux, boîte noire. Leur réponse ne se calcule pas, elle se sait.

Deux défauts corrigés à cette occasion, tous deux invisibles :

- **Le générateur des jeux de données lisait ses bits de poids faible.** Sur
  une suite congruentielle de module 2³¹, le bit de poids faible ALTERNE : la
  parité de G-06 était prévisible sans regarder une donnée. Il lit désormais
  les bits de poids fort.
- **G-06 demandait une somme de chiffres**, qu'aucun composant natif ne
  calcule. Le troisième niveau compare désormais à la moyenne des survivants
  du niveau 2 — chaîne entièrement native, et le piège devient réel : traiter
  les trois conditions indépendamment garde quinze index au lieu de huit.

Trois câblages n'ont été démasqués que par le relevé dans Rhino : `Sub List`
dont le domaine était une valeur figée (G-08), `Merge` sur deux ARBRES qui
entrelace branche à branche (G-22), et `Mass Addition` qui somme PAR BRANCHE
(G-30, même défaut que QT-04 en août — la troisième fois).
