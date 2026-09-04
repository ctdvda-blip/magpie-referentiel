# GP-07 — Ce que la soudure retire

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP4 · Maillages et SubD |
| **Référence au référentiel** | REF-076 |
| **Compétence visée** | Mesurer la redondance d'un maillage construit face par face, et ce que la soudure des sommets lui retire. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | GP-06 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-16 Livrable pesé |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mesurer la redondance d'un maillage construit face par face, et ce que la soudure des sommets lui retire.

### Contexte

Le maillage a été construit quadrangle par quadrangle. Chaque face porte ses quatre sommets, sans savoir que ses voisines portent les mêmes.

### Énoncé

> La nappe compte 48 divisions par 30, en quadrangles construits un à un. Donnez le nombre de sommets que la soudure supprimera.

### Ce qui vous est fourni

Les deux nombres de divisions, et le mode de construction face par face.

### Ce qui est attendu

4 241 sommets supprimés — de 5 760 à 1 519.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-07_sujet.gh`

### Barème

1 point si le nombre de sommets supprimés est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
