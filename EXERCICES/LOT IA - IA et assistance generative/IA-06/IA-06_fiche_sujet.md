# IA-06 — Transposer sans changer le résultat

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA2 · Composants scriptés assistés |
| **Référence au référentiel** | REF-122, REF-123 |
| **Compétence visée** | Porter un composant vers un autre langage et établir l'équivalence des deux versions. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | IA-04 |
| **Mode de validation** | ExactOrderedList — tolérance — |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-18 Duel de versions |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Porter un composant vers un autre langage et établir l'équivalence des deux versions.

### Contexte

Une définition ancienne repose sur un composant VB.NET que plus personne ne maintient ; il faut le porter sans changer un seul résultat.

### Énoncé

> Le composant existant produit une liste de valeurs. Faites-le porter vers un autre langage, puis établissez que les deux versions produisent exactement la même liste, dans le même ordre.

### Ce qui vous est fourni

Le composant d'origine, en place et fonctionnel, et le jeu de données qu'il traite.

### Ce qui est attendu

La liste ordonnée des sommes cumulées, telle que la produit le composant d'origine.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-06_sujet.gh`

### Barème

1 point si les deux listes sont identiques élément par élément.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
