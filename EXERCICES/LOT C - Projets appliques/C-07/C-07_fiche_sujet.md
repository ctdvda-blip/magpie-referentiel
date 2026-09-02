# C-07 — Table de nuit configurable

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C2 · Design de mobilier |
| **Référence au référentiel** | REF-070, REF-072, REF-082, REF-106 |
| **Compétence visée** | Établir un prix par composition, en appliquant chaque coefficient sur son assiette. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 80 min |
| **Prérequis** | B-06, B-07 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 48 composants |
| **Gamification associée** | G-28 Avatar + G-10 Coffre à butin |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire un configurateur complet, avec variantes discrètes et contrôle de cohérence.

### Contexte

Le configurateur affiche un prix à chaque changement. Un coefficient mal appliqué se voit sur des milliers de configurations, jamais sur celle qu'on a testée.

### Énoncé

> Réalise un configurateur de table de nuit : 4 types de pieds au choix, de 1 à 3 tiroirs, deux matériaux avec des épaisseurs différentes. Le modèle doit rester valide dans toutes les combinaisons et produire son prix estimatif.

### Ce qui vous est fourni

Une Value List de types de pied, un slider de nombre de tiroirs, une Value List de matériau.

### Ce qui est attendu

1 033,76 € pour la combinaison compas, trois tiroirs, noyer.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-07_sujet.gh`

### Barème

4 points configurateur, 3 points robustesse, 3 points chiffrage.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
