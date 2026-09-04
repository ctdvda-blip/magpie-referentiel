# PL-15 — Combien de plugins pour douze composants

**Fiche d'exercice Magpie** · Lot PL — Écosystème de plugins

| | |
|---|---|
| **Thématique** | PL4 · Plugins fonctionnels |
| **Référence au référentiel** | REF-038, REF-039 |
| **Compétence visée** | Couvrir un besoin en composants par le plus petit nombre de plugins, en exploitant leurs recouvrements. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 22 min |
| **Prérequis** | PL-07 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-21 Le golf de composants |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Couvrir un besoin en composants par le plus petit nombre de plugins, en exploitant leurs recouvrements.

### Contexte

Chaque plugin installé est une dépendance de plus à maintenir, à faire installer par l'apprenant et à revérifier à chaque version de Rhino. On en installe le moins possible.

### Énoncé

> La définition à reprendre emploie douze composants non natifs. Le tableau donne ce qu'apporte chacun des six plugins candidats. Donnez le nombre MINIMAL de plugins à installer pour couvrir les douze.

### Ce qui vous est fourni

La liste des douze composants requis et le tableau des six plugins avec leurs apports.

### Ce qui est attendu

4 plugins suffisent à couvrir les douze composants.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`PL-15_sujet.gh`

### Barème

1 point si le minimum est exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `PL-15_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser les six ensembles d'apports.

**Étape 2.** Écarter d'emblée les plugins dont l'apport est déjà couvert.

**Étape 3.** Chercher la plus petite réunion qui contienne les douze.

**Étape 4.** Vérifier qu'aucun trio n'y parvient.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Installer un plugin par composant manquant — douze, ou les six disponibles « pour être tranquille ». Les plugins se RECOUVRENT : `Mesh Thicken` vient de deux d'entre eux, `Catmull-Clark` aussi, et c'est ce recouvrement qui fait descendre le compte de six à quatre.

### Pièges fréquents

- Compter un plugin par composant.
- Croire la solution unique et rendre une liste de noms.

### Pourquoi ce jeu de données

Six plugins, douze composants, quatre suffisent — et deux quartets différents y parviennent. C'est le NOMBRE qui est demandé, précisément parce qu'il est unique là où la solution ne l'est pas. Aucun trio ne couvre le besoin : la réponse ne s'obtient pas au jugé.

### Limite de la correction automatique

> Le minimum porte sur les COMPOSANTS. Il ignore le poids des plugins, leur stabilité et leur licence : quatre plugins abandonnés valent moins que cinq maintenus, et cet arbitrage-là ne se calcule pas.

### Pour aller plus loin

- Donner le quartet le plus léger en temps de chargement.
- Refaire le calcul en retirant LunchBox du catalogue.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `PL-15_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `PL-15_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `PL-15.json` | Descripteur pour le plugin Magpie |
| `PL-15_fiche.md` | La présente fiche |
| `PL-15_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `PL-15_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `PL-15_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
