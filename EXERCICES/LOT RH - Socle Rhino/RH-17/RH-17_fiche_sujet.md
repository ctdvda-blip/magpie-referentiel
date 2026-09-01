# RH-17 — Le volume de deux blocs qui se recouvrent

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Modélisation Rhino |
| **Référence au référentiel** | REF-012 |
| **Compétence visée** | Calculer le volume d'une réunion de solides sans compter deux fois la matière commune. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-05 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Calculer le volume d'une réunion de solides sans compter deux fois la matière commune.

### Contexte

Deux massifs de béton se recoupent en angle. On commande le béton au volume.

### Énoncé

> Le premier massif mesure 400 × 300 × 200 mm, le second 250 × 350 × 180 mm, et leur recouvrement 150 × 200 × 180 mm. Donnez le volume de béton, en décimètres cubes.

### Ce qui vous est fourni

Les dimensions des deux massifs et celles de leur recouvrement.

### Ce qui est attendu

34,35 dm³ — la réunion des deux massifs.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-17_sujet.gh`

### Barème

1 point si le volume de la réunion est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
