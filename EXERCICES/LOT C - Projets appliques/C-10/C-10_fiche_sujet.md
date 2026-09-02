# C-10 — Motif gravé génératif sur bijou

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C3 · Joaillerie |
| **Référence au référentiel** | REF-115, REF-095, REF-069 |
| **Compétence visée** | Dimensionner une partition de surface en tenant compte de ce que les séparations consomment. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Expérimenté |
| **Durée cible** | 80 min |
| **Prérequis** | B-10, C-08 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 45 composants |
| **Gamification associée** | G-27 Narration Serengeti + G-09 Récompense cachée |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire un motif non répétitif contrôlé par des règles, puis le graver physiquement.

### Contexte

Le filet entre cellules doit rester gravable. Trop fin, il disparaît au polissage.

### Énoncé

> Génère sur le corps de bague un motif de type Voronoï dont les cellules mesurent entre 0,8 et 2,2 mm², sépare les cellules par un filet de 0,25 mm, grave à 0,3 mm de profondeur, et fais en sorte que le motif boucle sans rupture visible.

### Ce qui vous est fourni

La bague de l'exercice C-08 et un slider de densité de motif.

### Ce qui est attendu

77 cellules.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-10_sujet.gh`

### Barème

4 points motif, 3 points contraintes d'aire, 3 points raccord.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
