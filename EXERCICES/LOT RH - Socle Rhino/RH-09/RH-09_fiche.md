# RH-09 — Une pièce imprimable

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH5 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-016, REF-018 |
| **Compétence visée** | Vérifier qu'une pièce respecte les contraintes dimensionnelles d'une machine avant de la lancer. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-08 |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Vérifier qu'une pièce respecte les contraintes dimensionnelles d'une machine avant de la lancer.

### Contexte

L'imprimante du bureau accepte 220 × 220 × 250 mm et ne tient pas une paroi sous 1,2 mm.

### Énoncé

> La pièce fournie doit passer sur cette machine. Établissez le facteur d'échelle maximal qui la fait tenir dans le volume d'impression, arrondi au centième inférieur, et donnez-le.

### Ce qui vous est fourni

Un fichier Rhino contenant la pièce — 380 × 260 × 195 mm hors tout — et les cotes du volume d'impression.

### Ce qui est attendu

0,57 — le facteur limitant vient de la longueur : 220 ÷ 380 vaut 0,5789, arrondi vers le bas au centième.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-09_sujet.gh`

### Barème

1 point si le facteur est juste et arrondi vers le bas.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-09_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Encadrer la pièce pour obtenir ses trois dimensions hors tout.

**Étape 2.** Calculer le rapport disponible sur chacun des trois axes.

**Étape 3.** Retenir le plus petit des trois : c'est lui qui limite.

**Étape 4.** Arrondir vers le bas, jamais au plus proche.

**Étape 5.** Contrôler, après mise à l'échelle, que la paroi la plus fine reste au-dessus de 1,2 mm.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Arrondir le facteur au plus proche plutôt qu'au inférieur. À 0,005 près, la pièce dépasse — et la machine s'en aperçoit après trois heures d'impression, pas avant. Le contexte impose le sens de l'arrondi, comme en A-06.

### Pièges fréquents

- Prendre la moyenne des trois rapports.
- Oublier que la mise à l'échelle réduit aussi les parois : une pièce qui rentre peut devenir non imprimable.

### Pourquoi ce jeu de données

Les trois rapports valent 0,579, 0,846 et 1,282 : le troisième axe passerait sans réduction, et prendre la moyenne des trois donnerait 0,90 — une pièce qui ne rentre pas. C'est le plus petit qui commande.

### Limite de la correction automatique

> 0,57 est le facteur GÉOMÉTRIQUE. Une impression réelle réserve en plus la place des supports et du bord de plateau, et une pièce à 0,57 exactement touche les parois : on descend en pratique un ou deux centièmes plus bas.

### Pour aller plus loin

- Faire pivoter la pièce de 90° et voir si le facteur s'améliore.
- Ajouter une marge de 2 mm sur chaque axe et refaire le calcul.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-09_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-09_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-09.json` | Descripteur pour le plugin Magpie |
| `RH-09_fiche.md` | La présente fiche |
| `RH-09_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-09_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-09_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
