# MP-03 — Une définition qui réagit

**Question charnière Magpie** · Lot MP — Méthode, performance et évènements

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | MP1 · Chronologie et évènements |
| **Référence au référentiel** | REF-091, REF-092 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 8 min |
| **Prérequis** | MP-02 |
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

On voudrait qu'une définition réagisse à une touche ou à un clic dans la vue.

## LA QUESTION

Grasshopper recalcule quand une donnée change. Comment lui faire prendre en compte un évènement clavier ou souris ?
a) C'est impossible, Grasshopper n'écoute rien.
b) En relançant la définition à la main.
c) Par un composant qui expose l'évènement comme une donnée, laquelle déclenche alors le recalcul habituel. ← réponse
d) En écrivant un plugin, il n'y a pas d'autre voie.

Valeur diagnostique : (a) et (d) sont deux façons de renoncer trop tôt. Le point à faire passer est conceptuel : le modèle de Grasshopper reste le même — une donnée change, l'aval se recalcule. L'évènement n'est pas une exception au modèle, c'est une donnée de plus.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
