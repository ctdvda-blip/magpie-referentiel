# C-05 — Bibliothèque paramétrique avec débit et mise à plat CNC

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C2 · Design de mobilier |
| **Référence au référentiel** | REF-070, REF-082, REF-115, REF-087 |
| **Compétence visée** | Déduire le nombre d'éléments d'un meuble d'une contrainte d'entraxe maximal, et en tirer la nomenclature. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 90 min |
| **Prérequis** | B-06, B-12, B-17 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 50 composants |
| **Gamification associée** | G-06 Niveaux et déblocage + G-05 Badges |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Aller du modèle paramétrique au fichier de fabrication, en passant par la nomenclature.

### Contexte

Une tablette de plus de 800 mm de portée flèche sous la charge. C'est cette règle qui fixe le nombre de montants, pas l'esthétique.

### Énoncé

> Modélise une bibliothèque de largeur, hauteur et profondeur paramétrables, à montants verticaux tous les 800 mm maximum et tablettes réglables. Produis la nomenclature de débit et la mise à plat repérée de tous les panneaux, prête pour la CNC.

### Ce qui vous est fourni

Trois sliders de dimensions générales et un slider d'épaisseur de panneau.

### Ce qui est attendu

28 panneaux à débiter.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-05_sujet.gh`

### Barème

4 points modèle, 3 points nomenclature, 3 points mise à plat.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
