# AV-03 — Chercher la meilleure trame

**Fiche d'exercice Magpie** · Lot AV — Algorithmique avancée

| | |
|---|---|
| **Thématique** | AV3 · Design génératif |
| **Référence au référentiel** | REF-095 |
| **Compétence visée** | Poser un problème de recherche de forme — variables, objectif, contraintes — et juger l'optimum obtenu. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 40 min |
| **Prérequis** | AV-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Poser un problème de recherche de forme — variables, objectif, contraintes — et juger l'optimum obtenu.

### Contexte

Une façade doit être calepinée : moins de panneaux coûte moins cher, mais aucun panneau ne peut dépasser 2 400 mm.

### Énoncé

> La façade mesure 18 600 mm de long. Cherchez le calepinage qui minimise le nombre de panneaux sans qu'aucun dépasse 2 400 mm, et donnez ce nombre.

### Ce qui vous est fourni

La longueur de façade, la largeur maximale de panneau, et un moteur de recherche.

### Ce qui est attendu

Un nombre entier : combien de panneaux au minimum.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`AV-03_sujet.gh`

### Barème

1 point si le nombre vaut 8 et si la contrainte figure dans la fonction évaluée.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `AV-03_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 8 — le nombre minimal de panneaux.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Écrire d'abord ce qu'on minimise et sous quelle contrainte.

**Étape 2.** Exprimer la contrainte DANS la fonction évaluée, non à côté.

**Étape 3.** Lancer la recherche.

**Étape 4.** Contrôler l'optimum par le calcul direct : 18 600 ÷ 2 400 arrondi au supérieur.

**Étape 5.** Conclure : quand le calcul direct suffit, le moteur de recherche est un luxe — savoir le reconnaître fait partie de la compétence.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Laisser le moteur chercher sans contrainte et retenir son meilleur résultat. Sans la contrainte des 2 400 mm exprimée dans la fonction évaluée, l'optimum est un panneau unique de 18 600 mm : mathématiquement parfait, physiquement absurde. Une recherche de forme ne vaut que ce que vaut ce qu'on lui demande d'optimiser.

### Pièges fréquents

- Contrainte laissée hors de la fonction évaluée.
- Employer un moteur de recherche là où une division suffit, et ne pas s'en apercevoir.

### Pourquoi ce jeu de données

18 600 divisé par 2 400 vaut 7,75 : la réponse est 8, et l'exercice ne se résout pas en arrondissant au plus proche. C'est aussi un cas où le moteur de recherche est un détour — le calcul direct suffit, et c'est un enseignement en soi.

### Limite de la correction automatique

> La recherche demande un moteur d'optimisation. Ce qui est validé est le nombre de panneaux ; l'exercice vaut surtout pour la formulation du problème, que le formateur relit.

### Pour aller plus loin

- Ajouter une contrainte de panneaux tous égaux et refaire la recherche.
- Introduire un coût par joint et voir l'optimum se déplacer.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `AV-03_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `AV-03_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `AV-03.json` | Descripteur pour le plugin Magpie |
| `AV-03_fiche.md` | La présente fiche |
| `AV-03_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `AV-03_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `AV-03_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
