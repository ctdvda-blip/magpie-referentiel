# GP-06 — Les sommets d'une nappe maillée

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP4 · Maillages et SubD |
| **Référence au référentiel** | REF-074 |
| **Compétence visée** | Distinguer le nombre de faces d'un maillage de son nombre de sommets, et savoir lequel commande quoi. |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 20 min |
| **Prérequis** | GP-03 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Distinguer le nombre de faces d'un maillage de son nombre de sommets, et savoir lequel commande quoi.

### Contexte

La nappe part vers un calcul aux éléments finis, qui se dimensionne au nombre de NŒUDS, pas de faces.

### Énoncé

> La nappe est maillée en 48 divisions dans un sens et 30 dans l'autre, en quadrangles. Donnez le nombre de sommets.

### Ce qui vous est fourni

Les deux nombres de divisions.

### Ce qui est attendu

1 519 sommets — 49 × 31.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-06_sujet.gh`

### Barème

1 point si le nombre de sommets est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
