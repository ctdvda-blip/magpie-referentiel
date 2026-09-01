# RH-20 — Un maillage est-il fermé

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-019, REF-020, REF-021 |
| **Compétence visée** | Établir par le calcul qu'un maillage est ouvert, et de combien, sans se fier à son apparence. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 25 min |
| **Prérequis** | RH-08 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir par le calcul qu'un maillage est ouvert, et de combien, sans se fier à son apparence.

### Contexte

Le maillage part à l'impression. À l'écran, il paraît parfaitement fermé — c'est toujours le cas.

### Énoncé

> Le maillage compte 2 960 faces triangulaires et 4 434 arêtes. Donnez le nombre d'arêtes nues.

### Ce qui vous est fourni

Le nombre de faces triangulaires et le nombre d'arêtes.

### Ce qui est attendu

12 arêtes nues.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-20_sujet.gh`

### Barème

1 point si le nombre d'arêtes nues est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-20_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Compter les arêtes qu'exigent les faces : trois par triangle.

**Étape 2.** Compter celles qu'offrent les arêtes réelles : deux usages chacune si elles sont intérieures.

**Étape 3.** La différence est le nombre d'arêtes nues.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Conclure que le maillage est fermé parce que rien ne se voit. Un maillage fermé de 2 960 triangles aurait exactement 4 440 arêtes : chaque arête y est partagée par deux faces. Il en manque six, donc douze arêtes ne sont bordées que d'une seule face — et la pièce sortira de la machine avec un trou.

### Pièges fréquents

- Se fier à l'aperçu.
- Confondre arêtes nues et faces manquantes.

### Pourquoi ce jeu de données

Le raisonnement tient en une ligne : trois arêtes par triangle, deux triangles par arête intérieure, donc 3F − 2E arêtes nues. Douze arêtes nues sur 4 434, c'est 0,3 % — invisible à l'œil, rédhibitoire à la machine.

### Limite de la correction automatique

> Le compte dit qu'il y a des trous, pas où ils sont. Les localiser demande les outils d'analyse, que RH-21 aborde.

### Pour aller plus loin

- Retrouver le nombre d'arêtes d'un maillage fermé de même nombre de faces.
- Refaire le calcul pour un maillage quadrangulaire.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-20_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-20_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-20.json` | Descripteur pour le plugin Magpie |
| `RH-20_fiche.md` | La présente fiche |
| `RH-20_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-20_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-20_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
