# A-37 — Déplacer par un vecteur

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A9 · Transformations et réseaux |
| **Référence au référentiel** | REF-067 |
| **Compétence visée** | Appliquer une translation et l'échelonner, en sachant que la transformation ne consomme pas l'original. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | A-32 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-25 Animation de la solution |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Appliquer une translation et l'échelonner, en sachant que la transformation ne consomme pas l'original.

### Contexte

Une rangée d'entretoises est répartie sur la hauteur d'un montant.

### Énoncé

> L'entretoise de base vous est fournie. Remontez-la de 120 mm, puis produisez cinq entretoises supplémentaires échelonnées tous les 24 mm au-dessus d'elle, sans employer de composant de réseau.

### Ce qui vous est fourni

Un cercle internalisé dans le plan XY.

### Ce qui est attendu

Six entretoises espacées de 24 mm.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-37_sujet.gh`

### Barème

1 point si 6 cercles espacés de 24 mm sont produits.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-37_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Series avec Start = 0, Step = 24, Count = 6.

**Étape 2.** Poser Unit Z et brancher la série sur son entrée Factor.

**Étape 3.** Poser Move : cercle sur G, liste de vecteurs sur T.

**Étape 4.** Le composant produit 6 cercles : une liste de vecteurs génère une liste de résultats.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Croire que la translation déplace l'original et compter cinq entretoises au lieu de six. La transformation produit une copie ; l'original reste dans le flux.

### Pièges fréquents

- Brancher un seul vecteur et attendre plusieurs copies.
- Oublier que la géométrie d'origine reste visible en plus des copies.

### Pour aller plus loin

- Décaler selon un vecteur oblique.
- Faire varier le rayon en même temps que la hauteur.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-37_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-37_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-37.json` | Descripteur pour le plugin Magpie |
| `A-37_fiche.md` | La présente fiche |
| `A-37_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-37_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-37_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
