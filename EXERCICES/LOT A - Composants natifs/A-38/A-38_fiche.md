# A-38 — Rotation et symétrie

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A9 · Transformations et réseaux |
| **Référence au référentiel** | REF-067 |
| **Compétence visée** | Faire tourner une géométrie autour d'un axe choisi et en produire le symétrique par rapport à un plan choisi. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-37 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-14 Puzzle de câblage |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire tourner une géométrie autour d'un axe choisi et en produire le symétrique par rapport à un plan choisi.

### Contexte

Un profil d'angle se décline en version droite et version gauche, orientées à 45° sur la trame.

### Énoncé

> Le profil vous est fourni. Faites-le tourner de 45° autour de l'axe vertical passant par l'origine, puis produisez sa version symétrique par rapport au plan vertical contenant l'axe X.

### Ce qui vous est fourni

Un profil fermé internalisé.

### Ce qui est attendu

Le profil tourné et son symétrique.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-38_sujet.gh`

### Barème

1 point par transformation correcte.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-38_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Rotate : profil sur G, angle sur A, plan XY sur P.

**Étape 2.** Convertir 45° en radians avec Radians, ou saisir directement 45 dans un slider réglé en degrés puis convertir.

**Étape 3.** Poser Mirror : résultat sur G, XZ Plane sur P.

**Étape 4.** Vérifier la position des deux résultats.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Prendre le mauvais plan de symétrie et obtenir une version superposable à l'originale par rotation : une pièce gauche et une pièce droite ne sont pas superposables, c'est le contrôle à faire.

### Pièges fréquents

- Saisir 45 sans conversion : la rotation vaut 45 radians.
- Le plan de symétrie de Mirror est un plan, pas un axe.

### Limite de la correction automatique

> Le profil tourné et son symétrique sont produits. Une symétrie INVERSE le sens de parcours de la courbe : sans conséquence à l'affichage, elle en a une dès qu'on extrude ou qu'on décale, et c'est un piège classique.

### Pour aller plus loin

- Enchaîner rotation et symétrie et comparer avec l'ordre inverse.
- Utiliser Rotate Axis pour tourner autour d'un axe quelconque.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-38_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-38_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-38.json` | Descripteur pour le plugin Magpie |
| `A-38_fiche.md` | La présente fiche |
| `A-38_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-38_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-38_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
