# QT-05 — Le fichier que le fournisseur va lire

**Fiche d'exercice Magpie** · Lot QT — Quantitatifs, chiffrage et export

| | |
|---|---|
| **Thématique** | QT3 · Export de données |
| **Référence au référentiel** | REF-086, REF-087 |
| **Compétence visée** | Produire un fichier d'échange dont la structure est celle qu'attend le destinataire, en-tête comprise, et savoir combien de lignes il doit contenir avant de l'ouvrir. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | QT-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-11 Commande à passer |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire un fichier d'échange dont la structure est celle qu'attend le destinataire, en-tête comprise, et savoir combien de lignes il doit contenir avant de l'ouvrir.

### Contexte

La commande part en CSV vers le fournisseur, qui l'importe automatiquement. Un fichier mal structuré n'est pas rejeté : il est importé de travers.

### Énoncé

> Vous exportez la commande regroupée de l'exercice précédent au format CSV, avec une ligne d'en-tête nommant les colonnes. Donnez le nombre de lignes que le fichier doit contenir.

### Ce qui vous est fourni

Le débit de vingt-quatre lignes, et la commande regroupée qui en découle.

### Ce qui est attendu

9 — huit références, plus la ligne d'en-tête.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`QT-05_sujet.gh`

### Barème

1 point si le nombre de lignes est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `QT-05_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Reprendre la commande regroupée par référence.

**Étape 2.** Compter les références distinctes.

**Étape 3.** Ajouter la ligne d'en-tête.

**Étape 4.** Écrire le fichier, et le rouvrir pour vérifier le compte.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Exporter les vingt-quatre lignes du débit (25 avec l'en-tête) ou oublier l'en-tête (8). Le premier fait commander huit références en double ; le second fait lire la première référence comme un nom de colonne, et elle disparaît de la commande.

### Pièges fréquents

- Oublier l'en-tête.
- Exporter le débit au lieu de la commande.
- Employer la virgule comme séparateur alors que les quantités peuvent être décimales.

### Pourquoi ce jeu de données

Le compte attendu — 9 — ne ressemble ni au nombre de lignes du débit (24) ni au nombre de références (8) : les trois erreurs possibles donnent trois valeurs distinctes, donc lisibles.

### Limite de la correction automatique

> Le compte des lignes ne dit rien du séparateur ni de l'encodage, qui font échouer autant d'imports. La fiche les signale ; l'exercice ne les valide pas.

### Pour aller plus loin

- Ajouter une colonne d'unité et vérifier que le compte des lignes ne change pas.
- Exporter la même commande en XLSX et comparer ce que chaque format garantit.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `QT-05_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `QT-05_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `QT-05.json` | Descripteur pour le plugin Magpie |
| `QT-05_fiche.md` | La présente fiche |
| `QT-05_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `QT-05_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `QT-05_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
