---
name: magpie-conception-exercices
description: "Concevoir des exercices auto-corrigés Magpie (Grasshopper) : distinguer compétence et connaissance, aligner objectif / tâche / validation, étayer par le graphe de départ, ancrer dans un contexte d'application, et respecter les contraintes du checker. À utiliser dès qu'il s'agit d'écrire, réviser ou trier des exercices Magpie."
disable-model-invocation: false
user-invocable: true
effort: medium

domain: "magpie"
version: "2.3"
chains_well_with:
  - "worked-example-fading-designer"
  - "assessment-validity-checker"
  - "hinge-question-designer"
  - "cognitive-load-analyser"
---

# Conception d'exercices Magpie

Magpie évalue en **auto-correction** : l'apprenant construit un graphe Grasshopper, un
composant compare sa sortie à une valeur attendue, et rend un verdict. Ce dispositif est
puissant sur un point et aveugle sur trois autres — il voit un résultat, jamais une méthode,
jamais une intention, jamais une difficulté. Toute la conception consiste à faire porter au
**choix de la tâche** ce que la correction automatique ne peut pas porter.

Six fondements, chacun avec sa conséquence opérationnelle.

---

## 1. Un exercice teste une compétence, jamais une connaissance

C'est le filtre qui élimine le plus de propositions, et il n'est pas cosmétique : c'est une
distinction ancienne et bien établie.

**Ryle (1949)** sépare le *knowing that* du *knowing how* : savoir qu'un booléen vaut 1 une
fois converti, et savoir s'en servir pour compter des pièces conformes, sont deux choses
qu'aucune ne garantit l'autre. **Anderson (1982)** en donne le mécanisme cognitif : la
connaissance déclarative se **procéduralise** par la pratique, en passant d'un savoir
verbalisable à des productions directement exécutables. Un exercice qui demande la
connaissance déclarative n'entraîne pas la procédure — il vérifie seulement qu'elle a été
lue.

**Miller (1990)** en tire la conséquence évaluative sous forme de pyramide :

| Niveau | Ce qu'on évalue | Format adapté |
|---|---|---|
| *Knows* | le fait | question, QCM |
| *Knows how* | savoir comment on ferait | question de raisonnement |
| *Shows how* | faire, en situation construite | **l'exercice Magpie** |
| *Does* | faire, en situation réelle | projet, mise en situation |

Magpie vit au niveau *shows how*. Y placer un item de niveau *knows* est une erreur
d'instrument : on paie le coût d'un exercice pour la valeur d'une question.

### Le test d'élimination

Si la réponse s'obtient en **sachant** plutôt qu'en **construisant**, ce n'est pas un
exercice. Trois signaux :

1. **Un seul composant suffit.** On mesure la connaissance de l'existence de ce composant,
   pas une logique de conception.
2. **L'exercice met en évidence un comportement du logiciel** au lieu de demander un
   résultat. « Constatez que deux listes inégales s'apparient ainsi » est une démonstration.
3. **La bonne réponse est devinable sans rien monter.** On mesure la mémoire.

**Ce n'est pas une raison de supprimer la notion.** Une connaissance nécessaire reste à
transmettre — par une explication ou une **question charnière** en amont, pas par un
exercice noté. Une bonne question charnière (Wiliam, 2011) est celle dont la mauvaise
réponse est *diagnostique* : elle dit laquelle des représentations fausses l'apprenant
porte.

### Bloom : la grille, pas l'échelle

La **taxonomie de Bloom révisée** (Anderson & Krathwohl, 2001) est utile à condition de
l'employer pour ce qu'elle est devenue. La version de 1956 postulait une hiérarchie
cumulative — il faudrait maîtriser « comprendre » avant « appliquer » — et cette hiérarchie
stricte **ne résiste pas à l'examen empirique** : les niveaux ne s'ordonnent pas
proprement en difficulté. La révision de 2001 abandonne la hiérarchie stricte et croise
deux dimensions indépendantes :

- **dimension connaissance** — factuelle, conceptuelle, **procédurale**, métacognitive ;
- **dimension processus cognitif** — mémoriser, comprendre, appliquer, analyser, évaluer, créer.

