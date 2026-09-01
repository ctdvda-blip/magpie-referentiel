# DV-02 — Un composant scripté qui parle à RhinoCommon

**Fiche d'exercice Magpie** · Lot DV — Développement, scripting et API

| | |
|---|---|
| **Thématique** | DV2 · API et librairies |
| **Référence au référentiel** | REF-101, REF-102, REF-103 |
| **Compétence visée** | Employer l'interface de programmation de Rhino depuis un composant scripté pour obtenir ce qu'aucun composant natif ne donne. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Expert |
| **Durée cible** | 35 min |
| **Prérequis** | IA-04 |
| **Mode de validation** | NumericTolerance — tolérance 5 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Employer l'interface de programmation de Rhino depuis un composant scripté pour obtenir ce qu'aucun composant natif ne donne.

### Contexte

On cherche, sur une courbe, le point où le rayon de courbure passe sous le rayon de cintrage de la machine — information qu'aucun composant natif ne rend directement.

### Énoncé

> Le rayon de cintrage minimal de la machine est de 250 mm. Sur la courbe fournie, donnez la longueur cumulée des portions où le rayon de courbure descend sous cette valeur, en millimètres.

### Ce qui vous est fourni

La courbe de tracé et le rayon de cintrage minimal.

### Ce qui est attendu

La longueur cumulée des portions trop cintrées, à 5 mm près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 5.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`DV-02_sujet.gh`

### Barème

1 point si la longueur est juste à 1 mm près et si le pas a été contrôlé par convergence.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
