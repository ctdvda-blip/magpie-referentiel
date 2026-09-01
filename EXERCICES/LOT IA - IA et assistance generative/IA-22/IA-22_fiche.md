# IA-22 — L'arrondi qui change avec le langage

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA2 · Composants scriptés assistés |
| **Référence au référentiel** | REF-123 |
| **Compétence visée** | Vérifier qu'un script transposé rend le même résultat que l'original, en se méfiant des comportements par défaut. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | IA-06 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-15 Relecture de code |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Vérifier qu'un script transposé rend le même résultat que l'original, en se méfiant des comportements par défaut.

### Contexte

Le script de chiffrage est transposé d'un langage à un autre. Il compile, il tourne, et le total a bougé de six unités.

### Énoncé

> Les douze quantités à arrondir vous sont fournies ; toutes tombent sur une demi-unité. Le métier arrondit la demie vers le haut. Donnez la somme des quantités arrondies selon la règle du métier.

### Ce qui vous est fourni

Les douze quantités et la règle d'arrondi du métier.

### Ce qui est attendu

170 — la somme des arrondis commerciaux.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-22_sujet.gh`

### Barème

1 point si la somme selon la règle du métier est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-22_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Arrondir chaque valeur selon la règle du métier.

**Étape 2.** Sommer.

**Étape 3.** Refaire la somme avec l'arrondi par défaut du langage et mesurer l'écart.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Laisser l'arrondi par défaut du langage faire son office : il rend 164. La plupart des langages arrondissent la demie vers le nombre PAIR, pour ne pas biaiser les sommes — 2,5 donne 2 et 3,5 donne 4. C'est statistiquement vertueux et commercialement faux : sur douze lignes, six unités s'évaporent, et le devis ne tombe plus juste.

### Pièges fréquents

- Se fier à l'arrondi par défaut.
- Supposer que deux langages arrondissent pareil.

### Pourquoi ce jeu de données

Douze valeurs tombant toutes exactement sur la demie, dont six paires et six impaires : l'arrondi au pair descend une valeur sur deux, d'où un écart de six exactement. Sur des données ordinaires, l'écart serait nul la plupart du temps — et le défaut resterait invisible jusqu'au jour où il ne l'est plus.

### Limite de la correction automatique

> Aucune des deux règles n'est « la bonne » dans l'absolu. Ce qui est fautif est de ne pas savoir laquelle le langage applique, et de découvrir l'écart sur une facture.

### Pour aller plus loin

- Retrouver l'écart sur un jeu où une valeur sur dix seulement tombe sur la demie.
- Écrire la règle du métier explicitement, sans dépendre du langage.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-22_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-22_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-22.json` | Descripteur pour le plugin Magpie |
| `IA-22_fiche.md` | La présente fiche |
| `IA-22_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-22_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-22_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
