# C-09 — Pavage de pierres sur surface libre

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C3 · Joaillerie |
| **Référence au référentiel** | REF-068, REF-101, REF-080, REF-045 |
| **Compétence visée** | Estimer combien d'éléments circulaires tiennent sur une surface en tenant compte de l'écart imposé entre eux. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Expérimenté |
| **Durée cible** | 85 min |
| **Prérequis** | B-04, C-08 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 48 composants |
| **Gamification associée** | G-13 Casino motifs assortis + G-16 Chasse au trésor |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Répartir des éléments de tailles variées sur une surface courbe en respectant des distances minimales.

### Contexte

Le métal entre deux pierres tient le serti. Sous 0,3 mm il cède, et la pierre part.

### Énoncé

> Pave la surface libre fournie de pierres rondes de 1,2 à 2,5 mm réparties de manière quasi aléatoire mais sans jamais laisser moins de 0,3 mm de métal entre deux pierres voisines. Perce ensuite les logements coniques correspondants.

### Ce qui vous est fourni

Une surface libre internalisée et un slider de densité.

### Ce qui est attendu

64 pierres.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-09_sujet.gh`

### Barème

4 points répartition, 3 points respect de la distance, 3 points logements.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `C-09_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Semer des points sur la surface avec Populate Geometry.

**Étape 2.** Attribuer un diamètre aléatoire à chaque point avec Random dans le domaine 1,2 à 2,5.

**Étape 3.** Calculer les distances entre paires de points voisins avec Closest Points.

**Étape 4.** Comparer chaque distance à la somme des deux rayons plus 0,3 mm.

**Étape 5.** Éliminer itérativement les points en conflit avec un Cull Pattern piloté par ce test, dans une boucle Anemone.

**Étape 6.** Récupérer les normales locales avec Evaluate Surface et construire un plan par pierre.

**Étape 7.** Modéliser chaque pierre et son logement conique dans ce plan.

**Étape 8.** Percer la surface épaissie avec Solid Difference.

**Étape 9.** Recontrôler a posteriori que la distance minimale est respectée.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Diviser la surface par l'aire d'une pierre : 96. Deux erreurs se cumulent — l'écart de métal est ignoré, et des disques ne pavent pas un plan. La maille hexagonale la plus dense laisse 9 % de vide même sans écart ; avec 0,3 mm de métal, chaque pierre occupe 4,00 mm² au lieu de 2,69.

### Pièges fréquents

- Test de distance effectué sur les centres sans tenir compte des rayons.
- Élimination en une seule passe : de nouveaux conflits apparaissent après suppression.
- Logements percés perpendiculairement au plan global et non à la normale locale.

### Pourquoi ce jeu de données

Une surface de 260 mm², des pierres de 1,85 mm et 0,3 mm de métal : le pas monte à 2,15 mm. Les deux réponses, 64 et 96, sont dans un rapport de 1,5 — assez pour que la commande de pierres soit franchement fausse.

### Limite de la correction automatique

> 64 est le compte d'une maille régulière. La consigne demande une répartition « quasi aléatoire », qui en fait toujours tenir un peu moins : le chiffre est un plafond, et c'est ce qu'il faut savoir en le donnant au client.

### Pour aller plus loin

- Imposer une densité variable pilotée par un attracteur.
- Trier les pierres par taille et produire la nomenclature de commande.
- Calculer le poids en carats.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `C-09_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `C-09_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `C-09.json` | Descripteur pour le plugin Magpie |
| `C-09_fiche.md` | La présente fiche |
| `C-09_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `C-09_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `C-09_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
