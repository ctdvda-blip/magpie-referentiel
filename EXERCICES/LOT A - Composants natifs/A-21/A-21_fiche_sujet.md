# A-21 — Nettoyer une structure

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A4 · Arbres de données |
| **Référence au référentiel** | REF-050 |
| **Compétence visée** | Supprimer les niveaux de regroupement devenus inutiles sans détruire le regroupement utile. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-20 |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-30 Mode coopératif |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Supprimer les niveaux de regroupement devenus inutiles sans détruire le regroupement utile.

### Contexte

Un enchaînement d'opérations a empilé des niveaux de branche dont aucun ne porte plus de sens.

### Énoncé

> Le flux fourni porte des chemins à quatre niveaux, dont trois ne distinguent plus rien. Ramenez-le à un seul niveau, sans fusionner les groupes entre eux. Indiquez le nombre de branches obtenu.

### Ce qui vous est fourni

Un arbre internalisé de chemins {0;0;0;0} à {0;0;0;3}.

### Ce qui est attendu

Quatre branches, aux chemins {0} à {3}.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SetEquality**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-21_sujet.gh`

### Barème

1 point si les chemins finaux sont {0} à {3}.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
