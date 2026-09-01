# IA-20 — Ce qu'un budget de calcul permet d'essayer

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA5 · Apprentissage automatique |
| **Référence au référentiel** | REF-131, REF-132 |
| **Compétence visée** | Dimensionner une campagne d'évaluations à partir du temps disponible, et mesurer l'écart avec ce qu'exigerait l'exploration exhaustive. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | IA-09 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-13 Chronomètre |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Dimensionner une campagne d'évaluations à partir du temps disponible, et mesurer l'écart avec ce qu'exigerait l'exploration exhaustive.

### Contexte

Chaque évaluation demande un calcul thermique complet. On dispose d'une nuit de machine.

### Énoncé

> Le budget est de 6 heures et chaque évaluation prend 42 secondes. Donnez le nombre d'évaluations réalisables.

### Ce qui vous est fourni

Le budget en heures, la durée d'une évaluation, et le nombre de paramètres et de niveaux du problème.

### Ce qui est attendu

514 évaluations tiennent dans le budget.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-20_sujet.gh`

### Barème

1 point si le nombre d'évaluations est juste et arrondi à l'inférieur.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
