# GP-05 — La chaîne de cotes d'une façade

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP3 · Plan paramétrique |
| **Référence au référentiel** | REF-065, REF-066 |
| **Compétence visée** | Produire une cotation en chaîne qui se recalcule avec le modèle, en distinguant ce qui se mesure d'un voisin à l'autre de ce qui se repère depuis une origine unique. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | GP-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-08 Relevé contradictoire |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire une cotation en chaîne qui se recalcule avec le modèle, en distinguant ce qui se mesure d'un voisin à l'autre de ce qui se repère depuis une origine unique.

### Contexte

Le poseur implante les percements d'une façade au décamètre, depuis un unique point de référence : c'est la seule manière de ne pas cumuler les erreurs de report.

### Énoncé

> Le bureau d'études fournit les entraxes des sept percements, mesurés chacun depuis le précédent, et la distance du premier au point de référence. Donnez la cote du dernier percement telle qu'elle doit figurer au plan de pose, en millimètres.

### Ce qui vous est fourni

La distance du premier percement au point de référence, et les sept entraxes successifs, en millimètres.

### Ce qui est attendu

8 955 mm — la position du dernier percement, comptée depuis le point de référence.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-05_sujet.gh`

### Barème

1 point si la cote finale est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
