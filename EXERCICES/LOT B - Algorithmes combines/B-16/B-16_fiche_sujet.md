# B-16 — Lampe à lamelles de section variable

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B5 · Design produit |
| **Référence au référentiel** | REF-064, REF-069, REF-067 |
| **Compétence visée** | Chiffrer une surface développée dont une dimension varie continûment. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 28 min |
| **Prérequis** | A-35, A-41 |
| **Mode de validation** | NumericTolerance — tolérance 0.0001 |
| **Solution de référence** | 22 composants |
| **Gamification associée** | G-28 Avatar et personnalisation |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire varier une section le long d'un parcours par interpolation contrôlée.

### Contexte

La tôle de l'abat-jour se commande à plat, au mètre carré. La lamelle est large au milieu et étroite aux extrémités.

### Énoncé

> Produis un abat-jour composé de 24 lamelles réparties autour d'un axe. Chaque lamelle suit un profil dont la largeur varie de 15 mm aux extrémités à 45 mm au milieu, selon une courbe douce.

### Ce qui vous est fourni

Une courbe génératrice internalisée et un slider de nombre de lamelles.

### Ce qui est attendu

0,3024 m² de surface développée, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-16_sujet.gh`

### Barème

2 points pour la variation, 2 points pour la répartition.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
