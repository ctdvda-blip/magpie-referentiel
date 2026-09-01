# A-22 — Construire un arbre

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A4 · Arbres de données |
| **Référence au référentiel** | REF-048, REF-051 |
| **Compétence visée** | Assembler plusieurs listes en un flux structuré, puis en réextraire chaque groupe. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-21 |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-14 Puzzle de câblage |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Assembler plusieurs listes en un flux structuré, puis en réextraire chaque groupe.

### Contexte

Trois lots de fabrication doivent voyager ensemble dans la définition tout en restant distincts à l'arrivée.

### Énoncé

> Trois listes de longueurs différentes vous sont fournies. Faites-les circuler dans un flux unique où chacune reste un groupe séparé, puis récupérez les trois listes d'origine à l'identique.

### Ce qui vous est fourni

Trois listes internalisées de 2, 5 et 3 éléments.

### Ce qui est attendu

Un flux à trois branches, puis trois sorties identiques aux listes de départ.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SetEquality**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-22_sujet.gh`

### Barème

1 point pour l'arbre, 1 point pour la décomposition.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-22_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Entwine et brancher les trois listes sur trois entrées.

**Étape 2.** Vérifier au Param Viewer : trois branches de 2, 5 et 3 éléments.

**Étape 3.** Poser Explode Tree en aval et zoomer pour faire apparaître les sorties.

**Étape 4.** Chaque sortie restitue la liste d'origine.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Obtenir moins de sorties que de groupes : le composant de décomposition n'expose que le nombre de sorties qu'on lui a demandé, et perd silencieusement le reste.

### Pièges fréquents

- Merge à la place d'Entwine : les trois listes fusionnent en une seule.
- Explode Tree n'affiche ses sorties qu'après un zoom suffisant.

### Note au formateur

> Assembler puis redécomposer reste un aller-retour scolaire. En parcours, lui donner une finalité : trois lots qui doivent rester distincts jusqu'à l'export.

### Pour aller plus loin

- Entwiner des géométries de types différents.
- Renommer les chemins produits avec Path Mapper.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-22_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-22_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-22.json` | Descripteur pour le plugin Magpie |
| `A-22_fiche.md` | La présente fiche |
| `A-22_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-22_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-22_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
