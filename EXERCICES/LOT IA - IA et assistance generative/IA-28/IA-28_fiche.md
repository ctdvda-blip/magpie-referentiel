# IA-28 — Regrouper des pièces par similarité

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA5 · Apprentissage automatique |
| **Référence au référentiel** | REF-130 |
| **Compétence visée** | Regrouper des éléments sur plusieurs critères à la fois et lire l'effectif du groupe dominant. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 20 min |
| **Prérequis** | IA-10 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 10 composants |
| **Gamification associée** | G-12 Le memory des composants |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Regrouper des éléments sur plusieurs critères à la fois et lire l'effectif du groupe dominant.

### Contexte

Rationaliser un débit, c'est ramener des pièces toutes différentes à quelques familles. La famille la plus fournie décide du réglage de la machine.

### Énoncé

> Les vingt pièces vous sont données par leur longueur et leur épaisseur. Regroupez-les selon qu'elles dépassent ou non 900 mm de long et 34 mm d'épaisseur. Donnez l'effectif du groupe le plus fourni.

### Ce qui vous est fourni

Les vingt couples longueur-épaisseur et les deux seuils.

### Ce qui est attendu

10 pièces dans le groupe le plus fourni.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-28_sujet.gh`

### Barème

1 point si l'effectif est exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-28_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Tester chaque pièce sur les deux seuils.

**Étape 2.** Former les quatre combinaisons de vrai et de faux.

**Étape 3.** Compter chaque famille.

**Étape 4.** Prendre le plus grand des quatre effectifs.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Regrouper sur un seul critère. La longueur seule donne deux groupes de dix ; c'est le CROISEMENT des deux critères qui produit quatre familles d'effectifs 10, 4, 4 et 2 — et seul le croisement dit quoi régler sur la machine.

### Pièges fréquents

- Ne croiser qu'un critère.
- Rendre le nombre de familles au lieu de l'effectif.

### Pourquoi ce jeu de données

Vingt pièces, quatre familles d'effectifs 10, 4, 4 et 2. Deux familles sont à égalité : le maximum, lui, est unique. Le groupe dominant rassemble la moitié des pièces, ce qui rend le regroupement utile plutôt que décoratif.

### Limite de la correction automatique

> Les seuils sont DONNÉS. Un vrai regroupement les cherche — c'est ce que fait un algorithme de partitionnement — et le nombre de familles devient lui-même un résultat, pas une hypothèse.

### Pour aller plus loin

- Faire varier le seuil de longueur et suivre le groupe dominant.
- Chercher les seuils qui équilibrent les quatre familles.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-28_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-28_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-28.json` | Descripteur pour le plugin Magpie |
| `IA-28_fiche.md` | La présente fiche |
| `IA-28_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-28_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-28_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
