# A-38 — Rotation et symétrie

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A9 · Transformations et réseaux |
| **Référence au référentiel** | REF-067 |
| **Compétence visée** | Faire tourner une géométrie autour d'un axe choisi et en produire le symétrique par rapport à un plan choisi. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-37 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-14 Puzzle de câblage |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire tourner une géométrie autour d'un axe choisi et en produire le symétrique par rapport à un plan choisi.

### Contexte

Un profil d'angle se décline en version droite et version gauche, orientées à 45° sur la trame.

### Énoncé

> Le profil vous est fourni. Faites-le tourner de 45° autour de l'axe vertical passant par l'origine, puis produisez sa version symétrique par rapport au plan vertical contenant l'axe X.

### Ce qui vous est fourni

Un profil fermé internalisé.

### Ce qui est attendu

Le profil tourné et son symétrique.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-38_sujet.gh`

### Barème

1 point par transformation correcte.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
