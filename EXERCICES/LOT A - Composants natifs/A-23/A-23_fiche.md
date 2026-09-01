# A-23 — Renommer les chemins avec Path Mapper

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A4 · Arbres de données |
| **Référence au référentiel** | REF-050 |
| **Compétence visée** | Réécrire les chemins d'un flux pour préparer une mise en correspondance. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 9 min |
| **Prérequis** | A-22 |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-32 Indices payants |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Réécrire les chemins d'un flux pour préparer une mise en correspondance.

### Contexte

Deux flux décrivent le même ouvrage, l'un rangé par niveau puis par file, l'autre par file puis par niveau : ils ne s'apparient pas.

### Énoncé

> Le flux fourni est rangé par niveau puis par file. Réorganisez-le par file puis par niveau, sans modifier les éléments eux-mêmes. Indiquez le nombre de branches obtenu.

### Ce qui vous est fourni

Un arbre internalisé de 12 branches à deux niveaux.

### Ce qui est attendu

Un flux dont les deux niveaux de chemin sont permutés.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SetEquality**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-23_sujet.gh`

### Barème

1 point si les chemins sont permutés.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-23_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Path Mapper et double-cliquer pour ouvrir l'éditeur.

**Étape 2.** Saisir le masque source {A;B}.

**Étape 3.** Saisir le masque cible {B;A}.

**Étape 4.** Valider et vérifier les chemins au Param Viewer.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Réordonner les éléments au lieu des chemins : le contenu bouge, la structure reste, et l'appariement échoue toujours.

### Pièges fréquents

- Oublier les accolades dans les masques.
- Utiliser des lettres différentes entre source et cible.

### Réglages à poser à la main

Ces réglages ne peuvent pas être enregistrés dans le fichier : ils sont à poser dans Grasshopper.

- Path Mapper : double-cliquer, saisir {A;B} en source et {B;A} en cible.
- Ne pas oublier les accolades, et réutiliser les mêmes lettres de part et d'autre.

### Note au formateur

> Le composant de réécriture des chemins est à lui seul la solution. Le maintenir comme exercice n'a de sens que si l'appariement qui suit est réellement demandé.

### Pour aller plus loin

- Fusionner deux niveaux avec le masque {A;B} vers {A}.
- Insérer un niveau constant avec {A} vers {0;A}.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-23_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-23_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-23.json` | Descripteur pour le plugin Magpie |
| `A-23_fiche.md` | La présente fiche |
| `A-23_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-23_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-23_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
