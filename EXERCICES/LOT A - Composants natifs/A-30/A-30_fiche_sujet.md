# A-30 — Combiner plusieurs conditions

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A7 · Portes logiques |
| **Référence au référentiel** | REF-060 |
| **Compétence visée** | Combiner deux conditions en une décision unique par élément. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-29 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-06 Niveaux et déblocage |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Combiner deux conditions en une décision unique par élément.

### Contexte

Seules les chutes comprises entre 500 et 1 500 mm sont remises en stock : en deçà elles partent au rebut, au-delà elles retournent en barre.

### Énoncé

> Les longueurs des 24 chutes du jour vous sont fournies. Comptez celles qui repartent en stock, bornes incluses.

### Ce qui vous est fourni

Les 24 longueurs de chutes du jour, en millimètres, et les deux bornes de 500 et 1 500 mm.

### Ce qui est attendu

Un nombre entier : combien de chutes repartent en stock.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-30_sujet.gh`

### Barème

1 point si les 20 booléens sont exacts.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
