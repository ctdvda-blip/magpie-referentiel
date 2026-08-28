# IA-05 — Le code qui tourne et se trompe

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA2 · Composants scriptés assistés |
| **Référence au référentiel** | REF-124 |
| **Compétence visée** | Localiser une erreur de logique dans un code qui s'exécute sans planter. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 22 min |
| **Prérequis** | IA-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-11 Chasse à l'erreur |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Localiser une erreur de logique dans un code qui s'exécute sans planter.

### Contexte

Un composant livré par un confrère chiffre le nombre de tronçons dépassant une longueur de transport de 4 mètres.

### Énoncé

> Le composant fourni s'exécute sans erreur et annonce un résultat. Ce résultat est faux. Trouvez pourquoi et faites-le corriger, puis donnez le nombre exact de tronçons concernés.

### Ce qui vous est fourni

Les 16 longueurs de tronçons, en mètres, et un composant scripté déjà en place qui les traite.

### Ce qui est attendu

9 — le nombre de tronçons de plus de 4 mètres.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-05_sujet.gh`

### Barème

1 point si la sortie corrigée vaut 9.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
