# A-41 — Extrusion et surface réglée

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A10 · Surfaces et solides |
| **Référence au référentiel** | REF-069 |
| **Compétence visée** | Passer d'une courbe à une surface par extrusion et par transition entre profils. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-34 |
| **Mode de validation** | GeometryTolerance — tolérance 0,5 mm |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-27 Narration Serengeti |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Passer d'une courbe à une surface par extrusion et par transition entre profils.

### Contexte

Une trémie relie deux sections différentes ; un conduit droit relie deux sections identiques.

### Énoncé

> Deux profils fermés superposés vous sont fournis. Produisez la surface de transition qui les relie, puis, séparément, la surface obtenue en poussant le profil du bas de 200 mm vers le haut. Comparez les deux.

### Ce qui vous est fourni

Deux profils fermés internalisés à 0 et 300 mm.

### Ce qui est attendu

Une surface de transition et une surface d'extrusion.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,5 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-41_sujet.gh`

### Barème

1 point par surface correcte.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-41_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Loft et brancher les deux profils dans l'ordre bas puis haut.

**Étape 2.** Régler les options de Loft (Normal, Straight) via son menu contextuel.

**Étape 3.** Poser Extrude avec Unit Z multiplié par 200.

**Étape 4.** Comparer : Loft suit les deux profils, Extrude conserve la section constante.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Obtenir une transition vrillée parce que les deux profils ne démarrent pas au même endroit : la surface est valide mais inconstruisible.

### Pièges fréquents

- Profils branchés dans le désordre : le Loft se vrille.
- Extrude attend un vecteur, pas une distance.

### Limite de la correction automatique

> Les deux surfaces sont produites. Elles n'ont pas la même NATURE : la transition entre deux profils dépend de leur paramétrage et peut se vriller, là où l'extrusion ne le peut pas. Deux surfaces d'apparence proche se comportent différemment en aval.

### Pour aller plus loin

- Lofter trois profils et observer la continuité.
- Extruder le long d'une courbe avec Extrude Along.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-41_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-41_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-41.json` | Descripteur pour le plugin Magpie |
| `A-41_fiche.md` | La présente fiche |
| `A-41_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-41_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-41_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
