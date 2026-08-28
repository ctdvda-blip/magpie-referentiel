# WB-01 — Une définition utilisable par quelqu'un d'autre

**Fiche d'exercice Magpie** · Lot WB — Interfaces, web et interopérabilité

| | |
|---|---|
| **Thématique** | WB1 · Interfaces utilisateur |
| **Référence au référentiel** | REF-106, REF-107 |
| **Compétence visée** | Donner à une définition une interface qui permette de s'en servir sans l'ouvrir. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 40 min |
| **Prérequis** | MP-01 |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-25 Projet jalonné |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Donner à une définition une interface qui permette de s'en servir sans l'ouvrir.

### Contexte

Le commercial doit pouvoir configurer un produit devant le client, sans voir un seul composant.

### Énoncé

> Reprenez une de vos définitions et donnez-lui une interface : seuls les paramètres utiles sont exposés, nommés en langage métier, avec leurs bornes. Faites-la utiliser par quelqu'un qui ne connaît pas Grasshopper.

### Ce qui vous est fourni

Une définition fonctionnelle et organisée.

### Ce qui est attendu

Une définition pilotable par un tiers, sans ouverture du graphe.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **Visuel**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`WB-01_sujet.gh`

### Barème

Grille : paramètres choisis et nommés (2), bornes posées (1), usage réussi par un tiers (2).

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `WB-01_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Lister les paramètres et distinguer ceux que l'utilisateur doit régler de ceux qui relèvent du concepteur.

**Étape 2.** Renommer les premiers en langage métier — « hauteur d'allège », non « slider 3 ».

**Étape 3.** Poser des bornes qui interdisent les valeurs absurdes.

**Étape 4.** Rassembler l'interface au même endroit et masquer le reste.

**Étape 5.** Faire l'essai avec quelqu'un qui ne connaît pas l'outil.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Exposer tous les paramètres. Une interface qui montre trente curseurs n'est pas une interface : le travail consiste justement à choisir les cinq qui comptent et à cacher le reste.

### Pièges fréquents

- Bornes trop larges : l'utilisateur produit une géométrie impossible et croit s'être trompé.
- Noms techniques conservés : l'interface reste illisible.

### Pourquoi ce jeu de données

—

### Limite de la correction automatique

> L'utilisabilité ne se mesure pas par un nombre. Le contrôle est celui que l'énoncé prescrit : un tiers s'en sert, ou n'y arrive pas.

### Pour aller plus loin

- Ajouter un jeu de valeurs par défaut correspondant au produit courant.
- Intégrer la définition dans Rhino pour qu'elle se lance comme une commande.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `WB-01_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `WB-01_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `WB-01.json` | Descripteur pour le plugin Magpie |
| `WB-01_fiche.md` | La présente fiche |
| `WB-01_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `WB-01_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `WB-01_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
