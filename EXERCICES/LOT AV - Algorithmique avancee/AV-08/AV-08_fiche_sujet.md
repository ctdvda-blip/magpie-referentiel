# AV-08 — Quand la relaxation a-t-elle convergé

**Fiche d'exercice Magpie** · Lot AV — Algorithmique avancée

| | |
|---|---|
| **Thématique** | AV3 · Simulation physique |
| **Référence au référentiel** | REF-155 |
| **Compétence visée** | Établir qu'une simulation s'est stabilisée, en distinguant un passage sous la tolérance d'une stabilisation durable. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | AV-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-20 Contre-expertise |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir qu'une simulation s'est stabilisée, en distinguant un passage sous la tolérance d'une stabilisation durable.

### Contexte

La forme relâchée ne bouge plus à l'écran depuis quelques passes. Le relevé de résidu, lui, raconte autre chose.

### Énoncé

> Le résidu de chacune des dix passes vous est fourni. La tolérance vaut 0,1. Donnez le numéro de la première passe à partir de laquelle le résidu RESTE sous la tolérance.

### Ce qui vous est fourni

Le résidu de chaque passe, et la tolérance.

### Ce qui est attendu

8 — c'est à partir de la huitième passe que le résidu ne remonte plus.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`AV-08_sujet.gh`

### Barème

1 point si le rang de stabilisation durable est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
