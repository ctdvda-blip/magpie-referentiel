# G-06 — Le déblocage progressif

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G1 · Progression et récompense |
| **Référence au référentiel** | REF-059, REF-060, REF-061 |
| **Compétence visée** | Enchaîner trois filtres dont chacun s'applique au résultat du précédent, et non aux données de départ. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 18 min |
| **Prérequis** | A-29, A-30, A-31 |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 18 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Enchaîner des difficultés croissantes, chaque niveau ouvrant l'accès au suivant.

### Contexte

Le déblocage progressif protège l'apprenant d'une difficulté qu'il n'est pas prêt à affronter. Il rend aussi visible qu'un filtre s'applique à ce qui reste, pas à tout.

### Énoncé

> Trois niveaux de logique. Le niveau 2 ne devient actif qu'une fois le niveau 1 validé, et ainsi de suite. Les groupes verrouillés apparaissent grisés.

### Ce qui vous est fourni

Trois groupes de travail dont deux verrouillés.

### Ce qui est attendu

Les index survivants : 0, 8, 11, 26, 27, 31, 36, 53.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SetEquality**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-06_sujet.gh`

### Barème

3 points, 1 par niveau.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-06_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Niveau 1 : produire un booléen unique par comparaison.

**Étape 2.** Niveau 2 : combiner deux conditions par Gate And.

**Étape 3.** Niveau 3 : orienter un flux géométrique selon la condition combinée.

**Étape 4.** Valider chaque niveau avant de passer au suivant.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Prendre la moyenne des SOIXANTE valeurs de départ, 518,93, au lieu de celle des seize qui ont franchi le niveau 2, 771,50. Le niveau 3 garde alors quinze index au lieu de huit — presque le double. Un filtre s'applique à ce qui RESTE, jamais aux données de départ, et c'est toute la différence entre trois niveaux enchaînés et trois conditions indépendantes.

### Pièges fréquents

- Tenter de câbler le niveau 3 avant validation du niveau 1.
- Réutiliser un booléen d'un niveau antérieur devenu obsolète.

### Pourquoi ce jeu de données

Soixante valeurs de 100 à 999. Le premier niveau en garde 32, le deuxième 16, le troisième 8 : chaque niveau divise exactement par deux, ce qui donne à la progression une allure de niveaux de jeu. Le seuil du niveau 3 est une moyenne CALCULÉE sur les survivants — c'est ce qui rend le chaînage obligatoire, et le résultat impossible à retrouver de tête.

### Limite de la correction automatique

> Le déblocage est ici SIMULÉ par des groupes grisés. Grasshopper ne sait pas verrouiller un groupe : rien n'empêche l'apprenant d'ouvrir le niveau 3 d'emblée, et l'exercice ne le détecte pas.

### Pour aller plus loin

- Déblocage d'un niveau bonus caché.
- Retour possible sur un niveau validé pour améliorer son score.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-06_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-06_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-06.json` | Descripteur pour le plugin Magpie |
| `G-06_fiche.md` | La présente fiche |
| `G-06_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-06_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-06_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
