# G-28 — L'avatar paramétrique

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G6 · Sensations et immersion |
| **Référence au référentiel** | REF-067, REF-106, REF-061 |
| **Compétence visée** | Concevoir un codage qui reste valide sur TOUTES les combinaisons, et le prouver en les parcourant. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 22 min |
| **Prérequis** | B-16, A-31 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 20 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire construire à l'apprenant un objet personnel qu'il retrouvera tout au long du parcours.

### Contexte

L'avatar est un objet que l'apprenant retrouve tout au long du parcours. Il n'a de valeur que s'il ne casse jamais — d'où l'exigence de robustesse sur les soixante-douze combinaisons.

### Énoncé

> Compose ton avatar : 3 formes de corps, 4 motifs, 6 couleurs. Ton avatar doit rester valide dans les 72 combinaisons possibles et son code de configuration doit s'afficher dans le Panel.

### Ce qui vous est fourni

Trois Value List et les bibliothèques de formes et de motifs.

### Ce qui est attendu

16 452 — la somme des soixante-douze codes de configuration.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-28_sujet.gh`

### Barème

2 points : 1 pour la robustesse, 1 pour le code de configuration.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-28_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Sélectionner la forme active avec Stream Filter piloté par la première Value List.

**Étape 2.** Appliquer le motif choisi par la même mécanique.

**Étape 3.** Appliquer la couleur avec un Colour Swatch sélectionné par la troisième Value List.

**Étape 4.** Composer le code avec Concatenate à partir des trois index.

**Étape 5.** Balayer les 72 combinaisons pour vérifier qu'aucune ne produit d'erreur.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Vérifier son avatar sur la seule combinaison choisie. Un codage qui marche sur 1-1-1 et casse sur 3-4-6 passe tous les contrôles visuels — c'est la définition même d'une régression, et la somme des 72 codes est le seul moyen simple de l'exclure.

### Pièges fréquents

- Value List renvoyant du texte plutôt qu'un entier : Stream Filter échoue.
- Combinaisons non testées : certaines produisent une géométrie invalide.

### Pourquoi ce jeu de données

3 formes, 4 motifs, 6 couleurs, code = forme×100 + motif×10 + couleur : les codes vont de 111 à 346 sans collision, et leur somme 16 452 n'est atteinte que si les soixante-douze sont produits. Il en manque un, la somme le dit.

### Limite de la correction automatique

> La somme prouve que les 72 codes sont PRODUITS, pas que les 72 avatars sont beaux ni même géométriquement valides. La robustesse visuelle se regarde.

### Pour aller plus loin

- Avatar évoluant avec le niveau atteint.
- Avatar exporté en image pour le certificat.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-28_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-28_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-28.json` | Descripteur pour le plugin Magpie |
| `G-28_fiche.md` | La présente fiche |
| `G-28_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-28_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-28_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
