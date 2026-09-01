# MP-05 — Mesurer avant d'optimiser

**Fiche d'exercice Magpie** · Lot MP — Méthode, performance et évènements

| | |
|---|---|
| **Thématique** | MP2 · Organisation et performance |
| **Référence au référentiel** | REF-150 |
| **Compétence visée** | Fonder une optimisation sur un relevé de temps, et non sur l'intuition de ce qui coûte cher. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | MP-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-13 Chronomètre |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Fonder une optimisation sur un relevé de temps, et non sur l'intuition de ce qui coûte cher.

### Contexte

La définition met huit secondes à répondre. On a une après-midi pour la rendre utilisable, et douze composants candidats.

### Énoncé

> Le relevé de temps des douze composants vous est fourni, en millisecondes. Donnez la part du composant le plus lourd dans le temps total, en pour cent, arrondie à l'entier.

### Ce qui vous est fourni

Les douze composants et le temps mesuré pour chacun.

### Ce qui est attendu

61 % — la part du maillage adaptatif.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`MP-05_sujet.gh`

### Barème

1 point si la part est juste à l'entier près.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `MP-05_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Sommer les temps.

**Étape 2.** Trouver le plus grand.

**Étape 3.** En faire le rapport au total, puis un pourcentage.

**Étape 4.** Arrondir à l'entier.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Répartir l'effort sur les composants qu'on soupçonne. Un seul composant pèse 61 % du temps : le diviser par dix ferait gagner 55 % à lui seul, quand optimiser les onze autres jusqu'à les annuler n'en ferait gagner que 39.

### Pièges fréquents

- Optimiser sans mesurer.
- Prendre la moyenne pour la part du plus lourd.
- Confondre le plus lourd et le plus fréquent.

### Pourquoi ce jeu de données

Douze composants dont un à 4 820 ms et le suivant à 1 310 : le profil réel d'une définition, où le temps se concentre au lieu de se répartir. Les neuf plus légers cumulés pèsent moins d'un quart du plus lourd.

### Limite de la correction automatique

> Le relevé dit où le temps passe, pas comment le réduire. Un maillage adaptatif se règle avant de se réécrire — et parfois il ne se réduit pas.

### Pour aller plus loin

- Chiffrer le gain total si le plus lourd était divisé par dix.
- Trouver combien de composants il faut cumuler pour atteindre la moitié du temps.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `MP-05_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `MP-05_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `MP-05.json` | Descripteur pour le plugin Magpie |
| `MP-05_fiche.md` | La présente fiche |
| `MP-05_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `MP-05_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `MP-05_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
