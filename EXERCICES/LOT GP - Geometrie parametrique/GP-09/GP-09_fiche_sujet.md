# GP-09 — Ce que les contraintes imposent

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP3 · Plan paramétrique |
| **Référence au référentiel** | REF-146 |
| **Compétence visée** | Déduire d'un jeu de contraintes la dimension qui n'est pas donnée, plutôt que de la mesurer sur le dessin. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | GP-05 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-08 Relevé contradictoire |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Déduire d'un jeu de contraintes la dimension qui n'est pas donnée, plutôt que de la mesurer sur le dessin.

### Contexte

Le joue de meuble suit la pente du rampant. Le plan donne la base, la hauteur et l'angle ; la petite base, elle, se déduit et doit se recalculer si l'angle change.

### Énoncé

> Le joue est un trapèze rectangle de 2 400 mm de base et 1 800 mm de hauteur, dont le fuyant fait 68° avec l'horizontale. Donnez la longueur de la petite base, en millimètres.

### Ce qui vous est fourni

La base, la hauteur et l'angle du fuyant.

### Ce qui est attendu

1 672,75 mm — la petite base, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-09_sujet.gh`

### Barème

1 point si la petite base est juste à 0,01 mm près.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
