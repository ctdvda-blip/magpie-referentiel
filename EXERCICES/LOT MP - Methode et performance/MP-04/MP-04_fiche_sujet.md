# MP-04 — Ce qu'un curseur fait recalculer

**Fiche d'exercice Magpie** · Lot MP — Méthode, performance et évènements

| | |
|---|---|
| **Thématique** | MP1 · Chronologie et évènements |
| **Référence au référentiel** | REF-090 |
| **Compétence visée** | Déterminer ce qu'une modification fait recalculer, en suivant les dépendances plutôt qu'en supposant que tout repasse. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | MP-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-13 Chronomètre |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Déterminer ce qu'une modification fait recalculer, en suivant les dépendances plutôt qu'en supposant que tout repasse.

### Contexte

La définition met trois secondes à répondre au moindre mouvement de curseur. Avant d'optimiser quoi que ce soit, il faut savoir ce qui repasse réellement.

### Énoncé

> Les liaisons du graphe vous sont fournies. Donnez le nombre de composants qui se recalculent lorsque le curseur Largeur est déplacé.

### Ce qui vous est fourni

Les quatorze composants du graphe et leurs liaisons.

### Ce qui est attendu

10 composants se recalculent.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`MP-04_sujet.gh`

### Barème

1 point si le compte des composants recalculés est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
