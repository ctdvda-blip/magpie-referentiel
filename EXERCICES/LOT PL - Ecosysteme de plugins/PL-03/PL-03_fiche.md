# PL-03 — Les plugins qui ne servent qu'à travailler mieux

**Fiche d'exercice Magpie** · Lot PL — Écosystème de plugins

| | |
|---|---|
| **Thématique** | PL3 · Plugins d'ergonomie |
| **Référence au référentiel** | REF-031, REF-032, REF-033, REF-034, REF-035, REF-036, REF-037 |
| **Compétence visée** | Installer et régler les plugins d'ergonomie, et juger lesquels valent la place qu'ils prennent. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | PL-02 |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-18 Duel de versions |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Installer et régler les plugins d'ergonomie, et juger lesquels valent la place qu'ils prennent.

### Contexte

Une définition d'équipe se relit à plusieurs : ce qui la rend lisible fait gagner plus de temps que ce qui la rend puissante.

### Énoncé

> Installez les plugins d'ergonomie proposés, réglez-les, puis reprenez une définition existante et dites, pour chacun, ce qu'il vous a réellement fait gagner. Concluez par les deux que vous garderiez et les raisons.

### Ce qui vous est fourni

Une définition d'exercice déjà produite, à relire, et l'accès au gestionnaire de paquets.

### Ce qui est attendu

Une définition relue, les plugins réglés, et un jugement motivé sur chacun.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **Visuel**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`PL-03_sujet.gh`

### Barème

Grille : plugins installés et réglés (2), jugement motivé sur chacun (2), définition lisible sans eux (1).

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `PL-03_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Installer les plugins un par un, en relançant Rhino entre chacun : installer en bloc empêche de savoir lequel fait quoi.

**Étape 2.** Reprendre la même définition après chaque installation.

**Étape 3.** Noter ce que le plugin change concrètement : temps gagné, erreur évitée, lisibilité.

**Étape 4.** Désactiver ceux qui n'ont rien apporté.

**Étape 5.** Vérifier que la définition reste lisible pour un collègue qui n'a aucun de ces plugins.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Tout installer et tout garder. Chaque plugin d'ergonomie ajoute un affichage, un raccourci ou une couleur ; empilés sans choix, ils encombrent l'écran plus qu'ils n'aident, et la définition devient illisible pour qui ne les a pas.

### Pièges fréquents

- Confondre confort personnel et lisibilité partagée : une couleur qui vous parle n'existe pas chez le voisin.
- Dépendre d'un plugin d'ergonomie pour comprendre sa propre définition : elle devient intransmissible.

### Pourquoi ce jeu de données

—

### Limite de la correction automatique

> Le livrable est un jugement argumenté, pas un nombre : la validation est visuelle. Ramener cet exercice à une valeur chiffrée n'aurait aucun sens.

### Pour aller plus loin

- Faire relire votre définition par quelqu'un qui n'a aucun plugin installé.
- Chronométrer la même reprise avec et sans.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `PL-03_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `PL-03_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `PL-03.json` | Descripteur pour le plugin Magpie |
| `PL-03_fiche.md` | La présente fiche |
| `PL-03_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `PL-03_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `PL-03_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
