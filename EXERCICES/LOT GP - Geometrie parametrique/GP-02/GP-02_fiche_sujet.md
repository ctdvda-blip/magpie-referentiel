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
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Enchaîner tracé, surface et volume dans une définition unique dont un seul paramètre commande l'ensemble.

### Contexte

Un escalier droit doit être chiffré en volume de béton avant que sa hauteur d'étage soit figée.

### Énoncé

> L'escalier est massif, 1 100 mm de large, giron de 280 mm. Pour une hauteur d'étage de 2 700 mm et une hauteur de marche visée de 175 mm, produisez le volume de béton, en mètres cubes.

### Ce qui vous est fourni

Trois valeurs réglables : hauteur d'étage, hauteur de marche visée et giron.

### Ce qui est attendu

6,653 m³ — le volume de béton de l'escalier massif, à 0,001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-02_sujet.gh`

### Barème

Grille : nombre de marches juste (1), hauteur réelle recalculée (1), volume juste (2).

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
