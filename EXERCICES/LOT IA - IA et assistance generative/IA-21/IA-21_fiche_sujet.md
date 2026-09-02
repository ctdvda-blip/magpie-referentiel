# IA-21 — Le script qui compte les intervalles

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA2 · Composants scriptés assistés |
| **Référence au référentiel** | REF-121 |
| **Compétence visée** | Relire un script produit par un assistant en confrontant ce qu'il compte à ce que la tâche demande. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | IA-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-15 Relecture de code |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Relire un script produit par un assistant en confrontant ce qu'il compte à ce que la tâche demande.

### Contexte

La clôture fait 18,60 m et les poteaux ne doivent pas être espacés de plus de 2,50 m. Le script généré rend un nombre, et il paraît raisonnable.

### Énoncé

> La file mesure 18 600 mm et l'entraxe ne doit pas dépasser 2 500 mm. Donnez le nombre de poteaux.

### Ce qui vous est fourni

La longueur de la file et l'entraxe maximal admis.

### Ce qui est attendu

9 poteaux — huit travées de 2 325 mm.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-21_sujet.gh`

### Barème

1 point si le nombre de poteaux est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
