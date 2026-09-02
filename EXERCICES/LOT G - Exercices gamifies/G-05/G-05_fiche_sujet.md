# G-05 — La collection de badges

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G1 · Progression et récompense |
| **Référence au référentiel** | REF-079, REF-081, REF-098 |
| **Compétence visée** | Produire une famille complète de mesures sur un même assemblage, en gardant la cohérence des unités. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | A-47, A-49 |
| **Mode de validation** | NumericTolerance — tolérance 1 |
| **Solution de référence** | 16 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Valoriser la maîtrise d'une famille complète de composants.

### Contexte

Le badge récompense la maîtrise d'une famille entière, pas d'un geste isolé. Un métreur qui sait mesurer une longueur mais pas un volume n'est pas un métreur.

### Énoncé

> Six mesures à produire sur le même assemblage. Chaque mesure exacte débloque un badge. La collection complète débloque le badge doré ARPENTEUR.

### Ce qui vous est fourni

Un assemblage internalisé et six paramètres de réponse.

### Ce qui est attendu

Les six mesures : 15 200 mm de développé, 11 904 mm² de section, 180 940,8 cm³, 1 420,385 kg, 4 370 mm hors tout, 6 620 mm de portée.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-05_sujet.gh`

### Barème

1 point par badge, badge doré à 6/6.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
