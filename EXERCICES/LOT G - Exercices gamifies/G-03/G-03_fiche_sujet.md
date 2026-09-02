# G-03 — Contre la montre

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G1 · Progression et récompense |
| **Référence au référentiel** | REF-042, REF-043 |
| **Compétence visée** | Enchaîner cinq extractions de liste de natures différentes sans confondre rang, position et valeur. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 6 min |
| **Prérequis** | A-11, A-12 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 12 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Travailler la vitesse d'exécution sur des gestes déjà maîtrisés.

### Contexte

Le contre-la-montre travaille la vitesse sur des gestes déjà acquis. Il ne s'adresse pas à qui découvre : il sert à rendre automatique ce qui est encore réfléchi.

### Énoncé

> Cinq extractions de listes à réaliser en moins de 180 secondes. Le chronomètre démarre à l'ouverture de l'exercice et s'affiche en haut du canvas.

### Ce qui vous est fourni

Cinq listes internalisées et cinq paramètres de réponse.

### Ce qui est attendu

Les cinq extractions, dans l'ordre : 806, 729, 965, 148, 578.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-03_sujet.gh`

### Barème

5 points, plus 3 points de bonus si le temps cible est tenu.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
