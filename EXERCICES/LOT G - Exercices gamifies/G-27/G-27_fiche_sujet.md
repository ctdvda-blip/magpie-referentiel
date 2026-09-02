# G-27 — La savane paramétrique

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G6 · Sensations et immersion |
| **Référence au référentiel** | REF-063, REF-067, REF-068 |
| **Compétence visée** | Disposer une série d'objets sur un cercle et mesurer la disposition obtenue plutôt que de la constater. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | A-34, A-39 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 14 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Inscrire une série d'exercices dans un fil narratif cohérent avec l'identité de la marque.

### Contexte

La scénarisation inscrit une série d'exercices dans un fil narratif. Un apprenant qui construit une savane retient mieux qu'un apprenant qui construit « une trame polaire de douze éléments ».

### Énoncé

> Chapitre 1 de la savane : construis l'abreuvoir circulaire, puis dispose la harde de 12 animaux en trame autour du point d'eau, chacun orienté vers le centre.

### Ce qui vous est fourni

Un décor de fond et un module d'animal simplifié.

### Ce qui est attendu

17 082,06 mm — le périmètre du polygone que forment les douze animaux, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-27_sujet.gh`

### Barème

2 points : 1 pour la disposition, 1 pour l'orientation.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
