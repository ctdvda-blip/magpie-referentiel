# A-30 — Combiner plusieurs conditions

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A7 · Portes logiques |
| **Référence au référentiel** | REF-060 |
| **Compétence visée** | Combiner deux conditions en une décision unique par élément. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-29 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-06 Niveaux et déblocage |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Combiner deux conditions en une décision unique par élément.

### Contexte

Seules les chutes comprises entre 500 et 1 500 mm sont remises en stock : en deçà elles partent au rebut, au-delà elles retournent en barre.

### Énoncé

> Les longueurs des 24 chutes du jour vous sont fournies. Comptez celles qui repartent en stock, bornes incluses.

### Ce qui vous est fourni

Les 24 longueurs de chutes du jour, en millimètres, et les deux bornes de 500 et 1 500 mm.

### Ce qui est attendu

16 — le nombre de chutes remises en stock, bornes incluses.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-30_sujet.gh`

### Barème

1 point si les 20 booléens sont exacts.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-30_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Larger Than or Equal avec 500 sur B.

**Étape 2.** Poser Smaller Than or Equal avec 1500 sur B.

**Étape 3.** Poser Gate And et brancher les deux listes de booléens.

**Étape 4.** Relier vers un Panel pour contrôler.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Traiter les bornes en strict : les chutes à 505 et 1 495 restent prises, mais une chute à exactement 500 ou 1 500 serait écartée. Le jeu de données contient l'une et l'autre pour que l'écart se voie.

### Pièges fréquents

- Utiliser Gate Or : toutes les pièces ressortent True.
- Bornes strictes alors que l'énoncé dit « inclus ».

### Pourquoi ce jeu de données

24 longueurs, dont une exactement à 500 et une exactement à 1 500. C'est là tout l'intérêt du jeu : bornes incluses la réponse est 16, bornes exclues elle tombe à 14. Un jeu de données sans valeur sur la borne rendrait les deux montages indiscernables.

### Pour aller plus loin

- Exclure une plage avec Gate Not.
- Ajouter une troisième condition sur le matériau.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-30_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-30_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-30.json` | Descripteur pour le plugin Magpie |
| `A-30_fiche.md` | La présente fiche |
| `A-30_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-30_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-30_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
