# A-12 — Longueur et bornes d'une liste

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A3 · Listes |
| **Référence au référentiel** | REF-043 |
| **Compétence visée** | Caractériser un lot par son effectif et ses valeurs extrêmes. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | A-11 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-21 Golf de composants |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Caractériser un lot par son effectif et ses valeurs extrêmes.

### Contexte

Un lot de placage est contrôlé en épaisseur avant mise en presse.

### Énoncé

> Les épaisseurs relevées sur le lot vous sont fournies, en centièmes de millimètre. Produisez, dans cet ordre, l'effectif du lot, l'épaisseur la plus faible et l'épaisseur la plus forte.

### Ce qui vous est fourni

Les 28 épaisseurs relevées sur le lot, en centièmes de millimètre.

### Ce qui est attendu

Trois valeurs, dans cet ordre : 28, 51, 78.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-12_sujet.gh`

### Barème

1 point si les trois valeurs sont exactes et dans l'ordre.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
