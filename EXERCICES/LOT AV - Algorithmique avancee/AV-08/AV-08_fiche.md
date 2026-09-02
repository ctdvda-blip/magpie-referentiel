# AV-08 — Quand la relaxation a-t-elle convergé

**Fiche d'exercice Magpie** · Lot AV — Algorithmique avancée

| | |
|---|---|
| **Thématique** | AV3 · Simulation physique |
| **Référence au référentiel** | REF-155 |
| **Compétence visée** | Établir qu'une simulation s'est stabilisée, en distinguant un passage sous la tolérance d'une stabilisation durable. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | AV-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-20 Contre-expertise |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir qu'une simulation s'est stabilisée, en distinguant un passage sous la tolérance d'une stabilisation durable.

### Contexte

La forme relâchée ne bouge plus à l'écran depuis quelques passes. Le relevé de résidu, lui, raconte autre chose.

### Énoncé

> Le résidu de chacune des dix passes vous est fourni. La tolérance vaut 0,1. Donnez le numéro de la première passe à partir de laquelle le résidu RESTE sous la tolérance.

### Ce qui vous est fourni

Le résidu de chaque passe, et la tolérance.

### Ce qui est attendu

8 — c'est à partir de la huitième passe que le résidu ne remonte plus.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`AV-08_sujet.gh`

### Barème

1 point si le rang de stabilisation durable est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `AV-08_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Comparer chaque résidu à la tolérance.

**Étape 2.** Chercher le premier rang à partir duquel TOUTES les comparaisons suivantes sont vraies.

**Étape 3.** Ne pas s'arrêter au premier passage sous le seuil.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Répondre 6, la première passe sous la tolérance. Le résidu y descend à 0,09, puis REMONTE à 0,13 à la septième : la simulation n'était pas stabilisée, elle passait. S'arrêter là fige une forme qui bougeait encore, et rien à l'écran ne le distingue d'une forme convergée.

### Pièges fréquents

- Prendre la première passe sous la tolérance.
- Prendre la dernière passe du relevé.
- Se fier à l'aperçu, qui ne bouge plus depuis longtemps.

### Pourquoi ce jeu de données

Le résidu descend, franchit la tolérance, la refranchit en sens inverse d'un cheveu — 0,09 puis 0,13 — puis redescend pour de bon. Cette remontée est le cœur de l'exercice, et elle est réaliste : une relaxation oscille avant de se poser. Les deux réponses possibles, 6 et 8, sont toutes deux plausibles à la lecture.

### Limite de la correction automatique

> Rester sous la tolérance sur trois passes n'est pas une preuve de convergence, c'est un faisceau. Une simulation mal contrainte peut se stabiliser sur une forme fausse — le résidu ne dit rien de la justesse du modèle.

### Pour aller plus loin

- Dire ce qu'il faudrait relever de plus pour être sûr.
- Reprendre avec une tolérance de 0,05.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `AV-08_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `AV-08_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `AV-08.json` | Descripteur pour le plugin Magpie |
| `AV-08_fiche.md` | La présente fiche |
| `AV-08_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `AV-08_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `AV-08_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
