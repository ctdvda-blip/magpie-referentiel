# B-11 — Chaîne de maillons le long d'une courbe

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B3 · Joaillerie |
| **Référence au référentiel** | REF-064, REF-067, REF-046 |
| **Compétence visée** | Compter des éléments qui se recouvrent, où le pas n'est pas la taille de l'élément. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-35, A-38 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 20 composants |
| **Gamification associée** | G-12 Memory |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Répartir et orienter alternativement des éléments le long d'un parcours.

### Contexte

Les maillons d'une chaîne s'enfilent l'un dans l'autre : le pas est plus court que le maillon, sans quoi la chaîne se casse.

### Énoncé

> Répartis des maillons ovales de 4 mm le long de la courbe fournie, chaque maillon tourné de 90° par rapport au précédent, sans jeu ni recouvrement excessif.

### Ce qui vous est fourni

Une courbe de collier internalisée.

### Ce qui est attendu

66 maillons.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-11_sujet.gh`

### Barème

2 points pour la répartition, 2 points pour l'alternance.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
