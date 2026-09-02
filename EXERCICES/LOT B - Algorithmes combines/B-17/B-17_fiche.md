# B-17 — Coque à nervures depuis une surface libre

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B5 · Design produit |
| **Référence au référentiel** | REF-069, REF-101, REF-049 |
| **Compétence visée** | Mesurer le développé d'un élément courbe, et non sa corde. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | A-45, B-04 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 24 composants |
| **Gamification associée** | G-22 Boss de fin de chapitre |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Extraire des sections structurelles d'une forme libre et préparer leur fabrication.

### Contexte

Les nervures se débitent à plat puis se cintrent. C'est leur longueur développée qu'on commande.

### Énoncé

> Sur la coque libre fournie, extrais 9 nervures transversales espacées régulièrement, donne-leur 12 mm d'épaisseur et 60 mm de hauteur vers l'intérieur, puis prépare leur mise à plat.

### Ce qui vous est fourni

Une surface de coque internalisée.

### Ce qui est attendu

32,34 m de nervure au total, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-17_sujet.gh`

### Barème

2 points pour les nervures, 2 points pour la mise à plat.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-17_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Bounding Box puis Deconstruct Box pour connaître l'étendue en X.

**Étape 2.** Générer 9 plans de coupe régulièrement espacés avec Range et YZ Plane.

**Étape 3.** Poser Brep | Plane pour obtenir les 9 courbes de section.

**Étape 4.** Décaler chaque section vers l'intérieur de 60 mm avec Offset Curve.

**Étape 5.** Construire la surface de nervure entre la section et son décalé avec Boundary Surfaces ou Loft.

**Étape 6.** Extruder de 12 mm pour donner l'épaisseur.

**Étape 7.** Aligner chaque nervure à plat par Orient vers le plan XY pour la mise à plat.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Prendre la corde : 28,80 m. L'arc d'une coque de 3 200 mm de corde et 700 mm de flèche mesure 3 594 mm, soit 12 % de plus. Trois mètres et demi de nervure manqueraient à la livraison — et le manque se répartit sur les neuf pièces, donc se voit tard.

### Pièges fréquents

- Offset Curve du mauvais côté : la nervure sort de la coque.
- Courbes de section multiples sur une coque non convexe : les traiter en arbre.
- Oublier de conserver le repérage des nervures après mise à plat.

### Pourquoi ce jeu de données

Une flèche de 700 pour 3 200 de corde donne un rayon de 2 179 mm : une coque franchement courbe, où l'écart entre arc et corde est net sans être caricatural.

### Pour aller plus loin

- Ajouter des encoches d'assemblage aux croisements avec des longerons.
- Exporter les développés en DXF.
- Faire varier l'espacement selon la courbure.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-17_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-17_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-17.json` | Descripteur pour le plugin Magpie |
| `B-17_fiche.md` | La présente fiche |
| `B-17_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-17_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-17_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
