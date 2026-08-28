# A-45 — Intersections entre géométries

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A10 · Surfaces et solides |
| **Référence au référentiel** | REF-071 |
| **Compétence visée** | Extraire le contour d'intersection entre un solide et un plan, et le mesurer. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-44 |
| **Mode de validation** | NumericTolerance — tolérance 0,5 % |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-16 Chasse au trésor |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Extraire le contour d'intersection entre un solide et un plan, et le mesurer.

### Contexte

Une coupe horizontale à mi-hauteur sert à chiffrer le linéaire de joint périphérique.

### Énoncé

> Le solide vous est fourni. Établissez son contour de coupe à mi-hauteur et donnez le linéaire total de ce contour.

### Ce qui vous est fourni

Un solide internalisé.

### Ce qui est attendu

Le contour de coupe et son linéaire total.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,5 %.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-45_sujet.gh`

### Barème

1 point pour le contour, 1 point pour la longueur.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-45_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Bounding Box puis Deconstruct Box pour obtenir la hauteur.

**Étape 2.** Construire le plan de coupe à mi-hauteur avec XY Plane et Construct Point.

**Étape 3.** Poser Brep | Plane et récupérer la sortie C (courbes).

**Étape 4.** Poser Length et Mass Addition pour la longueur totale.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Ne mesurer qu'un seul morceau du contour quand la coupe en produit plusieurs : le linéaire est sous-évalué sans que rien ne le signale.

### Pièges fréquents

- Plan de coupe placé hors du solide : aucune courbe produite.
- Plusieurs contours produits : additionner toutes les longueurs.

### Pour aller plus loin

- Produire une série de coupes régulières pour un plan de fabrication.
- Intersecter deux solides et récupérer la courbe commune.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-45_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-45_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-45.json` | Descripteur pour le plugin Magpie |
| `A-45_fiche.md` | La présente fiche |
| `A-45_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-45_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-45_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
