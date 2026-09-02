# G-25 — L'animation de la solution

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G6 · Sensations et immersion |
| **Référence au référentiel** | REF-090, REF-093, REF-067 |
| **Compétence visée** | Piloter une révélation progressive par un paramètre unique et savoir lire un état INTERMÉDIAIRE, pas seulement le final. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | A-37, B-05 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 14 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Rendre visible le déroulement d'un algorithme plutôt que son seul résultat.

### Contexte

Animer la construction d'un algorithme le rend enseignable : on voit dans quel ORDRE les choses arrivent, ce que le résultat final ne dit jamais.

### Énoncé

> Anime la construction de la structure : les 40 barres doivent apparaître une par une en trois secondes, puis la structure entière change de couleur. Le pilotage se fait par un unique slider de 0 à 1.

### Ce qui vous est fourni

Une structure de 40 barres déjà modélisée.

### Ce qui est attendu

8 508 mm — la longueur cumulée des barres visibles à t = 0,375.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-25_sujet.gh`

### Barème

2 points : 1 pour l'état final, 1 pour l'état intermédiaire.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-25_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Multiplier la valeur du slider par 40 et arrondir pour obtenir le nombre de barres visibles.

**Étape 2.** Construire le domaine 0 à ce nombre avec Construct Domain.

**Étape 3.** Poser Sub List pour ne conserver que les barres de ce domaine.

**Étape 4.** Poser Custom Preview avec un Gradient piloté par le même slider.

**Étape 5.** Vérifier les deux états de contrôle, à 0,5 puis à 1.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Vérifier l'animation à t = 1 seulement. À t = 1 toute animation juste ou fausse affiche les quarante barres : l'état final ne prouve rien. C'est l'état intermédiaire qui dit si le pilotage est réellement progressif, et c'est lui qu'on demande.

### Pièges fréquents

- Sub List sur un domaine non entier : le nombre de barres devient imprévisible.
- Timer branché en permanence : la définition recalcule sans arrêt et devient inutilisable.

### Pourquoi ce jeu de données

Quarante barres de 300 à 1 900 mm, révélées de la plus courte à la plus longue : à t = 0,375, quinze barres sont visibles et pèsent 8 508 mm sur 44 028 au total, soit 19 % de la longueur pour 37,5 % des barres. Un cumul proportionnel au temps — 16 510 mm — signalerait une révélation dans le désordre.

### Limite de la correction automatique

> Trois secondes de durée sont une consigne de CONFORT, non vérifiable : la vitesse de lecture du slider dépend de la machine et de la complexité de la définition.

### Pour aller plus loin

- Animation par vagues plutôt que séquentielle.
- Export de l'animation en séquence d'images.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-25_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-25_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-25.json` | Descripteur pour le plugin Magpie |
| `G-25_fiche.md` | La présente fiche |
| `G-25_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-25_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-25_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
