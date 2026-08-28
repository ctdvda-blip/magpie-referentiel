# IA-09 — Prédire une déperdition sur une baie nouvelle

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA4 · Apprentissage automatique |
| **Référence au référentiel** | REF-129, REF-131, REF-132 |
| **Compétence visée** | Ajuster un modèle sur des mesures existantes et l'employer pour prédire un cas non mesuré. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | IA-04 |
| **Mode de validation** | NumericTolerance — tolérance 10 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Ajuster un modèle sur des mesures existantes et l'employer pour prédire un cas non mesuré.

### Contexte

Les déperditions ont été mesurées sur 24 baies d'un bâtiment existant ; une 25e baie est projetée et il faut l'estimer avant instrumentation.

### Énoncé

> Les surfaces et les déperditions mesurées des 24 baies vous sont fournies. Estimez la déperdition d'une baie de 2,75 m².

### Ce qui vous est fourni

Les 24 couples surface / déperdition mesurés, et la surface de la baie à estimer.

### Ce qui est attendu

Environ 380 W — la déperdition estimée pour une baie de 2,75 m², acceptée à 10 W près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 10.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-09_sujet.gh`

### Barème

1 point si l'estimation tombe à 10 W près de la valeur de référence.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
