# G-13 — La machine à sous des motifs

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G2 · Exploration et découverte |
| **Référence au référentiel** | REF-045, REF-068 |
| **Compétence visée** | Chercher le décalage cyclique qui aligne trois séquences, en raisonnant sur le modulo plutôt que par essais. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 15 min |
| **Prérequis** | A-14, B-03 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 12 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Comprendre la logique des motifs cycliques par une mécanique de rouleaux.

### Contexte

La machine à sous rend tangible la logique des motifs cycliques — celle qui régit `Shift List`, les listes de répétition et tout calepinage à motif alterné.

### Énoncé

> Trois rouleaux affichent chacun une séquence de 8 motifs. Trouve les trois valeurs de décalage qui alignent trois motifs identiques sur la ligne centrale.

### Ce qui vous est fourni

Trois listes de 8 motifs et trois sliders de décalage.

### Ce qui est attendu

Les trois décalages, dans l'ordre : 7, 6, 6.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-13_sujet.gh`

### Barème

3 points, validation sur le triplet exact.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
