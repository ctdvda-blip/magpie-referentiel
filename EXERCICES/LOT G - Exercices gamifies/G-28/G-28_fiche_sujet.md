# G-28 — L'avatar paramétrique

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G6 · Sensations et immersion |
| **Référence au référentiel** | REF-067, REF-106, REF-061 |
| **Compétence visée** | Concevoir un codage qui reste valide sur TOUTES les combinaisons, et le prouver en les parcourant. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 22 min |
| **Prérequis** | B-16, A-31 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 20 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire construire à l'apprenant un objet personnel qu'il retrouvera tout au long du parcours.

### Contexte

L'avatar est un objet que l'apprenant retrouve tout au long du parcours. Il n'a de valeur que s'il ne casse jamais — d'où l'exigence de robustesse sur les soixante-douze combinaisons.

### Énoncé

> Compose ton avatar : 3 formes de corps, 4 motifs, 6 couleurs. Ton avatar doit rester valide dans les 72 combinaisons possibles et son code de configuration doit s'afficher dans le Panel.

### Ce qui vous est fourni

Trois Value List et les bibliothèques de formes et de motifs.

### Ce qui est attendu

16 452 — la somme des soixante-douze codes de configuration.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-28_sujet.gh`

### Barème

2 points : 1 pour la robustesse, 1 pour le code de configuration.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
