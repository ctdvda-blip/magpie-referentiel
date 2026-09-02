# G-14 — Le puzzle de câblage

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G3 · Manipulation et adresse |
| **Référence au référentiel** | REF-027, REF-048 |
| **Compétence visée** | Rétablir un câblage à partir du seul résultat attendu, en lisant les types d'entrée et de sortie. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | A-01, A-19 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Travailler la lecture des entrées et sorties d'un composant.

### Contexte

Un câblage se lit avant de s'écrire. Le puzzle enlève les câbles et laisse les composants : ce qui reste à trouver est exactement ce qu'on ne voit pas quand on recopie un tutoriel.

### Énoncé

> Six composants sont posés sur le canvas, tous les câbles ont été supprimés. Rétablis le câblage pour reproduire la géométrie affichée en filigrane, sans ajouter ni supprimer aucun composant.

### Ce qui vous est fourni

Six composants dispersés, aucun câble, une géométrie cible en filigrane.

### Ce qui est attendu

2 033,29 mm — la longueur du contour fermé, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-14_sujet.gh`

### Barème

1 point pour la géométrie, 1 point pour le respect du nombre de composants.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
