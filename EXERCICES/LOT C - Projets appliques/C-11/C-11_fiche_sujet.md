# C-11 — Déroulé de tôle pliée avec compensation

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C4 · Fabrication |
| **Référence au référentiel** | REF-116, REF-115, REF-082 |
| **Compétence visée** | Calculer le développé d'une tôle à plis multiples, en comptant le bon nombre de plis par segment. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 80 min |
| **Prérequis** | B-17, C-05 |
| **Mode de validation** | NumericTolerance — tolérance 0.1 |
| **Solution de référence** | 40 composants |
| **Gamification associée** | G-20 Erreur à débusquer + G-03 Compte à rebours |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Calculer un développé industriel exact et produire le plan de pliage.

### Contexte

La bande part au débit avant pliage. Cinq plis, c'est cinq occasions de se tromper d'un rayon.

### Énoncé

> La pièce en tôle de 2 mm comporte 5 plis à 90° de rayon intérieur 3 mm. Produis son développé en tenant compte du facteur K de 0,44, cote les lignes de pli et vérifie que la longueur développée calculée correspond à la longueur mesurée sur le développé.

### Ce qui vous est fourni

Une pièce en tôle pliée internalisée et les paramètres matière.

### Ce qui est attendu

500,47 mm de développé, à 0,1 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-11_sujet.gh`

### Barème

4 points développé, 3 points compensation, 3 points cotation.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
