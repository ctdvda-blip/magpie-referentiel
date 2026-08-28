# A-48 — Courbure et point le plus proche

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A11 · Mesures géométriques |
| **Référence au référentiel** | REF-080 |
| **Compétence visée** | Analyser localement une courbe pour y localiser la zone la plus contraignante. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-35 |
| **Mode de validation** | NumericTolerance — tolérance 1 % |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-28 Avatar et personnalisation |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Analyser localement une courbe pour y localiser la zone la plus contraignante.

### Contexte

Un profilé cintré ne peut descendre sous un rayon de cintrage minimal : c'est le point le plus serré du tracé qui décide de la faisabilité.

### Énoncé

> Le tracé vous est fourni. Localisez son point le plus serré et donnez le rayon de cintrage à cet endroit.

### Ce qui vous est fourni

Une courbe libre internalisée.

### Ce qui est attendu

Le point de courbure maximale et son rayon de courbure.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 1 %.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-48_sujet.gh`

### Barème

1 point pour le point, 1 point pour le rayon.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-48_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Divide Curve avec 200 divisions pour échantillonner finement.

**Étape 2.** Poser Curvature sur ces paramètres : la sortie K donne le vecteur de courbure.

**Étape 3.** Poser Vector Length puis Sort List pour trouver la valeur maximale.

**Étape 4.** Le rayon vaut l'inverse de la courbure : poser Division avec 1 sur A.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Confondre courbure et rayon, qui varient en sens inverse : chercher le rayon maximal conduit au point le plus plat, c'est-à-dire exactement l'inverse de ce que la fabrication demande.

### Pièges fréquents

- Courbure nulle sur un segment droit : la division par zéro produit une valeur infinie.
- Échantillonnage trop grossier : le maximum réel est manqué.

### Réglages à poser à la main

Ces réglages ne peuvent pas être enregistrés dans le fichier : ils sont à poser dans Grasshopper.

- Remplacer le second Bounds par un Deconstruct Domain si le nom diffère : on cherche la borne haute du domaine des courbures.

### Pour aller plus loin

- Colorer la courbe selon sa courbure avec Gradient.
- Détecter les points d'inflexion.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-48_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-48_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-48.json` | Descripteur pour le plugin Magpie |
| `A-48_fiche.md` | La présente fiche |
| `A-48_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-48_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-48_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
