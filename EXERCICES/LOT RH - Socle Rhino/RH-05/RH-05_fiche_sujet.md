# RH-05 — Percer une platine dans Rhino

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Modélisation Rhino |
| **Référence au référentiel** | REF-012 |
| **Compétence visée** | Combiner des solides par soustraction dans Rhino et quantifier la matière retirée. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | RH-04 |
| **Mode de validation** | NumericTolerance — tolérance 1 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-11 Chasse à l'erreur |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Combiner des solides par soustraction dans Rhino et quantifier la matière retirée.

### Contexte

Une platine d'assemblage reçoit quatre boulons ; la matière retirée entre dans le bilan de poids.

### Énoncé

> La platine mesure 300 × 200 × 15 mm. Percez-la de quatre trous traversants de 18 mm de diamètre, centrés à 40 mm de chaque bord. Donnez le volume de matière retirée, en millimètres cubes.

### Ce qui vous est fourni

Un fichier Rhino contenant la platine pleine.

### Ce qui est attendu

Une valeur : le volume de matière retirée, en millimètres cubes.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-05_sujet.gh`

### Barème

1 point si le volume retiré est juste à 1 mm³ près.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
