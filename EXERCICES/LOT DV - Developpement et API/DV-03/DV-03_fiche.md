# DV-03 — Ce que les librairies évitent d'écrire

**Question charnière Magpie** · Lot DV — Développement, scripting et API

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | DV2 · API et librairies |
| **Référence au référentiel** | REF-104, REF-105 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Expert |
| **Durée cible** | 8 min |
| **Prérequis** | DV-02 |
| **Mode de validation** | — (non notée) |
| **Gamification associée** | G-14 Question éclair |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## POURQUOI CE N'EST PAS UN EXERCICE

L'énoncé d'origine demandait de **constater un comportement** du logiciel plutôt que de produire un résultat. La réponse s'obtenait en sachant, non en construisant : c'est le signal qu'on paie le coût d'un exercice pour la valeur d'une question.

L'énoncé initial est conservé ci-dessous à titre d'archive.

> **

## CONTEXTE

Un besoin de géométrie de calcul — enveloppe convexe, triangulation — se présente dans un composant scripté.

## LA QUESTION

Vous avez besoin d'une triangulation dans un composant scripté. Par où commencez-vous ?
a) L'écrire : c'est un bon exercice.
b) Chercher si RhinoCommon la fournit déjà, puis une librairie éprouvée. ← réponse
c) La demander à un assistant, qui l'écrira vite.
d) Changer d'approche pour éviter d'en avoir besoin.

Valeur diagnostique : (c) est devenu le réflexe majoritaire et c'est le plus trompeur — un assistant produit vite une triangulation qui marche sur le cas d'essai et échoue sur les cas dégénérés, que trente ans de bibliothèque ont, eux, déjà rencontrés. La question ne porte pas sur la difficulté d'écrire, mais sur le coût de valider.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
