# DV-01 — Quand écrire du script plutôt que câbler

**Question charnière Magpie** · Lot DV — Développement, scripting et API

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | DV1 · Scripting dans Grasshopper |
| **Référence au référentiel** | REF-100 |
| **Case Bloom (révisée)** | Évaluer × conceptuelle |
| **Niveau** | Expert |
| **Durée cible** | 8 min |
| **Prérequis** | IA-04 |
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

Une partie de définition compte quarante composants pour une opération qui s'écrirait en cinq lignes.

## LA QUESTION

Quand vaut-il mieux écrire un composant scripté que câbler des composants natifs ?
a) Dès qu'on sait programmer : c'est toujours plus rapide.
b) Quand la logique est itérative ou conditionnelle, et que le câblage la rendrait illisible. ← réponse
c) Jamais : une définition doit rester lisible par des non-programmeurs.
d) Uniquement pour les performances.

Valeur diagnostique : (a) et (c) sont deux dogmes symétriques et également coûteux. Le premier produit des définitions que personne d'autre ne maintient ; le second fait câbler des boucles sur cinquante composants. Le critère utile est la lisibilité du résultat, pas la préférence de celui qui écrit.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
