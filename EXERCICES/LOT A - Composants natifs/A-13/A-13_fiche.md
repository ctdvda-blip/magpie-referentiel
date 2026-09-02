# A-13 — Trier une liste avec une clé

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A3 · Listes |
| **Référence au référentiel** | REF-044, REF-047 |
| **Compétence visée** | Réordonner une liste selon les valeurs portées par une autre. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-12 |
| **Mode de validation** | ExactOrderedList — tolérance — |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-08 Combo / série |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Réordonner une liste selon les valeurs portées par une autre.

### Contexte

L'atelier veut débiter les pièces les plus longues en premier, pour engager la barre la plus contraignante tant que le stock est intact.

### Énoncé

> Six pièces portent chacune un numéro de repère et une longueur. L'atelier débite la plus longue en premier. Produisez la liste des numéros de repère dans l'ordre de passage à la scie.

### Ce qui vous est fourni

Les six numéros de repère et les six longueurs correspondantes, dans deux listes de même rang.

### Ce qui est attendu

La liste ordonnée des numéros de repère, du plus long débit au plus court.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-13_sujet.gh`

### Barème

1 point si l'ordre exact est respecté.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-13_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 4256, 4207, 4229, 4198, 4183, 4171.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Poser Sort List : longueurs sur Keys, noms sur Values A.

**Étape 2.** La sortie A est triée par longueur croissante.

**Étape 3.** Poser Reverse List sur la sortie A pour obtenir l'ordre décroissant.

**Étape 4.** Relier vers un Panel.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Trier les repères eux-mêmes, ce qui donne un classement alphabétique sans rapport avec les longueurs. L'erreur révèle qu'on n'a pas vu que le tri devait être commandé par une autre liste.

### Pièges fréquents

- Brancher les noms sur Keys : le tri se fait alors par ordre alphabétique.
- Oublier que Sort List renvoie aussi les clés triées sur la sortie K.

### Pourquoi ce jeu de données

Les numéros de repère sont volontairement décorrélés des longueurs : un tri portant sur les repères eux-mêmes donne un ordre différent, donc détectable. La réponse est numérique, comme l'exige le checker.

### Pour aller plus loin

- Trier selon deux critères successifs.
- Trier des points par distance à un point de référence.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-13_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-13_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-13.json` | Descripteur pour le plugin Magpie |
| `A-13_fiche.md` | La présente fiche |
| `A-13_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-13_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-13_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
