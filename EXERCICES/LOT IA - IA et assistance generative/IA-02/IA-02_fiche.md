# IA-02 — Le contexte technique manquant

**Question charnière Magpie** · Lot IA — IA et assistance générative

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | IA1 · Formuler et cadrer une demande |
| **Référence au référentiel** | REF-118 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | — |
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

Un assistant produit un code qui refuse de se compiler dans Rhino 8 alors qu'il semble correct.

## LA QUESTION

Vous demandez un composant Grasshopper à un assistant, sans autre précision. Le code obtenu ne compile pas. Quelle information manquait le plus probablement ?
a) La version de Rhino et la bibliothèque visée. ← réponse
b) Le nom que vous vouliez donner au composant.
c) La couleur de l'icône.
d) Rien : les assistants ne savent pas écrire de composant.

Valeur diagnostique : (d) est la conclusion qu'en tire l'apprenant découragé, et elle est fausse — le modèle a produit du code valide pour une autre version de l'API. Nommer la version déplace le problème de « l'outil ne marche pas » à « ma demande était incomplète », qui est la seule formulation sur laquelle on peut agir.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
