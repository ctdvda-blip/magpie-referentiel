# WB-05 — Dimensionner le calcul d'un configurateur

**Fiche d'exercice Magpie** · Lot WB — Interfaces, web et interopérabilité

| | |
|---|---|
| **Thématique** | WB3 · Interopérabilité |
| **Référence au référentiel** | REF-112 |
| **Compétence visée** | Dimensionner une capacité de calcul distante à partir de la fréquentation attendue, en raisonnant sur la pointe et non sur la moyenne. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Expert |
| **Durée cible** | 30 min |
| **Prérequis** | WB-03 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-22 Mise en charge |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Dimensionner une capacité de calcul distante à partir de la fréquentation attendue, en raisonnant sur la pointe et non sur la moyenne.

### Contexte

Le configurateur en ligne délègue ses recalculs à un service distant, facturé à l'instance et à l'heure. Sous-dimensionné, il fait attendre ; sur-dimensionné, il coûte pour rien.

### Énoncé

> Le configurateur reçoit 12 000 visites par jour, dont 18 % se concentrent sur l'heure de pointe. Chaque visite déclenche 6 recalculs, et un recalcul occupe une instance pendant 1,2 seconde. Donnez le nombre d'instances nécessaires pour tenir la pointe sans faire attendre.

### Ce qui vous est fourni

La fréquentation quotidienne, la part de l'heure de pointe, le nombre de recalculs par visite et la durée d'un recalcul.

### Ce qui est attendu

5 instances — la pointe demande 15 552 secondes de calcul pour 3 600 secondes d'horloge.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`WB-05_sujet.gh`

### Barème

1 point si le nombre d'instances est juste et arrondi au supérieur.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
