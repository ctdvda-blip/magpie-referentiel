# A-20 — Graft et Flatten

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A4 · Arbres de données |
| **Référence au référentiel** | REF-049, REF-052 |
| **Compétence visée** | Modifier la structure d'un flux pour obtenir un croisement complet plutôt qu'un appariement terme à terme. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-19 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-22 Boss de fin de chapitre |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Modifier la structure d'un flux pour obtenir un croisement complet plutôt qu'un appariement terme à terme.

### Contexte

Une passerelle est haubanée : chaque ancrage de rive doit être relié à chaque ancrage de mât, et non au seul ancrage de même rang.

### Énoncé

> Trois ancrages de rive et trois ancrages de mât vous sont fournis. Le tracé livre aujourd'hui trois haubans, un par paire de même rang. Obtenez les neuf haubans de toutes les combinaisons possibles, sans dupliquer le composant de tracé.

### Ce qui vous est fourni

Deux listes de 3 points internalisées, reliées par un Line.

### Ce qui est attendu

Neuf segments.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-20_sujet.gh`

### Barème

1 point si 9 segments sont produits.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
