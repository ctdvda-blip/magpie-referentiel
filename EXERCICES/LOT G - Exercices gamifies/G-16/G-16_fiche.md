# G-16 — La chasse au trésor

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G3 · Manipulation et adresse |
| **Référence au référentiel** | REF-055, REF-101 |
| **Compétence visée** | Isoler la donnée aberrante d'un ensemble volumineux par un test d'appartenance, et en rendre l'index. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 18 min |
| **Prérequis** | A-09, A-45 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Rechercher une donnée anormale dans un ensemble volumineux.

### Contexte

Un point hors volume dans un nuage de cinq cents, c'est le cas réel du relevé qui contient une mesure parasite. Le trouver à l'œil est impossible ; le trouver par un test est immédiat.

### Énoncé

> Parmi 500 points, un seul est aberrant : il est hors du volume de référence. Trouve son index. Trois indices sont disponibles, chacun coûte 2 points.

### Ce qui vous est fourni

500 points internalisés et un volume de référence.

### Ce qui est attendu

337 — l'index du point aberrant.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-16_sujet.gh`

### Barème

10 points, moins 2 points par indice consulté.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-16_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser un test d'inclusion des points dans le volume de référence.

**Étape 2.** Récupérer la liste de booléens résultante.

**Étape 3.** Poser Gate Not puis un composant d'index des True pour localiser le point hors volume.

**Étape 4.** Afficher son index dans le Panel de réponse.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Chercher le point le plus ÉLOIGNÉ du centre au lieu de celui qui sort du volume. Le plus éloigné du centre est un coin parfaitement légitime du volume : la méthode donne un index faux et paraît pourtant raisonnable, ce qui en fait l'erreur la plus coûteuse de l'exercice.

### Pièges fréquents

- Chercher visuellement dans la vue Rhino sur 500 points.
- Confondre l'index dans la liste filtrée et l'index dans la liste d'origine.

### Pourquoi ce jeu de données

Cinq cents points tirés dans le volume 2 000 × 1 200 × 800, plus un seul qui en sort sur les TROIS axes à la fois. Un seul point est hors volume : la réponse est unique, et aucun cas limite ne traîne sur une face.

### Limite de la correction automatique

> L'index dépend de l'ORDRE des points. Réordonner le nuage — par un tri, une projection — change la réponse sans changer le point. C'est vrai de tout index, et c'est ce qui les rend fragiles dans les échanges.

### Pour aller plus loin

- Plusieurs points aberrants.
- Indice révélant une zone au lieu du point.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-16_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-16_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-16.json` | Descripteur pour le plugin Magpie |
| `G-16_fiche.md` | La présente fiche |
| `G-16_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-16_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-16_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
