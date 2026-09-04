# B-07 — Tiroir paramétrique avec jeux fonctionnels

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B2 · Design de mobilier |
| **Référence au référentiel** | REF-070, REF-072 |
| **Compétence visée** | Appliquer un jeu fonctionnel du bon côté, et le bon nombre de fois. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | B-06, A-46 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 20 composants |
| **Gamification associée** | G-04 Système de vies |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Intégrer des jeux de fonctionnement et vérifier l'absence de collision.

### Contexte

La coulisse demande 13 mm de chaque côté. Un tiroir trop large ne rentre pas ; trop étroit, il se met en travers.

### Énoncé

> Insère dans le caisson un tiroir sur coulisses de 13 mm de jeu latéral par côté et 2 mm en hauteur. Le tiroir doit pouvoir coulisser de toute sa profondeur sans collision : prouve-le.

### Ce qui vous est fourni

Le caisson de l'exercice B-06.

### Ce qui est attendu

736 mm de largeur de tiroir.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-07_sujet.gh`

### Barème

2 points pour le tiroir, 2 points pour la preuve d'absence de collision.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
