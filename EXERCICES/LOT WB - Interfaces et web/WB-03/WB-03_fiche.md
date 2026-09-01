# WB-03 — Rhino sans Rhino

**Question charnière Magpie** · Lot WB — Interfaces, web et interopérabilité

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | WB3 · Interopérabilité |
| **Référence au référentiel** | REF-111, REF-112 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Expert |
| **Durée cible** | 8 min |
| **Prérequis** | WB-02 |
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

Une application métier doit exploiter la géométrie de Rhino sans que l'utilisateur ouvre Rhino.

## LA QUESTION

Vous voulez faire tourner une définition Grasshopper depuis une application web, sans interface Rhino. Que cherchez-vous ?
a) Rhino.Compute, qui expose le moteur de calcul comme un service appelable à distance. ← réponse
b) Rhino.Inside, qui charge Rhino dans un autre logiciel hôte.
c) Un export en maillage, qui suffit toujours.
d) Les deux font la même chose.

Valeur diagnostique : (b) et (d) confondent deux réponses à deux besoins différents — Rhino.Inside fait cohabiter Rhino avec Revit ou AutoCAD sur le même poste ; Rhino.Compute met le moteur au bout d'un appel réseau. Se tromper de l'un pour l'autre fait partir sur une architecture entière qu'il faudra défaire.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
