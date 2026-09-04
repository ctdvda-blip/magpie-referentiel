# G-19 — Le composant mystère

**Question charnière Magpie** · Lot G — Exercices gamifiés

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | G4 · Connaissance et mémorisation |
| **Référence au référentiel** | REF-028, REF-042 |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Intermédiaire |
| **Durée cible** | 12 min |
| **Prérequis** | A-05, A-11 |
| **Mode de validation** | — (non notée) |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## POURQUOI CE N'EST PAS UN EXERCICE

L'énoncé d'origine demandait de **constater un comportement** du logiciel plutôt que de produire un résultat. La réponse s'obtenait en sachant, non en construisant : c'est le signal qu'on paie le coût d'un exercice pour la valeur d'une question.

L'énoncé initial est conservé ci-dessous à titre d'archive.

> *Quatre clusters anonymes transforment les données. Observe leurs entrées et sorties, puis identifie le composant natif que chacun reproduit.*

## CONTEXTE

Reconnaître un composant à son comportement, c'est ce qu'on fait devant la définition d'un confrère. La boîte noire entraîne exactement ce geste.

## LA QUESTION

Quatre clusters anonymes transforment les données. Identifie le composant natif que chacun reproduit, puis applique-le au jeu de preuve et donne les quatre résultats.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.

## DÉMONSTRATION FACULTATIVE

Le fichier `G-19_complet.gh` reste disponible comme support de démonstration au vidéoprojecteur. Il n'est pas à faire construire.

**1.** Alimenter chaque cluster avec une liste simple de 1 à 5 et observer la sortie.

**2.** Répéter avec une liste contenant des doublons puis avec un arbre à deux branches.

**3.** Déduire la transformation opérée à partir des trois essais.

**4.** Sélectionner le nom dans la Value List correspondante.
