# B-17 — Coque à nervures depuis une surface libre

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B5 · Design produit |
| **Référence au référentiel** | REF-069, REF-101, REF-049 |
| **Compétence visée** | Mesurer le développé d'un élément courbe, et non sa corde. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | A-45, B-04 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 24 composants |
| **Gamification associée** | G-22 Boss de fin de chapitre |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Extraire des sections structurelles d'une forme libre et préparer leur fabrication.

### Contexte

Les nervures se débitent à plat puis se cintrent. C'est leur longueur développée qu'on commande.

### Énoncé

> Sur la coque libre fournie, extrais 9 nervures transversales espacées régulièrement, donne-leur 12 mm d'épaisseur et 60 mm de hauteur vers l'intérieur, puis prépare leur mise à plat.

### Ce qui vous est fourni

Une surface de coque internalisée.

### Ce qui est attendu

32,34 m de nervure au total, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-17_sujet.gh`

### Barème

2 points pour les nervures, 2 points pour la mise à plat.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
