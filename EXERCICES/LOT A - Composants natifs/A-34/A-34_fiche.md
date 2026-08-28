# A-34 — Primitives filaires

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A8 · Géométrie vectorielle et filaire |
| **Référence au référentiel** | REF-063 |
| **Compétence visée** | Produire des primitives filaires en maîtrisant ce que désignent leurs paramètres. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-33 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-15 Dessin à compléter |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire des primitives filaires en maîtrisant ce que désignent leurs paramètres.

### Contexte

Un poteau de section hexagonale est inscrit dans un fourreau circulaire, lui-même logé dans un coffrage carré.

### Énoncé

> Le fourreau a 40 de rayon. Construisez la section hexagonale inscrite dans ce fourreau, ainsi que le carré de coffrage circonscrit au même fourreau.

### Ce qui vous est fourni

Canvas vide.

### Ce qui est attendu

Un hexagone de rayon 40 et un carré de 80 × 80.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-34_sujet.gh`

### Barème

1 point par courbe correcte.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-34_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Polygon avec un plan XY, un rayon de 40 et 6 segments.

**Étape 2.** Poser Rectangle avec le même plan et deux domaines de -40 à 40.

**Étape 3.** Utiliser Construct Domain pour produire ces domaines.

**Étape 4.** Vérifier que le rectangle est tangent au cercle circonscrit.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Prendre 40 pour l'apothème de l'hexagone au lieu du rayon circonscrit : la section ne tient plus dans le fourreau. Inscrit et circonscrit ne se devinent pas, ils se vérifient.

### Pièges fréquents

- Polygon attend un nombre de côtés, pas un nombre de sommets à calculer.
- Rectangle attend des domaines centrés, pas une largeur et une hauteur.

### Pour aller plus loin

- Ajouter un congé aux angles du rectangle (entrée R).
- Construire un polygone étoilé avec Polygon Edge.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-34_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-34_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-34.json` | Descripteur pour le plugin Magpie |
| `A-34_fiche.md` | La présente fiche |
| `A-34_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-34_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-34_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
