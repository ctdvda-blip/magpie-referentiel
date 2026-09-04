# IA-19 — Regrouper un débit en trois familles

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA4 · Apprentissage automatique |
| **Référence au référentiel** | REF-130 |
| **Compétence visée** | Regrouper des pièces en familles de fabrication et identifier celle qui pèse le plus dans l'organisation de l'atelier. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | IA-10 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Regrouper des pièces en familles de fabrication et identifier celle qui pèse le plus dans l'organisation de l'atelier.

### Contexte

L'atelier organise ses postes par famille de format. Le débit arrive en vrac, et c'est la famille la plus fournie qui dimensionne le poste.

### Énoncé

> Les vingt-quatre longueurs du débit vous sont fournies. Les familles sont : petit sous 300 mm, moyen jusqu'à 900 mm exclus, grand au-delà. Donnez l'effectif de la famille la plus fournie.

### Ce qui vous est fourni

Les vingt-quatre longueurs, en millimètres, et les deux seuils.

### Ce qui est attendu

9 pièces — l'effectif de la famille des petits.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-19_sujet.gh`

### Barème

1 point si l'effectif de la famille la plus fournie est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-19_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Classer chaque pièce selon les deux seuils.

**Étape 2.** Compter chaque famille.

**Étape 3.** Prendre le plus grand effectif.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Rendre le nombre de familles (3), ou l'effectif de la famille des grands, qu'on suppose la plus nombreuse parce qu'elle occupe le plus de place. Les grands sont sept, les moyens huit : c'est la famille des PETITS qui est la plus fournie, et c'est contre-intuitif — la place occupée n'est pas l'effectif.

### Pièges fréquents

- Rendre le nombre de familles.
- Placer mal la borne : « jusqu'à 900 exclus » n'est pas « jusqu'à 900 ».
- Supposer la réponse au lieu de compter.

### Pourquoi ce jeu de données

Neuf, huit et sept : les trois effectifs sont proches, de sorte que la réponse ne se devine pas d'un coup d'œil et qu'un comptage approximatif se trompe de famille. Les longueurs vont de 45 à 1 510 mm, l'étendue ordinaire d'un débit de mobilier.

### Limite de la correction automatique

> Les seuils sont donnés. Les TROUVER — c'est-à-dire laisser un regroupement automatique les proposer — est l'étape suivante, et elle demande de juger si les familles obtenues ont un sens pour l'atelier.

### Pour aller plus loin

- Donner les trois effectifs.
- Chercher les seuils qui équilibreraient les trois familles.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-19_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-19_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-19.json` | Descripteur pour le plugin Magpie |
| `IA-19_fiche.md` | La présente fiche |
| `IA-19_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-19_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-19_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
