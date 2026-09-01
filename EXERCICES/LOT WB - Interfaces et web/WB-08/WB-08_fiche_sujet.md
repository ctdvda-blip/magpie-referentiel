# WB-08 — Les bornes qui empêchent l'infabricable

**Fiche d'exercice Magpie** · Lot WB — Interfaces, web et interopérabilité

| | |
|---|---|
| **Thématique** | WB1 · Interfaces utilisateur |
| **Référence au référentiel** | REF-157 |
| **Compétence visée** | Éprouver les bornes d'une interface en cherchant les combinaisons admises qui produisent une pièce infabricable. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | WB-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-17 Passation |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Éprouver les bornes d'une interface en cherchant les combinaisons admises qui produisent une pièce infabricable.

### Contexte

Chaque paramètre du configurateur est borné. Pris séparément, aucun ne pose problème ; c'est leur COMBINAISON qui décide.

### Énoncé

> Une tablette exige 180 mm de hauteur libre, plus son épaisseur. Les douze réglages soumis vous sont fournis : hauteur du meuble, nombre de tablettes, épaisseur. Donnez le nombre de réglages infabricables.

### Ce qui vous est fourni

Les douze combinaisons, et la règle de hauteur libre.

### Ce qui est attendu

3 réglages sur douze sont infabricables.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`WB-08_sujet.gh`

### Barème

1 point si le compte des réglages infabricables est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
