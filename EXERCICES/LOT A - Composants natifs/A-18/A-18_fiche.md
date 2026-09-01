# A-18 — Extraire une portion de liste

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A3 · Listes |
| **Référence au référentiel** | REF-042, REF-043 |
| **Compétence visée** | Prélever une tranche continue d'une liste par ses rangs. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-12 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-03 Compte à rebours |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Prélever une tranche continue d'une liste par ses rangs.

### Contexte

Sur un profil en long, seule la section courante intéresse le calcul ; les relevés d'extrémité relèvent des ouvrages voisins.

### Énoncé

> Le profil compte 28 relevés altimétriques. Isolez ceux des rangs 5 à 12 inclus, qui correspondent à la section courante.

### Ce qui vous est fourni

Les 28 relevés altimétriques du profil en long, en millimètres.

### Ce qui est attendu

Huit relevés : 466, 419, 448, 433, 471, 405, 459, 424.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-18_sujet.gh`

### Barème

1 point si les 8 bons éléments sortent.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-18_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Construct Domain avec A = 5 et B = 12.

**Étape 2.** Poser Sub List : liste sur L, domaine sur D.

**Étape 3.** Vérifier avec List Length que la sous-liste contient 8 éléments.

**Étape 4.** Retenir : le domaine est inclusif aux deux bornes.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Livrer sept valeurs, en oubliant que la borne haute est incluse — ou neuf, en comptant deux fois une extrémité. L'écart d'une unité est l'erreur canonique sur les domaines de rangs.

### Pièges fréquents

- Croire la borne haute exclusive : on obtiendrait 7 éléments.
- Saisir le domaine dans un Panel sous la forme « 5 to 12 » sans Construct Domain.

### Pourquoi ce jeu de données

28 altitudes non ordonnées : la tranche demandée n'a aucune signature visuelle, il faut la prélever.

### Pour aller plus loin

- Couper la liste en deux avec Split List.
- Extraire les 5 derniers éléments quelle que soit la taille de la liste.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-18_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-18_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-18.json` | Descripteur pour le plugin Magpie |
| `A-18_fiche.md` | La présente fiche |
| `A-18_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-18_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-18_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
