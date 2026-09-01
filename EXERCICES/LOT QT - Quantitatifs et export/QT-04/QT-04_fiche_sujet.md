# QT-04 — Un débit qui devient une commande

**Fiche d'exercice Magpie** · Lot QT — Quantitatifs, chiffrage et export

| | |
|---|---|
| **Thématique** | QT3 · Export de données |
| **Référence au référentiel** | REF-085 |
| **Compétence visée** | Regrouper un relevé ligne à ligne en une table par référence, de sorte que chaque référence n'apparaisse qu'une fois avec sa quantité cumulée. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | QT-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-11 Commande à passer |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Regrouper un relevé ligne à ligne en une table par référence, de sorte que chaque référence n'apparaisse qu'une fois avec sa quantité cumulée.

### Contexte

Le débit sort de l'atelier ligne par ligne, dans l'ordre du montage. Le fournisseur, lui, veut une commande : une ligne par référence, et la quantité totale.

### Énoncé

> Le débit vous est fourni tel qu'il sort de l'atelier : vingt-quatre lignes, dans le désordre, où la même référence revient plusieurs fois. Donnez la quantité totale de la référence la plus commandée.

### Ce qui vous est fourni

Les vingt-quatre lignes du débit : une référence de panneau et une quantité par ligne.

### Ce qui est attendu

17 — la quantité cumulée de la référence la plus commandée.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`QT-04_sujet.gh`

### Barème

1 point si la quantité cumulée est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
