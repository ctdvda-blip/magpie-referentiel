# A-28 — Découper et remplacer du texte

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A6 · Outils de texte |
| **Référence au référentiel** | REF-058 |
| **Compétence visée** | Extraire un fragment d'une référence structurée et le normaliser. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-27 |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-19 Le composant mystère |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Extraire un fragment d'une référence structurée et le normaliser.

### Contexte

Les références fournisseur encodent la famille, le code produit et l'essence ; seul le code produit alimente la commande.

### Énoncé

> Les références vous sont fournies au format « MEUB-A12-CHENE ». Extrayez le seul code central et livrez-le en minuscules.

### Ce qui vous est fourni

Une liste de 6 références internalisée.

### Ce qui est attendu

Six codes en minuscules : a12, b07, …

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **Visuel**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-28_sujet.gh`

### Barème

1 point si les 6 codes sont exacts.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-28_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Text Split avec le séparateur - (tiret).

**Étape 2.** La sortie est un arbre : chaque référence donne une branche de 3 fragments.

**Étape 3.** Poser List Item avec l'index 1 pour prendre le fragment central de chaque branche.

**Étape 4.** Poser Text Case en mode Lower.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Découper par position de caractère plutôt que par séparateur : le montage tient tant que la famille fait quatre lettres, et se rompt à la première référence au format différent.

### Pièges fréquents

- Oublier que Text Split produit un arbre et non une liste plate.
- Espaces parasites : appliquer Trim avant le découpage.

### Limite de la correction automatique

> Même limite qu'en A-27 : le livrable est une liste de codes en minuscules, que le checker ne sait pas comparer. Validation visuelle.

### Pour aller plus loin

- Remplacer le matériau par un autre avec Replace Text.
- Reconstituer la référence complète après modification.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-28_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-28_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-28.json` | Descripteur pour le plugin Magpie |
| `A-28_fiche.md` | La présente fiche |
| `A-28_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-28_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-28_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
