# B-05 — Poutre treillis paramétrique

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B1 · Architecture et construction |
| **Référence au référentiel** | REF-046, REF-063, REF-079 |
| **Compétence visée** | Chiffrer le linéaire d'une structure treillis en distinguant ce qui court le long de la portée de ce qui la traverse en diagonale. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-16, A-47 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 22 composants |
| **Gamification associée** | G-21 Golf de composants |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Construire une structure par décalage de listes et produire directement son métré.

### Contexte

Le tube se commande au mètre. Une diagonale n'a pas la longueur du panneau qu'elle traverse.

### Énoncé

> Produis une poutre treillis Warren de 12 000 mm de portée et 900 mm de hauteur, avec 8 panneaux. Affiche le linéaire total de tube nécessaire, membrures et diagonales séparées.

### Ce qui vous est fourni

Trois sliders : portée, hauteur, nombre de panneaux.

### Ce qui est attendu

37,99 m de tube pour les membrures et les diagonales, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-05_sujet.gh`

### Barème

2 points pour la géométrie, 2 points pour les deux linéaires.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-05_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Générer les abscisses des nœuds avec Range sur la portée.

**Étape 2.** Construire la membrure basse (Z = 0) et la membrure haute (Z = 900) par Construct Point.

**Étape 3.** Relier chaque nœud au suivant avec Shift List + Line pour les deux membrures.

**Étape 4.** Pour les diagonales, alterner nœud bas i vers nœud haut i+1 puis nœud haut i+1 vers nœud bas i+2 : utiliser Cull Pattern ou Weave.

**Étape 5.** Transformer les lignes en Pipe avec deux diamètres distincts.

**Étape 6.** Mesurer les longueurs avec Length puis Mass Addition sur chaque famille.

**Étape 7.** Afficher les deux linéaires dans un Panel.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter la diagonale comme un panneau : on obtient 36,00 m. Une diagonale sur un panneau de 1 500 mm et 900 mm de hauteur mesure 1 749 mm, pas 1 500 — et il y en a huit. Deux mètres de tube manquent à la livraison.

### Pièges fréquents

- Shift List sans Wrap : la dernière barre manque ou la première est en trop.
- Alternance des diagonales mal construite : on obtient un treillis Pratt et non Warren.
- Compter deux fois les nœuds partagés dans le métré.

### Pourquoi ce jeu de données

Portée de 12 000 mm en 8 panneaux de 1 500, hauteur 900 : la diagonale fait 1 749,3 mm, soit 17 % de plus que le pas. L'écart est assez petit pour qu'on l'oublie, assez grand pour manquer sur un chantier.

### Limite de la correction automatique

> Le linéaire annoncé ne compte pas les montants verticaux, qui dépendent du schéma retenu — un Warren strict n'en a pas, un Warren à montants en a neuf.

### Pour aller plus loin

- Passer d'un treillis Warren à un treillis Pratt par un simple changement de motif.
- Exporter la nomenclature des barres vers Excel.
- Faire varier la hauteur pour obtenir une poutre à inertie variable.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-05_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-05_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-05.json` | Descripteur pour le plugin Magpie |
| `B-05_fiche.md` | La présente fiche |
| `B-05_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-05_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-05_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
