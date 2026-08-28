# A-02 — Construire un point par coordonnées

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A1 · Interface, flux de données et paramètres |
| **Référence au référentiel** | REF-062 |
| **Compétence visée** | Construire une position dans l'espace à partir de trois valeurs séparées, y compris négatives. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-01 |
| **Mode de validation** | GeometryTolerance — tolérance 0,01 mm |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-26 Feedback visuel immédiat |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Construire une position dans l'espace à partir de trois valeurs séparées, y compris négatives.

### Contexte

Le géomètre communique la position d'un repère de nivellement par rapport à la borne de chantier.

### Énoncé

> Le repère se trouve à 30 m à l'est, 15 m au sud et 8 m au-dessus de la borne, laquelle est à l'origine du modèle. Placez ce repère dans le modèle à partir de trois valeurs réglables indépendantes.

### Ce qui vous est fourni

Canvas vide.

### Ce qui est attendu

Un point unique aux coordonnées (30 ; −15 ; 8).

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,01 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-02_sujet.gh`

### Barème

1 point si le point est à moins de 0,01 mm de la cible.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-02_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser trois Number Slider et les nommer X, Y et Z (double-clic sur le nom).

**Étape 2.** Régler les bornes de Y de -50 à 50 pour autoriser la valeur négative.

**Étape 3.** Poser Construct Point (Vector > Point).

**Étape 4.** Relier chaque slider sur l'entrée correspondante X, Y, Z.

**Étape 5.** Vérifier l'aperçu du point dans la vue Rhino.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Laisser la valeur nord-sud bornée aux positifs : le repère se place au nord au lieu du sud. L'erreur révèle qu'on a réglé une valeur sans vérifier l'étendue autorisée.

### Pièges fréquents

- Slider borné à 0-100 : impossible d'atteindre -15.
- Confondre Construct Point et Deconstruct Point.

### Pour aller plus loin

- Ajouter un second point et tracer la Line entre les deux.
- Remplacer les sliders par un unique Panel multiligne.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-02_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-02_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-02.json` | Descripteur pour le plugin Magpie |
| `A-02_fiche.md` | La présente fiche |
| `A-02_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-02_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-02_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
