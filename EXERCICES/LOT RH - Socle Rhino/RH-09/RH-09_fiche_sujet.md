# RH-09 — Une pièce imprimable

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH5 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-016, REF-018 |
| **Compétence visée** | Vérifier qu'une pièce respecte les contraintes dimensionnelles d'une machine avant de la lancer. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-08 |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Vérifier qu'une pièce respecte les contraintes dimensionnelles d'une machine avant de la lancer.

### Contexte

L'imprimante du bureau accepte 220 × 220 × 250 mm et ne tient pas une paroi sous 1,2 mm.

### Énoncé

> La pièce fournie doit passer sur cette machine. Établissez le facteur d'échelle maximal qui la fait tenir dans le volume d'impression, arrondi au centième inférieur, et donnez-le.

### Ce qui vous est fourni

Un fichier Rhino contenant la pièce — 380 × 260 × 195 mm hors tout — et les cotes du volume d'impression.

### Ce qui est attendu

0,57 — le facteur limitant vient de la longueur : 220 ÷ 380 vaut 0,5789, arrondi vers le bas au centième.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-09_sujet.gh`

### Barème

1 point si le facteur est juste et arrondi vers le bas.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
