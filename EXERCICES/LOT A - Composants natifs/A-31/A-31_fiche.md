# A-31 — Orienter un flux avec une condition

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A7 · Portes logiques |
| **Référence au référentiel** | REF-061 |
| **Compétence visée** | Orienter un flux vers l'une ou l'autre de deux sorties selon une condition, sans démonter le montage. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-30 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-24 Sons et retours audio |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Orienter un flux vers l'une ou l'autre de deux sorties selon une condition, sans démonter le montage.

### Contexte

Deux variantes de remplissage sont à l'étude ; le client veut les voir alternativement sans qu'on retouche la définition devant lui.

### Énoncé

> Les deux variantes de remplissage sont montées et fonctionnent. Faites en sorte qu'un seul interrupteur bascule l'affichage de l'une à l'autre, sans supprimer ni débrancher aucun composant.

### Ce qui vous est fourni

Un Circle, un Rectangle et un Boolean Toggle.

### Ce qui est attendu

Une seule géométrie affichée à la fois, commandée par l'interrupteur.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-31_sujet.gh`

### Barème

1 point si l'alternance fonctionne dans les deux sens.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-31_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Stream Filter (Sets > Tree).

**Étape 2.** Brancher le cercle sur Stream 0 et le rectangle sur Stream 1.

**Étape 3.** Brancher le Boolean Toggle sur l'entrée Gate.

**Étape 4.** Basculer le toggle et vérifier l'alternance.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Couper un câble pour masquer une variante : l'affichage est bon, mais la bascule n'est plus réversible et la seconde variante est perdue. La contrainte « sans débrancher » ferme cette voie.

### Pièges fréquents

- Stream Filter attend un entier : le booléen est converti en 0 ou 1.
- Confondre Stream Filter (choisit une entrée) et Stream Gate (aiguille vers une sortie).

### Pour aller plus loin

- Piloter trois géométries avec un slider entier.
- Reproduire le comportement avec un Dispatch.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-31_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-31_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-31.json` | Descripteur pour le plugin Magpie |
| `A-31_fiche.md` | La présente fiche |
| `A-31_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-31_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-31_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
