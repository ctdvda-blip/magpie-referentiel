# A-32 — Vecteur, amplitude et direction

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A8 · Géométrie vectorielle et filaire |
| **Référence au référentiel** | REF-062 |
| **Compétence visée** | Construire un vecteur entre deux points, puis en régler la longueur sans en changer la direction. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-02 |
| **Mode de validation** | GeometryTolerance — tolérance 0,01 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-26 Feedback visuel immédiat |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Construire un vecteur entre deux points, puis en régler la longueur sans en changer la direction.

### Contexte

Une potence de levage est reprise par un tirant : la direction est imposée par la géométrie, la longueur par la portée à couvrir.

### Énoncé

> Le tirant part de l'origine et rejoint le point situé à 30 en X et 40 en Y. Construisez sa direction, puis produisez un second tirant de même direction mais de 100 unités de long.

### Ce qui vous est fourni

Deux points internalisés.

### Ce qui est attendu

Un vecteur de longueur 50 et un vecteur de longueur 100, de même direction.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-32_sujet.gh`

### Barème

1 point par vecteur correct.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-32_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Vector 2Pt avec les deux points : sa longueur vaut 50.

**Étape 2.** Vérifier avec Vector Length.

**Étape 3.** Poser Amplitude et régler l'amplitude sur 100.

**Étape 4.** Afficher les deux vecteurs avec Vector Display pour comparer.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Multiplier le vecteur par 100 au lieu de porter sa longueur à 100 : on obtient 5 000 unités. L'erreur révèle qu'on confond mise à l'échelle et fixation d'amplitude.

### Pièges fréquents

- Confondre Amplitude (impose une longueur) et Multiplication (multiplie la longueur).
- Oublier d'activer Unitize sur Vector 2Pt quand on veut une direction pure.

### Limite de la correction automatique

> Les deux vecteurs ont la bonne longueur et la bonne direction. Un vecteur n'a pas de POINT D'APPLICATION : que le second tirant parte du même endroit que le premier est une décision de construction, pas une propriété du vecteur.

### Pour aller plus loin

- Construire le vecteur normal d'un plan.
- Additionner deux vecteurs et vérifier la résultante.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-32_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-32_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-32.json` | Descripteur pour le plugin Magpie |
| `A-32_fiche.md` | La présente fiche |
| `A-32_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-32_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-32_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
