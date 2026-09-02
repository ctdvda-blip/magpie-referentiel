# A-09 — Valeur nulle et propagation

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A2 · Types, conversion et valeurs |
| **Référence au référentiel** | REF-055 |
| **Compétence visée** | Écarter les valeurs manquantes d'un relevé et dénombrer ce qui reste exploitable. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-07 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-16 Chasse au trésor sur le canvas |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Écarter les valeurs manquantes d'un relevé et dénombrer ce qui reste exploitable.

### Contexte

Un relevé de hauteurs d'allège importé d'un tableur comporte des cellules restées vides.

### Énoncé

> Le relevé porte sur 24 baies, mais certaines lignes n'ont pas été renseignées. Indiquez combien de hauteurs sont réellement exploitables.

### Ce qui vous est fourni

Le relevé des 24 baies, cellules non renseignées comprises.

### Ce qui est attendu

Un nombre entier : combien de hauteurs sont réellement renseignées.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-09_sujet.gh`

### Barème

1 point si le Panel affiche 6.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-09_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 18 — le nombre de hauteurs réellement renseignées.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Brancher Null Item (Sets > Tree) pour localiser les nulles.

**Étape 2.** Poser Clean Tree avec Remove Nulls activé.

**Étape 3.** Brancher List Length sur la sortie nettoyée.

**Étape 4.** Relier vers un Panel : 6 éléments valides.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter la longueur brute de la liste — 24 — sans voir que les cellules vides y figurent encore. L'erreur révèle qu'on confond « absence de valeur » et « absence d'élément ».

### Pièges fréquents

- Un Panel affiche une ligne vide pour une valeur nulle : elle passe inaperçue.
- Clean Tree supprime aussi les branches vides si l'option est cochée.

### Pourquoi ce jeu de données

24 lignes dont 6 non renseignées, dispersées et non groupées en fin de liste, pour que le nettoyage ne puisse pas se deviner. Répondre 24 signale qu'on a mesuré la liste sans la nettoyer.

### Note au formateur

> La solution de référence tient en peu de composants : l'exercice mesure surtout la connaissance du composant de nettoyage. En parcours, le fusionner avec un calcul qui exploite le relevé nettoyé.

### Pour aller plus loin

- Remplacer les nulles par une valeur par défaut avec Replace Nulls.
- Observer la propagation d'une nulle à travers une Addition.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-09_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-09_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-09.json` | Descripteur pour le plugin Magpie |
| `A-09_fiche.md` | La présente fiche |
| `A-09_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-09_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-09_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
