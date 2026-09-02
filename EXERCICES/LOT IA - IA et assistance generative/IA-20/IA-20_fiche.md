# IA-20 — Ce qu'un budget de calcul permet d'essayer

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA5 · Apprentissage automatique |
| **Référence au référentiel** | REF-131, REF-132 |
| **Compétence visée** | Dimensionner une campagne d'évaluations à partir du temps disponible, et mesurer l'écart avec ce qu'exigerait l'exploration exhaustive. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | IA-09 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-13 Chronomètre |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Dimensionner une campagne d'évaluations à partir du temps disponible, et mesurer l'écart avec ce qu'exigerait l'exploration exhaustive.

### Contexte

Chaque évaluation demande un calcul thermique complet. On dispose d'une nuit de machine.

### Énoncé

> Le budget est de 6 heures et chaque évaluation prend 42 secondes. Donnez le nombre d'évaluations réalisables.

### Ce qui vous est fourni

Le budget en heures, la durée d'une évaluation, et le nombre de paramètres et de niveaux du problème.

### Ce qui est attendu

514 évaluations tiennent dans le budget.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-20_sujet.gh`

### Barème

1 point si le nombre d'évaluations est juste et arrondi à l'inférieur.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-20_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Convertir le budget en secondes.

**Étape 2.** Diviser par la durée d'une évaluation.

**Étape 3.** Arrondir à l'entier INFÉRIEUR : une évaluation entamée ne compte pas.

**Étape 4.** Calculer, pour comparaison, la taille du plan complet.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Vouloir explorer toutes les combinaisons. Douze paramètres à cinq niveaux font 244 millions d'évaluations, soit trois cent vingt-cinq ans de machine. Ce n'est pas une question de patience : c'est ce qui rend le métamodèle nécessaire plutôt que confortable.

### Pièges fréquents

- Arrondir au supérieur.
- Oublier de convertir les heures en secondes.
- Croire qu'on peut approcher l'exhaustif en optimisant le calcul.

### Pourquoi ce jeu de données

514 évaluations pour un espace de 244 millions de points : le budget couvre deux millionièmes de pour cent de l'espace. Le chiffre n'est pas là pour impressionner — il dit que le plan d'expériences ne peut pas être régulier, et qu'il faut le choisir.

### Limite de la correction automatique

> Le nombre d'évaluations tenables ne dit pas LESQUELLES faire. C'est tout l'objet d'un plan d'expériences, et la qualité du métamodèle en dépend plus que leur nombre.

### Pour aller plus loin

- Trouver la durée d'évaluation qui permettrait mille essais.
- Comparer un plan aléatoire et un plan en hypercube latin à budget égal.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-20_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-20_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-20.json` | Descripteur pour le plugin Magpie |
| `IA-20_fiche.md` | La présente fiche |
| `IA-20_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-20_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-20_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
