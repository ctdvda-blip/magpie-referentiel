# GP-11 — L'ordre des opérations

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP5 · Synthèse géométrie |
| **Référence au référentiel** | REF-148 |
| **Compétence visée** | Établir qu'une suite d'opérations géométriques ne commute pas, et chiffrer ce que l'ordre change. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | GP-10 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 10 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir qu'une suite d'opérations géométriques ne commute pas, et chiffrer ce que l'ordre change.

### Contexte

Le contour part à la découpe. Il doit être congé de 120 mm et décalé de 40 mm vers l'extérieur pour la surcote d'usinage.

### Énoncé

> Le contour est un rectangle de 1 800 × 900 mm. Il faut le congéer d'un rayon de 120 mm et le décaler de 40 mm vers l'extérieur. Donnez l'écart de périmètre entre les deux ordres possibles, en millimètres.

### Ce qui vous est fourni

Les dimensions du rectangle, le rayon de congé et la valeur du décalage.

### Ce qui est attendu

68,67 mm d'écart entre les deux ordres, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-11_sujet.gh`

### Barème

1 point si l'écart est juste à 0,01 mm près.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `GP-11_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Calculer le périmètre pour l'ordre congé puis décalage : les rayons valent alors rayon + décalage.

**Étape 2.** Calculer celui de l'ordre inverse : le contour grandit de deux décalages dans chaque dimension, les rayons restent.

**Étape 3.** Prendre la valeur absolue de la différence.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Supposer que l'ordre est indifférent et n'en calculer qu'un. Congéer puis décaler donne des congés de 160 mm ; décaler puis congéer les laisse à 120 mm sur un contour plus grand. Les deux pièces sortent différentes, et rien sur le plan ne dit laquelle était voulue.

### Pièges fréquents

- Supposer la commutativité.
- Oublier que le décalage agit des DEUX côtés de chaque dimension.

### Pourquoi ce jeu de données

Un écart de 68,67 mm sur un périmètre de 5 445 mm, soit 1,3 % : trop peu pour se voir à l'écran, assez pour que deux ateliers travaillant chacun dans son ordre livrent des pièces qui ne s'assemblent pas.

### Limite de la correction automatique

> L'exercice chiffre l'écart de PÉRIMÈTRE. L'écart de forme est ailleurs : les rayons ne sont pas les mêmes, et c'est cela que le plan doit préciser.

### Pour aller plus loin

- Faire tendre le rayon vers zéro et vérifier que l'écart disparaît.
- Reprendre avec un décalage vers l'intérieur.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `GP-11_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `GP-11_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `GP-11.json` | Descripteur pour le plugin Magpie |
| `GP-11_fiche.md` | La présente fiche |
| `GP-11_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `GP-11_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `GP-11_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
