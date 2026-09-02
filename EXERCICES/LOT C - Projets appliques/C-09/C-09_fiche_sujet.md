# C-09 — Pavage de pierres sur surface libre

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C3 · Joaillerie |
| **Référence au référentiel** | REF-068, REF-101, REF-080, REF-045 |
| **Compétence visée** | Estimer combien d'éléments circulaires tiennent sur une surface en tenant compte de l'écart imposé entre eux. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Expérimenté |
| **Durée cible** | 85 min |
| **Prérequis** | B-04, C-08 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 48 composants |
| **Gamification associée** | G-13 Casino motifs assortis + G-16 Chasse au trésor |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Répartir des éléments de tailles variées sur une surface courbe en respectant des distances minimales.

### Contexte

Le métal entre deux pierres tient le serti. Sous 0,3 mm il cède, et la pierre part.

### Énoncé

> Pave la surface libre fournie de pierres rondes de 1,2 à 2,5 mm réparties de manière quasi aléatoire mais sans jamais laisser moins de 0,3 mm de métal entre deux pierres voisines. Perce ensuite les logements coniques correspondants.

### Ce qui vous est fourni

Une surface libre internalisée et un slider de densité.

### Ce qui est attendu

64 pierres.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-09_sujet.gh`

### Barème

4 points répartition, 3 points respect de la distance, 3 points logements.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
