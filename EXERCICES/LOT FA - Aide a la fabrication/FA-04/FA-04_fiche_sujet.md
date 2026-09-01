# FA-04 — Combien de pièces par fournée

**Fiche d'exercice Magpie** · Lot FA — Aide à la fabrication

| | |
|---|---|
| **Thématique** | FA1 · Imbrication |
| **Référence au référentiel** | REF-114 |
| **Compétence visée** | Estimer le remplissage d'un volume de fabrication en raisonnant par encombrement, et non par volume de matière. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | FA-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 10 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Estimer le remplissage d'un volume de fabrication en raisonnant par encombrement, et non par volume de matière.

### Contexte

La machine de fabrication additive facture à la fournée, pas à la pièce : le prix unitaire dépend entièrement du nombre de pièces qu'on fait tenir dans le volume de construction.

### Énoncé

> Le volume de construction mesure 250 × 210 × 210 mm. La pièce tient dans un encombrement de 62 × 38 × 95 mm et ne peut pas être réorientée. Il faut 4 mm entre deux pièces et 4 mm entre une pièce et chaque paroi. Donnez le nombre de pièces par fournée.

### Ce qui vous est fourni

Les dimensions du volume de construction, l'encombrement de la pièce et l'écart minimal à respecter.

### Ce qui est attendu

24 — soit 3 pièces en longueur, 4 en largeur et 2 en hauteur.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`FA-04_sujet.gh`

### Barème

1 point si le nombre de pièces est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
