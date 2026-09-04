# DV-06 — Le plugin qui parle aussi à Rhino

**Question charnière Magpie** · Lot DV — Développement, scripting et API

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | DV3 · Compilation et IDE |
| **Référence au référentiel** | REF-097, REF-099 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Expert |
| **Durée cible** | 8 min |
| **Prérequis** | DV-05 |
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

Le composant compilé rend service dans Grasshopper. On voudrait le même service depuis la ligne de commande Rhino.

## LA QUESTION

Vous avez un .gha qui marche. Que faut-il pour offrir le même service en commande Rhino ?
a) Rien : un .gha est déjà chargé par Rhino, la commande suit.
b) Réécrire le calcul en RhinoScript.
c) Un plugin .rhp qui déclare la commande, les deux partageant la même bibliothèque de calcul. ← réponse
d) Publier le .gha sur le gestionnaire de paquets.

Valeur diagnostique : (a) confond « chargé par Rhino » et « exposé dans Rhino » — un .gha vit dans Grasshopper, et la ligne de commande ne connaît pas ses composants. La bonne réponse vaut surtout pour ce qu'elle implique : le calcul ne se duplique pas, il se met dans une bibliothèque que les deux plugins référencent. Sans quoi la commande et le composant divergeront à la première correction.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
