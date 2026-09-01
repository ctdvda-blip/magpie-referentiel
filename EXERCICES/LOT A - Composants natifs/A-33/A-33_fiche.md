# A-33 — Plans de construction

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A8 · Géométrie vectorielle et filaire |
| **Référence au référentiel** | REF-062 |
| **Compétence visée** | Poser un repère orienté et y construire une géométrie. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-32 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-07 Étoiles de performance |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Poser un repère orienté et y construire une géométrie.

### Contexte

Une buse traverse un mur en biais : son tracé se pose dans un plan incliné, pas dans le plan horizontal.

### Énoncé

> Le percement est circulaire, de 20 de rayon, centré à 50 au-dessus de l'origine, et son plan est incliné de 30° autour de l'axe X. Construisez ce tracé.

### Ce qui vous est fourni

Canvas vide.

### Ce qui est attendu

Un cercle de rayon 20 dans le plan incliné demandé.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-33_sujet.gh`

### Barème

1 point si le cercle respecte position et inclinaison.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-33_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser XY Plane et lui donner l'origine (0;0;50) via Construct Point.

**Étape 2.** Poser Rotate Plane avec un angle de 30° converti en radians (Radians ou saisie 30 avec le composant Degrees).

**Étape 3.** Poser Circle et brancher le plan sur P et 20 sur R.

**Étape 4.** Contrôler visuellement l'inclinaison dans la vue Rhino.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Construire le cercle à plat puis le faire tourner : le résultat est visuellement identique mais le repère local ne suit pas, et tout ce qu'on y accrochera ensuite sera mal orienté.

### Pièges fréquents

- Grasshopper travaille en radians : saisir 30 donne 30 radians.
- Confondre l'origine du plan et le centre du cercle quand on décale ensuite.

### Pour aller plus loin

- Construire le plan directement avec Construct Plane et deux vecteurs.
- Décomposer le plan avec Deconstruct Plane pour lire ses axes.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-33_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-33_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-33.json` | Descripteur pour le plugin Magpie |
| `A-33_fiche.md` | La présente fiche |
| `A-33_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-33_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-33_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
