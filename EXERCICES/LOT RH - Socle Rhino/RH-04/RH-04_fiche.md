# RH-04 — Du profil à la surface

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Modélisation Rhino |
| **Référence au référentiel** | REF-009, REF-010, REF-011 |
| **Compétence visée** | Passer d'une courbe tracée dans Rhino à une surface, et contrôler la grandeur obtenue. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-03 |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Passer d'une courbe tracée dans Rhino à une surface, et contrôler la grandeur obtenue.

### Contexte

Un bardage courbe se chiffre à la surface développée ; le tracé vient d'un relevé, la surface doit en découler.

### Énoncé

> Le relevé fournit la ligne au sol du bardage. Produisez la surface du bardage en la montant de 2 800 mm à la verticale, puis donnez sa surface en mètres carrés.

### Ce qui vous est fourni

Un fichier Rhino contenant la courbe de relevé au sol.

### Ce qui est attendu

La surface du bardage, en mètres carrés, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-04_sujet.gh`

### Barème

1 point si la surface est juste à 0,01 m² près.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-04_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Vérifier que la courbe de relevé est bien une seule courbe, non une suite de segments disjoints.

**Étape 2.** Monter la surface à la verticale, pas selon la normale.

**Étape 3.** Référencer la surface dans la définition par son calque.

**Étape 4.** Mesurer l'aire, en millimètres carrés.

**Étape 5.** Convertir en mètres carrés : diviser par un million, pas par mille.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Monter la surface en suivant la normale de la courbe plutôt qu'à la verticale : sur une ligne au sol non plane, la hauteur cesse d'être constante et la surface obtenue n'est plus celle d'un bardage.

### Pièges fréquents

- Une courbe en plusieurs morceaux produit autant de surfaces, et l'aire mesurée n'est plus celle d'un seul objet.
- Conversion d'unités : un mètre carré vaut un million de millimètres carrés.

### Pourquoi ce jeu de données

La ligne au sol présente une courbure variable : une extrusion suivant la normale donnerait un résultat visuellement proche et numériquement différent.

### Limite de la correction automatique

> La surface est celle du BARDAGE DÉVELOPPÉ. Elle ne déduit ni les baies ni les recouvrements de lames : la commande se fait sur une surface majorée, typiquement de 5 à 10 %.

### Pour aller plus loin

- Incliner le bardage de 10° et mesurer l'écart de surface.
- Découper la surface en lés de 1 200 mm et compter les lés.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-04_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-04_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-04.json` | Descripteur pour le plugin Magpie |
| `RH-04_fiche.md` | La présente fiche |
| `RH-04_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-04_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-04_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
