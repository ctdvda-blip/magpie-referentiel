# PL-06 — Qui pourra ouvrir votre définition

**Fiche d'exercice Magpie** · Lot PL — Écosystème de plugins

| | |
|---|---|
| **Thématique** | PL1 · Écosystème de plugins |
| **Référence au référentiel** | REF-038, REF-039 |
| **Compétence visée** | Mesurer ce qu'une dépendance à des plugins coûte en portabilité, avant de livrer. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | PL-05 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-17 Passation |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mesurer ce qu'une dépendance à des plugins coûte en portabilité, avant de livrer.

### Contexte

La définition part chez sept destinataires. Chez ceux qui n'ont pas les plugins, elle s'ouvrira — avec des composants rouges à la place du calcul.

### Énoncé

> Votre définition exige trois plugins. L'inventaire des sept postes destinataires vous est fourni. Donnez le nombre de postes qui pourront l'exécuter.

### Ce qui vous est fourni

Les trois plugins requis, et pour chacun des sept postes la liste de ceux qu'il possède.

### Ce qui est attendu

3 postes sur 7 pourront l'exécuter.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`PL-06_sujet.gh`

### Barème

1 point si le compte des postes capables est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
