# DV-02 — Un composant scripté qui parle à RhinoCommon

**Fiche d'exercice Magpie** · Lot DV — Développement, scripting et API

| | |
|---|---|
| **Thématique** | DV2 · API et librairies |
| **Référence au référentiel** | REF-101, REF-102, REF-103 |
| **Compétence visée** | Employer l'interface de programmation de Rhino depuis un composant scripté pour obtenir ce qu'aucun composant natif ne donne. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Expert |
| **Durée cible** | 35 min |
| **Prérequis** | IA-04 |
| **Mode de validation** | NumericTolerance — tolérance 1 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Employer l'interface de programmation de Rhino depuis un composant scripté pour obtenir ce qu'aucun composant natif ne donne.

### Contexte

On cherche, sur une courbe, le point où le rayon de courbure passe sous le rayon de cintrage de la machine — information qu'aucun composant natif ne rend directement.

### Énoncé

> Le rayon de cintrage minimal de la machine est de 250 mm. Sur la courbe fournie, donnez la longueur cumulée des portions où le rayon de courbure descend sous cette valeur, en millimètres.

### Ce qui vous est fourni

La courbe de tracé et le rayon de cintrage minimal.

### Ce qui est attendu

La longueur cumulée des portions trop cintrées, à 1 mm près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`DV-02_sujet.gh`

### Barème

1 point si la longueur est juste à 1 mm près et si le pas a été contrôlé par convergence.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `DV-02_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Choisir un pas d'échantillonnage et le justifier par rapport à la taille de la zone recherchée.

**Étape 2.** Parcourir la courbe et relever la courbure en chaque point, via l'interface de programmation.

**Étape 3.** Convertir la courbure en rayon — l'un est l'inverse de l'autre.

**Étape 4.** Repérer les intervalles où le rayon passe sous le seuil.

**Étape 5.** Sommer leurs longueurs, et contrôler en divisant le pas par deux : le résultat doit peu bouger.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Échantillonner la courbe trop grossièrement. La courbure varie continûment : un échantillon tous les 50 mm peut enjamber entièrement une zone trop cintrée et conclure que la pièce est fabricable. Le pas d'échantillonnage est un choix, et il doit être justifié.

### Pièges fréquents

- Confondre courbure et rayon : ils varient en sens inverse.
- Pas d'échantillonnage choisi au hasard, sans contrôle de convergence.

### Pourquoi ce jeu de données

La courbe présente une zone serrée d'une soixantaine de millimètres : assez large pour être trouvée avec un pas raisonnable, assez étroite pour être manquée avec un pas négligent.

### Pour aller plus loin

- Rendre le pas adaptatif : plus fin là où la courbure varie vite.
- Sortir aussi la position du point le plus cintré.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `DV-02_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `DV-02_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `DV-02.json` | Descripteur pour le plugin Magpie |
| `DV-02_fiche.md` | La présente fiche |
| `DV-02_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `DV-02_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `DV-02_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
