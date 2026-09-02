# G-10 — Le coffre à butin

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G2 · Exploration et découverte |
| **Référence au référentiel** | REF-068, REF-045 |
| **Compétence visée** | Identifier les extrêmes d'un jeu de valeurs et en rendre les INDEX plutôt que les valeurs. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 14 min |
| **Prérequis** | A-14, A-39 |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Introduire une part d'aléatoire maîtrisé pour renouveler l'intérêt.

### Contexte

Le coffre à butin introduit une part d'aléatoire maîtrisé : le contenu change à chaque tirage, la méthode pour le trouver non. C'est ce qui permet de rejouer l'exercice.

### Énoncé

> Vingt coffres sont disposés en trame. Trois contiennent une récompense, désignés par le tirage aléatoire de graine 7. Identifie-les et affiche leurs index.

### Ce qui vous est fourni

Une trame de 20 positions et un Random de graine imposée.

### Ce qui est attendu

Les index des trois coffres pleins : 7, 13, 16.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SetEquality**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-10_sujet.gh`

### Barème

3 points, 1 par coffre correctement identifié.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
