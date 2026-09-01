# DV-05 — Ce que la compilation change vraiment

**Question charnière Magpie** · Lot DV — Développement, scripting et API

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | DV3 · Compilation et IDE |
| **Référence au référentiel** | REF-096 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Expert |
| **Durée cible** | 8 min |
| **Prérequis** | DV-02 |
| **Mode de validation** | — (non notée) |
| **Gamification associée** | G-14 Question éclair |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## POURQUOI CE N'EST PAS UN EXERCICE

L'énoncé d'origine demandait de **constater un comportement** du logiciel plutôt que de produire un résultat. La réponse s'obtenait en sachant, non en construisant : c'est le signal qu'on paie le coût d'un exercice pour la valeur d'une question.

L'énoncé initial est conservé ci-dessous à titre d'archive.

> **

## CONTEXTE

Un composant scripté rend le service attendu depuis six mois, dans une trentaine de définitions. La question de le compiler se pose.

## LA QUESTION

Votre composant scripté fonctionne. Que vous apporte d'abord sa compilation en .gha ?
a) Il ira plus vite : le code n'est plus interprété.
b) Le code source devient illisible pour l'utilisateur.
c) Il se distribue et se corrige en un seul endroit, sans que personne n'ouvre les définitions. ← réponse
d) Il pourra enfin appeler RhinoCommon.

Valeur diagnostique : (a) et (d) révèlent qu'on n'a pas situé ce qu'un composant scripté sait déjà faire — il appelle RhinoCommon, et sa lenteur vient presque toujours de l'algorithme, pas de l'interprétation. (b) est accessoire, et faux au sens strict : un .gha se décompile. Le vrai gain est de DISTRIBUTION : trente définitions qui embarquaient chacune leur copie du script deviennent trente définitions qui pointent vers une version unique.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
