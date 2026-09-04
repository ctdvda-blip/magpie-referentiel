# G-01 — Le tableau des scores

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G1 · Progression et récompense |
| **Référence au référentiel** | REF-047, REF-043 |
| **Compétence visée** | Trier une liste et lire le score que le tri produit, en distinguant ce qui est compté de ce qui est trié. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 10 min |
| **Prérequis** | A-10 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Rendre visible la performance immédiate de l'apprenant sur une tâche de tri.

### Contexte

Le tableau des scores rend la performance immédiate. Il ne récompense pas l'effort mais le résultat, et l'apprenant le voit avant de soumettre.

### Énoncé

> Trie les 12 valeurs par ordre croissant. Chaque valeur correctement placée rapporte 10 points, chaque valeur mal placée en coûte 5. Le score s'affiche en direct dans le panneau SCORE.

### Ce qui vous est fourni

Une liste de 12 nombres mélangés et un groupe SCORE pré-câblé.

### Ce qui est attendu

Les douze valeurs triées : 61, 132, 168, 274, 389, 458, 502, 596, 725, 847, 913, 941.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-01_sujet.gh`

### Barème

120 points maximum, validation à 120.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-01_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Sort List sur la liste fournie.

**Étape 2.** Brancher la sortie sur le paramètre de réponse attendu par Magpie.

**Étape 3.** Le groupe SCORE compare position par position et cumule les points.

**Étape 4.** Le score atteint 120 lorsque les 12 valeurs sont bien placées.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Trier une COPIE de la liste sans la rebrancher sur le paramètre de réponse. Le canvas affiche alors une liste triée, le score reste à zéro, et rien n'indique pourquoi — c'est le défaut le plus fréquent du lot, et le tableau des scores est justement là pour le rendre visible en une seconde.

### Pièges fréquents

- Trier une copie de la liste sans la rebrancher sur le paramètre de réponse.
- Score partiel accepté comme réussite : le seuil de validation reste à 100 %.

### Pourquoi ce jeu de données

Douze valeurs de 61 à 941, sans ordre ni régularité : aucune ne se devine, et le tri doit être fait. Le score de 120 n'est atteint qu'à douze bonnes places sur douze — un score partiel n'est pas une réussite partielle.

### Limite de la correction automatique

> Le score mesure le RÉSULTAT, pas la méthode. Trier douze valeurs à la main dans un panneau donne le même score que `Sort List`, et ne s'effondre qu'au treizième.

### Pour aller plus loin

- Introduire un malus de temps.
- Afficher un score cumulé sur tout le parcours.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-01_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-01_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-01.json` | Descripteur pour le plugin Magpie |
| `G-01_fiche.md` | La présente fiche |
| `G-01_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-01_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-01_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
