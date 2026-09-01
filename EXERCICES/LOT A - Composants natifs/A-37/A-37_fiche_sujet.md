# A-37 — Déplacer par un vecteur

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A9 · Transformations et réseaux |
| **Référence au référentiel** | REF-067 |
| **Compétence visée** | Appliquer une translation et l'échelonner, en sachant que la transformation ne consomme pas l'original. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | A-32 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-25 Animation de la solution |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Appliquer une translation et l'échelonner, en sachant que la transformation ne consomme pas l'original.

### Contexte

Une rangée d'entretoises est répartie sur la hauteur d'un montant.

### Énoncé

> L'entretoise de base vous est fournie. Remontez-la de 120 mm, puis produisez cinq entretoises supplémentaires échelonnées tous les 24 mm au-dessus d'elle, sans employer de composant de réseau.

### Ce qui vous est fourni

Un cercle internalisé dans le plan XY.

### Ce qui est attendu

Six entretoises espacées de 24 mm.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-37_sujet.gh`

### Barème

1 point si 6 cercles espacés de 24 mm sont produits.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
