# QT-02 — Du métré au prix

**Fiche d'exercice Magpie** · Lot QT — Quantitatifs, chiffrage et export

| | |
|---|---|
| **Thématique** | QT1 · Quantitatifs et chiffrage |
| **Référence au référentiel** | REF-083 |
| **Compétence visée** | Croiser un métré avec un bordereau de prix pour obtenir un montant, sans apparier les mauvaises lignes. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | QT-01 |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Croiser un métré avec un bordereau de prix pour obtenir un montant, sans apparier les mauvaises lignes.

### Contexte

Le bordereau du fournisseur donne un prix au mètre linéaire par section ; le métré donne des longueurs par solive.

### Énoncé

> Le bordereau fournit un prix au mètre linéaire pour chacune des cinq sections. Donnez le montant total du plancher, en euros.

### Ce qui vous est fourni

Les 20 solives avec leur section et leur longueur, et le bordereau des cinq prix unitaires par section.

### Ce qui est attendu

Le montant total, en euros, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`QT-02_sujet.gh`

### Barème

1 point si le montant est juste à 0,01 € près.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `QT-02_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Convertir les longueurs en mètres.

**Étape 2.** Pour chaque solive, retrouver le RANG de sa section dans le bordereau — c'est cet appariement-là qui compte.

**Étape 3.** Extraire le prix correspondant à ce rang.

**Étape 4.** Multiplier prix par longueur, solive par solive.

**Étape 5.** Sommer, et contrôler par un ordre de grandeur : longueur totale multipliée par un prix moyen.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Apparier le bordereau aux solives par leur rang plutôt que par leur section. Il y a vingt solives et cinq prix : un appariement par rang donne silencieusement un résultat, calculé sur le mauvais prix répété — c'est le comportement par défaut vu en A-24, appliqué ici à de l'argent.

### Pièges fréquents

- Laisser les deux listes s'apparier par défaut.
- Oublier la conversion en mètres : le prix est au mètre linéaire, les longueurs sont en millimètres.

### Pourquoi ce jeu de données

Vingt solives pour cinq sections : le déséquilibre est volontaire, c'est lui qui rend l'erreur d'appariement possible et détectable.

### Pour aller plus loin

- Appliquer une remise de 8 % au-delà de 100 mètres linéaires.
- Sortir le montant par section plutôt que le total.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `QT-02_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `QT-02_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `QT-02.json` | Descripteur pour le plugin Magpie |
| `QT-02_fiche.md` | La présente fiche |
| `QT-02_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `QT-02_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `QT-02_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
