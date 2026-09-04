# IA-29 — Les GUID qui cassent les définitions

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA3 · Développement de plugins assisté |
| **Référence au référentiel** | REF-128 |
| **Compétence visée** | Mesurer l'effet d'un GUID régénéré sur le parc de définitions existantes. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 18 min |
| **Prérequis** | IA-08 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-29 Le défi du jour |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mesurer l'effet d'un GUID régénéré sur le parc de définitions existantes.

### Contexte

Publier la version suivante d'un plugin ne doit pas casser les définitions déjà écrites. Un GUID régénéré rend un composant introuvable, et la définition s'ouvre avec un trou.

### Énoncé

> Le tableau donne, pour huit composants du plugin, si leur GUID a été conservé d'une version à l'autre et combien de définitions les emploient. Donnez le nombre de définitions cassées par la mise à jour.

### Ce qui vous est fourni

Le tableau des huit composants, de leurs GUID et de leur usage.

### Ce qui est attendu

16 définitions sont cassées par la mise à jour.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-29_sujet.gh`

### Barème

1 point si le compte est exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-29_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Isoler les composants dont le GUID a changé.

**Étape 2.** Récupérer le nombre de définitions correspondantes.

**Étape 3.** En faire la somme.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter les COMPOSANTS dont le GUID a changé — quatre — au lieu des définitions qui les emploient. Un composant régénéré casse autant de définitions qu'il en sert : le préjudice se mesure chez les utilisateurs, pas dans le code.

### Pièges fréquents

- Compter les composants au lieu des définitions.
- Sommer tout le parc sans filtrer.

### Pourquoi ce jeu de données

Huit composants, quatre GUID régénérés, et des usages de 1 à 9 définitions. Les composants les plus employés ne sont pas ceux dont le GUID a changé : le total, 16, ne se déduit ni du nombre de composants ni de l'usage moyen.

### Limite de la correction automatique

> Le compte suppose qu'une définition cassée l'est ENTIÈREMENT. En pratique elle s'ouvre, le composant manquant apparaît en substitut rouge, et le reste continue de fonctionner — le préjudice est réel mais gradué, ce que ce chiffre n'exprime pas.

### Pour aller plus loin

- Chercher le composant dont la régénération coûte le plus cher.
- Estimer le gain d'une table de correspondance des anciens GUID.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-29_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-29_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-29.json` | Descripteur pour le plugin Magpie |
| `IA-29_fiche.md` | La présente fiche |
| `IA-29_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-29_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-29_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
