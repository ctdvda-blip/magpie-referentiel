# GP-11 — L'ordre des opérations

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP2 · Synthèse géométrie |
| **Référence au référentiel** | REF-148 |
| **Compétence visée** | Établir qu'une suite d'opérations géométriques ne commute pas, et chiffrer ce que l'ordre change. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | GP-10 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 10 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir qu'une suite d'opérations géométriques ne commute pas, et chiffrer ce que l'ordre change.

### Contexte

Le contour part à la découpe. Il doit être congé de 120 mm et décalé de 40 mm vers l'extérieur pour la surcote d'usinage.

### Énoncé

> Le contour est un rectangle de 1 800 × 900 mm. Il faut le congéer d'un rayon de 120 mm et le décaler de 40 mm vers l'extérieur. Donnez l'écart de périmètre entre les deux ordres possibles, en millimètres.

### Ce qui vous est fourni

Les dimensions du rectangle, le rayon de congé et la valeur du décalage.

### Ce qui est attendu

68,67 mm d'écart entre les deux ordres, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-11_sujet.gh`

### Barème

1 point si l'écart est juste à 0,01 mm près.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
