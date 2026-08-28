# MP-02 — Trouver ce qui coûte le temps de calcul

**Fiche d'exercice Magpie** · Lot MP — Méthode, performance et évènements

| | |
|---|---|
| **Thématique** | MP2 · Performance d'exécution |
| **Référence au référentiel** | REF-089 |
| **Compétence visée** | Localiser le composant qui coûte le temps de recalcul, plutôt que d'optimiser au hasard. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | MP-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-01 Score visible |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Localiser le composant qui coûte le temps de recalcul, plutôt que d'optimiser au hasard.

### Contexte

Une définition met plusieurs secondes à se recalculer à chaque mouvement de curseur, et le client attend devant l'écran.

### Énoncé

> Les temps de recalcul des 20 composants d'une définition vous sont fournis, en millisecondes. Donnez la part du temps total que représentent les trois composants les plus coûteux, en pourcentage arrondi à l'entier.

### Ce qui vous est fourni

Les 20 temps mesurés, en millisecondes, dans l'ordre du profil affiché par Grasshopper.

### Ce qui est attendu

La part des trois composants les plus coûteux, en pourcentage entier.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`MP-02_sujet.gh`

### Barème

1 point si la part est juste à l'entier près.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `MP-02_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Sommer les vingt temps pour obtenir le total.

**Étape 2.** Trier les temps par ordre décroissant.

**Étape 3.** Prélever les trois premiers et les sommer.

**Étape 4.** Rapporter au total et convertir en pourcentage.

**Étape 5.** Arrondir à l'entier, et en tirer la conclusion : c'est là, et seulement là, qu'il faut travailler.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Optimiser les composants nombreux plutôt que les composants lents. Dix-sept composants du relevé coûtent moins de 15 ms chacun : les régler tous ne fera rien gagner. Trois en coûtent presque tout — et c'est contre-intuitif tant qu'on n'a pas mesuré.

### Pièges fréquents

- Trier sans inverser : on prend les trois plus rapides.
- Conclure que la définition est « globalement lente » : elle ne l'est pas, trois composants le sont.

### Pourquoi ce jeu de données

Le relevé est volontairement très déséquilibré : trois composants au-dessus de 1 800 ms, dix-sept sous 15 ms. C'est la répartition réelle d'une définition lente, et c'est ce qui rend la mesure indispensable.

### Pour aller plus loin

- Chiffrer le gain si l'un des trois passait à 100 ms.
- Mesurer le profil réel d'une de vos définitions et refaire l'analyse.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `MP-02_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `MP-02_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `MP-02.json` | Descripteur pour le plugin Magpie |
| `MP-02_fiche.md` | La présente fiche |
| `MP-02_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `MP-02_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `MP-02_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
