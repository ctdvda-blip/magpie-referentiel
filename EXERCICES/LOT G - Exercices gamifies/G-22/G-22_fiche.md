# G-22 — Le boss de fin de chapitre

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G5 · Performance et compétition |
| **Référence au référentiel** | REF-047, REF-051, REF-068, REF-079 |
| **Compétence visée** | Enchaîner structuration en arbre, filtrage à deux conditions et synthèse, sans validation intermédiaire. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 45 min |
| **Prérequis** | Tous les exercices du chapitre Données |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 32 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Éprouver en une seule tâche l'ensemble des notions du chapitre Données et logique.

### Contexte

Le boss de fin de chapitre éprouve l'ensemble des notions du chapitre en une seule tâche. Ce qu'il mesure n'est pas la connaissance des composants mais la capacité à tenir une chaîne longue sans se perdre.

### Énoncé

> Trois phases s'enchaînent sans validation intermédiaire. Phase 1 : structurer les données en arbre. Phase 2 : filtrer selon deux conditions combinées. Phase 3 : produire le tableau de synthèse. Toute erreur en phase 3 impose de reprendre depuis la phase 1.

### Ce qui vous est fourni

Un jeu de 240 valeurs et un modèle de tableau de sortie.

### Ce qui est attendu

Le tableau de synthèse : 6, 5, 6, 5, 5, 8, 10, 4, puis 3 585, 3 369, 4 380, 3 594, 3 792, 5 796, 7 818, 3 150.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-22_sujet.gh`

### Barème

10 points, validation à 100 % uniquement.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-22_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Phase 1 : répartir les 240 valeurs en 12 branches de 20 avec Partition List puis contrôler au Param Viewer.

**Étape 2.** Phase 2 : construire les deux conditions et les combiner avec Gate And.

**Étape 3.** Phase 2 : filtrer chaque branche avec Dispatch en conservant la structure d'arbre.

**Étape 4.** Phase 3 : calculer par branche le compte, la somme et la moyenne avec Mass Addition et Average.

**Étape 5.** Phase 3 : assembler le tableau avec Merge dans l'ordre imposé et soumettre.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Structurer en huit branches CONSÉCUTIVES de trente au lieu de répartir une valeur sur deux — huit branches par pas de huit. Les deux découpages donnent huit branches de trente ; les comptes filtrés, eux, n'ont plus rien à voir, et rien ne signale lequel était demandé sinon l'énoncé.

### Pièges fréquents

- Aplatir l'arbre en phase 2 : les statistiques de phase 3 portent alors sur l'ensemble et non par branche.
- Ordre des colonnes du tableau non respecté.
- Moyenne calculée sur la liste filtrée mais compte calculé sur la liste complète.

### Pourquoi ce jeu de données

240 valeurs de 10 à 999. Le double filtre — supérieur à 400 ET multiple de 3 — laisse de 4 à 10 valeurs par branche : assez pour que les huit comptes diffèrent, trop peu pour qu'ils se ressemblent. Les huit sommes vont de 3 150 à 7 818, sans recouvrement possible.

### Limite de la correction automatique

> « Toute erreur en phase 3 impose de reprendre depuis la phase 1 » est une règle de JEU, pas une contrainte de l'outil. Rien n'empêche de corriger la seule phase 3 ; c'est l'apprenant qui s'impose la règle, et c'est tout l'intérêt.

### Pour aller plus loin

- Boss de chapitre pour chaque domaine du référentiel.
- Version chronométrée avec classement.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-22_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-22_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-22.json` | Descripteur pour le plugin Magpie |
| `G-22_fiche.md` | La présente fiche |
| `G-22_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-22_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-22_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
