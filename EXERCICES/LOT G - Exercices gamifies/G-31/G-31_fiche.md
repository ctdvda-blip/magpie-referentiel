# G-31 — L'arbre de compétences

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G7 · Régularité et communauté |
| **Référence au référentiel** | REF-048, REF-051 |
| **Compétence visée** | Croiser deux séries — ce qui est requis, ce qui est acquis — et compter ce qui est complet. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 15 min |
| **Prérequis** | A-19, A-22 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 22 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Donner à l'apprenant une vue d'ensemble de son avancement et des chemins possibles.

### Contexte

L'arbre de compétences donne à l'apprenant la vue d'ensemble qui manque toujours : ce qu'il a fait, ce qu'il lui reste, et par où passer.

### Énoncé

> Construis la représentation graphique de ton propre arbre de compétences à partir de la liste des exercices validés : un nœud par notion, une branche par domaine, un code couleur par niveau atteint.

### Ce qui vous est fourni

La liste des exercices validés exportée par Magpie et la structure du référentiel.

### Ce qui est attendu

21 notions entièrement acquises.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-31_sujet.gh`

### Barème

4 points : 2 pour la structure, 2 pour la lisibilité.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-31_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Lire le fichier de résultats et en extraire les identifiants d'exercices validés.

**Étape 2.** Rattacher chaque identifiant à son domaine et à sa catégorie via la table du référentiel.

**Étape 3.** Construire l'arbre de données correspondant avec Entwine puis Path Mapper.

**Étape 4.** Placer un nœud par notion sur un cercle par domaine.

**Étape 5.** Relier les nœuds à leur domaine avec Line et colorer selon le niveau atteint.

**Étape 6.** Étiqueter chaque nœud avec Text Tag 3D.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter les notions ENTAMÉES — celles où au moins un exercice est validé — au lieu des notions complètes : 37 au lieu de 21. L'arbre paraît alors aux trois quarts vert alors qu'il est à 44 %, et l'apprenant se croit plus avancé qu'il n'est.

### Pièges fréquents

- Structure d'arbre construite à plat : les domaines se mélangent.
- Nœuds superposés faute d'avoir réparti les angles selon le nombre de notions par domaine.

### Pourquoi ce jeu de données

Quarante-huit notions portant de 1 à 4 exercices, avec de 0 à 4 validés. Une notion peut avoir PLUS de validés que d'exercices portés — cas réel d'un exercice retiré du référentiel — et la comparaison doit rester « au moins », pas « exactement ».

### Limite de la correction automatique

> Le compte se vérifie ; la LISIBILITÉ de l'arbre — la moitié du barème — non. Un nœud par notion et une branche par domaine se jugent à l'œil, comme tout dessin.

### Pour aller plus loin

- Arbre mis à jour automatiquement après chaque parcours.
- Comparaison avec la moyenne de la promotion.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-31_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-31_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-31.json` | Descripteur pour le plugin Magpie |
| `G-31_fiche.md` | La présente fiche |
| `G-31_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-31_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-31_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
