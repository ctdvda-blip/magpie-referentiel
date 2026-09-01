# FA-02 — Le développé d'une virole

**Fiche d'exercice Magpie** · Lot FA — Aide à la fabrication

| | |
|---|---|
| **Thématique** | FA2 · Déroulé et mise à plat |
| **Référence au référentiel** | REF-115, REF-116 |
| **Compétence visée** | Établir le développé à plat d'une surface réglée et le contrôler par un calcul indépendant. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | A-42 |
| **Mode de validation** | NumericTolerance — tolérance 0,0001 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir le développé à plat d'une surface réglée et le contrôler par un calcul indépendant.

### Contexte

Une virole conique de ventilation se découpe à plat dans la tôle avant d'être roulée.

### Énoncé

> La virole relie un diamètre de 360 mm à un diamètre de 190 mm sur une hauteur de 340 mm. Produisez son développé à plat et donnez la surface développée, en mètres carrés.

### Ce qui vous est fourni

Les deux rayons et la hauteur, en valeurs réglables.

### Ce qui est attendu

La surface développée, en mètres carrés, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`FA-02_sujet.gh`

### Barème

1 point si la surface développée est juste et si le contrôle par le calcul est fourni.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
