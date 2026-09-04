# A-11 — List Item et indexation

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A3 · Listes |
| **Référence au référentiel** | REF-042 |
| **Compétence visée** | Atteindre un élément par son rang, et atteindre le dernier sans présumer de l'effectif. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-10 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-12 Memory |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Atteindre un élément par son rang, et atteindre le dernier sans présumer de l'effectif.

### Contexte

Une liste de débit est reprise par un opérateur qui doit contrôler deux pièces précises avant lancement.

### Énoncé

> Le débit comporte 24 pièces. Relevez la longueur de la quatrième pièce, puis celle de la dernière — sachant que le débit s'allongera la semaine prochaine et que votre montage devra encore désigner la dernière pièce sans être retouché.

### Ce qui vous est fourni

Les 24 longueurs de débit, en millimètres, dans l'ordre du bon de commande.

### Ce qui est attendu

Deux longueurs, dans cet ordre : 2 075 mm puis 2 830 mm — celle du quatrième rang, puis celle du dernier.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-11_sujet.gh`

### Barème

2 points : 1 par extraction correcte.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
