# A-02 — Construire un point par coordonnées

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A1 · Interface, flux de données et paramètres |
| **Référence au référentiel** | REF-062 |
| **Compétence visée** | Construire une position dans l'espace à partir de trois valeurs séparées, y compris négatives. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-01 |
| **Mode de validation** | GeometryTolerance — tolérance 0,01 mm |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-26 Feedback visuel immédiat |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Construire une position dans l'espace à partir de trois valeurs séparées, y compris négatives.

### Contexte

Le géomètre communique la position d'un repère de nivellement par rapport à la borne de chantier.

### Énoncé

> Le repère se trouve à 30 m à l'est, 15 m au sud et 8 m au-dessus de la borne, laquelle est à l'origine du modèle. Placez ce repère dans le modèle à partir de trois valeurs réglables indépendantes.

### Ce qui vous est fourni

Canvas vide.

### Ce qui est attendu

Un point unique aux coordonnées (30 ; −15 ; 8).

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,01 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-02_sujet.gh`

### Barème

1 point si le point est à moins de 0,01 mm de la cible.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
