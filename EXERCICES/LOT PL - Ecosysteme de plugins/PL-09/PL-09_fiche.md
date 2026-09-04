# PL-09 — Ce qui s'installera vraiment sur ce poste

**Fiche d'exercice Magpie** · Lot PL — Écosystème de plugins

| | |
|---|---|
| **Thématique** | PL1 · Écosystème de plugins |
| **Référence au référentiel** | REF-030 |
| **Compétence visée** | Confronter les exigences de version d'un ensemble de plugins à la version installée, avant de promettre une configuration. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 15 min |
| **Prérequis** | PL-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-06 Valise de chantier |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Confronter les exigences de version d'un ensemble de plugins à la version installée, avant de promettre une configuration.

### Contexte

Le poste tourne sous Rhino 8. La liste des plugins souhaités vient d'ailleurs, et chacun annonce la version qu'il exige.

### Énoncé

> Les neuf plugins vous sont fournis avec la version de Rhino qu'ils exigent au minimum. Le poste tourne sous Rhino 8. Donnez le nombre de plugins installables.

### Ce qui vous est fourni

Les neuf plugins et la version minimale exigée par chacun.

### Ce qui est attendu

7 plugins sur 9 sont installables sur Rhino 8.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`PL-09_sujet.gh`

### Barème

1 point si le compte est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `PL-09_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Comprendre que la version déclarée est un minimum.

**Étape 2.** Comparer chaque exigence à la version du poste.

**Étape 3.** Compter.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Ne retenir que ceux qui annoncent exactement 8 — il y en a trois. Une version minimale est un PLANCHER : un plugin écrit pour Rhino 6 s'installe sur Rhino 8. Ce sont les deux qui exigent Rhino 9 qui ne passeront pas.

### Pièges fréquents

- Chercher l'égalité exacte.
- Supposer qu'un plugin ancien ne fonctionnera pas.

### Pourquoi ce jeu de données

Neuf plugins répartis de Rhino 5 à Rhino 9, dont trois exactement à 8 : la lecture « exactement » donne 3, la lecture « au moins » donne 7, et la lecture « tous sauf le plus récent » donne 8. Trois réponses distinctes pour trois façons de se tromper.

### Limite de la correction automatique

> Une version minimale ne garantit pas la compatibilité vers le haut : un plugin écrit pour Rhino 6 peut ne plus fonctionner sous Rhino 8. L'exercice traite ce que le catalogue déclare, pas ce que l'exécution révèle.

### Pour aller plus loin

- Trouver la version de Rhino qui permettrait d'installer les neuf.
- Croiser avec les dépendances de PL-05.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `PL-09_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `PL-09_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `PL-09.json` | Descripteur pour le plugin Magpie |
| `PL-09_fiche.md` | La présente fiche |
| `PL-09_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `PL-09_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `PL-09_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
