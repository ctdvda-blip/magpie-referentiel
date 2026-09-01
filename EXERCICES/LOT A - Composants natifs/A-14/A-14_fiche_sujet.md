# A-14 — Filtrer avec Cull Pattern

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A3 · Listes |
| **Référence au référentiel** | REF-045 |
| **Compétence visée** | Éliminer les éléments d'une liste selon un motif régulier. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-13 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-13 Casino — motifs assortis |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Éliminer les éléments d'une liste selon un motif régulier.

### Contexte

Un bardage à claire-voie se pose en déposant une lame sur trois du calepinage plein.

### Énoncé

> Le calepinage plein comporte 36 lames. Produisez la liste des lames réellement posées, sachant qu'on conserve la première puis une sur trois.

### Ce qui vous est fourni

Le calepinage plein : les 36 longueurs de lames, en millimètres.

### Ce qui est attendu

La liste ordonnée des longueurs des lames réellement posées.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-14_sujet.gh`

### Barème

1 point si les 4 bons éléments sont conservés.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
