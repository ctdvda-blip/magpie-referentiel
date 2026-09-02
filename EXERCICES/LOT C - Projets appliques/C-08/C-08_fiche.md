# C-08 — Bague solitaire complète

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C3 · Joaillerie |
| **Référence au référentiel** | REF-069, REF-068, REF-081, REF-079 |
| **Compétence visée** | Chiffrer la masse d'une pièce à partir de sa fibre moyenne, et la confronter à une limite de projet. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Expérimenté |
| **Durée cible** | 85 min |
| **Prérequis** | B-09, B-10 |
| **Mode de validation** | NumericTolerance — tolérance 0.05 |
| **Solution de référence** | 45 composants |
| **Gamification associée** | G-05 Badges + G-09 Récompense cachée |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Assembler plusieurs sous-ensembles techniques en un bijou complet, avec contrôle de poids.

### Contexte

L'or se pèse avant d'être coulé. Un gramme de trop sur un solitaire, c'est cinquante euros et un anneau qui paraît lourd au doigt.

### Énoncé

> Modélise une bague solitaire pour une pierre ronde de 6,5 mm : anneau de taille paramétrable, chaton, panier et 4 griffes. Contrôle que la masse en or 750 reste inférieure à 3,2 g et que la hauteur totale ne dépasse pas 8 mm.

### Ce qui vous est fourni

Un slider de taille de doigt et un slider de diamètre de pierre.

### Ce qui est attendu

3,011 g d'or 750, à 0,05 près — sous la limite de 3,2 g.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.05.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-08_sujet.gh`

### Barème

4 points géométrie, 3 points unicité du solide, 3 points indicateurs.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `C-08_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Calculer le diamètre intérieur à partir de la taille française : diamètre = (taille + 40) / π.

**Étape 2.** Construire le profil de l'anneau et le révolutionner.

**Étape 3.** Construire le chaton et le panier par balayage et révolution.

**Étape 4.** Reprendre les griffes de l'exercice B-09 et les répartir par Polar Array.

**Étape 5.** Unir l'ensemble avec Solid Union et vérifier que le résultat est un solide unique fermé.

**Étape 6.** Mesurer le volume total et le multiplier par la masse volumique de l'or 750 (environ 15,6 g/cm³).

**Étape 7.** Mesurer la hauteur totale par Bounding Box.

**Étape 8.** Afficher les deux indicateurs avec un test de conformité.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Calculer le volume sur la circonférence NOMINALE, celle du doigt : 2,845 g. L'anneau a une épaisseur ; sa fibre moyenne court à mi-épaisseur, donc sur une circonférence plus grande de π fois l'épaisseur. L'écart de 0,17 g dépasse quatre fois la tolérance, et il sous-estime toujours — c'est de l'or qu'on croit économiser et qu'il faudra ajouter.

### Pièges fréquents

- Solid Union renvoyant plusieurs solides : des éléments ne se touchent pas réellement.
- Volume en mm³ multiplié directement par une masse volumique en g/cm³.
- Taille de doigt confondue avec le diamètre.

### Pourquoi ce jeu de données

Taille 54, section 2,0 × 1,3 mm, or 750 à 15,6 g/cm³ : la masse tombe à 3,011 g pour une limite de 3,2. La marge est de 6 % — assez serrée pour que l'erreur de fibre moyenne compte, assez large pour que la pièce reste faisable.

### Pour aller plus loin

- Ajouter un pavage sur le corps de bague.
- Optimiser le profil pour minimiser la masse à rigidité constante.
- Produire la vue technique cotée.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `C-08_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `C-08_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `C-08.json` | Descripteur pour le plugin Magpie |
| `C-08_fiche.md` | La présente fiche |
| `C-08_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `C-08_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `C-08_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
