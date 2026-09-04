# GP-12 — Tourner puis déplacer, ou l'inverse

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP3 · Transformations et réseaux |
| **Référence au référentiel** | REF-149 |
| **Compétence visée** | Composer deux transformations en sachant que leur ordre décide du résultat. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | GP-11 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 12 composants |
| **Gamification associée** | G-08 Relevé contradictoire |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Composer deux transformations en sachant que leur ordre décide du résultat.

### Contexte

Le bras de la potence est décrit par une rotation et une translation. Selon l'ordre où on les applique, son extrémité ne tombe pas au même endroit.

### Énoncé

> Le point est à 1 200 mm de l'origine sur l'axe des abscisses. On lui applique une rotation de 35° autour de l'origine et une translation de 800 mm en X et 300 mm en Y. Donnez la distance entre les deux positions finales possibles, en millimètres.

### Ce qui vous est fourni

La position du point, l'angle de rotation et le vecteur de translation.

### Ce qui est attendu

513,85 mm séparent les deux résultats, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-12_sujet.gh`

### Barème

1 point si la distance est juste à 0,01 mm près.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `GP-12_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Appliquer la rotation puis la translation.

**Étape 2.** Appliquer la translation puis la rotation.

**Étape 3.** Mesurer la distance entre les deux points obtenus.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Croire que la composition commute et n'appliquer qu'un ordre. Une rotation autour de l'ORIGINE emporte la translation déjà faite ; appliquée après, elle ne la touche pas. 514 mm d'écart sur un bras de 1,2 m, c'est un point d'ancrage qui tombe à côté du poteau.

### Pièges fréquents

- N'appliquer qu'un ordre.
- Tourner autour du point plutôt qu'autour de l'origine.

### Pourquoi ce jeu de données

Un angle de 35° et une translation du même ordre de grandeur que le bras : les deux résultats sont tous deux plausibles, et 514 mm d'écart ne se voit pas sur un aperçu à l'échelle du bâtiment.

### Limite de la correction automatique

> L'exercice mesure l'écart entre deux ordres. Lequel est le bon dépend de ce que décrit le mécanisme — et c'est au plan de le dire, pas au calcul de le deviner.

### Pour aller plus loin

- Chercher la translation qui rendrait les deux ordres équivalents.
- Reprendre avec une rotation autour du point lui-même.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `GP-12_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `GP-12_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `GP-12.json` | Descripteur pour le plugin Magpie |
| `GP-12_fiche.md` | La présente fiche |
| `GP-12_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `GP-12_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `GP-12_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
