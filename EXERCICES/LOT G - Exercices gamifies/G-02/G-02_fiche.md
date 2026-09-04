# G-02 — La barre de progression

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G1 · Progression et récompense |
| **Référence au référentiel** | REF-062, REF-063 |
| **Compétence visée** | Construire cinq primitives distinctes et mesurer l'ensemble qu'elles forment, chaque forme étant un jalon. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | A-34 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 14 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Découper une tâche en jalons visibles pour soutenir l'effort.

### Contexte

La barre de progression soutient l'effort en découpant une tâche longue en jalons visibles. Sans elle, cinq formes à poser se vivent comme une seule tâche qui n'avance pas.

### Énoncé

> Reconstitue le logo en 5 étapes. Chaque forme correctement placée fait progresser la barre de 20 %. La barre passe au vert à 100 %.

### Ce qui vous est fourni

Un gabarit du logo en filigrane et une barre de progression pré-câblée.

### Ce qui est attendu

1 372,74 mm — la somme des cinq périmètres, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-02_sujet.gh`

### Barème

20 % par forme, validation à 100 %.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-02_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Identifier les 5 formes du gabarit : cercle, rectangle, triangle, hexagone, segment.

**Étape 2.** Construire chaque forme avec le composant natif adapté.

**Étape 3.** Positionner chaque forme sur son repère.

**Étape 4.** Brancher chaque forme sur l'entrée correspondante du groupe de contrôle.

**Étape 5.** Observer la barre progresser à chaque forme validée.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Prendre le côté du triangle et de l'hexagone pour leur périmètre : 936,74 au lieu de 1 372,74. Un polygone régulier de côté c a un périmètre de n×c, et l'erreur passe inaperçue tant qu'on ne compare pas le cercle aux autres.

### Pièges fréquents

- Formes correctes mais mal positionnées : le sous-critère reste rouge.
- Brancher toutes les formes sur une seule entrée.

### Pourquoi ce jeu de données

Cinq formes de familles différentes — cercle, rectangle, triangle, hexagone, segment — pour que la somme ne puisse pas se retrouver par une seule formule. Le cercle apporte π, ce qui rend le total non entier et donc non devinable.

### Limite de la correction automatique

> La somme des périmètres dit que les cinq formes ont la bonne TAILLE, pas qu'elles sont au bon endroit. Le positionnement sur le gabarit se juge à l'œil, et c'est le rôle de la barre.

### Pour aller plus loin

- Barre segmentée par chapitre.
- Ajouter un pourcentage chiffré.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-02_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-02_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-02.json` | Descripteur pour le plugin Magpie |
| `G-02_fiche.md` | La présente fiche |
| `G-02_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-02_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-02_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
