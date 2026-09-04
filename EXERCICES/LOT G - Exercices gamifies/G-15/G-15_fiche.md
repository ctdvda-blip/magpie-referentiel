# G-15 — Le dessin à compléter

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G3 · Manipulation et adresse |
| **Référence au référentiel** | REF-063, REF-067 |
| **Compétence visée** | Reconstituer une figure par symétrie et la refermer, puis mesurer ce qu'on a produit. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 14 min |
| **Prérequis** | A-34, A-38 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Reconstituer une figure par déduction géométrique.

### Contexte

La silhouette à compléter fait travailler la déduction géométrique : ce qui manque se déduit de ce qui est là, sans cote supplémentaire.

### Énoncé

> La moitié gauche du motif est dessinée. Complète la moitié droite pour obtenir une figure parfaitement symétrique, puis referme le contour.

### Ce qui vous est fourni

Une demi-figure internalisée et un axe de symétrie.

### Ce qui est attendu

91 550 mm² d'aire et 1 098,42 mm de périmètre.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-15_sujet.gh`

### Barème

1 point pour la symétrie, 1 point pour la fermeture.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-15_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Mirror avec le plan de symétrie fourni.

**Étape 2.** Vérifier que la copie miroir se raccorde exactement à l'original.

**Étape 3.** Poser Join Curves pour souder les deux moitiés.

**Étape 4.** Contrôler la fermeture avec un composant de test de courbe fermée.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Reproduire la moitié droite en la DÉCALANT au lieu de la symétriser : la figure obtenue a le même périmètre mais une aire nulle ou doublée selon le sens. C'est pourquoi les deux mesures sont demandées — le périmètre seul ne distingue pas une symétrie d'une translation.

### Pièges fréquents

- Plan de symétrie décalé : un décrochement apparaît à la jonction.
- Join Curves sans tolérance suffisante : le contour reste ouvert.

### Pourquoi ce jeu de données

Six sommets à gauche, dont deux sur l'axe : la moitié droite n'en compte que quatre, et recopier les six produit deux sommets en double sur l'axe. L'aire ne bouge pas, le périmètre si — le contrôle croisé attrape le cas.

### Limite de la correction automatique

> Aire et périmètre ne disent pas que la figure est SYMÉTRIQUE : une figure quelconque de mêmes mesures les satisferait. Ils disent qu'elle est fermée et de la bonne taille, ce qui écarte les erreurs réellement rencontrées.

### Pour aller plus loin

- Symétrie centrale plutôt qu'axiale.
- Figure à compléter par rotation d'ordre 5.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-15_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-15_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-15.json` | Descripteur pour le plugin Magpie |
| `G-15_fiche.md` | La présente fiche |
| `G-15_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-15_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-15_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
