# B-16 — Lampe à lamelles de section variable

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B5 · Design produit |
| **Référence au référentiel** | REF-064, REF-069, REF-067 |
| **Compétence visée** | Chiffrer une surface développée dont une dimension varie continûment. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 28 min |
| **Prérequis** | A-35, A-41 |
| **Mode de validation** | NumericTolerance — tolérance 0.0001 |
| **Solution de référence** | 22 composants |
| **Gamification associée** | G-28 Avatar et personnalisation |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire varier une section le long d'un parcours par interpolation contrôlée.

### Contexte

La tôle de l'abat-jour se commande à plat, au mètre carré. La lamelle est large au milieu et étroite aux extrémités.

### Énoncé

> Produis un abat-jour composé de 24 lamelles réparties autour d'un axe. Chaque lamelle suit un profil dont la largeur varie de 15 mm aux extrémités à 45 mm au milieu, selon une courbe douce.

### Ce qui vous est fourni

Une courbe génératrice internalisée et un slider de nombre de lamelles.

### Ce qui est attendu

0,3024 m² de surface développée, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-16_sujet.gh`

### Barème

2 points pour la variation, 2 points pour la répartition.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-16_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Diviser la courbe génératrice en 30 stations avec Divide Curve.

**Étape 2.** Générer une série normalisée de 0 à 1 sur ces stations.

**Étape 3.** Passer cette série dans un Graph Mapper en courbe de Bézier symétrique.

**Étape 4.** Remapper la sortie sur le domaine 15 à 45 : on obtient la largeur à chaque station.

**Étape 5.** Construire un rectangle de cette largeur dans le plan perpendiculaire de chaque station.

**Étape 6.** Lofter ces rectangles pour obtenir la lamelle.

**Étape 7.** Répartir par Polar Array avec Count = 24.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Prendre la largeur maximale partout : 0,4536 m², soit 50 % de trop. La largeur varie linéairement — sa moyenne est la demi-somme des extrêmes, pas le maximum.

### Pièges fréquents

- Graph Mapper non symétrique : les deux extrémités n'ont pas la même largeur.
- Rectangles non alignés : le Loft se vrille.
- Lamelles voisines en interférence près de l'axe.

### Pourquoi ce jeu de données

24 lamelles de 420 mm, largeur de 15 à 45 mm : la largeur moyenne vaut 30 mm, exactement le tiers de la somme des extrêmes plus le minimum. Le rapport de 1,5 entre les deux réponses est trop grand pour passer inaperçu sur une commande.

### Pour aller plus loin

- Faire varier aussi l'épaisseur.
- Contrôler l'ouverture lumineuse résultante.
- Adapter le nombre de lamelles à un diamètre imposé.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-16_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-16_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-16.json` | Descripteur pour le plugin Magpie |
| `B-16_fiche.md` | La présente fiche |
| `B-16_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-16_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-16_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
