# G-01 — Le tableau des scores

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G1 · Progression et récompense |
| **Référence au référentiel** | REF-047, REF-043 |
| **Compétence visée** | Trier une liste et lire le score que le tri produit, en distinguant ce qui est compté de ce qui est trié. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 10 min |
| **Prérequis** | A-10 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Rendre visible la performance immédiate de l'apprenant sur une tâche de tri.

### Contexte

Le tableau des scores rend la performance immédiate. Il ne récompense pas l'effort mais le résultat, et l'apprenant le voit avant de soumettre.

### Énoncé

> Trie les 12 valeurs par ordre croissant. Chaque valeur correctement placée rapporte 10 points, chaque valeur mal placée en coûte 5. Le score s'affiche en direct dans le panneau SCORE.

### Ce qui vous est fourni

Une liste de 12 nombres mélangés et un groupe SCORE pré-câblé.

### Ce qui est attendu

Les douze valeurs triées : 61, 132, 168, 274, 389, 458, 502, 596, 725, 847, 913, 941.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-01_sujet.gh`

### Barème

120 points maximum, validation à 120.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
