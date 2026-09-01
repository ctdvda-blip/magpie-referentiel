# RH-22 — La finesse du maillage à l'export

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-024 |
| **Compétence visée** | Régler la finesse d'un maillage d'export à partir de l'écart admissible à la surface, et non au jugé. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 25 min |
| **Prérequis** | RH-10 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Régler la finesse d'un maillage d'export à partir de l'écart admissible à la surface, et non au jugé.

### Contexte

Le cylindre part en fabrication. Le maillage d'export remplace le cercle par un polygone : la question est de savoir de combien il s'en écarte.

### Énoncé

> Le cylindre a 30 mm de rayon. L'écart entre le maillage et la surface réelle ne doit pas dépasser 0,05 mm. Donnez le nombre minimal de facettes sur un demi-tour.

### Ce qui vous est fourni

Le rayon du cylindre et l'écart maximal admis.

### Ce qui est attendu

55 facettes sur un demi-tour.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-22_sujet.gh`

### Barème

1 point si le nombre de facettes est juste et arrondi au supérieur.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-22_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Écrire l'écart entre la corde et l'arc en fonction du nombre de facettes.

**Étape 2.** Inverser la relation pour obtenir le nombre de facettes.

**Étape 3.** Arrondir au SUPÉRIEUR.

**Étape 4.** Vérifier l'écart obtenu, et celui d'une facette de moins.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Régler la finesse sur un curseur, au jugé, jusqu'à ce que l'aperçu paraisse lisse. L'aperçu paraît lisse bien avant que l'écart soit tenu — à 54 facettes il vaut déjà 0,0508 mm, au-delà du toléré, et rien à l'écran ne le signale.

### Pièges fréquents

- Arrondir au plus proche.
- Régler au jugé sur l'aperçu.
- Confondre l'écart à la surface et la longueur de la corde.

### Pourquoi ce jeu de données

L'écart d'une corde à son arc vaut r(1 − cos(π/n)). Avec r = 30 et 0,05 mm admis, n vaut 54,41 : la frontière tombe entre deux entiers, de sorte qu'un arrondi au plus proche donnerait 54 — qui ne tient pas l'écart. C'est un arrondi au SUPÉRIEUR.

### Limite de la correction automatique

> Le calcul porte sur la circonférence. La finesse selon l'axe, elle, ne dépend pas de l'écart mais du procédé.

### Pour aller plus loin

- Refaire pour un rayon de 5 mm : le nombre de facettes change peu, le poids du fichier beaucoup.
- Chiffrer le poids du fichier obtenu.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-22_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-22_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-22.json` | Descripteur pour le plugin Magpie |
| `RH-22_fiche.md` | La présente fiche |
| `RH-22_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-22_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-22_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
