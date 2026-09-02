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

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `C-04_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Classer les solides par lot à partir de leur calque d'origine via Geometry Pipeline.

**Étape 2.** Mesurer les quantités pertinentes par lot : volumes pour le gros œuvre, surfaces pour le second œuvre, linéaires pour les menuiseries.

**Étape 3.** Convertir chaque quantité dans son unité de devis (m³, m², ml).

**Étape 4.** Associer chaque poste à son prix unitaire par Member Index dans la table des prix.

**Étape 5.** Calculer les totaux par poste puis les sous-totaux par lot avec Mass Addition sur arbre.

**Étape 6.** Calculer le total général.

**Étape 7.** Composer les lignes de texte avec Concatenate et Format à deux décimales.

**Étape 8.** Écrire le fichier CSV et vérifier la recalculabilité en modifiant une dimension du module.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Additionner les quantités au lieu des montants, ou sommer les sous-totaux d'un lot en oubliant une ligne. Un devis à trois lots et neuf lignes se vérifie de deux façons — par les lots et par les lignes — et les deux doivent tomber sur le même chiffre.

### Pièges fréquents

- Sous-totaux calculés sur l'arbre aplati : les lots se mélangent.
- Prix unitaires codés en dur dans le graphe au lieu d'une table.
- Doubles comptes entre postes (une paroi comptée en volume et en surface).

### Pourquoi ce jeu de données

Neuf lignes en trois lots, avec des unités différentes — m³, tonne, unité, m² — pour que la somme des quantités n'ait aucun sens et que l'erreur se voie. Les trois sous-totaux sont de tailles très différentes : 9 353, 23 790, 21 956.

### Pour aller plus loin

- Ajouter un coefficient de perte par lot.
- Produire une variante haute et une variante basse.
- Exporter vers Excel avec mise en forme.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `C-04_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `C-04_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `C-04.json` | Descripteur pour le plugin Magpie |
| `C-04_fiche.md` | La présente fiche |
| `C-04_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `C-04_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `C-04_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
