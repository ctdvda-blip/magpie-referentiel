# IA-25 — Ce que le service coûte par mois

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA4 · Vérification, licences et limites |
| **Référence au référentiel** | REF-142 |
| **Compétence visée** | Chiffrer le coût d'usage d'un service d'IA à partir de sa consommation réelle, en distinguant ce qui entre de ce qui sort. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | IA-13 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-16 Livrable pesé |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Chiffrer le coût d'usage d'un service d'IA à partir de sa consommation réelle, en distinguant ce qui entre de ce qui sort.

### Contexte

Le composant appelle un service distant à chaque recalcul. La facture arrive à la fin du mois, et personne n'a chiffré avant.

### Énoncé

> Le service traite 4 200 requêtes par mois. Chacune envoie 1 850 jetons et en reçoit 320. L'entrée est facturée 3 € le million de jetons, la sortie 15 €. Donnez le coût mensuel, en euros.

### Ce qui vous est fourni

Le nombre de requêtes, les jetons échangés par requête, et les deux tarifs.

### Ce qui est attendu

43,47 € par mois.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-25_sujet.gh`

### Barème

1 point si le coût mensuel est juste au centime.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
