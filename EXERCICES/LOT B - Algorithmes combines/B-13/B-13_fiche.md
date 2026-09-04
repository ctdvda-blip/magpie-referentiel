# B-13 — Calepinage de plaques et calcul de chute

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B4 · Données, métrés et livrables |
| **Référence au référentiel** | REF-113, REF-082, REF-045 |
| **Compétence visée** | Estimer un taux de chute à partir des surfaces, en sachant que c'est un MINORANT et pourquoi. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 28 min |
| **Prérequis** | B-12, A-15 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 20 composants |
| **Gamification associée** | G-23 Duel et classement |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Optimiser un débit et quantifier la perte matière.

### Contexte

La plaque se commande à l'unité. Le taux de chute décide de la marge, et il est toujours annoncé optimiste.

### Énoncé

> Les 22 pièces rectangulaires fournies doivent être débitées dans des plaques de 2 800 × 2 070 mm. Calcule le nombre de plaques nécessaires et le taux de chute en pourcentage.

### Ce qui vous est fourni

Une liste de 22 rectangles et les dimensions de plaque.

### Ce qui est attendu

31,00 % de chute, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-13_sujet.gh`

### Barème

2 points pour le calepinage, 1 point pour le nombre de plaques, 1 point pour le taux de chute.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-13_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Mesurer l'aire de chaque pièce avec Area puis sommer avec Mass Addition.

**Étape 2.** Calculer l'aire d'une plaque : 2800 × 2070.

**Étape 3.** Diviser l'aire totale des pièces par l'aire d'une plaque et arrondir à l'entier supérieur : nombre théorique minimal.

**Étape 4.** Placer les pièces par un calepinage simple en bandes (tri par hauteur décroissante puis remplissage ligne par ligne).

**Étape 5.** Compter le nombre réel de plaques utilisées.

**Étape 6.** Calculer le taux de chute : 1 − (aire des pièces / aire des plaques utilisées).

**Étape 7.** Afficher les deux valeurs et signaler l'écart avec le minimum théorique.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Annoncer ce taux comme celui du débit réel. Il ne compte que la surface : le placement, lui, ajoute sa propre chute, et le taux observé en atelier est toujours supérieur. Un devis calé sur 31 % perd de l'argent à chaque plaque.

### Pièges fréquents

- Confondre le minimum théorique et le nombre réellement atteignable.
- Oublier le trait de scie entre les pièces.
- Ne pas gérer les pièces plus grandes que la plaque.

### Pourquoi ce jeu de données

22 pièces pour 12,00 m² dans des plaques de 5,80 m² : trois plaques suffisent en surface, d'où 31 % de chute théorique. Le rapport 11 997 500 ÷ 5 796 000 vaut 2,07 — juste au-dessus de deux, ce qui rend l'arrondi au supérieur décisif.

### Limite de la correction automatique

> Le taux calculé est un plancher. Seule une imbrication réelle donne le taux vrai, et FA-01 dit pourquoi aucune ne peut faire mieux que ce plancher.

### Pour aller plus loin

- Ajouter une contrainte de sens de fil du bois.
- Comparer le résultat avec l'imbrication OpenNest.
- Chiffrer le coût matière à partir du prix de plaque.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-13_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-13_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-13.json` | Descripteur pour le plugin Magpie |
| `B-13_fiche.md` | La présente fiche |
| `B-13_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-13_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-13_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
