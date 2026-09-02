# G-11 — Les mots croisés des composants

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G2 · Exploration et découverte |
| **Référence au référentiel** | REF-057, REF-058 |
| **Compétence visée** | Retrouver le nom anglais des composants natifs à partir de leur effet, et contrôler sa grille par une mesure globale. |
| **Case Bloom (révisée)** | Se rappeler × factuelle |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | A-27, A-28 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 10 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Consolider le vocabulaire des composants natifs par un jeu de lettres.

### Contexte

Le vocabulaire des composants est la barrière la plus basse et la plus haute : on ne trouve pas ce dont on ignore le nom. Les mots croisés le travaillent sans réciter.

### Énoncé

> Complète la grille de mots croisés dessinée sur le canvas. Chaque définition renvoie au nom anglais d'un composant natif. Assemble ensuite les lettres des cases grisées pour former le mot final.

### Ce qui vous est fourni

Une grille dessinée en Text Tag 3D et une liste de définitions en Scribble.

### Ce qui est attendu

43 — la somme des longueurs des sept mots placés.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-11_sujet.gh`

### Barème

1 point par définition, 3 points pour le mot final.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-11_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Résoudre chaque définition : par exemple « éclate une liste en branches » donne GRAFT.

**Étape 2.** Saisir chaque réponse dans le Panel correspondant.

**Étape 3.** Extraire les lettres des cases grisées avec List Item aux index indiqués.

**Étape 4.** Assembler avec Concatenate et soumettre le mot final.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Écrire `SORT` pour « ranger une liste » alors que la grille attend `SERIES` pour « produire une suite régulière » : la définition parle de PRODUIRE, pas de ranger. Une case de trop ou de moins fait tomber la somme, et c'est ce qui la signale.

### Pièges fréquents

- Répondre en français alors que les noms de composants sont en anglais.
- Index de cases grisées comptés à partir de 1.

### Pourquoi ce jeu de données

Sept mots de 4 à 9 lettres, tous des composants natifs réellement employés dans le référentiel. La somme 43 ne se devine pas : elle exige les sept mots, et un seul faux la décale.

### Limite de la correction automatique

> La somme des longueurs ne dit pas que les mots sont les BONS : deux mots de même longueur se substituent sans qu'elle bouge. C'est un contrôle de cohérence, pas une correction lettre à lettre — le mot final grisé, lui, se lit sur la fiche.

### Pour aller plus loin

- Grille thématique par domaine du référentiel.
- Version mots mêlés.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-11_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-11_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-11.json` | Descripteur pour le plugin Magpie |
| `G-11_fiche.md` | La présente fiche |
| `G-11_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-11_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-11_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
