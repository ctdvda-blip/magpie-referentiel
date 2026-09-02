# A-25 — Longest List et Cross Reference

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A5 · Comportements implicites |
| **Référence au référentiel** | REF-054 |
| **Compétence visée** | Choisir délibérément un mode d'appariement entre deux listes de tailles différentes. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-24 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-23 Duel et classement |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Choisir délibérément un mode d'appariement entre deux listes de tailles différentes.

### Contexte

Un calepinage croise 10 files et 4 niveaux : selon qu'on veut une valeur par file ou une valeur par intersection, l'appariement change.

### Énoncé

> Une liste de 10 valeurs et une liste de 4 valeurs vous sont fournies. Produisez d'abord un résultat par file — 10 valeurs — puis un résultat par intersection file × niveau — 40 valeurs.

### Ce qui vous est fourni

Deux listes internalisées de 10 et 4 éléments.

### Ce qui est attendu

Deux effectifs : 10 puis 40.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-25_sujet.gh`

### Barème

1 point par valeur correcte.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
