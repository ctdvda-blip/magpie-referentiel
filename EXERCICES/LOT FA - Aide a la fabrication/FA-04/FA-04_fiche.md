# FA-04 — Combien de pièces par fournée

**Fiche d'exercice Magpie** · Lot FA — Aide à la fabrication

| | |
|---|---|
| **Thématique** | FA1 · Imbrication |
| **Référence au référentiel** | REF-114 |
| **Compétence visée** | Estimer le remplissage d'un volume de fabrication en raisonnant par encombrement, et non par volume de matière. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | FA-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 10 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Estimer le remplissage d'un volume de fabrication en raisonnant par encombrement, et non par volume de matière.

### Contexte

La machine de fabrication additive facture à la fournée, pas à la pièce : le prix unitaire dépend entièrement du nombre de pièces qu'on fait tenir dans le volume de construction.

### Énoncé

> Le volume de construction mesure 250 × 210 × 210 mm. La pièce tient dans un encombrement de 62 × 38 × 95 mm et ne peut pas être réorientée. Il faut 4 mm entre deux pièces et 4 mm entre une pièce et chaque paroi. Donnez le nombre de pièces par fournée.

### Ce qui vous est fourni

Les dimensions du volume de construction, l'encombrement de la pièce et l'écart minimal à respecter.

### Ce qui est attendu

24 — soit 3 pièces en longueur, 4 en largeur et 2 en hauteur.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`FA-04_sujet.gh`

### Barème

1 point si le nombre de pièces est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `FA-04_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Retrancher les deux écarts de paroi de chaque dimension du plateau.

**Étape 2.** Sur chaque axe, chercher combien de pièces séparées d'un écart tiennent dans la longueur utile.

**Étape 3.** Arrondir chaque compte à l'entier INFÉRIEUR : une pièce qui dépasse ne se produit pas.

**Étape 4.** Multiplier les trois comptes.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Diviser le volume du plateau par le volume de la pièce : 11 025 000 ÷ 223 820 donne 49 pièces, soit le double. Le rapport des volumes ignore que les pièces ne se déforment pas pour combler les creux — c'est la même erreur que le rapport des surfaces en FA-01, et elle se paie ici au prix de la fournée.

### Pièges fréquents

- Diviser les volumes.
- Arrondir au plus proche au lieu de l'inférieur.
- Compter un écart de trop ou de moins : entre n pièces il y a n − 1 intervalles, plus les deux écarts de paroi.

### Pourquoi ce jeu de données

Les trois divisions tombent chacune sur une valeur franchement non entière — 3,72, 4,90 et 2,08 — de sorte qu'un arrondi au plus proche donnerait 4, 5 et 2, soit 40 pièces qui ne rentrent pas. L'écart entre le rapport des volumes (49) et le compte réel (24) est du simple au double : impossible de confondre les deux méthodes.

### Limite de la correction automatique

> Le compte suppose une orientation fixe et une grille régulière. Un imbriquement réel, qui autorise la rotation et l'entrelacement, fait mieux — mais jamais autant que le rapport des volumes.

### Pour aller plus loin

- Autoriser la rotation à 90° autour de l'axe vertical et recompter.
- Chiffrer le prix unitaire pour une fournée facturée 380 € et le comparer à celui qu'aurait donné le rapport des volumes.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `FA-04_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `FA-04_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `FA-04.json` | Descripteur pour le plugin Magpie |
| `FA-04_fiche.md` | La présente fiche |
| `FA-04_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `FA-04_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `FA-04_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
