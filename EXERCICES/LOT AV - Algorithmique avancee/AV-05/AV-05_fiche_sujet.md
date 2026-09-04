# AV-05 — Charger jusqu'à la limite

**Fiche d'exercice Magpie** · Lot AV — Algorithmique avancée

| | |
|---|---|
| **Thématique** | AV1 · Boucles et itération |
| **Référence au référentiel** | REF-152 |
| **Compétence visée** | Transporter un cumul d'un passage au suivant, et repérer le rang où il franchit une limite. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | AV-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-11 Commande à passer |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Transporter un cumul d'un passage au suivant, et repérer le rang où il franchit une limite.

### Contexte

Les pièces se chargent dans l'ordre du montage, pas dans celui qui remplirait le mieux. Le camion accepte 4 000 mm de longueur cumulée.

### Énoncé

> Les vingt longueurs vous sont fournies dans l'ordre de chargement. La capacité est de 4 000 mm cumulés. Donnez le rang de la première pièce qui fait dépasser la capacité.

### Ce qui vous est fourni

Les vingt longueurs, dans l'ordre, et la capacité.

### Ce qui est attendu

8 — c'est la huitième pièce qui fait passer le cumul au-delà de 4 000 mm.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`AV-05_sujet.gh`

### Barème

1 point si le rang est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
