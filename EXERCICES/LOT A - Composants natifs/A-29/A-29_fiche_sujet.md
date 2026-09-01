# A-29 — Comparer deux valeurs

**Question charnière Magpie** · Lot A — Découverte des composants natifs

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | A7 · Portes logiques |
| **Référence au référentiel** | REF-059 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | A-08 |
| **Mode de validation** | — (non notée) |
| **Gamification associée** | G-18 Vrai / Faux à élimination |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## POURQUOI CE N'EST PAS UN EXERCICE

L'énoncé d'origine demandait de **constater un comportement** du logiciel plutôt que de produire un résultat. La réponse s'obtenait en sachant, non en construisant : c'est le signal qu'on paie le coût d'un exercice pour la valeur d'une question.

L'énoncé initial est conservé ci-dessous à titre d'archive.

> *Compare les valeurs 0,1 + 0,2 et 0,3 avec Equality. Le résultat est-il True ? Corrige le montage pour qu'il le devienne.*

## CONTEXTE

Deux cotes calculées par des chemins différents devraient coïncider.

## LA QUESTION

Vous comparez 0,1 + 0,2 à 0,3 par un test d'égalité stricte. Le résultat est faux. Pourquoi ?
a) Grasshopper arrondit les affichages à trois décimales.
b) Le test d'égalité ne fonctionne pas sur les décimaux.
c) Il faut convertir en entiers avant de comparer.
d) Les nombres à virgule sont codés en binaire : la somme vaut 0,30000000000000004. ← réponse

Valeur diagnostique : c'est la connaissance qui, non transmise, produit des heures de débogage sur des géométries « qui devraient se toucher ». Elle explique aussi pourquoi le mode de validation tolérant existe.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.

## DÉMONSTRATION FACULTATIVE

Le fichier `A-29_complet.gh` reste disponible comme support de démonstration au vidéoprojecteur. Il n'est pas à faire construire.

**1.** Constater que Equality renvoie False en raison de la représentation des décimaux.

**2.** Remplacer Equality par Similarity (Maths > Operators).

**3.** Régler l'entrée de tolérance sur 0,001.

**4.** La sortie passe à True.
