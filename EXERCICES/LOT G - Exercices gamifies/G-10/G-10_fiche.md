# G-10 — Le coffre à butin

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G2 · Exploration et découverte |
| **Référence au référentiel** | REF-068, REF-045 |
| **Compétence visée** | Identifier les extrêmes d'un jeu de valeurs et en rendre les INDEX plutôt que les valeurs. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 14 min |
| **Prérequis** | A-14, A-39 |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Introduire une part d'aléatoire maîtrisé pour renouveler l'intérêt.

### Contexte

Le coffre à butin introduit une part d'aléatoire maîtrisé : le contenu change à chaque tirage, la méthode pour le trouver non. C'est ce qui permet de rejouer l'exercice.

### Énoncé

> Vingt coffres sont disposés en trame. Trois contiennent une récompense, désignés par le tirage aléatoire de graine 7. Identifie-les et affiche leurs index.

### Ce qui vous est fourni

Une trame de 20 positions et un Random de graine imposée.

### Ce qui est attendu

Les index des trois coffres pleins : 7, 13, 16.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SetEquality**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-10_sujet.gh`

### Barème

3 points, 1 par coffre correctement identifié.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-10_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Random avec Seed = 7 et Number = 3 dans le domaine 0 à 19.

**Étape 2.** Arrondir les valeurs avec Round pour obtenir des index entiers.

**Étape 3.** Poser List Item ou Cull Index pour marquer les coffres correspondants.

**Étape 4.** Afficher les index dans un Panel.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Rendre les valeurs — 87, 95, 93 — au lieu des index. Un index désigne une POSITION ; c'est lui qui permet ensuite d'aller chercher le coffre correspondant dans la trame, et les deux sont ici du même ordre de grandeur, ce qui rend la confusion invisible au premier regard.

### Pièges fréquents

- Changer la graine : le résultat ne correspond plus à l'attendu.
- Random produit des décimales : sans arrondi les index sont invalides.

### Pourquoi ce jeu de données

Vingt contenus de 10 à 99. Les trois plus riches — 95, 93 et 87 — sont nettement détachés du quatrième (86), de sorte que le seuil ne prête pas à discussion. Aucun ex æquo : l'ensemble des trois index est unique.

### Limite de la correction automatique

> L'aléatoire est FIGÉ par la graine. Deux apprenants trouvent les mêmes coffres, ce qui rend l'exercice corrigeable mais retire au loot box sa surprise dès la deuxième session.

### Pour aller plus loin

- Récompense de rareté variable.
- Coffre à ouvrir en résolvant une énigme.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-10_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-10_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-10.json` | Descripteur pour le plugin Magpie |
| `G-10_fiche.md` | La présente fiche |
| `G-10_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-10_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-10_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
