# AV-09 — Ce qu'une simulation ne dit pas

**Question charnière Magpie** · Lot AV — Algorithmique avancée

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | AV3 · Simulation physique |
| **Référence au référentiel** | REF-156 |
| **Case Bloom (révisée)** | Évaluer × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 8 min |
| **Prérequis** | AV-08 |
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

La forme relâchée est belle, stable, et le client la trouve convaincante. Reste à savoir ce qu'elle établit.

## LA QUESTION

Votre relaxation a convergé sur une forme de couverture tendue. Qu'avez-vous établi ?
a) Que la structure tient : la forme est en équilibre.
b) Rien d'utilisable : il faut un logiciel de calcul.
c) Une géométrie d'équilibre sous les hypothèses posées — ni sections, ni contraintes admissibles, ni dimensionnement. ← réponse
d) Que la forme est optimale.

Valeur diagnostique : (a) est l'erreur coûteuse, et elle est facile — « équilibre » est le mot qu'emploie le moteur, et ce n'est pas celui de l'ingénieur. Une forme d'équilibre dit où va l'effort, pas s'il passe. (d) confond équilibre et optimum : la relaxation ne compare rien. (b) jette ce qui a le plus de valeur — la forme obtenue est précisément ce qu'un logiciel de calcul demandera en entrée.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
