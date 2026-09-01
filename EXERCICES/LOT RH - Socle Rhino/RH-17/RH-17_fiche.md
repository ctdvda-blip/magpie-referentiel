# RH-17 — Le volume de deux blocs qui se recouvrent

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Modélisation Rhino |
| **Référence au référentiel** | REF-012 |
| **Compétence visée** | Calculer le volume d'une réunion de solides sans compter deux fois la matière commune. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-05 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Calculer le volume d'une réunion de solides sans compter deux fois la matière commune.

### Contexte

Deux massifs de béton se recoupent en angle. On commande le béton au volume.

### Énoncé

> Le premier massif mesure 400 × 300 × 200 mm, le second 250 × 350 × 180 mm, et leur recouvrement 150 × 200 × 180 mm. Donnez le volume de béton, en décimètres cubes.

### Ce qui vous est fourni

Les dimensions des deux massifs et celles de leur recouvrement.

### Ce qui est attendu

34,35 dm³ — la réunion des deux massifs.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-17_sujet.gh`

### Barème

1 point si le volume de la réunion est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-17_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Calculer chaque volume.

**Étape 2.** Additionner les deux massifs.

**Étape 3.** Retrancher une fois le recouvrement.

**Étape 4.** Convertir en décimètres cubes.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Additionner les deux volumes : 39,75 dm³. La zone commune est alors comptée deux fois — 5,4 dm³ de béton commandés pour rien, et l'erreur se répète à chaque massif de la série.

### Pièges fréquents

- Additionner sans retrancher.
- Retrancher deux fois le recouvrement.

### Pourquoi ce jeu de données

Le recouvrement représente 14 % de la réunion : assez pour que l'écart se voie sur une commande, assez peu pour qu'on l'oublie. Les trois volumes sont donnés, de sorte que l'exercice porte sur le raisonnement et non sur la construction géométrique.

### Pour aller plus loin

- Traiter trois massifs dont deux recouvrements.
- Donner le volume de la seule zone commune.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-17_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-17_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-17.json` | Descripteur pour le plugin Magpie |
| `RH-17_fiche.md` | La présente fiche |
| `RH-17_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-17_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-17_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
