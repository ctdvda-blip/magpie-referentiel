# RH-03 — Une trame de plots posée dans Rhino

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Modélisation Rhino |
| **Référence au référentiel** | REF-007, REF-008, REF-013 |
| **Compétence visée** | Produire dans Rhino une répétition régulière d'objets à partir d'un original et d'un pas, et la faire mesurer. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-01 Score visible |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire dans Rhino une répétition régulière d'objets à partir d'un original et d'un pas, et la faire mesurer.

### Contexte

Une terrasse sur plots demande un plot tous les 600 mm dans les deux sens, sur une emprise donnée.

### Énoncé

> L'emprise de la terrasse mesure 4 200 mm sur 3 000 mm. Posez un plot cylindrique de 100 mm de diamètre à chaque nœud d'une trame de 600 mm, le premier au coin d'origine. Donnez le nombre de plots.

### Ce qui vous est fourni

Un fichier Rhino avec l'emprise tracée et un plot modèle à l'origine.

### Ce qui est attendu

Un nombre entier : combien de plots compte la trame.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-03_sujet.gh`

### Barème

1 point si le compte vaut 48 et si les quatre angles sont appuyés.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
