# A-17 — Fusionner et entrelacer

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A3 · Listes |
| **Référence au référentiel** | REF-042 |
| **Compétence visée** | Entrelacer deux listes selon un motif d'alternance. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-13 |
| **Mode de validation** | ExactOrderedList — tolérance — |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-11 Mots croisés de composants |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Entrelacer deux listes selon un motif d'alternance.

### Contexte

Un plateau se compose de lames de deux essences posées en alternance stricte.

### Énoncé

> Cinq lames de chêne et cinq lames de noyer vous sont fournies dans deux listes séparées, repérées par leur longueur. Produisez l'ordre de pose du plateau, une essence sur deux en commençant par le chêne.

### Ce qui vous est fourni

Les longueurs des cinq lames de chêne et des cinq lames de noyer, dans deux listes séparées.

### Ce qui est attendu

La liste ordonnée des longueurs, dans l'ordre de pose du plateau.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-17_sujet.gh`

### Barème

1 point si l'ordre exact est obtenu.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-17_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 1245, 1418, 1268, 1463, 1231, 1437, 1287, 1409, 1252, 1481.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Poser Weave (Sets > List).

**Étape 2.** Relier la première liste sur Stream 0, la seconde sur Stream 1.

**Étape 3.** Laisser le motif par défaut 0, 1 : l'alternance est automatique.

**Étape 4.** Comparer avec Merge qui produirait A, B, C, 1, 2, 3.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Mettre les deux listes bout à bout : on obtient les dix lames, dans un ordre où les cinq chênes précèdent les cinq noyers. L'effectif est bon, le plateau est faux.

### Pièges fréquents

- Confondre Weave (alternance) et Merge (concaténation).
- Motif de tissage personnalisé mal renseigné.

### Pourquoi ce jeu de données

Les deux essences occupent deux plages de longueur distinctes — chêne autour de 1 250, noyer autour de 1 440. L'alternance se contrôle donc à la lecture, et une mise bout à bout se repère au premier coup d'œil. La réponse est numérique, comme l'exige le checker.

### Note au formateur

> Un seul composant suffit. La compétence réelle — choisir entre mettre bout à bout et entrelacer — gagnerait à être posée en question charnière avant l'exercice.

### Pour aller plus loin

- Tisser trois listes avec un motif 0, 1, 2.
- Reconstituer les deux listes d'origine avec Cull Pattern.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-17_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-17_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-17.json` | Descripteur pour le plugin Magpie |
| `A-17_fiche.md` | La présente fiche |
| `A-17_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-17_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-17_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
