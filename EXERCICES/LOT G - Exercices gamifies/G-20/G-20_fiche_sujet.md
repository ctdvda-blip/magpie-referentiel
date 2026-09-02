# G-20 — La chasse aux bugs

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G4 · Connaissance et mémorisation |
| **Référence au référentiel** | REF-041, REF-053, REF-055 |
| **Compétence visée** | Diagnostiquer une définition qui produit un résultat plausible mais faux, sans en changer la structure. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | A-07, A-09, A-24 |
| **Mode de validation** | NumericTolerance — tolérance 1 |
| **Solution de référence** | 30 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Développer le réflexe de diagnostic sur une définition qui ne produit pas le résultat attendu.

### Contexte

Une définition qui plante se répare ; une définition qui rend six modules au lieu de vingt-quatre se livre. C'est le second cas qui coûte cher, et c'est celui-là qu'on entraîne.

### Énoncé

> Cette définition devrait produire 24 modules, elle n'en produit que 6. Trois défauts se cachent dans le graphe. Identifie-les et corrige la définition sans en changer la structure générale.

### Ce qui vous est fourni

Une définition fautive de 30 composants.

### Ce qui est attendu

2 306 400 mm² — l'aire totale des 24 modules retrouvés.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-20_sujet.gh`

### Barème

3 points, 1 par défaut corrigé.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
