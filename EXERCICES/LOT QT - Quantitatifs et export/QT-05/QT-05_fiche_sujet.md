# QT-05 — Le fichier que le fournisseur va lire

**Fiche d'exercice Magpie** · Lot QT — Quantitatifs, chiffrage et export

| | |
|---|---|
| **Thématique** | QT2 · Export de données |
| **Référence au référentiel** | REF-086, REF-087 |
| **Compétence visée** | Produire un fichier d'échange dont la structure est celle qu'attend le destinataire, en-tête comprise, et savoir combien de lignes il doit contenir avant de l'ouvrir. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | QT-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-11 Commande à passer |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Produire un fichier d'échange dont la structure est celle qu'attend le destinataire, en-tête comprise, et savoir combien de lignes il doit contenir avant de l'ouvrir.

### Contexte

La commande part en CSV vers le fournisseur, qui l'importe automatiquement. Un fichier mal structuré n'est pas rejeté : il est importé de travers.

### Énoncé

> Vous exportez la commande regroupée de l'exercice précédent au format CSV, avec une ligne d'en-tête nommant les colonnes. Donnez le nombre de lignes que le fichier doit contenir.

### Ce qui vous est fourni

Le débit de vingt-quatre lignes, et la commande regroupée qui en découle.

### Ce qui est attendu

9 — huit références, plus la ligne d'en-tête.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`QT-05_sujet.gh`

### Barème

1 point si le nombre de lignes est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
