# RH-16 — La surface d'un rampant

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Modélisation Rhino |
| **Référence au référentiel** | REF-010, REF-011 |
| **Compétence visée** | Mesurer une surface inclinée dans son plan, et non dans sa projection horizontale. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-15 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mesurer une surface inclinée dans son plan, et non dans sa projection horizontale.

### Contexte

On commande la couverture d'un appentis : le couvreur pose sur le rampant, le plan le montre en projection.

### Énoncé

> L'appentis mesure 8 400 mm de long, 3 200 mm de profondeur en projection, pour un dénivelé de 1 500 mm. Donnez la surface de couverture à commander, en mètres carrés.

### Ce qui vous est fourni

La longueur, la profondeur en projection et le dénivelé.

### Ce qui est attendu

29,69 m² — la surface du rampant, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-16_sujet.gh`

### Barème

1 point si la surface du rampant est juste à 0,01 m² près.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-16_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Calculer la longueur du rampant par le théorème de Pythagore.

**Étape 2.** Multiplier par la longueur de l'appentis.

**Étape 3.** Convertir en mètres carrés.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Multiplier la longueur par la profondeur en projection : 26,88 m². Il manque 2,81 m², soit près de 10 % — de quoi arrêter le chantier à trois rangs de la faîtière.

### Pièges fréquents

- Prendre la profondeur en projection pour le rampant.
- Oublier la conversion en mètres carrés.

### Pourquoi ce jeu de données

Un dénivelé de 1 500 pour 3 200 de projection fait une pente de 25°, courante en appentis. L'écart de 10 % entre les deux réponses est trop petit pour se voir sur un plan, trop grand pour se rattraper sur une commande.

### Pour aller plus loin

- Ajouter un débord de 400 mm et reprendre.
- Donner le nombre de plaques de 2 000 × 1 050 mm nécessaires.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-16_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-16_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-16.json` | Descripteur pour le plugin Magpie |
| `RH-16_fiche.md` | La présente fiche |
| `RH-16_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-16_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-16_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
