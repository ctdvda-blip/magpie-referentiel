# G-29 — Le défi du jour

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G7 · Régularité et communauté |
| **Référence au référentiel** | REF-047, REF-079 |
| **Compétence visée** | Trier une série et en extraire la médiane, en distinguant médiane et moyenne. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 10 min |
| **Prérequis** | A-13, A-47 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 10 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Installer une habitude de pratique par une tâche courte et renouvelée.

### Contexte

Le défi du jour installe une habitude : dix minutes, une question, tous les jours. Sa vertu n'est pas la difficulté mais la régularité.

### Énoncé

> Un défi court, différent chaque jour, tiré d'une banque de 30 micro-tâches. Celui du jour : trie les pièces par longueur et donne la longueur médiane.

### Ce qui vous est fourni

Une banque de micro-tâches et un jeu de données du jour.

### Ce qui est attendu

1 119 mm — la longueur médiane.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-29_sujet.gh`

### Barème

1 point par défi, badge à 7 jours consécutifs.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-29_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Lire l'énoncé du jour affiché dans le Scribble.

**Étape 2.** Mesurer les longueurs avec Length.

**Étape 3.** Trier avec Sort List.

**Étape 4.** Extraire l'élément médian avec List Length, une division par 2 et List Item.

**Étape 5.** Soumettre la valeur.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Rendre la MOYENNE, 1 203 mm, au lieu de la médiane. Les deux répondent à « la longueur typique » et ne diffèrent que de 84 mm ici — assez pour fausser un débit, pas assez pour alerter. La moyenne suit les extrêmes, la médiane non.

### Pièges fréquents

- Confondre médiane et moyenne.
- Liste de taille paire : la médiane est la moyenne des deux valeurs centrales.

### Pourquoi ce jeu de données

Quarante-et-une pièces — un nombre IMPAIR, de sorte que la médiane est une valeur réellement présente dans la liste et non une demi-somme. Les longueurs vont de 120 à 2 400 mm, assez étalées pour que moyenne et médiane s'écartent nettement.

### Limite de la correction automatique

> Le défi est présenté comme « différent chaque jour ». La définition livrée en fige UN : la banque de trente micro-tâches annoncée par la fiche reste à écrire, et l'exercice ne la fournit pas.

### Pour aller plus loin

- Série de sept jours donnant un badge hebdomadaire.
- Défi collectif avec objectif commun.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-29_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-29_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-29.json` | Descripteur pour le plugin Magpie |
| `G-29_fiche.md` | La présente fiche |
| `G-29_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-29_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-29_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
