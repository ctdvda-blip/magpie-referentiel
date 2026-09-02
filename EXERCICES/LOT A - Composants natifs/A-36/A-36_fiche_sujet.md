# A-36 — Courbes passant par des points

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A8 · Géométrie vectorielle et filaire |
| **Référence au référentiel** | REF-063 |
| **Compétence visée** | Distinguer une courbe qui passe par des points d'une courbe que ces points contrôlent. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-35 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-12 Memory |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Distinguer une courbe qui passe par des points d'une courbe que ces points contrôlent.

### Contexte

Un profil de main courante est défini par des points de passage imposés ; un second tracé, plus souple, sert d'étude de forme.

### Énoncé

> Six points vous sont fournis. Tracez la courbe qui passe exactement par chacun d'eux, puis celle qui ne fait que s'en approcher en les prenant pour points de commande. Superposez les deux.

### Ce qui vous est fourni

Une liste de 6 points internalisée.

### Ce qui est attendu

Deux courbes distinctes appuyées sur les mêmes points.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-36_sujet.gh`

### Barème

1 point par courbe correcte.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
