# A-04 — Référencer et cuire de la géométrie Rhino

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A1 · Interface, flux de données et paramètres |
| **Référence au référentiel** | REF-026 |
| **Compétence visée** | Faire circuler une géométrie entre Rhino et Grasshopper dans les deux sens, par calque plutôt que par sélection manuelle. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-03 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-05 Badges et trophées |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire circuler une géométrie entre Rhino et Grasshopper dans les deux sens, par calque plutôt que par sélection manuelle.

### Contexte

Le géomètre a livré l'implantation des poteaux sous forme de cercles ; le bureau d'études doit en produire un calque de contrôle décalé.

### Énoncé

> Les cercles d'implantation occupent le calque « CERCLES » du fichier Rhino. Récupérez-les sans les désigner un par un — l'implantation peut encore changer — remontez-les de 50 mm, et déposez le résultat dans le modèle sur le calque « COPIES ».

### Ce qui vous est fourni

Fichier 3DM joint contenant trois cercles sur le calque CERCLES.

### Ce qui est attendu

Trois cercles présents sur le calque COPIES, décalés de 50 mm en Z.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-04_sujet.gh`

### Barème

1 point si les trois cercles sont cuits au bon niveau.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-04_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Geometry Pipeline (Params > Util) et saisir CERCLES dans le champ Layer.

**Étape 2.** Vérifier que trois courbes sont captées (survol de la sortie).

**Étape 3.** Poser Unit Z (Vector > Vector) et un slider réglé sur 50.

**Étape 4.** Poser Move et relier la géométrie et le vecteur.

**Étape 5.** Clic droit sur Move > Bake, choisir le calque COPIES.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Désigner les cercles à la main : le montage cesse de suivre dès que le géomètre ajoute un poteau. L'erreur ne se voit pas au premier essai, seulement à la mise à jour.

### Pièges fréquents

- Le Geometry Pipeline est sensible à la casse du nom de calque.
- Oublier de multiplier Unit Z par la valeur du slider : le décalage vaut 1 mm.

### Réglages à poser à la main

Ces réglages ne peuvent pas être enregistrés dans le fichier : ils sont à poser dans Grasshopper.

- Geometry Pipeline : saisir CERCLES dans le champ Layer (sensible à la casse).
- Bake du composant Move : choisir le calque COPIES.

### Pour aller plus loin

- Filtrer le Pipeline par type de géométrie plutôt que par calque.
- Utiliser Elefront pour cuire avec des attributs.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-04_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-04_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-04.json` | Descripteur pour le plugin Magpie |
| `A-04_fiche.md` | La présente fiche |
| `A-04_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-04_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-04_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
| `Ressources/A-04_ressources.3dm` | Géométrie Rhino à ouvrir avant de commencer |
