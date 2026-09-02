# B-08 — Étagère modulaire à pas variable

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B2 · Design de mobilier |
| **Référence au référentiel** | REF-043, REF-044, REF-047 |
| **Compétence visée** | Répartir des éléments selon une progression imposée en respectant une hauteur totale et une valeur de départ. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 22 min |
| **Prérequis** | A-13, A-10 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 16 composants |
| **Gamification associée** | G-08 Combo / série |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Répartir des tablettes selon une progression non uniforme pilotée par une courbe.

### Contexte

Une bibliothèque range des livres de plus en plus grands vers le haut. La hauteur totale, elle, ne bouge pas.

### Énoncé

> Répartis 6 tablettes sur une hauteur de 2 000 mm de sorte que les entre-deux augmentent progressivement du bas vers le haut, la plus petite hauteur libre valant au moins 220 mm.

### Ce qui vous est fourni

Un slider de hauteur totale et un slider de nombre de tablettes.

### Ce qui est attendu

353,71 mm — le plus grand entre-deux, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-08_sujet.gh`

### Barème

2 points pour la répartition, 1 point pour la contrainte de 220 mm.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-08_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Générer une série normalisée de 0 à 1 avec Range.

**Étape 2.** Passer cette série dans un Graph Mapper réglé en courbe puissance.

**Étape 3.** Remapper le résultat sur le domaine 0 à 2000 : les positions se resserrent en bas.

**Étape 4.** Poser les tablettes à ces altitudes avec Move.

**Étape 5.** Calculer les entre-deux par Shift List et soustraction, puis retirer l'épaisseur de tablette.

**Étape 6.** Contrôler la valeur minimale avec Bounds et un Larger Than.

**Étape 7.** Afficher les hauteurs libres dans un Panel.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Oublier l'épaisseur des tablettes et répartir 2 000 mm au lieu des 1 868 mm réellement libres : le plus grand entre-deux monte à 378,3 mm, et la dernière tablette dépasse du meuble de 132 mm.

### Pièges fréquents

- Oublier de retirer l'épaisseur des tablettes pour obtenir la hauteur libre.
- Graph Mapper non internalisé : la courbe se réinitialise à l'ouverture du fichier.
- Contrainte de 220 mm vérifiée sur les entraxes et non sur les vides.

### Pourquoi ce jeu de données

Six tablettes de 22 mm laissent 1 868 mm libres à répartir en sept entre-deux, le plus petit valant 180 mm. La raison de la progression tombe sur 28,95 mm — jamais un compte rond, donc jamais devinable.

### Pour aller plus loin

- Inverser la progression du haut vers le bas.
- Imposer un nombre entier de modules standards.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-08_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-08_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-08.json` | Descripteur pour le plugin Magpie |
| `B-08_fiche.md` | La présente fiche |
| `B-08_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-08_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-08_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
