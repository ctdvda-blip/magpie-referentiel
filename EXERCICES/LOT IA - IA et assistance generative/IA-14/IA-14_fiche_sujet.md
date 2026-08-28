# IA-14 — Le résultat plausible et faux

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA7 · Vérification, licences et limites |
| **Référence au référentiel** | REF-139, REF-142 |
| **Compétence visée** | Contrôler un résultat produit par une IA par un moyen indépendant de la manière dont il a été obtenu. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | IA-01 |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-11 Chasse à l'erreur |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
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

40 800 000 mm³, soit 0,0408 m³ — à comparer aux 40,8 m³ annoncés par le composant fourni.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-14_sujet.gh`

### Barème

1 point si le volume exact est donné et si l'écart du composant fourni est expliqué.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
