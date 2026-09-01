# DV-07 — Un plugin qui s'installe chez quelqu'un d'autre

**Fiche d'exercice Magpie** · Lot DV — Développement, scripting et API

| | |
|---|---|
| **Thématique** | DV3 · Compilation et IDE |
| **Référence au référentiel** | REF-098 |
| **Compétence visée** | Livrer un plugin qui se charge sur un poste qui n'est pas celui du développeur, et le prouver. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Expert |
| **Durée cible** | 50 min |
| **Prérequis** | DV-06 |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-23 Livraison à l'aveugle |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Livrer un plugin qui se charge sur un poste qui n'est pas celui du développeur, et le prouver.

### Contexte

Le plugin marche sur votre poste. C'est la situation la moins informative qui soit : votre poste porte le SDK, les dépendances et les chemins de développement.

### Énoncé

> Reprenez le plugin de DV-04 et rendez-le installable : manifeste renseigné, dépendances embarquées ou déclarées, version visible. Faites-le installer par quelqu'un d'autre, sur un poste où l'environnement de développement n'est pas présent, et faites-lui exécuter le composant sans un mot d'explication.

### Ce qui vous est fourni

Le plugin de DV-04, et un poste qui n'est pas le vôtre.

### Ce qui est attendu

Un plugin installé et fonctionnel sur un poste tiers, dont le composant apparaît dans l'onglet visé et rend le résultat attendu.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **Visuel**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`DV-07_sujet.gh`

### Barème

Grille : manifeste complet (1), dépendances traitées (1), installation réussie sur un poste tiers (2), composant exécuté sans assistance (1).

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
