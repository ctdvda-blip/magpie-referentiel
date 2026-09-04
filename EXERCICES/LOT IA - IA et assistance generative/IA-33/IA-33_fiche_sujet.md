# IA-33 — Du texte aux paramètres

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA6 · Modèles de langage et IA générative |
| **Référence au référentiel** | REF-134 |
| **Compétence visée** | Tirer d'un texte de programme les paramètres qui pilotent une définition, en distinguant ce qui est donné de ce qui se déduit. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 18 min |
| **Prérequis** | IA-11 |
| **Mode de validation** | NumericTolerance — tolérance 0.0001 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-19 Le composant mystère |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Tirer d'un texte de programme les paramètres qui pilotent une définition, en distinguant ce qui est donné de ce qui se déduit.

### Contexte

Un cahier des charges décrit une verrière en toutes lettres. La définition, elle, a besoin d'une largeur de travée et d'une hauteur vitrée, qu'aucune phrase ne donne directement.

### Énoncé

> L'extrait décrit une verrière de 3 200 mm de large et 2 450 mm de haut, à 6 travées égales séparées par des montants de 60 mm, avec une imposte de 380 mm en partie haute. Donnez la largeur d'une travée puis la hauteur vitrée, en millimètres.

### Ce qui vous est fourni

L'extrait de programme, en toutes lettres.

### Ce qui est attendu

483,3333 mm de largeur de travée, puis 2 070 mm de hauteur vitrée.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-33_sujet.gh`

### Barème

1 point si les deux valeurs sont justes à 0,0001 mm.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
