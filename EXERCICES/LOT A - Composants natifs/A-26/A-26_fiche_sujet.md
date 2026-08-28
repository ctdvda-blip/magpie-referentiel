# A-26 — Ordre d'évaluation et recalcul

**Question charnière Magpie** · Lot A — Découverte des composants natifs

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | A5 · Comportements implicites |
| **Référence au référentiel** | REF-056, REF-090 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-24 |
| **Mode de validation** | — (non notée) |
| **Gamification associée** | G-17 Quiz éclair |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## POURQUOI CE N'EST PAS UN EXERCICE

L'énoncé d'origine demandait de **constater un comportement** du logiciel plutôt que de produire un résultat. La réponse s'obtenait en sachant, non en construisant : c'est le signal qu'on paie le coût d'un exercice pour la valeur d'une question.

L'énoncé initial est conservé ci-dessous à titre d'archive.

> *Deux branches indépendantes du graphe produisent chacune un résultat. Dans quel ordre sont-elles évaluées ? Réponds par QCM et justifie en modifiant un seul slider.*

## CONTEXTE

Deux branches indépendantes cohabitent sur un même canvas.

## LA QUESTION

Deux branches indépendantes produisent chacune un résultat. Dans quel ordre sont-elles évaluées ?
a) De gauche à droite, selon leur position sur le canvas.
b) Dans l'ordre où elles ont été créées.
c) L'ordre entre deux branches indépendantes n'est pas défini ; seules les dépendances imposent un ordre. ← réponse
d) Simultanément, sur plusieurs cœurs.

Valeur diagnostique : (a) est la croyance qui pousse à ranger le canvas pour « corriger » un résultat — un temps perdu considérable. (d) fait espérer un gain de performance qui n'existe pas ici.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.

## DÉMONSTRATION FACULTATIVE

Le fichier `A-26_complet.gh` reste disponible comme support de démonstration au vidéoprojecteur. Il n'est pas à faire construire.

**1.** Activer le widget Profiler (menu Display) pour lire les temps par composant.

**2.** Modifier un slider et observer que seule la branche dépendante se recalcule.

**3.** Déplacer physiquement un composant : aucun changement d'ordre.

**4.** Conclure : l'ordre suit les dépendances de données.
