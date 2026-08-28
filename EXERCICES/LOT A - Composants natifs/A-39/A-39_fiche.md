# A-39 — Réseaux rectangulaire et polaire

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A9 · Transformations et réseaux |
| **Référence au référentiel** | REF-068 |
| **Compétence visée** | Produire des répétitions régulières en trame et en couronne, et lire la structure de données obtenue. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-38 |
| **Mode de validation** | GeometryTolerance — tolérance 0,5 mm |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-10 Coffre à butin |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire des répétitions régulières en trame et en couronne, et lire la structure de données obtenue.

### Contexte

Une façade est calepinée en modules réguliers ; une verrière circulaire reprend le même module en couronne.

### Énoncé

> Le module vous est fourni. Produisez la trame de 5 modules en largeur et 4 en hauteur, espacés de 600 mm et 400 mm, puis la couronne de 12 modules répartis sur un tour complet.

### Ce qui vous est fourni

Un module rectangulaire internalisé.

### Ce qui est attendu

Les deux ensembles demandés : la trame rectangulaire et la couronne, chacun au complet.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,5 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-39_sujet.gh`

### Barème

1 point par réseau correct.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-39_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 20 modules en trame et 12 modules en couronne.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Poser Rectangular Array avec Nx = 5, Ny = 4.

**Étape 2.** Régler la cellule via un Construct Plane ou en réglant les entrées Sx et Sy sur 600 et 400.

**Étape 3.** Poser Polar Array avec Count = 12 et Angle = 2π.

**Étape 4.** Brancher un Param Viewer pour observer l'arbre à deux niveaux produit par le réseau rectangulaire.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Produire 12 modules répartis sur 360° en comptant la position d'origine deux fois : le douzième se superpose au premier et il n'y a que 11 modules visibles.

### Pièges fréquents

- Le réseau rectangulaire produit un arbre, pas une liste plate.
- Polar Array attend un angle en radians.

### Pour aller plus loin

- Faire varier la taille des modules selon leur position.
- Combiner les deux réseaux.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-39_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-39_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-39.json` | Descripteur pour le plugin Magpie |
| `A-39_fiche.md` | La présente fiche |
| `A-39_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-39_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-39_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
