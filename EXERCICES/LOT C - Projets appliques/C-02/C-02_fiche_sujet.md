# C-02 — Résille structurelle sur plan libre

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C1 · Architecture |
| **Référence au référentiel** | REF-069, REF-094, REF-074, REF-049 |
| **Compétence visée** | Chiffrer le linéaire d'une structure triangulée en n'oubliant aucune des trois familles de barres. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 90 min |
| **Prérequis** | B-04, C-01 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 50 composants |
| **Gamification associée** | G-25 Animation de la relaxation |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Générer une structure maillée relaxée et en extraire les données de fabrication.

### Contexte

La résille se chiffre au mètre de barre avant d'être relaxée. C'est ce chiffre qui décide si le projet passe le budget.

### Énoncé

> Sur le contour libre fourni, génère une toiture en résille triangulée, relaxe-la par Kangaroo pour obtenir une forme en équilibre de traction, puis produis la nomenclature des barres regroupées par longueur à 5 mm près et la liste des nœuds avec leur nombre de branches.

### Ce qui vous est fourni

Un contour fermé et trois points d'appui internalisés.

### Ce qui est attendu

695,53 m de barres, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-02_sujet.gh`

### Barème

4 points structure, 3 points nomenclature barres, 3 points nomenclature nœuds.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
