# PL-05 — Ce qu'un plugin traîne derrière lui

**Fiche d'exercice Magpie** · Lot PL — Écosystème de plugins

| | |
|---|---|
| **Thématique** | PL1 · Écosystème de plugins |
| **Référence au référentiel** | REF-029, REF-030 |
| **Compétence visée** | Établir la liste complète des paquets qu'une installation suppose, en suivant les dépendances jusqu'au bout. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | PL-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-06 Valise de chantier |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir la liste complète des paquets qu'une installation suppose, en suivant les dépendances jusqu'au bout.

### Contexte

Le poste du chantier n'a pas Internet. Ce qui n'est pas emporté sur la clé ne sera pas installé.

### Énoncé

> Le tableau des dépendances déclarées vous est fourni. Donnez le nombre total de paquets à emporter pour installer Nid, celui-ci compris.

### Ce qui vous est fourni

Le tableau des dépendances : pour chaque paquet, ceux qu'il exige.

### Ce qui est attendu

6 paquets — Nid, plus les cinq dont il dépend directement ou indirectement.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`PL-05_sujet.gh`

### Barème

1 point si le compte total est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `PL-05_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Relever les dépendances directes du paquet visé.

**Étape 2.** Relever celles de chacune, et ainsi de suite.

**Étape 3.** Écarter les doublons.

**Étape 4.** Ajouter le paquet lui-même.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> S'arrêter aux dépendances DIRECTES et n'en emporter que trois. Trame et Aiguille en exigent d'autres, qui en exigent encore : la chaîne fait trois niveaux. Sur un poste sans réseau, l'installation s'arrête au premier maillon manquant, et le message ne nomme que celui-là.

### Pièges fréquents

- S'arrêter au premier niveau.
- Compter deux fois un paquet exigé par deux autres.

### Pourquoi ce jeu de données

Le graphe fait trois niveaux de profondeur et comporte un paquet exigé par DEUX autres — Noyau — qu'il ne faut compter qu'une fois. Les réponses fausses plausibles sont 3 (les directes) et 7 (Noyau compté deux fois) : toutes deux distinctes de 6. Les noms sont neutres à dessein — ce qui est évalué est le parcours du graphe, pas la mémoire d'un catalogue.

### Pour aller plus loin

- Faire la même liste pour Cadran, et mesurer ce que les deux installations partagent.
- Repérer les paquets dont plus rien ne dépend.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `PL-05_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `PL-05_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `PL-05.json` | Descripteur pour le plugin Magpie |
| `PL-05_fiche.md` | La présente fiche |
| `PL-05_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `PL-05_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `PL-05_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
