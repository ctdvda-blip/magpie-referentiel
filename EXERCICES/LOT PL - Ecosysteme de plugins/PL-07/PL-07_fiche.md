# PL-07 — Ce qu'un plugin vous épargne d'écrire

**Fiche d'exercice Magpie** · Lot PL — Écosystème de plugins

| | |
|---|---|
| **Thématique** | PL1 · Écosystème de plugins |
| **Référence au référentiel** | REF-038, REF-039 |
| **Compétence visée** | Chiffrer ce qu'un plugin fait gagner en construction, pour le mettre en regard de ce qu'il coûte en dépendance. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | PL-04 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Chiffrer ce qu'un plugin fait gagner en construction, pour le mettre en regard de ce qu'il coûte en dépendance.

### Contexte

La question n'est jamais « ce plugin est-il bon ». Elle est « ce qu'il m'épargne vaut-il ce qu'il m'impose ».

### Énoncé

> Cinq tâches vous sont données, avec le nombre de composants qu'elles demandent en natif et avec le plugin adapté. Donnez le nombre de composants économisés au total.

### Ce qui vous est fourni

Les cinq tâches, et pour chacune le compte natif et le compte avec plugin.

### Ce qui est attendu

115 composants économisés — 123 en natif contre 8 avec plugins.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`PL-07_sujet.gh`

### Barème

1 point si l'économie totale est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `PL-07_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Sommer les comptes natifs.

**Étape 2.** Sommer les comptes avec plugins.

**Étape 3.** Soustraire.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Rendre le compte avec plugins (8) ou le compte natif (123) au lieu de l'écart. C'est l'ÉCART qui se met en balance avec le coût de la dépendance mesuré en PL-06 : 115 composants épargnés contre quatre postes sur sept qui ne pourront plus ouvrir le fichier.

### Pièges fréquents

- Rendre l'un des deux totaux.
- Conclure du gain seul, sans regarder ce que la dépendance coûte.

### Pourquoi ce jeu de données

Les rapports vont de 9 contre 1 à 34 contre 1 selon la tâche : le gain n'est pas uniforme, et l'exercice se prolonge naturellement en « lequel des cinq mérite vraiment sa dépendance ».

### Limite de la correction automatique

> Le nombre de composants n'est qu'un indice. Un plugin peut épargner peu de composants et beaucoup de justesse — une imbrication écrite à la main est fausse avant d'être longue.

### Pour aller plus loin

- Classer les cinq tâches par rapport gain sur dépendance.
- Reprendre en comptant les heures plutôt que les composants.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `PL-07_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `PL-07_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `PL-07.json` | Descripteur pour le plugin Magpie |
| `PL-07_fiche.md` | La présente fiche |
| `PL-07_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `PL-07_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `PL-07_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
