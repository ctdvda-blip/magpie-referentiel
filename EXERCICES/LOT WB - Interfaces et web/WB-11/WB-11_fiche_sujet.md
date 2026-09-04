# WB-11 — Le temps de calcul, une fois en ligne

**Fiche d'exercice Magpie** · Lot WB — Interfaces, web et interopérabilité

| | |
|---|---|
| **Thématique** | WB2 · Publication web |
| **Référence au référentiel** | REF-108, REF-109, REF-110 |
| **Compétence visée** | Estimer le temps de réponse d'une définition publiée en ligne, en tenant compte de l'écart entre le poste et le serveur. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 16 min |
| **Prérequis** | WB-06 |
| **Mode de validation** | NumericTolerance — tolérance 0.0001 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-03 Contre la montre |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Estimer le temps de réponse d'une définition publiée en ligne, en tenant compte de l'écart entre le poste et le serveur.

### Contexte

Un configurateur publié doit répondre en quelques secondes. Ce qui tourne en dix secondes sur le poste du concepteur peut dépasser la limite du service une fois en ligne.

### Énoncé

> Le profilage donne le temps de recalcul des vingt-quatre composants sur votre poste, en millisecondes. Le serveur est 2,4 fois plus lent. Donnez le temps de réponse en ligne, en secondes.

### Ce qui vous est fourni

Le relevé des vingt-quatre temps et le facteur serveur.

### Ce qui est attendu

25,1736 s de temps de réponse en ligne, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`WB-11_sujet.gh`

### Barème

1 point si le temps est juste à 0,0001 s.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
