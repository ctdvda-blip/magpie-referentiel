# PL-14 — Ce que l'ergonomie coûte au démarrage

**Fiche d'exercice Magpie** · Lot PL — Écosystème de plugins

| | |
|---|---|
| **Thématique** | PL3 · Plugins d'ergonomie |
| **Référence au référentiel** | REF-031, REF-032, REF-033, REF-034, REF-035, REF-036, REF-037 |
| **Compétence visée** | Chiffrer le coût d'une panoplie d'ergonomie sans compter deux fois ce qui est déjà installé. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 14 min |
| **Prérequis** | PL-06 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-05 La collection de badges |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Chiffrer le coût d'une panoplie d'ergonomie sans compter deux fois ce qui est déjà installé.

### Contexte

Chaque plugin allonge le démarrage de Rhino. Sur un poste de formation ouvert et fermé dix fois par jour, la panoplie d'ergonomie se paie en secondes d'attente.

### Énoncé

> Le relevé donne le temps de chargement de sept plugins, et signale ceux qu'un autre plugin déjà installé exige de toute façon. Donnez le temps AJOUTÉ par la panoplie d'ergonomie, en millisecondes.

### Ce qui vous est fourni

Le relevé des sept temps de chargement, et la colonne des dépendances déjà satisfaites.

### Ce qui est attendu

1 220 ms ajoutés au démarrage.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`PL-14_sujet.gh`

### Barème

1 point si le total est exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `PL-14_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Isoler la colonne des dépendances déjà satisfaites.

**Étape 2.** En prendre la négation.

**Étape 3.** Écarter les temps correspondants.

**Étape 4.** Sommer ce qui reste.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Tout additionner, Metahopper compris : 1 395 ms. Metahopper est déjà exigé par un plugin fonctionnel installé sur le poste — son chargement n'est pas imputable à l'ergonomie, et le compter revient à facturer deux fois la même seconde.

### Pièges fréquents

- Sommer les sept temps sans filtrer.
- Écarter les mauvais, en oubliant la négation.

### Pourquoi ce jeu de données

Sept plugins de 95 à 380 ms. L'écart entre les deux réponses est de 175 ms, soit 14 % : assez pour fausser une décision d'équipement, trop peu pour sauter aux yeux.

### Limite de la correction automatique

> Les temps sont des MESURES sur un poste. Ils dépendent du disque, de la version de Rhino et de ce qui est déjà chargé — le classement des plugins entre eux est stable, les valeurs absolues non.

### Pour aller plus loin

- Chiffrer le coût sur dix démarrages quotidiens.
- Chercher le plugin dont le retrait gagne le plus.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `PL-14_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `PL-14_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `PL-14.json` | Descripteur pour le plugin Magpie |
| `PL-14_fiche.md` | La présente fiche |
| `PL-14_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `PL-14_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `PL-14_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
