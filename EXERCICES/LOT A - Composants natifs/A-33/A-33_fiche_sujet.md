# A-33 — Plans de construction

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A8 · Géométrie vectorielle et filaire |
| **Référence au référentiel** | REF-062 |
| **Compétence visée** | Poser un repère orienté et y construire une géométrie. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-32 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-07 Étoiles de performance |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Poser un repère orienté et y construire une géométrie.

### Contexte

Une buse traverse un mur en biais : son tracé se pose dans un plan incliné, pas dans le plan horizontal.

### Énoncé

> Le percement est circulaire, de 20 de rayon, centré à 50 au-dessus de l'origine, et son plan est incliné de 30° autour de l'axe X. Construisez ce tracé.

### Ce qui vous est fourni

Canvas vide.

### Ce qui est attendu

Un cercle de rayon 20 dans le plan incliné demandé.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-33_sujet.gh`

### Barème

1 point si le cercle respecte position et inclinaison.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
