# RH-29 — La platine percée en réseau

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Modélisation Rhino |
| **Référence au référentiel** | REF-012, REF-013 |
| **Compétence visée** | Chiffrer la matière restante après un réseau de percements, en distinguant rayon et diamètre. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 14 min |
| **Prérequis** | RH-05 |
| **Mode de validation** | NumericTolerance — tolérance 0.0001 |
| **Solution de référence** | 10 composants |
| **Gamification associée** | G-20 La chasse aux bugs |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Chiffrer la matière restante après un réseau de percements, en distinguant rayon et diamètre.

### Contexte

Une platine percée se pèse pour le transport et se chiffre au kilo. Vingt-quatre trous enlèvent une matière qui compte.

### Énoncé

> La platine mesure 900 × 600 × 12 mm. Elle reçoit un réseau de 6 par 4 trous traversants de 22 mm de diamètre. Donnez le volume de matière restante, en décimètres cubes.

### Ce qui vous est fourni

Les cotes de la platine, la trame et le diamètre des trous.

### Ce qui est attendu

6,3705 dm³ de matière restante, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-29_sujet.gh`

### Barème

1 point si le volume est juste à 0,0001 dm³.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
