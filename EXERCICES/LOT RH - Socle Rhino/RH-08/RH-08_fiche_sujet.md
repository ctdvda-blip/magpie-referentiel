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

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
