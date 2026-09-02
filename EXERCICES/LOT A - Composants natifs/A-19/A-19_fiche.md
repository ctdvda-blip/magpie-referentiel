# A-19 — Lire un chemin d'arbre

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A4 · Arbres de données |
| **Référence au référentiel** | REF-048, REF-051 |
| **Compétence visée** | Lire la structure d'un flux arborescent : nombre de branches et chemin d'une branche donnée. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-05 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-31 Carte de progression |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Lire la structure d'un flux arborescent : nombre de branches et chemin d'une branche donnée.

### Contexte

Une définition reçue d'un confrère produit des résultats groupés ; avant d'y brancher quoi que ce soit, il faut savoir comment.

### Énoncé

> Le flux fourni est structuré en branches. Indiquez combien il en compte.

### Ce qui vous est fourni

Un arbre internalisé de 4 branches contenant chacune 3 éléments.

### Ce qui est attendu

Un nombre entier : combien de branches compte le flux.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-19_sujet.gh`

### Barème

1 point par réponse correcte.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-19_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 4 — le nombre de branches du flux.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Poser Tree Statistics (Sets > Tree) : la sortie P donne la liste des chemins.

**Étape 2.** Brancher List Length sur P pour obtenir le nombre de branches.

**Étape 3.** Poser List Item sur P avec l'index 2 pour lire le troisième chemin.

**Étape 4.** Relier les deux résultats vers un Panel.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Répondre par le nombre total d'éléments, en confondant l'effectif global et le nombre de regroupements.

### Pièges fréquents

- Confondre nombre de branches et nombre total d'éléments.
- Compter les branches à partir de 1.

### Pour aller plus loin

- Afficher le nombre d'éléments par branche avec la sortie C.
- Comparer l'affichage du Param Viewer en mode graphe et en mode texte.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-19_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-19_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-19.json` | Descripteur pour le plugin Magpie |
| `A-19_fiche.md` | La présente fiche |
| `A-19_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-19_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-19_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
