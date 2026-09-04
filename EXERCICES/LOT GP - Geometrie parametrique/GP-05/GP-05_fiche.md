# GP-05 — La chaîne de cotes d'une façade

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP1 · Plan paramétrique |
| **Référence au référentiel** | REF-065, REF-066 |
| **Compétence visée** | Produire une cotation en chaîne qui se recalcule avec le modèle, en distinguant ce qui se mesure d'un voisin à l'autre de ce qui se repère depuis une origine unique. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | GP-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-08 Relevé contradictoire |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire une cotation en chaîne qui se recalcule avec le modèle, en distinguant ce qui se mesure d'un voisin à l'autre de ce qui se repère depuis une origine unique.

### Contexte

Le poseur implante les percements d'une façade au décamètre, depuis un unique point de référence : c'est la seule manière de ne pas cumuler les erreurs de report.

### Énoncé

> Le bureau d'études fournit les entraxes des sept percements, mesurés chacun depuis le précédent, et la distance du premier au point de référence. Donnez la cote du dernier percement telle qu'elle doit figurer au plan de pose, en millimètres.

### Ce qui vous est fourni

La distance du premier percement au point de référence, et les sept entraxes successifs, en millimètres.

### Ce qui est attendu

8 955 mm — la position du dernier percement, comptée depuis le point de référence.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-05_sujet.gh`

### Barème

1 point si la cote finale est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `GP-05_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Distinguer la donnée relative (l'entraxe) de la donnée absolue (la position depuis l'origine).

**Étape 2.** Cumuler les entraxes.

**Étape 3.** Ajouter l'écart d'origine.

**Étape 4.** Vérifier que la première cote vaut bien l'écart d'origine, et non zéro.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Reporter le dernier entraxe (1 290 mm) ou la somme des seuls entraxes (8 535 mm). Le premier oublie que l'entraxe est une distance relative ; le second oublie l'écart d'origine. Sur le chantier, les deux se traduisent par un percement au mauvais endroit — et l'un des deux le met à 420 mm près, un écart assez petit pour n'être vu qu'une fois la menuiserie livrée.

### Pièges fréquents

- Confondre entraxe et cote cumulée.
- Oublier l'écart entre le point de référence et le premier percement.
- Coter chaque percement depuis son voisin sur le plan de pose : les erreurs de report s'additionnent alors.

### Pourquoi ce jeu de données

Sept entraxes irréguliers, aucun multiple d'un pas commun : la cote finale ne se retrouve pas de tête. L'écart d'origine de 420 mm est du même ordre qu'un tableau de baie, donc plausible et facile à oublier.

### Limite de la correction automatique

> L'exercice valide la cote finale, pas la cotation entière. Une chaîne juste sur son dernier maillon peut être fausse au milieu : le formateur regarde le graphe, pas seulement la réponse.

### Pour aller plus loin

- Produire la chaîne complète des huit cotes, et non la seule dernière.
- Ajouter un percement au milieu et vérifier que toutes les cotes suivantes se recalculent seules.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `GP-05_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `GP-05_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `GP-05.json` | Descripteur pour le plugin Magpie |
| `GP-05_fiche.md` | La présente fiche |
| `GP-05_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `GP-05_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `GP-05_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
