# WB-07 — Le plan qui tient sur la feuille

**Fiche d'exercice Magpie** · Lot WB — Interfaces, web et interopérabilité

| | |
|---|---|
| **Thématique** | WB2 · Publication web |
| **Référence au référentiel** | REF-110 |
| **Compétence visée** | Choisir l'échelle normalisée qui fait tenir une pièce sur un format donné, marges comprises. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | WB-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-16 Livrable pesé |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Choisir l'échelle normalisée qui fait tenir une pièce sur un format donné, marges comprises.

### Contexte

Le configurateur produit le plan en PDF, que le client imprime lui-même. Une échelle non normalisée rend le plan inutilisable : personne ne mesure au 1:6,1.

### Énoncé

> La pièce mesure 2 380 mm de long et 1 640 mm de haut. Le plan sort sur une feuille de 420 × 297 mm, avec 15 mm de marge sur chaque bord. Les échelles disponibles sont 1:1, 1:2, 1:5, 1:10, 1:20, 1:50 et 1:100. Donnez le dénominateur de la plus grande échelle qui convient.

### Ce qui vous est fourni

Les dimensions de la pièce, le format de la feuille, la marge, et la liste des échelles normalisées.

### Ce qui est attendu

10 — l'échelle 1:10, qui donne 238 × 164 mm dans une zone utile de 390 × 267 mm.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`WB-07_sujet.gh`

### Barème

1 point si le dénominateur est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `WB-07_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Retrancher les marges pour obtenir la zone utile.

**Étape 2.** Calculer le rapport nécessaire sur chacune des deux dimensions.

**Étape 3.** Retenir le plus grand des deux.

**Étape 4.** Choisir dans la liste la première échelle dont le dénominateur l'atteint ou le dépasse.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Calculer le rapport exact — 6,10 en longueur — et retenir 1:5 en arrondissant vers l'échelle voisine. Au 1:5, la pièce fait 476 mm et déborde de 86 mm : le PDF s'imprime quand même, tronqué. Une échelle se choisit DANS la liste, et toujours vers la plus petite.

### Pièges fréquents

- Ne vérifier que la longueur.
- Oublier les marges.
- Retenir une échelle non normalisée parce qu'elle « tient mieux ».

### Pourquoi ce jeu de données

Le rapport nécessaire vaut 6,10 en longueur et 6,14 en hauteur : les deux dépassent 5 et aucun n'atteint 10, de sorte que ni la longueur seule ni la hauteur seule ne suffisent à trancher — il faut vérifier les deux. Une pièce plus étroite aurait laissé passer le réflexe de ne regarder que la plus grande dimension.

### Limite de la correction automatique

> L'exercice choisit l'échelle, pas la mise en page : cartouche, cotation et nomenclature occupent aussi la feuille, et se traitent au format supérieur ou en plusieurs vues.

### Pour aller plus loin

- Passer au format inférieur et reprendre le choix.
- Réserver 60 mm de cartouche en bas de feuille et recommencer.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `WB-07_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `WB-07_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `WB-07.json` | Descripteur pour le plugin Magpie |
| `WB-07_fiche.md` | La présente fiche |
| `WB-07_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `WB-07_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `WB-07_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