Ce qui est opérationnel ici, c'est la **case**, pas l'étage. Un exercice Magpie vise
typiquement *appliquer* ou *analyser* × connaissance **procédurale**. Écrire la case avant
d'écrire la consigne évite deux dérives : croire qu'un verbe ronflant élève le niveau
cognitif, et confondre « exercice difficile » avec « exercice de haut niveau ».

> **Attention aux référentiels.** Ils mélangent couramment connaissances et compétences.
> Passer chaque ligne au filtre avant d'écrire, et **le dire** quand une ligne du référentiel
> est en réalité une connaissance : c'est une information utile pour le formateur, pas une
> critique.

---

## 2. Aligner objectif, tâche et validation

**Biggs (1996)** : un dispositif n'enseigne bien que si l'objectif, l'activité et
l'évaluation visent le même verbe — l'*alignement constructif*. Le maillon faible impose
son niveau à tout le reste : une intention « concevoir » évaluée par un QCM produit des
apprenants qui révisent pour le QCM.

Dans Magpie, l'alignement a une pièce de plus : **le mode de validation fait partie de
l'objectif**. Décider qu'une réponse est acceptée « dans n'importe quel ordre » ou « dans
cet ordre exact », c'est décider si l'ordre fait partie de la compétence. Ce choix se fait
en écrivant l'objectif, pas en constatant après coup ce que la sortie produit.

**Conséquence** : écrire dans cet ordre — (1) la compétence visée et sa case Bloom, (2) la
tâche, (3) le mode de validation qui rend cette tâche discriminante, (4) seulement ensuite
la consigne.

---

## 3. Étayer : le graphe de départ est un échafaudage

**Vygotsky (1978)** situe l'apprentissage dans la *zone proximale de développement* — l'écart
entre ce que l'apprenant fait seul et ce qu'il fait avec assistance. **Wood, Bruner & Ross
(1976)**, qui introduisent le terme *scaffolding*, décrivent la fonction de l'étayage :
réduire les degrés de liberté de la tâche pour que l'apprenant se concentre sur ce qu'il
peut effectivement traiter.

**van de Pol, Volman & Beishuizen (2010)**, en synthétisant une décennie de recherche,
dégagent trois caractéristiques sans lesquelles il n'y a pas d'étayage :

1. **contingence** — le soutien répond à ce que l'apprenant fait ;
2. **estompage (fading)** — le soutien décroît ;
3. **transfert de responsabilité** — l'apprenant reprend la main.

Le **graphe de départ** est exactement cela : il fournit la donnée pré-câblée et paramétrée,
ce qui décharge la mise en place et laisse l'apprenant produire le seul geste que la
compétence décrit.

> **Limite à assumer.** Magpie n'a **pas** de contingence : le graphe de départ est le même
> pour tous et ne s'adapte pas. Ce n'est donc pas de l'étayage au sens plein, c'est du
> *completion fading* (van Merriënboer & Kirschner, 2018) — une suite de tâches à trous dont
> la part fournie diminue. Le fading se joue donc **sur le parcours**, pas dans un exercice :
> les premiers exercices fournissent l'essentiel du montage, les derniers démarrent sur
> canvas vide. Toute contingence réelle demanderait de choisir l'exercice suivant d'après la
> performance — fonctionnalité absente à ce jour.

**Kalyuga, Ayres, Chandler & Sweller (2003)** ajoutent la contrainte inverse : l'*effet
d'inversion d'expertise*. Un étayage bénéfique au novice devient nuisible à l'apprenant
avancé, qui doit alors traiter une information redondante. Un graphe de départ trop
complet, arrivé trop tard dans un parcours, coûte au lieu d'aider.

**Conséquences** :

- **La consigne donne l'objectif, le graphe de départ donne la donnée.**
- **Aucun nom de composant dans la consigne.** Nommer l'outil, c'est donner la réponse.
- **Une contrainte plutôt qu'une marche à suivre** : « sans compter les éléments » ferme une
  voie de contournement sans nommer la solution.
- **Pas de gymnastique intellectuelle.** Une consigne qu'il faut relire trois fois évalue la
  compréhension de l'énoncé. Si l'objectif ne s'énonce pas simplement, l'exercice est mal posé.
