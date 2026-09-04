# RH-22 — La finesse du maillage à l'export

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH4 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-024 |
| **Compétence visée** | Régler la finesse d'un maillage d'export à partir de l'écart admissible à la surface, et non au jugé. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 25 min |
| **Prérequis** | RH-10 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Régler la finesse d'un maillage d'export à partir de l'écart admissible à la surface, et non au jugé.

### Contexte

Le cylindre part en fabrication. Le maillage d'export remplace le cercle par un polygone : la question est de savoir de combien il s'en écarte.

### Énoncé

> Le cylindre a 30 mm de rayon. L'écart entre le maillage et la surface réelle ne doit pas dépasser 0,05 mm. Donnez le nombre minimal de facettes sur un demi-tour.

### Ce qui vous est fourni

Le rayon du cylindre et l'écart maximal admis.

### Ce qui est attendu

55 facettes sur un demi-tour.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-22_sujet.gh`

### Barème

1 point si le nombre de facettes est juste et arrondi au supérieur.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
