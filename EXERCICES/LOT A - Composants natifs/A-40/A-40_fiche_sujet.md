# A-40 — Mise à l'échelle

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A9 · Transformations et réseaux |
| **Référence au référentiel** | REF-067 |
| **Compétence visée** | Mettre à l'échelle une géométrie, en maîtrisant le centre et en distinguant l'échelle uniforme de l'échelle par direction. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-39 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-04 Système de vies |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mettre à l'échelle une géométrie, en maîtrisant le centre et en distinguant l'échelle uniforme de l'échelle par direction.

### Contexte

Un profil de menuiserie est décliné en une version réduite et une version surhaussée, sans changer sa largeur de passage.

### Énoncé

> Le profil vous est fourni. Produisez d'abord une version réduite à 60 % autour de son propre centre de gravité, puis une version deux fois plus haute dont la largeur reste inchangée.

### Ce qui vous est fourni

Un profil fermé internalisé.

### Ce qui est attendu

Un profil réduit centré et un profil étiré verticalement.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-40_sujet.gh`

### Barème

1 point par mise à l'échelle correcte.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
