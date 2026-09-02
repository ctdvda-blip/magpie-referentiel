# G-26 — Le retour visuel immédiat

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G6 · Sensations et immersion |
| **Référence au référentiel** | REF-026, REF-059 |
| **Compétence visée** | Comparer une série de mesures à un intervalle de tolérance et compter les écarts, des deux côtés. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | A-29 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 12 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Colorer le résultat en fonction de sa conformité, pour un diagnostic instantané.

### Contexte

La coloration conditionnelle est le contrôle qualité du modeleur : elle dit d'un coup d'œil ce qu'un tableau de vingt lignes met une minute à dire.

### Énoncé

> Vingt pièces doivent mesurer entre 400 et 900 mm. Colore en vert celles qui sont conformes, en rouge les autres, et affiche le nombre de non-conformes.

### Ce qui vous est fourni

Vingt pièces internalisées de longueurs variées.

### Ce qui est attendu

8 pièces non conformes.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-26_sujet.gh`

### Barème

2 points : 1 pour la coloration, 1 pour le compte.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
