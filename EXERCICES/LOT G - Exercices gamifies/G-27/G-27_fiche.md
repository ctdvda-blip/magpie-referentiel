# G-27 — La savane paramétrique

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G6 · Sensations et immersion |
| **Référence au référentiel** | REF-063, REF-067, REF-068 |
| **Compétence visée** | Disposer une série d'objets sur un cercle et mesurer la disposition obtenue plutôt que de la constater. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | A-34, A-39 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 14 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Inscrire une série d'exercices dans un fil narratif cohérent avec l'identité de la marque.

### Contexte

La scénarisation inscrit une série d'exercices dans un fil narratif. Un apprenant qui construit une savane retient mieux qu'un apprenant qui construit « une trame polaire de douze éléments ».

### Énoncé

> Chapitre 1 de la savane : construis l'abreuvoir circulaire, puis dispose la harde de 12 animaux en trame autour du point d'eau, chacun orienté vers le centre.

### Ce qui vous est fourni

Un décor de fond et un module d'animal simplifié.

### Ce qui est attendu

17 082,06 mm — le périmètre du polygone que forment les douze animaux, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-27_sujet.gh`

### Barème

2 points : 1 pour la disposition, 1 pour l'orientation.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-27_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Construire l'abreuvoir par un Circle centré à l'origine.

**Étape 2.** Répartir 12 positions par Polar Array ou Divide Curve sur un cercle plus grand.

**Étape 3.** Construire pour chaque position le vecteur pointant vers le centre avec Vector 2Pt.

**Étape 4.** Orienter chaque module avec Orient ou Rotate selon l'angle calculé.

**Étape 5.** Vérifier que tous les modules regardent bien le centre.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Disposer les animaux sur le cercle de l'abreuvoir lui-même, rayon 1 800, au lieu du cercle à 950 mm au-delà : 11 180,98 mm. Les douze animaux boivent alors les pieds dans l'eau — l'écart demandé est une distance AU BORD, pas au centre.

### Pièges fréquents

- Vecteur construit du centre vers la position : les animaux tournent le dos à l'eau.
- Angle calculé sans Atan2 : l'orientation est fausse sur deux quadrants.

### Pourquoi ce jeu de données

Un abreuvoir de 1 800 mm de rayon, des animaux à 950 mm du bord : le rayon de la harde vaut 2 750 mm, et le périmètre du douzagone régulier 17 082,06. La confusion bord/centre change la réponse de 53 %, ce qui ne peut pas passer pour un arrondi.

### Limite de la correction automatique

> Le périmètre dit que les douze animaux sont bien RÉPARTIS sur le bon cercle. Il ne dit rien de leur ORIENTATION vers le centre, qui se juge à l'aperçu — un animal retourné laisse le périmètre intact.

### Pour aller plus loin

- Chapitres successifs formant un parcours complet.
- Personnages débloqués par les badges.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-27_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-27_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-27.json` | Descripteur pour le plugin Magpie |
| `G-27_fiche.md` | La présente fiche |
| `G-27_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-27_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-27_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
