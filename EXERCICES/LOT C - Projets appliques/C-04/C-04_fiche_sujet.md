# C-04 — Métré et chiffrage complet d'un module

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C1 · Architecture |
| **Référence au référentiel** | REF-082, REF-083, REF-084, REF-086 |
| **Compétence visée** | Structurer un devis par lot avec sous-totaux, et le rendre exact au centime. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 75 min |
| **Prérequis** | B-12, B-13 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 45 composants |
| **Gamification associée** | G-01 Score visible + G-29 Défi quotidien |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire un livrable économique complet à partir d'un modèle, avec traçabilité des hypothèses.

### Contexte

Le devis part au maître d'ouvrage. Un sous-total faux ne se voit pas ; un total faux se voit toujours, et trop tard.

### Énoncé

> À partir du module constructif fourni, produis un devis quantitatif estimatif par lot (gros œuvre, menuiserie, second œuvre) avec quantités, unités, prix unitaires et totaux, ainsi qu'un récapitulatif par lot et un total général. Le calcul doit rester juste si l'on modifie les dimensions du module.

### Ce qui vous est fourni

Un module constructif complet et une table de prix unitaires internalisée.

### Ce qui est attendu

55 099,00 € de total général.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-04_sujet.gh`

### Barème

4 points quantités, 3 points structure du devis, 3 points recalculabilité.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
