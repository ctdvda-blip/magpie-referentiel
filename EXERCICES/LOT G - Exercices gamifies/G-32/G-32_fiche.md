# G-32 — Les indices payants

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G7 · Régularité et communauté |
| **Référence au référentiel** | REF-052, REF-049, REF-050 |
| **Compétence visée** | Restructurer un arbre pour atteindre une structure imposée, et savoir décrire cette structure par ses effectifs. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | A-20, A-21, A-23 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Responsabiliser l'apprenant sur le recours à l'aide.

### Contexte

L'économie d'indices responsabilise : demander de l'aide a un coût, ne pas en demander quand on est bloqué en a un autre. L'apprenant apprend à arbitrer, ce qui est le vrai sujet.

### Énoncé

> Restructure l'arbre fourni pour atteindre la structure cible. Quatre indices sont disponibles, du plus général au plus précis, coûtant respectivement 1, 2, 3 et 4 points sur un total de 12.

### Ce qui vous est fourni

Un arbre source, une structure cible affichée et quatre groupes d'indices repliés.

### Ce qui est attendu

La structure cible, branche par branche : 4, 1, 0, 3, 2, 2, 3, 2, 2.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-32_sujet.gh`

### Barème

12 points, moins le coût des indices consultés.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-32_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Comparer les chemins source et cible dans le Param Viewer.

**Étape 2.** Identifier l'opération nécessaire : ajout de niveau, suppression, permutation.

**Étape 3.** Appliquer Path Mapper avec les masques adaptés.

**Étape 4.** Vérifier la structure obtenue avant de soumettre.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Rendre les VALEURS retenues au lieu des effectifs par branche. La structure d'un arbre se décrit par le nombre d'éléments de chaque branche — c'est ce que montre le Panel, et c'est ce qui permet de comparer deux arbres sans comparer leur contenu.

### Pièges fréquents

- Utiliser Flatten puis Graft pour reconstruire : la structure obtenue diffère de la cible.
- Consommer les quatre indices avant d'avoir essayé.

### Pourquoi ce jeu de données

Soixante-douze valeurs en neuf branches de huit. Une branche est VIDE — zéro multiple de 5 — et deux branches ont le même effectif : la structure ne peut pas se deviner par régularité, et la branche vide vérifie qu'on ne supprime pas les branches sans contenu.

### Limite de la correction automatique

> Les effectifs disent la FORME de l'arbre, pas son contenu. Deux arbres de mêmes effectifs mais de valeurs différentes passeraient tous deux — le contrôle porte sur la restructuration, qui est le sujet de l'exercice.

### Pour aller plus loin

- Indices sous forme de vidéo courte.
- Indices offerts par une série de bonnes réponses.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-32_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-32_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-32.json` | Descripteur pour le plugin Magpie |
| `G-32_fiche.md` | La présente fiche |
| `G-32_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-32_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-32_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
