# B-09 — Griffe de sertissage paramétrique

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B3 · Joaillerie |
| **Référence au référentiel** | REF-068, REF-069, REF-067 |
| **Compétence visée** | Chiffrer la matière d'un élément incliné, dont la longueur n'est pas sa projection. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 28 min |
| **Prérequis** | A-39, A-42 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 22 composants |
| **Gamification associée** | G-10 Coffre à butin |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Construire un détail technique répétitif autour d'un axe, avec contrôle d'inclinaison.

### Contexte

Le fil d'or se pèse et se facture au millimètre. Une griffe inclinée est plus longue que la hauteur qu'elle couvre.

### Énoncé

> Modélise 4 griffes réparties à 90° autour d'une pierre ronde de 5 mm de diamètre. Chaque griffe est un fil de 0,9 mm de diamètre, incliné de 12° vers l'intérieur, avec une tête arrondie recouvrant la ceinture de la pierre.

### Ce qui vous est fourni

Un slider de diamètre de pierre et une sphère de gabarit.

### Ce qui est attendu

14,72 mm de fil, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-09_sujet.gh`

### Barème

2 points pour la géométrie, 1 point pour l'inclinaison, 1 point pour le recouvrement.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
