# A-20 — Graft et Flatten

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A4 · Arbres de données |
| **Référence au référentiel** | REF-049, REF-052 |
| **Compétence visée** | Modifier la structure d'un flux pour obtenir un croisement complet plutôt qu'un appariement terme à terme. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-19 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-22 Boss de fin de chapitre |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Modifier la structure d'un flux pour obtenir un croisement complet plutôt qu'un appariement terme à terme.

### Contexte

Une passerelle est haubanée : chaque ancrage de rive doit être relié à chaque ancrage de mât, et non au seul ancrage de même rang.

### Énoncé

> Trois ancrages de rive et trois ancrages de mât vous sont fournis. Le tracé livre aujourd'hui trois haubans, un par paire de même rang. Obtenez les neuf haubans de toutes les combinaisons possibles, sans dupliquer le composant de tracé.

### Ce qui vous est fourni

Deux listes de 3 points internalisées, reliées par un Line.

### Ce qui est attendu

Neuf segments.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-20_sujet.gh`

### Barème

1 point si 9 segments sont produits.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-20_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Vérifier l'état initial : 3 segments seulement (correspondance un à un).

**Étape 2.** Clic droit sur l'entrée A du Line > Graft : chaque point part dans sa propre branche.

**Étape 3.** Grasshopper croise alors chaque branche de A avec la liste complète de B : 9 segments.

**Étape 4.** Ajouter un Flatten en sortie et observer que les 9 segments retombent dans une seule liste.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Dupliquer le tracé et le brancher trois fois : on obtient neuf segments par force brute, et un montage qui ne tiendra pas à quatre ancrages. La contrainte d'un seul composant ferme cette voie sans nommer la solution.

### Pièges fréquents

- Grafter les deux entrées : on retombe à 3 segments.
- Confondre Graft (éclate en branches) et Flatten (aplatit).

### Note au formateur

> Le geste tient en une option de menu contextuel. L'intérêt est dans la conséquence sur le résultat, ce que l'énoncé exploite déjà ; surveiller qu'il ne se réduise pas à « savoir où cliquer ».

### Pour aller plus loin

- Obtenir le même résultat avec Cross Reference.
- Grafter une liste de courbes avant un Divide Curve.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-20_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-20_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-20.json` | Descripteur pour le plugin Magpie |
| `A-20_fiche.md` | La présente fiche |
| `A-20_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-20_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-20_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
