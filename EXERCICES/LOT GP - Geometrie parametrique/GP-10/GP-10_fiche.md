# GP-10 — Courbe, surface, solide ou maillage

**Question charnière Magpie** · Lot GP — Géométrie paramétrique appliquée

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | GP5 · Synthèse géométrie |
| **Référence au référentiel** | REF-147 |
| **Case Bloom (révisée)** | Évaluer × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 8 min |
| **Prérequis** | GP-03 |
| **Mode de validation** | — (non notée) |
| **Gamification associée** | G-14 Question éclair |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## POURQUOI CE N'EST PAS UN EXERCICE

L'énoncé d'origine demandait de **constater un comportement** du logiciel plutôt que de produire un résultat. La réponse s'obtenait en sachant, non en construisant : c'est le signal qu'on paie le coût d'un exercice pour la valeur d'une question.

L'énoncé initial est conservé ci-dessous à titre d'archive.

> **

## CONTEXTE

La même pièce peut se traiter de quatre façons. Chacune répond à des questions différentes, et coûte un prix différent.

## LA QUESTION

Vous devez chiffrer le VOLUME de matière d'une pièce moulurée. Sur quelle représentation travaillez-vous ?
a) Le maillage : c'est le plus rapide à obtenir.
b) Les courbes de profil : elles suffisent, le volume s'en déduit.
c) Un solide fermé : seul un volume étanche a un volume. ← réponse
d) Peu importe : Grasshopper convertit tout seul.

Valeur diagnostique : (a) est la réponse la plus fréquente et elle n'est pas absurde — un maillage fermé a bien un volume, mais approché, et sa finesse décide de l'erreur. (b) confond ce qui ENGENDRE la forme et ce qui la mesure. (d) est le vrai piège : Grasshopper convertit en effet, silencieusement, et le résultat dépend alors d'une conversion que personne n'a choisie. Le choix se fait sur ce qu'on veut MESURER.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.
