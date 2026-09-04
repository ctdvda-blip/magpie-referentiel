# IA-31 — Ce que l'agent a modifié

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA7 · Agents et protocoles |
| **Référence au référentiel** | REF-136, REF-137, REF-138 |
| **Compétence visée** | Distinguer, dans le journal d'un agent, les opérations qui ont modifié le document de celles qui l'ont seulement lu. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 16 min |
| **Prérequis** | IA-12 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-16 La chasse au trésor |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Distinguer, dans le journal d'un agent, les opérations qui ont modifié le document de celles qui l'ont seulement lu.

### Contexte

Avant de laisser un agent travailler sur une définition, on veut savoir ce qu'il a touché. Le journal le dit, à condition de trier les lectures des écritures.

### Énoncé

> Le journal donne les vingt-deux opérations menées par l'agent. Donnez le nombre d'opérations qui ont MODIFIÉ le document.

### Ce qui vous est fourni

Le journal des vingt-deux opérations.

### Ce qui est attendu

10 opérations ont modifié le document.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-31_sujet.gh`

### Barème

1 point si le compte est exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-31_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser la liste des verbes d'écriture.

**Étape 2.** Pour chaque opération du journal, chercher si son verbe y figure.

**Étape 3.** Compter les correspondances.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Ne compter que les ajouts et les suppressions — cinq. Câbler, déplacer et renommer modifient le document tout autant : un fil rebranché change le résultat sans que rien n'apparaisse ni ne disparaisse, et c'est la modification la plus difficile à retrouver après coup.

### Pièges fréquents

- Réduire l'écriture à l'ajout et à la suppression.
- Compter les lectures.

### Pourquoi ce jeu de données

Vingt-deux opérations dont douze lectures. Les cinq verbes d'écriture se répartissent en trois familles — création, destruction, altération — et seule la troisième est oubliée par le compte naïf.

### Limite de la correction automatique

> Le journal dit ce que l'agent a FAIT, pas ce qu'il a cassé. Dix modifications peuvent être toutes justes, ou une seule peut avoir rompu la chaîne : c'est la raison pour laquelle on travaille sur une copie et qu'on versionne avant d'agir.

### Pour aller plus loin

- Donner le nombre d'opérations irréversibles.
- Reconstituer l'état du document après les dix modifications.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-31_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-31_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-31.json` | Descripteur pour le plugin Magpie |
| `IA-31_fiche.md` | La présente fiche |
| `IA-31_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-31_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-31_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
