# RH-07 — Le fichier au mauvais millimètre

**Question charnière Magpie** · Lot RH — Socle Rhino

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | RH4 · Précision et unités |
| **Référence au référentiel** | REF-015, REF-017 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | — |
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

Un modèle reçu d'un partenaire arrive mille fois trop petit.

## LA QUESTION

Un fichier reçu s'affiche mille fois trop petit. Que faites-vous ?
a) Mettre le modèle à l'échelle 1000.
b) Vérifier d'abord l'unité du document : il a sans doute été modélisé en mètres et ouvert en millimètres. ← réponse
c) Changer l'unité du document, ce qui remet tout d'aplomb sans toucher au modèle.
d) Redemander le fichier.

Valeur diagnostique : (a) « marche » et laisse une tolérance absolue devenue mille fois trop grossière — les jonctions cesseront de se fermer sans qu'on comprenne pourquoi. (c) est presque juste : changer l'unité ne met pas le modèle à l'échelle, il faut choisir explicitement de le faire. C'est la nuance que la question sert à révéler.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
