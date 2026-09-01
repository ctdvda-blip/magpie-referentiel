# A-28 — Découper et remplacer du texte

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A6 · Outils de texte |
| **Référence au référentiel** | REF-058 |
| **Compétence visée** | Extraire un fragment d'une référence structurée et le normaliser. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-27 |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-19 Le composant mystère |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Extraire un fragment d'une référence structurée et le normaliser.

### Contexte

Les références fournisseur encodent la famille, le code produit et l'essence ; seul le code produit alimente la commande.

### Énoncé

> Les références vous sont fournies au format « MEUB-A12-CHENE ». Extrayez le seul code central et livrez-le en minuscules.

### Ce qui vous est fourni

Une liste de 6 références internalisée.

### Ce qui est attendu

Six codes en minuscules : a12, b07, …

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **Visuel**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-28_sujet.gh`

### Barème

1 point si les 6 codes sont exacts.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
