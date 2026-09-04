# G-13 — La machine à sous des motifs

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G2 · Exploration et découverte |
| **Référence au référentiel** | REF-045, REF-068 |
| **Compétence visée** | Chercher le décalage cyclique qui aligne trois séquences, en raisonnant sur le modulo plutôt que par essais. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 15 min |
| **Prérequis** | A-14, B-03 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 12 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Comprendre la logique des motifs cycliques par une mécanique de rouleaux.

### Contexte

La machine à sous rend tangible la logique des motifs cycliques — celle qui régit `Shift List`, les listes de répétition et tout calepinage à motif alterné.

### Énoncé

> Trois rouleaux affichent chacun une séquence de 8 motifs. Trouve les trois valeurs de décalage qui alignent trois motifs identiques sur la ligne centrale.

### Ce qui vous est fourni

Trois listes de 8 motifs et trois sliders de décalage.

### Ce qui est attendu

Les trois décalages, dans l'ordre : 7, 6, 6.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-13_sujet.gh`

### Barème

3 points, validation sur le triplet exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-13_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Lire les trois séquences dans les Panels fournis.

**Étape 2.** Repérer un motif présent dans les trois séquences.

**Étape 3.** Calculer pour chaque rouleau le décalage amenant ce motif en position centrale.

**Étape 4.** Régler les trois sliders et soumettre le triplet.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Chercher un décalage qui aligne les PREMIÈRES cases plutôt que la ligne centrale. Le centre est en position 3 : décaler pour amener le motif en tête donne trois valeurs fausses de 3, et l'affichage ne montre pas l'erreur puisque les rouleaux tournent quand même.

### Pièges fréquents

- Shift List sans Wrap : les positions extrêmes deviennent inaccessibles.
- Motif présent dans deux séquences seulement.

### Pourquoi ce jeu de données

Neuf motifs répartis sur trois rouleaux de huit, choisis pour qu'UN SEUL motif — le 4 — soit présent dans les trois, et une seule fois dans chacun. La solution est donc unique : avec des rouleaux ordinaires, huit triplets alignent, et la question n'aurait pas de réponse.

### Limite de la correction automatique

> Un seul triplet aligne ici. Une vraie machine à sous en aurait plusieurs, et il faudrait alors demander le plus petit — l'exercice évite cette complication au lieu de la traiter.

### Pour aller plus loin

- Rouleaux animés par un Timer.
- Motifs géométriques plutôt que textuels.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-13_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-13_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-13.json` | Descripteur pour le plugin Magpie |
| `G-13_fiche.md` | La présente fiche |
| `G-13_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-13_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-13_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
