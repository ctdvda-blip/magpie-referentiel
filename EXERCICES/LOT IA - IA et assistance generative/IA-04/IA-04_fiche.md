# IA-04 — Un composant scripté qui somme un métré

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA2 · Composants scriptés assistés |
| **Référence au référentiel** | REF-120, REF-121 |
| **Compétence visée** | Faire produire, installer et brancher un composant scripté qui traite deux listes appariées. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | IA-01 |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Faire produire, installer et brancher un composant scripté qui traite deux listes appariées.

### Contexte

Le calorifugeage d'un réseau de gaines se chiffre à la surface : chaque tronçon développe sa longueur multipliée par le périmètre de sa section.

### Énoncé

> Les longueurs et les diamètres des 16 tronçons vous sont fournis dans deux listes de même rang. Faites produire un composant scripté qui renvoie la surface totale à calorifuger, en mètres carrés.

### Ce qui vous est fourni

Les 16 longueurs en mètres et les 16 diamètres en millimètres, dans deux listes de même rang.

### Ce qui est attendu

Une valeur décimale : la surface développée totale, en mètres carrés.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-04_sujet.gh`

### Barème

1 point si la surface est juste à 0,01 m² près.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-04_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 58,03 m² — la surface développée totale, à 0,01 près.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Spécifier : deux entrées en accès liste, une sortie décimale, et l'unité attendue en sortie.

**Étape 2.** Signaler explicitement que les diamètres sont en millimètres et les longueurs en mètres.

**Étape 3.** Rappeler la formule attendue : périmètre multiplié par longueur, sommé sur tous les tronçons.

**Étape 4.** Installer le code et déclarer les deux entrées en accès liste.

**Étape 5.** Contrôler l'ordre de grandeur avant de valider : quelques dizaines de mètres carrés pour un réseau de cette taille.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Mélanger les unités : les diamètres sont en millimètres et les longueurs en mètres. Un composant qui les multiplie sans conversion donne un résultat mille fois trop grand — assez visible pour être détecté, ce qui est précisément l'intérêt du contexte.

### Pièges fréquents

- Laisser les deux entrées en accès élément : le composant s'exécute 16 fois et la somme n'est jamais faite.
- Oublier de préciser l'unité de sortie et obtenir des millimètres carrés.

### Pourquoi ce jeu de données

Longueurs et diamètres pris dans des séries réelles de gaines circulaires (125 à 400 mm), avec des unités volontairement différentes entre les deux listes : c'est le cas courant en métré, et la spécification doit le dire.

### Pour aller plus loin

- Ajouter une épaisseur d'isolant et demander le volume.
- Refaire le composant dans l'autre langage et comparer les deux sorties.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-04_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-04_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-04.json` | Descripteur pour le plugin Magpie |
| `IA-04_fiche.md` | La présente fiche |
| `IA-04_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-04_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-04_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
