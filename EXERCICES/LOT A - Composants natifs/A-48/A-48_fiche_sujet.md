# A-48 — Courbure et point le plus proche

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A11 · Mesures géométriques |
| **Référence au référentiel** | REF-080 |
| **Compétence visée** | Analyser localement une courbe pour y localiser la zone la plus contraignante. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-35 |
| **Mode de validation** | NumericTolerance — tolérance 1 % |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-28 Avatar et personnalisation |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Analyser localement une courbe pour y localiser la zone la plus contraignante.

### Contexte

Un profilé cintré ne peut descendre sous un rayon de cintrage minimal : c'est le point le plus serré du tracé qui décide de la faisabilité.

### Énoncé

> Le tracé vous est fourni. Localisez son point le plus serré et donnez le rayon de cintrage à cet endroit.

### Ce qui vous est fourni

Une courbe libre internalisée.

### Ce qui est attendu

Le point de courbure maximale et son rayon de courbure.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 1 %.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-48_sujet.gh`

### Barème

1 point pour le point, 1 point pour le rayon.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
