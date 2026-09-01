# FA-01 — Combien de panneaux pour ce débit

**Fiche d'exercice Magpie** · Lot FA — Aide à la fabrication

| | |
|---|---|
| **Thématique** | FA1 · Imbrication |
| **Référence au référentiel** | REF-113, REF-114 |
| **Compétence visée** | Estimer le nombre de panneaux nécessaires à un débit et chiffrer la chute, avant toute imbrication réelle. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 35 min |
| **Prérequis** | QT-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Estimer le nombre de panneaux nécessaires à un débit et chiffrer la chute, avant toute imbrication réelle.

### Contexte

Le débit part sur une découpeuse à commande numérique ; le panneau brut mesure 2 500 × 1 250 mm et se commande à l'unité.

### Énoncé

> Les 20 pièces à débiter vous sont fournies avec leurs dimensions. Donnez le nombre minimal théorique de panneaux, c'est-à-dire celui qu'imposerait déjà la seule surface, avant toute contrainte de placement.

### Ce qui vous est fourni

Les 20 longueurs et les 20 hauteurs, en millimètres, et les dimensions du panneau brut.

### Ce qui est attendu

4 — le nombre minimal théorique de panneaux. La surface exige 3,10 panneaux, et l'on n'en commande pas un dixième.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`FA-01_sujet.gh`

### Barème

1 point si le nombre est juste et arrondi au supérieur.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
