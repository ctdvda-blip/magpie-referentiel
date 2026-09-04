# WB-11 — Le temps de calcul, une fois en ligne

**Fiche d'exercice Magpie** · Lot WB — Interfaces, web et interopérabilité

| | |
|---|---|
| **Thématique** | WB2 · Publication web |
| **Référence au référentiel** | REF-108, REF-109, REF-110 |
| **Compétence visée** | Estimer le temps de réponse d'une définition publiée en ligne, en tenant compte de l'écart entre le poste et le serveur. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 16 min |
| **Prérequis** | WB-06 |
| **Mode de validation** | NumericTolerance — tolérance 0.0001 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-03 Contre la montre |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Estimer le temps de réponse d'une définition publiée en ligne, en tenant compte de l'écart entre le poste et le serveur.

### Contexte

Un configurateur publié doit répondre en quelques secondes. Ce qui tourne en dix secondes sur le poste du concepteur peut dépasser la limite du service une fois en ligne.

### Énoncé

> Le profilage donne le temps de recalcul des vingt-quatre composants sur votre poste, en millisecondes. Le serveur est 2,4 fois plus lent. Donnez le temps de réponse en ligne, en secondes.

### Ce qui vous est fourni

Le relevé des vingt-quatre temps et le facteur serveur.

### Ce qui est attendu

25,1736 s de temps de réponse en ligne, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`WB-11_sujet.gh`

### Barème

1 point si le temps est juste à 0,0001 s.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `WB-11_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Sommer les vingt-quatre temps locaux.

**Étape 2.** Multiplier par le facteur serveur.

**Étape 3.** Convertir en secondes.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Oublier le facteur serveur : 10,489 s, sous la limite de vingt secondes. La définition est alors publiée, et c'est le premier visiteur qui découvre qu'elle dépasse — le profilage local donne toujours le résultat rassurant.

### Pièges fréquents

- Oublier le facteur.
- Multiplier chaque temps puis re-multiplier la somme.

### Pourquoi ce jeu de données

Vingt-quatre composants de 20 à 900 ms. Le total local passe sous la limite, le total en ligne la dépasse de cinq secondes : c'est le cas qui décide, et il est invisible tant qu'on ne multiplie pas.

### Limite de la correction automatique

> Le facteur 2,4 est une MOYENNE mesurée. Il varie avec le type d'opération — un maillage et une intersection ne se dégradent pas dans le même rapport — et ne dit rien de la latence réseau, qui s'ajoute au temps de calcul.

### Pour aller plus loin

- Chercher les composants à retirer pour tenir sous vingt secondes.
- Refaire le calcul avec un facteur de 1,8.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `WB-11_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `WB-11_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `WB-11.json` | Descripteur pour le plugin Magpie |
| `WB-11_fiche.md` | La présente fiche |
| `WB-11_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `WB-11_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `WB-11_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
