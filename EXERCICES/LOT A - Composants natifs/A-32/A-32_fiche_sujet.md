# A-32 — Vecteur, amplitude et direction

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A8 · Géométrie vectorielle et filaire |
| **Référence au référentiel** | REF-062 |
| **Compétence visée** | Construire un vecteur entre deux points, puis en régler la longueur sans en changer la direction. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-02 |
| **Mode de validation** | GeometryTolerance — tolérance 0,01 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-26 Feedback visuel immédiat |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Construire un vecteur entre deux points, puis en régler la longueur sans en changer la direction.

### Contexte

Une potence de levage est reprise par un tirant : la direction est imposée par la géométrie, la longueur par la portée à couvrir.

### Énoncé

> Le tirant part de l'origine et rejoint le point situé à 30 en X et 40 en Y. Construisez sa direction, puis produisez un second tirant de même direction mais de 100 unités de long.

### Ce qui vous est fourni

Deux points internalisés.

### Ce qui est attendu

Un vecteur de longueur 50 et un vecteur de longueur 100, de même direction.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-32_sujet.gh`

### Barème

1 point par vecteur correct.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
