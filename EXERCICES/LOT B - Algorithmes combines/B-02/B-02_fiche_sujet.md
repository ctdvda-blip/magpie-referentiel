# B-02 — Garde-corps à barreaudage régulier

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B1 · Architecture et construction |
| **Référence au référentiel** | REF-064, REF-047, REF-043 |
| **Compétence visée** | Répartir des éléments sous une contrainte d'espacement LIBRE, en distinguant l'entraxe de l'espace entre matières. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | A-35, A-12 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 14 composants |
| **Gamification associée** | G-07 Étoiles de performance |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Répartir des éléments à pas maximal imposé, cas classique de calcul d'entraxe.

### Contexte

L'espacement libre d'un garde-corps est une règle de sécurité : c'est le vide qui est mesuré, pas la distance d'axe en axe.

### Énoncé

> Sur la main courante fournie, place des barreaux verticaux de 16 mm de diamètre. L'espacement libre entre barreaux ne doit jamais dépasser 110 mm. Détermine le nombre de barreaux et affiche l'entraxe réel.

### Ce qui vous est fourni

Une courbe de main courante et une hauteur de garde-corps internalisées.

### Ce qui est attendu

25 barreaux, pour un espacement libre de 108 mm.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-02_sujet.gh`

### Barème

2 points pour le barreaudage, 1 point pour le respect strict des 110 mm.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
