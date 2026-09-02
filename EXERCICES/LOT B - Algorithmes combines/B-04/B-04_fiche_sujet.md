# B-04 — Pavage hexagonal sur surface

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B1 · Architecture et construction |
| **Référence au référentiel** | REF-068, REF-069, REF-049 |
| **Compétence visée** | Établir combien d'éléments d'une trame non orthogonale tiennent dans une emprise donnée. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 28 min |
| **Prérequis** | B-03, A-20 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 20 composants |
| **Gamification associée** | G-22 Boss de fin de chapitre |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Projeter une trame plane sur une surface libre en maîtrisant la structure de données.

### Contexte

Le bardage hexagonal se commande à l'unité. Le pas d'une trame hexagonale n'est pas son côté.

### Énoncé

> Applique un pavage hexagonal de 400 mm de côté sur la surface libre fournie, puis extrude chaque hexagone de 60 mm suivant la normale locale de la surface.

### Ce qui vous est fourni

Une surface libre internalisée.

### Ce qui est attendu

130 hexagones.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-04_sujet.gh`

### Barème

2 points pour le pavage, 2 points pour l'orientation selon les normales.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
