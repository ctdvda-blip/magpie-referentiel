# GP-13 — La pièce qui enchaîne trois opérations

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP2 · Synthèse géométrie |
| **Référence au référentiel** | REF-073, REF-147, REF-148 |
| **Compétence visée** | Ordonner congé, perçage et épaississement de sorte que chaque opération reçoive ce dont elle a besoin. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 22 min |
| **Prérequis** | GP-11 |
| **Mode de validation** | NumericTolerance — tolérance 0.0001 |
| **Solution de référence** | 11 composants |
| **Gamification associée** | G-21 Le golf de composants |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Ordonner congé, perçage et épaississement de sorte que chaque opération reçoive ce dont elle a besoin.

### Contexte

Une platine de fixation se dessine à plat, se congé, se perce, puis s'épaissit. L'ordre n'est pas indifférent : épaissir d'abord oblige à percer un solide.

### Énoncé

> La platine mesure 420 × 260 mm, ses quatre angles portent un congé de 35 mm de rayon, et elle reçoit sept perçages de 26 mm de diamètre. Elle fait 18 mm d'épaisseur. Donnez son volume, en décimètres cubes.

### Ce qui vous est fourni

Les cotes de la platine, le rayon de congé, le diamètre et le nombre de perçages, l'épaisseur.

### Ce qui est attendu

1,8798 dm³, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-13_sujet.gh`

### Barème

1 point si le volume est juste à 0,0001 dm³.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `GP-13_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Calculer l'aire du rectangle plein.

**Étape 2.** Retrancher ce que les quatre congés enlèvent : (4 − π) r².

**Étape 3.** Retrancher l'aire des sept perçages.

**Étape 4.** Multiplier par l'épaisseur, puis convertir.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Oublier les congés : 1,8987 dm³. Un congé de rayon r retire à chaque angle la différence entre le carré de côté r et le quart de disque, soit (4 − π)r² pour les quatre — ici 1 052 mm², un demi-pour-cent du volume. C'est peu, et c'est précisément pourquoi on ne le voit pas.

### Pièges fréquents

- Oublier les congés.
- Retrancher quatre quarts de disque au lieu de la différence.

### Pourquoi ce jeu de données

Les congés retirent 1 052 mm² et les perçages 3 717 mm² : les seconds pèsent trois fois plus, ce qui rend l'oubli des premiers d'autant plus facile. Sept perçages, nombre impair, interdisent de retrouver l'aire par symétrie.

### Limite de la correction automatique

> Le volume suppose que les perçages ne rencontrent PAS les congés. Un huitième perçage placé dans un angle recouperait la matière déjà retirée, et la soustraction cesserait d'être une simple somme.

### Pour aller plus loin

- Faire varier le rayon de congé jusqu'à ce qu'il rencontre un perçage.
- Chercher l'épaisseur qui donne exactement 2 dm³.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `GP-13_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `GP-13_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `GP-13.json` | Descripteur pour le plugin Magpie |
| `GP-13_fiche.md` | La présente fiche |
| `GP-13_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `GP-13_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `GP-13_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
