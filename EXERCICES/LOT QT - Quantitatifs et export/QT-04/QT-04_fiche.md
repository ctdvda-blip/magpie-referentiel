# QT-04 — Un débit qui devient une commande

**Fiche d'exercice Magpie** · Lot QT — Quantitatifs, chiffrage et export

| | |
|---|---|
| **Thématique** | QT3 · Export de données |
| **Référence au référentiel** | REF-085 |
| **Compétence visée** | Regrouper un relevé ligne à ligne en une table par référence, de sorte que chaque référence n'apparaisse qu'une fois avec sa quantité cumulée. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | QT-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-11 Commande à passer |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Regrouper un relevé ligne à ligne en une table par référence, de sorte que chaque référence n'apparaisse qu'une fois avec sa quantité cumulée.

### Contexte

Le débit sort de l'atelier ligne par ligne, dans l'ordre du montage. Le fournisseur, lui, veut une commande : une ligne par référence, et la quantité totale.

### Énoncé

> Le débit vous est fourni tel qu'il sort de l'atelier : vingt-quatre lignes, dans le désordre, où la même référence revient plusieurs fois. Donnez la quantité totale de la référence la plus commandée.

### Ce qui vous est fourni

Les vingt-quatre lignes du débit : une référence de panneau et une quantité par ligne.

### Ce qui est attendu

17 — la quantité cumulée de la référence la plus commandée.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`QT-04_sujet.gh`

### Barème

1 point si la quantité cumulée est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `QT-04_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Établir la liste des références distinctes.

**Étape 2.** Rattacher chaque ligne du débit à sa référence.

**Étape 3.** Cumuler les quantités par référence.

**Étape 4.** Prendre le plus grand cumul.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Prendre la plus grande quantité d'une seule ligne (8) au lieu du cumul par référence. La table n'est alors pas regroupée : elle est seulement triée, et le fournisseur recevra vingt-quatre lignes dont huit références en double.

### Pièges fréquents

- Confondre le nombre de lignes et la quantité.
- Regrouper sur un libellé approchant : les références se ressemblent, deux d'entre elles ne diffèrent que par leur épaisseur.

### Pourquoi ce jeu de données

Vingt-quatre lignes pour huit références, réparties de façon que la référence la plus FRÉQUENTE (quatre lignes) ne soit pas celle qui porte la plus grosse ligne unitaire : compter les occurrences donne une autre réponse que cumuler les quantités. Les deux suivantes sont à 15, assez proches pour qu'un cumul approximatif se trompe de référence.

### Pour aller plus loin

- Rendre la table complète, une ligne par référence, triée par quantité décroissante.
- Ajouter une colonne de prix unitaire et sortir le montant.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `QT-04_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `QT-04_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `QT-04.json` | Descripteur pour le plugin Magpie |
| `QT-04_fiche.md` | La présente fiche |
| `QT-04_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `QT-04_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `QT-04_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