- **Décroître.** Sur un parcours, la part fournie doit baisser ; le dernier exercice d'une
  compétence se fait sans graphe de départ.

---

## 4. Contextualiser : authenticité et transfert

C'est le point le plus mal compris de la conception d'exercices, parce que « contexte » y
est souvent confondu avec « décor ».

**Brown, Collins & Duguid (1989)** posent que le savoir est indissociable de l'activité et
de la situation dans lesquelles il s'élabore : une procédure apprise hors situation reste
« inerte », disponible en examen et indisponible en atelier.

**Gulikers, Bastiaens & Kirschner (2004)** en font un cadre exploitable en cinq dimensions —
la tâche, le contexte physique, le contexte social, la forme du résultat, et les critères
d'évaluation — et établissent un point décisif : **l'authenticité est perçue, pas
objective**. Ce qui compte est que l'apprenant reconnaisse la situation comme relevant de
son métier. Un enrobage réaliste et lourd n'authentifie rien si la tâche reste scolaire ;
**une phrase suffit** si la tâche, elle, est celle du métier.

C'est ce qui autorise — et impose — le format court :

> **Sans contexte** — « Combien de valeurs le composant fourni produit-il ? »
>
> **Avec contexte** — « Une poutre de 10 m est divisée en 4 travées égales. Combien de
> poteaux faut-il pour la soutenir ? »

Même calcul. Mais l'erreur classique — répondre 4, un poteau par travée — devient une poutre
qui s'effondre plutôt qu'un chiffre faux. Le contexte fournit à l'apprenant un **critère de
vraisemblance** qu'un énoncé abstrait ne donne pas.

**Barnett & Ceci (2002)** permettent de dire précisément ce que « varier le contexte »
signifie : leur taxonomie situe le transfert sur le **contenu** et sur le **contexte**, ce
dernier se déclinant en domaine de connaissance, contexte physique, temporel, fonctionnel,
social et modalité. Varier, ce n'est pas changer les nombres : c'est déplacer l'exercice sur
au moins une de ces dimensions. **Perkins & Salomon (1992)** distinguent de leur côté le
transfert par *voie basse* — automatisé, par similarité de surface — du transfert par *voie
haute*, qui exige une abstraction délibérée du principe.

**Paas & van Merriënboer (1994)** apportent la preuve expérimentale de l'*effet de
variabilité* : des exemples variés coûtent plus cher à traiter mais produisent un meilleur
transfert que des exemples uniformes.

**Un contexte trop spécifique introduit un biais étranger à la compétence.** Messick (1989)
nomme *variance non pertinente au construit* tout ce qui fait varier le score sans faire
varier la compétence visée — nommer un composant dans la consigne en est un exemple (§3), un
contexte que seule une partie du public reconnaît en est un autre. Un apprenant qui maîtrise
parfaitement la compétence peut échouer parce que le métier, la région ou l'unité évoquée lui
sont étrangers : ce n'est plus la compétence qui est mesurée, c'est la familiarité avec un
décor.

**Un contexte doit aussi être *plausible*, et ça se vérifie plutôt que ça ne se suppose.**
L'authenticité perçue (Gulikers et al.) et la mise en situation (Brown, Collins & Duguid) ne
fonctionnent que si le contexte résiste à l'examen de quelqu'un qui connaît vraiment le
métier. Un chiffre qui semble concret mais physiquement impossible casse l'authenticité au
lieu de la renforcer, et introduit un doute étranger à la compétence : l'apprenant hésite
parce que l'énoncé ne « sonne pas juste », pas parce qu'il ne sait pas résoudre le problème.
C'est un défaut de *validité apparente* — le contenu doit sembler mesurer ce qu'il prétend
mesurer dès l'inspection, y compris pour un lecteur du métier.

> Exemple : un panneau de bois **860 × 1200 × 2100 mm** n'existe pas. Un panneau a deux
> dimensions de l'ordre du mètre et une épaisseur de l'ordre du centimètre ; la troisième
> valeur, ici, en fait un bloc plein. L'erreur vient de traiter trois nombres comme
> interchangeables alors qu'ils ne le sont pas dans le métier — vérifier contre un ordre de
> grandeur ou un catalogue réel, jamais seulement contre la cohérence interne du calcul, qui
> sera toujours bonne puisque c'est nous qui l'avons construit.

