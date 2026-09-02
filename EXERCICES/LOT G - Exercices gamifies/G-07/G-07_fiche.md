# G-07 — Une, deux ou trois étoiles

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G1 · Progression et récompense |
| **Référence au référentiel** | REF-067, REF-068 |
| **Compétence visée** | Construire une trame dont le nombre de modules découle du pas, et non l'inverse. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 15 min |
| **Prérequis** | A-39 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Distinguer la simple réussite de la réussite élégante.

### Contexte

Les étoiles distinguent la réussite de la réussite élégante. Une trame juste mais figée vaut une étoile ; la même trame paramétrique en vaut trois, et c'est la seule qui survivra au prochain changement de cote.

### Énoncé

> Produis la trame demandée. Une étoile pour un résultat juste, deux étoiles si la solution tient en moins de 12 composants, trois étoiles si elle reste juste après changement des paramètres de trame.

### Ce qui vous est fourni

Un module et une trame cible affichée en filigrane.

### Ce qui est attendu

143 modules — 13 par 11.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-07_sujet.gh`

### Barème

3 étoiles, validation dès la première.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-07_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Analyser la trame cible : nombre de rangs, nombre de colonnes, entraxes.

**Étape 2.** Choisir Rectangular Array plutôt qu'une suite de Move.

**Étape 3.** Paramétrer les entraxes par des sliders et non par des valeurs codées en dur.

**Étape 4.** Vérifier que le résultat reste juste après modification des sliders.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Diviser sans arrondir vers le bas : 3 400 / 260 = 13,08, et un quatorzième module sort du cadre. Sur les deux axes, l'erreur donne 14 × 12 = 168 au lieu de 143, soit 25 modules fantômes.

### Pièges fréquents

- Placer les modules un par un : le résultat est juste mais coûte 40 composants.
- Coder les entraxes en dur : la troisième étoile est perdue.

### Pourquoi ce jeu de données

3 400 / 260 et 2 100 / 185 tombent tous deux JUSTE au-dessus d'un entier — 13,08 et 11,35. C'est le cas où l'arrondi compte, et il a été choisi pour cela : avec des divisions exactes, l'erreur n'apparaîtrait pas.

### Limite de la correction automatique

> 143 dit que la trame a le bon COMPTE. La troisième étoile — rester juste après changement des paramètres — ne se vérifie pas automatiquement : c'est le formateur qui bouge les sliders.

### Pour aller plus loin

- Étoile bonus pour une solution sans Graft.
- Comparatif des solutions de la promotion.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-07_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-07_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-07.json` | Descripteur pour le plugin Magpie |
| `G-07_fiche.md` | La présente fiche |
| `G-07_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-07_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-07_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
