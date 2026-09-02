# C-12 — Imbrication et export de fabrication

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C4 · Fabrication |
| **Référence au référentiel** | REF-113, REF-114, REF-087 |
| **Compétence visée** | Chiffrer un débit en tenant compte des espacements et des bords perdus, et en tirer un taux de chute défendable. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Expérimenté |
| **Durée cible** | 75 min |
| **Prérequis** | B-13, C-05 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 38 composants |
| **Gamification associée** | G-21 Golf de composants + G-23 Classement |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Boucler la chaîne conception-fabrication avec un livrable machine.

### Contexte

La plaque se commande à l'unité et le taux de chute figure au devis. Il engage l'entreprise.

### Énoncé

> Imbrique les 46 pièces découpées fournies dans des plaques de 3 000 × 1 500 mm avec un espacement de 8 mm entre pièces et 15 mm de bord de plaque. Produis le plan de découpe repéré, le nombre de plaques et le taux de matière utile, puis exporte en DXF par plaque.

### Ce qui vous est fourni

46 contours de pièces internalisés.

### Ce qui est attendu

27,36 % de chute, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-12_sujet.gh`

### Barème

4 points imbrication, 3 points indicateurs, 3 points export.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `C-12_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Préparer les contours : vérifier qu'ils sont fermés et plans avec un contrôle en amont.

**Étape 2.** Construire le contour de plaque utile en retirant 15 mm sur chaque bord.

**Étape 3.** Configurer OpenNest avec l'espacement de 8 mm et autoriser la rotation par pas de 90°.

**Étape 4.** Lancer l'imbrication et récupérer les pièces placées et leur numéro de plaque.

**Étape 5.** Compter les plaques avec Create Set sur les numéros de plaque.

**Étape 6.** Calculer le taux de matière utile : aire des pièces divisée par aire des plaques utilisées.

**Étape 7.** Repérer chaque pièce avec Text Tag 3D en conservant son repère d'origine.

**Étape 8.** Grouper les pièces par plaque avec un arbre et écrire un DXF par branche.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Calculer sur les surfaces nues, sans les 8 mm d'espacement ni les 15 mm de bord perdu : on conclut alors à TROIS plaques et 3 % de chute. Chaque pièce occupe en réalité 8 mm de plus dans chaque dimension, et la plaque perd 30 mm sur chaque côté — il en faut quatre. Une plaque manquante sur le bon de commande arrête la découpe en fin de série.

### Pièges fréquents

- Repères perdus car non triés dans le même ordre que les pièces placées.
- Espacement configuré comme un décalage de contour au lieu d'une distance entre pièces.
- Pièces non fermées silencieusement ignorées par l'imbrication.

### Pourquoi ce jeu de données

46 pièces de 255 à 925 mm dans des plaques de 3 × 1,5 m. Le jeu est calibré pour que l'espacement CHANGE le compte : 13,07 m² de pièces nues tiennent en trois plaques, mais 13,45 m² avec les espacements ne tiennent plus dans les 13,10 m² utiles de trois plaques. C'est le cas limite, et c'est celui où l'oubli se paie.

### Limite de la correction automatique

> Le taux est un MINORANT, comme en B-13 : il ne compte que les surfaces. Le plan d'imbrication réel ajoute la chute de placement, et c'est lui qui figure au bon de commande.

### Pour aller plus loin

- Comparer avec le calepinage manuel de l'exercice B-13.
- Ajouter une contrainte de sens de fil.
- Générer le parcours d'outil approximatif et estimer le temps de découpe.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `C-12_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `C-12_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `C-12.json` | Descripteur pour le plugin Magpie |
| `C-12_fiche.md` | La présente fiche |
| `C-12_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `C-12_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `C-12_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
