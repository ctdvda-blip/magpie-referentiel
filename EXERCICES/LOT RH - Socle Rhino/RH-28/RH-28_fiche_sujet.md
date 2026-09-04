# RH-28 — La surface d'une extrusion

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Modélisation Rhino |
| **Référence au référentiel** | REF-009, REF-010, REF-011 |
| **Compétence visée** | Établir la surface développée d'une extrusion à partir du périmètre de son contour, refermé. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 14 min |
| **Prérequis** | RH-04 |
| **Mode de validation** | NumericTolerance — tolérance 0.0001 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-14 Le puzzle de câblage |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir la surface développée d'une extrusion à partir du périmètre de son contour, refermé.

### Contexte

Le bardage d'un local technique se commande au mètre carré. Sa surface est celle du contour au sol, développé sur la hauteur.

### Énoncé

> Le contour au sol vous est donné par ses cinq sommets, en millimètres. Le bardage monte à 2 600 mm. Donnez sa surface, en mètres carrés.

### Ce qui vous est fourni

Les cinq sommets du contour et la hauteur de bardage.

### Ce qui est attendu

15,7566 m² de bardage, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-28_sujet.gh`

### Barème

1 point si la surface est juste à 0,0001 m².

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
