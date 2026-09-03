# B-09 — Griffe de sertissage paramétrique

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B3 · Joaillerie |
| **Référence au référentiel** | REF-068, REF-069, REF-067 |
| **Compétence visée** | Chiffrer la matière d'un élément incliné, dont la longueur n'est pas sa projection. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 28 min |
| **Prérequis** | A-39, A-42 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 22 composants |
| **Gamification associée** | G-10 Coffre à butin |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Construire un détail technique répétitif autour d'un axe, avec contrôle d'inclinaison.

### Contexte

Le fil d'or se pèse et se facture au millimètre. Une griffe inclinée est plus longue que la hauteur qu'elle couvre.

### Énoncé

> Modélise 4 griffes réparties à 90° autour d'une pierre ronde de 5 mm de diamètre. Chaque griffe est un fil de 0,9 mm de diamètre, incliné de 12° vers l'intérieur, avec une tête arrondie recouvrant la ceinture de la pierre.

### Ce qui vous est fourni

Un slider de diamètre de pierre et une sphère de gabarit.

### Ce qui est attendu

14,72 mm de fil, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-09_sujet.gh`

### Barème

2 points pour la géométrie, 1 point pour l'inclinaison, 1 point pour le recouvrement.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-09_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Construire le cercle de ceinture de la pierre.

**Étape 2.** Tracer le profil d'une griffe par Interpolate sur 3 ou 4 points de contrôle.

**Étape 3.** Incliner ce profil de 12° avec Rotate Axis autour d'un axe tangent au cercle.

**Étape 4.** Transformer le profil en solide avec Pipe de rayon 0,45.

**Étape 5.** Répartir par Polar Array avec Count = 4 et Angle = 2π.

**Étape 6.** Vérifier que la tête de griffe recouvre bien la ceinture par une intersection Brep|Brep.

**Étape 7.** Contrôler l'absence de collision entre griffes voisines.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Prendre la hauteur droite : 14,40 mm. Une griffe inclinée de 12° est 2,2 % plus longue que sa projection verticale. Sur une pièce unique cela ne se voit pas ; sur une série, c'est du fil d'or qui manque à chaque montage.

### Pièges fréquents

- Angle saisi en degrés au lieu de radians.
- Axe de rotation mal choisi : les griffes s'inclinent hors du plan attendu.
- Pipe de rayon égal au diamètre : la griffe fait le double de la cote demandée.

### Pourquoi ce jeu de données

Quatre griffes de 3,6 mm inclinées à 12° : l'écart avec la hauteur droite vaut 0,32 mm au total. À l'échelle de la joaillerie, c'est un tiers de diamètre de fil.

### Limite de la correction automatique

> 14,72 mm est la longueur de fil DÉVELOPPÉE. Le sertissage écrase la griffe sur la pierre et la raccourcit de quelques dixièmes : un joaillier ajoute une surlongueur d'atelier que ce calcul n'anticipe pas.

### Pour aller plus loin

- Passer à 6 griffes et vérifier la non-collision.
- Faire varier l'inclinaison en fonction du diamètre de pierre.
- Ajouter un panier sous la pierre.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-09_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-09_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-09.json` | Descripteur pour le plugin Magpie |
| `B-09_fiche.md` | La présente fiche |
| `B-09_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-09_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-09_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
