# IA-27 — Le script qui tourne et compte mal

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA2 · Composants scriptés assistés |
| **Référence au référentiel** | REF-124 |
| **Compétence visée** | Localiser une erreur de bornes dans un code qui s'exécute sans planter et rend un résultat crédible. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 16 min |
| **Prérequis** | IA-05 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-20 La chasse aux bugs |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Localiser une erreur de bornes dans un code qui s'exécute sans planter et rend un résultat crédible.

### Contexte

Un script qui plante se répare. Un script qui rend quatorze au lieu de quinze se livre, et l'écart se découvre trois semaines plus tard sur un autre jeu.

### Énoncé

> Le composant fourni doit compter les longueurs qui dépassent 1 500 mm parmi les trente relevées. Il rend un résultat faux. Corrigez-le et donnez le compte exact.

### Ce qui vous est fourni

Le composant fautif et les trente longueurs relevées.

### Ce qui est attendu

15 longueurs dépassent 1 500 mm.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-27_sujet.gh`

### Barème

1 point si le compte corrigé est exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-27_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Comparer le résultat du composant à un comptage natif.

**Étape 2.** Chercher où les deux divergent : la dernière valeur.

**Étape 3.** Corriger la borne de la boucle.

**Étape 4.** Vérifier que les deux comptes coïncident.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Accepter le quatorze que rend le composant. Sa boucle s'arrête un cran trop tôt et ne teste jamais le dernier élément — qui vaut ici 2 592 mm et dépasse largement. L'erreur ne se voit que si la dernière valeur est justement concernée.

### Pièges fréquents

- Corriger le seuil au lieu de la borne.
- Conclure que le composant est juste parce qu'il ne plante pas.

### Pourquoi ce jeu de données

Trente longueurs de 200 à 3 200 mm, et la DERNIÈRE dépasse le seuil : le jeu est choisi pour que le défaut de bornes se manifeste. Sur les deux tiers des jeux possibles, le même code faux rendrait la bonne réponse.

### Limite de la correction automatique

> Le compte exact prouve que le défaut est corrigé, pas qu'il est COMPRIS. Remplacer la boucle par un composant natif donne la bonne valeur sans avoir jamais vu l'erreur — l'exercice demande de la nommer, et cela se lit sur le canvas.

### Pour aller plus loin

- Chercher un jeu sur lequel le code faux rend la bonne réponse.
- Faire produire un test qui attrape ce défaut.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-27_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-27_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-27.json` | Descripteur pour le plugin Magpie |
| `IA-27_fiche.md` | La présente fiche |
| `IA-27_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-27_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-27_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
