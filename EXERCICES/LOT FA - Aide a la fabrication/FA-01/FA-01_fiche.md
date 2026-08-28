# FA-01 — Combien de panneaux pour ce débit

**Fiche d'exercice Magpie** · Lot FA — Aide à la fabrication

| | |
|---|---|
| **Thématique** | FA1 · Imbrication |
| **Référence au référentiel** | REF-113, REF-114 |
| **Compétence visée** | Estimer le nombre de panneaux nécessaires à un débit et chiffrer la chute, avant toute imbrication réelle. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 35 min |
| **Prérequis** | QT-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Estimer le nombre de panneaux nécessaires à un débit et chiffrer la chute, avant toute imbrication réelle.

### Contexte

Le débit part sur une découpeuse à commande numérique ; le panneau brut mesure 2 500 × 1 250 mm et se commande à l'unité.

### Énoncé

> Les 20 pièces à débiter vous sont fournies avec leurs dimensions. Donnez le nombre minimal théorique de panneaux, c'est-à-dire celui qu'imposerait déjà la seule surface, avant toute contrainte de placement.

### Ce qui vous est fourni

Les 20 longueurs et les 20 hauteurs, en millimètres, et les dimensions du panneau brut.

### Ce qui est attendu

Le nombre minimal théorique de panneaux, arrondi au supérieur.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`FA-01_sujet.gh`

### Barème

1 point si le nombre est juste et arrondi au supérieur.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `FA-01_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Calculer la surface de chaque pièce.

**Étape 2.** Sommer les vingt surfaces.

**Étape 3.** Diviser par la surface d'un panneau brut.

**Étape 4.** Arrondir au supérieur : c'est un approvisionnement.

**Étape 5.** Garder à l'esprit que le nombre réel sera supérieur — la chute de placement s'ajoute à la chute de surface.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Arrondir le rapport de surfaces au plus proche. Un panneau se commande entier : il en faut au moins autant que la surface l'exige, donc un arrondi au supérieur. C'est la même règle qu'en A-06, appliquée à un approvisionnement.

### Pièges fréquents

- Arrondir au plus proche.
- Oublier que ce minorant est inatteignable en pratique et le présenter comme la commande à passer.

### Pourquoi ce jeu de données

Vingt pièces de dimensions réalistes pour du mobilier, dont la surface totale tombe volontairement peu après un nombre entier de panneaux : arrondir au plus proche donnerait un panneau de moins, et le débit serait incomplet.

### Limite de la correction automatique

> Le nombre RÉEL de panneaux dépend de l'imbrication, qui relève d'un plugin dédié et ne se calcule pas ici. C'est le minorant théorique qui est validé — et c'est aussi ce que sert à comprendre l'exercice : aucune imbrication ne peut faire mieux.

### Pour aller plus loin

- Ajouter un trait de scie de 4 mm autour de chaque pièce et refaire l'estimation.
- Comparer au résultat d'une imbrication réelle et chiffrer l'écart : c'est le rendement de l'imbrication.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `FA-01_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `FA-01_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `FA-01.json` | Descripteur pour le plugin Magpie |
| `FA-01_fiche.md` | La présente fiche |
| `FA-01_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `FA-01_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `FA-01_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
