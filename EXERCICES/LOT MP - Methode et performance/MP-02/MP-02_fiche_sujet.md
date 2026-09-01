# MP-02 — Trouver ce qui coûte le temps de calcul

**Fiche d'exercice Magpie** · Lot MP — Méthode, performance et évènements

| | |
|---|---|
| **Thématique** | MP2 · Performance d'exécution |
| **Référence au référentiel** | REF-089 |
| **Compétence visée** | Localiser le composant qui coûte le temps de recalcul, plutôt que d'optimiser au hasard. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | MP-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-01 Score visible |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Localiser le composant qui coûte le temps de recalcul, plutôt que d'optimiser au hasard.

### Contexte

Une définition met plusieurs secondes à se recalculer à chaque mouvement de curseur, et le client attend devant l'écran.

### Énoncé

> Les temps de recalcul des 20 composants d'une définition vous sont fournis, en millisecondes. Donnez la part du temps total que représentent les trois composants les plus coûteux, en pourcentage arrondi à l'entier.

### Ce qui vous est fourni

Les 20 temps mesurés, en millisecondes, dans l'ordre du profil affiché par Grasshopper.

### Ce qui est attendu

97 — la part des trois composants les plus coûteux, en pourcentage entier.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`MP-02_sujet.gh`

### Barème

1 point si la part est juste à l'entier près.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
