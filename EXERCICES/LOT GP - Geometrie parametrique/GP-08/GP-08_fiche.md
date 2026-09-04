# GP-08 — Ce que coûte une subdivision de plus

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP4 · Maillages et SubD |
| **Référence au référentiel** | REF-077, REF-078 |
| **Compétence visée** | Anticiper la croissance d'une surface de subdivision, et choisir le niveau d'affichage en connaissance de cause. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 20 min |
| **Prérequis** | GP-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Anticiper la croissance d'une surface de subdivision, et choisir le niveau d'affichage en connaissance de cause.

### Contexte

La cage de subdivision est légère et se manipule bien. C'est l'affichage lissé qui fait ramer la machine.

### Énoncé

> La cage compte 26 faces. Chaque passe de subdivision remplace chaque face par quatre. Donnez le nombre de faces après trois passes.

### Ce qui vous est fourni

Le nombre de faces de la cage et le nombre de passes.

### Ce qui est attendu

1 664 faces après trois passes.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-08_sujet.gh`

### Barème

1 point si le nombre de faces est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `GP-08_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Comprendre que la croissance est géométrique.

**Étape 2.** Élever quatre à la puissance du nombre de passes.

**Étape 3.** Multiplier par le nombre de faces de la cage.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Multiplier une seule fois par quatre (104), ou multiplier par trois (78). La croissance est GÉOMÉTRIQUE : chaque passe quadruple ce que la précédente a produit. C'est pour cela qu'une passe de plus, décidée sans y penser, fait passer un modèle fluide à un modèle inutilisable.

### Pièges fréquents

- Multiplier par le nombre de passes.
- N'appliquer le facteur qu'une fois.

### Pourquoi ce jeu de données

26 faces est la taille d'une cage de mobilier. Les trois réponses possibles — 78, 104 et 1 664 — sont séparées d'un ordre de grandeur, ce qui rend chaque erreur immédiatement lisible.

### Limite de la correction automatique

> 1 664 faces est un compte de TOPOLOGIE, pas de coût. Le poids réel d'une subdivision dépend aussi de ce qui est calculé sur chaque face — aperçu, matériau, analyse — et deux cages de même compte peuvent tenir ou saturer selon ce qui les suit.

### Pour aller plus loin

- Trouver le nombre de passes qui dépasse cent mille faces.
- Comparer au coût d'affichage d'un maillage équivalent.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `GP-08_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `GP-08_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `GP-08.json` | Descripteur pour le plugin Magpie |
| `GP-08_fiche.md` | La présente fiche |
| `GP-08_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `GP-08_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `GP-08_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
