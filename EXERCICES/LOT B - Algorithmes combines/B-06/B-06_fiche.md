# B-06 — Caisson de meuble avec épaisseur et rainures

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B2 · Design de mobilier |
| **Référence au référentiel** | REF-070, REF-071, REF-068 |
| **Compétence visée** | Chiffrer la matière d'un assemblage en tenant compte des recouvrements et des usinages qui la font varier. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | A-43, A-44 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 26 composants |
| **Gamification associée** | G-06 Niveaux et déblocage |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Modéliser un assemblage menuisé où toutes les cotes dérivent de trois paramètres.

### Contexte

Le panneau se commande au mètre carré débité. La rainure n'enlève pas de matière au fond : elle lui en AJOUTE, puisqu'il faut le débiter plus grand.

### Énoncé

> Modélise un caisson de largeur L, hauteur H et profondeur P, en panneaux de 19 mm. Les joues reçoivent une rainure de 6 mm de profondeur pour le fond de 8 mm. Le dessus et le dessous s'insèrent entre les joues.

### Ce qui vous est fourni

Trois sliders L, H, P et un slider d'épaisseur.

### Ce qui est attendu

32,73 dm³ de panneau, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-06_sujet.gh`

### Barème

3 points pour l'assemblage, 1 point pour la rainure correcte.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-06_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Construire le volume englobant à partir de L, H, P.

**Étape 2.** Déduire la géométrie de chaque joue : épaisseur × H × P, positionnée à gauche et à droite.

**Étape 3.** Déduire dessus et dessous : (L − 2 × 19) × 19 × P, positionnés entre les joues.

**Étape 4.** Construire le volume de rainure : boîte de 8 mm d'épaisseur, profondeur 6 mm, courant sur toute la hauteur.

**Étape 5.** Soustraire cette boîte des quatre panneaux avec Solid Difference.

**Étape 6.** Poser le fond de 8 mm dans la rainure, avec un jeu de 0,2 mm.

**Étape 7.** Contrôler visuellement l'assemblage en vue éclatée par un Move paramétrable.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Débiter le fond aux cotes intérieures nettes, sans la profondeur des rainures : 32,40 dm³. Le fond entre DANS la rainure — il doit donc mesurer 6 mm de plus de chaque côté, soit 12 mm dans chaque dimension. Coupé trop court, il ne tient plus.

### Pièges fréquents

- Oublier de retirer deux épaisseurs à la longueur du dessus et du dessous.
- Rainure positionnée au nu arrière sans tenir compte de sa profondeur.
- Jeu de montage nul : les pièces s'interpénètrent lors du contrôle de collision.

### Pourquoi ce jeu de données

Un caisson de 800 × 720 × 400 en 19 mm, rainure de 6 mm : l'écart entre les deux calculs vaut 0,33 dm³, soit 1 %. Invisible sur un devis, fatal au montage.

### Pour aller plus loin

- Passer d'un assemblage rainuré à un assemblage par tourillons.
- Ajouter une nomenclature de débit avec chants.
- Générer la vue éclatée animée.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-06_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-06_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-06.json` | Descripteur pour le plugin Magpie |
| `B-06_fiche.md` | La présente fiche |
| `B-06_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-06_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-06_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
