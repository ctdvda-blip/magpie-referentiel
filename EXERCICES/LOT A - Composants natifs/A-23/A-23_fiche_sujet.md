# A-23 — Renommer les chemins avec Path Mapper

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A4 · Arbres de données |
| **Référence au référentiel** | REF-050 |
| **Compétence visée** | Réécrire les chemins d'un flux pour préparer une mise en correspondance. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 9 min |
| **Prérequis** | A-22 |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-32 Indices payants |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Réécrire les chemins d'un flux pour préparer une mise en correspondance.

### Contexte

Deux flux décrivent le même ouvrage, l'un rangé par niveau puis par file, l'autre par file puis par niveau : ils ne s'apparient pas.

### Énoncé

> Le flux fourni est rangé par niveau puis par file. Réorganisez-le par file puis par niveau, sans modifier les éléments eux-mêmes. Indiquez le nombre de branches obtenu.

### Ce qui vous est fourni

Un arbre internalisé de 12 branches à deux niveaux.

### Ce qui est attendu

Un flux dont les deux niveaux de chemin sont permutés.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SetEquality**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-23_sujet.gh`

### Barème

1 point si les chemins sont permutés.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
