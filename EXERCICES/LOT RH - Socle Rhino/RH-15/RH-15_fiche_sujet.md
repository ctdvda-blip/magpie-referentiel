# RH-15 — Le développé d'un cheminement

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Modélisation Rhino |
| **Référence au référentiel** | REF-009 |
| **Compétence visée** | Mesurer la longueur réellement parcourue par une polyligne, et non la distance entre ses extrémités. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-14 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mesurer la longueur réellement parcourue par une polyligne, et non la distance entre ses extrémités.

### Contexte

On chiffre un linéaire de garde-corps le long d'un cheminement qui tourne quatre fois.

### Énoncé

> Les six sommets du cheminement vous sont fournis. Donnez sa longueur développée, en millimètres.

### Ce qui vous est fourni

Les coordonnées en plan des six sommets.

### Ce qui est attendu

13 400 mm — la somme des cinq segments.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-15_sujet.gh`

### Barème

1 point si le développé est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
