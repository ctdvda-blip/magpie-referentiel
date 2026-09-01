# A-12 — Longueur et bornes d'une liste

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A3 · Listes |
| **Référence au référentiel** | REF-043 |
| **Compétence visée** | Caractériser un lot par son effectif et ses valeurs extrêmes. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | A-11 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-21 Golf de composants |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Caractériser un lot par son effectif et ses valeurs extrêmes.

### Contexte

Un lot de placage est contrôlé en épaisseur avant mise en presse.

### Énoncé

> Les épaisseurs relevées sur le lot vous sont fournies, en centièmes de millimètre. Produisez, dans cet ordre, l'effectif du lot, l'épaisseur la plus faible et l'épaisseur la plus forte.

### Ce qui vous est fourni

Les 28 épaisseurs relevées sur le lot, en centièmes de millimètre.

### Ce qui est attendu

Trois valeurs, dans cet ordre : 28, 51, 78.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-12_sujet.gh`

### Barème

1 point si les trois valeurs sont exactes et dans l'ordre.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-12_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser List Length pour l'effectif.

**Étape 2.** Poser Bounds (Maths > Domain) puis Deconstruct Domain pour obtenir min et max.

**Étape 3.** Assembler les trois valeurs avec Merge dans le bon ordre.

**Étape 4.** Relier vers un Panel.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Trier la liste puis lire les extrémités à l'œil : la réponse est juste, mais le montage ne suit plus si le lot change. La difficulté est ici de résister au contournement, pas de trouver le composant.

### Pièges fréquents

- Merge respecte l'ordre de branchement des entrées : vérifier l'ordre.
- Utiliser Sort List et lire le premier et le dernier élément fonctionne aussi mais coûte plus de composants.

### Pourquoi ce jeu de données

28 valeurs dispersées entre 51 et 78, sans ordre : les extrêmes ne sautent pas aux yeux et doivent être extraits par construction.

### Pour aller plus loin

- Ajouter la moyenne avec Average.
- Afficher l'index du minimum avec Sort List et List Item.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-12_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-12_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-12.json` | Descripteur pour le plugin Magpie |
| `A-12_fiche.md` | La présente fiche |
| `A-12_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-12_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-12_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
