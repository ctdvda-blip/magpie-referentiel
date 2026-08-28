# IA-10 — Regrouper un débit pour rationaliser la commande

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA4 · Apprentissage automatique |
| **Référence au référentiel** | REF-130 |
| **Compétence visée** | Regrouper automatiquement des éléments par similarité et exploiter le regroupement obtenu. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | IA-09 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Regrouper automatiquement des éléments par similarité et exploiter le regroupement obtenu.

### Contexte

Le fournisseur consent une remise à partir de trois longueurs standard seulement : il faut ramener un débit dispersé à trois longueurs de commande.

### Énoncé

> Les longueurs de débit vous sont fournies. Ramenez-les à trois longueurs de commande, chacune au moins égale à la plus longue pièce de son groupe, et donnez le nombre de pièces du groupe le plus fourni.

### Ce qui vous est fourni

Les 24 longueurs de débit, en millimètres.

### Ce qui est attendu

L'effectif du groupe le plus fourni.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-10_sujet.gh`

### Barème

1 point si l'effectif annoncé correspond au regroupement de référence.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
