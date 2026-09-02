# G-09 — Le composant caché

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G2 · Exploration et découverte |
| **Référence au référentiel** | REF-028, REF-056 |
| **Compétence visée** | Explorer un canvas pour y trouver ce qui a été rendu invisible, puis exploiter la donnée trouvée. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 10 min |
| **Prérequis** | A-05 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 1 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Encourager l'exploration du canvas et des menus contextuels.

### Contexte

Le composant caché récompense l'exploration des menus contextuels — l'endroit où se trouvent la moitié des réponses aux questions que les débutants posent.

### Énoncé

> Un composant a été rendu invisible sur ce canvas. Trouve-le, révèle-le et recopie dans le Panel le mot de passe qu'il contient.

### Ce qui vous est fourni

Un canvas contenant un composant masqué via le menu contextuel.

### Ce qui est attendu

8 538 — la somme des quatorze valeurs que porte le composant masqué.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-09_sujet.gh`

### Barème

1 point, plus badge secret EXPLORATEUR.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-09_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Utiliser Ctrl+A pour sélectionner tout le contenu du canvas et repérer l'élément invisible.

**Étape 2.** Ou utiliser Metahopper pour lister tous les composants du document.

**Étape 3.** Réactiver son affichage via le menu contextuel.

**Étape 4.** Lire le mot de passe et le recopier dans le Panel de réponse.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Chercher le composant à l'œil en déplaçant les autres, au lieu d'ouvrir Edit > Arrange ou de tout sélectionner par Ctrl+A : un composant masqué reste SÉLECTIONNABLE, il ne disparaît que de l'aperçu. C'est la leçon de l'exercice, et elle sert ensuite tous les jours.

### Pièges fréquents

- Chercher uniquement à l'écran sans utiliser la sélection globale.
- Recopier le mot de passe avec un espace parasite.

### Pourquoi ce jeu de données

Quatorze valeurs de trois chiffres, sans motif : la somme 8 538 ne se retrouve ni de tête ni par un raccourci. Il faut réellement avoir mis la main sur le composant.

### Limite de la correction automatique

> « Masqué » veut dire aperçu désactivé, pas protégé. Rien n'empêche d'ouvrir le fichier dans un éditeur de texte et d'y lire les quatorze valeurs — l'exercice suppose la bonne foi, comme tous les jeux de piste.

### Pour aller plus loin

- Plusieurs easter eggs dans un même parcours.
- Mot de passe déblocant un exercice bonus.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-09_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-09_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-09.json` | Descripteur pour le plugin Magpie |
| `G-09_fiche.md` | La présente fiche |
| `G-09_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-09_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-09_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
