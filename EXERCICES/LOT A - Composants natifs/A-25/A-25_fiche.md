# A-25 — Longest List et Cross Reference

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A5 · Comportements implicites |
| **Référence au référentiel** | REF-054 |
| **Compétence visée** | Choisir délibérément un mode d'appariement entre deux listes de tailles différentes. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-24 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-23 Duel et classement |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Choisir délibérément un mode d'appariement entre deux listes de tailles différentes.

### Contexte

Un calepinage croise 10 files et 4 niveaux : selon qu'on veut une valeur par file ou une valeur par intersection, l'appariement change.

### Énoncé

> Une liste de 10 valeurs et une liste de 4 valeurs vous sont fournies. Produisez d'abord un résultat par file — 10 valeurs — puis un résultat par intersection file × niveau — 40 valeurs.

### Ce qui vous est fourni

Deux listes internalisées de 10 et 4 éléments.

### Ce qui est attendu

Deux effectifs : 10 puis 40.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-25_sujet.gh`

### Barème

1 point par valeur correcte.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-25_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Insérer Longest List (Sets > List) en amont de l'Addition : la liste courte est complétée par son dernier élément, 10 résultats.

**Étape 2.** Insérer Cross Reference à la place : chaque élément de A est croisé avec chaque élément de B, 40 résultats.

**Étape 3.** Mesurer les deux sorties avec List Length.

**Étape 4.** Comparer avec le Graft de l'exercice A-20 qui produit le même croisement sous forme d'arbre.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Obtenir 40 dans les deux cas en laissant un croisement branché, ou 10 dans les deux cas en ne changeant que la position des câbles. L'appariement est un réglage, pas une conséquence du câblage.

### Pièges fréquents

- Cross Reference propose plusieurs variantes (Holistic, Diagonal) dans son menu contextuel.
- Longest List complète par répétition du dernier élément, pas par des zéros.

### Pour aller plus loin

- Obtenir 40 résultats par Graft plutôt que par Cross Reference et comparer les structures.
- Tester le mode Diagonal de Cross Reference.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-25_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-25_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-25.json` | Descripteur pour le plugin Magpie |
| `A-25_fiche.md` | La présente fiche |
| `A-25_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-25_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-25_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
