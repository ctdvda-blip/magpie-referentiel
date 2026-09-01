# FA-06 — Le trait de scie mange une pièce

**Fiche d'exercice Magpie** · Lot FA — Aide à la fabrication

| | |
|---|---|
| **Thématique** | FA1 · Imbrication |
| **Référence au référentiel** | REF-160 |
| **Compétence visée** | Compter les pièces d'un débit linéaire en tenant compte du trait de scie et des rives inutilisables. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | FA-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Compter les pièces d'un débit linéaire en tenant compte du trait de scie et des rives inutilisables.

### Contexte

Le panneau se refend en lames. La lame de scie prend 4 mm à chaque passage, et les 12 mm de rive ne sont pas utilisables.

### Énoncé

> Le panneau mesure 2 500 mm. Chaque pièce fait 352 mm, le trait de scie 4 mm, et 12 mm de rive sont à écarter de chaque côté. Donnez le nombre de pièces par panneau.

### Ce qui vous est fourni

La longueur du panneau, celle de la pièce, le trait de scie et la rive.

### Ce qui est attendu

6 pièces par panneau.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`FA-06_sujet.gh`

### Barème

1 point si le nombre de pièces est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `FA-06_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Retirer les deux rives de la longueur du panneau.

**Étape 2.** Chercher combien de pièces séparées d'un trait de scie tiennent dans ce qui reste : entre n pièces il y a n − 1 traits.

**Étape 3.** Arrondir à l'entier INFÉRIEUR.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Diviser la longueur du panneau par celle de la pièce : 2 500 ÷ 352 donne 7,1, donc 7 pièces. Il en manque une. Le trait de scie et les rives mangent 44 mm à eux tous — moins de 2 % du panneau, et une pièce sur sept. C'est le genre d'écart qui ne se voit qu'au moment où la dernière lame manque.

### Pièges fréquents

- Diviser sans rien retirer.
- Compter un trait de scie de trop ou de moins.
- Arrondir au plus proche.

### Pourquoi ce jeu de données

352 mm est choisi pour que le compte BASCULE : sans trait ni rives on en tire sept, avec on en tire six. À 360 mm les deux calculs donneraient six, et l'exercice ne prouverait rien.

### Limite de la correction automatique

> Le calcul suppose un débit dans un seul sens. Un panneau se refend souvent dans les deux, et le compte devient celui de FA-04 — une affaire d'encombrement, pas de longueur.

### Pour aller plus loin

- Chiffrer la chute, et sa part du panneau.
- Trouver la longueur de pièce qui ne laisserait aucune chute.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `FA-06_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `FA-06_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `FA-06.json` | Descripteur pour le plugin Magpie |
| `FA-06_fiche.md` | La présente fiche |
| `FA-06_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `FA-06_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `FA-06_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
