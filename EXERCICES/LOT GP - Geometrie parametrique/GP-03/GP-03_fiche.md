# GP-03 — Un maillage qu'on peut imprimer

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP3 · Maillages et SubD |
| **Référence au référentiel** | REF-074, REF-075, REF-076 |
| **Compétence visée** | Produire un maillage à partir d'une surface, en maîtriser la finesse, et le rendre exploitable. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | RH-08 |
| **Mode de validation** | NumericTolerance — tolérance 5 % |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire un maillage à partir d'une surface, en maîtriser la finesse, et le rendre exploitable.

### Contexte

Une pièce de forme libre part en impression : le trancheur n'accepte qu'un maillage fermé, et la finesse décide de la qualité comme du poids du fichier.

### Énoncé

> La surface fournie doit devenir un maillage fermé dont l'écart à la surface d'origine ne dépasse nulle part 0,2 mm. Donnez le nombre de faces du maillage obtenu.

### Ce qui vous est fourni

Un fichier contenant la surface fermée d'origine.

### Ce qui est attendu

1 024 faces avec les réglages par défaut du mailleur — la correction accepte 5 % autour de cette valeur.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 5 %.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-03_sujet.gh`

### Barème

1 point si l'écart maximal est respecté et le maillage fermé.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `GP-03_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Mailler la surface en fixant l'écart maximal, non la densité.

**Étape 2.** Vérifier que le maillage est fermé et sans face dégénérée.

**Étape 3.** Réparer les jonctions si le maillage sort en morceaux.

**Étape 4.** Compter les faces.

**Étape 5.** Contrôler le poids du fichier exporté : c'est la contrepartie directe de la finesse.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Augmenter la densité jusqu'à ce que « ça ait l'air bien ». L'écart maximal est un réglage explicite : à l'œil, on produit soit un maillage grossier qui passe pour lisse à l'écran, soit un maillage inutilement lourd.

### Pièges fréquents

- Régler la densité au lieu de l'écart : le résultat n'est plus contrôlable.
- Maillage en plusieurs morceaux non joints : il paraît fermé et ne l'est pas.

### Pourquoi ce jeu de données

La surface présente une zone de forte courbure et une zone plane : un maillage à densité uniforme y est toujours mauvais quelque part, ce qui oblige à passer par le critère d'écart.

### Limite de la correction automatique

> Le corrigé maille avec les réglages PAR DÉFAUT, et rend 1 024 faces. Il ne pilote pas l'écart maximal : ce réglage se pose dans la boîte de dialogue de maillage et ne se transporte pas dans le fichier. Le corrigé sert donc d'ordre de grandeur ; c'est au formateur de vérifier que l'apprenant a bien raisonné en écart et non en densité.

### Pour aller plus loin

- Doubler l'écart admis et mesurer le gain en nombre de faces.
- Lisser le maillage et vérifier ce que le lissage fait à l'écart.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `GP-03_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `GP-03_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `GP-03.json` | Descripteur pour le plugin Magpie |
| `GP-03_fiche.md` | La présente fiche |
| `GP-03_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `GP-03_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `GP-03_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
