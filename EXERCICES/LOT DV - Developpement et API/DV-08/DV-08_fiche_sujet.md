# DV-08 — Ce que le remappage fait aux branches

**Fiche d'exercice Magpie** · Lot DV — Développement, scripting et API

| | |
|---|---|
| **Thématique** | DV2 · API et librairies |
| **Référence au référentiel** | REF-105 |
| **Compétence visée** | Prévoir la structure d'un arbre après un remappage de chemins, en raisonnant sur les chemins plutôt que sur les données. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Expert |
| **Durée cible** | 25 min |
| **Prérequis** | DV-03 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-09 Arbre relu |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Prévoir la structure d'un arbre après un remappage de chemins, en raisonnant sur les chemins plutôt que sur les données.

### Contexte

Le composant scripté reçoit un arbre à deux niveaux et doit rendre un résultat par valeur du second niveau, toutes origines confondues.

### Énoncé

> L'arbre porte trois valeurs au premier niveau de chemin et quatre au second, soit une branche par combinaison. Le remappage ne conserve que le second niveau. Donnez le nombre de branches obtenues.

### Ce qui vous est fourni

La structure de l'arbre de départ et la règle de remappage.

### Ce qui est attendu

4 branches — une par valeur du second niveau.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`DV-08_sujet.gh`

### Barème

1 point si le nombre de branches est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
