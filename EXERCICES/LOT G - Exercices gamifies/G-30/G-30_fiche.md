# G-30 — Le relais à deux

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G7 · Régularité et communauté |
| **Référence au référentiel** | REF-088, REF-048 |
| **Compétence visée** | Structurer des données en branches puis les traiter branche par branche, de façon qu'un tiers puisse reprendre le travail. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | B-05, A-21 |
| **Mode de validation** | NumericTolerance — tolérance 0.0001 |
| **Solution de référence** | 30 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Travailler la lisibilité et la transmissibilité d'une définition.

### Contexte

Le relais mesure ce qu'aucun exercice individuel ne mesure : la lisibilité. Une définition qu'un binôme ne peut pas reprendre est une définition perdue, quelle que soit sa justesse.

### Énoncé

> Première moitié : construis la structure de données jusqu'au point de passage marqué, en la rendant compréhensible par un tiers. Ton binôme reprendra le fichier pour la seconde moitié sans explication orale.

### Ce qui vous est fourni

Un énoncé en deux parties et un point de passage matérialisé sur le canvas.

### Ce qui est attendu

2 904,3333 — la somme des six moyennes, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-30_sujet.gh`

### Barème

4 points : 2 pour le résultat, 2 pour la lisibilité évaluée par le binôme.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-30_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Construire la première moitié en nommant explicitement toutes les sorties.

**Étape 2.** Regrouper les blocs fonctionnels avec Group et les titrer.

**Étape 3.** Documenter les hypothèses dans des Scribbles.

**Étape 4.** Transmettre le fichier au binôme.

**Étape 5.** Le binôme complète sans poser de question et signale les points restés obscurs.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Écarter les extrêmes sur l'ENSEMBLE des 96 valeurs avant de répartir en branches, au lieu d'écarter deux valeurs hautes et deux basses DANS CHAQUE branche. Les deux lectures sont défendables à l'oral ; une seule donne 2 904,33, et c'est exactement le genre d'ambiguïté qu'un relais révèle.

### Pièges fréquents

- Nommage par défaut conservé : le binôme perd du temps à décoder.
- Structure d'arbre non documentée au point de passage.

### Pourquoi ce jeu de données

Quatre-vingt-seize valeurs de 20 à 980, en six branches de seize. Écarter deux extrêmes de chaque côté laisse douze valeurs par branche : les six moyennes vont de 415,0 à 579,25 et sont toutes différentes, de sorte qu'une branche mal traitée se voit dans la somme.

### Limite de la correction automatique

> La somme valide le RÉSULTAT. La lisibilité — la moitié du barème — est évaluée par le binôme, et ne peut pas l'être autrement : aucune mesure automatique ne dit si une définition se comprend.

### Pour aller plus loin

- Relais à quatre sur un projet complet.
- Évaluation croisée de la lisibilité.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-30_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-30_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-30.json` | Descripteur pour le plugin Magpie |
| `G-30_fiche.md` | La présente fiche |
| `G-30_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-30_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-30_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
