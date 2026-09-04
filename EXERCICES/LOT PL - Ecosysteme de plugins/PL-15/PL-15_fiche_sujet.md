# PL-15 — Combien de plugins pour douze composants

**Fiche d'exercice Magpie** · Lot PL — Écosystème de plugins

| | |
|---|---|
| **Thématique** | PL4 · Plugins fonctionnels |
| **Référence au référentiel** | REF-038, REF-039 |
| **Compétence visée** | Couvrir un besoin en composants par le plus petit nombre de plugins, en exploitant leurs recouvrements. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 22 min |
| **Prérequis** | PL-07 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-21 Le golf de composants |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Couvrir un besoin en composants par le plus petit nombre de plugins, en exploitant leurs recouvrements.

### Contexte

Chaque plugin installé est une dépendance de plus à maintenir, à faire installer par l'apprenant et à revérifier à chaque version de Rhino. On en installe le moins possible.

### Énoncé

> La définition à reprendre emploie douze composants non natifs. Le tableau donne ce qu'apporte chacun des six plugins candidats. Donnez le nombre MINIMAL de plugins à installer pour couvrir les douze.

### Ce qui vous est fourni

La liste des douze composants requis et le tableau des six plugins avec leurs apports.

### Ce qui est attendu

4 plugins suffisent à couvrir les douze composants.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`PL-15_sujet.gh`

### Barème

1 point si le minimum est exact.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
