# G-08 — La série de bonnes réponses

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G1 · Progression et récompense |
| **Référence au référentiel** | REF-044, REF-045, REF-046 |
| **Compétence visée** | Enchaîner huit manipulations de listes sans rompre la série, chacune portant sur une propriété différente du même jeu. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 16 min |
| **Prérequis** | A-13, A-14, A-16 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 20 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Récompenser la régularité plutôt que le coup de chance.

### Contexte

Le multiplicateur de série récompense la régularité plutôt que le coup de chance. Sept bonnes réponses suivies d'une erreur valent moins que huit réponses moyennes enchaînées.

### Énoncé

> Huit manipulations de listes s'enchaînent. Chaque bonne réponse consécutive augmente le multiplicateur : ×1, ×1,5, ×2, ×3. Une erreur remet le multiplicateur à ×1.

### Ce qui vous est fourni

Huit listes internalisées et huit paramètres de réponse.

### Ce qui est attendu

Les huit réponses : 11, 962, 69, 7 133, 404, 1 119, 5, 1 348.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-08_sujet.gh`

### Barème

8 points de base, jusqu'à 24 points avec multiplicateur.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
