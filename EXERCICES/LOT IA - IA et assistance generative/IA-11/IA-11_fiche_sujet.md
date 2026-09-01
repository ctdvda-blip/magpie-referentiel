# IA-11 — Un cahier des charges qui devient des paramètres

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA5 · Modèles de langage et IA générative |
| **Référence au référentiel** | REF-133, REF-134, REF-135 |
| **Compétence visée** | Extraire d'un texte de prescription les valeurs exploitables par une définition, et les contrôler. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | IA-03 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-16 Enquête documentaire |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Extraire d'un texte de prescription les valeurs exploitables par une définition, et les contrôler.

### Contexte

Un article de CCTP décrit un garde-corps en toutes lettres ; la définition attend des nombres.

### Énoncé

> L'article de CCTP vous est fourni. Faites-en extraire les valeurs dimensionnelles par un modèle de langage, puis donnez le nombre de montants nécessaires pour la longueur prescrite.

### Ce qui vous est fourni

Le texte de l'article, internalisé dans la définition, et l'accès à un modèle de langage.

### Ce qui est attendu

Le nombre de montants, entracte maximal respecté.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-11_sujet.gh`

### Barème

1 point si le nombre de montants est juste et si chaque valeur extraite est justifiée par sa phrase source.

---

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
