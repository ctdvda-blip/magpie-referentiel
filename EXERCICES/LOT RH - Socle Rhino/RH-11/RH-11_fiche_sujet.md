# RH-11 — Ce que le zoom étendue vous apprend

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH1 · Interface et navigation Rhino |
| **Référence au référentiel** | REF-001, REF-002, REF-003 |
| **Compétence visée** | Diagnostiquer l'étendue réelle d'un fichier au lieu de juger sur ce que l'écran montre. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | RH-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-02 Diagnostic éclair |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Diagnostiquer l'étendue réelle d'un fichier au lieu de juger sur ce que l'écran montre.

### Contexte

Le fichier arrive du géomètre. Un zoom étendue et l'on ne voit plus rien : le bâtiment est devenu un point.

### Énoncé

> Le fichier contient cinquante objets, dont les coordonnées vous sont fournies. Donnez l'étendue du fichier selon X, en mètres.

### Ce qui vous est fourni

Les coordonnées en plan des cinquante objets, en millimètres.

### Ce qui est attendu

6 050 m — l'étendue selon X de tout ce que le fichier contient.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-11_sujet.gh`

### Barème

1 point si l'étendue est juste, en mètres.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
