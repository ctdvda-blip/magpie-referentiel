# B-10 — Motif gravé développé sur un anneau

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B3 · Joaillerie |
| **Référence au référentiel** | REF-115, REF-069, REF-049 |
| **Compétence visée** | Répartir un motif répétitif sur un développé, en distinguant la circonférence du diamètre. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | B-04, A-42 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 24 composants |
| **Gamification associée** | G-09 Récompense cachée |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Concevoir un motif à plat puis l'enrouler sur une surface de révolution.

### Contexte

Le motif doit se refermer sur lui-même. Un raccord faux se voit immédiatement, et se voit toujours au même endroit.

### Énoncé

> Dessine à plat un motif géométrique répétitif de 12 modules, puis applique-le sur la face extérieure d'un anneau de taille 54 et de 4 mm de large. Le motif doit boucler sans rupture.

### Ce qui vous est fourni

Un anneau de révolution internalisé et un module de motif plan.

### Ce qui est attendu

4,50 mm — la largeur d'un module, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-10_sujet.gh`

### Barème

2 points pour le motif, 2 points pour la continuité du raccord.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-10_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Calculer la circonférence de l'anneau : diamètre intérieur = 54/π, puis circonférence extérieure.

**Étape 2.** Diviser cette circonférence par 12 pour obtenir la largeur exacte du module.

**Étape 3.** Construire le motif dans un rectangle de référence exactement de cette largeur.

**Étape 4.** Répliquer le module 12 fois avec Rectangular Array.

**Étape 5.** Construire la surface développée de référence (rectangle circonférence × largeur).

**Étape 6.** Appliquer Surface Morph ou Sporph entre la surface plane et la surface de l'anneau.

**Étape 7.** Vérifier la continuité au raccord en superposant le premier et le dernier module.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Diviser le DIAMÈTRE par le nombre de modules : 1,43 mm. La taille d'un anneau est une circonférence ; la confondre avec un diamètre divise le motif par π, et les douze modules ne couvrent plus qu'un tiers du tour.

### Pièges fréquents

- Largeur de module arrondie : le raccord présente un décalage cumulé.
- Confondre diamètre intérieur et diamètre extérieur pour le calcul de circonférence.
- Surface de référence et surface cible de proportions différentes : le motif se déforme.

### Pourquoi ce jeu de données

Une circonférence de 54 mm en 12 modules donne exactement 4,5 mm : un compte rond, à dessein — il rend le raccord vérifiable à la règle, et l'erreur d'un facteur π immédiate à voir.

### Limite de la correction automatique

> Le calcul porte sur le développé. Appliqué sur l'anneau, le motif subit la courbure : sa lisibilité dépend alors de la largeur de l'anneau, que l'exercice ne juge pas.

### Pour aller plus loin

- Rendre le nombre de modules paramétrable et recalculer automatiquement la largeur.
- Graver le motif en creux par Solid Difference.
- Adapter au cas d'un anneau de section variable.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-10_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-10_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-10.json` | Descripteur pour le plugin Magpie |
| `B-10_fiche.md` | La présente fiche |
| `B-10_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-10_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-10_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
