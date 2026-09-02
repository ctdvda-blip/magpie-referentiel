# B-15 — Optimisation d'une découpe linéaire

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B4 · Données, métrés et livrables |
| **Référence au référentiel** | REF-044, REF-045, REF-082 |
| **Compétence visée** | Appliquer une heuristique de découpe et mesurer l'écart entre son résultat et la borne théorique. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | B-13 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 18 composants |
| **Gamification associée** | G-23 Duel et classement + G-03 Compte à rebours |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mettre en œuvre un algorithme de placement glouton et en mesurer la performance.

### Contexte

La barre se commande à l'unité. La règle du plus grand d'abord est celle de l'atelier, parce qu'elle se tient de tête.

### Énoncé

> Débite 30 pièces de longueurs variées dans des barres de 6 000 mm. Applique la règle du plus grand d'abord et affiche le nombre de barres consommées ainsi que la chute totale.

### Ce qui vous est fourni

Une liste de 30 longueurs internalisée.

### Ce qui est attendu

12 barres.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-15_sujet.gh`

### Barème

2 points pour l'algorithme, 1 point pour le nombre de barres, 1 point pour la chute.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-15_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Trier les longueurs par ordre décroissant avec Sort List puis Reverse List.

**Étape 2.** Mettre en place une boucle Anemone : à chaque itération, tenter de placer la pièce suivante dans une barre ouverte.

**Étape 3.** Si aucune barre ne peut l'accueillir, ouvrir une nouvelle barre.

**Étape 4.** Accumuler l'état des barres dans la boucle avec un paramètre de rebouclage.

**Étape 5.** En sortie de boucle, compter les barres et sommer les chutes.

**Étape 6.** Afficher les deux valeurs.

**Étape 7.** Comparer avec le minimum théorique (somme des longueurs divisée par 6000, arrondi supérieur).

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Diviser la longueur totale par celle d'une barre : 11. C'est la BORNE théorique, et aucune découpe ne l'atteint ici — les longueurs ne se combinent pas pour remplir onze barres. Annoncer 11 revient à promettre un rendement qu'aucun débit ne donnera.

### Pièges fréquents

- Boucle sans condition d'arrêt : Grasshopper se fige.
- Oublier le trait de scie dans le cumul.
- Tri croissant au lieu de décroissant : le résultat se dégrade nettement.

### Pourquoi ce jeu de données

30 longueurs pour 65 120 mm, soit 10,85 barres en surface : la borne est 11, et la règle du plus grand d'abord en consomme 12. L'écart d'une seule barre est le cas intéressant — assez petit pour qu'on croie à une erreur de calcul, assez réel pour se payer.

### Limite de la correction automatique

> 12 est le résultat de CETTE heuristique. Un placement optimal pourrait faire mieux — le trouver est un problème dont on ne connaît pas de solution rapide, et c'est précisément pourquoi l'atelier emploie une règle simple.

### Pour aller plus loin

- Comparer avec une stratégie du meilleur ajustement.
- Écrire l'algorithme en composant Python plutôt qu'en boucle Anemone.
- Autoriser plusieurs longueurs de barre commerciale.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-15_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-15_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-15.json` | Descripteur pour le plugin Magpie |
| `B-15_fiche.md` | La présente fiche |
| `B-15_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-15_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-15_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
