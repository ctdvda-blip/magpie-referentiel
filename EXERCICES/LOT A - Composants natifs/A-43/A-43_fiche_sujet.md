# A-43 — Fermer une polysurface en solide

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A10 · Surfaces et solides |
| **Référence au référentiel** | REF-070 |
| **Compétence visée** | Refermer une enveloppe ouverte et établir qu'elle constitue bien un solide. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-41 |
| **Mode de validation** | NumericTolerance — tolérance 1 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-20 Erreur volontaire à débusquer |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Refermer une enveloppe ouverte et établir qu'elle constitue bien un solide.

### Contexte

Un caisson doit être étanche avant d'être chiffré en volume de remplissage ; une enveloppe ouverte n'a pas de volume.

### Énoncé

> L'enveloppe fournie présente deux ouvertures. Refermez-la, puis établissez par une valeur numérique qu'elle est désormais un solide.

### Ce qui vous est fourni

Une polysurface ouverte internalisée.

### Ce qui est attendu

Le volume du solide refermé, non nul — c'est lui qui prouve la fermeture : une enveloppe ouverte n'a pas de volume.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-43_sujet.gh`

### Barème

1 point si le solide est fermé et prouvé.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
