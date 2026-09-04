# RH-16 — La surface d'un rampant

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Modélisation Rhino |
| **Référence au référentiel** | REF-010, REF-011 |
| **Compétence visée** | Mesurer une surface inclinée dans son plan, et non dans sa projection horizontale. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-15 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mesurer une surface inclinée dans son plan, et non dans sa projection horizontale.

### Contexte

On commande la couverture d'un appentis : le couvreur pose sur le rampant, le plan le montre en projection.

### Énoncé

> L'appentis mesure 8 400 mm de long, 3 200 mm de profondeur en projection, pour un dénivelé de 1 500 mm. Donnez la surface de couverture à commander, en mètres carrés.

### Ce qui vous est fourni

La longueur, la profondeur en projection et le dénivelé.

### Ce qui est attendu

29,69 m² — la surface du rampant, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-16_sujet.gh`

### Barème

1 point si la surface du rampant est juste à 0,01 m² près.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
