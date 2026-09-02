# IA-05 — Le code qui tourne et se trompe

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA2 · Composants scriptés assistés |
| **Référence au référentiel** | REF-124 |
| **Compétence visée** | Localiser une erreur de logique dans un code qui s'exécute sans planter. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 22 min |
| **Prérequis** | IA-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-11 Chasse à l'erreur |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Localiser une erreur de logique dans un code qui s'exécute sans planter.

### Contexte

Un composant livré par un confrère chiffre le nombre de tronçons dépassant une longueur de transport de 4 mètres.

### Énoncé

> Le composant fourni s'exécute sans erreur et annonce un résultat. Ce résultat est faux. Trouvez pourquoi et faites-le corriger, puis donnez le nombre exact de tronçons concernés.

### Ce qui vous est fourni

Les 16 longueurs de tronçons, en mètres, et un composant scripté déjà en place qui les traite.

### Ce qui est attendu

Un nombre entier : combien de tronçons dépassent la longueur de transport. Le composant fourni en annonce un autre.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-05_sujet.gh`

### Barème

1 point si la sortie corrigée vaut 9.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-05_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 9 — le nombre de tronçons de plus de 4 mètres.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Ne pas relire le code en premier : établir d'abord la réponse juste par un montage natif indépendant.

**Étape 2.** Comparer les deux résultats et mesurer l'écart.

**Étape 3.** Relire le code en cherchant ce qui produirait cet écart-là, plutôt qu'en cherchant « une erreur ».

**Étape 4.** Décrire à l'assistant le symptôme constaté — la valeur obtenue et la valeur attendue — et non « corrige ce code ».

**Étape 5.** Vérifier que la sortie corrigée vaut 9.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Chercher l'erreur dans le langage plutôt que dans la logique. Le code est syntaxiquement irréprochable : c'est la condition qui est fausse. Un apprenant qui relit la syntaxe ligne à ligne peut y passer un long moment sans rien voir.

### Pièges fréquents

- Demander « corrige ce code » sans dire ce qui cloche : l'assistant réécrit tout et l'erreur peut survivre.
- Faire confiance au fait que le composant ne signale rien : l'absence d'erreur ne dit rien de la justesse.

### Pourquoi ce jeu de données

Les longueurs sont choisies pour qu'une comparaison large et une comparaison stricte donnent le même compte : l'erreur plantée dans le code est ailleurs, ce qui évite de résoudre l'exercice par tâtonnement sur l'inégalité.

### Pour aller plus loin

- Injecter une seconde erreur et refaire le diagnostic.
- Écrire un contrôle permanent : un composant natif qui recalcule la même chose et signale tout écart.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-05_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-05_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-05.json` | Descripteur pour le plugin Magpie |
| `IA-05_fiche.md` | La présente fiche |
| `IA-05_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-05_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-05_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
