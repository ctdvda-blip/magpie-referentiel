# A-45 — Intersections entre géométries

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A10 · Surfaces et solides |
| **Référence au référentiel** | REF-071 |
| **Compétence visée** | Extraire le contour d'intersection entre un solide et un plan, et le mesurer. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-44 |
| **Mode de validation** | NumericTolerance — tolérance 0,5 % |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-16 Chasse au trésor |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Extraire le contour d'intersection entre un solide et un plan, et le mesurer.

### Contexte

Une coupe horizontale à mi-hauteur sert à chiffrer le linéaire de joint périphérique.

### Énoncé

> Le solide vous est fourni. Établissez son contour de coupe à mi-hauteur et donnez le linéaire total de ce contour.

### Ce qui vous est fourni

Un solide internalisé.

### Ce qui est attendu

Le contour de coupe et son linéaire total.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,5 %.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-45_sujet.gh`

### Barème

1 point pour le contour, 1 point pour la longueur.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
