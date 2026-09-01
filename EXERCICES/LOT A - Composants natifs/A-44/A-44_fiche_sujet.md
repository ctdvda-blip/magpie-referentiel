# A-44 — Opérations booléennes

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A10 · Surfaces et solides |
| **Référence au référentiel** | REF-071 |
| **Compétence visée** | Combiner des solides par soustraction et quantifier la matière retirée. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-43 |
| **Mode de validation** | NumericTolerance — tolérance 1 % |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-21 Golf de composants |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Combiner des solides par soustraction et quantifier la matière retirée.

### Contexte

Une platine d'assemblage est percée pour le passage des boulons ; le poids retiré entre dans le bilan de charge.

### Énoncé

> La platine vous est fournie. Percez-la de quatre trous traversants de 20 mm de diamètre, puis donnez le volume de matière retirée.

### Ce qui vous est fourni

Un bloc et quatre cylindres internalisés.

### Ce qui est attendu

La platine percée et le volume retiré.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 1 %.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-44_sujet.gh`

### Barème

1 point pour le perçage, 1 point pour le volume.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
