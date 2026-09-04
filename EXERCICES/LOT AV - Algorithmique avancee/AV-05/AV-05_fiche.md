# AV-05 — Charger jusqu'à la limite

**Fiche d'exercice Magpie** · Lot AV — Algorithmique avancée

| | |
|---|---|
| **Thématique** | AV1 · Boucles et itération |
| **Référence au référentiel** | REF-152 |
| **Compétence visée** | Transporter un cumul d'un passage au suivant, et repérer le rang où il franchit une limite. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | AV-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-11 Commande à passer |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Transporter un cumul d'un passage au suivant, et repérer le rang où il franchit une limite.

### Contexte

Les pièces se chargent dans l'ordre du montage, pas dans celui qui remplirait le mieux. Le camion accepte 4 000 mm de longueur cumulée.

### Énoncé

> Les vingt longueurs vous sont fournies dans l'ordre de chargement. La capacité est de 4 000 mm cumulés. Donnez le rang de la première pièce qui fait dépasser la capacité.

### Ce qui vous est fourni

Les vingt longueurs, dans l'ordre, et la capacité.

### Ce qui est attendu

8 — c'est la huitième pièce qui fait passer le cumul au-delà de 4 000 mm.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`AV-05_sujet.gh`

### Barème

1 point si le rang est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `AV-05_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Cumuler les longueurs dans l'ordre — la somme partielle, pas le total.

**Étape 2.** Comparer chaque cumul à la capacité.

**Étape 3.** Prendre le rang du premier qui dépasse.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Rendre le rang de la dernière pièce qui TIENT, soit 7. Les deux réponses ne diffèrent que d'une unité, et la consigne tranche : c'est celle qui fait dépasser qui est demandée. Sur le quai, c'est la pièce qu'on repose.

### Pièges fréquents

- Rendre le rang de la dernière pièce qui tient.
- Sommer d'abord et chercher ensuite : le cumul PARTIEL est ce qui porte l'information.

### Pourquoi ce jeu de données

Le cumul atteint 3 150 mm à la septième pièce et 4 068 mm à la huitième : le franchissement est net, mais le rang ne se devine pas — il faut cumuler. Vingt longueurs pour que le calcul de tête soit exclu.

### Limite de la correction automatique

> L'exercice suit l'ordre imposé. Choisir l'ordre qui remplit le mieux est un tout autre problème, et il n'a pas de solution simple.

### Pour aller plus loin

- Donner le nombre de camions nécessaires pour les vingt pièces.
- Rendre la longueur inutilisée du premier camion.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `AV-05_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `AV-05_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `AV-05.json` | Descripteur pour le plugin Magpie |
| `AV-05_fiche.md` | La présente fiche |
| `AV-05_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `AV-05_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `AV-05_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
