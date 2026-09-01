# PL-05 — Ce qu'un plugin traîne derrière lui

**Fiche d'exercice Magpie** · Lot PL — Écosystème de plugins

| | |
|---|---|
| **Thématique** | PL1 · Écosystème de plugins |
| **Référence au référentiel** | REF-029, REF-030 |
| **Compétence visée** | Établir la liste complète des paquets qu'une installation suppose, en suivant les dépendances jusqu'au bout. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | PL-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-06 Valise de chantier |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir la liste complète des paquets qu'une installation suppose, en suivant les dépendances jusqu'au bout.

### Contexte

Le poste du chantier n'a pas Internet. Ce qui n'est pas emporté sur la clé ne sera pas installé.

### Énoncé

> Le tableau des dépendances déclarées vous est fourni. Donnez le nombre total de paquets à emporter pour installer Nid, celui-ci compris.

### Ce qui vous est fourni

Le tableau des dépendances : pour chaque paquet, ceux qu'il exige.

### Ce qui est attendu

6 paquets — Nid, plus les cinq dont il dépend directement ou indirectement.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`PL-05_sujet.gh`

### Barème

1 point si le compte total est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
