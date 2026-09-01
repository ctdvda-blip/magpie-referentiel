# DV-07 — Un plugin qui s'installe chez quelqu'un d'autre

**Fiche d'exercice Magpie** · Lot DV — Développement, scripting et API

| | |
|---|---|
| **Thématique** | DV3 · Compilation et IDE |
| **Référence au référentiel** | REF-098 |
| **Compétence visée** | Livrer un plugin qui se charge sur un poste qui n'est pas celui du développeur, et le prouver. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Expert |
| **Durée cible** | 50 min |
| **Prérequis** | DV-06 |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-23 Livraison à l'aveugle |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Livrer un plugin qui se charge sur un poste qui n'est pas celui du développeur, et le prouver.

### Contexte

Le plugin marche sur votre poste. C'est la situation la moins informative qui soit : votre poste porte le SDK, les dépendances et les chemins de développement.

### Énoncé

> Reprenez le plugin de DV-04 et rendez-le installable : manifeste renseigné, dépendances embarquées ou déclarées, version visible. Faites-le installer par quelqu'un d'autre, sur un poste où l'environnement de développement n'est pas présent, et faites-lui exécuter le composant sans un mot d'explication.

### Ce qui vous est fourni

Le plugin de DV-04, et un poste qui n'est pas le vôtre.

### Ce qui est attendu

Un plugin installé et fonctionnel sur un poste tiers, dont le composant apparaît dans l'onglet visé et rend le résultat attendu.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **Visuel**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`DV-07_sujet.gh`

### Barème

Grille : manifeste complet (1), dépendances traitées (1), installation réussie sur un poste tiers (2), composant exécuté sans assistance (1).

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `DV-07_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Renseigner le manifeste : nom, version, auteur, description, icône.

**Étape 2.** Lister les dépendances et décider, pour chacune, entre l'embarquer et l'exiger.

**Étape 3.** Produire le paquet d'installation.

**Étape 4.** Installer sur un poste tiers, sans environnement de développement.

**Étape 5.** Faire exécuter le composant par son utilisateur, sans assistance.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Livrer le seul fichier compilé. Il se chargera chez vous et nulle part ailleurs : les dépendances qu'il trouve dans votre dossier de compilation n'existent pas sur le poste d'arrivée. Et l'échec ne dit rien — le composant est simplement absent de l'onglet, sans message.

### Pièges fréquents

- Livrer le binaire seul.
- Oublier de faire croître le numéro de version : la mise à jour ne remplace alors rien.
- Tester sur son propre poste et conclure.

### Pourquoi ce jeu de données

—

### Limite de la correction automatique

> Le livrable se juge sur grille : il n'y a pas de définition Grasshopper à corriger, et c'est le propre de cet exercice. C'est aussi pourquoi la vérification passe par un TIERS — la seule qui distingue « ça marche » de « ça marche chez moi ».

### Pour aller plus loin

- Publier sur le gestionnaire de paquets et faire installer par la voie normale.
- Livrer une version 2 et vérifier qu'elle remplace bien la première.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `DV-07_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `DV-07_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `DV-07.json` | Descripteur pour le plugin Magpie |
| `DV-07_fiche.md` | La présente fiche |
| `DV-07_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `DV-07_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `DV-07_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
