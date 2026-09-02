# IA-09 — Prédire une déperdition sur une baie nouvelle

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA4 · Apprentissage automatique |
| **Référence au référentiel** | REF-129, REF-131, REF-132 |
| **Compétence visée** | Ajuster un modèle sur des mesures existantes et l'employer pour prédire un cas non mesuré. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | IA-04 |
| **Mode de validation** | NumericTolerance — tolérance 10 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Ajuster un modèle sur des mesures existantes et l'employer pour prédire un cas non mesuré.

### Contexte

Les déperditions ont été mesurées sur 24 baies d'un bâtiment existant ; une 25e baie est projetée et il faut l'estimer avant instrumentation.

### Énoncé

> Les surfaces et les déperditions mesurées des 24 baies vous sont fournies. Estimez la déperdition d'une baie de 2,75 m².

### Ce qui vous est fourni

Les 24 couples surface / déperdition mesurés, et la surface de la baie à estimer.

### Ce qui est attendu

Environ 380 W — la déperdition estimée pour une baie de 2,75 m², acceptée à 10 W près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 10.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-09_sujet.gh`

### Barème

1 point si l'estimation tombe à 10 W près de la valeur de référence.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-09_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Placer les mesures et les visualiser avant tout calcul : la relation se voit à l'œil et oriente le choix du modèle.

**Étape 2.** Ajuster un modèle sur les 24 couples.

**Étape 3.** Appliquer le modèle à la surface visée.

**Étape 4.** Contrôler l'estimation par un rapport simple — déperdition par mètre carré sur les baies voisines en surface.

**Étape 5.** Écarter l'estimation si elle sort de cet encadrement.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Estimer par la moyenne des déperditions plutôt que par la relation à la surface. La valeur obtenue est du bon ordre de grandeur — ce qui la rend dangereuse — mais ne suit pas la surface, et l'erreur explose sur les baies extrêmes.

### Pièges fréquents

- Ajuster sur toutes les données puis évaluer sur les mêmes : on ne mesure alors que la capacité du modèle à retenir, pas à prédire.
- Extrapoler hors de la plage mesurée sans le signaler.

### Pourquoi ce jeu de données

24 couples couvrant 1,10 à 3,60 m², assez dispersés pour qu'un ajustement soit nécessaire, et assez cohérents pour qu'il ait un sens. La baie à estimer tombe en milieu de plage : l'exercice porte sur l'ajustement, pas sur l'extrapolation, qui est un autre sujet.

### Pour aller plus loin

- Retirer les quatre plus grandes baies de l'ajustement et estimer l'une d'elles : mesurer ce que coûte l'extrapolation.
- Comparer l'estimation à un simple rapport moyen et chiffrer l'écart.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-09_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-09_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-09.json` | Descripteur pour le plugin Magpie |
| `IA-09_fiche.md` | La présente fiche |
| `IA-09_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-09_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-09_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
