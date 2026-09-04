# WB-05 — Dimensionner le calcul d'un configurateur

**Fiche d'exercice Magpie** · Lot WB — Interfaces, web et interopérabilité

| | |
|---|---|
| **Thématique** | WB3 · Interopérabilité |
| **Référence au référentiel** | REF-112 |
| **Compétence visée** | Dimensionner une capacité de calcul distante à partir de la fréquentation attendue, en raisonnant sur la pointe et non sur la moyenne. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Expert |
| **Durée cible** | 30 min |
| **Prérequis** | WB-03 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-22 Mise en charge |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Dimensionner une capacité de calcul distante à partir de la fréquentation attendue, en raisonnant sur la pointe et non sur la moyenne.

### Contexte

Le configurateur en ligne délègue ses recalculs à un service distant, facturé à l'instance et à l'heure. Sous-dimensionné, il fait attendre ; sur-dimensionné, il coûte pour rien.

### Énoncé

> Le configurateur reçoit 12 000 visites par jour, dont 18 % se concentrent sur l'heure de pointe. Chaque visite déclenche 6 recalculs, et un recalcul occupe une instance pendant 1,2 seconde. Donnez le nombre d'instances nécessaires pour tenir la pointe sans faire attendre.

### Ce qui vous est fourni

La fréquentation quotidienne, la part de l'heure de pointe, le nombre de recalculs par visite et la durée d'un recalcul.

### Ce qui est attendu

5 instances — la pointe demande 15 552 secondes de calcul pour 3 600 secondes d'horloge.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`WB-05_sujet.gh`

### Barème

1 point si le nombre d'instances est juste et arrondi au supérieur.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `WB-05_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Ramener la fréquentation à l'heure de pointe.

**Étape 2.** En déduire le nombre de recalculs à absorber dans l'heure.

**Étape 3.** Convertir en secondes de calcul demandées.

**Étape 4.** Rapporter aux 3 600 secondes que rend une instance en une heure.

**Étape 5.** Arrondir au SUPÉRIEUR : une instance ne se loue pas par quart.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Lisser la charge sur les vingt-quatre heures : 12 000 × 6 × 1,2 ÷ 86 400 donne 1 instance. Le service tiendra la nuit et s'effondrera à l'heure où il y a du monde, c'est-à-dire au seul moment qui compte. Un dimensionnement à la moyenne est un dimensionnement pour personne.

### Pièges fréquents

- Dimensionner sur la moyenne quotidienne.
- Arrondir au plus proche : 4,32 devient 4, et la pointe déborde.
- Oublier les six recalculs par visite et compter une visite pour un calcul.

### Pourquoi ce jeu de données

Une pointe à 18 % de la journée correspond à ce qu'observent les configurateurs grand public, dont le trafic se concentre en soirée. Le rapport entre le dimensionnement à la pointe (5) et à la moyenne (1) vaut cinq : l'erreur ne se rattrape pas par une marge de sécurité.

### Limite de la correction automatique

> Le calcul suppose des recalculs indépendants et de durée constante. Une mise en cache des configurations les plus demandées change tout — et c'est le premier levier à actionner avant d'acheter des instances.

### Pour aller plus loin

- Ajouter un cache qui absorbe 40 % des recalculs et refaire le dimensionnement.
- Chiffrer le coût mensuel des deux hypothèses, et le comparer au coût d'une seconde d'attente pour un visiteur.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `WB-05_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `WB-05_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `WB-05.json` | Descripteur pour le plugin Magpie |
| `WB-05_fiche.md` | La présente fiche |
| `WB-05_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `WB-05_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `WB-05_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
