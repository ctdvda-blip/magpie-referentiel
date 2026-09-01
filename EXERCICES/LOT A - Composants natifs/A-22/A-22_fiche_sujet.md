# A-22 — Construire un arbre

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A4 · Arbres de données |
| **Référence au référentiel** | REF-048, REF-051 |
| **Compétence visée** | Assembler plusieurs listes en un flux structuré, puis en réextraire chaque groupe. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-21 |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-14 Puzzle de câblage |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Assembler plusieurs listes en un flux structuré, puis en réextraire chaque groupe.

### Contexte

Trois lots de fabrication doivent voyager ensemble dans la définition tout en restant distincts à l'arrivée.

### Énoncé

> Trois listes de longueurs différentes vous sont fournies. Faites-les circuler dans un flux unique où chacune reste un groupe séparé, puis récupérez les trois listes d'origine à l'identique.

### Ce qui vous est fourni

Trois listes internalisées de 2, 5 et 3 éléments.

### Ce qui est attendu

Un flux à trois branches, puis trois sorties identiques aux listes de départ.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SetEquality**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-22_sujet.gh`

### Barème

1 point pour l'arbre, 1 point pour la décomposition.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
