# B-01 — Escalier droit paramétrique

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B1 · Architecture et construction |
| **Référence au référentiel** | REF-067, REF-068, REF-047, REF-043 |
| **Compétence visée** | Dimensionner un ouvrage dont le nombre d'éléments est un ENTIER imposé par une contrainte de confort, et recaler les dimensions réelles sur cet entier. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-37, A-39, A-10 |
| **Mode de validation** | NumericTolerance — tolérance 0.1 |
| **Solution de référence** | 18 composants |
| **Gamification associée** | G-02 Barre de progression + G-26 Feedback visuel |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Chaîner série, transformation et extrusion pour produire un ouvrage réglementé par un calcul.

### Contexte

L'escalier relie deux niveaux dont la distance est donnée : c'est le nombre de contremarches qui s'ajuste, jamais la hauteur d'étage.

### Énoncé

> Produis un escalier droit reliant deux niveaux distants de H = 2 850 mm. Le giron est fixé à 280 mm et la hauteur de marche doit rester comprise entre 165 et 180 mm. Détermine automatiquement le nombre de marches et vérifie la règle de Blondel (2h + g compris entre 600 et 650 mm).

### Ce qui vous est fourni

Deux Number Slider (H = 2850, giron = 280) et un Panel de contrôle.

### Ce qui est attendu

615,29 mm — la valeur de Blondel, à 0,1 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-01_sujet.gh`

### Barème

2 points pour la géométrie, 1 point pour le nombre de marches, 1 point pour le contrôle de Blondel.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-01_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Diviser H par 172,5 (hauteur moyenne visée) puis arrondir avec Round : on obtient le nombre de contremarches.

**Étape 2.** Recalculer la hauteur réelle h = H / nombre de contremarches.

**Étape 3.** Générer avec Series les positions verticales (0 à H, pas h) et horizontales (0 à n×giron, pas giron).

**Étape 4.** Construire le vecteur de déplacement de chaque marche avec Construct Point puis Vector 2Pt.

**Étape 5.** Poser le rectangle de marche (giron × largeur) et le déplacer par la liste de vecteurs.

**Étape 6.** Extruder chaque marche de l'épaisseur choisie.

**Étape 7.** Calculer 2h + g et le contrôler avec deux Larger Than et un Gate And : afficher CONFORME ou NON CONFORME.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Garder la hauteur de marche VISÉE (172,5 mm) au lieu de la recalculer sur le nombre entier de contremarches. Blondel donne alors 625 mm, également dans la plage admise — l'escalier semble conforme, et il n'atteint pas l'étage : 17 × 172,5 fait 2 932 mm pour 2 850 disponibles.

### Pièges fréquents

- Confondre nombre de marches et nombre de contremarches : il y a toujours une contremarche de plus.
- Arrondir la hauteur de marche au lieu de recalculer h à partir du nombre entier de contremarches.
- Oublier que la dernière marche est confondue avec le plancher haut.

### Pourquoi ce jeu de données

2 850 ÷ 172,5 vaut 16,52 : l'arrondi au plus proche donne 17 contremarches, d'où une hauteur réelle de 167,65 mm — sous la valeur visée, et toujours dans la plage 165-180. Les deux valeurs de Blondel, 615,29 et 625, tiennent toutes deux dans l'intervalle admis : le contrôle réglementaire ne rattrape pas l'erreur.

### Limite de la correction automatique

> L'exercice valide Blondel. Il ne dit rien de l'échappée, de la largeur de passage ni du garde-corps — trois contraintes qui peuvent condamner un escalier par ailleurs conforme.

### Pour aller plus loin

- Ajouter un limon latéral suivant la ligne de foulée.
- Passer en escalier à volée tournante avec un Polar Array partiel.
- Sortir une nomenclature des marches vers CSV.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-01_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-01_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-01.json` | Descripteur pour le plugin Magpie |
| `B-01_fiche.md` | La présente fiche |
| `B-01_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-01_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-01_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
