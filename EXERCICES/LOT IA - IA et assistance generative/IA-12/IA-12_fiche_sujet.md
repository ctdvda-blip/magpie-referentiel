# IA-12 — Faire construire un graphe par un agent

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA6 · Agents et protocoles |
| **Référence au référentiel** | REF-136, REF-137, REF-138 |
| **Compétence visée** | Faire construire une définition par un agent connecté à Grasshopper, et relever le résultat produit. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 35 min |
| **Prérequis** | IA-07 |
| **Mode de validation** | NumericTolerance — tolérance 0,1 |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-28 Pilotage à distance |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire construire une définition par un agent connecté à Grasshopper, et relever le résultat produit.

### Contexte

Une série de définitions répétitives doit être produite : les monter une à une à la main n'est pas raisonnable.

### Énoncé

> Avec un agent relié à Grasshopper, faites construire une définition qui répartit des points le long d'une courbe et renvoie la longueur cumulée des segments obtenus. Travaillez sur une copie du fichier, et donnez la longueur obtenue.

### Ce qui vous est fourni

Un serveur d'outils relié à Rhino et Grasshopper, en service, et la courbe de référence.

### Ce qui est attendu

Une valeur décimale : la longueur cumulée, en millimètres.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-12_sujet.gh`

### Barème

1 point si la longueur est juste à 0,1 près et si le travail a été mené sur une copie.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