**La plausibilité porte aussi sur la direction d'une conversion, pas seulement sur l'ordre
de grandeur d'une valeur.** Un contexte qui implique « il en faut au moins autant » (une
commande, un approvisionnement) appelle un arrondi au **supérieur** ; un contexte qui
implique « pas plus que ce qui existe réellement » (un débit, un prélèvement) appelle une
**troncature**. L'arrondi au plus proche — celui que produit la conversion implicite d'un
décimal vers un entier dans Grasshopper — ne correspond à aucun des deux : il coïncide avec
l'un ou l'autre selon la décimale, par hasard. Une consigne dont la conclusion attendue et
la conversion réellement testée ne s'accordent que pour la valeur choisie n'est juste que
par coïncidence : vérifier le raisonnement sur plusieurs valeurs plausibles, pas seulement
sur celle retenue pour l'exercice.

**Conséquences** :

- **Un contexte par exercice, en une phrase**, dans le domaine de l'apprenant
  (construction, fabrication, façade, structure).
- **Courant et transculturel** — reconnaissable par un public large, pas une pratique
  régionale ou un jargon de niche ; rédigé pour se traduire sans perte (éviter jeux de mots,
  idiomes, unités non standard).
- **Plausible, vérifié** — les valeurs numériques du contexte correspondent à un ordre de
  grandeur ou un catalogue réel du métier, pas seulement à une cohérence interne du calcul.
- **Le contexte n'ajoute aucune étape de calcul** : il habille la donnée, il ne la complique
  pas. Sinon la charge de lecture prend le pas sur la compétence évaluée.
- **Il rend l'erreur détectable** par l'apprenant lui-même.
- **Varier le contexte entre exercices d'une même compétence**, pas seulement les valeurs.
- **Si aucun contexte crédible ne vient**, c'est le signal que l'exercice teste une
  connaissance (§1). Supprimer plutôt qu'habiller artificiellement.

---

## 5. Des données réalistes, et des difficultés désirables

Une liste de 1 à 10 dans l'ordre se lit à l'œil : l'apprenant compte sur ses doigts et
court-circuite la compétence.

**Chi, Feltovich & Glaser (1981)** ont montré que novices et experts catégorisent les
problèmes différemment — les novices sur les traits de **surface**, les experts sur la
**structure profonde**. Des données de démonstration entretiennent le traitement de surface :
elles rendent visible une réponse qui devrait être *construite*.

**Bjork & Bjork (2011)** nomment *difficultés désirables* les conditions qui ralentissent
l'acquisition mais améliorent la rétention et le transfert. Allonger et désordonner une
liste est exactement cela : plus coûteux sur le moment, plus formateur.

**Conséquences** :

- **Listes longues** — 20 à 40 éléments plutôt que 5 à 10.
- **Non ordonnées** — sauf si l'ordre est justement le sujet.
- **Valeurs non devinables** — des cotes, des références ; pas 1, 2, 3.
- **Attention à la frontière** : la difficulté doit porter sur la compétence, pas sur la
  lecture de l'énoncé ni sur la saisie. Une difficulté qui n'entraîne rien est de la charge
  extrinsèque, pas une difficulté désirable.
- **La plausibilité du domaine prime sur la variété générique.** Ces deux règles entrent
  parfois en tension — des hauteurs de marche d'escalier, par exemple, doivent rester
  presque constantes (une exigence du métier, pas un détail), ce qui interdit de les
  disperser pour éviter le comptage à l'œil. Quand c'est le cas, loger la variété ailleurs
  (le nombre d'éléments, l'écart entre sous-ensembles, la longueur du calcul) plutôt que de
  forcer une donnée qui n'existerait pas dans la réalité du métier (§4).
- **Contrainte du checker** : la réponse attendue doit rester **numérique**. Une liste
  d'identifiants est excellente en *entrée* — elle interdit le dénombrement à l'œil — mais la
  réponse doit être un comptage, une somme, une cote extraite.

---

## 6. Le feedback : ce que Magpie rend, et à quel niveau

C'est le point où l'intuition trompe le plus.

