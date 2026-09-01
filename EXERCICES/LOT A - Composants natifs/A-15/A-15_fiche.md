# A-15 — Répartir avec Dispatch

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A3 · Listes |
| **Référence au référentiel** | REF-045, REF-061 |
| **Compétence visée** | Scinder un lot en deux ensembles selon une condition, en conservant les deux. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-14 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-15 Dessin à compléter |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Scinder un lot en deux ensembles selon une condition, en conservant les deux.

### Contexte

Au-delà de 2,50 m², un panneau ne se pose plus seul : il faut séparer ce qui part en pose individuelle de ce qui part en binôme.

### Énoncé

> Les surfaces des 24 panneaux du chantier vous sont fournies. Séparez-les en deux groupes selon qu'ils dépassent ou non 2,50 m², et donnez le nombre de panneaux à poser en binôme.

### Ce qui vous est fourni

Les 24 surfaces de panneaux, en mètres carrés, et le seuil de 2,50 m².

### Ce qui est attendu

Un nombre entier : combien de panneaux partent en pose à deux.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-15_sujet.gh`

### Barème

1 point par sortie correcte.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-15_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 11 — le nombre de panneaux de plus de 2,50 m², à poser en binôme.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Poser Larger Than or Equal : liste sur A, valeur 50 sur B.

**Étape 2.** Poser Dispatch : liste sur List, booléens sur Pattern.

**Étape 3.** La sortie A reçoit les True, la sortie B les False.

**Étape 4.** Relier chaque sortie vers un Panel.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Ne conserver qu'un seul des deux groupes, puis ne plus pouvoir vérifier que la somme des deux effectifs vaut bien 24.

### Pièges fréquents

- Inverser les sorties A et B.
- Utiliser Larger Than strict alors que l'énoncé inclut 50.

### Pourquoi ce jeu de données

24 surfaces réelles. Aucune ne vaut exactement 2,50 : la plus proche est à 2,49, de sorte que l'exercice ne dépende pas du sens de l'inégalité, qui n'est pas son objet. La somme des deux groupes doit valoir 24, ce qui donne à l'apprenant son propre moyen de contrôle.

### Pour aller plus loin

- Répartir des points selon leur coordonnée Z.
- Répartir en trois catégories en chaînant deux Dispatch.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-15_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-15_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-15.json` | Descripteur pour le plugin Magpie |
| `A-15_fiche.md` | La présente fiche |
| `A-15_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-15_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-15_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
