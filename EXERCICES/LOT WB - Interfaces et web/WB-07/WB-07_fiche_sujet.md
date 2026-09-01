# WB-07 — Le plan qui tient sur la feuille

**Fiche d'exercice Magpie** · Lot WB — Interfaces, web et interopérabilité

| | |
|---|---|
| **Thématique** | WB2 · Publication web |
| **Référence au référentiel** | REF-110 |
| **Compétence visée** | Choisir l'échelle normalisée qui fait tenir une pièce sur un format donné, marges comprises. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | WB-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-16 Livrable pesé |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Choisir l'échelle normalisée qui fait tenir une pièce sur un format donné, marges comprises.

### Contexte

Le configurateur produit le plan en PDF, que le client imprime lui-même. Une échelle non normalisée rend le plan inutilisable : personne ne mesure au 1:6,1.

### Énoncé

> La pièce mesure 2 380 mm de long et 1 640 mm de haut. Le plan sort sur une feuille de 420 × 297 mm, avec 15 mm de marge sur chaque bord. Les échelles disponibles sont 1:1, 1:2, 1:5, 1:10, 1:20, 1:50 et 1:100. Donnez le dénominateur de la plus grande échelle qui convient.

### Ce qui vous est fourni

Les dimensions de la pièce, le format de la feuille, la marge, et la liste des échelles normalisées.

### Ce qui est attendu

10 — l'échelle 1:10, qui donne 238 × 164 mm dans une zone utile de 390 × 267 mm.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`WB-07_sujet.gh`

### Barème

1 point si le dénominateur est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
