# IA-28 — Regrouper des pièces par similarité

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA4 · Apprentissage automatique |
| **Référence au référentiel** | REF-130 |
| **Compétence visée** | Regrouper des éléments sur plusieurs critères à la fois et lire l'effectif du groupe dominant. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 20 min |
| **Prérequis** | IA-10 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 10 composants |
| **Gamification associée** | G-12 Le memory des composants |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Regrouper des éléments sur plusieurs critères à la fois et lire l'effectif du groupe dominant.

### Contexte

Rationaliser un débit, c'est ramener des pièces toutes différentes à quelques familles. La famille la plus fournie décide du réglage de la machine.

### Énoncé

> Les vingt pièces vous sont données par leur longueur et leur épaisseur. Regroupez-les selon qu'elles dépassent ou non 900 mm de long et 34 mm d'épaisseur. Donnez l'effectif du groupe le plus fourni.

### Ce qui vous est fourni

Les vingt couples longueur-épaisseur et les deux seuils.

### Ce qui est attendu

10 pièces dans le groupe le plus fourni.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-28_sujet.gh`

### Barème

1 point si l'effectif est exact.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
