# WB-09 — Ce que le format transporte, et ce qu'il perd

**Fiche d'exercice Magpie** · Lot WB — Interfaces, web et interopérabilité

| | |
|---|---|
| **Thématique** | WB3 · Interopérabilité |
| **Référence au référentiel** | REF-158 |
| **Compétence visée** | Choisir un format d'échange sur ce qu'il transporte réellement, et non sur le fait que le fichier s'ouvre. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | WB-05 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-17 Passation |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Choisir un format d'échange sur ce qu'il transporte réellement, et non sur le fait que le fichier s'ouvre.

### Contexte

Le modèle part chez le bureau d'études, qui a besoin des courbes, des calques et des unités. Un fichier qui s'ouvre n'est pas un échange réussi.

### Énoncé

> Le tableau des six formats vous est fourni, avec ce que chacun transporte. L'échange exige la géométrie, les unités, les calques et les courbes. Donnez le nombre de formats qui conviennent.

### Ce qui vous est fourni

Les six formats et, pour chacun, ce qu'il transporte.

### Ce qui est attendu

3 formats répondent aux quatre exigences.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`WB-09_sujet.gh`

### Barème

1 point si le compte des formats convenables est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `WB-09_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Ne retenir que les colonnes exigées par l'échange.

**Étape 2.** Pour chaque format, exiger qu'elles soient TOUTES vraies.

**Étape 3.** Compter.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Retenir tout format qui transporte la géométrie : les six conviennent alors. Le fichier s'ouvrira, la forme sera là, et le bureau d'études redemandera les calques et les unités — c'est-à-dire la moitié du travail de mise en ordre.

### Pièges fréquents

- Se contenter de la géométrie.
- Traiter la liste des exigences comme un « au moins un ».

### Pourquoi ce jeu de données

Six formats, dont trois répondent aux quatre exigences et deux échouent sur un seul critère. Les réponses fausses plausibles — 6 si l'on ne regarde que la géométrie, 5 si l'on oublie les courbes — sont distinctes de 3.

### Limite de la correction automatique

> Le tableau dit ce que le format PEUT porter. Ce qu'il porte effectivement dépend aussi de l'exportateur et de l'importateur — deux logiciels qui parlent le même format peuvent ne pas s'entendre.

### Pour aller plus loin

- Nommer les formats écartés et le critère qui les écarte.
- Refaire le choix pour un échange qui exigerait les matières.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `WB-09_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `WB-09_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `WB-09.json` | Descripteur pour le plugin Magpie |
| `WB-09_fiche.md` | La présente fiche |
| `WB-09_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `WB-09_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `WB-09_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
