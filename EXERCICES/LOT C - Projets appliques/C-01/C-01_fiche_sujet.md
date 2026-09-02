# C-01 — Enveloppe à brise-soleil orientés selon l'ensoleillement

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C1 · Architecture |
| **Référence au référentiel** | REF-027, REF-068, REF-095, REF-079 |
| **Compétence visée** | Dimensionner un dispositif d'ombrage à partir de la course solaire, en distinguant ce qui se divise de ce qui se multiplie. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 90 min |
| **Prérequis** | B-03, B-04 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 45 composants |
| **Gamification associée** | G-22 Boss de fin de chapitre + G-23 Classement |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Construire une enveloppe dont chaque élément réagit à une donnée d'analyse, et justifier le résultat par une mesure.

### Contexte

Le brise-soleil doit occulter à l'heure la plus chaude sans assombrir le reste de l'année. Sa profondeur est ce qui coûte et ce qui se voit.

### Énoncé

> La façade sud du bâtiment reçoit 180 lames brise-soleil. Oriente chaque lame perpendiculairement à la direction du soleil au 21 juin à 15 h, puis optimise l'angle moyen pour limiter la surface exposée à 40 % de la surface vitrée tout en préservant au moins 25 % de vue directe.

### Ce qui vous est fourni

Une façade, un vecteur solaire et le contour vitré internalisés.

### Ce qui est attendu

249,95 mm — la profondeur minimale de lame, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-01_sujet.gh`

### Barème

4 points géométrie, 3 points indicateurs, 3 points optimisation.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
