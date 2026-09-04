# IA-15 — Relire le graphe qu'un agent a construit

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA7 · Agents et protocoles |
| **Référence au référentiel** | REF-137 |
| **Compétence visée** | Confronter le graphe produit par un agent à la spécification qu'on lui avait donnée, et compter ce qui diverge — plutôt que de juger sur l'aperçu. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | IA-12 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-20 Contre-expertise |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Confronter le graphe produit par un agent à la spécification qu'on lui avait donnée, et compter ce qui diverge.

### Contexte

L'agent a construit la définition en trente secondes. L'aperçu montre un volume plausible. C'est précisément le moment où l'on ne vérifie pas.

### Énoncé

> Vous aviez spécifié neuf liaisons, chacune avec son entrée de destination. Le relevé du graphe produit vous est fourni en regard. Donnez le nombre de liaisons qui ne sont pas conformes à la spécification.

### Ce qui vous est fourni

Les neuf liaisons demandées et les neuf liaisons produites, chacune avec l'indice de l'entrée de destination.

### Ce qui est attendu

3 — trois liaisons aboutissent sur une autre entrée que celle demandée.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-15_sujet.gh`

### Barème

1 point si le nombre de divergences est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-15_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Mettre les deux relevés en regard, liaison par liaison.

**Étape 2.** Comparer les indices d'entrée, et non les seuls noms.

**Étape 3.** Compter les désaccords.

**Étape 4.** Ne conclure à la conformité qu'après avoir aussi vérifié qu'aucune liaison ne manque.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter les liaisons manquantes, et n'en trouver aucune : les neuf liaisons existent bien, et le graphe est complet. Ce qui diffère est leur POINT D'ARRIVÉE. Un graphe complet peut être entièrement faux, et il produit alors un résultat — donc un aperçu — parfaitement crédible.

### Pièges fréquents

- Comparer les noms des composants et s'arrêter là.
- Se fier à l'aperçu, qui est plausible.
- Conclure de « neuf liaisons des deux côtés » à « graphe conforme ».

### Pourquoi ce jeu de données

Les trois divergences aboutissent toutes sur l'entrée d'indice 0, et c'est la panne réelle des ponts agentiques : beaucoup d'implémentations ignorent silencieusement l'indice demandé et écrivent sur la première entrée. Le graphe se construit, ne signale rien, et calcule autre chose. Neuf liaisons est un format assez court pour se vérifier à la main, assez long pour qu'on ne le fasse pas.

### Limite de la correction automatique

> L'exercice compte les écarts de câblage. Il ne dit rien des valeurs, des types ni des composants choisis — un graphe conforme au câblage près peut encore être faux. Compter est la première vérification, pas la seule.

### Pour aller plus loin

- Reprendre la spécification et faire corriger l'agent, puis recompter.
- Écrire la vérification comme une étape automatique du pont, exécutée après chaque construction.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-15_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-15_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-15.json` | Descripteur pour le plugin Magpie |
| `IA-15_fiche.md` | La présente fiche |
| `IA-15_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-15_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-15_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