**Kluger & DeNisi (1996)**, sur 607 tailles d'effet et 23 663 observations, trouvent un effet
moyen positif mais modeste (d ≈ 0,41) — **et plus d'un tiers des interventions de feedback
qui dégradent la performance**. Le feedback n'est pas bon en soi. Leur explication : il aide
quand il dirige l'attention vers la **tâche**, il nuit quand il la dirige vers le **soi**.

**Hattie & Timperley (2007)** structurent cela en quatre niveaux, par efficacité
décroissante pour l'apprentissage :

| Niveau | Contenu | Effet |
|---|---|---|
| Tâche | la réponse est-elle correcte | utile, mais plafonne vite |
| Processus | la démarche qui mène à la réponse | le plus efficace |
| Autorégulation | comment l'apprenant pilote son travail | très efficace, plus rare |
| Soi | « bravo », « tu es doué » | **inefficace, parfois nuisible** |

**Shute (2008)** ajoute les conditions pratiques : spécifique, centré sur la tâche, non
comparatif, et suffisamment bref pour être lu.

**Où en est Magpie.** Le verdict actuel est du feedback **de niveau tâche** — correct /
incorrect, avec parfois l'écart constaté. C'est le plancher utile : ça ne dit rien de la
démarche. Deux leviers existent sans développement :

- **le champ « erreur attendue » de chaque exercice** : en anticipant l'erreur typique, on
  prépare un message de niveau processus plutôt qu'un simple « faux » ;
- **la question charnière** : un exercice dont la mauvaise réponse est diagnostique
  transforme un verdict binaire en information exploitable.

**Sur l'immédiateté**, nuance : pour l'acquisition de **procédures**, un feedback immédiat
est généralement supérieur — c'est le principe des tuteurs cognitifs (Anderson, Corbett,
Koedinger & Pelletier, 1995), et c'est le régime naturel de Magpie. Mais l'immédiateté ne
compense jamais un feedback de mauvais niveau : rendre « faux » plus vite ne rend pas « faux »
plus utile.

**Sur la sécurité psychologique** que suppose la prise de risque : elle se joue en partie dans
le dispositif. Magpie compte les tentatives, et **ne compte pas une soumission vide** comme un
échec — un choix cohérent avec Kluger & DeNisi : moins le dispositif produit de jugement sur
la personne, plus l'attention reste sur la tâche.

---

## 7. Ancrer : récupération et espacement

Un exercice auto-corrigé n'est pas qu'une évaluation : c'est une **récupération active**, et
la récupération est un des mécanismes d'apprentissage les mieux établis.

**Roediger & Karpicke (2006)** montrent que se tester produit une rétention à long terme
supérieure à relire, alors même que les apprenants jugent l'inverse. **Dunlosky, Rawson,
Marsh, Nathan & Willingham (2013)**, en évaluant dix techniques d'apprentissage courantes,
ne classent que deux d'entre elles en **utilité élevée** : la *pratique de test* et la
*pratique distribuée*. **Cepeda, Pashler, Vul, Wixted & Rohrer (2006)** confirment par
méta-analyse l'avantage de l'espacement sur le massage des répétitions.

**Conséquences pour les parcours** :

- **Ne pas bloquer sur un exercice raté.** La valeur d'apprentissage est dans la tentative ;
  bloquer transforme une récupération en obstacle.
- **Faire revenir une compétence dans un parcours ultérieur**, dans un autre contexte — ce
  qui sert l'espacement (§7) et le transfert (§4) d'un même geste de conception.
- **Le récapitulatif de fin de parcours** est le moment du débriefing : c'est là qu'on peut
  nommer le principe commun à des exercices que l'apprenant a vécus comme distincts —
  autrement dit tenter le transfert par *voie haute* de Perkins & Salomon.

---

## Contraintes du checker Magpie

Vérifié sur `plugin/Core/GenericChecker.cs`, et relevé dans Grasshopper.

| Mode | Comportement réel |
|---|---|
| `SingleValue` | égalité à `1e-9` — **`Tolerance` est ignorée** |
| `ExactOrderedList` | `SequenceEqual` sur `double` — aucune tolérance |
| `SetEquality` | `HashSet.SetEquals` — aucune tolérance, **multiplicités non vérifiées** |
| `NumericTolerance` | seul mode positionnel tolérant |
| `GeometryTolerance` | un seul élément ; écart maximal en unités du modèle (§8 du journal plugin) |

