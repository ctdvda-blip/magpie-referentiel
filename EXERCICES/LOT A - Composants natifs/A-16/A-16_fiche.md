# A-16 — Décaler et inverser une liste

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A3 · Listes |
| **Référence au référentiel** | REF-046 |
| **Compétence visée** | Relier chaque élément d'une liste au suivant en refermant la boucle, sans traiter le dernier cas à part. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-11 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-25 Animation de la solution |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Relier chaque élément d'une liste au suivant en refermant la boucle, sans traiter le dernier cas à part.

### Contexte

Un garde-corps polygonal doit être chiffré en longueur de lisse : il faut les segments entre montants, y compris celui qui referme le contour.

### Énoncé

> Huit montants sont disposés en octogone. Tracez les huit lisses qui relient chaque montant au suivant, la dernière revenant au premier, en n'employant qu'une seule fois le composant de tracé.

### Ce qui vous est fourni

Une liste de 8 points internalisée, disposés en cercle.

### Ce qui est attendu

Huit segments formant un contour fermé.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-16_sujet.gh`

### Barème

1 point si les 8 segments sont produits.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-16_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Shift List avec un décalage de 1 et l'option Wrap activée.

**Étape 2.** Poser Line : liste d'origine sur A, liste décalée sur B.

**Étape 3.** Les huit segments se tracent, le huitième reliant le dernier point au premier.

**Étape 4.** Désactiver Wrap pour observer qu'il ne reste que sept segments.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Obtenir sept segments et refermer le contour à la main. Le montage marche pour huit montants et sera à refaire pour dix : l'exercice vise justement le décalage circulaire qui évite le cas particulier.

### Pièges fréquents

- Wrap désactivé : le polygone reste ouvert.
- Utiliser Polyline avec l'option Closed masque le mécanisme visé par l'exercice.

### Note au formateur

> Le décalage circulaire est un vrai geste de conception, mais la solution reste courte : le rapprocher d'un exercice de contour fermé.

### Pour aller plus loin

- Décaler de 2 pour obtenir les diagonales.
- Comparer avec PolyLine fermée.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-16_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-16_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-16.json` | Descripteur pour le plugin Magpie |
| `A-16_fiche.md` | La présente fiche |
| `A-16_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-16_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-16_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
