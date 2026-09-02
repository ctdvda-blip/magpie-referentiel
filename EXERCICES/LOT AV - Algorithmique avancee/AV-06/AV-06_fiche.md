# AV-06 — Ce qu'on demande à l'optimisation

**Question charnière Magpie** · Lot AV — Algorithmique avancée

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | AV2 · Design génératif |
| **Référence au référentiel** | REF-153 |
| **Case Bloom (révisée)** | Évaluer × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 8 min |
| **Prérequis** | AV-03 |
| **Mode de validation** | — (non notée) |
| **Gamification associée** | G-14 Question éclair |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## POURQUOI CE N'EST PAS UN EXERCICE

L'énoncé d'origine demandait de **constater un comportement** du logiciel plutôt que de produire un résultat. La réponse s'obtenait en sachant, non en construisant : c'est le signal qu'on paie le coût d'un exercice pour la valeur d'une question.

L'énoncé initial est conservé ci-dessous à titre d'archive.

> **

## CONTEXTE

On veut « la meilleure façade ». L'outil, lui, veut une grandeur à minimiser et des bornes.

## LA QUESTION

Le client veut « la meilleure façade ». Que posez-vous d'abord ?
a) La grandeur à optimiser, ET les contraintes qui bornent les solutions admissibles. ← réponse
b) Les contraintes : ce que la façade ne doit en aucun cas faire.
c) Les paramètres à faire varier : c'est eux qui définissent l'espace.
d) Le nombre de générations, pour cadrer le temps de calcul.

Valeur diagnostique : (c) est le réflexe de celui qui pense en graphe plutôt qu'en projet — les paramètres viennent après, et mal choisis ils ne font qu'agrandir un espace vide. (b) est à moitié juste, et c'est ce qui la rend dangereuse : des contraintes sans objectif rendent un ensemble de solutions admissibles, dont aucune n'est meilleure. Un objectif mal posé produit une solution optimale à un problème que personne n'avait.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
