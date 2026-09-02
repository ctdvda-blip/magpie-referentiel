# IA-17 — Une commande cachée dans un courriel

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA6 · Modèles de langage et IA générative |
| **Référence au référentiel** | REF-134 |
| **Compétence visée** | Extraire d'un texte libre les données chiffrées qui engagent, en distinguant ce qui est commandé de ce qui est seulement évoqué. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | IA-11 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-18 Dictée technique |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Extraire d'un texte libre les données chiffrées qui engagent, en distinguant ce qui est commandé de ce qui est seulement évoqué.

### Contexte

Le conducteur de travaux commande sa quincaillerie par courriel, en une phrase par ligne et sans tableau. La commande doit en sortir chiffrée.

### Énoncé

> Le courriel vous est fourni tel qu'il a été reçu. Donnez le nombre total de pièces réellement commandées.

### Ce qui vous est fourni

Le courriel du conducteur de travaux, en texte libre.

### Ce qui est attendu

96 pièces — 24 paumelles, 48 vis, 18 poignées et 6 serrures.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-17_sujet.gh`

### Barème

1 point si le total est juste.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
