# RH-21 — Les faces qui ne mesurent rien

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-022, REF-023 |
| **Compétence visée** | Repérer les faces dégénérées d'un maillage avant de le réparer, en s'appuyant sur la tolérance du document. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-20 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Repérer les faces dégénérées d'un maillage avant de le réparer, en s'appuyant sur la tolérance du document.

### Contexte

Le maillage vient d'une conversion. Certaines faces sont réduites à un fil : elles ne se voient pas, et font échouer la réparation automatique.

### Énoncé

> Les aires des quinze faces suspectes vous sont fournies, en millimètres carrés. La tolérance du document vaut 0,001 mm². Donnez le nombre de faces dégénérées.

### Ce qui vous est fourni

Les quinze aires relevées et la tolérance du document.

### Ce qui est attendu

4 faces dégénérées.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-21_sujet.gh`

### Barème

1 point si le compte est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-21_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Comparer chaque aire à la tolérance, et non à zéro.

**Étape 2.** Compter.

**Étape 3.** Retenir que la face à 0,0012 n'est pas dégénérée au sens du document.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Comparer à zéro. Aucune face n'a une aire exactement nulle : elles valent 0,0003 à 0,0012 mm², ce qui n'est pas zéro mais n'est rien à l'échelle du document. Une comparaison à zéro n'en trouve aucune, et la réparation échoue sans dire pourquoi.

### Pièges fréquents

- Comparer à zéro.
- Prendre une tolérance choisie au jugé plutôt que celle du document.

### Pourquoi ce jeu de données

Cinq faces sous le millième de millimètre carré, dont une à 0,0012 qui passe JUSTE au-dessus de la tolérance : la réponse est 4, et non 5. C'est la tolérance qui tranche, pas l'intuition.

### Limite de la correction automatique

> Quatre faces sont dégénérées AU REGARD de la tolérance du document. Changer cette tolérance change le compte : c'est une propriété du fichier, pas de la géométrie, et deux ouvertures du même modèle peuvent ne pas s'accorder.

### Pour aller plus loin

- Reprendre avec une tolérance de 0,01 mm².
- Donner l'aire totale perdue par la suppression de ces faces.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-21_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-21_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-21.json` | Descripteur pour le plugin Magpie |
| `RH-21_fiche.md` | La présente fiche |
| `RH-21_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-21_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-21_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
