# G-14 — Le puzzle de câblage

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G3 · Manipulation et adresse |
| **Référence au référentiel** | REF-027, REF-048 |
| **Compétence visée** | Rétablir un câblage à partir du seul résultat attendu, en lisant les types d'entrée et de sortie. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | A-01, A-19 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | — |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Travailler la lecture des entrées et sorties d'un composant.

### Contexte

Un câblage se lit avant de s'écrire. Le puzzle enlève les câbles et laisse les composants : ce qui reste à trouver est exactement ce qu'on ne voit pas quand on recopie un tutoriel.

### Énoncé

> Six composants sont posés sur le canvas, tous les câbles ont été supprimés. Rétablis le câblage pour reproduire la géométrie affichée en filigrane, sans ajouter ni supprimer aucun composant.

### Ce qui vous est fourni

Six composants dispersés, aucun câble, une géométrie cible en filigrane.

### Ce qui est attendu

2 033,29 mm — la longueur du contour fermé, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-14_sujet.gh`

### Barème

1 point pour la géométrie, 1 point pour le respect du nombre de composants.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-14_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Identifier le composant terminal produisant la géométrie visible.

**Étape 2.** Remonter la chaîne : quelle entrée attend un plan, laquelle attend un nombre.

**Étape 3.** Câbler de l'amont vers l'aval en contrôlant le type attendu à chaque port.

**Étape 4.** Vérifier la superposition avec le filigrane.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Oublier de refermer le contour : 1 530,00 mm, soit le seul chemin ouvert. La différence est le segment de retour, 503,29 mm — un quart de la réponse, et l'aperçu ne le montre pas puisqu'une polyligne ouverte se dessine comme une fermée à un segment près.

### Pièges fréquents

- Brancher un point sur une entrée attendant un plan : conversion silencieuse en plan XY à cette origine.
- Ajouter un composant pour contourner une difficulté : le contrôle du nombre échoue.

### Pourquoi ce jeu de données

Six sommets en marches d'escalier, tous à coordonnées entières, mais dont le segment de fermeture est oblique : la longueur totale est irrationnelle et ne se devine pas, alors que chaque segment se vérifie de tête.

### Limite de la correction automatique

> La longueur dit que le contour est le BON, pas qu'il a été obtenu avec les six composants imposés. Le respect du nombre de composants se compte à l'œil, sur le canvas.

### Pour aller plus loin

- Puzzle à 12 composants.
- Version où deux câblages différents donnent le même résultat.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-14_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-14_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-14.json` | Descripteur pour le plugin Magpie |
| `G-14_fiche.md` | La présente fiche |
| `G-14_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-14_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-14_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
