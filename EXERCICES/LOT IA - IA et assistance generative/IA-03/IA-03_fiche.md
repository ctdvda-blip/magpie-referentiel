# IA-03 — Reprendre une demande sur le point qui échoue

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA1 · Formuler et cadrer une demande |
| **Référence au référentiel** | REF-119 |
| **Compétence visée** | Isoler ce qui échoue dans un code produit et reformuler la demande sur ce seul point. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 18 min |
| **Prérequis** | IA-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-07 Indice progressif |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Isoler ce qui échoue dans un code produit et reformuler la demande sur ce seul point.

### Contexte

Un relevé de planéité de plancher doit être classé : on cherche l'amplitude totale, du point le plus haut au plus bas.

### Énoncé

> Les 28 niveaux relevés vous sont fournis, en millimètres autour du zéro. Faites produire un composant qui renvoie l'amplitude du relevé. Le premier code obtenu donnera un résultat faux : reprenez la demande sur le seul point fautif, sans la réécrire en entier.

### Ce qui vous est fourni

Les 28 niveaux relevés, en millimètres, positifs et négatifs.

### Ce qui est attendu

Un nombre : l'amplitude du relevé, en millimètres.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-03_sujet.gh`

### Barème

1 point si la sortie vaut 48 après une seule reformulation.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-03_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 48 — l'écart entre le point le plus haut (+25) et le plus bas (−23).

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Demander un composant renvoyant « l'écart maximal » du relevé, volontairement formulé ainsi.

**Étape 2.** Relever le résultat : 25, qui est la plus grande valeur absolue.

**Étape 3.** Contrôler à la main sur les données : le plus haut vaut +25, le plus bas −23, l'amplitude vaut donc 48.

**Étape 4.** Reformuler sur ce seul point — « la différence entre la valeur maximale et la valeur minimale » — sans redécrire les entrées.

**Étape 5.** Vérifier que la sortie vaut 48.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Obtenir la plus grande valeur absolue, 25, au lieu de l'amplitude, 48 : « l'écart maximal » se comprend des deux façons. Un relevé entièrement positif ne révélerait pas l'ambiguïté — c'est la présence de valeurs négatives qui la rend visible.

### Pièges fréquents

- Repartir d'une demande entièrement neuve : on perd le contexte déjà établi et souvent on réintroduit une autre ambiguïté.
- Corriger le code à la main : l'exercice porte sur la formulation, pas sur la retouche.

### Pourquoi ce jeu de données

28 niveaux répartis de part et d'autre du zéro, de −23 à +25. Sur un relevé positif, la valeur absolue maximale et l'amplitude coïncideraient et l'exercice n'aurait plus d'objet.

### Limite de la correction automatique

> L'amplitude juste prouve que la reprise a abouti, pas qu'elle était BIEN formulée. Deux apprenants peuvent obtenir 48 en deux échanges ou en douze — l'écart est tout le sujet de l'exercice, et il ne se mesure pas automatiquement.

### Pour aller plus loin

- Demander en plus la position du point le plus bas, et constater que la question du rang se pose exactement comme en A-11.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-03_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-03_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-03.json` | Descripteur pour le plugin Magpie |
| `IA-03_fiche.md` | La présente fiche |
| `IA-03_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-03_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-03_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
