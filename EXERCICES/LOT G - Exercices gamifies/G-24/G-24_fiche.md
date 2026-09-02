# G-24 — Le retour sonore

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G6 · Sensations et immersion |
| **Référence au référentiel** | REF-027, REF-061 |
| **Compétence visée** | Composer trois conditions par un ET logique et compter ce qui les satisfait toutes. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 10 min |
| **Prérequis** | A-31 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Associer un retour immédiat perceptible à chaque action correcte ou fautive.

### Contexte

Le retour sonore associe une perception immédiate à chaque action. Il fait sentir la différence entre « une condition vraie » et « toutes les conditions vraies », qui reste abstraite tant qu'on ne l'entend pas.

### Énoncé

> Câble la définition de sorte qu'un son de validation retentisse quand la condition est vraie et un son d'erreur quand elle est fausse. Puis résous l'énigme logique qui déclenche le son de victoire.

### Ce qui vous est fourni

Deux fichiers audio référencés et un cluster de logique incomplet.

### Ce qui est attendu

8 — le nombre de valeurs qui remplissent les trois conditions.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-24_sujet.gh`

### Barème

2 points : 1 pour le câblage sonore, 1 pour l'énigme.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-24_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Brancher le booléen de condition sur un Stream Filter à deux entrées sonores.

**Étape 2.** Vérifier l'alternance en basculant manuellement le toggle.

**Étape 3.** Résoudre l'énigme logique du cluster : trouver la combinaison de trois booléens rendant la sortie vraie.

**Étape 4.** Soumettre la combinaison.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Enchaîner les trois conditions par un OU au lieu d'un ET : 71 valeurs sur 80 au lieu de 8. Le son de victoire retentit alors presque toujours, ce qui le rend inaudible — et c'est exactement pourquoi un retour sonore mal câblé est pire que pas de retour.

### Pièges fréquents

- Son déclenché à chaque recalcul et non au seul changement d'état.
- Chemin de fichier audio absolu, non transportable d'un poste à l'autre.

### Pourquoi ce jeu de données

Quatre-vingts valeurs de 1 à 400. Les trois conditions se recouvrent partiellement — tout multiple de 4 ne finit pas par 0, 4 ou 8 — de sorte que le ET et le OU donnent des comptes très éloignés, 8 contre 71 : l'erreur ne peut pas passer pour du bruit.

### Limite de la correction automatique

> Le câblage SONORE lui-même n'est pas vérifié : Grasshopper joue les sons par un plugin externe, et aucune valeur n'en sort. Seule l'énigme logique qui les déclenche est corrigée.

### Pour aller plus loin

- Palette sonore par thématique.
- Son de compte à rebours dans les dix dernières secondes.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-24_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-24_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-24.json` | Descripteur pour le plugin Magpie |
| `G-24_fiche.md` | La présente fiche |
| `G-24_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-24_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-24_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
