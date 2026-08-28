# A-07 — Quand la conversion échoue

**Question charnière Magpie** · Lot A — Découverte des composants natifs

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | A2 · Types, conversion et valeurs |
| **Référence au référentiel** | REF-041 |
| **Case Bloom (révisée)** | Comprendre × factuelle |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-06 |
| **Mode de validation** | — (non notée) |
| **Gamification associée** | G-20 Erreur volontaire à débusquer |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## POURQUOI CE N'EST PAS UN EXERCICE

L'énoncé d'origine demandait de **constater un comportement** du logiciel plutôt que de produire un résultat. La réponse s'obtenait en sachant, non en construisant : c'est le signal qu'on paie le coût d'un exercice pour la valeur d'une question.

L'énoncé initial est conservé ci-dessous à titre d'archive.

> *Un Panel contenant le texte « douze » alimente une Addition. Qu'affiche la sortie ? Corrige le montage pour que l'addition renvoie 15 sans supprimer le Panel.*

## CONTEXTE

Une donnée saisie en toutes lettres remonte d'un tableur mal rempli.

## LA QUESTION

Un composant passe en orange et sa sortie est vide. Que faites-vous en premier ?
a) Vous le supprimez et le reposez.
b) Vous survolez la pastille pour lire le message, qui nomme l'entrée fautive. ← réponse
c) Vous rebranchez toutes les entrées.
d) Vous relancez le recalcul du document.

Valeur diagnostique : (a) et (c) sont le réflexe de l'apprenant qui ne sait pas que Grasshopper dit précisément ce qui ne va pas ; l'orange signale un avertissement, pas une panne.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.

## DÉMONSTRATION FACULTATIVE

Le fichier `A-07_complet.gh` reste disponible comme support de démonstration au vidéoprojecteur. Il n'est pas à faire construire.

**1.** Survoler le composant orange pour lire l'avertissement de conversion.

**2.** Remplacer le contenu du Panel par 12 (valeur numérique).

**3.** Vérifier que le composant redevient normal et affiche 15.

**4.** Retenir : un texte non numérique produit une valeur nulle, pas un zéro.
