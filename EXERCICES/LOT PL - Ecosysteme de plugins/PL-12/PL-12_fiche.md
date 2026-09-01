# PL-12 — Le plugin qui n'est plus maintenu

**Question charnière Magpie** · Lot PL — Écosystème de plugins

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | PL1 · Écosystème de plugins |
| **Référence au référentiel** | REF-039 |
| **Case Bloom (révisée)** | Évaluer × conceptuelle |
| **Niveau** | Intermédiaire |
| **Durée cible** | 8 min |
| **Prérequis** | PL-11 |
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

Le plugin sur lequel repose une définition de production n'a pas été mis à jour depuis trois ans.

## LA QUESTION

Une définition de production dépend d'un plugin abandonné depuis trois ans. Que faites-vous en premier ?
a) Chercher un plugin de remplacement équivalent.
b) Repérer ce que ce plugin fait réellement dans la définition, et si c'est encore indispensable. ← réponse
c) Figer la version de Rhino pour que rien ne bouge.
d) Réécrire la partie concernée en natif, sans attendre.

Valeur diagnostique : (c) est la réaction la plus répandue, et c'est un report de décision — figer Rhino gèle aussi tout le reste, et le problème revient dans un an, aggravé. (a) et (d) sont des solutions, mais on ne choisit pas une solution avant de savoir ce qu'on remplace : sur une définition ancienne, il est fréquent que le plugin ne serve plus qu'à une étape devenue inutile.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
