# B-05 — Poutre treillis paramétrique

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B1 · Architecture et construction |
| **Référence au référentiel** | REF-046, REF-063, REF-079 |
| **Compétence visée** | Chiffrer le linéaire d'une structure treillis en distinguant ce qui court le long de la portée de ce qui la traverse en diagonale. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-16, A-47 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 22 composants |
| **Gamification associée** | G-21 Golf de composants |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Construire une structure par décalage de listes et produire directement son métré.

### Contexte

Le tube se commande au mètre. Une diagonale n'a pas la longueur du panneau qu'elle traverse.

### Énoncé

> Produis une poutre treillis Warren de 12 000 mm de portée et 900 mm de hauteur, avec 8 panneaux. Affiche le linéaire total de tube nécessaire, membrures et diagonales séparées.

### Ce qui vous est fourni

Trois sliders : portée, hauteur, nombre de panneaux.

### Ce qui est attendu

37,99 m de tube pour les membrures et les diagonales, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-05_sujet.gh`

### Barème

2 points pour la géométrie, 2 points pour les deux linéaires.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
