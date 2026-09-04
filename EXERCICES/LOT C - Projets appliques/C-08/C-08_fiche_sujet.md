# C-08 — Bague solitaire complète

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C3 · Joaillerie |
| **Référence au référentiel** | REF-069, REF-068, REF-081, REF-079 |
| **Compétence visée** | Chiffrer la masse d'une pièce à partir de sa fibre moyenne, et la confronter à une limite de projet. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 85 min |
| **Prérequis** | B-09, B-10 |
| **Mode de validation** | NumericTolerance — tolérance 0.05 |
| **Solution de référence** | 45 composants |
| **Gamification associée** | G-05 Badges + G-09 Récompense cachée |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Assembler plusieurs sous-ensembles techniques en un bijou complet, avec contrôle de poids.

### Contexte

L'or se pèse avant d'être coulé. Un gramme de trop sur un solitaire, c'est cinquante euros et un anneau qui paraît lourd au doigt.

### Énoncé

> Modélise une bague solitaire pour une pierre ronde de 6,5 mm : anneau de taille paramétrable, chaton, panier et 4 griffes. Contrôle que la masse en or 750 reste inférieure à 3,2 g et que la hauteur totale ne dépasse pas 8 mm.

### Ce qui vous est fourni

Un slider de taille de doigt et un slider de diamètre de pierre.

### Ce qui est attendu

3,011 g d'or 750, à 0,05 près — sous la limite de 3,2 g.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.05.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-08_sujet.gh`

### Barème

4 points géométrie, 3 points unicité du solide, 3 points indicateurs.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
