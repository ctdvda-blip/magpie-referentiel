# RH-20 — Un maillage est-il fermé

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-019, REF-020, REF-021 |
| **Compétence visée** | Établir par le calcul qu'un maillage est ouvert, et de combien, sans se fier à son apparence. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 25 min |
| **Prérequis** | RH-08 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir par le calcul qu'un maillage est ouvert, et de combien, sans se fier à son apparence.

### Contexte

Le maillage part à l'impression. À l'écran, il paraît parfaitement fermé — c'est toujours le cas.

### Énoncé

> Le maillage compte 2 960 faces triangulaires et 4 434 arêtes. Donnez le nombre d'arêtes nues.

### Ce qui vous est fourni

Le nombre de faces triangulaires et le nombre d'arêtes.

### Ce qui est attendu

12 arêtes nues.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-20_sujet.gh`

### Barème

1 point si le nombre d'arêtes nues est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
