# A-42 — Balayage et révolution

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A10 · Surfaces et solides |
| **Référence au référentiel** | REF-069 |
| **Compétence visée** | Engendrer une surface par déplacement d'un profil le long d'un guide, et par rotation autour d'un axe. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-41 |
| **Mode de validation** | GeometryTolerance — tolérance 0,5 mm |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-05 Badges et trophées |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Engendrer une surface par déplacement d'un profil le long d'un guide, et par rotation autour d'un axe.

### Contexte

Une main courante tubulaire suit un limon ; un fût de colonne est engendré par rotation de son profil.

### Énoncé

> Le profil circulaire et son guide vous sont fournis, ainsi qu'un profil plan. Engendrez le tube en promenant le profil circulaire le long du guide, puis le fût en faisant tourner le profil plan autour de l'axe vertical.

### Ce qui vous est fourni

Un profil circulaire, une courbe guide et un profil plan internalisés.

### Ce qui est attendu

Un tube et une surface de révolution.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,5 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-42_sujet.gh`

### Barème

1 point par surface correcte.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
