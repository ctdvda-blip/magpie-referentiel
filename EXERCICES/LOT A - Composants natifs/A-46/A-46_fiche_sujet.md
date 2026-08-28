# A-46 — Détecter une collision

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A10 · Surfaces et solides |
| **Référence au référentiel** | REF-072 |
| **Compétence visée** | Identifier, dans un ensemble, les objets qui interfèrent avec un volume donné. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-45 |
| **Mode de validation** | SetEquality — tolérance — |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-01 Score visible |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Identifier, dans un ensemble, les objets qui interfèrent avec un volume donné.

### Contexte

Un gabarit de passage doit rester libre : tout élément qui y pénètre est à reprendre.

### Énoncé

> Quinze blocs sont disposés autour du gabarit de passage fourni. Indiquez combien d'entre eux empiètent sur ce gabarit.

### Ce qui vous est fourni

15 blocs et un volume de gabarit internalisés.

### Ce qui est attendu

Le nombre de blocs en interférence avec le gabarit.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SetEquality**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-46_sujet.gh`

### Barème

1 point si les bons blocs sont identifiés.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
