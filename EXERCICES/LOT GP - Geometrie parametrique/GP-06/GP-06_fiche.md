# GP-06 — Les sommets d'une nappe maillée

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP4 · Maillages et SubD |
| **Référence au référentiel** | REF-074 |
| **Compétence visée** | Distinguer le nombre de faces d'un maillage de son nombre de sommets, et savoir lequel commande quoi. |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 20 min |
| **Prérequis** | GP-03 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Distinguer le nombre de faces d'un maillage de son nombre de sommets, et savoir lequel commande quoi.

### Contexte

La nappe part vers un calcul aux éléments finis, qui se dimensionne au nombre de NŒUDS, pas de faces.

### Énoncé

> La nappe est maillée en 48 divisions dans un sens et 30 dans l'autre, en quadrangles. Donnez le nombre de sommets.

### Ce qui vous est fourni

Les deux nombres de divisions.

### Ce qui est attendu

1 519 sommets — 49 × 31.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-06_sujet.gh`

### Barème

1 point si le nombre de sommets est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `GP-06_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Compter les rangées de sommets dans chaque sens : une de plus que les divisions.

**Étape 2.** Multiplier.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Répondre 1 440, le nombre de faces. Un maillage de n divisions a n + 1 rangées de sommets : l'écart de 79 sommets ne se voit pas sur l'image, mais il change la taille du système à résoudre.

### Pièges fréquents

- Multiplier les divisions entre elles.
- Oublier que le maillage n'est pas fermé sur lui-même.

### Pourquoi ce jeu de données

48 et 30 sont des divisions courantes pour une nappe d'étude. Les deux réponses — 1 440 et 1 519 — sont assez proches pour qu'on ne les distingue pas à vue, assez différentes pour que le calcul ne soit pas le même.

### Pour aller plus loin

- Donner le nombre d'arêtes.
- Reprendre pour une nappe refermée dans un sens.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `GP-06_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `GP-06_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `GP-06.json` | Descripteur pour le plugin Magpie |
| `GP-06_fiche.md` | La présente fiche |
| `GP-06_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `GP-06_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `GP-06_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
