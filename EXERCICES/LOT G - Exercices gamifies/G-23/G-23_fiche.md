# G-23 — Le duel

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G5 · Performance et compétition |
| **Référence au référentiel** | REF-082, REF-044 |
| **Compétence visée** | Produire une nomenclature triée et la rendre sous une forme comparable entre participants. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | B-12 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 18 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Confronter deux approches d'un même problème et en mesurer les écarts.

### Contexte

Le duel confronte deux approches du même problème. Il n'a de sens que si le résultat attendu est strictement le même pour tous — sinon on compare des réponses, pas des méthodes.

### Énoncé

> Même énoncé pour tous : produire la nomenclature triée de l'assemblage. Trois critères départagent les participants : justesse, nombre de composants, temps d'exécution de la définition.

### Ce qui vous est fourni

Un assemblage identique pour tous les participants.

### Ce qui est attendu

Les quantités, par ordre décroissant : 44, 31, 27, 22, 18, 14, 9, 6.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-23_sujet.gh`

### Barème

Classement combiné sur les trois critères, validation à la justesse seule.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-23_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Produire la nomenclature comme dans l'exercice B-12.

**Étape 2.** Relever le nombre de composants dans le panneau de métriques.

**Étape 3.** Activer le Profiler pour relever le temps de calcul de la définition.

**Étape 4.** Soumettre et exporter le résultat.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Trier par ORDRE ALPHABÉTIQUE des désignations, ce que fait `Sort List` sur des textes, au lieu de trier les quantités. On obtient une nomenclature parfaitement présentable et un classement faux — et comme les deux tris produisent huit lignes, rien ne le signale.

### Pièges fréquents

- Optimiser le temps de calcul au détriment de la justesse.
- Comparer des temps mesurés sur des machines différentes.

### Pourquoi ce jeu de données

Huit pièces aux quantités toutes différentes, de 6 à 44, et dont l'ordre alphabétique ne coïncide avec l'ordre des quantités en aucun point : les deux tris sont totalement disjoints, ce qui rend l'erreur immédiatement lisible.

### Limite de la correction automatique

> La justesse seule valide. Le nombre de composants et le temps d'exécution départagent au CLASSEMENT, mais ne sont pas mesurés par la définition — c'est le plugin Magpie qui les relève.

### Pour aller plus loin

- Duel en direct pendant une session de formation.
- Classement par thématique du référentiel.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-23_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-23_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-23.json` | Descripteur pour le plugin Magpie |
| `G-23_fiche.md` | La présente fiche |
| `G-23_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-23_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-23_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
