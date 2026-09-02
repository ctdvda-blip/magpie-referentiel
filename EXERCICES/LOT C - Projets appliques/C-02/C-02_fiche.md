# C-02 — Résille structurelle sur plan libre

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C1 · Architecture |
| **Référence au référentiel** | REF-069, REF-094, REF-074, REF-049 |
| **Compétence visée** | Chiffrer le linéaire d'une structure triangulée en n'oubliant aucune des trois familles de barres. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 90 min |
| **Prérequis** | B-04, C-01 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 50 composants |
| **Gamification associée** | G-25 Animation de la relaxation |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Générer une structure maillée relaxée et en extraire les données de fabrication.

### Contexte

La résille se chiffre au mètre de barre avant d'être relaxée. C'est ce chiffre qui décide si le projet passe le budget.

### Énoncé

> Sur le contour libre fourni, génère une toiture en résille triangulée, relaxe-la par Kangaroo pour obtenir une forme en équilibre de traction, puis produis la nomenclature des barres regroupées par longueur à 5 mm près et la liste des nœuds avec leur nombre de branches.

### Ce qui vous est fourni

Un contour fermé et trois points d'appui internalisés.

### Ce qui est attendu

695,53 m de barres, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-02_sujet.gh`

### Barème

4 points structure, 3 points nomenclature barres, 3 points nomenclature nœuds.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `C-02_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Mailler le contour avec Mesh Surface ou Delaunay Mesh.

**Étape 2.** Extraire les arêtes du maillage avec Deconstruct Mesh et Mesh Edges.

**Étape 3.** Configurer Kangaroo : Length goal sur les arêtes, Anchor sur les appuis, Load vertical.

**Étape 4.** Lancer la relaxation jusqu'à convergence et figer le résultat.

**Étape 5.** Mesurer la longueur de chaque arête avec Length.

**Étape 6.** Regrouper les longueurs par tranche de 5 mm avec une division, un Round et un Create Set.

**Étape 7.** Compter les occurrences de chaque groupe avec Member Index.

**Étape 8.** Compter le nombre d'arêtes par sommet pour caractériser les nœuds.

**Étape 9.** Produire les deux tableaux et les exporter.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Oublier les diagonales : 424 m. Or ce sont elles qui TRIANGULENT — sans elles la résille n'est pas une structure, c'est une grille articulée. Elles pèsent 271 m, soit 39 % du total, et leur oubli fait passer le projet pour deux fois moins cher qu'il n'est.

### Pièges fréquents

- Relaxation non figée : le résultat change à chaque recalcul et la nomenclature devient instable.
- Regroupement par arrondi au plus proche : deux barres de 102 et 108 mm tombent dans des groupes différents alors qu'elles sont à 6 mm l'une de l'autre.
- Arêtes comptées deux fois car partagées par deux faces.

### Pourquoi ce jeu de données

Une maille de 2 000 mm sur 24 × 16 m donne 12 × 8 panneaux. La diagonale d'une maille carrée vaut √2 fois son côté : les diagonales pèsent donc plus que les horizontales, ce qui est contre-intuitif et rend leur oubli d'autant plus coûteux.

### Limite de la correction automatique

> Le linéaire est celui de la résille PLANE. La relaxation la déforme, et les barres s'allongent — de quelques pour cent selon la flèche obtenue. Le chiffrage se refait après relaxation.

### Pour aller plus loin

- Comparer une résille triangulée et une résille quadrangulaire.
- Ajouter une contrainte de longueur maximale de barre.
- Générer les platines de nœud.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `C-02_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `C-02_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `C-02.json` | Descripteur pour le plugin Magpie |
| `C-02_fiche.md` | La présente fiche |
| `C-02_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `C-02_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `C-02_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
