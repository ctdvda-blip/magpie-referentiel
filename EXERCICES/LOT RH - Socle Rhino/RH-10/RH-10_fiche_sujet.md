# RH-10 — Ce que l'export STL perd

**Question charnière Magpie** · Lot RH — Socle Rhino

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | RH5 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-024 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | RH-08 |
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

Une pièce parfaitement lisse dans Rhino ressort facettée de l'imprimante.

## LA QUESTION

Votre cylindre est parfait dans Rhino, et il sort facetté de l'imprimante. Pourquoi ?
a) Le format STL ne connaît que des triangles : la conversion a échantillonné la surface, et la finesse de cet échantillonnage est un réglage. ← réponse
b) L'imprimante n'est pas assez précise.
c) Le fichier a été enregistré en basse résolution.
d) Il fallait exporter en OBJ.

Valeur diagnostique : (b) fait accuser la machine et acheter du matériel qui ne changera rien. (d) est faux pour la même raison — l'OBJ maille aussi. La bonne réponse déplace l'attention vers le seul endroit où l'on peut agir : les réglages de maillage au moment de l'export.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
