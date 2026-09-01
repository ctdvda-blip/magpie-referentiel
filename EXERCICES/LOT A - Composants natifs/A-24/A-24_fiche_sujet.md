# A-24 — Correspondance par défaut

**Question charnière Magpie** · Lot A — Découverte des composants natifs

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | A5 · Comportements implicites |
| **Référence au référentiel** | REF-053 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-10 |
| **Mode de validation** | — (non notée) |
| **Gamification associée** | G-09 Récompense cachée |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## POURQUOI CE N'EST PAS UN EXERCICE

L'énoncé d'origine demandait de **constater un comportement** du logiciel plutôt que de produire un résultat. La réponse s'obtenait en sachant, non en construisant : c'est le signal qu'on paie le coût d'un exercice pour la valeur d'une question.

L'énoncé initial est conservé ci-dessous à titre d'archive.

> *Une liste de 10 nombres et une liste de 4 nombres entrent dans une même Addition. Combien de résultats sortent ? Affiche le compte dans un Panel, puis explique comment les 6 derniers ont été calculés.*

## CONTEXTE

Deux listes de tailles différentes arrivent dans un même opérateur.

## LA QUESTION

Une liste de 10 valeurs et une liste de 4 valeurs entrent dans un même opérateur, sans réglage particulier. Combien de résultats sortent ?
a) 4 — la liste la plus courte impose sa longueur.
b) 10 — la liste la plus courte est complétée par répétition de son dernier élément. ← réponse
c) 40 — toutes les combinaisons sont calculées.
d) 14 — les deux listes sont mises bout à bout.

Valeur diagnostique : (a) est la représentation fausse la plus répandue, et elle est dangereuse — elle fait croire qu'un appariement déséquilibré se voit, alors qu'il produit silencieusement six résultats calculés sur une valeur répétée. (c) confond le comportement par défaut avec le croisement explicite, qui fait l'objet de l'exercice suivant.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.

## DÉMONSTRATION FACULTATIVE

Le fichier `A-24_complet.gh` reste disponible comme support de démonstration au vidéoprojecteur. Il n'est pas à faire construire.

**1.** Brancher List Length sur la sortie de l'Addition.

**2.** Relier vers un Panel : 10 résultats, et non 4.

**3.** Comparer les 6 derniers résultats à la liste longue : ils ont tous été additionnés au MÊME nombre, le dernier de la liste courte.

**4.** Constater qu'aucun avertissement n'est émis : ce complètement est silencieux.

**5.** Retenir : le comportement par défaut est la correspondance sur la liste la plus longue, la liste courte étant prolongée par son dernier élément.
