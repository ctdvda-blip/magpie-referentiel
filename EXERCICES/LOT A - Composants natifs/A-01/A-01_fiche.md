# A-01 — Premier flux de données

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A1 · Interface, flux de données et paramètres |
| **Référence au référentiel** | REF-027, REF-028 |
| **Compétence visée** | Raccorder deux sources sur les deux entrées d'un même opérateur et lire la valeur produite. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | — |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Raccorder deux sources sur les deux entrées d'un même opérateur et lire la valeur produite.

### Contexte

Un ensemble menuisé se compose d'une imposte et d'un châssis superposés ; leur hauteur cumulée doit remplir exactement la baie.

### Énoncé

> La baie mesure 2 400 mm de haut. Une valeur de hauteur vous est déjà fournie pour l'imposte. Ajoutez une seconde valeur réglable pour le châssis, faites-en la somme, et réglez les deux hauteurs pour que la baie soit exactement remplie.

### Ce qui vous est fourni

Un Number Slider (0-100, valeur 17) déjà placé.

### Ce qui est attendu

La somme des deux hauteurs vaut exactement 2 400.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-01_sujet.gh`

### Barème

1 point si la valeur du Panel vaut 42.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-01_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser un second Number Slider (menu Params > Input) et l'étendre de 0 à 100.

**Étape 2.** Poser un composant Addition (Maths > Operators).

**Étape 3.** Relier le premier slider sur l'entrée A, le second sur l'entrée B.

**Étape 4.** Relier la sortie R vers un Panel (Params > Input > Panel).

**Étape 5.** Ajuster les deux curseurs jusqu'à lire 42 dans le Panel.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Brancher les deux sources sur la même entrée : l'opérateur additionne alors les deux valeurs sur une seule entrée et laisse l'autre vide. Le résultat est faux d'un facteur qui trahit la confusion entre « deux câbles » et « deux entrées ».

### Pièges fréquents

- Relier deux câbles sur la même entrée A : Grasshopper additionne alors les deux valeurs sur A et laisse B vide.
- Slider réglé en entier alors que la cible demande une décimale.

### Pour aller plus loin

- Remplacer Addition par Subtraction et viser -42.
- Ajouter un troisième slider avec Mass Addition.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-01_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-01_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-01.json` | Descripteur pour le plugin Magpie |
| `A-01_fiche.md` | La présente fiche |
| `A-01_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-01_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-01_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
