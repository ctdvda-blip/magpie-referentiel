# RH-15 — Le développé d'un cheminement

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Modélisation Rhino |
| **Référence au référentiel** | REF-009 |
| **Compétence visée** | Mesurer la longueur réellement parcourue par une polyligne, et non la distance entre ses extrémités. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-14 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mesurer la longueur réellement parcourue par une polyligne, et non la distance entre ses extrémités.

### Contexte

On chiffre un linéaire de garde-corps le long d'un cheminement qui tourne quatre fois.

### Énoncé

> Les six sommets du cheminement vous sont fournis. Donnez sa longueur développée, en millimètres.

### Ce qui vous est fourni

Les coordonnées en plan des six sommets.

### Ce qui est attendu

13 400 mm — la somme des cinq segments.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-15_sujet.gh`

### Barème

1 point si le développé est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-15_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Relier les sommets dans l'ordre.

**Étape 2.** Mesurer la courbe obtenue, et non la distance entre ses extrémités.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Mesurer la distance du premier au dernier point : 10 065 mm. C'est la corde, pas le parcours — et 3,3 m de garde-corps manqueraient à la livraison.

### Pièges fréquents

- Mesurer la corde.
- Fermer la polyligne sans que la consigne le demande.

### Pourquoi ce jeu de données

Cinq segments orthogonaux de longueurs différentes, et un écart de 25 % entre la corde et le développé : assez grand pour que l'erreur se voie au chiffrage, assez petit pour qu'elle ne saute pas aux yeux sur le plan.

### Pour aller plus loin

- Donner la longueur de chaque segment, pour le débit.
- Ajouter un congé de 300 mm à chaque angle et reprendre la mesure.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-15_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-15_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-15.json` | Descripteur pour le plugin Magpie |
| `RH-15_fiche.md` | La présente fiche |
| `RH-15_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-15_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-15_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
