# B-03 — Façade à trame variable pilotée par un attracteur

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B1 · Architecture et construction |
| **Référence au référentiel** | REF-068, REF-053, REF-054 |
| **Compétence visée** | Piloter une variation continue par la distance à un attracteur, et en chiffrer l'effet global. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | A-39, A-25 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 16 composants |
| **Gamification associée** | G-25 Animation + G-13 Casino motifs assortis |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire varier un paramètre géométrique en fonction d'une distance, méthode fondamentale du paramétrique.

### Contexte

La façade doit laisser passer plus de lumière près de l'atrium. Le maître d'ouvrage, lui, achète du vitrage au mètre carré.

### Énoncé

> Sur la trame de façade 12 × 8, perce chaque panneau d'une ouverture circulaire dont le rayon varie de 50 mm (loin de l'attracteur) à 350 mm (au plus près). Le point attracteur est déplaçable dans Rhino.

### Ce qui vous est fourni

Une surface de façade et un point attracteur référencés.

### Ce qui est attendu

13,30 m² d'ouverture au total, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-03_sujet.gh`

### Barème

2 points pour la variation, 1 point pour la borne de sécurité du rayon.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-03_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Diviser la façade avec Divide Surface ou Rectangular Array pour obtenir les 96 centres de panneaux.

**Étape 2.** Mesurer la distance de chaque centre à l'attracteur avec Distance.

**Étape 3.** Poser Bounds sur ces distances pour obtenir le domaine réel.

**Étape 4.** Poser Remap Numbers : source = domaine des distances, cible = domaine 350 à 50 (inversé).

**Étape 5.** Poser Circle avec les centres et les rayons remappés.

**Étape 6.** Percer les panneaux avec Region Difference (2D) ou Solid Difference (3D).

**Étape 7.** Vérifier que le rayon reste inférieur à la demi-largeur du panneau.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Prendre le rayon MOYEN et le multiplier par 96 : on obtient 12,06 m². L'aire varie comme le CARRÉ du rayon, jamais comme le rayon — la moyenne des carrés n'est pas le carré de la moyenne, et l'écart de 1,24 m² se paie au vitrage.

### Pièges fréquents

- Domaine cible non inversé : les grandes ouvertures se retrouvent au plus loin.
- Rayon supérieur à la demi-largeur : la découpe déborde sur les panneaux voisins.
- Attracteur non internalisé : la définition casse à l'ouverture du fichier.

### Pourquoi ce jeu de données

96 panneaux, rayon de 50 à 350 mm selon la distance à l'attracteur : un rapport de sept sur le rayon, donc de quarante-neuf sur l'aire. C'est cette non-linéarité qui rend la moyenne trompeuse, et elle l'est toujours dans le même sens — par défaut.

### Limite de la correction automatique

> L'exercice chiffre l'aire percée. Il ne vérifie pas que les ouvertures restent dans leur panneau : au rayon maximal, 350 mm dans une maille de 1 200, la marge est confortable — elle ne le serait plus sur une trame plus serrée.

### Pour aller plus loin

- Piloter la rotation des panneaux plutôt que le rayon.
- Utiliser une courbe attractrice au lieu d'un point.
- Contraindre le taux de vide global à une valeur cible.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-03_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-03_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-03.json` | Descripteur pour le plugin Magpie |
| `B-03_fiche.md` | La présente fiche |
| `B-03_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-03_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-03_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
