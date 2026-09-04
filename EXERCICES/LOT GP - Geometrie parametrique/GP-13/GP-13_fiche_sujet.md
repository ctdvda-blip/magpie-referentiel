# GP-13 — La pièce qui enchaîne trois opérations

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP2 · Synthèse géométrie |
| **Référence au référentiel** | REF-073, REF-147, REF-148 |
| **Compétence visée** | Ordonner congé, perçage et épaississement de sorte que chaque opération reçoive ce dont elle a besoin. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 22 min |
| **Prérequis** | GP-11 |
| **Mode de validation** | NumericTolerance — tolérance 0.0001 |
| **Solution de référence** | 11 composants |
| **Gamification associée** | G-21 Le golf de composants |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Ordonner congé, perçage et épaississement de sorte que chaque opération reçoive ce dont elle a besoin.

### Contexte

Une platine de fixation se dessine à plat, se congé, se perce, puis s'épaissit. L'ordre n'est pas indifférent : épaissir d'abord oblige à percer un solide.

### Énoncé

> La platine mesure 420 × 260 mm, ses quatre angles portent un congé de 35 mm de rayon, et elle reçoit sept perçages de 26 mm de diamètre. Elle fait 18 mm d'épaisseur. Donnez son volume, en décimètres cubes.

### Ce qui vous est fourni

Les cotes de la platine, le rayon de congé, le diamètre et le nombre de perçages, l'épaisseur.

### Ce qui est attendu

1,8798 dm³, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-13_sujet.gh`

### Barème

1 point si le volume est juste à 0,0001 dm³.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
