# AV-01 — Converger vers une portée

**Fiche d'exercice Magpie** · Lot AV — Algorithmique avancée

| | |
|---|---|
| **Thématique** | AV1 · Boucles et itération |
| **Référence au référentiel** | REF-093 |
| **Compétence visée** | Faire converger un calcul par itérations successives jusqu'à un critère d'arrêt. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 35 min |
| **Prérequis** | A-30 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire converger un calcul par itérations successives jusqu'à un critère d'arrêt.

### Contexte

La flèche d'une poutre dépend de sa portée d'une façon qui ne s'inverse pas simplement : on cherche la portée qui donne la flèche admissible.

### Énoncé

> La flèche admissible est atteinte pour une portée comprise entre 1 000 et 4 000 mm. Approchez cette portée par bissection jusqu'à ce que l'intervalle passe sous 1 mm, et donnez le nombre d'itérations nécessaires.

### Ce qui vous est fourni

La fonction de flèche, l'intervalle de départ et le critère d'arrêt.

### Ce qui est attendu

Un nombre entier : combien de bissections ont été nécessaires pour atteindre le critère.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`AV-01_sujet.gh`

### Barème

1 point si le nombre d'itérations vaut 12 et si la sortie se fait sur le critère, non sur un compte.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `AV-01_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 12 — le nombre de bissections pour ramener 3 000 mm sous 1 mm.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Poser l'intervalle de départ et le critère d'arrêt avant d'écrire la boucle.

**Étape 2.** À chaque passage, couper l'intervalle en deux et garder la moitié qui encadre la solution.

**Étape 3.** Compter les passages.

**Étape 4.** Sortir dès que la largeur de l'intervalle passe sous 1 mm.

**Étape 5.** Contrôler : 3 000 divisé douze fois par deux vaut 0,73 mm, onze fois seulement 1,46.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Fixer le nombre d'itérations à l'avance plutôt que de sortir sur un critère. Une boucle à compte fixe s'arrête trop tôt ou tourne pour rien ; c'est le critère qui doit commander, et c'est là toute la différence entre répéter et converger.

### Pièges fréquents

- Boucle sans critère de sortie : elle tourne indéfiniment.
- Garder la mauvaise moitié de l'intervalle : la boucle converge, mais ailleurs.

### Pourquoi ce jeu de données

L'intervalle de départ vaut 3 000 mm : chaque bissection le divise par deux, il faut donc douze passages pour descendre sous 1 mm. Le compte est vérifiable à la main, ce qui permet de contrôler la boucle sans la croire sur parole.

### Limite de la correction automatique

> L'itération demande un plugin de boucle : ce n'est pas natif. C'est le nombre d'itérations qui est validé, pas le montage.

### Pour aller plus loin

- Passer le critère à 0,1 mm et prévoir le nombre d'itérations avant de le mesurer.
- Comparer à une recherche par pas constant et chiffrer l'écart.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `AV-01_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `AV-01_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `AV-01.json` | Descripteur pour le plugin Magpie |
| `AV-01_fiche.md` | La présente fiche |
| `AV-01_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `AV-01_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `AV-01_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
