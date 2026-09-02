# C-06 — Chaise à assise en lamelles courbes

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C2 · Design de mobilier |
| **Référence au référentiel** | REF-069, REF-064, REF-074 |
| **Compétence visée** | Vérifier qu'une forme voulue respecte une contrainte de matière, en comparant un rayon obtenu à un rayon admissible. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 85 min |
| **Prérequis** | B-16, B-17 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 42 composants |
| **Gamification associée** | G-26 Feedback visuel + G-07 Étoiles |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Conjuguer une forme ergonomique libre et une contrainte de fabrication en lamelles droites.

### Contexte

Une lamelle de contreplaqué cintrée trop serré casse au pressage. Le rapport rayon sur épaisseur est ce que l'atelier regarde.

### Énoncé

> Modélise l'assise et le dossier d'une chaise en 22 lamelles de 40 mm de large et 8 mm d'épaisseur suivant deux courbes directrices. Le rayon de courbure de chaque lamelle ne doit jamais descendre sous 350 mm, limite de cintrage du matériau : signale toute lamelle non conforme.

### Ce qui vous est fourni

Deux courbes directrices internalisées.

### Ce qui est attendu

371,73 mm — le rayon de la directrice, à 0,01 près, à comparer aux 200 mm admissibles.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-06_sujet.gh`

### Barème

4 points géométrie, 3 points contrôle de courbure, 3 points conformité générale.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
