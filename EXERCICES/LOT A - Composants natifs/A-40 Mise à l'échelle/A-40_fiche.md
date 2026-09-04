# A-40 — Mise à l'échelle

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A9 · Transformations et réseaux |
| **Référence au référentiel** | REF-067 |
| **Compétence visée** | Mettre à l'échelle une géométrie, en maîtrisant le centre et en distinguant l'échelle uniforme de l'échelle par direction. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-39 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-04 Système de vies |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mettre à l'échelle une géométrie, en maîtrisant le centre et en distinguant l'échelle uniforme de l'échelle par direction.

### Contexte

Un profil de menuiserie est décliné en une version réduite et une version surhaussée, sans changer sa largeur de passage.

### Énoncé

> Le profil vous est fourni. Produisez d'abord une version réduite à 60 % autour de son propre centre de gravité, puis une version deux fois plus haute dont la largeur reste inchangée.

### Ce qui vous est fourni

Un profil fermé internalisé.

### Ce qui est attendu

Un profil réduit centré et un profil étiré verticalement.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-40_sujet.gh`

### Barème

1 point par mise à l'échelle correcte.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-40_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Area sur le profil pour récupérer son centroïde.

**Étape 2.** Poser Scale : centre = centroïde, facteur = 0,6.

**Étape 3.** Poser Scale NU avec X = 1, Y = 1, Z = 2 (ou Y = 2 selon l'orientation).

**Étape 4.** Comparer les deux résultats.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Réduire autour de l'origine du modèle plutôt qu'autour du centre du profil : la taille est bonne, la position ne l'est plus.

### Pièges fréquents

- Scale utilise par défaut l'origine du repère, pas le centre de l'objet.
- Scale NU s'applique selon les axes du plan fourni.

### Limite de la correction automatique

> Les deux mises à l'échelle sont justes. Une échelle non uniforme déforme les CONGÉS et les épaisseurs : un profil deux fois plus haut n'a plus les mêmes rayons de raccordement, et n'est plus fabricable avec le même outil.

### Pour aller plus loin

- Mettre à l'échelle une liste d'objets avec des facteurs différents.
- Utiliser Bounding Box pour recadrer avant mise à l'échelle.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-40_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-40_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-40.json` | Descripteur pour le plugin Magpie |
| `A-40_fiche.md` | La présente fiche |
| `A-40_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-40_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-40_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
