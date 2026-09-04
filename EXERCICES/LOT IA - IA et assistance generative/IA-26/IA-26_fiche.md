# IA-26 — Transposer, et le prouver sur un second jeu

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA2 · Composants scriptés assistés |
| **Référence au référentiel** | REF-122, REF-123 |
| **Compétence visée** | Établir qu'un script porté vers un autre langage produit exactement la même chose, sur un jeu qu'il n'a pas servi à écrire. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 18 min |
| **Prérequis** | IA-06 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-19 Le composant mystère |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir qu'un script porté vers un autre langage produit exactement la même chose, sur un jeu qu'il n'a pas servi à écrire.

### Contexte

Reprendre une définition ancienne maintenue en VB.NET, c'est la porter sans changer un résultat dont personne ne se souvient de la règle exacte.

### Énoncé

> Le composant existant produit les sommes cumulées d'une liste. Faites-le porter vers un autre langage, puis appliquez les deux versions au jeu de preuve fourni et donnez les quatorze valeurs obtenues.

### Ce qui vous est fourni

Le composant d'origine et le jeu de preuve de quatorze valeurs.

### Ce qui est attendu

Les quatorze cumuls : 213, 230, 656, 1 011, 1 306, 1 560, 1 711, 1 801, 2 150, 2 234, 2 390, 2 524, 2 989, 3 141.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-26_sujet.gh`

### Barème

1 point si les quatorze valeurs concordent dans l'ordre.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-26_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Lire ce que fait le composant d'origine sur un petit jeu.

**Étape 2.** Faire produire la version dans l'autre langage.

**Étape 3.** Appliquer les deux au jeu de preuve.

**Étape 4.** Comparer élément par élément, dans l'ordre.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Vérifier le portage sur le jeu qui a servi à l'écrire. Les deux versions s'y accordent forcément — c'est ce jeu-là que l'assistant avait sous les yeux. La preuve n'a de valeur que sur des données qu'il n'a pas vues.

### Pièges fréquents

- Comparer des ensembles au lieu de listes ordonnées.
- Prouver le portage sur le jeu d'origine.

### Pourquoi ce jeu de données

Quatorze valeurs de 15 à 480, sans ordre. Le cumul est strictement croissant : un décalage d'un rang se voit immédiatement, et une somme oubliée décale tout ce qui suit. C'est ce qui rend la comparaison sévère.

### Limite de la correction automatique

> L'égalité sur quatorze valeurs établit que les deux versions s'accordent SUR CE JEU. Un cas limite absent — liste vide, valeur négative, dépassement de capacité — peut encore les séparer, et c'est le défaut classique du portage.

### Pour aller plus loin

- Ajouter une valeur négative au jeu et voir si l'accord tient.
- Porter vers un troisième langage.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-26_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-26_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-26.json` | Descripteur pour le plugin Magpie |
| `IA-26_fiche.md` | La présente fiche |
| `IA-26_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-26_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-26_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
