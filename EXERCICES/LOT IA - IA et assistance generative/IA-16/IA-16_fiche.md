# IA-16 — Ce qu'un agent ne fait pas sans vous

**Question charnière Magpie** · Lot IA — IA et assistance générative

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | IA7 · Agents et protocoles |
| **Référence au référentiel** | REF-138 |
| **Case Bloom (révisée)** | Évaluer × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 8 min |
| **Prérequis** | IA-15 |
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

L'agent pilote Grasshopper et Rhino par un pont ouvert sur votre poste. Il a accès au document, aux fichiers, et à ce que vous lui laissez.

## LA QUESTION

Vous ouvrez un pont agentique sur votre poste de travail. Quel garde-fou pose-t-on en premier ?
a) Relire chaque commande avant de la laisser passer.
b) Limiter l'agent aux composants natifs.
c) Travailler sur une copie du document, et exiger une confirmation pour tout ce qui écrit hors de cette copie. ← réponse
d) Journaliser les appels pour pouvoir les rejouer.

Valeur diagnostique : (a) est le réflexe naturel et il ne tient pas — un agent émet des dizaines d'appels par minute, personne ne les relit. (d) est utile mais ne protège de rien : un journal se lit après. (b) confond la puissance de l'agent et son droit d'écriture. Le seul garde-fou qui tienne est celui qui reste efficace quand on cesse de regarder : borner ce qui est réversible, et faire confirmer le reste.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
