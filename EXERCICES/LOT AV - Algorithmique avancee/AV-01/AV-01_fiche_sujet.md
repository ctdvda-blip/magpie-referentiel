# AV-01 — Converger vers une portée

**Fiche d'exercice Magpie** · Lot AV — Algorithmique avancée

| | |
|---|---|
| **Thématique** | AV1 · Boucles et itération |
| **Référence au référentiel** | REF-093 |
| **Compétence visée** | Faire converger un calcul par itérations successives jusqu'à un critère d'arrêt. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 35 min |
| **Prérequis** | A-30 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire converger un calcul par itérations successives jusqu'à un critère d'arrêt.

### Contexte

La flèche d'une poutre dépend de sa portée d'une façon qui ne s'inverse pas simplement : on cherche la portée qui donne la flèche admissible.

### Énoncé

> La flèche admissible est atteinte pour une portée comprise entre 1 000 et 4 000 mm. Approchez cette portée par bissection jusqu'à ce que l'intervalle passe sous 1 mm, et donnez le nombre d'itérations nécessaires.

### Ce qui vous est fourni

La fonction de flèche, l'intervalle de départ et le critère d'arrêt.

### Ce qui est attendu

Un nombre entier : combien de bissections ont été nécessaires pour atteindre le critère.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`AV-01_sujet.gh`

### Barème

1 point si le nombre d'itérations vaut 12 et si la sortie se fait sur le critère, non sur un compte.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
