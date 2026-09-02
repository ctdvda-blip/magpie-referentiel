# C-01 — Enveloppe à brise-soleil orientés selon l'ensoleillement

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C1 · Architecture |
| **Référence au référentiel** | REF-027, REF-068, REF-095, REF-079 |
| **Compétence visée** | Dimensionner un dispositif d'ombrage à partir de la course solaire, en distinguant ce qui se divise de ce qui se multiplie. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 90 min |
| **Prérequis** | B-03, B-04 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 45 composants |
| **Gamification associée** | G-22 Boss de fin de chapitre + G-23 Classement |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Construire une enveloppe dont chaque élément réagit à une donnée d'analyse, et justifier le résultat par une mesure.

### Contexte

Le brise-soleil doit occulter à l'heure la plus chaude sans assombrir le reste de l'année. Sa profondeur est ce qui coûte et ce qui se voit.

### Énoncé

> La façade sud du bâtiment reçoit 180 lames brise-soleil. Oriente chaque lame perpendiculairement à la direction du soleil au 21 juin à 15 h, puis optimise l'angle moyen pour limiter la surface exposée à 40 % de la surface vitrée tout en préservant au moins 25 % de vue directe.

### Ce qui vous est fourni

Une façade, un vecteur solaire et le contour vitré internalisés.

### Ce qui est attendu

249,95 mm — la profondeur minimale de lame, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-01_sujet.gh`

### Barème

4 points géométrie, 3 points indicateurs, 3 points optimisation.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `C-01_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Diviser la façade en 180 stations avec Divide Surface.

**Étape 2.** Récupérer les plans locaux avec Evaluate Surface.

**Étape 3.** Construire le vecteur solaire à partir de l'azimut et de la hauteur fournis.

**Étape 4.** Calculer pour chaque station l'angle entre la normale de lame et le vecteur solaire avec Angle.

**Étape 5.** Faire tourner chaque lame avec Rotate Axis autour de son axe horizontal.

**Étape 6.** Projeter les lames sur le plan perpendiculaire au soleil et mesurer l'aire projetée cumulée avec Area.

**Étape 7.** Calculer le taux d'ombrage et le taux de vue directe.

**Étape 8.** Brancher Galapagos sur l'angle de base et l'amplitude de variation, fonction objectif combinant les deux critères.

**Étape 9.** Lancer l'optimisation et internaliser le meilleur jeu de paramètres.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Multiplier l'entraxe par la tangente au lieu de le diviser : 640 mm, soit deux fois et demie trop. Une lame de 640 mm sur un entraxe de 400 se recouvre elle-même — la façade devient un mur, et le calcul reste plausible tant qu'on ne le dessine pas.

### Pièges fréquents

- Aires projetées additionnées sans traiter les recouvrements entre lames.
- Fonction objectif à un seul critère : l'optimiseur ferme totalement la façade.
- Galapagos relié à un slider non borné : la recherche n'aboutit pas.

### Pourquoi ce jeu de données

Un soleil à 58° correspond au 21 juin en milieu d'après-midi sous nos latitudes. Les deux réponses, 250 et 640 mm, sont dans un rapport de 2,56 — soit exactement le carré de la tangente, ce qui est la signature de l'erreur.

### Limite de la correction automatique

> Le calcul assure l'occultation à CET instant. Une lame dimensionnée pour le 21 juin à 15 h laisse passer le soleil rasant de septembre — c'est la limite de tout brise-soleil fixe, et l'exercice ne la traite pas.

### Pour aller plus loin

- Étendre l'étude à quatre dates de référence.
- Piloter la largeur de lame plutôt que son angle.
- Produire la nomenclature des lames par angle distinct.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `C-01_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `C-01_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `C-01.json` | Descripteur pour le plugin Magpie |
| `C-01_fiche.md` | La présente fiche |
| `C-01_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `C-01_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `C-01_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
