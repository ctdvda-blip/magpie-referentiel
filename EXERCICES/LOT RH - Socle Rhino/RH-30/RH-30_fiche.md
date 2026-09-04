# RH-30 — Ce que le filtre de sélection retient

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH1 · Interface et navigation Rhino |
| **Référence au référentiel** | REF-003, REF-004 |
| **Compétence visée** | Prévoir le résultat d'une sélection filtrée en tenant compte de ce qui est verrouillé. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | RH-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-16 La chasse au trésor |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Prévoir le résultat d'une sélection filtrée en tenant compte de ce qui est verrouillé.

### Contexte

Sélectionner par type et par calque est le geste de base d'un fichier bien rangé. Ce qui est verrouillé n'entre pas dans la sélection, et l'oublier fait croire à un fichier incomplet.

### Énoncé

> L'inventaire donne, pour seize objets, leur type, leur calque et leur état de verrouillage. Donnez le nombre d'objets que retient une sélection des courbes du calque 10-Porteurs.

### Ce qui vous est fourni

L'inventaire des seize objets et de leurs trois attributs.

### Ce qui est attendu

3 objets sont retenus par la sélection.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-30_sujet.gh`

### Barème

1 point si le compte est exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-30_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Tester l'égalité du type à « Courbe ».

**Étape 2.** Tester l'égalité du calque à « 10-Porteurs ».

**Étape 3.** Prendre la négation du verrouillage.

**Étape 4.** Combiner les trois par des ET, puis compter.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Ignorer le verrouillage : cinq. Deux courbes du bon calque sont verrouillées et n'entreront jamais dans la sélection — l'apprenant cherche alors pourquoi son compte ne tombe pas, sans penser au cadenas.

### Pièges fréquents

- Oublier la troisième condition.
- Employer un OU entre le type et le calque.

### Pourquoi ce jeu de données

Seize objets répartis sur trois calques et quatre types. Cinq courbes sont sur 10-Porteurs, dont deux verrouillées : les deux réponses sont proches et toutes deux crédibles devant un fichier qu'on découvre.

### Limite de la correction automatique

> Le compte suppose que le verrouillage vient de l'OBJET. Un objet peut aussi être inaccessible parce que son calque est verrouillé, ce que l'inventaire ne distingue pas ici et qui produit le même symptôme.

### Pour aller plus loin

- Compter ce que retiendrait le même filtre après déverrouillage.
- Donner le calque le mieux fourni en courbes.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-30_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-30_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-30.json` | Descripteur pour le plugin Magpie |
| `RH-30_fiche.md` | La présente fiche |
| `RH-30_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-30_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-30_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
