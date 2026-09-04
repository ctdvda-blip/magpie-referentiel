# IA-30 — Ce qu'un appel coûte dans une définition qui recalcule

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA7 · Vérification, licences et limites |
| **Référence au référentiel** | REF-142 |
| **Compétence visée** | Chiffrer le coût d'un service distant appelé depuis une définition qui recalcule à chaque manipulation. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 15 min |
| **Prérequis** | IA-13 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-03 Contre la montre |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Chiffrer le coût d'un service distant appelé depuis une définition qui recalcule à chaque manipulation.

### Contexte

Un composant qui interroge un modèle de langage se paie à l'appel. Dans une définition qui recalcule à chaque déplacement de curseur, la facture ne suit pas le nombre de réponses utiles.

### Énoncé

> La définition émet trois appels par recalcul, et la séance en a compté 240. Chaque appel coûte 0,004 € et prend 1,8 s. Donnez le coût de la séance, en euros.

### Ce qui vous est fourni

Le nombre d'appels par recalcul, le nombre de recalculs, le prix et la latence unitaires.

### Ce qui est attendu

2,88 € pour la séance.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-30_sujet.gh`

### Barème

1 point si le coût est juste au centime.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
