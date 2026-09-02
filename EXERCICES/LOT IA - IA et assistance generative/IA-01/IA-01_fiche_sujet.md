# IA-01 — Spécifier un composant plutôt que le décrire

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA1 · Formuler et cadrer une demande |
| **Référence au référentiel** | REF-117, REF-139 |
| **Compétence visée** | Rédiger la spécification d'un composant assez précise pour que le code obtenu soit juste du premier coup. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | A-08 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-01 Score visible |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Rédiger la spécification d'un composant assez précise pour que le code obtenu soit juste du premier coup.

### Contexte

Le contrôle de réception d'un lot de platines porte sur l'entraxe de perçage, nominal 250 mm, toléré à ± 1,5 mm.

### Énoncé

> Les 28 entraxes relevés vous sont fournis. Faites produire par un assistant un composant scripté qui renvoie le nombre de platines hors tolérance, et branchez sa sortie sur la réponse. Vous ne corrigerez pas le code à la main : si le résultat est faux, c'est la demande qu'il faut reprendre.

### Ce qui vous est fourni

Les 28 entraxes relevés, en millimètres, ainsi que l'entraxe nominal et la tolérance, chacun sur une entrée distincte.

### Ce qui est attendu

Un nombre entier : combien de platines sortent de la tolérance. Il doit sortir du composant produit par l'assistant, non d'un comptage à la main.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-01_sujet.gh`

### Barème

1 point si la sortie vaut 5 sans retouche manuelle du code.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
