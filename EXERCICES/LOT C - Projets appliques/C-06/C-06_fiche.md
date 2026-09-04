# C-06 — Chaise à assise en lamelles courbes

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C2 · Design de mobilier |
| **Référence au référentiel** | REF-069, REF-064, REF-074 |
| **Compétence visée** | Vérifier qu'une forme voulue respecte une contrainte de matière, en comparant un rayon obtenu à un rayon admissible. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 85 min |
| **Prérequis** | B-16, B-17 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 42 composants |
| **Gamification associée** | G-26 Feedback visuel + G-07 Étoiles |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Conjuguer une forme ergonomique libre et une contrainte de fabrication en lamelles droites.

### Contexte

Une lamelle de contreplaqué cintrée trop serré casse au pressage. Le rapport rayon sur épaisseur est ce que l'atelier regarde.

### Énoncé

> Modélise l'assise et le dossier d'une chaise en 22 lamelles de 40 mm de large et 8 mm d'épaisseur suivant deux courbes directrices. Le rayon de courbure de chaque lamelle ne doit jamais descendre sous 350 mm, limite de cintrage du matériau : signale toute lamelle non conforme.

### Ce qui vous est fourni

Deux courbes directrices internalisées.

### Ce qui est attendu

371,73 mm — le rayon de la directrice, à 0,01 près, à comparer aux 200 mm admissibles.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-06_sujet.gh`

### Barème

4 points géométrie, 3 points contrôle de courbure, 3 points conformité générale.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `C-06_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Diviser les deux directrices en 22 stations.

**Étape 2.** Construire la courbe de chaque lamelle par Interpolate entre les points correspondants.

**Étape 3.** Récupérer les plans perpendiculaires au départ de chaque lamelle.

**Étape 4.** Construire la section de 40 × 8 mm et la balayer le long de chaque lamelle avec Sweep 1.

**Étape 5.** Échantillonner chaque lamelle avec Divide Curve et mesurer la courbure.

**Étape 6.** Convertir en rayon de courbure et prendre le minimum par lamelle avec Bounds.

**Étape 7.** Comparer à 350 mm avec Larger Than et afficher les lamelles non conformes en rouge.

**Étape 8.** Ajuster les directrices jusqu'à conformité générale.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Prendre la flèche pour le rayon, ou la demi-corde. Le rayon d'un arc se retrouve de sa corde ET de sa flèche : (c²/4 + f²) ÷ 2f. Ni 65 ni 210 ne sont le rayon, et les deux sont sous la limite admissible — l'assise serait déclarée infaisable alors qu'elle passe avec 86 % de marge.

### Pièges fréquents

- Courbure mesurée sur un échantillonnage trop grossier : le point critique est manqué.
- Confondre courbure et rayon de courbure (l'un est l'inverse de l'autre).
- Sections non perpendiculaires : les lamelles se vrillent.

### Pourquoi ce jeu de données

Corde de 420 et flèche de 65 donnent 371,7 mm de rayon, contre 200 admissibles pour une lamelle de 8 mm au rapport 25. La marge est confortable, à dessein : l'exercice porte sur la façon de CONCLURE, pas sur un cas limite.

### Limite de la correction automatique

> Le rayon vérifie la faisabilité du CINTRAGE. Il ne dit rien du retour élastique : une lamelle relâchée s'ouvre de quelques degrés, et le gabarit se creuse en conséquence. C'est un réglage d'atelier, pas un calcul.

### Pour aller plus loin

- Ajouter le piètement et vérifier la stabilité par le centre de gravité.
- Faire varier la largeur de lamelle selon la zone.
- Produire les gabarits de cintrage.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `C-06_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `C-06_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `C-06.json` | Descripteur pour le plugin Magpie |
| `C-06_fiche.md` | La présente fiche |
| `C-06_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `C-06_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `C-06_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
