# DV-04 — Du composant scripté au plugin installé

**Fiche d'exercice Magpie** · Lot DV — Développement, scripting et API

| | |
|---|---|
| **Thématique** | DV3 · Compilation et IDE |
| **Référence au référentiel** | REF-096, REF-097, REF-098, REF-099 |
| **Compétence visée** | Passer d'un composant scripté à un plugin compilé et installé, côté Grasshopper et côté Rhino. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Expert |
| **Durée cible** | 120 min |
| **Prérequis** | IA-07, DV-02 |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-25 Projet jalonné |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Passer d'un composant scripté à un plugin compilé et installé, côté Grasshopper et côté Rhino.

### Contexte

Un composant scripté qui a fait ses preuves doit être distribué à l'équipe, sans que chacun recolle du code.

### Énoncé

> Reprenez le composant scripté de DV-02 et faites-en un plugin compilé, installé et visible dans Grasshopper. Ajoutez-y une commande Rhino qui rend le même service depuis la ligne de commande.

### Ce qui vous est fourni

Le composant scripté de DV-02, un environnement de compilation et les modèles de projet Rhino.

### Ce qui est attendu

Un plugin chargé par Rhino, dont le composant apparaît dans Grasshopper et dont la commande répond en ligne de commande.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **Visuel**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`DV-04_sujet.gh`

### Barème

Grille : composant visible dans Grasshopper (2), commande Rhino opérante (2), GUID stable et version documentée (1).

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
