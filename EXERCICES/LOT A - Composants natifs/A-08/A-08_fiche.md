# A-08 — Booléen et nombre

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A2 · Types, conversion et valeurs |
| **Référence au référentiel** | REF-040, REF-059 |
| **Compétence visée** | Dénombrer les éléments d'un lot qui satisfont une condition, en exploitant l'équivalence entre vrai et 1. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | A-06 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-01 Score visible |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Dénombrer les éléments d'un lot qui satisfont une condition, en exploitant l'équivalence entre vrai et 1.

### Contexte

Le contrôle de réception d'un lot de traverses porte sur une cote nominale de 1 200 mm, avec une tolérance de ± 5 mm.

### Énoncé

> Les cotes relevées sur les 28 traverses du lot vous sont fournies. Comptez combien de traverses sortent de la tolérance, sans écarter aucun élément de la liste.

### Ce qui vous est fourni

Les 28 cotes relevées sur le lot, en millimètres, ainsi que la cote nominale de 1 200 mm et la tolérance de 5 mm.

### Ce qui est attendu

Un nombre entier : combien de traverses sortent de la tolérance.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-08_sujet.gh`

### Barème

1 point si le compte est exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-08_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 11 — le nombre de traverses dont l'écart à 1 200 mm dépasse 5 mm.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Poser Larger Than (Maths > Operators) : liste sur A, slider sur B.

**Étape 2.** La sortie est une liste de booléens.

**Étape 3.** Poser Mass Addition (Maths > Operators) sur cette liste de booléens.

**Étape 4.** Le total correspond au nombre de valeurs True.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter les traverses conformes au lieu des rebuts — le complément à 28 — ou traiter l'écart sans le ramener en valeur absolue, ce qui ne retient que les cotes trop grandes et laisse passer les trop petites.

### Pièges fréquents

- Brancher Mass Addition sur la liste d'origine au lieu des booléens.
- Utiliser Larger Than au lieu de Larger Than or Equal quand l'énoncé dit « au moins ».

### Pourquoi ce jeu de données

28 cotes resserrées autour de 1 200 : impossible de compter à l'œil. Les 11 hors-tolérance sont répartis dans les deux sens — 7 trop grandes, 4 trop petites — pour que l'oubli de la valeur absolue donne 7 au lieu de 11 et se voie donc immédiatement.

### Pour aller plus loin

- Compter les valeurs comprises entre deux bornes avec Gate And.
- Afficher le pourcentage plutôt que le compte.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-08_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-08_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-08.json` | Descripteur pour le plugin Magpie |
| `A-08_fiche.md` | La présente fiche |
| `A-08_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-08_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-08_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
