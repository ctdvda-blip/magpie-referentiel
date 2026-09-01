# MP-04 — Ce qu'un curseur fait recalculer

**Fiche d'exercice Magpie** · Lot MP — Méthode, performance et évènements

| | |
|---|---|
| **Thématique** | MP1 · Chronologie et évènements |
| **Référence au référentiel** | REF-090 |
| **Compétence visée** | Déterminer ce qu'une modification fait recalculer, en suivant les dépendances plutôt qu'en supposant que tout repasse. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | MP-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-13 Chronomètre |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Déterminer ce qu'une modification fait recalculer, en suivant les dépendances plutôt qu'en supposant que tout repasse.

### Contexte

La définition met trois secondes à répondre au moindre mouvement de curseur. Avant d'optimiser quoi que ce soit, il faut savoir ce qui repasse réellement.

### Énoncé

> Les liaisons du graphe vous sont fournies. Donnez le nombre de composants qui se recalculent lorsque le curseur Largeur est déplacé.

### Ce qui vous est fourni

Les quatorze composants du graphe et leurs liaisons.

### Ce qui est attendu

10 composants se recalculent.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`MP-04_sujet.gh`

### Barème

1 point si le compte des composants recalculés est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `MP-04_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Partir du composant modifié.

**Étape 2.** Suivre les liaisons vers l'aval, de proche en proche.

**Étape 3.** Compter ce qui a été atteint, sans compter deux fois ce que deux branches atteignent.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Répondre 13, tout le graphe moins le curseur. Grasshopper ne recalcule que ce qui DÉPEND de ce qui a changé : Hauteur, Essence et Prix unitaire ne dépendent pas de Largeur, et restent intacts. Croire que tout repasse conduit à optimiser au mauvais endroit.

### Pièges fréquents

- Compter tout le graphe.
- Compter deux fois un composant atteint par deux chemins.
- Remonter vers l'amont : ce qui alimente un composant ne se recalcule pas parce qu'il change.

### Pourquoi ce jeu de données

Quatorze composants, dont trois entrées indépendantes et un graphe à deux branches qui se rejoignent : suivre les dépendances à la main est faisable mais fastidieux, et c'est exactement le genre de comptage qu'on préfère supposer plutôt que faire.

### Limite de la correction automatique

> Le compte des composants n'est pas le compte des secondes : un seul composant lourd pèse plus que neuf légers. C'est le profileur qui le dit, et MP-02 qui l'aborde.

### Pour aller plus loin

- Refaire le compte pour le curseur Essence.
- Trouver l'entrée dont la modification recalcule le moins.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `MP-04_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `MP-04_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `MP-04.json` | Descripteur pour le plugin Magpie |
| `MP-04_fiche.md` | La présente fiche |
| `MP-04_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `MP-04_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `MP-04_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
