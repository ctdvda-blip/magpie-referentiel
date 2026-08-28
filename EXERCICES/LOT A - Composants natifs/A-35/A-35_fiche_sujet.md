# A-35 — Diviser et évaluer une courbe

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A8 · Géométrie vectorielle et filaire |
| **Référence au référentiel** | REF-064 |
| **Compétence visée** | Répartir des positions régulières le long d'une courbe et récupérer le repère local en chaque position. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-34 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Répartir des positions régulières le long d'une courbe et récupérer le repère local en chaque position.

### Contexte

Un conduit souple est maintenu par des colliers régulièrement espacés le long de son tracé ; chaque collier est perpendiculaire au conduit.

### Énoncé

> Le tracé du conduit vous est fourni. Placez 12 colliers de 5 de rayon, régulièrement espacés le long du tracé et perpendiculaires à celui-ci en chaque point.

### Ce qui vous est fourni

Une courbe libre internalisée.

### Ce qui est attendu

12 cercles de rayon 5, perpendiculaires au tracé.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-35_sujet.gh`

### Barème

1 point si 12 cercles perpendiculaires sont produits.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
