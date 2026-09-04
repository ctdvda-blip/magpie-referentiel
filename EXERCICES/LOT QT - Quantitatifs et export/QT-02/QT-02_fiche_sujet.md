# QT-02 — Du métré au prix

**Fiche d'exercice Magpie** · Lot QT — Quantitatifs, chiffrage et export

| | |
|---|---|
| **Thématique** | QT1 · Quantitatifs et chiffrage |
| **Référence au référentiel** | REF-083 |
| **Compétence visée** | Croiser un métré avec un bordereau de prix pour obtenir un montant, sans apparier les mauvaises lignes. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | QT-01 |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Croiser un métré avec un bordereau de prix pour obtenir un montant, sans apparier les mauvaises lignes.

### Contexte

Le bordereau du fournisseur donne un prix au mètre linéaire par section ; le métré donne des longueurs par solive.

### Énoncé

> Le bordereau fournit un prix au mètre linéaire pour chacune des cinq sections. Donnez le montant total du plancher, en euros.

### Ce qui vous est fourni

Les 20 solives avec leur section et leur longueur, et le bordereau des cinq prix unitaires par section.

### Ce qui est attendu

Le montant total, en euros, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`QT-02_sujet.gh`

### Barème

1 point si le montant est juste à 0,01 € près.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
