# C-11 — Déroulé de tôle pliée avec compensation

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C4 · Fabrication |
| **Référence au référentiel** | REF-116, REF-115, REF-082 |
| **Compétence visée** | Calculer le développé d'une tôle à plis multiples, en comptant le bon nombre de plis par segment. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Expérimenté |
| **Durée cible** | 80 min |
| **Prérequis** | B-17, C-05 |
| **Mode de validation** | NumericTolerance — tolérance 0.1 |
| **Solution de référence** | 40 composants |
| **Gamification associée** | G-20 Erreur à débusquer + G-03 Compte à rebours |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Calculer un développé industriel exact et produire le plan de pliage.

### Contexte

La bande part au débit avant pliage. Cinq plis, c'est cinq occasions de se tromper d'un rayon.

### Énoncé

> La pièce en tôle de 2 mm comporte 5 plis à 90° de rayon intérieur 3 mm. Produis son développé en tenant compte du facteur K de 0,44, cote les lignes de pli et vérifie que la longueur développée calculée correspond à la longueur mesurée sur le développé.

### Ce qui vous est fourni

Une pièce en tôle pliée internalisée et les paramètres matière.

### Ce qui est attendu

500,47 mm de développé, à 0,1 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-11_sujet.gh`

### Barème

4 points développé, 3 points compensation, 3 points cotation.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `C-11_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Identifier les faces planes et les zones de pli par analyse des normales.

**Étape 2.** Calculer pour chaque pli la longueur de la fibre neutre : (rayon intérieur + K × épaisseur) × angle en radians.

**Étape 3.** Sommer les longueurs des faces planes et des fibres neutres pour obtenir la longueur développée théorique.

**Étape 4.** Déplier la pièce face par face avec Orient successifs, ou utiliser un composant de dépliage.

**Étape 5.** Insérer les longueurs de fibre neutre entre les faces dépliées.

**Étape 6.** Tracer les lignes de pli et les coter avec Text Tag 3D en indiquant le sens de pliage.

**Étape 7.** Mesurer la longueur du développé obtenu et la comparer à la valeur théorique.

**Étape 8.** Exporter le développé en DXF.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Additionner les cotes extérieures : 520 mm, soit près de 20 mm de trop. Mais l'erreur la plus coûteuse est ailleurs : retirer rayon et épaisseur UNE fois par segment. Les quatre segments intérieurs portent DEUX plis chacun, les deux segments d'extrémité un seul — c'est ce décompte qui fait la différence entre une bande juste et une bande courte de 20 mm.

### Pièges fréquents

- Utiliser le rayon extérieur au lieu du rayon intérieur dans la formule.
- Angle de pli confondu avec l'angle d'ouverture (90° de pli correspond à un angle complémentaire selon la convention).
- Facteur K appliqué à l'épaisseur totale au lieu de la position de la fibre neutre.

### Pourquoi ce jeu de données

Six segments et cinq plis : deux extrémités à un pli, quatre segments intérieurs à deux plis. Le facteur K de 0,44 est celui d'un acier doux plié sur un rayon supérieur à l'épaisseur. Le développé, 500,47, est inférieur à la somme des cotes — contre-intuitif, et c'est bien le cas général.

### Limite de la correction automatique

> Cinq plis à 90° dans le même sens font une pièce qui se referme presque. La faisabilité du pliage — l'ordre des plis, la place de l'outil — n'est pas jugée ici, et c'est elle qui décide en atelier.

### Pour aller plus loin

- Traiter des plis à angles quelconques.
- Gérer plusieurs épaisseurs et facteurs K.
- Ajouter les dégagements de pli aux angles.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `C-11_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `C-11_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `C-11.json` | Descripteur pour le plugin Magpie |
| `C-11_fiche.md` | La présente fiche |
| `C-11_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `C-11_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `C-11_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
