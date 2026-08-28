# A-13 — Trier une liste avec une clé

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A3 · Listes |
| **Référence au référentiel** | REF-044, REF-047 |
| **Compétence visée** | Réordonner une liste selon les valeurs portées par une autre. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-12 |
| **Mode de validation** | ExactOrderedList — tolérance — |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-08 Combo / série |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Réordonner une liste selon les valeurs portées par une autre.

### Contexte

L'atelier veut débiter les pièces les plus longues en premier, pour engager la barre la plus contraignante tant que le stock est intact.

### Énoncé

> Six pièces portent chacune un numéro de repère et une longueur. L'atelier débite la plus longue en premier. Produisez la liste des numéros de repère dans l'ordre de passage à la scie.

### Ce qui vous est fourni

Les six numéros de repère et les six longueurs correspondantes, dans deux listes de même rang.

### Ce qui est attendu

La liste ordonnée des numéros de repère, du plus long débit au plus court.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-13_sujet.gh`

### Barème

1 point si l'ordre exact est respecté.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
