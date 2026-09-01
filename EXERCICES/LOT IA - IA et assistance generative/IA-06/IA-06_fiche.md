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

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-06_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> Les seize sommes cumulées, de 3,42 à 68,92, dans cet ordre — identiques à celles de l'original.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Faire lire le composant d'origine à l'assistant, en fournissant le code, pas une description de ce qu'il fait.

**Étape 2.** Demander une transposition à l'identique, en signalant les cas limites à préserver.

**Étape 3.** Installer la version portée à côté de l'original, sans supprimer ce dernier.

**Étape 4.** Brancher les deux sur les mêmes données et comparer les sorties élément par élément.

**Étape 5.** Ne retirer l'original qu'une fois l'équivalence établie.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Vérifier l'équivalence sur la seule longueur des deux listes, ou sur leurs premières valeurs. Deux implémentations peuvent diverger sur un cas limite — une liste vide, une valeur négative — et coïncider partout ailleurs.

### Pièges fréquents

- Supprimer l'original avant d'avoir comparé : on perd la référence.
- Décrire le composant au lieu de fournir son code : l'assistant réinvente une logique voisine mais différente.

### Pourquoi ce jeu de données

Le jeu comprend une valeur limite et une valeur négative, pour que deux implémentations plausibles puissent diverger et que la comparaison ait un sens.

### Pour aller plus loin

- Comparer aussi les temps de calcul sur un jeu de données plus grand.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-06_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-06_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-06.json` | Descripteur pour le plugin Magpie |
| `IA-06_fiche.md` | La présente fiche |
| `IA-06_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-06_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-06_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
