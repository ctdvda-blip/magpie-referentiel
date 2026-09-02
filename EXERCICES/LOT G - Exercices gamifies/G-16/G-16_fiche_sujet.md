# G-16 — La chasse au trésor

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G3 · Manipulation et adresse |
| **Référence au référentiel** | REF-055, REF-101 |
| **Compétence visée** | Isoler la donnée aberrante d'un ensemble volumineux par un test d'appartenance, et en rendre l'index. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 18 min |
| **Prérequis** | A-09, A-45 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Rechercher une donnée anormale dans un ensemble volumineux.

### Contexte

Un point hors volume dans un nuage de cinq cents, c'est le cas réel du relevé qui contient une mesure parasite. Le trouver à l'œil est impossible ; le trouver par un test est immédiat.

### Énoncé

> Parmi 500 points, un seul est aberrant : il est hors du volume de référence. Trouve son index. Trois indices sont disponibles, chacun coûte 2 points.

### Ce qui vous est fourni

500 points internalisés et un volume de référence.

### Ce qui est attendu

337 — l'index du point aberrant.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-16_sujet.gh`

### Barème

10 points, moins 2 points par indice consulté.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
