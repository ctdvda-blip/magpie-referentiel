# IA-31 — Ce que l'agent a modifié

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA6 · Agents et protocoles |
| **Référence au référentiel** | REF-136, REF-137, REF-138 |
| **Compétence visée** | Distinguer, dans le journal d'un agent, les opérations qui ont modifié le document de celles qui l'ont seulement lu. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 16 min |
| **Prérequis** | IA-12 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-16 La chasse au trésor |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Distinguer, dans le journal d'un agent, les opérations qui ont modifié le document de celles qui l'ont seulement lu.

### Contexte

Avant de laisser un agent travailler sur une définition, on veut savoir ce qu'il a touché. Le journal le dit, à condition de trier les lectures des écritures.

### Énoncé

> Le journal donne les vingt-deux opérations menées par l'agent. Donnez le nombre d'opérations qui ont MODIFIÉ le document.

### Ce qui vous est fourni

Le journal des vingt-deux opérations.

### Ce qui est attendu

10 opérations ont modifié le document.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-31_sujet.gh`

### Barème

1 point si le compte est exact.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
