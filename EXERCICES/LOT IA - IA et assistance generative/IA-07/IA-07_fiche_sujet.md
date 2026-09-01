# IA-07 — Un plugin .gha conduit par un agent

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA3 · Développement de plugins assisté |
| **Référence au référentiel** | REF-125, REF-126, REF-127 |
| **Compétence visée** | Conduire le développement d'un plugin Grasshopper avec un agent de code, jusqu'au composant réellement chargé par Rhino. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 90 min |
| **Prérequis** | IA-06 |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-25 Projet jalonné |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Conduire le développement d'un plugin Grasshopper avec un agent de code, jusqu'au composant réellement chargé par Rhino.

### Contexte

Un geste répété dans plusieurs définitions mérite son propre composant, distribuable à l'équipe.

### Énoncé

> Choisissez un traitement que vous refaites souvent à la main. Faites-en un composant distribuable, chargé par Rhino et visible dans l'onglet de votre choix, en conduisant le développement avec un agent de code.

### Ce qui vous est fourni

Un poste avec l'environnement de compilation en place et un agent de code disposant de l'accès aux fichiers du projet.

### Ce qui est attendu

Un plugin chargé par Rhino, dont le composant apparaît dans l'onglet visé et produit le résultat attendu.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **Visuel**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-07_sujet.gh`

### Barème

Grille : composant chargé (2), résultat juste (2), GUID stable entre deux versions (1), documentation (1).

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
