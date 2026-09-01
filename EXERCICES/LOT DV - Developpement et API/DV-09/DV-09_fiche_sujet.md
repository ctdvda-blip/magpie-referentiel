# DV-09 — La division qui n'est pas celle qu'on croit

**Fiche d'exercice Magpie** · Lot DV — Développement, scripting et API

| | |
|---|---|
| **Thématique** | DV1 · Scripting dans Grasshopper |
| **Référence au référentiel** | REF-100, REF-102 |
| **Compétence visée** | Anticiper le comportement d'un opérateur selon le TYPE de ses opérandes, dans un composant scripté. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Expert |
| **Durée cible** | 25 min |
| **Prérequis** | DV-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-15 Relecture de code |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Anticiper le comportement d'un opérateur selon le type de ses opérandes, dans un composant scripté.

### Contexte

Le script calcule combien de panneaux entiers chaque pièce consomme. Les quantités sont des entiers, et l'opérateur de division aussi.

### Énoncé

> Le script divise chacune des dix quantités par 4 et somme les résultats. Les quantités et le diviseur sont déclarés comme des ENTIERS. Donnez la somme rendue par le script.

### Ce qui vous est fourni

Les dix quantités, le diviseur, et le type déclaré des variables.

### Ce qui est attendu

32 — la somme des quotients entiers.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`DV-09_sujet.gh`

### Barème

1 point si la somme des quotients entiers est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
