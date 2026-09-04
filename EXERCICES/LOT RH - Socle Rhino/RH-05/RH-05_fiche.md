# RH-05 — Percer une platine dans Rhino

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Modélisation Rhino |
| **Référence au référentiel** | REF-012 |
| **Compétence visée** | Combiner des solides par soustraction dans Rhino et quantifier la matière retirée. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | RH-04 |
| **Mode de validation** | NumericTolerance — tolérance 1 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-11 Chasse à l'erreur |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Combiner des solides par soustraction dans Rhino et quantifier la matière retirée.

### Contexte

Une platine d'assemblage reçoit quatre boulons ; la matière retirée entre dans le bilan de poids.

### Énoncé

> La platine mesure 300 × 200 × 15 mm. Percez-la de quatre trous traversants de 18 mm de diamètre, centrés à 40 mm de chaque bord. Donnez le volume de matière retirée, en millimètres cubes.

### Ce qui vous est fourni

Un fichier Rhino contenant la platine pleine.

### Ce qui est attendu

Une valeur : le volume de matière retirée, en millimètres cubes.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-05_sujet.gh`

### Barème

1 point si le volume retiré est juste à 1 mm³ près.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-05_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 15 268 mm³ environ — quatre cylindres de 18 mm de diamètre sur 15 mm d'épaisseur.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Poser les quatre cylindres, plus longs que l'épaisseur de la platine et débordant des deux côtés.

**Étape 2.** Mesurer le volume de la platine pleine avant le perçage.

**Étape 3.** Réaliser la soustraction booléenne.

**Étape 4.** Mesurer le volume après perçage.

**Étape 5.** La différence des deux volumes est la matière retirée — et non le volume des cylindres, qui dépassent.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Percer avec des cylindres exactement à fleur des faces : l'opération booléenne échoue ou laisse une face résiduelle, parce que deux surfaces coplanaires ne se coupent pas proprement. Il faut faire dépasser les cylindres.

### Pièges fréquents

- Cylindres à fleur : la booléenne échoue silencieusement ou laisse un objet non fermé.
- Prendre le volume des cylindres entiers comme réponse : ils dépassent de la platine.

### Pourquoi ce jeu de données

L'épaisseur de 15 mm et le diamètre de 18 mm sont ceux d'une platine courante pour boulons M16 : les valeurs parlent à qui connaît le métier.

### Limite de la correction automatique

> Le volume retiré est GÉOMÉTRIQUE. Le perçage réel enlève un peu plus — ébavurage et jeu du foret — et surtout ne dit rien de la tenue de la platine : quatre trous à 40 mm des bords affaiblissent une pièce de 15 mm, ce qui est un calcul de résistance.

### Pour aller plus loin

- Passer les trous en oblongs et refaire le calcul.
- Chiffrer le poids retiré, en acier à 7 850 kg/m³.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-05_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-05_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-05.json` | Descripteur pour le plugin Magpie |
| `RH-05_fiche.md` | La présente fiche |
| `RH-05_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-05_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-05_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
