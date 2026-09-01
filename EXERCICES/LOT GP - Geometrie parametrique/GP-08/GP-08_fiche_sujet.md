# GP-08 — Ce que coûte une subdivision de plus

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP4 · Maillages et SubD |
| **Référence au référentiel** | REF-077, REF-078 |
| **Compétence visée** | Anticiper la croissance d'une surface de subdivision, et choisir le niveau d'affichage en connaissance de cause. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 20 min |
| **Prérequis** | GP-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Anticiper la croissance d'une surface de subdivision, et choisir le niveau d'affichage en connaissance de cause.

### Contexte

La cage de subdivision est légère et se manipule bien. C'est l'affichage lissé qui fait ramer la machine.

### Énoncé

> La cage compte 26 faces. Chaque passe de subdivision remplace chaque face par quatre. Donnez le nombre de faces après trois passes.

### Ce qui vous est fourni

Le nombre de faces de la cage et le nombre de passes.

### Ce qui est attendu

1 664 faces après trois passes.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-08_sujet.gh`

### Barème

1 point si le nombre de faces est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
