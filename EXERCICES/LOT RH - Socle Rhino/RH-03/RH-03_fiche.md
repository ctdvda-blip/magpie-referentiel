# RH-03 — Une trame de plots posée dans Rhino

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Modélisation Rhino |
| **Référence au référentiel** | REF-007, REF-008, REF-013 |
| **Compétence visée** | Produire dans Rhino une répétition régulière d'objets à partir d'un original et d'un pas, et la faire mesurer. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-01 Score visible |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire dans Rhino une répétition régulière d'objets à partir d'un original et d'un pas, et la faire mesurer.

### Contexte

Une terrasse sur plots demande un plot tous les 600 mm dans les deux sens, sur une emprise donnée.

### Énoncé

> L'emprise de la terrasse mesure 4 200 mm sur 3 000 mm. Posez un plot cylindrique de 100 mm de diamètre à chaque nœud d'une trame de 600 mm, le premier au coin d'origine. Donnez le nombre de plots.

### Ce qui vous est fourni

Un fichier Rhino avec l'emprise tracée et un plot modèle à l'origine.

### Ce qui est attendu

Un nombre entier : combien de plots compte la trame.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-03_sujet.gh`

### Barème

1 point si le compte vaut 48 et si les quatre angles sont appuyés.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-03_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 48 — huit rangées de six plots.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Poser le plot modèle au coin d'origine de l'emprise.

**Étape 2.** Établir le nombre de nœuds avant de lancer le réseau : 4 200 ÷ 600 = 7 intervalles, donc 8 positions.

**Étape 3.** Lancer le réseau rectangulaire avec 8 et 6 éléments, pas 7 et 5.

**Étape 4.** Vérifier visuellement que les quatre angles portent un plot.

**Étape 5.** Faire compter les plots par la définition, par leur calque.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter 4 200 ÷ 600 = 7 plots dans la longueur au lieu de 8. C'est la confusion entre le nombre d'intervalles et le nombre de nœuds, déjà vue en A-10 : ici elle laisse un angle de terrasse sans appui.

### Pièges fréquents

- Compter les intervalles au lieu des nœuds.
- Réseau lancé depuis le centre du plot modèle sans vérifier que le premier tombe bien sur l'angle.

### Pourquoi ce jeu de données

L'emprise tombe juste sur la trame dans les deux sens, pour que l'exercice porte sur le décompte et non sur le traitement des rives incomplètes.

### Pour aller plus loin

- Porter l'emprise à 4 500 mm et traiter la rive incomplète.
- Passer la trame en quinconce et recompter.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-03_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-03_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-03.json` | Descripteur pour le plugin Magpie |
| `RH-03_fiche.md` | La présente fiche |
| `RH-03_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-03_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-03_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
