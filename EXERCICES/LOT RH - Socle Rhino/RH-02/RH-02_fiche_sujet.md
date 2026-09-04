# RH-02 — Reprendre une implantation par son calque

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Organisation du document |
| **Référence au référentiel** | REF-004, REF-006, REF-014 |
| **Compétence visée** | Organiser un document Rhino par calques de sorte qu'une définition puisse en reprendre une partie sans sélection manuelle. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | A-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Organiser un document Rhino par calques de sorte qu'une définition puisse en reprendre une partie sans sélection manuelle.

### Contexte

Le géomètre livre l'implantation d'un plancher : poteaux porteurs et cloisons sont mélangés sur un même calque, alors que seuls les porteurs entrent dans la descente de charges.

### Énoncé

> Le fichier fourni contient 18 points d'implantation sur un calque unique. Séparez les 12 porteurs des 6 cloisons sur deux calques distincts, puis faites compter les porteurs par la définition — sans les désigner un par un.

### Ce qui vous est fourni

Un fichier Rhino contenant les 18 points sur le calque « IMPLANTATION », et une définition prête à référencer un calque.

### Ce qui est attendu

Un nombre entier : combien de points portent le calque des porteurs, une fois le tri fait.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-02_sujet.gh`

### Barème

1 point si le compte vaut 12 et si aucun point n'a été désigné individuellement.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
