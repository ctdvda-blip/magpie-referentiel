# QT-01 — Le métré d'un plancher bois

**Fiche d'exercice Magpie** · Lot QT — Quantitatifs, chiffrage et export

| | |
|---|---|
| **Thématique** | QT1 · Quantitatifs et chiffrage |
| **Référence au référentiel** | REF-082, REF-084 |
| **Compétence visée** | Établir un métré à partir de sections et de longueurs, en distinguant les grandeurs qui s'additionnent de celles qui ne s'additionnent pas. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-47 |
| **Mode de validation** | NumericTolerance — tolérance 0,0001 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-01 Score visible |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir un métré à partir de sections et de longueurs, en distinguant les grandeurs qui s'additionnent de celles qui ne s'additionnent pas.

### Contexte

Un plancher bois se commande au volume de bois, mais se pose au linéaire : le métré doit rendre les deux.

### Énoncé

> Les 20 solives du plancher vous sont fournies avec leur section et leur longueur. Donnez le volume total de bois, en mètres cubes.

### Ce qui vous est fourni

Les 20 sections, en millimètres, et les 20 longueurs correspondantes, en millimètres.

### Ce qui est attendu

Le volume total de bois, en mètres cubes, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`QT-01_sujet.gh`

### Barème

1 point si le volume est juste à 0,0001 m³ près.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
