# FA-03 — Le développé d'un profil plié

**Fiche d'exercice Magpie** · Lot FA — Aide à la fabrication

| | |
|---|---|
| **Thématique** | FA2 · Déroulé et mise à plat |
| **Référence au référentiel** | REF-116 |
| **Compétence visée** | Calculer la longueur développée d'une tôle pliée en tenant compte de l'allongement de la matière au droit des plis. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 35 min |
| **Prérequis** | FA-02 |
| **Mode de validation** | NumericTolerance — tolérance 0.1 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Calculer la longueur développée d'une tôle pliée en tenant compte de l'allongement de la matière au droit des plis.

### Contexte

Le profil en U part au débit avant pliage : la bande découpée doit avoir exactement la longueur qui, une fois pliée, donnera les cotes du plan.

### Énoncé

> Le profil en U mesure 120 mm d'aile, 300 mm d'âme, cotes extérieures, dans une tôle de 3 mm. Les deux plis à 90° se font sur un rayon intérieur de 5 mm, avec un facteur K de 0,42. Donnez la longueur de la bande à débiter, en millimètres.

### Ce qui vous est fourni

Les cotes extérieures du profil, l'épaisseur de la tôle, le rayon intérieur de pliage et le facteur K.

### Ce qui est attendu

527,67 mm — la longueur développée, à 0,1 mm près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`FA-03_sujet.gh`

### Barème

1 point si le développé est juste à 0,1 mm près.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
