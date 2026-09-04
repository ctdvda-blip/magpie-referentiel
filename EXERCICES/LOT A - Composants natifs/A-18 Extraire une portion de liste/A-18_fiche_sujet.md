# A-18 — Extraire une portion de liste

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A3 · Listes |
| **Référence au référentiel** | REF-042, REF-043 |
| **Compétence visée** | Prélever une tranche continue d'une liste par ses rangs. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-12 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-03 Compte à rebours |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Prélever une tranche continue d'une liste par ses rangs.

### Contexte

Sur un profil en long, seule la section courante intéresse le calcul ; les relevés d'extrémité relèvent des ouvrages voisins.

### Énoncé

> Le profil compte 28 relevés altimétriques. Isolez ceux des rangs 5 à 12 inclus, qui correspondent à la section courante.

### Ce qui vous est fourni

Les 28 relevés altimétriques du profil en long, en millimètres.

### Ce qui est attendu

Huit relevés : 466, 419, 448, 433, 471, 405, 459, 424.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-18_sujet.gh`

### Barème

1 point si les 8 bons éléments sortent.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
