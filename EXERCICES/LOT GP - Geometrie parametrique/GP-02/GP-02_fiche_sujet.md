# GP-02 — Un modèle paramétrique de bout en bout

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP2 · Synthèse géométrie |
| **Référence au référentiel** | REF-073 |
| **Compétence visée** | Enchaîner tracé, surface et volume dans une définition unique dont un seul paramètre commande l'ensemble. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 45 min |
| **Prérequis** | GP-01, A-41 |
| **Mode de validation** | NumericTolerance — tolérance 0,001 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-25 Projet jalonné |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Enchaîner tracé, surface et volume dans une définition unique dont un seul paramètre commande l'ensemble.

### Contexte

Un escalier droit doit être chiffré en volume de béton avant que sa hauteur d'étage soit figée.

### Énoncé

> L'escalier fait 1 100 mm de large, avec un giron de 280 mm et une paillasse de 150 mm d'épaisseur. Pour une hauteur d'étage de 2 700 mm et des marches de 175 mm, produisez le volume de béton, en mètres cubes.

### Ce qui vous est fourni

Trois valeurs réglables : hauteur d'étage, hauteur de marche visée et giron.

### Ce qui est attendu

Le volume de béton, en mètres cubes, à 0,001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-02_sujet.gh`

### Barème

Grille : nombre de marches juste (1), hauteur réelle recalculée (1), volume juste (2).

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
