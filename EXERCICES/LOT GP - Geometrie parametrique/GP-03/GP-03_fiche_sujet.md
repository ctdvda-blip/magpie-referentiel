# GP-03 — Un maillage qu'on peut imprimer

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP3 · Maillages et SubD |
| **Référence au référentiel** | REF-074, REF-075, REF-076 |
| **Compétence visée** | Produire un maillage à partir d'une surface, en maîtriser la finesse, et le rendre exploitable. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | RH-08 |
| **Mode de validation** | NumericTolerance — tolérance 5 % |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire un maillage à partir d'une surface, en maîtriser la finesse, et le rendre exploitable.

### Contexte

Une pièce de forme libre part en impression : le trancheur n'accepte qu'un maillage fermé, et la finesse décide de la qualité comme du poids du fichier.

### Énoncé

> La surface fournie doit devenir un maillage fermé dont l'écart à la surface d'origine ne dépasse nulle part 0,2 mm. Donnez le nombre de faces du maillage obtenu.

### Ce qui vous est fourni

Un fichier contenant la surface fermée d'origine.

### Ce qui est attendu

1 024 faces avec les réglages par défaut du mailleur — la correction accepte 5 % autour de cette valeur.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 5 %.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-03_sujet.gh`

### Barème

1 point si l'écart maximal est respecté et le maillage fermé.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
