# RH-24 — Les parois trop minces après mise à l'échelle

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH5 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-016, REF-017, REF-018 |
| **Compétence visée** | Confronter un relevé d'épaisseurs à la contrainte machine APRÈS mise à l'échelle, et non avant. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | RH-10 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-26 Le retour visuel immédiat |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Confronter un relevé d'épaisseurs à la contrainte machine APRÈS mise à l'échelle, et non avant.

### Contexte

Une maquette se réduit pour tenir dans le volume d'impression. Les parois se réduisent avec elle, et celles qui passaient au 1/1 ne passent plus.

### Énoncé

> Le relevé donne dix-huit épaisseurs de paroi, en centièmes de millimètre. La pièce sera imprimée à 62 % de sa taille, et la machine ne tient pas sous 1,20 mm. Donnez le nombre de parois qui ne passeront pas.

### Ce qui vous est fourni

Les dix-huit épaisseurs relevées, le facteur d'échelle et le minimum machine.

### Ce qui est attendu

12 parois passent sous le minimum après réduction.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-24_sujet.gh`

### Barème

1 point si le compte est exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-24_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Ramener les centièmes en millimètres.

**Étape 2.** Appliquer le facteur d'échelle.

**Étape 3.** Comparer au minimum machine.

**Étape 4.** Compter les parois retenues.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Juger les épaisseurs AVANT la mise à l'échelle : cinq seulement. Sept parois franchissent le seuil pendant la réduction — elles sortiront de la machine en dentelle, et rien dans le modèle au 1/1 ne le laissait voir.

### Pièges fréquents

- Comparer avant la mise à l'échelle.
- Oublier la conversion des centièmes.

### Pourquoi ce jeu de données

Dix-huit épaisseurs de 0,40 à 3,40 mm. Le facteur 0,62 place le seuil effectif à 1,94 mm au 1/1 : sept parois tombent entre 1,20 et 1,94, et ce sont elles qui font toute la différence entre les deux réponses.

### Limite de la correction automatique

> Le compte suppose une réduction UNIFORME. Une mise à l'échelle non uniforme — pour tenir dans un plateau étroit — réduit différemment selon l'axe, et l'épaisseur d'une paroi dépend alors de son orientation.

### Pour aller plus loin

- Chercher le facteur maximal qui ne sacrifie aucune paroi.
- Refaire le compte pour une machine à 0,8 mm.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-24_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-24_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-24.json` | Descripteur pour le plugin Magpie |
| `RH-24_fiche.md` | La présente fiche |
| `RH-24_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-24_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-24_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
