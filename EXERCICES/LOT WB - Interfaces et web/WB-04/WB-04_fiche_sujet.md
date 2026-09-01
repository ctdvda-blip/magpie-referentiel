# WB-04 — Ce qu'on expose, et ce qu'on cache

**Fiche d'exercice Magpie** · Lot WB — Interfaces, web et interopérabilité

| | |
|---|---|
| **Thématique** | WB1 · Interfaces utilisateur |
| **Référence au référentiel** | REF-107 |
| **Compétence visée** | Distinguer, parmi les entrées d'une définition, celles qui relèvent d'un choix de l'utilisateur de celles qui se déduisent ou qui règlent l'outil. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | WB-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-17 Passation |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Distinguer, parmi les entrées d'une définition, celles qui relèvent d'un choix de l'utilisateur de celles qui se déduisent ou qui règlent l'outil.

### Contexte

La définition va être pilotée depuis Rhino par quelqu'un qui n'ouvrira jamais le graphe. Tout ce qu'on expose, il faudra le lui expliquer ; tout ce qu'on cache, il ne pourra plus le régler.

### Énoncé

> La définition du meuble compte quatorze entrées, décrites une à une avec ce qu'elles commandent et ce dont elles dépendent. Donnez le nombre d'entrées à exposer dans l'interface.

### Ce qui vous est fourni

La liste des quatorze entrées et leur description.

### Ce qui est attendu

6 — les six entrées qui relèvent d'un choix du client.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`WB-04_sujet.gh`

### Barème

1 point si le compte est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
