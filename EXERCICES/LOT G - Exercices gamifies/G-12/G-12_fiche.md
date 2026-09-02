# G-12 — Le memory des composants

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G2 · Exploration et découverte |
| **Référence au référentiel** | REF-047, REF-051, REF-049 |
| **Compétence visée** | Associer chaque composant à son effet sur la structure des données, et exprimer l'appariement de façon exploitable. |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | A-20 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Associer chaque composant à son effet sur les données, par appariement.

### Contexte

Le memory fait travailler l'association plutôt que la définition. Savoir que `Graft` fait une branche par élément vaut mieux que savoir réciter sa description.

### Énoncé

> Douze cartes affichent d'un côté un nom de composant, de l'autre une structure de données avant/après. Reconstitue les six paires en indiquant les couples d'index.

### Ce qui vous est fourni

Douze cartes numérotées et douze structures de données affichées.

### Ce qui est attendu

Le partenaire de chaque carte, dans l'ordre des cartes : 8, 11, 6, 12, 9, 3, 10, 1, 5, 7, 2, 4.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-12_sujet.gh`

### Barème

6 points, 1 par paire.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-12_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Analyser chaque structure avec le Param Viewer fourni.

**Étape 2.** Identifier l'opération réalisée entre l'état avant et l'état après.

**Étape 3.** Associer cette opération au nom de composant correspondant.

**Étape 4.** Saisir les six couples dans le Panel de réponse, index le plus petit en premier.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Rendre les six paires comme six couples, dans un ordre libre. L'ordre libre n'est pas comparable — deux apprenants justes rendraient deux listes différentes. La forme demandée, un partenaire PAR CARTE, est unique par construction.

### Pièges fréquents

- Confondre Graft et Simplify sur la carte 5.
- Saisir les couples dans un ordre interne inversé.

### Pourquoi ce jeu de données

Douze cartes, six paires, aucune carte appariée avec sa voisine immédiate : la liste des partenaires ne présente aucune régularité, et se lit comme une permutation involutive — chaque carte est le partenaire de son partenaire.

### Limite de la correction automatique

> L'appariement se vérifie, la MÉMOIRE non. Un apprenant qui retourne les douze cartes et les compare une à une obtient le même résultat que celui qui les a retenues.

### Pour aller plus loin

- Memory chronométré.
- Memory à trois cartes par famille (nom, icône, effet).

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-12_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-12_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-12.json` | Descripteur pour le plugin Magpie |
| `G-12_fiche.md` | La présente fiche |
| `G-12_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-12_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-12_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
