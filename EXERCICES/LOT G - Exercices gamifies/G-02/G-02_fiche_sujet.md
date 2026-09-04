# G-02 — La barre de progression

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G1 · Progression et récompense |
| **Référence au référentiel** | REF-062, REF-063 |
| **Compétence visée** | Construire cinq primitives distinctes et mesurer l'ensemble qu'elles forment, chaque forme étant un jalon. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | A-34 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 14 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Découper une tâche en jalons visibles pour soutenir l'effort.

### Contexte

La barre de progression soutient l'effort en découpant une tâche longue en jalons visibles. Sans elle, cinq formes à poser se vivent comme une seule tâche qui n'avance pas.

### Énoncé

> Reconstitue le logo en 5 étapes. Chaque forme correctement placée fait progresser la barre de 20 %. La barre passe au vert à 100 %.

### Ce qui vous est fourni

Un gabarit du logo en filigrane et une barre de progression pré-câblée.

### Ce qui est attendu

1 372,74 mm — la somme des cinq périmètres, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-02_sujet.gh`

### Barème

20 % par forme, validation à 100 %.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
