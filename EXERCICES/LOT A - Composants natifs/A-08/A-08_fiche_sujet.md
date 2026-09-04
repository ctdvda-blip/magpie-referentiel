# A-08 — Booléen et nombre

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A2 · Types et conversion implicite |
| **Référence au référentiel** | REF-040, REF-059 |
| **Compétence visée** | Dénombrer les éléments d'un lot qui satisfont une condition, en exploitant l'équivalence entre vrai et 1. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | A-06 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-01 Score visible |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Dénombrer les éléments d'un lot qui satisfont une condition, en exploitant l'équivalence entre vrai et 1.

### Contexte

Le contrôle de réception d'un lot de traverses porte sur une cote nominale de 1 200 mm, avec une tolérance de ± 5 mm.

### Énoncé

> Les cotes relevées sur les 28 traverses du lot vous sont fournies. Comptez combien de traverses sortent de la tolérance, sans écarter aucun élément de la liste.

### Ce qui vous est fourni

Les 28 cotes relevées sur le lot, en millimètres, ainsi que la cote nominale de 1 200 mm et la tolérance de 5 mm.

### Ce qui est attendu

Un nombre entier : combien de traverses sortent de la tolérance.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-08_sujet.gh`

### Barème

1 point si le compte est exact.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
