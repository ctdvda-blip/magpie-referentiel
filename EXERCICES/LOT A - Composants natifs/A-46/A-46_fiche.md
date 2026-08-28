# A-46 — Détecter une collision

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A10 · Surfaces et solides |
| **Référence au référentiel** | REF-072 |
| **Compétence visée** | Identifier, dans un ensemble, les objets qui interfèrent avec un volume donné. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-45 |
| **Mode de validation** | SetEquality — tolérance — |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-01 Score visible |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Identifier, dans un ensemble, les objets qui interfèrent avec un volume donné.

### Contexte

Un gabarit de passage doit rester libre : tout élément qui y pénètre est à reprendre.

### Énoncé

> Quinze blocs sont disposés autour du gabarit de passage fourni. Indiquez combien d'entre eux empiètent sur ce gabarit.

### Ce qui vous est fourni

15 blocs et un volume de gabarit internalisés.

### Ce qui est attendu

Le nombre de blocs en interférence avec le gabarit.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SetEquality**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-46_sujet.gh`

### Barème

1 point si les bons blocs sont identifiés.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-46_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Collision One|Many, mais en inversant les rôles attendus : les blocs sur Collider, le gabarit sur Obstacles.

**Étape 2.** Grafter l'entrée Collider : chaque bloc se retrouve seul dans sa branche.

**Étape 3.** La sortie Collision donne alors un booléen PAR BLOC ; aplatir le résultat avec Flatten Tree.

**Étape 4.** Poser Dispatch : les blocs sur List, les booléens sur Pattern.

**Étape 5.** Afficher la sortie A avec un Custom Preview alimenté par un Colour Swatch rouge.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Obtenir une réponse unique pour l'ensemble au lieu d'une réponse par bloc : le test renvoie un verdict global si on ne lui présente pas les blocs un à un.

### Pièges fréquents

- Brancher le gabarit sur Collider et les blocs sur Obstacles sans grafter : le composant ne renvoie alors qu'un SEUL booléen global et l'index du PREMIER bloc touché, pas la liste complète. C'est le piège central de cet exercice.
- Confondre la sortie Collision (booléens) et la sortie Index.
- Collision One|Many ne détecte pas le simple contact tangent.
- Croire que Collision Many|Many convient : ce composant n'a qu'une entrée et teste un ensemble contre lui-même.

### Réglages à poser à la main

Ces réglages ne peuvent pas être enregistrés dans le fichier : ils sont à poser dans Grasshopper.

- Colour Swatch : régler la couleur sur rouge par double-clic.

### Pour aller plus loin

- Compter les collisions avec Mass Addition.
- Décaler automatiquement les blocs en collision.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-46_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-46_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-46.json` | Descripteur pour le plugin Magpie |
| `A-46_fiche.md` | La présente fiche |
| `A-46_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-46_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-46_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
