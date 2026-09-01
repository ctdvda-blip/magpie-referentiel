# A-05 — Lire ce qui circule dans un câble

**Question charnière Magpie** · Lot A — Découverte des composants natifs

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | A1 · Interface, flux de données et paramètres |
| **Référence au référentiel** | REF-027, REF-028 |
| **Case Bloom (révisée)** | Comprendre × factuelle |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | A-01 |
| **Mode de validation** | — (non notée) |
| **Gamification associée** | G-17 Quiz éclair |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## POURQUOI CE N'EST PAS UN EXERCICE

L'énoncé d'origine demandait de **constater un comportement** du logiciel plutôt que de produire un résultat. La réponse s'obtenait en sachant, non en construisant : c'est le signal qu'on paie le coût d'un exercice pour la valeur d'une question.

L'énoncé initial est conservé ci-dessous à titre d'archive.

> *Un câble transporte une donnée inconnue. Sans modifier le graphe, indique dans un Panel le nombre d'éléments qu'il transporte.*

## CONTEXTE

Reprise d'une définition écrite par un tiers, dont on ignore ce que transportent les liaisons.

## LA QUESTION

Une liaison transporte une donnée que vous n'avez pas produite. Sans rien modifier, où lisez-vous d'un coup d'œil le nombre d'éléments qu'elle transporte, leur type et leur structure ?
a) En ouvrant les propriétés du composant aval.
b) En survolant la sortie du composant amont. ← réponse
c) En branchant obligatoirement un afficheur.
d) Cette information n'est pas accessible sans calcul.

Valeur diagnostique : (c) révèle qu'on croit devoir modifier le graphe pour l'inspecter — le réflexe qui fait casser les définitions des autres ; (d) qu'on ignore l'existence de l'infobulle.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.

## DÉMONSTRATION FACULTATIVE

Le fichier `A-05_complet.gh` reste disponible comme support de démonstration au vidéoprojecteur. Il n'est pas à faire construire.

**1.** Poser un Param Viewer et le brancher sur le câble à inspecter.

**2.** Basculer le Param Viewer en mode texte pour lire la structure.

**3.** Poser List Length (Sets > List) sur le même câble.

**4.** Relier la sortie L vers un Panel.
