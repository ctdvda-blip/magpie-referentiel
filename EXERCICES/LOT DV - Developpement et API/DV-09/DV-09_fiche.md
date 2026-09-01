# DV-09 — La division qui n'est pas celle qu'on croit

**Fiche d'exercice Magpie** · Lot DV — Développement, scripting et API

| | |
|---|---|
| **Thématique** | DV1 · Scripting dans Grasshopper |
| **Référence au référentiel** | REF-100, REF-102 |
| **Compétence visée** | Anticiper le comportement d'un opérateur selon le TYPE de ses opérandes, dans un composant scripté. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Expert |
| **Durée cible** | 25 min |
| **Prérequis** | DV-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-15 Relecture de code |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Anticiper le comportement d'un opérateur selon le type de ses opérandes, dans un composant scripté.

### Contexte

Le script calcule combien de panneaux entiers chaque pièce consomme. Les quantités sont des entiers, et l'opérateur de division aussi.

### Énoncé

> Le script divise chacune des dix quantités par 4 et somme les résultats. Les quantités et le diviseur sont déclarés comme des ENTIERS. Donnez la somme rendue par le script.

### Ce qui vous est fourni

Les dix quantités, le diviseur, et le type déclaré des variables.

### Ce qui est attendu

32 — la somme des quotients entiers.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`DV-09_sujet.gh`

### Barème

1 point si la somme des quotients entiers est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `DV-09_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Diviser chaque quantité en respectant le type entier.

**Étape 2.** Sommer.

**Étape 3.** Comparer au résultat qu'aurait donné une division réelle.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Calculer en réel et rendre 37. Sur des entiers, la division tronque : 7 ÷ 4 donne 1 et non 1,75. L'écart de 5 est ici visible, mais le même script rendrait un résultat plausible sur d'autres données — et c'est ce qui rend l'erreur durable.

### Pièges fréquents

- Diviser en réel.
- Arrondir au lieu de tronquer : sur ces données les deux diffèrent.

### Pourquoi ce jeu de données

Dix quantités dont aucune n'est multiple de 4 : la troncature agit à chaque terme, et l'écart s'accumule au lieu de se compenser. Les deux réponses, 32 et 37, sont assez proches pour paraître toutes deux crédibles — c'est exactement le danger.

### Limite de la correction automatique

> Ce que le script doit rendre dépend du métier : pour des panneaux entiers, la troncature est peut-être juste, ou peut-être faut-il arrondir au supérieur. L'exercice porte sur ce que le langage FAIT, pas sur ce qu'il faudrait vouloir.

### Pour aller plus loin

- Reprendre en déclarant les variables en réel et mesurer l'écart.
- Rendre le nombre de panneaux réellement nécessaires, arrondi au supérieur.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `DV-09_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `DV-09_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `DV-09.json` | Descripteur pour le plugin Magpie |
| `DV-09_fiche.md` | La présente fiche |
| `DV-09_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `DV-09_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `DV-09_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
