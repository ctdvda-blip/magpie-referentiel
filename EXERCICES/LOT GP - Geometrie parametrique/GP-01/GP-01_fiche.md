# GP-01 — Un plan coté qui suit ses paramètres

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP1 · Plan paramétrique |
| **Référence au référentiel** | REF-065, REF-066 |
| **Compétence visée** | Produire un tracé 2D dont les cotes se mettent à jour avec la géométrie, plutôt que d'être écrites à côté. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 25 min |
| **Prérequis** | A-34 |
| **Mode de validation** | NumericTolerance — tolérance 0,1 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire un tracé 2D dont les cotes se mettent à jour avec la géométrie, plutôt que d'être écrites à côté.

### Contexte

Un plan de réservation part au gros œuvre ; la dimension bouge encore, et une cote fausse coûte un percement au mauvais endroit.

### Énoncé

> La réservation est rectangulaire, avec un congé de 60 mm à chaque angle. Produisez son tracé pour une réservation de 1 400 × 850 mm, et donnez le périmètre développé du contour.

### Ce qui vous est fourni

Deux valeurs réglables pour la largeur et la hauteur, et une troisième pour le rayon de congé.

### Ce qui est attendu

Le périmètre du contour congé compris, à 0,1 mm près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-01_sujet.gh`

### Barème

1 point si le périmètre est juste à 0,1 mm près et si la cote suit une modification de largeur.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `GP-01_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Construire le rectangle à partir des deux valeurs réglables.

**Étape 2.** Appliquer le congé par le paramètre du composant de tracé plutôt qu'en raccordant les angles après coup.

**Étape 3.** Mesurer la longueur du contour obtenu.

**Étape 4.** Faire varier la largeur et vérifier que la cote suit.

**Étape 5.** Contrôler le résultat sur un cas connu : congé nul, le périmètre doit valoir deux fois la somme des côtés.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Calculer le périmètre du rectangle nu et y ajouter les quatre quarts de cercle, sans retrancher ce que les congés ont supprimé des côtés droits. On obtient une valeur trop grande d'environ 4 × (2r − πr/2), soit une erreur systématique que le contexte ne signale pas.

### Pièges fréquents

- Congé appliqué après coup : le contour cesse d'être une seule courbe et la mesure porte sur des morceaux.
- Rayon de congé supérieur à la moitié du petit côté : le tracé devient impossible et le composant se met en défaut.

### Pourquoi ce jeu de données

Le congé de 60 mm est assez grand pour que l'oubli du retranchement se voie au dixième de millimètre, et assez petit pour rester une réservation plausible.

### Limite de la correction automatique

> Le périmètre valide le TRACÉ, pas la cotation. Qu'un plan porte les bonnes cotes, aux bons endroits et à la bonne échelle ne se vérifie pas par un nombre : c'est le formateur qui ouvre la mise en page.

### Pour aller plus loin

- Ajouter une cotation automatique de la largeur et vérifier qu'elle suit la valeur réglable.
- Passer le congé à zéro et retrouver le périmètre du rectangle.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `GP-01_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `GP-01_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `GP-01.json` | Descripteur pour le plugin Magpie |
| `GP-01_fiche.md` | La présente fiche |
| `GP-01_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `GP-01_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `GP-01_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
