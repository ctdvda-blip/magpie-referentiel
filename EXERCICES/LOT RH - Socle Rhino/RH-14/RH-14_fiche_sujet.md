# RH-14 — La trame percée d'une trémie

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Modélisation Rhino |
| **Référence au référentiel** | REF-013, REF-008 |
| **Compétence visée** | Compter les éléments d'un réseau régulier dont une zone a été retirée. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-03 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Compter les éléments d'un réseau régulier dont une zone a été retirée.

### Contexte

La dalle repose sur une trame de plots, sauf à l'aplomb de la trémie d'escalier, où ils sont supprimés.

### Énoncé

> La trame compte huit plots en longueur et six en largeur, au pas de 1 200 mm. La trémie en supprime trois en longueur et deux en largeur. Donnez le nombre de plots.

### Ce qui vous est fourni

Les dimensions de la trame, son pas, et l'emprise de la trémie en nombre de plots.

### Ce qui est attendu

42 plots — 48 moins les 6 de la trémie.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-14_sujet.gh`

### Barème

1 point si le compte est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
