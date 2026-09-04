# GP-04 — SubD ou NURBS ?

**Question charnière Magpie** · Lot GP — Géométrie paramétrique appliquée

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | GP4 · Maillages et SubD |
| **Référence au référentiel** | REF-077, REF-078 |
| **Case Bloom (révisée)** | Évaluer × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 7 min |
| **Prérequis** | GP-03 |
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

Une poignée de meuble doit être dessinée en forme libre, puis usinée.

## LA QUESTION

Vous devez dessiner une poignée de forme libre, qui sera ensuite usinée à partir d'un modèle exact. Par quoi commencez-vous ?
a) Directement en NURBS, puisque c'est ce qu'il faut à la fin.
b) En maillage, plus simple à déformer.
c) Peu importe, les trois sont équivalents.
d) En SubD pour la recherche de forme, converti en NURBS pour l'usinage. ← réponse

Valeur diagnostique : (a) est le réflexe de qui connaît la contrainte de sortie et pas les outils de forme — on y passe un temps considérable à recaler des points de contrôle. (b) donne une forme facile à modeler et impossible à usiner proprement. La bonne réponse tient à ce que SubD et NURBS ne s'opposent pas : l'un sert la conception, l'autre la fabrication, et la conversion est prévue pour.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
