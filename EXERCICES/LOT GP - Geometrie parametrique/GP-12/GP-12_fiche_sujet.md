# GP-12 — Tourner puis déplacer, ou l'inverse

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP2 · Transformations et réseaux |
| **Référence au référentiel** | REF-149 |
| **Compétence visée** | Composer deux transformations en sachant que leur ordre décide du résultat. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | GP-11 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 12 composants |
| **Gamification associée** | G-08 Relevé contradictoire |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Composer deux transformations en sachant que leur ordre décide du résultat.

### Contexte

Le bras de la potence est décrit par une rotation et une translation. Selon l'ordre où on les applique, son extrémité ne tombe pas au même endroit.

### Énoncé

> Le point est à 1 200 mm de l'origine sur l'axe des abscisses. On lui applique une rotation de 35° autour de l'origine et une translation de 800 mm en X et 300 mm en Y. Donnez la distance entre les deux positions finales possibles, en millimètres.

### Ce qui vous est fourni

La position du point, l'angle de rotation et le vecteur de translation.

### Ce qui est attendu

513,85 mm séparent les deux résultats, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-12_sujet.gh`

### Barème

1 point si la distance est juste à 0,01 mm près.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
