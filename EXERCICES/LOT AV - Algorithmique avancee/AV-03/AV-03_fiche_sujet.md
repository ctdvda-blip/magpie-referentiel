# AV-03 — Chercher la meilleure trame

**Fiche d'exercice Magpie** · Lot AV — Algorithmique avancée

| | |
|---|---|
| **Thématique** | AV3 · Design génératif |
| **Référence au référentiel** | REF-095 |
| **Compétence visée** | Poser un problème de recherche de forme — variables, objectif, contraintes — et juger l'optimum obtenu. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 40 min |
| **Prérequis** | AV-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Poser un problème de recherche de forme — variables, objectif, contraintes — et juger l'optimum obtenu.

### Contexte

Une façade doit être calepinée : moins de panneaux coûte moins cher, mais aucun panneau ne peut dépasser 2 400 mm.

### Énoncé

> La façade mesure 18 600 mm de long. Cherchez le calepinage qui minimise le nombre de panneaux sans qu'aucun dépasse 2 400 mm, et donnez ce nombre.

### Ce qui vous est fourni

La longueur de façade, la largeur maximale de panneau, et un moteur de recherche.

### Ce qui est attendu

Un nombre entier : combien de panneaux au minimum.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`AV-03_sujet.gh`

### Barème

1 point si le nombre vaut 8 et si la contrainte figure dans la fonction évaluée.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
