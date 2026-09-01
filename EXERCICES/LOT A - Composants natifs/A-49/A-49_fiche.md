# A-49 — Centre de gravité

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A11 · Mesures géométriques |
| **Référence au référentiel** | REF-081 |
| **Compétence visée** | Localiser le centre de gravité de pièces et s'en servir comme point d'accroche. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-47 |
| **Mode de validation** | GeometryTolerance — tolérance 0,5 mm |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-05 Badges et trophées |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Localiser le centre de gravité de pièces et s'en servir comme point d'accroche.

### Contexte

Chaque pièce d'un lot reçoit son repère au centre, à l'endroit où l'étiquette sera collée et où l'élingue sera accrochée.

### Énoncé

> Six pièces vous sont fournies. Placez au centre de gravité de chacune une étiquette portant son numéro.

### Ce qui vous est fourni

6 solides internalisés.

### Ce qui est attendu

Six étiquettes numérotées, placées aux centres de gravité.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,5 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-49_sujet.gh`

### Barème

1 point si les 6 étiquettes sont bien placées.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-49_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Volume sur la liste des solides : la sortie C donne les centroïdes.

**Étape 2.** Poser Series pour produire les numéros de 1 à 6.

**Étape 3.** Formater les numéros avec Format si un affichage sur deux chiffres est souhaité.

**Étape 4.** Poser Text Tag 3D avec les centroïdes en L et les textes en T.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Prendre le centre de la boîte englobante plutôt que le centre de gravité : les deux coïncident sur une pièce symétrique et divergent sur une pièce en L — et c'est précisément là que l'élingue compte.

### Pièges fréquents

- Area donne le centroïde surfacique, Volume le centroïde volumique : ils diffèrent.
- Text Tag 3D n'apparaît qu'en aperçu, il ne se cuit qu'avec un Bake explicite.

### Pour aller plus loin

- Trier les pièces par masse en pondérant par la densité.
- Placer un repère orienté au centroïde.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-49_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-49_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-49.json` | Descripteur pour le plugin Magpie |
| `A-49_fiche.md` | La présente fiche |
| `A-49_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-49_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-49_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
