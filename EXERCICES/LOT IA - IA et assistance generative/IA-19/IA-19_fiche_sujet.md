# IA-19 — Regrouper un débit en trois familles

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA5 · Apprentissage automatique |
| **Référence au référentiel** | REF-130 |
| **Compétence visée** | Regrouper des pièces en familles de fabrication et identifier celle qui pèse le plus dans l'organisation de l'atelier. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | IA-10 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Regrouper des pièces en familles de fabrication et identifier celle qui pèse le plus dans l'organisation de l'atelier.

### Contexte

L'atelier organise ses postes par famille de format. Le débit arrive en vrac, et c'est la famille la plus fournie qui dimensionne le poste.

### Énoncé

> Les vingt-quatre longueurs du débit vous sont fournies. Les familles sont : petit sous 300 mm, moyen jusqu'à 900 mm exclus, grand au-delà. Donnez l'effectif de la famille la plus fournie.

### Ce qui vous est fourni

Les vingt-quatre longueurs, en millimètres, et les deux seuils.

### Ce qui est attendu

9 pièces — l'effectif de la famille des petits.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-19_sujet.gh`

### Barème

1 point si l'effectif de la famille la plus fournie est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
