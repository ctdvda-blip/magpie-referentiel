# RH-27 — Le volume d'un assemblage de primitives

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Modélisation Rhino |
| **Référence au référentiel** | REF-007, REF-008 |
| **Compétence visée** | Chiffrer la matière d'un assemblage de primitives en déduisant ce qu'elles ont en commun. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 16 min |
| **Prérequis** | RH-05 |
| **Mode de validation** | NumericTolerance — tolérance 0.0001 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-14 Le puzzle de câblage |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Chiffrer la matière d'un assemblage de primitives en déduisant ce qu'elles ont en commun.

### Contexte

Un socle et son fût se commandent au volume de matière. Les deux se recouvrent là où le second s'encastre dans le premier, et cette matière-là n'existe qu'une fois.

### Énoncé

> Le socle mesure 240 × 160 × 40 mm. Le fût cylindrique fait 45 mm de rayon et 120 mm de haut, et s'encastre de 15 mm dans le socle. Donnez le volume de matière, en décimètres cubes.

### Ce qui vous est fourni

Les cotes du socle, celles du fût et la profondeur d'encastrement.

### Ce qui est attendu

2,2040 dm³ de matière, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-27_sujet.gh`

### Barème

1 point si le volume est juste à 0,0001 dm³.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-27_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Calculer le volume du socle.

**Étape 2.** Calculer celui du fût entier.

**Étape 3.** Calculer le volume encastré : le disque du fût sur 15 mm.

**Étape 4.** Additionner les deux premiers et retrancher le troisième.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Additionner les deux volumes : 2,2994 dm³. Les 15 mm d'encastrement sont comptés deux fois — une fois dans le socle, une fois dans le fût. L'écart est de 4 %, assez pour fausser un devis de fonderie, trop peu pour se voir.

### Pièges fréquents

- Additionner sans déduire.
- Retrancher le volume du fût entier au lieu de la seule partie encastrée.

### Pourquoi ce jeu de données

Le recouvrement vaut 95 426 mm³, soit 4,3 % du total. C'est l'ordre de grandeur d'une erreur qui passe : au-delà de 20 % on la cherche, en dessous de 1 % elle ne coûte rien.

### Limite de la correction automatique

> Le volume est celui de la GÉOMÉTRIE. Une pièce fondue y ajoute les dépouilles, les congés de raccordement et la surépaisseur d'usinage, que ce calcul ignore.

### Pour aller plus loin

- Faire varier l'encastrement et suivre le volume.
- Chercher l'encastrement qui ramène le volume à 2,15 dm³.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-27_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-27_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-27.json` | Descripteur pour le plugin Magpie |
| `RH-27_fiche.md` | La présente fiche |
| `RH-27_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-27_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-27_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
