# C-03 — Gradins avec contrôle de visibilité

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C1 · Architecture |
| **Référence au référentiel** | REF-047, REF-079, REF-046, REF-060 |
| **Compétence visée** | Construire une progression dont chaque terme dépend du précédent ET de sa position, et en tirer une cote de projet. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Expérimenté |
| **Durée cible** | 80 min |
| **Prérequis** | B-01, B-08 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 35 composants |
| **Gamification associée** | G-02 Barre de progression + G-20 Erreur à débusquer |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Construire une géométrie pilotée par une contrainte de performance vérifiée rang par rang.

### Contexte

Le dégagement visuel est une règle de sécurité et de confort. Il se vérifie rang par rang, et la hauteur du dernier décide de tout le volume construit.

### Énoncé

> Modélise 18 rangs de gradins de 850 mm de profondeur. La ligne de visée de chaque spectateur vers le point focal doit passer au moins 90 mm au-dessus de la tête du spectateur du rang précédent. Détermine automatiquement la hauteur de chaque marche et signale tout rang non conforme.

### Ce qui vous est fourni

Le point focal, la profondeur de rang et le nombre de rangs.

### Ce qui est attendu

3 105,01 mm — la hauteur du dernier rang, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-03_sujet.gh`

### Barème

4 points géométrie, 3 points calcul cumulatif, 3 points contrôle.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
