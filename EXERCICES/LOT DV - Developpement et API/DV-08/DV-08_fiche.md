# DV-08 — Ce que le remappage fait aux branches

**Fiche d'exercice Magpie** · Lot DV — Développement, scripting et API

| | |
|---|---|
| **Thématique** | DV2 · API et librairies |
| **Référence au référentiel** | REF-105 |
| **Compétence visée** | Prévoir la structure d'un arbre après un remappage de chemins, en raisonnant sur les chemins plutôt que sur les données. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Expert |
| **Durée cible** | 25 min |
| **Prérequis** | DV-03 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-09 Arbre relu |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Prévoir la structure d'un arbre après un remappage de chemins, en raisonnant sur les chemins plutôt que sur les données.

### Contexte

Le composant scripté reçoit un arbre à deux niveaux et doit rendre un résultat par valeur du second niveau, toutes origines confondues.

### Énoncé

> L'arbre porte trois valeurs au premier niveau de chemin et quatre au second, soit une branche par combinaison. Le remappage ne conserve que le second niveau. Donnez le nombre de branches obtenues.

### Ce qui vous est fourni

La structure de l'arbre de départ et la règle de remappage.

### Ce qui est attendu

4 branches — une par valeur du second niveau.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`DV-08_sujet.gh`

### Barème

1 point si le nombre de branches est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `DV-08_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Compter les branches de départ : le produit des deux niveaux.

**Étape 2.** Comprendre que le remappage retire un niveau du chemin.

**Étape 3.** Compter les chemins distincts qui subsistent.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Répondre 3, en conservant le mauvais maillon, ou 12 en supposant que le remappage ne change rien. Un remappage qui laisse tomber un niveau FUSIONNE les branches qui ne différaient que par lui : douze branches deviennent quatre, et chacune porte désormais trois fois plus de données.

### Pièges fréquents

- Conserver le mauvais niveau.
- Croire qu'un remappage ne change que l'étiquette.

### Pourquoi ce jeu de données

Trois et quatre sont premiers entre eux, de sorte que les trois réponses — 3, 4 et 12 — sont toutes distinctes et qu'aucune n'est un multiple trompeur des autres.

### Limite de la correction automatique

> Le compte des branches ne dit rien de leur CONTENU ni de l'ordre dans lequel les données s'y retrouvent — qui dépend de l'ordre de parcours, et se relève plutôt qu'il ne se devine.

### Pour aller plus loin

- Donner le nombre d'éléments par branche après remappage.
- Reprendre avec un aplatissement complet.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `DV-08_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `DV-08_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `DV-08.json` | Descripteur pour le plugin Magpie |
| `DV-08_fiche.md` | La présente fiche |
| `DV-08_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `DV-08_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `DV-08_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
