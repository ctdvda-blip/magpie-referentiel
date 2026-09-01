# FA-05 — Ce qui se met à plat, et ce qui ne s'y met pas

**Question charnière Magpie** · Lot FA — Aide à la fabrication

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | FA2 · Déroulé et mise à plat |
| **Référence au référentiel** | REF-159 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 8 min |
| **Prérequis** | FA-03 |
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

La commande porte sur une coque à double courbure. Le logiciel propose un déroulé, et il le fait sans se plaindre.

## LA QUESTION

Le logiciel a déroulé votre coque à double courbure sans message. Qu'en concluez-vous ?
a) Que la surface est développable, sinon il aurait refusé.
b) Que le déroulé est juste aux tolérances près du logiciel.
c) Qu'il faut découper la surface en bandes pour être tranquille.
d) Qu'il a produit une APPROXIMATION, dont l'écart se chiffre et doit être vérifié. ← réponse

Valeur diagnostique : (a) prend l'absence de message pour une validation — or aucun outil ne refuse de dérouler, ils déforment. (b) confond la tolérance de calcul et l'erreur de modèle : ici l'écart ne vient pas d'un arrondi, il vient de ce que la surface ne se met pas à plat. (c) est le bon REMÈDE, proposé avant le diagnostic — et découper en bandes ne dispense pas de chiffrer ce qu'on perd.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
