# RH-29 — La platine percée en réseau

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Modélisation Rhino |
| **Référence au référentiel** | REF-012, REF-013 |
| **Compétence visée** | Chiffrer la matière restante après un réseau de percements, en distinguant rayon et diamètre. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 14 min |
| **Prérequis** | RH-05 |
| **Mode de validation** | NumericTolerance — tolérance 0.0001 |
| **Solution de référence** | 10 composants |
| **Gamification associée** | G-20 La chasse aux bugs |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Chiffrer la matière restante après un réseau de percements, en distinguant rayon et diamètre.

### Contexte

Une platine percée se pèse pour le transport et se chiffre au kilo. Vingt-quatre trous enlèvent une matière qui compte.

### Énoncé

> La platine mesure 900 × 600 × 12 mm. Elle reçoit un réseau de 6 par 4 trous traversants de 22 mm de diamètre. Donnez le volume de matière restante, en décimètres cubes.

### Ce qui vous est fourni

Les cotes de la platine, la trame et le diamètre des trous.

### Ce qui est attendu

6,3705 dm³ de matière restante, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-29_sujet.gh`

### Barème

1 point si le volume est juste à 0,0001 dm³.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-29_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Calculer le volume plein de la platine.

**Étape 2.** Diviser le diamètre par deux pour obtenir le rayon.

**Étape 3.** Calculer le volume d'un trou, puis des vingt-quatre.

**Étape 4.** Retrancher.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Prendre le diamètre pour le rayon dans l'aire du disque : 6,0421 dm³. L'aire va comme le CARRÉ du rayon — l'erreur quadruple le volume percé, et la platine est annoncée 5 % plus légère qu'elle n'est.

### Pièges fréquents

- Employer le diamètre comme rayon.
- Oublier de multiplier par le nombre de trous.

### Pourquoi ce jeu de données

Vingt-quatre trous de 22 mm dans 12 mm d'épaisseur retirent 109 500 mm³, soit 1,7 % de la platine. L'erreur de rayon en retire quatre fois plus : 6,8 %. Les deux réponses restent plausibles pour une platine d'acier.

### Limite de la correction automatique

> Le volume suppose des trous CYLINDRIQUES et traversants. Un perçage fraisé ou taraudé enlève davantage, et la tolérance de perçage — un dixième sur le diamètre — pèse plus que la précision affichée ici.

### Pour aller plus loin

- Donner la masse en acier à 7,85 g/cm³.
- Chercher le diamètre qui allège la platine de 10 %.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-29_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-29_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-29.json` | Descripteur pour le plugin Magpie |
| `RH-29_fiche.md` | La présente fiche |
| `RH-29_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-29_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-29_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
