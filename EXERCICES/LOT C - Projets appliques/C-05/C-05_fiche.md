# C-05 — Bibliothèque paramétrique avec débit et mise à plat CNC

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C2 · Design de mobilier |
| **Référence au référentiel** | REF-070, REF-082, REF-115, REF-087 |
| **Compétence visée** | Déduire le nombre d'éléments d'un meuble d'une contrainte d'entraxe maximal, et en tirer la nomenclature. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Expérimenté |
| **Durée cible** | 90 min |
| **Prérequis** | B-06, B-12, B-17 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 50 composants |
| **Gamification associée** | G-06 Niveaux et déblocage + G-05 Badges |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Aller du modèle paramétrique au fichier de fabrication, en passant par la nomenclature.

### Contexte

Une tablette de plus de 800 mm de portée flèche sous la charge. C'est cette règle qui fixe le nombre de montants, pas l'esthétique.

### Énoncé

> Modélise une bibliothèque de largeur, hauteur et profondeur paramétrables, à montants verticaux tous les 800 mm maximum et tablettes réglables. Produis la nomenclature de débit et la mise à plat repérée de tous les panneaux, prête pour la CNC.

### Ce qui vous est fourni

Trois sliders de dimensions générales et un slider d'épaisseur de panneau.

### Ce qui est attendu

28 panneaux à débiter.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-05_sujet.gh`

### Barème

4 points modèle, 3 points nomenclature, 3 points mise à plat.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `C-05_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Calculer le nombre de travées : largeur divisée par 800, arrondi supérieur.

**Étape 2.** Répartir les montants et en déduire la largeur réelle de travée.

**Étape 3.** Construire montants, traverses et tablettes par Box paramétrés.

**Étape 4.** Percer les rangées de trous de tablettes par un réseau de cylindres et Solid Difference.

**Étape 5.** Extraire la face principale de chaque panneau avec Deconstruct Brep et un tri par aire.

**Étape 6.** Orienter chaque face vers le plan XY avec Orient.

**Étape 7.** Répartir les panneaux à plat sans recouvrement par un calepinage simple.

**Étape 8.** Repérer chaque panneau avec Text Tag 3D et produire la nomenclature de débit.

**Étape 9.** Contrôler que le total des surfaces à plat correspond à la somme des faces d'origine.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter quatre montants pour quatre travées. Il en faut CINQ — un de plus que les intervalles, comme toujours. Le meuble monté sur le calcul faux n'a pas de joue à une extrémité.

### Pièges fréquents

- Faces sélectionnées par index fixe : le tri casse dès qu'un panneau change de forme.
- Panneaux mis à plat qui se recouvrent.
- Repères perdus lors de la mise à plat car non propagés en parallèle des géométries.

### Pourquoi ce jeu de données

3 200 mm de largeur pour 800 mm d'entraxe maximal donnent exactement quatre travées : le cas limite, où l'arrondi au supérieur ne change rien et où seul le « n + 1 » compte. Cinq montants, vingt tablettes, deux traverses et un fond.

### Limite de la correction automatique

> L'exercice compte les panneaux. Leur DÉBIT — comment ils se placent dans les plaques — est l'objet de C-12, et n'a pas la même réponse.

### Pour aller plus loin

- Ajouter des portes et calculer leurs jeux.
- Générer le fichier DXF des panneaux.
- Ajouter une contrainte de nombre de plaques disponibles.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `C-05_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `C-05_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `C-05.json` | Descripteur pour le plugin Magpie |
| `C-05_fiche.md` | La présente fiche |
| `C-05_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `C-05_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `C-05_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
