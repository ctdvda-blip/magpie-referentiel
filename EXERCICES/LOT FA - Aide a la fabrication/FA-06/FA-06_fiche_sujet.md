# FA-06 — Le trait de scie mange une pièce

**Fiche d'exercice Magpie** · Lot FA — Aide à la fabrication

| | |
|---|---|
| **Thématique** | FA1 · Imbrication |
| **Référence au référentiel** | REF-160 |
| **Compétence visée** | Compter les pièces d'un débit linéaire en tenant compte du trait de scie et des rives inutilisables. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | FA-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Compter les pièces d'un débit linéaire en tenant compte du trait de scie et des rives inutilisables.

### Contexte

Le panneau se refend en lames. La lame de scie prend 4 mm à chaque passage, et les 12 mm de rive ne sont pas utilisables.

### Énoncé

> Le panneau mesure 2 500 mm. Chaque pièce fait 352 mm, le trait de scie 4 mm, et 12 mm de rive sont à écarter de chaque côté. Donnez le nombre de pièces par panneau.

### Ce qui vous est fourni

La longueur du panneau, celle de la pièce, le trait de scie et la rive.

### Ce qui est attendu

6 pièces par panneau.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`FA-06_sujet.gh`

### Barème

1 point si le nombre de pièces est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
