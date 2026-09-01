# IA-15 — Relire le graphe qu'un agent a construit

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA7 · Agents et protocoles |
| **Référence au référentiel** | REF-137 |
| **Compétence visée** | Confronter le graphe produit par un agent à la spécification qu'on lui avait donnée, et compter ce qui diverge — plutôt que de juger sur l'aperçu. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | IA-12 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-20 Contre-expertise |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Confronter le graphe produit par un agent à la spécification qu'on lui avait donnée, et compter ce qui diverge.

### Contexte

L'agent a construit la définition en trente secondes. L'aperçu montre un volume plausible. C'est précisément le moment où l'on ne vérifie pas.

### Énoncé

> Vous aviez spécifié neuf liaisons, chacune avec son entrée de destination. Le relevé du graphe produit vous est fourni en regard. Donnez le nombre de liaisons qui ne sont pas conformes à la spécification.

### Ce qui vous est fourni

Les neuf liaisons demandées et les neuf liaisons produites, chacune avec l'indice de l'entrée de destination.

### Ce qui est attendu

3 — trois liaisons aboutissent sur une autre entrée que celle demandée.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-15_sujet.gh`

### Barème

1 point si le nombre de divergences est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
