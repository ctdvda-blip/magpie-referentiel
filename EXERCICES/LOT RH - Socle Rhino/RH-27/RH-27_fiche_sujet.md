# RH-27 — Le volume d'un assemblage de primitives

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Modélisation Rhino |
| **Référence au référentiel** | REF-007, REF-008 |
| **Compétence visée** | Chiffrer la matière d'un assemblage de primitives en déduisant ce qu'elles ont en commun. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 16 min |
| **Prérequis** | RH-05 |
| **Mode de validation** | NumericTolerance — tolérance 0.0001 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-14 Le puzzle de câblage |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Chiffrer la matière d'un assemblage de primitives en déduisant ce qu'elles ont en commun.

### Contexte

Un socle et son fût se commandent au volume de matière. Les deux se recouvrent là où le second s'encastre dans le premier, et cette matière-là n'existe qu'une fois.

### Énoncé

> Le socle mesure 240 × 160 × 40 mm. Le fût cylindrique fait 45 mm de rayon et 120 mm de haut, et s'encastre de 15 mm dans le socle. Donnez le volume de matière, en décimètres cubes.

### Ce qui vous est fourni

Les cotes du socle, celles du fût et la profondeur d'encastrement.

### Ce qui est attendu

2,2040 dm³ de matière, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-27_sujet.gh`

### Barème

1 point si le volume est juste à 0,0001 dm³.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
