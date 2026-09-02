# RH-14 — La trame percée d'une trémie

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Modélisation Rhino |
| **Référence au référentiel** | REF-013, REF-008 |
| **Compétence visée** | Compter les éléments d'un réseau régulier dont une zone a été retirée. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-03 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Compter les éléments d'un réseau régulier dont une zone a été retirée.

### Contexte

La dalle repose sur une trame de plots, sauf à l'aplomb de la trémie d'escalier, où ils sont supprimés.

### Énoncé

> La trame compte huit plots en longueur et six en largeur, au pas de 1 200 mm. La trémie en supprime trois en longueur et deux en largeur. Donnez le nombre de plots.

### Ce qui vous est fourni

Les dimensions de la trame, son pas, et l'emprise de la trémie en nombre de plots.

### Ce qui est attendu

42 plots — 48 moins les 6 de la trémie.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-14_sujet.gh`

### Barème

1 point si le compte est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-14_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Compter la trame complète.

**Étape 2.** Compter l'emprise de la trémie comme un rectangle.

**Étape 3.** Soustraire.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Retrancher 3 + 2 = 5 au lieu de 3 × 2 = 6. La trémie retire un RECTANGLE de plots, pas une ligne et une colonne : l'erreur ne se voit pas sur le compte, mais le plot qu'on a oublié de retirer se retrouve au milieu de l'escalier.

### Pièges fréquents

- Additionner les deux dimensions de la trémie.
- Compter les intervalles au lieu des plots.

### Pourquoi ce jeu de données

Huit par six donne un total, 48, qui ne se confond avec aucune des réponses fausses ; et 3 × 2 = 6 se distingue nettement de 3 + 2 = 5, donc 42 de 43.

### Pour aller plus loin

- Donner la position du dernier plot depuis l'origine.
- Ajouter une seconde trémie, qui chevauche la première d'un plot.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-14_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-14_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-14.json` | Descripteur pour le plugin Magpie |
| `RH-14_fiche.md` | La présente fiche |
| `RH-14_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-14_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-14_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
