# IA-22 — L'arrondi qui change avec le langage

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA2 · Composants scriptés assistés |
| **Référence au référentiel** | REF-123 |
| **Compétence visée** | Vérifier qu'un script transposé rend le même résultat que l'original, en se méfiant des comportements par défaut. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | IA-06 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-15 Relecture de code |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Vérifier qu'un script transposé rend le même résultat que l'original, en se méfiant des comportements par défaut.

### Contexte

Le script de chiffrage est transposé d'un langage à un autre. Il compile, il tourne, et le total a bougé de six unités.

### Énoncé

> Les douze quantités à arrondir vous sont fournies ; toutes tombent sur une demi-unité. Le métier arrondit la demie vers le haut. Donnez la somme des quantités arrondies selon la règle du métier.

### Ce qui vous est fourni

Les douze quantités et la règle d'arrondi du métier.

### Ce qui est attendu

170 — la somme des arrondis commerciaux.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-22_sujet.gh`

### Barème

1 point si la somme selon la règle du métier est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
