# B-18 — Filetage hélicoïdal paramétrique

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B5 · Design produit |
| **Référence au référentiel** | REF-069, REF-103 |
| **Compétence visée** | Retrouver une cote fonctionnelle à partir d'une norme, plutôt que de la mesurer sur un modèle. |
| **Case Bloom (révisée)** | Appliquer × conceptuelle |
| **Niveau** | Intermédiaire |
| **Durée cible** | 28 min |
| **Prérequis** | A-42 |
| **Mode de validation** | NumericTolerance — tolérance 0.001 |
| **Solution de référence** | 22 composants |
| **Gamification associée** | G-32 Indices payants |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Construire une hélice et balayer un profil normalisé le long de celle-ci.

### Contexte

Le diamètre à fond de filet décide de la section résistante de la vis. Il ne se lit pas sur la désignation.

### Énoncé

> Modélise une vis M10 au pas de 1,5 mm sur 30 mm de longueur filetée, profil triangulaire à 60°, et vérifie que le diamètre à fond de filet correspond bien à la valeur normalisée de 8,376 mm.

### Ce qui vous est fourni

Trois sliders : diamètre nominal, pas, longueur filetée.

### Ce qui est attendu

8,16 mm — le diamètre à fond de filet, à 0,001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-18_sujet.gh`

### Barème

2 points pour le filetage, 2 points pour la vérification dimensionnelle.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
