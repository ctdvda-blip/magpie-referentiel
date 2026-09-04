# A-09 — Valeur nulle et propagation

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A2 · Types et conversion implicite |
| **Référence au référentiel** | REF-055 |
| **Compétence visée** | Écarter les valeurs manquantes d'un relevé et dénombrer ce qui reste exploitable. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-07 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-16 Chasse au trésor sur le canvas |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Écarter les valeurs manquantes d'un relevé et dénombrer ce qui reste exploitable.

### Contexte

Un relevé de hauteurs d'allège importé d'un tableur comporte des cellules restées vides.

### Énoncé

> Le relevé porte sur 24 baies, mais certaines lignes n'ont pas été renseignées. Indiquez combien de hauteurs sont réellement exploitables.

### Ce qui vous est fourni

Le relevé des 24 baies, cellules non renseignées comprises.

### Ce qui est attendu

Un nombre entier : combien de hauteurs sont réellement renseignées.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-09_sujet.gh`

### Barème

1 point si le Panel affiche 6.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
