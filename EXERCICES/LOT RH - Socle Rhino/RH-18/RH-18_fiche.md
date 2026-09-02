# RH-18 — Les parois que la machine ne saura pas faire

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-016 |
| **Compétence visée** | Confronter une pièce aux contraintes de la machine avant de lancer une impression. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-08 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Confronter une pièce aux contraintes de la machine avant de lancer une impression.

### Contexte

La machine ne descend pas sous 1,2 mm de paroi. En deçà, elle imprime quelque chose — qui casse à la première manipulation.

### Énoncé

> Les quatorze épaisseurs de paroi relevées sur la pièce vous sont fournies. Donnez le nombre de parois strictement inférieures au minimum imprimable de 1,2 mm.

### Ce qui vous est fourni

Les quatorze épaisseurs relevées, en millimètres, et le minimum imprimable.

### Ce qui est attendu

5 parois passent sous le minimum.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-18_sujet.gh`

### Barème

1 point si le compte est juste et strict.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-18_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Comparer chaque épaisseur au minimum.

**Étape 2.** Choisir sciemment entre strict et large.

**Étape 3.** Compter.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter 6 en incluant la paroi qui vaut exactement 1,2 mm. Le minimum est atteignable : c'est un minimum, pas une borne exclue. Se tromper de sens conduit à reprendre une paroi qui n'en avait pas besoin — ou, dans l'autre sens, à en laisser passer une.

### Pièges fréquents

- Inclure la paroi qui vaut exactement le minimum.
- Juger sur l'aperçu plutôt que sur les relevés.

### Pourquoi ce jeu de données

Quatorze relevés, dont un exactement au minimum et trois entre 1,1 et 1,25 : la frontière est peuplée, et le sens de la comparaison change la réponse d'exactement un.

### Limite de la correction automatique

> L'exercice compte les parois trop minces. Il ne dit pas comment les épaissir — ce qui suppose de savoir laquelle est structurelle et laquelle est décorative.

### Pour aller plus loin

- Donner l'épaisseur minimale relevée.
- Reprendre avec une machine descendant à 0,8 mm.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-18_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-18_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-18.json` | Descripteur pour le plugin Magpie |
| `RH-18_fiche.md` | La présente fiche |
| `RH-18_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-18_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-18_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
