# G-05 — La collection de badges

**Fiche d'exercice Magpie** · Lot G — Exercices gamifiés

| | |
|---|---|
| **Thématique** | G1 · Progression et récompense |
| **Référence au référentiel** | REF-079, REF-081, REF-098 |
| **Compétence visée** | Produire une famille complète de mesures sur un même assemblage, en gardant la cohérence des unités. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | A-47, A-49 |
| **Mode de validation** | NumericTolerance — tolérance 1 |
| **Solution de référence** | 16 composants |
| **Gamification associée** | — |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Valoriser la maîtrise d'une famille complète de composants.

### Contexte

Le badge récompense la maîtrise d'une famille entière, pas d'un geste isolé. Un métreur qui sait mesurer une longueur mais pas un volume n'est pas un métreur.

### Énoncé

> Six mesures à produire sur le même assemblage. Chaque mesure exacte débloque un badge. La collection complète débloque le badge doré ARPENTEUR.

### Ce qui vous est fourni

Un assemblage internalisé et six paramètres de réponse.

### Ce qui est attendu

Les six mesures : 15 200 mm de développé, 11 904 mm² de section, 180 940,8 cm³, 1 420,385 kg, 4 370 mm hors tout, 6 620 mm de portée.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`G-05_sujet.gh`

### Barème

1 point par badge, badge doré à 6/6.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `G-05_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Mesurer le développé des arêtes avec Length et Mass Addition.

**Étape 2.** Mesurer la surface totale avec Area.

**Étape 3.** Mesurer le volume avec Volume.

**Étape 4.** Localiser le centre de gravité avec la sortie C de Volume.

**Étape 5.** Mesurer l'encombrement avec Bounding Box et Deconstruct Box.

**Étape 6.** Compter les faces avec Deconstruct Brep et List Length.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Calculer l'aire de la section comme un plein, 180 × 340 = 61 200, au lieu de déduire l'intérieur du profil creux : 11 904. Le volume et la masse suivent, et le portique est annoncé cinq fois trop lourd — une erreur qui se propage à toute la collection de badges.

### Pièges fréquents

- Mesurer la surface d'une face au lieu de la surface totale.
- Encombrement mesuré dans un repère tourné.

### Pourquoi ce jeu de données

Un profil creux 180 × 340 de 12 mm d'épaisseur : le rapport plein/creux est de 5,14, assez pour que l'erreur soit flagrante à la lecture. Les six mesures s'enchaînent — section, développé, volume, masse — de sorte qu'une seule fausse en compromet trois.

### Limite de la correction automatique

> La masse est celle de la MATIÈRE. Assemblages, platines et soudures ajoutent couramment 8 à 12 % qu'aucune de ces six mesures ne voit.

### Pour aller plus loin

- Badges de rareté selon le nombre de tentatives.
- Badge secret pour une solution en moins de 12 composants.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `G-05_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `G-05_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `G-05.json` | Descripteur pour le plugin Magpie |
| `G-05_fiche.md` | La présente fiche |
| `G-05_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `G-05_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `G-05_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
