# A-14 — Filtrer avec Cull Pattern

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A3 · Listes |
| **Référence au référentiel** | REF-045 |
| **Compétence visée** | Éliminer les éléments d'une liste selon un motif régulier. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-13 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-13 Casino — motifs assortis |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Éliminer les éléments d'une liste selon un motif régulier.

### Contexte

Un bardage à claire-voie se pose en déposant une lame sur trois du calepinage plein.

### Énoncé

> Le calepinage plein comporte 36 lames. Produisez la liste des lames réellement posées, sachant qu'on conserve la première puis une sur trois.

### Ce qui vous est fourni

Le calepinage plein : les 36 longueurs de lames, en millimètres.

### Ce qui est attendu

La liste ordonnée des longueurs des lames réellement posées.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-14_sujet.gh`

### Barème

1 point si les 4 bons éléments sont conservés.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-14_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 12 longueurs : les rangs 0, 3, 6, … 33 du calepinage.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Poser Cull Pattern (Sets > Sequence).

**Étape 2.** Dans un Panel, saisir le motif True, False, False sur trois lignes.

**Étape 3.** Relier le Panel sur l'entrée Pattern et la liste sur List.

**Étape 4.** Le motif se répète cycliquement sur toute la liste.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Décaler le motif d'un cran et commencer par déposer la première lame : on obtient encore 12 lames, mais pas les mêmes. L'effectif seul ne suffit donc pas à valider — c'est pourquoi la réponse porte sur les longueurs conservées.

### Pièges fréquents

- Saisir le motif sur une seule ligne : Grasshopper lit un seul élément.
- Confondre Cull Pattern (motif cyclique) et Cull Index (index explicites).

### Pourquoi ce jeu de données

36 lames de longueurs voisines mais toutes distinctes : un décalage du motif conserve l'effectif de 12 tout en changeant la réponse. C'est pourquoi la validation porte sur les longueurs et non sur le seul comptage.

### Note au formateur

> Un seul composant fait le travail. À terme, mieux vaut l'absorber dans un exercice de calepinage complet que le maintenir isolé.

### Pour aller plus loin

- Inverser le motif pour conserver les deux autres tiers.
- Piloter le motif par une comparaison numérique.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-14_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-14_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-14.json` | Descripteur pour le plugin Magpie |
| `A-14_fiche.md` | La présente fiche |
| `A-14_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-14_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-14_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