- Toute valeur attendue non entière impose `NumericTolerance`.
- En `GeometryTolerance`, la réponse est comparée **par la forme**, pas par la construction :
  point, courbe (ligne, arc, cercle, rectangle inclus), surface / brep / boîte, maillage. Le
  sens de parcours, la couture et le paramétrage sont ignorés — un exercice qui doit porter
  là-dessus se valide numériquement. La famille et la fermeture (courbe fermée, solide) sont
  vérifiées, elles.
- **`Tolerance` est obligatoire dès que l'attendu est une surface, un brep ou un maillage**,
  et doit valoir au moins `√(aire / 1500)` — soit 0.09 pour une sphère unité, 0.26 pour une
  plaque 10×10. C'est la maille de l'échantillonnage : en deçà, deux constructions de la même
  forme sont déclarées différentes. Non renseignée, la tolérance retombe sur celle du document
  Rhino (0.001), qui refuserait une réponse correcte. Points et courbes ne sont pas concernés.
- Un attendu contenant des **doublons** interdit `SetEquality` : passer en `ExactOrderedList`.
- Un booléen ou un texte branché sur la vérification échoue. La réponse doit être ramenée à
  un nombre **par le montage de l'apprenant** — ce qui doit rester une étape naturelle de la
  tâche, pas une gymnastique imposée par l'outil. Si la conversion est le seul enjeu, c'est
  une connaissance (§1).
- L'entrée est en `GH_ParamAccess.list` : un arbre non aplati est vérifié **branche par
  branche**. Utile — l'aplatissement devient observable — mais dès qu'une réponse peut
  arriver en arbre, la consigne doit demander une liste unique, sinon l'exercice est
  insoluble.
- **La validation ne contrôle que le résultat, jamais la méthode.** Rien n'empêche de saisir
  la réponse à la main. C'est la principale menace de validité du dispositif : préférer les
  résultats qu'on ne peut pas obtenir de tête, et le savoir quand on interprète un score.

---

## Procédure

1. **Filtrer** — compétence ou connaissance (§1) ? Si connaissance : question charnière ou
   support de cours, pas exercice.
2. **Situer** — case Bloom révisée : quel processus cognitif, sur quel type de connaissance ?
3. **Aligner** — objectif, tâche, mode de validation (§2), dans cet ordre.
4. **Contextualiser** — une phrase, dans le métier de l'apprenant (§4).
5. **Doser l'étayage** — que fournit le graphe de départ, que reste-t-il à construire (§3) ?
   Où se situe l'exercice dans la décroissance du parcours ?
6. **Choisir les données** — longues, désordonnées, non devinables ; réponse numérique (§5).
7. **Anticiper l'erreur** — quelle est l'erreur typique, et la consigne la rend-elle
   distinguable d'une réussite (§6) ?
8. **Vérifier** — voir ci-dessous.

## Vérifier avant de livrer

1. **Solution unique** — confronter l'attendu au mode de validation et vérifier qu'une
   réponse voisine (un élément faux, en moins, en trop, ordre inversé, multiplicité fausse,
   une seule branche) échoue bien.
2. **Valeurs relevées, pas déduites** — monter le graphe dans Grasshopper et lire la sortie.
   La sémantique se devine mal : ordre de sortie d'un croisement, profondeur d'un arbre après
   deux transformations, nombre de branches d'un découpage. Attention : l'aperçu d'inspection
   est tronqué à 10 éléments, lire le compte réel.
3. **Consigne muette** — aucun nom de composant.
4. **Désambiguïser par GUID** — de nombreux noms correspondent à plusieurs composants,
   dépréciés compris.
