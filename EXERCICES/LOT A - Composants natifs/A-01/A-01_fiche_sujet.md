# A-01 — Premier flux de données

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A1 · Interface, flux de données et paramètres |
| **Référence au référentiel** | REF-027, REF-028 |
| **Compétence visée** | Raccorder deux sources sur les deux entrées d'un même opérateur et lire la valeur produite. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | — |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Raccorder deux sources sur les deux entrées d'un même opérateur et lire la valeur produite.

### Contexte

Un ensemble menuisé se compose d'une imposte et d'un châssis superposés ; leur hauteur cumulée doit remplir exactement la baie.

### Énoncé

> La baie mesure 2 400 mm de haut. Une valeur de hauteur vous est déjà fournie pour l'imposte. Ajoutez une seconde valeur réglable pour le châssis, faites-en la somme, et réglez les deux hauteurs pour que la baie soit exactement remplie.

### Ce qui vous est fourni

Un Number Slider (0-100, valeur 17) déjà placé.

### Ce qui est attendu

La somme des deux hauteurs vaut exactement 2 400.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-01_sujet.gh`

### Barème

1 point si la valeur du Panel vaut 42.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
