# A-06 — Conversion implicite Number vers Integer

**Question charnière Magpie** · Lot A — Découverte des composants natifs

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | A2 · Types, conversion et valeurs |
| **Référence au référentiel** | REF-040 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-01 |
| **Mode de validation** | — (non notée) |
| **Gamification associée** | G-18 Vrai / Faux à élimination |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## POURQUOI CE N'EST PAS UN EXERCICE

L'énoncé d'origine demandait de **constater un comportement** du logiciel plutôt que de produire un résultat. La réponse s'obtenait en sachant, non en construisant : c'est le signal qu'on paie le coût d'un exercice pour la valeur d'une question.

L'énoncé initial est conservé ci-dessous à titre d'archive.

> *Le slider vaut 4,6. Il alimente l'entrée Count d'un Series qui attend un entier. Combien d'éléments la série contient-elle ? Affiche le nombre dans un Panel et explique la règle appliquée.*

## CONTEXTE

Un nombre de travées calculé produit une valeur décimale, alors que le composant en aval attend un compte entier.

## LA QUESTION

Une valeur décimale de 4,6 alimente une entrée qui n'accepte que des entiers. Que vaut l'entier réellement utilisé ?
a) 4 — la partie entière est conservée.
b) 5 — la valeur est toujours arrondie au supérieur.
c) Le composant se met en erreur.
d) 5 — la valeur est arrondie au plus proche. ← réponse

Valeur diagnostique : c'est la question la plus utile du lot, parce que (a) et (d) donnent tous deux la bonne réponse pour 4,6 et se trompent pour 4,4. Un apprenant qui coche (d) « réussit » et garde une règle fausse. Sur un approvisionnement — où il faut au moins autant de pièces — c'est bien un arrondi au supérieur qu'il faut, et il doit être posé explicitement : la conversion implicite ne le fera pas.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.

## DÉMONSTRATION FACULTATIVE

Le fichier `A-06_complet.gh` reste disponible comme support de démonstration au vidéoprojecteur. Il n'est pas à faire construire.

**1.** Brancher un List Length sur la sortie de Series.

**2.** Relier vers un Panel : la série contient 5 éléments.

**3.** Faire varier le slider entre 4,4 et 4,6 pour observer la bascule.

**4.** Conclure : Grasshopper arrondit au plus proche, il ne tronque pas.
