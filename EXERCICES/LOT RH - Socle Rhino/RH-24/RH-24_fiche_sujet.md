# RH-24 — Les parois trop minces après mise à l'échelle

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH5 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-016, REF-017, REF-018 |
| **Compétence visée** | Confronter un relevé d'épaisseurs à la contrainte machine APRÈS mise à l'échelle, et non avant. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | RH-10 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-26 Le retour visuel immédiat |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Confronter un relevé d'épaisseurs à la contrainte machine APRÈS mise à l'échelle, et non avant.

### Contexte

Une maquette se réduit pour tenir dans le volume d'impression. Les parois se réduisent avec elle, et celles qui passaient au 1/1 ne passent plus.

### Énoncé

> Le relevé donne dix-huit épaisseurs de paroi, en centièmes de millimètre. La pièce sera imprimée à 62 % de sa taille, et la machine ne tient pas sous 1,20 mm. Donnez le nombre de parois qui ne passeront pas.

### Ce qui vous est fourni

Les dix-huit épaisseurs relevées, le facteur d'échelle et le minimum machine.

### Ce qui est attendu

12 parois passent sous le minimum après réduction.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-24_sujet.gh`

### Barème

1 point si le compte est exact.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
