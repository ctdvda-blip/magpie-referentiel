# GP-09 — Ce que les contraintes imposent

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP3 · Plan paramétrique |
| **Référence au référentiel** | REF-146 |
| **Compétence visée** | Déduire d'un jeu de contraintes la dimension qui n'est pas donnée, plutôt que de la mesurer sur le dessin. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | GP-05 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-08 Relevé contradictoire |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Déduire d'un jeu de contraintes la dimension qui n'est pas donnée, plutôt que de la mesurer sur le dessin.

### Contexte

Le joue de meuble suit la pente du rampant. Le plan donne la base, la hauteur et l'angle ; la petite base, elle, se déduit et doit se recalculer si l'angle change.

### Énoncé

> Le joue est un trapèze rectangle de 2 400 mm de base et 1 800 mm de hauteur, dont le fuyant fait 68° avec l'horizontale. Donnez la longueur de la petite base, en millimètres.

### Ce qui vous est fourni

La base, la hauteur et l'angle du fuyant.

### Ce qui est attendu

1 672,75 mm — la petite base, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-09_sujet.gh`

### Barème

1 point si la petite base est juste à 0,01 mm près.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `GP-09_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Convertir l'angle en radians.

**Étape 2.** Calculer le RECUL horizontal du fuyant : hauteur divisée par la tangente de l'angle.

**Étape 3.** Le retrancher à la base.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Retrancher la LONGUEUR du fuyant (1 941 mm) au lieu de son recul horizontal (727 mm), ce qui donne 459 mm. La valeur reste positive et plausible sur un plan ; la pièce, elle, sort de l'atelier avec 1,2 m de moins.

### Pièges fréquents

- Prendre la longueur du fuyant pour son recul.
- Multiplier par la tangente au lieu de diviser.
- Oublier la conversion en radians.

### Pourquoi ce jeu de données

Un angle de 68° donne un recul de 727 mm et un fuyant de 1 941 mm : les deux sont du même ordre que les cotes du meuble, donc tous deux crédibles. C'est ce qui rend la confusion durable.

### Pour aller plus loin

- Faire varier l'angle et vérifier que la petite base suit.
- Trouver l'angle qui annule la petite base.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `GP-09_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `GP-09_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `GP-09.json` | Descripteur pour le plugin Magpie |
| `GP-09_fiche.md` | La présente fiche |
| `GP-09_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `GP-09_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `GP-09_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
