# AV-02 — Une chaînette qui se stabilise

**Fiche d'exercice Magpie** · Lot AV — Algorithmique avancée

| | |
|---|---|
| **Thématique** | AV2 · Simulation physique |
| **Référence au référentiel** | REF-094 |
| **Compétence visée** | Conduire une simulation jusqu'à l'équilibre et relever une grandeur sur l'état stabilisé. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 35 min |
| **Prérequis** | AV-01 |
| **Mode de validation** | NumericTolerance — tolérance 5 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Conduire une simulation jusqu'à l'équilibre et relever une grandeur sur l'état stabilisé.

### Contexte

Un câble de suspension prend, sous son propre poids, une forme qu'on ne dessine pas : on la laisse s'établir.

### Énoncé

> Le câble mesure 6 000 mm et ses deux ancrages sont distants de 4 800 mm. Laissez la forme s'établir sous son poids propre, et donnez la flèche au point bas, en millimètres.

### Ce qui vous est fourni

Les deux ancrages, la longueur de câble et le moteur de simulation.

### Ce qui est attendu

La flèche au point bas, à 5 mm près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 5.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`AV-02_sujet.gh`

### Barème

1 point si la flèche est juste à 5 mm près sur un état stabilisé.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `AV-02_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Discrétiser le câble en segments réguliers.

**Étape 2.** Ancrer les deux extrémités, laisser le reste libre.

**Étape 3.** Appliquer le poids propre et lancer la simulation.

**Étape 4.** Attendre que la valeur relevée cesse d'évoluer — c'est le seul critère d'arrêt honnête.

**Étape 5.** Mesurer l'écart vertical entre les ancrages et le point bas.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Relever la valeur avant stabilisation. Une simulation affiche un résultat dès la première itération, et il change encore. Lire trop tôt donne une valeur plausible et fausse — le seul contrôle est que la valeur cesse de bouger.

### Pièges fréquents

- Trop peu de segments : la forme est anguleuse et la flèche sous-évaluée.
- Lire la valeur en cours de convergence.

### Pourquoi ce jeu de données

6 000 mm de câble pour 4 800 mm de portée : le mou est assez important pour que la flèche soit franche, et la forme obtenue reste une chaînette, dont la flèche se vérifie par le calcul.

### Limite de la correction automatique

> La simulation demande un moteur dédié, non natif. La tolérance de 5 mm tient compte de la convergence, qui n'est jamais exactement reproductible.

### Pour aller plus loin

- Rallonger le câble de 10 % et prévoir l'effet sur la flèche avant de le mesurer.
- Comparer à la formule de la chaînette.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `AV-02_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `AV-02_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `AV-02.json` | Descripteur pour le plugin Magpie |
| `AV-02_fiche.md` | La présente fiche |
| `AV-02_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `AV-02_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `AV-02_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
