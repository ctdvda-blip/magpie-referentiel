# AV-04 — Ce qui met fin à la boucle

**Fiche d'exercice Magpie** · Lot AV — Algorithmique avancée

| | |
|---|---|
| **Thématique** | AV1 · Boucles et itération |
| **Référence au référentiel** | REF-151 |
| **Compétence visée** | Déterminer le nombre de passages qu'exige un critère d'arrêt, et savoir que c'est LUI qui commande la sortie. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | AV-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-13 Chronomètre |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Déterminer le nombre de passages qu'exige un critère d'arrêt, et savoir que c'est lui qui commande la sortie.

### Contexte

Le tassement du remblai décroît de 15 % à chaque passe de compactage. On s'arrête quand il descend sous 5 mm.

### Énoncé

> Le tassement initial vaut 48 mm et chaque passe le réduit de 15 %. Donnez le nombre de passes nécessaires pour descendre sous 5 mm.

### Ce qui vous est fourni

Le tassement initial, le facteur de décroissance et le seuil.

### Ce qui est attendu

14 passes — la treizième laisse encore 5,80 mm.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`AV-04_sujet.gh`

### Barème

1 point si le nombre de passes est juste et arrondi au supérieur.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
