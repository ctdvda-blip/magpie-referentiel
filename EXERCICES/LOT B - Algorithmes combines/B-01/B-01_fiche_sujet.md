# B-01 — Escalier droit paramétrique

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B1 · Architecture et construction |
| **Référence au référentiel** | REF-067, REF-068, REF-047, REF-043 |
| **Compétence visée** | Dimensionner un ouvrage dont le nombre d'éléments est un ENTIER imposé par une contrainte de confort, et recaler les dimensions réelles sur cet entier. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-37, A-39, A-10 |
| **Mode de validation** | NumericTolerance — tolérance 0.1 |
| **Solution de référence** | 18 composants |
| **Gamification associée** | G-02 Barre de progression + G-26 Feedback visuel |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Chaîner série, transformation et extrusion pour produire un ouvrage réglementé par un calcul.

### Contexte

L'escalier relie deux niveaux dont la distance est donnée : c'est le nombre de contremarches qui s'ajuste, jamais la hauteur d'étage.

### Énoncé

> Produis un escalier droit reliant deux niveaux distants de H = 2 850 mm. Le giron est fixé à 280 mm et la hauteur de marche doit rester comprise entre 165 et 180 mm. Détermine automatiquement le nombre de marches et vérifie la règle de Blondel (2h + g compris entre 600 et 650 mm).

### Ce qui vous est fourni

Deux Number Slider (H = 2850, giron = 280) et un Panel de contrôle.

### Ce qui est attendu

615,29 mm — la valeur de Blondel, à 0,1 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-01_sujet.gh`

### Barème

2 points pour la géométrie, 1 point pour le nombre de marches, 1 point pour le contrôle de Blondel.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
