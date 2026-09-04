# MP-05 — Mesurer avant d'optimiser

**Fiche d'exercice Magpie** · Lot MP — Méthode, performance et évènements

| | |
|---|---|
| **Thématique** | MP2 · Organisation et performance |
| **Référence au référentiel** | REF-150 |
| **Compétence visée** | Fonder une optimisation sur un relevé de temps, et non sur l'intuition de ce qui coûte cher. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | MP-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-13 Chronomètre |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Fonder une optimisation sur un relevé de temps, et non sur l'intuition de ce qui coûte cher.

### Contexte

La définition met huit secondes à répondre. On a une après-midi pour la rendre utilisable, et douze composants candidats.

### Énoncé

> Le relevé de temps des douze composants vous est fourni, en millisecondes. Donnez la part du composant le plus lourd dans le temps total, en pour cent, arrondie à l'entier.

### Ce qui vous est fourni

Les douze composants et le temps mesuré pour chacun.

### Ce qui est attendu

61 % — la part du maillage adaptatif.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`MP-05_sujet.gh`

### Barème

1 point si la part est juste à l'entier près.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
