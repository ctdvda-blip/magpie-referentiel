# IA-24 — Le composant qui n'apparaît pas

**Question charnière Magpie** · Lot IA — IA et assistance générative

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | IA3 · Développement de plugins assisté |
| **Référence au référentiel** | REF-127 |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 8 min |
| **Prérequis** | IA-23 |
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

L'agent annonce que la compilation a réussi. Grasshopper n'affiche aucun nouveau composant, et ne dit rien.

## LA QUESTION

Compilation réussie, aucun composant dans l'onglet, aucun message. Que regardez-vous en premier ?
a) Le code du composant : il manque sans doute une méthode.
b) Où le fichier compilé a été déposé, et si Rhino regarde ce dossier. ← réponse
c) La version du SDK utilisée pour compiler.
d) Le journal de Grasshopper, qui doit contenir l'erreur.

Valeur diagnostique : l'absence de MESSAGE est l'information. Un composant mal écrit produit une erreur ; un composant que Rhino n'a jamais chargé ne produit rien. (a) et (c) supposent que le fichier a été lu, ce que rien n'établit. (d) est un bon réflexe, mais un journal vide dit la même chose que le silence : personne n'a essayé de charger quoi que ce soit.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
