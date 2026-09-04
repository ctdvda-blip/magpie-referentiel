# RH-23 — Sélectionner sur ce que les objets sont

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Organisation du document Rhino |
| **Référence au référentiel** | REF-143 |
| **Compétence visée** | Retrouver des objets par le croisement de leurs propriétés, plutôt que par ce qu'on voit à l'écran. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-13 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-02 Diagnostic éclair |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Retrouver des objets par le croisement de leurs propriétés, plutôt que par ce qu'on voit à l'écran.

### Contexte

Il faut isoler les axes de porteurs pour les envoyer au bureau d'études. Une sélection à la souris cesse d'être juste dès la livraison suivante.

### Énoncé

> Le relevé des vingt-quatre objets vous est fourni, avec pour chacun son calque et son type. Donnez le nombre d'objets qui sont À LA FOIS sur le calque des porteurs et de type courbe.

### Ce qui vous est fourni

Les vingt-quatre objets, leur calque et leur type.

### Ce qui est attendu

6 objets satisfont les deux conditions.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-23_sujet.gh`

### Barème

1 point si le croisement est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-23_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Comparer le calque de chaque objet à celui recherché.

**Étape 2.** Comparer son type à celui recherché.

**Étape 3.** Ne retenir que les objets qui satisfont les DEUX.

**Étape 4.** Compter.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter sur une seule propriété : onze objets sont sur le calque des porteurs, et onze sont des courbes. Les deux comptes sont égaux, ce qui donne l'illusion d'une réponse — mais seuls six objets vérifient les deux conditions ensemble.

### Pièges fréquents

- Ne vérifier qu'une propriété.
- Additionner les deux comptes partiels.
- Sélectionner à l'écran plutôt que sur la propriété.

### Pourquoi ce jeu de données

Les deux comptes partiels valent onze chacun, à dessein : un apprenant qui n'en vérifie qu'un obtient le même chiffre des deux côtés et n'a aucune raison de se méfier. Le croisement, lui, en donne six.

### Limite de la correction automatique

> L'exercice croise deux propriétés. En pratique on en croise souvent trois ou quatre, et c'est le même geste — mais aussi le moment où une sélection à la souris devient impossible à reproduire.

### Pour aller plus loin

- Ajouter une troisième condition sur la couleur.
- Enregistrer la sélection comme un filtre rejouable.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-23_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-23_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-23.json` | Descripteur pour le plugin Magpie |
| `RH-23_fiche.md` | La présente fiche |
| `RH-23_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-23_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-23_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
