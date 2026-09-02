# C-10 — Motif gravé génératif sur bijou

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C3 · Joaillerie |
| **Référence au référentiel** | REF-115, REF-095, REF-069 |
| **Compétence visée** | Dimensionner une partition de surface en tenant compte de ce que les séparations consomment. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Expérimenté |
| **Durée cible** | 80 min |
| **Prérequis** | B-10, C-08 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 45 composants |
| **Gamification associée** | G-27 Narration Serengeti + G-09 Récompense cachée |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire un motif non répétitif contrôlé par des règles, puis le graver physiquement.

### Contexte

Le filet entre cellules doit rester gravable. Trop fin, il disparaît au polissage.

### Énoncé

> Génère sur le corps de bague un motif de type Voronoï dont les cellules mesurent entre 0,8 et 2,2 mm², sépare les cellules par un filet de 0,25 mm, grave à 0,3 mm de profondeur, et fais en sorte que le motif boucle sans rupture visible.

### Ce qui vous est fourni

La bague de l'exercice C-08 et un slider de densité de motif.

### Ce qui est attendu

77 cellules.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-10_sujet.gh`

### Barème

4 points motif, 3 points contraintes d'aire, 3 points raccord.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `C-10_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Construire la surface développée du corps de bague (rectangle circonférence × largeur).

**Étape 2.** Semer des points avec Populate 2D dans ce rectangle, en dupliquant une bande aux deux extrémités pour assurer la continuité du raccord.

**Étape 3.** Générer le diagramme de Voronoï sur ces points.

**Étape 4.** Décaler chaque cellule vers l'intérieur de 0,125 mm avec Offset Curve pour créer le filet.

**Étape 5.** Mesurer l'aire de chaque cellule et éliminer celles hors du domaine 0,8 à 2,2 mm².

**Étape 6.** Appliquer le motif sur la surface de la bague par Surface Morph.

**Étape 7.** Extruder vers l'intérieur de 0,3 mm et soustraire avec Solid Difference.

**Étape 8.** Vérifier la continuité au raccord et régler la densité par Galapagos si nécessaire.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Diviser la surface par l'aire visée d'une cellule : 112. Le filet de 0,25 mm court AUTOUR de chaque cellule : le pas réel n'est pas le côté de la cellule mais le côté plus le filet, ce qui fait perdre un tiers des cellules. Le motif calculé sans lui arrive trop dense, et le filet disparaît.

### Pièges fréquents

- Points semés uniquement dans le rectangle : le raccord présente une rupture nette.
- Offset produisant des cellules dégénérées pour les petites cellules.
- Profondeur de gravure supérieure à l'épaisseur locale de l'anneau.

### Pourquoi ce jeu de données

Une cellule de 1,5 mm² fait 1,22 mm de côté ; avec le filet le pas monte à 1,47 mm, soit une aire de 2,17 mm² par cellule — 45 % de plus. C'est la marge que le filet coûte, et elle est loin d'être négligeable à cette échelle.

### Pour aller plus loin

- Remplacer le Voronoï par un motif hexagonal déformé.
- Faire varier la profondeur de gravure selon la position.
- Exporter en STL pour impression cire.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `C-10_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `C-10_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `C-10.json` | Descripteur pour le plugin Magpie |
| `C-10_fiche.md` | La présente fiche |
| `C-10_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `C-10_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `C-10_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
