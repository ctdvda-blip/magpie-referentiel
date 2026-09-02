# C-07 — Table de nuit configurable

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C2 · Design de mobilier |
| **Référence au référentiel** | REF-070, REF-072, REF-082, REF-106 |
| **Compétence visée** | Établir un prix par composition, en appliquant chaque coefficient sur son assiette. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Expérimenté |
| **Durée cible** | 80 min |
| **Prérequis** | B-06, B-07 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 48 composants |
| **Gamification associée** | G-28 Avatar + G-10 Coffre à butin |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire un configurateur complet, avec variantes discrètes et contrôle de cohérence.

### Contexte

Le configurateur affiche un prix à chaque changement. Un coefficient mal appliqué se voit sur des milliers de configurations, jamais sur celle qu'on a testée.

### Énoncé

> Réalise un configurateur de table de nuit : 4 types de pieds au choix, de 1 à 3 tiroirs, deux matériaux avec des épaisseurs différentes. Le modèle doit rester valide dans toutes les combinaisons et produire son prix estimatif.

### Ce qui vous est fourni

Une Value List de types de pied, un slider de nombre de tiroirs, une Value List de matériau.

### Ce qui est attendu

1 033,76 € pour la combinaison compas, trois tiroirs, noyer.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-07_sujet.gh`

### Barème

4 points configurateur, 3 points robustesse, 3 points chiffrage.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `C-07_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Modéliser les quatre familles de pieds dans des groupes distincts.

**Étape 2.** Sélectionner la famille active avec Stream Filter piloté par la Value List.

**Étape 3.** Déduire l'épaisseur de panneau du matériau choisi via Member Index dans une table.

**Étape 4.** Répartir automatiquement les tiroirs sur la hauteur disponible selon leur nombre.

**Étape 5.** Appliquer les jeux fonctionnels et vérifier l'absence de collision dans chaque configuration.

**Étape 6.** Mesurer les volumes par matériau et appliquer les prix unitaires.

**Étape 7.** Composer le libellé de configuration et le prix dans un Panel.

**Étape 8.** Balayer systématiquement les 24 combinaisons pour vérifier qu'aucune ne produit d'erreur.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> N'appliquer la majoration de matière qu'au prix de base : 858,20 €. Le noyer coûte plus cher pour TOUT le meuble — pieds et tiroirs compris. L'écart de 175 € est un sixième du prix, et il est toujours dans le même sens : à la perte.

### Pièges fréquents

- Une seule combinaison testée : les cas limites (3 tiroirs, panneau épais) échouent.
- Stream Filter alimenté par une Value List dont les valeurs ne sont pas des entiers consécutifs.
- Hauteur de tiroir négative quand la hauteur disponible est insuffisante.

### Pourquoi ce jeu de données

Quatre types de pieds, un à trois tiroirs, deux matières : vingt-quatre combinaisons. Celle qui est demandée cumule le pied le plus cher, le maximum de tiroirs et la matière majorée — c'est là que l'erreur de coefficient coûte le plus, donc là qu'il faut la chercher.

### Limite de la correction automatique

> Le barème est linéaire. Un vrai configurateur applique des remises par quantité et des suppléments non linéaires, mais la question de l'assiette du coefficient reste la même.

### Pour aller plus loin

- Ajouter une poignée au choix.
- Publier le configurateur sur le web avec ShapeDiver.
- Générer la fiche produit PDF.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `C-07_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `C-07_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `C-07.json` | Descripteur pour le plugin Magpie |
| `C-07_fiche.md` | La présente fiche |
| `C-07_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `C-07_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `C-07_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
