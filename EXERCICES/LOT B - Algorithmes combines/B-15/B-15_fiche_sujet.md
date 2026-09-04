# B-15 — Optimisation d'une découpe linéaire

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B4 · Données, métrés et livrables |
| **Référence au référentiel** | REF-044, REF-045, REF-082 |
| **Compétence visée** | Appliquer une heuristique de découpe et mesurer l'écart entre son résultat et la borne théorique. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | B-13 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 18 composants |
| **Gamification associée** | G-23 Duel et classement + G-03 Compte à rebours |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mettre en œuvre un algorithme de placement glouton et en mesurer la performance.

### Contexte

La barre se commande à l'unité. La règle du plus grand d'abord est celle de l'atelier, parce qu'elle se tient de tête.

### Énoncé

> Débite 30 pièces de longueurs variées dans des barres de 6 000 mm. Applique la règle du plus grand d'abord et affiche le nombre de barres consommées ainsi que la chute totale.

### Ce qui vous est fourni

Une liste de 30 longueurs internalisée.

### Ce qui est attendu

12 barres.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-15_sujet.gh`

### Barème

2 points pour l'algorithme, 1 point pour le nombre de barres, 1 point pour la chute.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
