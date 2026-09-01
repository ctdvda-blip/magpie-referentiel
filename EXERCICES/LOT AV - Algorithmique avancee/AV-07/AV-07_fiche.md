# AV-07 — Les solutions qu'on ne peut pas départager

**Fiche d'exercice Magpie** · Lot AV — Algorithmique avancée

| | |
|---|---|
| **Thématique** | AV2 · Design génératif |
| **Référence au référentiel** | REF-154 |
| **Compétence visée** | Distinguer, parmi des solutions, celles qu'aucune autre ne surpasse sur tous les critères à la fois. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | AV-06 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 10 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Distinguer, parmi des solutions, celles qu'aucune autre ne surpasse sur tous les critères à la fois.

### Contexte

L'optimisation a rendu huit variantes. Aucune n'est la meilleure partout : c'est le principe, et c'est ce qui reste à arbitrer.

### Énoncé

> Les huit solutions vous sont fournies avec leur coût, à minimiser, et leur performance, à maximiser. Donnez le nombre de solutions qu'aucune autre ne surpasse sur les deux critères à la fois.

### Ce qui vous est fourni

Les huit solutions, leur coût et leur performance.

### Ce qui est attendu

5 solutions ne sont surpassées par aucune autre.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`AV-07_sujet.gh`

### Barème

1 point si le nombre de solutions non surpassées est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `AV-07_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Pour chaque solution, chercher s'il en existe une autre au moins aussi bonne partout et strictement meilleure quelque part.

**Étape 2.** Si oui, elle est surpassée.

**Étape 3.** Compter celles qui ne le sont pas.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Chercher LA meilleure et n'en garder qu'une — la moins chère, ou la plus performante. Les deux existent, elles ne sont pas la même, et trois autres solutions restent défendables. Réduire un arbitrage à un classement, c'est décider à la place du projeteur sans le lui dire.

### Pièges fréquents

- Ne garder que l'extrême d'un critère.
- Oublier qu'une solution ne se surpasse pas elle-même.
- Traiter « au moins aussi bon » comme « meilleur ».

### Pourquoi ce jeu de données

Huit solutions dont trois sont réellement surpassées : pour chacune, il existe une autre à la fois moins chère ET plus performante. Les cinq restantes forment le front, et le fait qu'elles soient majoritaires est le message — une optimisation ne réduit pas le choix, elle l'éclaire.

### Limite de la correction automatique

> L'exercice porte sur deux critères. À trois ou plus, le front grossit vite et cesse d'être lisible : c'est le moment où il faut hiérarchiser les critères, et cela ne se calcule pas.

### Pour aller plus loin

- Nommer les trois solutions écartées et dire par laquelle.
- Ajouter un troisième critère et observer le front grossir.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `AV-07_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `AV-07_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `AV-07.json` | Descripteur pour le plugin Magpie |
| `AV-07_fiche.md` | La présente fiche |
| `AV-07_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `AV-07_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `AV-07_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
