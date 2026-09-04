# IA-26 — Transposer, et le prouver sur un second jeu

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA2 · Composants scriptés assistés |
| **Référence au référentiel** | REF-122, REF-123 |
| **Compétence visée** | Établir qu'un script porté vers un autre langage produit exactement la même chose, sur un jeu qu'il n'a pas servi à écrire. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 18 min |
| **Prérequis** | IA-06 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-19 Le composant mystère |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir qu'un script porté vers un autre langage produit exactement la même chose, sur un jeu qu'il n'a pas servi à écrire.

### Contexte

Reprendre une définition ancienne maintenue en VB.NET, c'est la porter sans changer un résultat dont personne ne se souvient de la règle exacte.

### Énoncé

> Le composant existant produit les sommes cumulées d'une liste. Faites-le porter vers un autre langage, puis appliquez les deux versions au jeu de preuve fourni et donnez les quatorze valeurs obtenues.

### Ce qui vous est fourni

Le composant d'origine et le jeu de preuve de quatorze valeurs.

### Ce qui est attendu

Les quatorze cumuls : 213, 230, 656, 1 011, 1 306, 1 560, 1 711, 1 801, 2 150, 2 234, 2 390, 2 524, 2 989, 3 141.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-26_sujet.gh`

### Barème

1 point si les quatorze valeurs concordent dans l'ordre.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
