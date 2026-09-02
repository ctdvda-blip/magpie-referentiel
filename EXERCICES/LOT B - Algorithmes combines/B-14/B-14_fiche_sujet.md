# B-14 — Numérotation et étiquetage automatiques

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B4 · Données, métrés et livrables |
| **Référence au référentiel** | REF-066, REF-081, REF-057 |
| **Compétence visée** | Ordonner des éléments selon un critère composé, en respectant l'ordre de priorité des critères. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 22 min |
| **Prérequis** | A-49, A-27 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 18 composants |
| **Gamification associée** | G-11 Mots croisés de composants |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire des repères lisibles, cohérents et positionnés dans le modèle.

### Contexte

Le repérage suit l'ordre de pose : rangée du bas d'abord, de gauche à droite. Le poseur lit les repères dans cet ordre-là.

### Énoncé

> Numérote les 14 pièces de l'assemblage de gauche à droite puis de bas en haut, au format R-A01 à R-A14, et place l'étiquette au centre de gravité de chaque pièce, orientée face à la vue de face.

### Ce qui vous est fourni

Un assemblage de 14 solides internalisés.

### Ce qui est attendu

7 — le rang de la pièce située à 800 mm en abscisse et 900 mm en ordonnée.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-14_sujet.gh`

### Barème

2 points pour l'ordre, 1 point pour le format, 1 point pour le placement.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
