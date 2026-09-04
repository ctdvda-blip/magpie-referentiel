# IA-27 — Le script qui tourne et compte mal

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA2 · Composants scriptés assistés |
| **Référence au référentiel** | REF-124 |
| **Compétence visée** | Localiser une erreur de bornes dans un code qui s'exécute sans planter et rend un résultat crédible. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 16 min |
| **Prérequis** | IA-05 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-20 La chasse aux bugs |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Localiser une erreur de bornes dans un code qui s'exécute sans planter et rend un résultat crédible.

### Contexte

Un script qui plante se répare. Un script qui rend quatorze au lieu de quinze se livre, et l'écart se découvre trois semaines plus tard sur un autre jeu.

### Énoncé

> Le composant fourni doit compter les longueurs qui dépassent 1 500 mm parmi les trente relevées. Il rend un résultat faux. Corrigez-le et donnez le compte exact.

### Ce qui vous est fourni

Le composant fautif et les trente longueurs relevées.

### Ce qui est attendu

15 longueurs dépassent 1 500 mm.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-27_sujet.gh`

### Barème

1 point si le compte corrigé est exact.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
