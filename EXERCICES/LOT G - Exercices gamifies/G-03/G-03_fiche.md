# G-03 — Contre la montre

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G1 · Progression et récompense |
| **Référence au référentiel** | REF-042, REF-043 |
| **Compétence visée** | Enchaîner cinq extractions de liste de natures différentes sans confondre rang, position et valeur. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 6 min |
| **Prérequis** | A-11, A-12 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 12 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Travailler la vitesse d'exécution sur des gestes déjà maîtrisés.

### Contexte

Le contre-la-montre travaille la vitesse sur des gestes déjà acquis. Il ne s'adresse pas à qui découvre : il sert à rendre automatique ce qui est encore réfléchi.

### Énoncé

> Cinq extractions de listes à réaliser en moins de 180 secondes. Le chronomètre démarre à l'ouverture de l'exercice et s'affiche en haut du canvas.

### Ce qui vous est fourni

Cinq listes internalisées et cinq paramètres de réponse.

### Ce qui est attendu

Les cinq extractions, dans l'ordre : 806, 729, 965, 148, 578.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-03_sujet.gh`

### Barème

5 points, plus 3 points de bonus si le temps cible est tenu.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-03_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Lire les cinq consignes affichées dans le Scribble.

**Étape 2.** Traiter chaque liste avec le composant adapté sans chercher l'élégance.

**Étape 3.** Brancher les cinq réponses.

**Étape 4.** Valider avant la fin du compte à rebours.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Confondre le rang et la valeur : rendre 3 au lieu de 806 pour « l'élément d'index 3 ». Sous chronomètre, cette confusion coûte plus que le temps qu'elle fait gagner.

### Pièges fréquents

- Perdre du temps à ranger le canvas au lieu de répondre.
- Réponse correcte soumise après l'échéance : la validation reste acquise, le bonus est perdu.

### Pourquoi ce jeu de données

Cinq listes de 8 ou 9 valeurs, de longueurs inégales pour que le médian ne tombe pas au même endroit. Les cinq extractions sont de cinq natures différentes — index, dernier, maximum, minimum, médian — de sorte qu'un seul composant ne peut pas toutes les faire.

### Limite de la correction automatique

> Le chronomètre n'entre PAS dans la validation : une réponse juste hors délai reste juste. Il ne pilote que le bonus, et c'est délibéré — un exercice qui refuse une bonne réponse pour un retard n'enseigne plus rien.

### Pour aller plus loin

- Mode survie où chaque erreur retire 15 secondes.
- Classement des temps entre apprenants.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-03_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-03_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-03.json` | Descripteur pour le plugin Magpie |
| `G-03_fiche.md` | La présente fiche |
| `G-03_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-03_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-03_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
