# G-15 — Le dessin à compléter

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G3 · Manipulation et adresse |
| **Référence au référentiel** | REF-063, REF-067 |
| **Compétence visée** | Reconstituer une figure par symétrie et la refermer, puis mesurer ce qu'on a produit. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 14 min |
| **Prérequis** | A-34, A-38 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Reconstituer une figure par déduction géométrique.

### Contexte

La silhouette à compléter fait travailler la déduction géométrique : ce qui manque se déduit de ce qui est là, sans cote supplémentaire.

### Énoncé

> La moitié gauche du motif est dessinée. Complète la moitié droite pour obtenir une figure parfaitement symétrique, puis referme le contour.

### Ce qui vous est fourni

Une demi-figure internalisée et un axe de symétrie.

### Ce qui est attendu

91 550 mm² d'aire et 1 098,42 mm de périmètre.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-15_sujet.gh`

### Barème

1 point pour la symétrie, 1 point pour la fermeture.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
