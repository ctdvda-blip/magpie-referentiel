# A-04 — Référencer et cuire de la géométrie Rhino

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A1 · Interface, flux de données et paramètres |
| **Référence au référentiel** | REF-026 |
| **Compétence visée** | Faire circuler une géométrie entre Rhino et Grasshopper dans les deux sens, par calque plutôt que par sélection manuelle. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-03 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-05 Badges et trophées |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire circuler une géométrie entre Rhino et Grasshopper dans les deux sens, par calque plutôt que par sélection manuelle.

### Contexte

Le géomètre a livré l'implantation des poteaux sous forme de cercles ; le bureau d'études doit en produire un calque de contrôle décalé.

### Énoncé

> Les cercles d'implantation occupent le calque « CERCLES » du fichier Rhino. Récupérez-les sans les désigner un par un — l'implantation peut encore changer — remontez-les de 50 mm, et déposez le résultat dans le modèle sur le calque « COPIES ».

### Ce qui vous est fourni

Fichier 3DM joint contenant trois cercles sur le calque CERCLES.

### Ce qui est attendu

Trois cercles présents sur le calque COPIES, décalés de 50 mm en Z.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-04_sujet.gh`

### Barème

1 point si les trois cercles sont cuits au bon niveau.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
