# IA-03 — Reprendre une demande sur le point qui échoue

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA1 · Formuler et cadrer une demande |
| **Référence au référentiel** | REF-119 |
| **Compétence visée** | Isoler ce qui échoue dans un code produit et reformuler la demande sur ce seul point. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 18 min |
| **Prérequis** | IA-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-07 Indice progressif |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Isoler ce qui échoue dans un code produit et reformuler la demande sur ce seul point.

### Contexte

Un relevé de planéité de plancher doit être classé : on cherche l'amplitude totale, du point le plus haut au plus bas.

### Énoncé

> Les 28 niveaux relevés vous sont fournis, en millimètres autour du zéro. Faites produire un composant qui renvoie l'amplitude du relevé. Le premier code obtenu donnera un résultat faux : reprenez la demande sur le seul point fautif, sans la réécrire en entier.

### Ce qui vous est fourni

Les 28 niveaux relevés, en millimètres, positifs et négatifs.

### Ce qui est attendu

48 — l'écart entre le point le plus haut (+25) et le plus bas (−23).

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-03_sujet.gh`

### Barème

1 point si la sortie vaut 48 après une seule reformulation.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
