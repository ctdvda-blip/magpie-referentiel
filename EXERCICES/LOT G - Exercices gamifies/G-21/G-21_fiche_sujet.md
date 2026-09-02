# G-21 — Le golf de composants

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G5 · Performance et compétition |
| **Référence au référentiel** | REF-068, REF-043, REF-046 |
| **Compétence visée** | Produire une géométrie régulière par le chemin le plus économe, en cherchant le composant qui fait le travail de plusieurs. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | A-16, A-39 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Chercher la solution la plus économe, exercice d'élégance algorithmique.

### Contexte

Le golf de composants entraîne l'élégance, qui n'est pas une coquetterie : une définition de sept composants se relit, se transmet et se modifie, une de trente non.

### Énoncé

> Produis la géométrie cible avec le moins de composants possible. Le par du trou est fixé à 7 composants. Sliders et Panels comptent.

### Ce qui vous est fourni

Une géométrie cible en filigrane.

### Ce qui est attendu

1 582,75 mm — le périmètre de l'étoile à neuf branches, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-21_sujet.gh`

### Barème

Par 7 : 3 points au par, 5 points sous le par, 1 point au-dessus.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
