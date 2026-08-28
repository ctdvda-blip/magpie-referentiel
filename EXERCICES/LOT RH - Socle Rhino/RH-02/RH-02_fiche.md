# RH-02 — Reprendre une implantation par son calque

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Organisation du document |
| **Référence au référentiel** | REF-004, REF-006, REF-014 |
| **Compétence visée** | Organiser un document Rhino par calques de sorte qu'une définition puisse en reprendre une partie sans sélection manuelle. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | A-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Organiser un document Rhino par calques de sorte qu'une définition puisse en reprendre une partie sans sélection manuelle.

### Contexte

Le géomètre livre l'implantation d'un plancher : poteaux porteurs et cloisons sont mélangés sur un même calque, alors que seuls les porteurs entrent dans la descente de charges.

### Énoncé

> Le fichier fourni contient 18 points d'implantation sur un calque unique. Séparez les 12 porteurs des 6 cloisons sur deux calques distincts, puis faites compter les porteurs par la définition — sans les désigner un par un.

### Ce qui vous est fourni

Un fichier Rhino contenant les 18 points sur le calque « IMPLANTATION », et une définition prête à référencer un calque.

### Ce qui est attendu

Un nombre entier : combien de points portent le calque des porteurs, une fois le tri fait.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-02_sujet.gh`

### Barème

1 point si le compte vaut 12 et si aucun point n'a été désigné individuellement.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-02_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 12 — le nombre de points sur le calque des porteurs.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Créer les deux calques, « PORTEURS » et « CLOISONS », avant toute sélection.

**Étape 2.** Isoler les porteurs par leur régularité — un réseau de sélection ou une fenêtre suffit — et les déplacer sur leur calque.

**Étape 3.** Vérifier qu'il ne reste rien sur le calque d'origine.

**Étape 4.** Faire pointer la définition sur le calque des porteurs, pas sur une sélection.

**Étape 5.** Contrôler que le compte tombe à 12.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Sélectionner les porteurs à la main dans la vue plutôt que de les isoler sur un calque. Le compte est juste aujourd'hui, et faux dès que le géomètre livre une mise à jour — ce que l'exercice ne montre qu'à la seconde livraison.

### Pièges fréquents

- Masquer les cloisons au lieu de les déplacer : elles restent sur le calque et la définition les reprend quand même.
- Nommer les calques après coup : le lien de la définition se fait sur le nom, un renommage le casse.

### Pourquoi ce jeu de données

Les porteurs forment une trame régulière de 5 400 × 6 200 mm, les cloisons sont décalées à mi-portée. La distinction est lisible à l'œil dans la vue, ce qui rend le tri manuel tentant — et c'est justement le piège.

### Pour aller plus loin

- Ajouter deux porteurs dans Rhino et vérifier que le compte suit tout seul.
- Reprendre les porteurs par un filtre sur la couleur plutôt que sur le calque, et juger ce qui est le plus robuste.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-02_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-02_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-02.json` | Descripteur pour le plugin Magpie |
| `RH-02_fiche.md` | La présente fiche |
| `RH-02_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-02_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-02_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
