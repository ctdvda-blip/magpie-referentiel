# B-04 — Pavage hexagonal sur surface

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B1 · Architecture et construction |
| **Référence au référentiel** | REF-068, REF-069, REF-049 |
| **Compétence visée** | Établir combien d'éléments d'une trame non orthogonale tiennent dans une emprise donnée. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 28 min |
| **Prérequis** | B-03, A-20 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 20 composants |
| **Gamification associée** | G-22 Boss de fin de chapitre |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Projeter une trame plane sur une surface libre en maîtrisant la structure de données.

### Contexte

Le bardage hexagonal se commande à l'unité. Le pas d'une trame hexagonale n'est pas son côté.

### Énoncé

> Applique un pavage hexagonal de 400 mm de côté sur la surface libre fournie, puis extrude chaque hexagone de 60 mm suivant la normale locale de la surface.

### Ce qui vous est fourni

Une surface libre internalisée.

### Ce qui est attendu

130 hexagones.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-04_sujet.gh`

### Barème

2 points pour le pavage, 2 points pour l'orientation selon les normales.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-04_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Construire la trame hexagonale plane par deux Rectangular Array décalés d'un demi-pas.

**Étape 2.** Poser Polygon avec 6 côtés sur chaque centre.

**Étape 3.** Projeter les centres sur la surface avec Surface Closest Point.

**Étape 4.** Récupérer les normales avec Evaluate Surface (sortie N).

**Étape 5.** Construire un plan local par centre avec Plane Normal.

**Étape 6.** Orienter les hexagones sur ces plans avec Orient.

**Étape 7.** Extruder chaque hexagone suivant sa normale : Graft nécessaire pour associer un vecteur par hexagone.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Diviser l'emprise par le CÔTÉ de l'hexagone au lieu de son pas. Une trame hexagonale avance de √3 × côté horizontalement et de 1,5 × côté verticalement — jamais du côté lui-même. L'erreur donne 384 hexagones, soit trois fois trop.

### Pièges fréquents

- Oublier le Graft : tous les hexagones reçoivent le même vecteur.
- Trame plane plus petite que la surface : des zones restent non pavées.
- Surface très courbe : les hexagones se chevauchent.

### Pourquoi ce jeu de données

Côté de 400 mm : pas horizontal 692,8 mm, pas vertical 600 mm. Sur 9 600 × 6 400 mm cela fait 13 × 10 = 130 hexagones. Aucun des deux pas n'est un compte rond, et aucun ne vaut le côté : l'erreur ne peut pas passer pour un arrondi.

### Pour aller plus loin

- Faire varier la hauteur d'extrusion selon la courbure locale.
- Découper les hexagones dépassant du contour de la surface.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-04_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-04_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-04.json` | Descripteur pour le plugin Magpie |
| `B-04_fiche.md` | La présente fiche |
| `B-04_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-04_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-04_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
