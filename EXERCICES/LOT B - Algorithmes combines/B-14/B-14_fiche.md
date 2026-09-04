# B-14 — Numérotation et étiquetage automatiques

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B4 · Données, métrés et livrables |
| **Référence au référentiel** | REF-066, REF-081, REF-057 |
| **Compétence visée** | Ordonner des éléments selon un critère composé, en respectant l'ordre de priorité des critères. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 22 min |
| **Prérequis** | A-49, A-27 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 18 composants |
| **Gamification associée** | G-11 Mots croisés de composants |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire des repères lisibles, cohérents et positionnés dans le modèle.

### Contexte

Le repérage suit l'ordre de pose : rangée du bas d'abord, de gauche à droite. Le poseur lit les repères dans cet ordre-là.

### Énoncé

> Numérote les 14 pièces de l'assemblage de gauche à droite puis de bas en haut, au format R-A01 à R-A14, et place l'étiquette au centre de gravité de chaque pièce, orientée face à la vue de face.

### Ce qui vous est fourni

Un assemblage de 14 solides internalisés.

### Ce qui est attendu

7 — le rang de la pièce située à 800 mm en abscisse et 900 mm en ordonnée.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-14_sujet.gh`

### Barème

2 points pour l'ordre, 1 point pour le format, 1 point pour le placement.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-14_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Récupérer les centroïdes avec Volume.

**Étape 2.** Décomposer les points avec Deconstruct pour obtenir X et Z.

**Étape 3.** Construire une clé de tri combinée : Z multiplié par un grand facteur plus X.

**Étape 4.** Trier les pièces et les centroïdes avec Sort List sur cette clé.

**Étape 5.** Générer les numéros avec Series et Format (masque R-A{0:00}).

**Étape 6.** Poser Text Tag 3D avec un plan orienté XZ pour la lisibilité en vue de face.

**Étape 7.** Contrôler l'ordre obtenu dans un Panel.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Trier d'abord par abscisse : la pièce reçoit alors le rang 5. L'ordre des critères n'est pas commutatif — trier par colonne puis par rangée numérote le mur de haut en bas par bandes verticales, et le poseur ne s'y retrouve plus.

### Pièges fréquents

- Clé de tri mal pondérée : le tri secondaire prend le pas sur le tri principal.
- Format sans masque : les numéros s'affichent sans zéro de tête.
- Étiquettes orientées dans le plan XY donc illisibles en élévation.

### Pourquoi ce jeu de données

Quatorze pièces sur trois rangées, saisies dans le désordre. Pour la pièce visée, les trois lectures donnent trois rangs différents : 7 dans l'ordre demandé, 5 en triant par colonne, 4 dans l'ordre de saisie. Aucune confusion possible.

### Limite de la correction automatique

> Le rang dépend de l'ordre des critères, qui est une CONVENTION d'atelier. L'exercice en impose une ; un autre atelier numéroterait autrement, et aurait raison. Ce qui se vérifie est l'application de la convention, pas son bien-fondé.

### Pour aller plus loin

- Ajouter le repère dans un attribut Rhino via Elefront.
- Générer une planche de repérage cotée.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-14_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-14_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-14.json` | Descripteur pour le plugin Magpie |
| `B-14_fiche.md` | La présente fiche |
| `B-14_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-14_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-14_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
