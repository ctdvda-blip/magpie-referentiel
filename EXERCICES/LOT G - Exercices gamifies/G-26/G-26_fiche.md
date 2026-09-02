# G-26 — Le retour visuel immédiat

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G6 · Sensations et immersion |
| **Référence au référentiel** | REF-026, REF-059 |
| **Compétence visée** | Comparer une série de mesures à un intervalle de tolérance et compter les écarts, des deux côtés. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | A-29 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 12 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Colorer le résultat en fonction de sa conformité, pour un diagnostic instantané.

### Contexte

La coloration conditionnelle est le contrôle qualité du modeleur : elle dit d'un coup d'œil ce qu'un tableau de vingt lignes met une minute à dire.

### Énoncé

> Vingt pièces doivent mesurer entre 400 et 900 mm. Colore en vert celles qui sont conformes, en rouge les autres, et affiche le nombre de non-conformes.

### Ce qui vous est fourni

Vingt pièces internalisées de longueurs variées.

### Ce qui est attendu

8 pièces non conformes.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-26_sujet.gh`

### Barème

2 points : 1 pour la coloration, 1 pour le compte.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-26_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Mesurer les longueurs avec Length.

**Étape 2.** Construire le test de conformité avec deux comparaisons et un Gate And.

**Étape 3.** Séparer les pièces avec Dispatch selon ce booléen.

**Étape 4.** Poser deux Custom Preview avec deux Colour Swatch distincts.

**Étape 5.** Compter les non-conformes avec Mass Addition sur le booléen inversé.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Ne tester qu'une borne — les pièces trop courtes — et compter 5 au lieu de 8. Une tolérance a DEUX bornes : ici trois pièces dépassent 900 mm, et un contrôle qui ne regarde que le bas les laisse passer en vert.

### Pièges fréquents

- Custom Preview appliqué à la liste complète : toutes les pièces prennent la même couleur.
- Aperçu du composant amont resté actif : les deux couleurs se superposent.

### Pourquoi ce jeu de données

Vingt longueurs de 250 à 1 150 mm : cinq sous 400, trois au-dessus de 900, douze conformes. Les deux dépassements sont de tailles différentes, de sorte que le compte partiel (5) et le compte complet (8) ne se confondent pas — et qu'aucun ne vaut la moitié de vingt.

### Limite de la correction automatique

> Le compte se vérifie, la COULEUR non : Grasshopper n'exporte pas l'aperçu coloré sous forme de valeur. La coloration se juge à l'écran.

### Pour aller plus loin

- Dégradé continu plutôt que deux couleurs.
- Coloration par famille de matériau.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-26_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-26_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-26.json` | Descripteur pour le plugin Magpie |
| `G-26_fiche.md` | La présente fiche |
| `G-26_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-26_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-26_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
