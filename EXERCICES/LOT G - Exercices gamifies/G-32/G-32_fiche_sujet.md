# G-32 — Les indices payants

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G7 · Régularité et communauté |
| **Référence au référentiel** | REF-052, REF-049, REF-050 |
| **Compétence visée** | Restructurer un arbre pour atteindre une structure imposée, et savoir décrire cette structure par ses effectifs. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | A-20, A-21, A-23 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Responsabiliser l'apprenant sur le recours à l'aide.

### Contexte

L'économie d'indices responsabilise : demander de l'aide a un coût, ne pas en demander quand on est bloqué en a un autre. L'apprenant apprend à arbitrer, ce qui est le vrai sujet.

### Énoncé

> Restructure l'arbre fourni pour atteindre la structure cible. Quatre indices sont disponibles, du plus général au plus précis, coûtant respectivement 1, 2, 3 et 4 points sur un total de 12.

### Ce qui vous est fourni

Un arbre source, une structure cible affichée et quatre groupes d'indices repliés.

### Ce qui est attendu

La structure cible, branche par branche : 4, 1, 0, 3, 2, 2, 3, 2, 2.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-32_sujet.gh`

### Barème

12 points, moins le coût des indices consultés.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
