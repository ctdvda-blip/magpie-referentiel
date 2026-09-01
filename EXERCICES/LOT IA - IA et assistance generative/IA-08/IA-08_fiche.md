# IA-08 — Le GUID que l'on ne régénère pas

**Question charnière Magpie** · Lot IA — IA et assistance générative

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | IA3 · Développement de plugins assisté |
| **Référence au référentiel** | REF-128 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 6 min |
| **Prérequis** | — |
| **Mode de validation** | — (non notée) |
| **Gamification associée** | G-14 Question éclair |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## POURQUOI CE N'EST PAS UN EXERCICE

L'énoncé d'origine demandait de **constater un comportement** du logiciel plutôt que de produire un résultat. La réponse s'obtenait en sachant, non en construisant : c'est le signal qu'on paie le coût d'un exercice pour la valeur d'une question.

L'énoncé initial est conservé ci-dessous à titre d'archive.

> **

## CONTEXTE

Une nouvelle version d'un plugin est distribuée à l'équipe.

## LA QUESTION

Vous diffusez la version 2 d'un plugin. Les définitions de vos collègues affichent désormais un composant manquant à la place du vôtre. Que s'est-il passé ?
a) Le nom du composant a changé.
b) Le GUID du composant a été régénéré. ← réponse
c) Le plugin n'est pas signé.
d) Ils doivent vider le cache de Grasshopper.

Valeur diagnostique : (a) est plausible et fausse — le nom peut changer sans rien casser, c'est le GUID qui identifie le composant dans les fichiers enregistrés. (d) est la réponse qui fait perdre une demi-journée à toute l'équipe. Cette connaissance ne se découvre pas en construisant : elle se paie, une fois, très cher.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
