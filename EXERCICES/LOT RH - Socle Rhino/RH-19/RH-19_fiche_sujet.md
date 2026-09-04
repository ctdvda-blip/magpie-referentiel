# RH-19 — Ce que la mise à l'échelle fait aux détails

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-017, REF-018 |
| **Compétence visée** | Juger la finesse d'un modèle À L'ÉCHELLE OÙ IL SERA IMPRIMÉ, et non à celle où il a été dessiné. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 25 min |
| **Prérequis** | RH-07 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Juger la finesse d'un modèle à l'échelle où il sera imprimé, et non à celle où il a été dessiné.

### Contexte

La maquette d'étude est dessinée au 1:25 et sera imprimée à l'échelle 1. La machine ne distingue rien sous 0,4 mm.

### Énoncé

> Les douze détails les plus fins du modèle vous sont fournis, mesurés sur la maquette. Le modèle sera agrandi 25 fois. Donnez le nombre de détails qui resteront sous la résolution de 0,4 mm APRÈS agrandissement.

### Ce qui vous est fourni

Les douze dimensions relevées sur la maquette, le facteur d'agrandissement et la résolution de la machine.

### Ce qui est attendu

6 détails restent sous la résolution après agrandissement.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-19_sujet.gh`

### Barème

1 point si le compte après agrandissement est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
