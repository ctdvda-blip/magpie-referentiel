# RH-21 — Les faces qui ne mesurent rien

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-022, REF-023 |
| **Compétence visée** | Repérer les faces dégénérées d'un maillage avant de le réparer, en s'appuyant sur la tolérance du document. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-20 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Repérer les faces dégénérées d'un maillage avant de le réparer, en s'appuyant sur la tolérance du document.

### Contexte

Le maillage vient d'une conversion. Certaines faces sont réduites à un fil : elles ne se voient pas, et font échouer la réparation automatique.

### Énoncé

> Les aires des quinze faces suspectes vous sont fournies, en millimètres carrés. La tolérance du document vaut 0,001 mm². Donnez le nombre de faces dégénérées.

### Ce qui vous est fourni

Les quinze aires relevées et la tolérance du document.

### Ce qui est attendu

4 faces dégénérées.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-21_sujet.gh`

### Barème

1 point si le compte est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
