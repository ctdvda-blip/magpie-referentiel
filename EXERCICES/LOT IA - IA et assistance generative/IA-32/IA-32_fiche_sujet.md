# IA-32 — Ce qu'une demande floue laisse passer

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA1 · Formuler et cadrer une demande |
| **Référence au référentiel** | REF-117, REF-119 |
| **Compétence visée** | Mesurer l'écart entre plusieurs lectures défendables d'une même consigne, pour comprendre ce qu'une spécification doit trancher. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | IA-01 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 12 composants |
| **Gamification associée** | G-17 Le quiz éclair |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mesurer l'écart entre plusieurs lectures défendables d'une même consigne, pour comprendre ce qu'une spécification doit trancher.

### Contexte

« Compte les grandes valeurs » se lit de quatre façons. L'assistant en choisit une, silencieusement, et le résultat est juste au regard de sa lecture.

### Énoncé

> La consigne dit « compte les grandes valeurs » sur les seize relevés fournis. Appliquez-lui quatre lectures : strictement au-dessus de 500, au moins 500, au-dessus de la moyenne, au-dessus de la médiane. Donnez les quatre comptes, dans cet ordre.

### Ce qui vous est fourni

Les seize relevés et les quatre lectures à appliquer.

### Ce qui est attendu

Les quatre comptes, dans l'ordre : 7, 8, 9, 8.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-32_sujet.gh`

### Barème

1 point si les quatre comptes concordent dans l'ordre.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
