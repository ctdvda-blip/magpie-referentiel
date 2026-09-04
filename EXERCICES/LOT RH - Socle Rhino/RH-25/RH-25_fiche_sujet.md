# RH-25 — Les volumes réellement étanches

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH4 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-019, REF-020, REF-021 |
| **Compétence visée** | Établir l'étanchéité d'une polysurface en tenant compte des arêtes non-manifold autant que des arêtes nues. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 14 min |
| **Prérequis** | RH-08 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-20 La chasse aux bugs |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir l'étanchéité d'une polysurface en tenant compte des arêtes non-manifold autant que des arêtes nues.

### Contexte

Un solide qui n'est pas étanche ne s'imprime pas. Le diagnostic se lit sur deux compteurs, et le second est régulièrement ignoré.

### Énoncé

> Le rapport d'analyse donne, pour douze polysurfaces, le nombre d'arêtes nues et le nombre d'arêtes non-manifold. Donnez le nombre de polysurfaces réellement étanches.

### Ce qui vous est fourni

Le rapport des douze polysurfaces et de leurs deux compteurs.

### Ce qui est attendu

6 polysurfaces sur 12 sont réellement étanches.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-25_sujet.gh`

### Barème

1 point si le compte est exact.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
