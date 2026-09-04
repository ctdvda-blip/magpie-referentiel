# RH-18 — Les parois que la machine ne saura pas faire

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH4 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-016 |
| **Compétence visée** | Confronter une pièce aux contraintes de la machine avant de lancer une impression. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-08 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Confronter une pièce aux contraintes de la machine avant de lancer une impression.

### Contexte

La machine ne descend pas sous 1,2 mm de paroi. En deçà, elle imprime quelque chose — qui casse à la première manipulation.

### Énoncé

> Les quatorze épaisseurs de paroi relevées sur la pièce vous sont fournies. Donnez le nombre de parois strictement inférieures au minimum imprimable de 1,2 mm.

### Ce qui vous est fourni

Les quatorze épaisseurs relevées, en millimètres, et le minimum imprimable.

### Ce qui est attendu

5 parois passent sous le minimum.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-18_sujet.gh`

### Barème

1 point si le compte est juste et strict.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
