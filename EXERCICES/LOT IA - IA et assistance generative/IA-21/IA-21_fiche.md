# IA-21 — Le script qui compte les intervalles

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA2 · Composants scriptés assistés |
| **Référence au référentiel** | REF-121 |
| **Compétence visée** | Relire un script produit par un assistant en confrontant ce qu'il compte à ce que la tâche demande. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | IA-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-15 Relecture de code |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Relire un script produit par un assistant en confrontant ce qu'il compte à ce que la tâche demande.

### Contexte

La clôture fait 18,60 m et les poteaux ne doivent pas être espacés de plus de 2,50 m. Le script généré rend un nombre, et il paraît raisonnable.

### Énoncé

> La file mesure 18 600 mm et l'entraxe ne doit pas dépasser 2 500 mm. Donnez le nombre de poteaux.

### Ce qui vous est fourni

La longueur de la file et l'entraxe maximal admis.

### Ce qui est attendu

9 poteaux — huit travées de 2 325 mm.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-21_sujet.gh`

### Barème

1 point si le nombre de poteaux est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-21_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Diviser la longueur par l'entraxe maximal.

**Étape 2.** Arrondir au supérieur : c'est le nombre de TRAVÉES.

**Étape 3.** Ajouter un : les poteaux sont un de plus que les travées.

**Étape 4.** Vérifier l'entraxe réel obtenu.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Rendre 8, le nombre de TRAVÉES. C'est ce que rend un script qui divise et arrondit sans se demander ce qu'il compte. Le résultat est plausible, l'ordre de grandeur est juste, et il manque un poteau — celui du bout, qui est aussi celui qui tient la clôture.

### Pièges fréquents

- Rendre le nombre de travées.
- Arrondir au plus proche, ce qui donnerait 7 travées et un entraxe de 2 657 mm, au-delà du maximum.

### Pourquoi ce jeu de données

18 600 ÷ 2 500 vaut 7,44 : l'arrondi au supérieur donne 8 travées, donc 9 poteaux, et l'entraxe réel tombe à 2 325 mm. Les deux réponses possibles diffèrent d'une unité — l'erreur la plus fréquente en programmation, et celle qui passe le mieux la relecture.

### Limite de la correction automatique

> L'exercice suppose les deux extrémités équipées d'un poteau. Une clôture qui vient buter contre un mur n'en a qu'un — et c'est le genre de précision que la consigne doit porter, pas le script.

### Pour aller plus loin

- Reprendre pour une clôture butant sur un mur à chaque bout.
- Donner la position de chaque poteau depuis l'origine.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-21_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-21_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-21.json` | Descripteur pour le plugin Magpie |
| `IA-21_fiche.md` | La présente fiche |
| `IA-21_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-21_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-21_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
