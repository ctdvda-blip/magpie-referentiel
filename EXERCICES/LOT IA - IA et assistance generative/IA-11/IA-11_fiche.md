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

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-11_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Demander une extraction structurée, en imposant la liste des grandeurs attendues et leur unité.

**Étape 2.** Exiger que chaque valeur soit accompagnée de la phrase dont elle provient : c'est ce qui rend le contrôle possible.

**Étape 3.** Relire chaque valeur contre sa phrase d'origine.

**Étape 4.** Alimenter le calcul du nombre de montants avec les valeurs contrôlées.

**Étape 5.** Appliquer l'arrondi qu'impose le contexte : il faut au moins autant de montants, donc au supérieur.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Reprendre telle quelle une valeur extraite sans la confronter au texte. Un modèle qui hésite entre deux nombres du même paragraphe produit une valeur crédible et fausse, et rien dans la définition ne le signalera.

### Pièges fréquents

- Accepter une extraction sans justification textuelle.
- Arrondir au plus proche le nombre de montants : il en manque un une fois sur deux.

### Pourquoi ce jeu de données

Le texte contient volontairement deux dimensions proches — une hauteur et un entraxe — de sorte qu'une extraction non contrôlée puisse les intervertir sans que le résultat paraisse absurde.

### Limite de la correction automatique

> L'extraction elle-même n'est pas reproductible à l'identique d'un appel à l'autre : c'est le nombre de montants, contrôlé contre le texte, qui est validé — pas la sortie brute du modèle.

### Pour aller plus loin

- Rejouer l'extraction trois fois et comparer les résultats : la variabilité fait partie du sujet.
- Ajouter une prescription contradictoire dans le texte et observer ce que le modèle en fait.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-11_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-11_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-11.json` | Descripteur pour le plugin Magpie |
| `IA-11_fiche.md` | La présente fiche |
| `IA-11_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-11_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-11_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
