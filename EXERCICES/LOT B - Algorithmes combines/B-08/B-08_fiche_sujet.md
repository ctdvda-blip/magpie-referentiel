# B-08 — Étagère modulaire à pas variable

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B2 · Design de mobilier |
| **Référence au référentiel** | REF-043, REF-044, REF-047 |
| **Compétence visée** | Répartir des éléments selon une progression imposée en respectant une hauteur totale et une valeur de départ. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 22 min |
| **Prérequis** | A-13, A-10 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 16 composants |
| **Gamification associée** | G-08 Combo / série |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Répartir des tablettes selon une progression non uniforme pilotée par une courbe.

### Contexte

Une bibliothèque range des livres de plus en plus grands vers le haut. La hauteur totale, elle, ne bouge pas.

### Énoncé

> Répartis 6 tablettes sur une hauteur de 2 000 mm de sorte que les entre-deux augmentent progressivement du bas vers le haut, la plus petite hauteur libre valant au moins 220 mm.

### Ce qui vous est fourni

Un slider de hauteur totale et un slider de nombre de tablettes.

### Ce qui est attendu

353,71 mm — le plus grand entre-deux, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-08_sujet.gh`

### Barème

2 points pour la répartition, 1 point pour la contrainte de 220 mm.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
