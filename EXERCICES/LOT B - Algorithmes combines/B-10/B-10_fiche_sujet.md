# B-10 — Motif gravé développé sur un anneau

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B3 · Joaillerie |
| **Référence au référentiel** | REF-115, REF-069, REF-049 |
| **Compétence visée** | Répartir un motif répétitif sur un développé, en distinguant la circonférence du diamètre. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | B-04, A-42 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 24 composants |
| **Gamification associée** | G-09 Récompense cachée |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Concevoir un motif à plat puis l'enrouler sur une surface de révolution.

### Contexte

Le motif doit se refermer sur lui-même. Un raccord faux se voit immédiatement, et se voit toujours au même endroit.

### Énoncé

> Dessine à plat un motif géométrique répétitif de 12 modules, puis applique-le sur la face extérieure d'un anneau de taille 54 et de 4 mm de large. Le motif doit boucler sans rupture.

### Ce qui vous est fourni

Un anneau de révolution internalisé et un module de motif plan.

### Ce qui est attendu

4,50 mm — la largeur d'un module, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-10_sujet.gh`

### Barème

2 points pour le motif, 2 points pour la continuité du raccord.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