5. **Contexte plausible et universel** — les grandeurs citées correspondent à un ordre de
   grandeur ou un catalogue réel du métier (pas de panneau de bois de 2 m d'épaisseur) ; rien
   dans l'énoncé ne suppose une pratique régionale, un jargon de niche, ou ne résiste pas à
   la traduction.
6. **Direction de conversion cohérente** — pour tout exercice décimal → entier, le sens
   d'arrondi qu'implique le contexte (supérieur, inférieur, au plus proche) correspond à
   celui réellement testé par le graphe, et pas seulement pour la valeur choisie : essayer
   mentalement une valeur dont l'arrondi et la troncature divergent.
7. **Checker-safe par construction** — valeurs attendues entières sauf mode
   `NumericTolerance` ; jamais de `Tolerance` non nulle sur `SingleValue` ; jamais de
   doublon dans un attendu `SetEquality`.

## Ce que cette skill ne résout pas

- **Pas de contingence** : l'étayage ne s'adapte pas à l'apprenant (§3). C'est la principale
  distance entre ce dispositif et l'étayage décrit par la recherche.
- **Pas de feedback de processus automatique** (§6) : il faut l'anticiper exercice par
  exercice.
- **Pas de contrôle de la méthode** : la validation reste aveugle au graphe produit.
- **Le transfert n'est pas mesuré** : réussir l'exercice ne prouve pas que la compétence
  s'appliquera ailleurs. Seule la variation des contextes entre exercices y travaille (§4).

---

## Références

**Compétence et connaissance**
Ryle, G. (1949). *The Concept of Mind*. •
Anderson, J. R. (1982). Acquisition of cognitive skill. *Psychological Review*, 89(4), 369–406. •
Miller, G. E. (1990). The assessment of clinical skills/competence/performance. *Academic Medicine*, 65(9), S63–S67. •
Anderson, L. W., & Krathwohl, D. R. (dir.) (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy*.

**Alignement et validité**
Biggs, J. (1996). Enhancing teaching through constructive alignment. *Higher Education*, 32, 347–364. •
Messick, S. (1989). Validity. In R. L. Linn (dir.), *Educational Measurement* (3ᵉ éd.). •
Kane, M. T. (2006). Validation. In R. L. Brennan (dir.), *Educational Measurement* (4ᵉ éd.). •
Wiliam, D. (2011). *Embedded Formative Assessment*. •
Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education*, 5(1), 7–74.

**Étayage, charge cognitive, estompage**
Vygotsky, L. S. (1978). *Mind in Society*. •
Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry*, 17(2), 89–100. •
van de Pol, J., Volman, M., & Beishuizen, J. (2010). Scaffolding in teacher–student interaction: A decade of research. *Educational Psychology Review*, 22, 271–296. •
Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998/2019). Cognitive architecture and instructional design. *Educational Psychology Review*. •
Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist*, 38(1), 23–31. •
Renkl, A., & Atkinson, R. K. (2003). Structuring the transition from example study to problem solving. *Educational Psychologist*, 38(1), 15–22. •
van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten Steps to Complex Learning* (3ᵉ éd.).

**Contexte, authenticité, transfert**
Brown, J. S., Collins, A., & Duguid, P. (1989). Situated cognition and the culture of learning. *Educational Researcher*, 18(1), 32–42. •
Gulikers, J. T. M., Bastiaens, T. J., & Kirschner, P. A. (2004). A five-dimensional framework for authentic assessment. *Educational Technology Research and Development*, 52, 67–85. •
Barnett, S. M., & Ceci, S. J. (2002). When and where do we apply what we learn? A taxonomy for far transfer. *Psychological Bulletin*, 128(4), 612–637. •
Perkins, D. N., & Salomon, G. (1992). Transfer of learning. *International Encyclopedia of Education*. •
Paas, F., & van Merriënboer, J. J. G. (1994). Variability of worked examples and transfer of geometrical problem-solving skills. *Journal of Educational Psychology*, 86(1), 122–133. •
Chi, M. T. H., Feltovich, P. J., & Glaser, R. (1981). Categorization and representation of physics problems by experts and novices. *Cognitive Science*, 5(2), 121–152.

**Feedback**
Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance. *Psychological Bulletin*, 119(2), 254–284. •
Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research*, 77(1), 81–112. •
Shute, V. J. (2008). Focus on formative feedback. *Review of Educational Research*, 78(1), 153–189. •
Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors: Lessons learned. *Journal of the Learning Sciences*, 4(2), 167–207.

**Mémoire et pratique**
Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255. •
Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest*, 14(1), 4–58. •
Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380. •
Bjork, E. L., & Bjork, R. A. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning.
