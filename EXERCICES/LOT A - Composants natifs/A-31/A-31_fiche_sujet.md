# A-31 — Orienter un flux avec une condition

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A7 · Portes logiques |
| **Référence au référentiel** | REF-061 |
| **Compétence visée** | Orienter un flux vers l'une ou l'autre de deux sorties selon une condition, sans démonter le montage. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-30 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-24 Sons et retours audio |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Orienter un flux vers l'une ou l'autre de deux sorties selon une condition, sans démonter le montage.

### Contexte

Deux variantes de remplissage sont à l'étude ; le client veut les voir alternativement sans qu'on retouche la définition devant lui.

### Énoncé

> Les deux variantes de remplissage sont montées et fonctionnent. Faites en sorte qu'un seul interrupteur bascule l'affichage de l'une à l'autre, sans supprimer ni débrancher aucun composant.

### Ce qui vous est fourni

Un Circle, un Rectangle et un Boolean Toggle.

### Ce qui est attendu

Une seule géométrie affichée à la fois, commandée par l'interrupteur.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-31_sujet.gh`

### Barème

1 point si l'alternance fonctionne dans les deux sens.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
