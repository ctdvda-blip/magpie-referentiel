# B-03 — Façade à trame variable pilotée par un attracteur

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B1 · Architecture et construction |
| **Référence au référentiel** | REF-068, REF-053, REF-054 |
| **Compétence visée** | Piloter une variation continue par la distance à un attracteur, et en chiffrer l'effet global. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | A-39, A-25 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 16 composants |
| **Gamification associée** | G-25 Animation + G-13 Casino motifs assortis |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire varier un paramètre géométrique en fonction d'une distance, méthode fondamentale du paramétrique.

### Contexte

La façade doit laisser passer plus de lumière près de l'atrium. Le maître d'ouvrage, lui, achète du vitrage au mètre carré.

### Énoncé

> Sur la trame de façade 12 × 8, perce chaque panneau d'une ouverture circulaire dont le rayon varie de 50 mm (loin de l'attracteur) à 350 mm (au plus près). Le point attracteur est déplaçable dans Rhino.

### Ce qui vous est fourni

Une surface de façade et un point attracteur référencés.

### Ce qui est attendu

13,30 m² d'ouverture au total, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-03_sujet.gh`

### Barème

2 points pour la variation, 1 point pour la borne de sécurité du rayon.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
