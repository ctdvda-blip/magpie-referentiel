# RH-25 — Les volumes réellement étanches

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH4 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-019, REF-020, REF-021 |
| **Compétence visée** | Établir l'étanchéité d'une polysurface en tenant compte des arêtes non-manifold autant que des arêtes nues. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 14 min |
| **Prérequis** | RH-08 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-20 La chasse aux bugs |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir l'étanchéité d'une polysurface en tenant compte des arêtes non-manifold autant que des arêtes nues.

### Contexte

Un solide qui n'est pas étanche ne s'imprime pas. Le diagnostic se lit sur deux compteurs, et le second est régulièrement ignoré.

### Énoncé

> Le rapport d'analyse donne, pour douze polysurfaces, le nombre d'arêtes nues et le nombre d'arêtes non-manifold. Donnez le nombre de polysurfaces réellement étanches.

### Ce qui vous est fourni

Le rapport des douze polysurfaces et de leurs deux compteurs.

### Ce qui est attendu

6 polysurfaces sur 12 sont réellement étanches.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-25_sujet.gh`

### Barème

1 point si le compte est exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-25_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Tester l'égalité à zéro sur les arêtes nues.

**Étape 2.** Faire de même sur les arêtes non-manifold.

**Étape 3.** Combiner par un ET.

**Étape 4.** Compter les vrais.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Ne regarder que les arêtes nues : huit. Deux polysurfaces sans aucune arête nue portent des arêtes NON-MANIFOLD — trois faces partagent la même arête. Elles sont fermées et invalides : aucun trancheur n'en tirera un parcours d'outil.

### Pièges fréquents

- Ne tester qu'un des deux compteurs.
- Employer un OU au lieu d'un ET.

### Pourquoi ce jeu de données

Douze polysurfaces, dont deux à zéro arête nue mais avec des non-manifold, et une qui cumule les deux défauts. L'écart entre les deux réponses tient à ces deux cas — les seuls que le compteur d'arêtes nues déclare bons.

### Limite de la correction automatique

> Les deux compteurs à zéro rendent une polysurface FERMÉE. Ils ne disent rien des faces retournées ni des auto-intersections : un solide étanche peut encore être impossible à imprimer, et c'est l'objet de RH-08.

### Pour aller plus loin

- Donner le nombre de polysurfaces à corriger en priorité.
- Distinguer les défauts réparables des autres.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-25_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-25_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-25.json` | Descripteur pour le plugin Magpie |
| `RH-25_fiche.md` | La présente fiche |
| `RH-25_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-25_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-25_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
