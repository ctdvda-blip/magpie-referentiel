# G-25 — L'animation de la solution

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G6 · Sensations et immersion |
| **Référence au référentiel** | REF-090, REF-093, REF-067 |
| **Compétence visée** | Piloter une révélation progressive par un paramètre unique et savoir lire un état INTERMÉDIAIRE, pas seulement le final. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | A-37, B-05 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 14 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Rendre visible le déroulement d'un algorithme plutôt que son seul résultat.

### Contexte

Animer la construction d'un algorithme le rend enseignable : on voit dans quel ORDRE les choses arrivent, ce que le résultat final ne dit jamais.

### Énoncé

> Anime la construction de la structure : les 40 barres doivent apparaître une par une en trois secondes, puis la structure entière change de couleur. Le pilotage se fait par un unique slider de 0 à 1.

### Ce qui vous est fourni

Une structure de 40 barres déjà modélisée.

### Ce qui est attendu

8 508 mm — la longueur cumulée des barres visibles à t = 0,375.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-25_sujet.gh`

### Barème

2 points : 1 pour l'état final, 1 pour l'état intermédiaire.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
