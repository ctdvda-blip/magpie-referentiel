# A-03 — Internaliser une donnée

**Question charnière Magpie** · Lot A — Découverte des composants natifs

> Cet item **n'est pas un exercice noté**. Il porte une connaissance nécessaire, mais qui s'acquiert et se vérifie par une question, non par un montage — la construire dans Grasshopper mesurerait la mémoire, pas la compétence.

| | |
|---|---|
| **Thématique** | A1 · Interface, flux de données et paramètres |
| **Référence au référentiel** | REF-027 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-02 |
| **Mode de validation** | — (non notée) |
| **Gamification associée** | G-19 Le composant mystère |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## POURQUOI CE N'EST PAS UN EXERCICE

L'énoncé d'origine demandait de **constater un comportement** du logiciel plutôt que de produire un résultat. La réponse s'obtenait en sachant, non en construisant : c'est le signal qu'on paie le coût d'un exercice pour la valeur d'une question.

L'énoncé initial est conservé ci-dessous à titre d'archive.

> *Le point vert est produit par un Construct Point. Fige-le dans un paramètre Point autonome puis supprime la chaîne amont : le point doit rester affiché.*

## CONTEXTE

Un fond de plan doit être transmis à un confrère sans la chaîne de calcul qui l'a produit.

## LA QUESTION

Vous figez un point dans un paramètre autonome, puis vous supprimez toute la chaîne qui l'avait produit. Le point reste affiché. Pourquoi ?
a) La donnée a été recopiée dans le paramètre, qui ne dépend plus de rien. ← réponse
b) Grasshopper garde en mémoire le dernier calcul effectué.
c) Le paramètre reconstruit le point à chaque ouverture du fichier.
d) L'affichage est un reste à l'écran, il disparaîtra au prochain recalcul.

Valeur diagnostique : (b) et (d) révèlent qu'on confond persistance et cache d'affichage ; (c) qu'on croit le paramètre encore lié à sa source. Aucune de ces confusions ne se verrait dans un exercice où le montage fonctionne.

## COMMENT L'EMPLOYER

- **Avant** l'exercice qui mobilise cette connaissance, pas après : elle en est un prérequis.
- Poser la question à main levée, relever la répartition des réponses, et n'expliquer que si une réponse fausse est majoritaire.
- La valeur est dans la **mauvaise** réponse : elle nomme la représentation à corriger.

## DÉMONSTRATION FACULTATIVE

Le fichier `A-03_complet.gh` reste disponible comme support de démonstration au vidéoprojecteur. Il n'est pas à faire construire.

**1.** Poser un paramètre Point (Params > Geometry > Point).

**2.** Relier la sortie du Construct Point vers ce paramètre.

**3.** Clic droit sur le paramètre > Internalise data.

**4.** Supprimer le Construct Point et les trois sliders.

**5.** Vérifier que le point reste affiché : la donnée est désormais portée par le paramètre.
