# A-50 — Nettoyer avant de regrouper

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A7 · Outils de texte |
| **Référence au référentiel** | REF-144 |
| **Compétence visée** | Ramener des libellés saisis à la main à une forme comparable, avant tout regroupement. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-28 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-11 Commande à passer |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Ramener des libellés saisis à la main à une forme comparable, avant tout regroupement.

### Contexte

Les références du débit ont été saisies par trois personnes, sur trois postes. Le fournisseur, lui, attend une ligne par référence.

### Énoncé

> Les vingt libellés vous sont fournis tels qu'ils ont été saisis. Donnez le nombre de références réellement distinctes.

### Ce qui vous est fourni

Les vingt libellés, avec leurs espaces et leurs casses d'origine.

### Ce qui est attendu

6 références distinctes.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-50_sujet.gh`

### Barème

1 point si le nombre de références distinctes est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-50_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Retirer les espaces de bord.

**Étape 2.** Uniformiser la casse.

**Étape 3.** Établir l'ensemble des valeurs distinctes.

**Étape 4.** Compter.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Regrouper sans nettoyer : on en trouve dix-sept. « MEL-19 »,  « mel-19 » et « MEL-19 » avec une espace de bord sont trois chaînes différentes et une seule référence. Le fournisseur recevrait dix-sept lignes pour six produits, et le rapprochement de facture échouerait sans que rien ne soit signalé.

### Pièges fréquents

- Regrouper sur la chaîne brute.
- Retirer TOUS les espaces, y compris ceux de l'intérieur : un libellé composé y perdrait son sens.

### Pourquoi ce jeu de données

Trois écarts de saisie, et un seul de chaque sorte par référence : espace de bord, casse, et les deux à la fois. Dix-sept contre six, soit près du triple : l'erreur ne se rattrape pas au jugé.

### Limite de la correction automatique

> Le nettoyage traite les écarts de FORME. Deux références réellement différentes mal orthographiées resteront deux — et c'est heureux : aucun nettoyage ne doit deviner l'intention.

### Pour aller plus loin

- Rendre la liste des références nettoyées, triées.
- Repérer les libellés que le nettoyage n'a pas suffi à réconcilier.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-50_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-50_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-50.json` | Descripteur pour le plugin Magpie |
| `A-50_fiche.md` | La présente fiche |
| `A-50_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-50_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-50_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
