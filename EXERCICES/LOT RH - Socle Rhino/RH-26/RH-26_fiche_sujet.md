# RH-26 — Le poids du fichier à envoyer

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH5 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-022, REF-023, REF-024 |
| **Compétence visée** | Prévoir le poids d'un export maillé à partir du nombre de triangles et du format retenu. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | RH-22 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-05 La collection de badges |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Prévoir le poids d'un export maillé à partir du nombre de triangles et du format retenu.

### Contexte

Un STL s'envoie à un prestataire. Savoir avant l'export s'il fera sept mégaoctets ou trente-cinq décide du format et du moyen de transmission.

### Énoncé

> Le maillage compte 148 520 triangles. Un STL binaire pèse 84 octets d'en-tête plus 50 octets par triangle. Donnez le poids du fichier, en octets.

### Ce qui vous est fourni

Le nombre de triangles du maillage et la structure du format.

### Ce qui est attendu

7 426 084 octets, soit 7,08 Mo.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-26_sujet.gh`

### Barème

1 point si le poids est exact à l'octet.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
