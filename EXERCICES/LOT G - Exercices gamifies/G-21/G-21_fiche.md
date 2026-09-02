# G-21 — Le golf de composants

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G5 · Performance et compétition |
| **Référence au référentiel** | REF-068, REF-043, REF-046 |
| **Compétence visée** | Produire une géométrie régulière par le chemin le plus économe, en cherchant le composant qui fait le travail de plusieurs. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | A-16, A-39 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Chercher la solution la plus économe, exercice d'élégance algorithmique.

### Contexte

Le golf de composants entraîne l'élégance, qui n'est pas une coquetterie : une définition de sept composants se relit, se transmet et se modifie, une de trente non.

### Énoncé

> Produis la géométrie cible avec le moins de composants possible. Le par du trou est fixé à 7 composants. Sliders et Panels comptent.

### Ce qui vous est fourni

Une géométrie cible en filigrane.

### Ce qui est attendu

1 582,75 mm — le périmètre de l'étoile à neuf branches, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-21_sujet.gh`

### Barème

Par 7 : 3 points au par, 5 points sous le par, 1 point au-dessus.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-21_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Analyser la cible pour identifier la répétition sous-jacente.

**Étape 2.** Préférer un composant de réseau à une suite de transformations.

**Étape 3.** Utiliser les expressions dans les entrées pour éviter des composants de calcul.

**Étape 4.** Compter les composants et chercher à descendre sous le par.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Construire l'étoile par dix-huit segments explicites : le périmètre est juste, le score est catastrophique — dix-huit composants pour un par de sept. `Polygon` en mode étoile fait le même travail en un.

### Pièges fréquents

- Optimiser au détriment de la lisibilité au point de rendre la solution invérifiable.
- Oublier que les sliders comptent dans le total.

### Pourquoi ce jeu de données

Neuf branches, rayon 240, creux 46 : un nombre IMPAIR de branches, de sorte que l'étoile n'a pas d'axe de symétrie horizontal et ne peut pas se construire par simple miroir. Le périmètre irrationnel exclut toute réponse devinée.

### Limite de la correction automatique

> Le périmètre valide la GÉOMÉTRIE, pas le score. Le nombre de composants se compte à l'œil sur le canvas — sliders et panneaux compris, comme l'énoncé le précise.

### Pour aller plus loin

- Parcours de 9 trous de difficulté croissante.
- Classement de la promotion sur chaque trou.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-21_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-21_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-21.json` | Descripteur pour le plugin Magpie |
| `G-21_fiche.md` | La présente fiche |
| `G-21_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-21_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-21_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
