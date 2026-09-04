# A-16 — Décaler et inverser une liste

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A3 · Listes |
| **Référence au référentiel** | REF-046 |
| **Compétence visée** | Relier chaque élément d'une liste au suivant en refermant la boucle, sans traiter le dernier cas à part. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-11 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-25 Animation de la solution |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Relier chaque élément d'une liste au suivant en refermant la boucle, sans traiter le dernier cas à part.

### Contexte

Un garde-corps polygonal doit être chiffré en longueur de lisse : il faut les segments entre montants, y compris celui qui referme le contour.

### Énoncé

> Huit montants sont disposés en octogone. Tracez les huit lisses qui relient chaque montant au suivant, la dernière revenant au premier, en n'employant qu'une seule fois le composant de tracé.

### Ce qui vous est fourni

Une liste de 8 points internalisée, disposés en cercle.

### Ce qui est attendu

Huit segments formant un contour fermé.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-16_sujet.gh`

### Barème

1 point si les 8 segments sont produits.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
