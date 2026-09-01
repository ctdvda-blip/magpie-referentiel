# FA-03 — Le développé d'un profil plié

**Fiche d'exercice Magpie** · Lot FA — Aide à la fabrication

| | |
|---|---|
| **Thématique** | FA2 · Déroulé et mise à plat |
| **Référence au référentiel** | REF-116 |
| **Compétence visée** | Calculer la longueur développée d'une tôle pliée en tenant compte de l'allongement de la matière au droit des plis. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 35 min |
| **Prérequis** | FA-02 |
| **Mode de validation** | NumericTolerance — tolérance 0.1 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Calculer la longueur développée d'une tôle pliée en tenant compte de l'allongement de la matière au droit des plis.

### Contexte

Le profil en U part au débit avant pliage : la bande découpée doit avoir exactement la longueur qui, une fois pliée, donnera les cotes du plan.

### Énoncé

> Le profil en U mesure 120 mm d'aile, 300 mm d'âme, cotes extérieures, dans une tôle de 3 mm. Les deux plis à 90° se font sur un rayon intérieur de 5 mm, avec un facteur K de 0,42. Donnez la longueur de la bande à débiter, en millimètres.

### Ce qui vous est fourni

Les cotes extérieures du profil, l'épaisseur de la tôle, le rayon intérieur de pliage et le facteur K.

### Ce qui est attendu

527,67 mm — la longueur développée, à 0,1 mm près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`FA-03_sujet.gh`

### Barème

1 point si le développé est juste à 0,1 mm près.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `FA-03_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Retrancher rayon et épaisseur des cotes extérieures pour obtenir les parties réellement plates.

**Étape 2.** Calculer l'allongement d'un pli à 90° : un quart de cercle sur le rayon de la fibre neutre.

**Étape 3.** La fibre neutre est à r + K·e du centre de courbure.

**Étape 4.** Sommer les parties plates et les deux allongements.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Additionner les cotes extérieures : 120 + 300 + 120 = 540 mm. La matière s'allonge à l'extérieur du pli et se comprime à l'intérieur ; seule la fibre neutre garde sa longueur, et elle ne passe pas au milieu de l'épaisseur — c'est ce que dit le facteur K. L'écart fait 12,3 mm : invisible sur le plan, fatal à l'atelier, et il se répète sur chaque pièce de la série.

### Pièges fréquents

- Sommer les cotes extérieures.
- Placer la fibre neutre au milieu de l'épaisseur, ce qui revient à prendre K = 0,5.
- Oublier que l'âme perd rayon et épaisseur DEUX fois, une par pli.

### Pourquoi ce jeu de données

Un facteur K de 0,42 est la valeur courante pour un acier doux plié sur un rayon voisin de l'épaisseur. Les cotes sont extérieures, comme sur un plan de tôlerie — c'est précisément ce qui oblige à retrancher rayon et épaisseur avant de calculer les parties plates.

### Limite de la correction automatique

> Le facteur K dépend de la nuance, du rayon et de l'outil : celui de l'exercice est donné. En atelier, il se relève sur une pièce d'essai, et c'est le vrai geste métier.

### Pour aller plus loin

- Refaire le calcul avec un facteur K de 0,5 et chiffrer l'écart sur une série de 200 pièces.
- Traiter un profil à trois plis, dont un à 135°.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `FA-03_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `FA-03_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `FA-03.json` | Descripteur pour le plugin Magpie |
| `FA-03_fiche.md` | La présente fiche |
| `FA-03_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `FA-03_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `FA-03_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
