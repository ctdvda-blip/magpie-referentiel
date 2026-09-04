# IA-30 — Ce qu'un appel coûte dans une définition qui recalcule

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA5 · Vérification, licences et limites |
| **Référence au référentiel** | REF-142 |
| **Compétence visée** | Chiffrer le coût d'un service distant appelé depuis une définition qui recalcule à chaque manipulation. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 15 min |
| **Prérequis** | IA-13 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-03 Contre la montre |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Chiffrer le coût d'un service distant appelé depuis une définition qui recalcule à chaque manipulation.

### Contexte

Un composant qui interroge un modèle de langage se paie à l'appel. Dans une définition qui recalcule à chaque déplacement de curseur, la facture ne suit pas le nombre de réponses utiles.

### Énoncé

> La définition émet trois appels par recalcul, et la séance en a compté 240. Chaque appel coûte 0,004 € et prend 1,8 s. Donnez le coût de la séance, en euros.

### Ce qui vous est fourni

Le nombre d'appels par recalcul, le nombre de recalculs, le prix et la latence unitaires.

### Ce qui est attendu

2,88 € pour la séance.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-30_sujet.gh`

### Barème

1 point si le coût est juste au centime.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-30_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Multiplier les recalculs par les appels de chacun.

**Étape 2.** Multiplier par le prix unitaire.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter un appel par recalcul : 0,96 €, trois fois moins. La définition en émet trois — un par branche du graphe — et c'est le genre de multiplication qu'on ne découvre qu'à la facture.

### Pièges fréquents

- Oublier les trois appels par recalcul.
- Confondre le coût et la latence.

### Pourquoi ce jeu de données

720 appels pour une séance de travail ordinaire, et 1 296 s d'attente cumulée, soit vingt-deux minutes. Les deux nombres disent la même chose de deux façons : le coût se voit sur la facture, la latence se subit tout de suite.

### Limite de la correction automatique

> Le calcul suppose le prix et la latence CONSTANTS. Les deux varient avec la taille de la demande et la charge du service, et un modèle plus grand peut coûter dix fois plus pour la même question.

### Pour aller plus loin

- Donner l'attente cumulée en minutes.
- Chercher le nombre de recalculs qui tient dans un budget de 1 €.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-30_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-30_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-30.json` | Descripteur pour le plugin Magpie |
| `IA-30_fiche.md` | La présente fiche |
| `IA-30_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-30_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-30_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
