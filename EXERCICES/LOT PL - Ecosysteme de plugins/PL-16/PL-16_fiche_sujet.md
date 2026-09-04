# PL-16 — Ce qui tourne encore sous Rhino 8

**Fiche d'exercice Magpie** · Lot PL — Écosystème de plugins

| | |
|---|---|
| **Thématique** | PL1 · Écosystème de plugins |
| **Référence au référentiel** | REF-029, REF-038, REF-039 |
| **Compétence visée** | Vérifier la compatibilité d'un parc de plugins avec une version cible, en tenant les DEUX bornes. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 12 min |
| **Prérequis** | PL-09 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-18 Vrai ou faux à élimination |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Vérifier la compatibilité d'un parc de plugins avec une version cible, en tenant les DEUX bornes.

### Contexte

Migrer une salle de formation vers une nouvelle version de Rhino se prépare : un plugin abandonné à la version 7 ne chargera pas, et la définition qui l'emploie s'ouvrira en rouge devant les apprenants.

### Énoncé

> Le tableau donne, pour quatorze plugins, la version de Rhino minimale et la version maximale supportée. Donnez le nombre de plugins compatibles avec Rhino 8.

### Ce qui vous est fourni

Le tableau des quatorze plugins et de leurs deux bornes.

### Ce qui est attendu

10 plugins sur 14 sont compatibles avec Rhino 8.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`PL-16_sujet.gh`

### Barème

1 point si le compte est exact.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
