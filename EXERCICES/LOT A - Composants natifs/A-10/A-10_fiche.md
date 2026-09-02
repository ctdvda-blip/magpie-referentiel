# A-10 — Series et Range

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A3 · Listes |
| **Référence au référentiel** | REF-043, REF-047 |
| **Compétence visée** | Produire une suite régulière de positions à partir d'un pas et d'un nombre d'intervalles. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-01 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-07 Étoiles de performance |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire une suite régulière de positions à partir d'un pas et d'un nombre d'intervalles.

### Contexte

Les axes de portique d'une halle sont espacés régulièrement le long d'une file.

### Énoncé

> La halle compte 7 portiques espacés de 5 400 mm, le premier à l'origine de la file. Produisez la liste des abscisses des 7 axes.

### Ce qui vous est fourni

Canvas vide.

### Ce qui est attendu

La liste ordonnée des abscisses des axes, en millimètres, du premier au dernier.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-10_sujet.gh`

### Barème

2 points : 1 par suite correcte.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-10_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 0, 5400, 10800, 16200, 21600, 27000, 32400.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Series : Start = 10, Step = 5, Count = 5.

**Étape 2.** Range : Domain = 10 To 30 (Construct Domain), Steps = 4.

**Étape 3.** Relier chaque sortie vers un Panel.

**Étape 4.** Retenir : Series raisonne en pas et nombre d'éléments, Range en domaine et subdivisions.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Produire 7 intervalles au lieu de 7 axes, et donc 8 valeurs : la confusion entre le nombre d'éléments et le nombre d'espaces entre eux, qui se paie d'un portique en trop sur le chantier.

### Pièges fréquents

- Range avec Steps = 5 produit 6 valeurs, pas 5.
- Oublier Construct Domain et saisir le domaine dans un Panel.

### Pour aller plus loin

- Produire une suite décroissante avec un pas négatif.
- Générer 5 valeurs entre 0 et 1 pour piloter un paramètre normalisé.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-10_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-10_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-10.json` | Descripteur pour le plugin Magpie |
| `A-10_fiche.md` | La présente fiche |
| `A-10_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-10_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-10_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
