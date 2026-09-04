# B-13 — Calepinage de plaques et calcul de chute

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B4 · Données, métrés et livrables |
| **Référence au référentiel** | REF-113, REF-082, REF-045 |
| **Compétence visée** | Estimer un taux de chute à partir des surfaces, en sachant que c'est un MINORANT et pourquoi. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 28 min |
| **Prérequis** | B-12, A-15 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 20 composants |
| **Gamification associée** | G-23 Duel et classement |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Optimiser un débit et quantifier la perte matière.

### Contexte

La plaque se commande à l'unité. Le taux de chute décide de la marge, et il est toujours annoncé optimiste.

### Énoncé

> Les 22 pièces rectangulaires fournies doivent être débitées dans des plaques de 2 800 × 2 070 mm. Calcule le nombre de plaques nécessaires et le taux de chute en pourcentage.

### Ce qui vous est fourni

Une liste de 22 rectangles et les dimensions de plaque.

### Ce qui est attendu

31,00 % de chute, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-13_sujet.gh`

### Barème

2 points pour le calepinage, 1 point pour le nombre de plaques, 1 point pour le taux de chute.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
