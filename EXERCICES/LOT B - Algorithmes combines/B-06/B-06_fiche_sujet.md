# B-06 — Caisson de meuble avec épaisseur et rainures

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B2 · Design de mobilier |
| **Référence au référentiel** | REF-070, REF-071, REF-068 |
| **Compétence visée** | Chiffrer la matière d'un assemblage en tenant compte des recouvrements et des usinages qui la font varier. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | A-43, A-44 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 26 composants |
| **Gamification associée** | G-06 Niveaux et déblocage |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Modéliser un assemblage menuisé où toutes les cotes dérivent de trois paramètres.

### Contexte

Le panneau se commande au mètre carré débité. La rainure n'enlève pas de matière au fond : elle lui en AJOUTE, puisqu'il faut le débiter plus grand.

### Énoncé

> Modélise un caisson de largeur L, hauteur H et profondeur P, en panneaux de 19 mm. Les joues reçoivent une rainure de 6 mm de profondeur pour le fond de 8 mm. Le dessus et le dessous s'insèrent entre les joues.

### Ce qui vous est fourni

Trois sliders L, H, P et un slider d'épaisseur.

### Ce qui est attendu

32,73 dm³ de panneau, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-06_sujet.gh`

### Barème

3 points pour l'assemblage, 1 point pour la rainure correcte.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
