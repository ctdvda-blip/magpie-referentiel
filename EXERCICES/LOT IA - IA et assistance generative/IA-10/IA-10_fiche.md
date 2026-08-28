# IA-10 — Regrouper un débit pour rationaliser la commande

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA4 · Apprentissage automatique |
| **Référence au référentiel** | REF-130 |
| **Compétence visée** | Regrouper automatiquement des éléments par similarité et exploiter le regroupement obtenu. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | IA-09 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Regrouper automatiquement des éléments par similarité et exploiter le regroupement obtenu.

### Contexte

Le fournisseur consent une remise à partir de trois longueurs standard seulement : il faut ramener un débit dispersé à trois longueurs de commande.

### Énoncé

> Les longueurs de débit vous sont fournies. Ramenez-les à trois longueurs de commande, chacune au moins égale à la plus longue pièce de son groupe, et donnez le nombre de pièces du groupe le plus fourni.

### Ce qui vous est fourni

Les 24 longueurs de débit, en millimètres.

### Ce qui est attendu

L'effectif du groupe le plus fourni.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-10_sujet.gh`

### Barème

1 point si l'effectif annoncé correspond au regroupement de référence.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-10_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Regrouper les longueurs en trois ensembles par similarité.

**Étape 2.** Relever le maximum de chaque groupe : c'est la longueur de commande, pas la moyenne.

**Étape 3.** Compter les pièces de chaque groupe.

**Étape 4.** Contrôler que la somme des trois effectifs vaut bien 24.

**Étape 5.** Chiffrer la chute engendrée, pour vérifier que la remise vaut la matière perdue.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Retenir la longueur moyenne de chaque groupe comme longueur de commande : une pièce sur deux devient alors trop courte. Le contexte impose un arrondi au supérieur, que le regroupement seul ne fournit pas.

### Pièges fréquents

- Prendre la moyenne du groupe comme longueur de commande.
- Oublier de vérifier que tous les groupes sont non vides.

### Pourquoi ce jeu de données

Les longueurs du débit du lot A sont réemployées ici dans un autre métier et une autre finalité : c'est la variation de contexte que la recherche sur le transfert recommande, à données constantes.

### Pour aller plus loin

- Passer à quatre longueurs et comparer la chute totale.
- Chiffrer le seuil de remise à partir duquel le regroupement devient rentable.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-10_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-10_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-10.json` | Descripteur pour le plugin Magpie |
| `IA-10_fiche.md` | La présente fiche |
| `IA-10_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-10_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-10_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
