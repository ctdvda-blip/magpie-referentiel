# IA-04 — Un composant scripté qui somme un métré

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA2 · Composants scriptés assistés |
| **Référence au référentiel** | REF-120, REF-121 |
| **Compétence visée** | Faire produire, installer et brancher un composant scripté qui traite deux listes appariées. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | IA-01 |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire produire, installer et brancher un composant scripté qui traite deux listes appariées.

### Contexte

Le calorifugeage d'un réseau de gaines se chiffre à la surface : chaque tronçon développe sa longueur multipliée par le périmètre de sa section.

### Énoncé

> Les longueurs et les diamètres des 16 tronçons vous sont fournis dans deux listes de même rang. Faites produire un composant scripté qui renvoie la surface totale à calorifuger, en mètres carrés.

### Ce qui vous est fourni

Les 16 longueurs en mètres et les 16 diamètres en millimètres, dans deux listes de même rang.

### Ce qui est attendu

Une valeur décimale : la surface développée totale, en mètres carrés.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-04_sujet.gh`

### Barème

1 point si la surface est juste à 0,01 m² près.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
