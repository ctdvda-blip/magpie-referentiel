# G-20 — La chasse aux bugs

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G4 · Connaissance et mémorisation |
| **Référence au référentiel** | REF-041, REF-053, REF-055 |
| **Compétence visée** | Diagnostiquer une définition qui produit un résultat plausible mais faux, sans en changer la structure. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | A-07, A-09, A-24 |
| **Mode de validation** | NumericTolerance — tolérance 1 |
| **Solution de référence** | 30 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Développer le réflexe de diagnostic sur une définition qui ne produit pas le résultat attendu.

### Contexte

Une définition qui plante se répare ; une définition qui rend six modules au lieu de vingt-quatre se livre. C'est le second cas qui coûte cher, et c'est celui-là qu'on entraîne.

### Énoncé

> Cette définition devrait produire 24 modules, elle n'en produit que 6. Trois défauts se cachent dans le graphe. Identifie-les et corrige la définition sans en changer la structure générale.

### Ce qui vous est fourni

Une définition fautive de 30 composants.

### Ce qui est attendu

2 306 400 mm² — l'aire totale des 24 modules retrouvés.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-20_sujet.gh`

### Barème

3 points, 1 par défaut corrigé.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-20_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Brancher un Param Viewer en plusieurs points de la chaîne pour localiser la rupture.

**Étape 2.** Défaut 1 : une correspondance en Shortest List tronque une liste de 24 à 6.

**Étape 3.** Défaut 2 : un Flatten mal placé écrase la structure d'arbre attendue.

**Étape 4.** Défaut 3 : une valeur nulle en entrée invalide quatre éléments.

**Étape 5.** Corriger les trois points et vérifier le compte final.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Corriger le symptôme en ajoutant un `Duplicate Data` jusqu'à obtenir vingt-quatre objets. Le compte devient juste, l'aire aussi — et la définition reste fausse, puisqu'elle empile quatre fois la même rangée au même endroit. Le compte seul ne suffit donc pas à valider une correction.

### Pièges fréquents

- Corriger le symptôme en aval plutôt que la cause en amont.
- Supprimer le composant fautif au lieu de le régler : le contrôle du nombre échoue.

### Pourquoi ce jeu de données

Six par quatre, modules de 310 mm : 24 modules et 2 306 400 mm². Le nombre attendu est ANNONCÉ dans l'énoncé — c'est l'aire qui est l'indicateur, précisément parce que le compte est déjà connu et ne prouve rien.

### Limite de la correction automatique

> L'aire ne dit pas que les trois défauts ont été trouvés, ni qu'ils l'ont été proprement. Elle dit que le résultat est revenu. La qualité de la correction se lit sur le canvas.

### Pour aller plus loin

- Cinq défauts dont deux sans effet visible.
- Définition fournie par un autre apprenant.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-20_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-20_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-20.json` | Descripteur pour le plugin Magpie |
| `G-20_fiche.md` | La présente fiche |
| `G-20_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-20_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-20_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
