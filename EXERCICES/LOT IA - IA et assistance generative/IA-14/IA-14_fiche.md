# IA-14 — Le résultat plausible et faux

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA5 · Vérification, licences et limites |
| **Référence au référentiel** | REF-139, REF-142 |
| **Compétence visée** | Contrôler un résultat produit par une IA par un moyen indépendant de la manière dont il a été obtenu. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | IA-01 |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-11 Chasse à l'erreur |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Contrôler un résultat produit par une IA par un moyen indépendant de la manière dont il a été obtenu.

### Contexte

Un assistant propose une section de poutre pour une portée donnée, avec une assurance qui n'a rien à voir avec sa justesse.

### Énoncé

> Le composant fourni annonce un volume de matière pour l'assemblage donné. Établissez si ce volume est juste, et donnez le volume exact.

### Ce qui vous est fourni

L'assemblage, et un composant scripté qui en annonce le volume.

### Ce qui est attendu

Une valeur décimale : le volume exact de l'assemblage, dans l'unité du modèle. Le composant fourni en annonce un autre.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-14_sujet.gh`

### Barème

1 point si le volume exact est donné et si l'écart du composant fourni est expliqué.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-14_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 40 800 000 mm³, soit 0,0408 m³ — à comparer aux 40,8 m³ annoncés par le composant fourni.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Estimer l'ordre de grandeur à la main avant tout calcul.

**Étape 2.** Mesurer le volume par un moyen natif, indépendant du composant fourni.

**Étape 3.** Comparer les deux valeurs et qualifier l'écart.

**Étape 4.** Identifier la cause de l'écart dans le composant fourni.

**Étape 5.** Retenir la valeur établie par le moyen indépendant.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Recontrôler le résultat avec le même outil, ou en redemandant à l'assistant s'il est sûr. Un contrôle qui emprunte le même chemin que le calcul ne contrôle rien : il faut un moyen indépendant — un ordre de grandeur, un calcul natif, une mesure dans Rhino.

### Pièges fréquents

- Demander confirmation à l'assistant qui a produit le résultat.
- Conclure que le composant a raison parce qu'il donne une valeur précise : la précision affichée ne dit rien de la justesse.

### Pourquoi ce jeu de données

Le composant fourni divise par un million au lieu d'un milliard : il annonce 40,8 m³ pour un assemblage qui en fait 0,0408. Un facteur mille, invisible sans contrôle de l'ordre de grandeur.

### Limite de la correction automatique

> Le volume exact tranche la question posée. Il ne dit pas COMMENT l'écart a été trouvé : un facteur mille se repère à l'ordre de grandeur, et c'est ce réflexe — comparer au plausible avant de comparer au juste — que l'exercice travaille et que le nombre seul ne mesure pas.

### Pour aller plus loin

- Faire produire par l'assistant son propre contrôle indépendant, et juger si le contrôle est réellement indépendant.
- Reprendre A-47 et comparer les deux démarches.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-14_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-14_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-14.json` | Descripteur pour le plugin Magpie |
| `IA-14_fiche.md` | La présente fiche |
| `IA-14_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-14_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-14_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
