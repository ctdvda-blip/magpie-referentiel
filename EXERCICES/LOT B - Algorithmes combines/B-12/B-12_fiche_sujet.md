# B-12 — Nomenclature automatique et export CSV

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B4 · Données, métrés et livrables |
| **Référence au référentiel** | REF-082, REF-083, REF-085, REF-087 |
| **Compétence visée** | Produire un livrable d'échange dont on connaît la structure avant de l'ouvrir. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-27, A-47 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 24 composants |
| **Gamification associée** | G-01 Score visible |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Transformer un modèle en tableau de données exploitable.

### Contexte

La nomenclature part au bureau des méthodes, qui l'importe automatiquement. Un fichier mal structuré n'est pas rejeté : il est importé de travers.

### Énoncé

> À partir du modèle fourni, produis une nomenclature triée par volume décroissant comportant, pour chaque pièce, le repère, le volume en dm³, la surface en dm² et la masse en kg pour une densité de 700 kg/m³. Exporte le tableau au format CSV.

### Ce qui vous est fourni

Un assemblage de 14 solides internalisés.

### Ce qui est attendu

15 lignes — quatorze pièces, plus l'en-tête.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-12_sujet.gh`

### Barème

2 points pour les calculs, 1 point pour le tri, 1 point pour le format du fichier.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
