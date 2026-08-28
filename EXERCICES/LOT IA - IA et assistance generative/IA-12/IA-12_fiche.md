# IA-12 — Faire construire un graphe par un agent

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA6 · Agents et protocoles |
| **Référence au référentiel** | REF-136, REF-137, REF-138 |
| **Compétence visée** | Faire construire une définition par un agent connecté à Grasshopper, et relever le résultat produit. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 35 min |
| **Prérequis** | IA-07 |
| **Mode de validation** | NumericTolerance — tolérance 0,1 |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-28 Pilotage à distance |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire construire une définition par un agent connecté à Grasshopper, et relever le résultat produit.

### Contexte

Une série de définitions répétitives doit être produite : les monter une à une à la main n'est pas raisonnable.

### Énoncé

> Avec un agent relié à Grasshopper, faites construire une définition qui répartit des points le long d'une courbe et renvoie la longueur cumulée des segments obtenus. Travaillez sur une copie du fichier, et donnez la longueur obtenue.

### Ce qui vous est fourni

Un serveur d'outils relié à Rhino et Grasshopper, en service, et la courbe de référence.

### Ce qui est attendu

Une valeur décimale : la longueur cumulée, en millimètres.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-12_sujet.gh`

### Barème

1 point si la longueur est juste à 0,1 près et si le travail a été mené sur une copie.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-12_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 7 110,8 mm — la longueur de la polyligne inscrite, à 0,1 près.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Enregistrer et dupliquer le fichier avant toute action de l'agent.

**Étape 2.** Vérifier que le serveur d'outils répond avant de formuler la demande.

**Étape 3.** Décrire le résultat attendu, pas la suite de composants à poser : l'agent choisit les moyens.

**Étape 4.** Relire le graphe produit avant de lui faire confiance.

**Étape 5.** Relever la longueur et la contrôler par un calcul indépendant.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Laisser l'agent travailler sur le document ouvert plutôt que sur une copie. Le montage produit peut être juste, mais le travail en cours dans le même document est écrasé sans avertissement — et l'agent ne le signalera pas.

### Pièges fréquents

- Travailler dans le document ouvert.
- Dicter la liste des composants : on retombe alors sur une saisie assistée, sans le bénéfice de l'agent.
- Accepter un graphe qui produit la bonne valeur mais qu'on serait incapable de maintenir.

### Pourquoi ce jeu de données

—

### Limite de la correction automatique

> Un agent ne reproduit pas exactement le même graphe d'une fois sur l'autre. C'est la longueur cumulée qui est validée, pas la forme du graphe : deux montages différents et justes doivent tous deux être acceptés.

### Pour aller plus loin

- Faire produire dix variantes paramétrées et comparer les longueurs.
- Demander à l'agent de documenter le graphe qu'il a construit.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-12_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-12_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-12.json` | Descripteur pour le plugin Magpie |
| `IA-12_fiche.md` | La présente fiche |
| `IA-12_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-12_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-12_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
