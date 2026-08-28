# QT-03 — Une nomenclature exportable

**Fiche d'exercice Magpie** · Lot QT — Quantitatifs, chiffrage et export

| | |
|---|---|
| **Thématique** | QT2 · Export de données |
| **Référence au référentiel** | REF-085, REF-086, REF-087 |
| **Compétence visée** | Mettre en forme des données de projet en un tableau exportable, colonne par colonne, et le sortir en fichier. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | A-27 |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-16 Enquête documentaire |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mettre en forme des données de projet en un tableau exportable, colonne par colonne, et le sortir en fichier.

### Contexte

Le bureau d'études attend la nomenclature des menuiseries au format tableur, pour la reprendre dans son chiffrage.

### Énoncé

> Les 18 menuiseries vous sont fournies avec leur repère, leur largeur et leur hauteur. Produisez le tableau à quatre colonnes — repère, largeur, hauteur, surface — et exportez-le en CSV. Donnez la surface totale, en mètres carrés.

### Ce qui vous est fourni

Les 18 repères, les 18 largeurs et les 18 hauteurs, en millimètres.

### Ce qui est attendu

La surface totale des menuiseries, en mètres carrés, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`QT-03_sujet.gh`

### Barème

1 point si la surface totale est juste et si le CSV s'ouvre en quatre colonnes distinctes.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
