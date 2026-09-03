# B-11 — Chaîne de maillons le long d'une courbe

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B3 · Joaillerie |
| **Référence au référentiel** | REF-064, REF-067, REF-046 |
| **Compétence visée** | Compter des éléments qui se recouvrent, où le pas n'est pas la taille de l'élément. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-35, A-38 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 20 composants |
| **Gamification associée** | G-12 Memory |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Répartir et orienter alternativement des éléments le long d'un parcours.

### Contexte

Les maillons d'une chaîne s'enfilent l'un dans l'autre : le pas est plus court que le maillon, sans quoi la chaîne se casse.

### Énoncé

> Répartis des maillons ovales de 4 mm le long de la courbe fournie, chaque maillon tourné de 90° par rapport au précédent, sans jeu ni recouvrement excessif.

### Ce qui vous est fourni

Une courbe de collier internalisée.

### Ce qui est attendu

66 maillons.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-11_sujet.gh`

### Barème

2 points pour la répartition, 2 points pour l'alternance.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-11_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Divide Length avec un pas égal au pas de maillon (longueur moins recouvrement).

**Étape 2.** Poser Perp Frames pour obtenir un plan par position.

**Étape 3.** Modéliser un maillon de référence dans le plan XY.

**Étape 4.** Orienter le maillon sur chaque plan avec Orient.

**Étape 5.** Séparer les positions paires et impaires avec Cull Pattern (motif True, False).

**Étape 6.** Appliquer une rotation de 90° (π/2) aux maillons impairs avec Rotate Axis.

**Étape 7.** Recombiner les deux familles avec Weave pour retrouver l'ordre initial.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Diviser la longueur par la taille du maillon : 46. Le recouvrement de 1,2 mm ramène le pas à 2,8 mm — il faut donc 43 % de maillons en plus. Une chaîne commandée sur le calcul faux arrive vingt maillons trop courte.

### Pièges fréquents

- Pas de division égal à la longueur du maillon : les maillons ne se touchent pas.
- Recombiner avec Merge au lieu de Weave : l'ordre est perdu.
- Courbe trop courbée : les maillons se coincent.

### Pourquoi ce jeu de données

187,5 mm de courbe, maillons de 4 mm recouverts de 1,2 : le pas tombe à 2,8 mm. Les deux réponses, 46 et 66, sont éloignées de moitié — impossible de confondre les deux méthodes.

### Limite de la correction automatique

> 66 maillons suivent la courbe THÉORIQUE. Une chaîne réelle pend : sa ligne est une chaînette, plus longue que la courbe dessinée, et le compte monte. L'exercice traite le cas guidé, pas le cas suspendu.

### Pour aller plus loin

- Faire varier la taille des maillons selon la position sur la courbe.
- Ajouter un fermoir aux extrémités.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-11_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-11_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-11.json` | Descripteur pour le plugin Magpie |
| `B-11_fiche.md` | La présente fiche |
| `B-11_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-11_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-11_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
