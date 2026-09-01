# RH-08 — Un caisson vraiment fermé

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH5 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-019, REF-020, REF-021, REF-022, REF-023 |
| **Compétence visée** | Établir qu'un solide est réellement étanche, et le réparer quand il ne l'est pas. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 25 min |
| **Prérequis** | RH-05 |
| **Mode de validation** | NumericTolerance — tolérance 1 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-11 Chasse à l'erreur |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir qu'un solide est réellement étanche, et le réparer quand il ne l'est pas.

### Contexte

Une pièce partant en impression 3D doit être un volume fermé : une enveloppe ouverte n'a pas d'intérieur, et le trancheur la refuse ou la remplit n'importe comment.

### Énoncé

> Le caisson fourni paraît fermé mais ne l'est pas. Trouvez ce qui l'empêche, réparez-le, et donnez son volume une fois étanche, en millimètres cubes.

### Ce qui vous est fourni

Un fichier Rhino contenant le caisson, 420 × 260 × 180 mm, auquel il manque deux faces.

### Ce qui est attendu

19 656 000 mm³ — le volume du caisson une fois refermé. Une enveloppe ouverte n'en a aucun : c'est là toute la preuve.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 1.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-08_sujet.gh`

### Barème

1 point si l'objet est déclaré solide et si le volume est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-08_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Ne pas mesurer d'abord : contrôler d'abord l'étanchéité.

**Étape 2.** Afficher les arêtes nues — ce sont elles qui nomment les jonctions défaillantes.

**Étape 3.** Réparer par jonction des faces adjacentes, en resserrant la tolérance si nécessaire.

**Étape 4.** Revérifier qu'il ne reste aucune arête nue.

**Étape 5.** Mesurer alors le volume : sur une enveloppe ouverte, il n'aurait aucun sens.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Se fier à l'aspect. Un caisson non fermé s'affiche exactement comme un caisson fermé : rien à l'écran ne distingue les deux. Seul le contrôle des arêtes nues tranche, et il faut le faire avant de mesurer, pas après.

### Pièges fréquents

- Mesurer le volume d'un objet non fermé : la valeur sort quand même, et elle est fausse.
- Élargir la tolérance jusqu'à ce que ça ferme : les faces finissent par se joindre au mauvais endroit.

### Pourquoi ce jeu de données

Le caisson s'affiche exactement comme s'il était fermé : rien à l'écran ne distingue une enveloppe ouverte d'un solide. C'est ce qui rend le contrôle numérique indispensable, et non facultatif.

### Pour aller plus loin

- Mesurer le volume avant réparation et chiffrer l'écart.
- Ajouter un congé intérieur et refaire le contrôle.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-08_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-08_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-08.json` | Descripteur pour le plugin Magpie |
| `RH-08_fiche.md` | La présente fiche |
| `RH-08_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-08_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-08_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
