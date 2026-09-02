# G-06 — Le déblocage progressif

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G1 · Progression et récompense |
| **Référence au référentiel** | REF-059, REF-060, REF-061 |
| **Compétence visée** | Enchaîner trois filtres dont chacun s'applique au résultat du précédent, et non aux données de départ. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 18 min |
| **Prérequis** | A-29, A-30, A-31 |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 18 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Enchaîner des difficultés croissantes, chaque niveau ouvrant l'accès au suivant.

### Contexte

Le déblocage progressif protège l'apprenant d'une difficulté qu'il n'est pas prêt à affronter. Il rend aussi visible qu'un filtre s'applique à ce qui reste, pas à tout.

### Énoncé

> Trois niveaux de logique. Le niveau 2 ne devient actif qu'une fois le niveau 1 validé, et ainsi de suite. Les groupes verrouillés apparaissent grisés.

### Ce qui vous est fourni

Trois groupes de travail dont deux verrouillés.

### Ce qui est attendu

Les index survivants : 0, 8, 11, 26, 27, 31, 36, 53.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SetEquality**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-06_sujet.gh`

### Barème

3 points, 1 par niveau.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
