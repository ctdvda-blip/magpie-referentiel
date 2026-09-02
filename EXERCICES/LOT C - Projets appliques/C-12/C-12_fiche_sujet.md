# C-12 — Imbrication et export de fabrication

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C4 · Fabrication |
| **Référence au référentiel** | REF-113, REF-114, REF-087 |
| **Compétence visée** | Chiffrer un débit en tenant compte des espacements et des bords perdus, et en tirer un taux de chute défendable. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 75 min |
| **Prérequis** | B-13, C-05 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 38 composants |
| **Gamification associée** | G-21 Golf de composants + G-23 Classement |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Boucler la chaîne conception-fabrication avec un livrable machine.

### Contexte

La plaque se commande à l'unité et le taux de chute figure au devis. Il engage l'entreprise.

### Énoncé

> Imbrique les 46 pièces découpées fournies dans des plaques de 3 000 × 1 500 mm avec un espacement de 8 mm entre pièces et 15 mm de bord de plaque. Produis le plan de découpe repéré, le nombre de plaques et le taux de matière utile, puis exporte en DXF par plaque.

### Ce qui vous est fourni

46 contours de pièces internalisés.

### Ce qui est attendu

27,36 % de chute, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-12_sujet.gh`

### Barème

4 points imbrication, 3 points indicateurs, 3 points export.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
