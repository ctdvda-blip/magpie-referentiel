# A-27 — Construire une chaîne de caractères

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A6 · Outils de texte |
| **Référence au référentiel** | REF-057 |
| **Compétence visée** | Composer un libellé exploitable à partir de valeurs numériques et de fragments de texte. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-11 |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-11 Mots croisés de composants |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Composer un libellé exploitable à partir de valeurs numériques et de fragments de texte.

### Contexte

Chaque pièce débitée part à l'atelier avec une étiquette portant son repère et sa longueur.

### Énoncé

> Les numéros et les longueurs des 5 pièces vous sont fournis dans deux listes. Produisez les cinq étiquettes au format « PIECE-01 : 1250 mm », le numéro étant cadré sur deux chiffres.

### Ce qui vous est fourni

Deux listes internalisées : 5 numéros et 5 longueurs.

### Ce qui est attendu

Cinq libellés au format demandé.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **Visuel**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-27_sujet.gh`

### Barème

1 point si les 5 libellés sont exacts.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-27_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Formater le numéro sur deux chiffres avec Format (masque {0:00}).

**Étape 2.** Poser Concatenate et brancher successivement PIECE-, le numéro formaté, le séparateur, la longueur et l'unité.

**Étape 3.** Zoomer sur Concatenate pour ajouter des entrées si nécessaire.

**Étape 4.** Relier vers un Panel et contrôler les espaces.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Livrer « PIECE-1 » au lieu de « PIECE-01 » : le cadrage sur deux chiffres saute, et le tri alphabétique des étiquettes à l'atelier place la pièce 10 avant la pièce 2.

### Pièges fréquents

- Oublier les espaces autour du deux-points.
- Concaténer un nombre décimal sans le formater : 1250,0 s'affiche.

### Limite de la correction automatique

> Le livrable de cet exercice est un texte, et le checker Magpie ne sait comparer que des nombres. La validation est donc visuelle : le formateur lit les cinq étiquettes. Ramener la réponse à un nombre — un total de caractères, par exemple — serait une gymnastique imposée par l'outil et non une étape de la tâche ; la skill le déconseille explicitement.

### Pour aller plus loin

- Produire un libellé multiligne avec Text Join et un séparateur retour ligne.
- Utiliser ces libellés comme texte de cotation dans Rhino.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-27_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-27_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-27.json` | Descripteur pour le plugin Magpie |
| `A-27_fiche.md` | La présente fiche |
| `A-27_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-27_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-27_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
