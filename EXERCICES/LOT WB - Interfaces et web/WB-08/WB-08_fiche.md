# WB-08 — Les bornes qui empêchent l'infabricable

**Fiche d'exercice Magpie** · Lot WB — Interfaces, web et interopérabilité

| | |
|---|---|
| **Thématique** | WB1 · Interfaces utilisateur |
| **Référence au référentiel** | REF-157 |
| **Compétence visée** | Éprouver les bornes d'une interface en cherchant les combinaisons admises qui produisent une pièce infabricable. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | WB-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-17 Passation |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Éprouver les bornes d'une interface en cherchant les combinaisons admises qui produisent une pièce infabricable.

### Contexte

Chaque paramètre du configurateur est borné. Pris séparément, aucun ne pose problème ; c'est leur COMBINAISON qui décide.

### Énoncé

> Une tablette exige 180 mm de hauteur libre, plus son épaisseur. Les douze réglages soumis vous sont fournis : hauteur du meuble, nombre de tablettes, épaisseur. Donnez le nombre de réglages infabricables.

### Ce qui vous est fourni

Les douze combinaisons, et la règle de hauteur libre.

### Ce qui est attendu

3 réglages sur douze sont infabricables.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`WB-08_sujet.gh`

### Barème

1 point si le compte des réglages infabricables est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `WB-08_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Calculer, pour chaque réglage, la hauteur qu'exigent les tablettes : leur nombre multiplié par la hauteur libre plus l'épaisseur.

**Étape 2.** Comparer à la hauteur du meuble.

**Étape 3.** Compter les réglages où l'exigence dépasse le disponible.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Vérifier chaque paramètre contre sa propre borne et conclure que tout va bien : pris un à un, les douze réglages sont dans les plages admises. C'est leur croisement qui échoue — une hauteur permise et un nombre de tablettes permis peuvent être incompatibles entre eux.

### Pièges fréquents

- Vérifier les paramètres un à un.
- Oublier d'ajouter l'épaisseur de la tablette à la hauteur libre.

### Pourquoi ce jeu de données

Trois combinaisons infaisables sur douze, et trois autres qui passent de justesse — 588 mm exigés pour 600 disponibles, 1 584 pour 1 600. La frontière est peuplée des deux côtés, de sorte qu'un contrôle approximatif se trompe dans les deux sens.

### Limite de la correction automatique

> L'exercice compte les combinaisons fautives d'un lot soumis. Une interface robuste ne les compte pas : elle les rend impossibles à saisir, en faisant dépendre la borne d'un paramètre de la valeur des autres.

### Pour aller plus loin

- Écrire la borne du nombre de tablettes en fonction de la hauteur.
- Trouver la hauteur minimale qui rendrait les douze réglages admissibles.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `WB-08_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `WB-08_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `WB-08.json` | Descripteur pour le plugin Magpie |
| `WB-08_fiche.md` | La présente fiche |
| `WB-08_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `WB-08_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `WB-08_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
