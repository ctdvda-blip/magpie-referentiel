# RH-04 — Du profil à la surface

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Modélisation Rhino |
| **Référence au référentiel** | REF-009, REF-010, REF-011 |
| **Compétence visée** | Passer d'une courbe tracée dans Rhino à une surface, et contrôler la grandeur obtenue. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-03 |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Passer d'une courbe tracée dans Rhino à une surface, et contrôler la grandeur obtenue.

### Contexte

Un bardage courbe se chiffre à la surface développée ; le tracé vient d'un relevé, la surface doit en découler.

### Énoncé

> Le relevé fournit la ligne au sol du bardage. Produisez la surface du bardage en la montant de 2 800 mm à la verticale, puis donnez sa surface en mètres carrés.

### Ce qui vous est fourni

Un fichier Rhino contenant la courbe de relevé au sol.

### Ce qui est attendu

La surface du bardage, en mètres carrés, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-04_sujet.gh`

### Barème

1 point si la surface est juste à 0,01 m² près.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
