# A-41 — Extrusion et surface réglée

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A10 · Surfaces et solides |
| **Référence au référentiel** | REF-069 |
| **Compétence visée** | Passer d'une courbe à une surface par extrusion et par transition entre profils. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-34 |
| **Mode de validation** | GeometryTolerance — tolérance 0,5 mm |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-27 Narration Serengeti |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Passer d'une courbe à une surface par extrusion et par transition entre profils.

### Contexte

Une trémie relie deux sections différentes ; un conduit droit relie deux sections identiques.

### Énoncé

> Deux profils fermés superposés vous sont fournis. Produisez la surface de transition qui les relie, puis, séparément, la surface obtenue en poussant le profil du bas de 200 mm vers le haut. Comparez les deux.

### Ce qui vous est fourni

Deux profils fermés internalisés à 0 et 300 mm.

### Ce qui est attendu

Une surface de transition et une surface d'extrusion.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,5 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-41_sujet.gh`

### Barème

1 point par surface correcte.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
