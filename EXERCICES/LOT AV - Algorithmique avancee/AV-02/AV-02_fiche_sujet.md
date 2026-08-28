# AV-02 — Une chaînette qui se stabilise

**Fiche d'exercice Magpie** · Lot AV — Algorithmique avancée

| | |
|---|---|
| **Thématique** | AV2 · Simulation physique |
| **Référence au référentiel** | REF-094 |
| **Compétence visée** | Conduire une simulation jusqu'à l'équilibre et relever une grandeur sur l'état stabilisé. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 35 min |
| **Prérequis** | AV-01 |
| **Mode de validation** | NumericTolerance — tolérance 5 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Conduire une simulation jusqu'à l'équilibre et relever une grandeur sur l'état stabilisé.

### Contexte

Un câble de suspension prend, sous son propre poids, une forme qu'on ne dessine pas : on la laisse s'établir.

### Énoncé

> Le câble mesure 6 000 mm et ses deux ancrages sont distants de 4 800 mm. Laissez la forme s'établir sous son poids propre, et donnez la flèche au point bas, en millimètres.

### Ce qui vous est fourni

Les deux ancrages, la longueur de câble et le moteur de simulation.

### Ce qui est attendu

La flèche au point bas, à 5 mm près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 5.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`AV-02_sujet.gh`

### Barème

1 point si la flèche est juste à 5 mm près sur un état stabilisé.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
