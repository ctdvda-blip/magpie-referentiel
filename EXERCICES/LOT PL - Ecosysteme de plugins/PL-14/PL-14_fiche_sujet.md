# PL-14 — Ce que l'ergonomie coûte au démarrage

**Fiche d'exercice Magpie** · Lot PL — Écosystème de plugins

| | |
|---|---|
| **Thématique** | PL3 · Plugins d'ergonomie |
| **Référence au référentiel** | REF-031, REF-032, REF-033, REF-034, REF-035, REF-036, REF-037 |
| **Compétence visée** | Chiffrer le coût d'une panoplie d'ergonomie sans compter deux fois ce qui est déjà installé. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 14 min |
| **Prérequis** | PL-06 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-05 La collection de badges |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Chiffrer le coût d'une panoplie d'ergonomie sans compter deux fois ce qui est déjà installé.

### Contexte

Chaque plugin allonge le démarrage de Rhino. Sur un poste de formation ouvert et fermé dix fois par jour, la panoplie d'ergonomie se paie en secondes d'attente.

### Énoncé

> Le relevé donne le temps de chargement de sept plugins, et signale ceux qu'un autre plugin déjà installé exige de toute façon. Donnez le temps AJOUTÉ par la panoplie d'ergonomie, en millisecondes.

### Ce qui vous est fourni

Le relevé des sept temps de chargement, et la colonne des dépendances déjà satisfaites.

### Ce qui est attendu

1 220 ms ajoutés au démarrage.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`PL-14_sujet.gh`

### Barème

1 point si le total est exact.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
