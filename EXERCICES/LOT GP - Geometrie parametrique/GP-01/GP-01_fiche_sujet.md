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
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
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

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
