# PL-16 — Ce qui tourne encore sous Rhino 8

**Fiche d'exercice Magpie** · Lot PL — Écosystème de plugins

| | |
|---|---|
| **Thématique** | PL1 · Écosystème de plugins |
| **Référence au référentiel** | REF-029, REF-038, REF-039 |
| **Compétence visée** | Vérifier la compatibilité d'un parc de plugins avec une version cible, en tenant les DEUX bornes. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 12 min |
| **Prérequis** | PL-09 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-18 Vrai ou faux à élimination |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Vérifier la compatibilité d'un parc de plugins avec une version cible, en tenant les DEUX bornes.

### Contexte

Migrer une salle de formation vers une nouvelle version de Rhino se prépare : un plugin abandonné à la version 7 ne chargera pas, et la définition qui l'emploie s'ouvrira en rouge devant les apprenants.

### Énoncé

> Le tableau donne, pour quatorze plugins, la version de Rhino minimale et la version maximale supportée. Donnez le nombre de plugins compatibles avec Rhino 8.

### Ce qui vous est fourni

Le tableau des quatorze plugins et de leurs deux bornes.

### Ce qui est attendu

10 plugins sur 14 sont compatibles avec Rhino 8.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`PL-16_sujet.gh`

### Barème

1 point si le compte est exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `PL-16_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Tester la borne minimale : au plus 8.

**Étape 2.** Tester la borne maximale : au moins 8.

**Étape 3.** Combiner les deux par un ET.

**Étape 4.** Compter les vrais.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Ne regarder que la version MINIMALE : quatorze sur quatorze, puisque aucun n'exige mieux que Rhino 8. Un intervalle a deux bornes, et ce sont les quatre plugins abandonnés en 6 ou en 7 qui feront échouer la migration.

### Pièges fréquents

- N'appliquer qu'une des deux bornes.
- Employer une comparaison stricte là où la version 8 est elle-même admise.

### Pourquoi ce jeu de données

Quatorze plugins, dont quatre s'arrêtent avant la version 8. La borne minimale ne rejette personne : le test naïf donne donc le score parfait, ce qui est exactement ce qui le rend crédible.

### Limite de la correction automatique

> La compatibilité DÉCLARÉE n'est pas la compatibilité observée. Un plugin annoncé pour Rhino 8 peut échouer sur une fonction précise, et un plugin annoncé pour Rhino 7 fonctionner parfaitement. Le tableau donne une présomption, pas un test.

### Pour aller plus loin

- Refaire le compte pour Rhino 9.
- Donner la liste des plugins qui bloquent la migration.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `PL-16_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `PL-16_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `PL-16.json` | Descripteur pour le plugin Magpie |
| `PL-16_fiche.md` | La présente fiche |
| `PL-16_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `PL-16_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `PL-16_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
