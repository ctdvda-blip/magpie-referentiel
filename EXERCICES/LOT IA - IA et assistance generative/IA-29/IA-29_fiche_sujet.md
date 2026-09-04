# IA-29 — Les GUID qui cassent les définitions

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA3 · Développement de plugins assisté |
| **Référence au référentiel** | REF-128 |
| **Compétence visée** | Mesurer l'effet d'un GUID régénéré sur le parc de définitions existantes. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 18 min |
| **Prérequis** | IA-08 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-29 Le défi du jour |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mesurer l'effet d'un GUID régénéré sur le parc de définitions existantes.

### Contexte

Publier la version suivante d'un plugin ne doit pas casser les définitions déjà écrites. Un GUID régénéré rend un composant introuvable, et la définition s'ouvre avec un trou.

### Énoncé

> Le tableau donne, pour huit composants du plugin, si leur GUID a été conservé d'une version à l'autre et combien de définitions les emploient. Donnez le nombre de définitions cassées par la mise à jour.

### Ce qui vous est fourni

Le tableau des huit composants, de leurs GUID et de leur usage.

### Ce qui est attendu

16 définitions sont cassées par la mise à jour.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-29_sujet.gh`

### Barème

1 point si le compte est exact.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
