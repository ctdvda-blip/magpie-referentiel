# G-08 — La série de bonnes réponses

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G1 · Progression et récompense |
| **Référence au référentiel** | REF-044, REF-045, REF-046 |
| **Compétence visée** | Enchaîner huit manipulations de listes sans rompre la série, chacune portant sur une propriété différente du même jeu. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 16 min |
| **Prérequis** | A-13, A-14, A-16 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 20 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Récompenser la régularité plutôt que le coup de chance.

### Contexte

Le multiplicateur de série récompense la régularité plutôt que le coup de chance. Sept bonnes réponses suivies d'une erreur valent moins que huit réponses moyennes enchaînées.

### Énoncé

> Huit manipulations de listes s'enchaînent. Chaque bonne réponse consécutive augmente le multiplicateur : ×1, ×1,5, ×2, ×3. Une erreur remet le multiplicateur à ×1.

### Ce qui vous est fourni

Huit listes internalisées et huit paramètres de réponse.

### Ce qui est attendu

Les huit réponses : 11, 962, 69, 7 133, 404, 1 119, 5, 1 348.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-08_sujet.gh`

### Barème

8 points de base, jusqu'à 24 points avec multiplicateur.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-08_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Traiter les huit consignes dans l'ordre imposé par le Scribble.

**Étape 2.** Vérifier chaque résultat dans un Panel avant de brancher la réponse.

**Étape 3.** Ne soumettre qu'une fois l'ensemble contrôlé.

**Étape 4.** Observer le multiplicateur monter dans le panneau de score.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Prendre le médian d'une liste de 16 éléments sans la TRIER d'abord : on rend l'élément de rang 8 de la liste brute, 857 au lieu de 404 — plus du double. Le médian est une valeur de la liste ORDONNÉE, et la série se casse sur cette seule réponse.

### Pièges fréquents

- Traiter les listes dans le désordre : la série se casse.
- Confondre Cull Pattern et Cull Index sur la manipulation 4.

### Pourquoi ce jeu de données

Seize valeurs de 10 à 990. Les huit résultats sont deux à deux DISTINCTS — 11 pairs, 5 au-dessus de 500, médian 404 — de sorte qu'une confusion entre deux questions se voit. Le jeu a été choisi pour que l'élément brut de rang 8 (857) diffère nettement du médian (404) : sans quoi le piège de la cinquième question serait muet.

### Limite de la correction automatique

> Le multiplicateur est une mécanique de SCORE : il ne change ni la validation ni la difficulté. Un apprenant qui reprend depuis le début obtient le même verdict, avec moins de points.

### Pour aller plus loin

- Série conservée d'une session à l'autre.
- Bonus de série sur toute une thématique.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-08_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-08_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-08.json` | Descripteur pour le plugin Magpie |
| `G-08_fiche.md` | La présente fiche |
| `G-08_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-08_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-08_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
