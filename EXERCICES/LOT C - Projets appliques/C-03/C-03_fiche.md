# C-03 — Gradins avec contrôle de visibilité

**Fiche d'exercice Magpie** · Lot C — Projets appliqués

| | |
|---|---|
| **Thématique** | C1 · Architecture |
| **Référence au référentiel** | REF-047, REF-079, REF-046, REF-060 |
| **Compétence visée** | Construire une progression dont chaque terme dépend du précédent ET de sa position, et en tirer une cote de projet. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 80 min |
| **Prérequis** | B-01, B-08 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 35 composants |
| **Gamification associée** | G-02 Barre de progression + G-20 Erreur à débusquer |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Construire une géométrie pilotée par une contrainte de performance vérifiée rang par rang.

### Contexte

Le dégagement visuel est une règle de sécurité et de confort. Il se vérifie rang par rang, et la hauteur du dernier décide de tout le volume construit.

### Énoncé

> Modélise 18 rangs de gradins de 850 mm de profondeur. La ligne de visée de chaque spectateur vers le point focal doit passer au moins 90 mm au-dessus de la tête du spectateur du rang précédent. Détermine automatiquement la hauteur de chaque marche et signale tout rang non conforme.

### Ce qui vous est fourni

Le point focal, la profondeur de rang et le nombre de rangs.

### Ce qui est attendu

3 105,01 mm — la hauteur du dernier rang, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`C-03_sujet.gh`

### Barème

4 points géométrie, 3 points calcul cumulatif, 3 points contrôle.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `C-03_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser le premier rang à une altitude de départ connue.

**Étape 2.** Pour chaque rang, calculer la hauteur minimale garantissant 90 mm de dégagement par géométrie de la ligne de visée.

**Étape 3.** Mettre en place le calcul cumulatif avec une boucle Anemone ou un composant Python, la hauteur d'un rang dépendant du précédent.

**Étape 4.** Générer les positions de tous les rangs.

**Étape 5.** Construire le profil en gradins par PolyLine puis extruder sur la largeur.

**Étape 6.** Recalculer a posteriori le dégagement réel de chaque rang.

**Étape 7.** Contrôler avec Larger Than et afficher le tableau de conformité.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Ajouter 90 mm à chaque rang : 1 530 mm au dernier, soit la moitié. Le dégagement ne s'ajoute pas — il se PROPAGE : chaque rang doit dépasser la ligne de visée du précédent, et cette ligne s'élève d'autant plus qu'on s'éloigne du foyer. La salle construite sur le calcul faux ne voit rien depuis le fond.

### Pièges fréquents

- Calcul non cumulatif : le dégagement se dégrade à partir du troisième rang.
- Hauteur d'œil du spectateur oubliée (environ 1 200 mm en position assise).
- Vérification effectuée sur la hauteur de marche et non sur le dégagement de visée.

### Pourquoi ce jeu de données

Dix-huit rangs de 850 mm, foyer à 4 200 mm : la hauteur croît de 108 mm au deuxième rang à plus de 200 au dernier. C'est cette accélération que la somme constante ignore, et elle donne un facteur deux sur la hauteur totale.

### Limite de la correction automatique

> Le calcul suppose un foyer ponctuel et des spectateurs alignés. Une salle réelle a une scène étendue et des rangs décalés, ce qui adoucit la progression — mais jamais au point de la rendre linéaire.

### Pour aller plus loin

- Comparer une courbe de gradins optimisée et une pente constante.
- Ajouter les circulations et les paliers.
- Calculer le volume de béton.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `C-03_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `C-03_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `C-03.json` | Descripteur pour le plugin Magpie |
| `C-03_fiche.md` | La présente fiche |
| `C-03_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `C-03_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `C-03_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
