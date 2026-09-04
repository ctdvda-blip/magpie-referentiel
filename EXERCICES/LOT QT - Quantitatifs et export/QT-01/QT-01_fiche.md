# QT-01 — Le métré d'un plancher bois

**Fiche d'exercice Magpie** · Lot QT — Quantitatifs, chiffrage et export

| | |
|---|---|
| **Thématique** | QT1 · Quantitatifs et chiffrage |
| **Référence au référentiel** | REF-082, REF-084 |
| **Compétence visée** | Établir un métré à partir de sections et de longueurs, en distinguant les grandeurs qui s'additionnent de celles qui ne s'additionnent pas. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-47 |
| **Mode de validation** | NumericTolerance — tolérance 0,0001 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-01 Score visible |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir un métré à partir de sections et de longueurs, en distinguant les grandeurs qui s'additionnent de celles qui ne s'additionnent pas.

### Contexte

Un plancher bois se commande au volume de bois, mais se pose au linéaire : le métré doit rendre les deux.

### Énoncé

> Les 20 solives du plancher vous sont fournies avec leur section et leur longueur. Donnez le volume total de bois, en mètres cubes.

### Ce qui vous est fourni

Les 20 sections, en millimètres, et les 20 longueurs correspondantes, en millimètres.

### Ce qui est attendu

Le volume total de bois, en mètres cubes, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`QT-01_sujet.gh`

### Barème

1 point si le volume est juste à 0,0001 m³ près.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `QT-01_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Calculer l'aire de chaque section, en millimètres carrés.

**Étape 2.** Multiplier chaque aire par la longueur de SA solive, terme à terme.

**Étape 3.** Sommer les vingt volumes.

**Étape 4.** Convertir en mètres cubes : diviser par un milliard.

**Étape 5.** Contrôler l'ordre de grandeur : un plancher de cette taille représente quelques dixièmes de mètre cube.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Multiplier la section moyenne par la longueur totale. Les sections varient, et la moyenne ne rend pas le produit : l'écart est faible, l'ordre de grandeur reste juste, et le chiffrage est faux de quelques pour cent — le genre d'erreur qu'on ne voit jamais.

### Pièges fréquents

- Appariement des deux listes : sections et longueurs doivent rester au même rang.
- Conversion : un mètre cube vaut un milliard de millimètres cubes, pas un million.

### Pourquoi ce jeu de données

Cinq sections courantes de charpente, réparties de façon que la corrélation entre section et longueur soit positive : la moyenne sous-estime alors le volume, toujours dans le même sens.

### Limite de la correction automatique

> Le volume est celui du BOIS FINI. Le débit part de sections brutes plus grandes — rabotage, tolérance de sciage — et le volume commandé au scieur dépasse celui-ci de 8 à 15 % selon l'essence et le corroyage.

### Pour aller plus loin

- Ajouter 10 % de chutes et refaire le chiffrage.
- Sortir aussi le linéaire total et comparer les deux unités.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `QT-01_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `QT-01_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `QT-01.json` | Descripteur pour le plugin Magpie |
| `QT-01_fiche.md` | La présente fiche |
| `QT-01_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `QT-01_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `QT-01_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
