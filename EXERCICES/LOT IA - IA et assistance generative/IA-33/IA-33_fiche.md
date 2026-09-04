# IA-33 — Du texte aux paramètres

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA5 · Modèles de langage et IA générative |
| **Référence au référentiel** | REF-134 |
| **Compétence visée** | Tirer d'un texte de programme les paramètres qui pilotent une définition, en distinguant ce qui est donné de ce qui se déduit. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 18 min |
| **Prérequis** | IA-11 |
| **Mode de validation** | NumericTolerance — tolérance 0.0001 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-19 Le composant mystère |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Tirer d'un texte de programme les paramètres qui pilotent une définition, en distinguant ce qui est donné de ce qui se déduit.

### Contexte

Un cahier des charges décrit une verrière en toutes lettres. La définition, elle, a besoin d'une largeur de travée et d'une hauteur vitrée, qu'aucune phrase ne donne directement.

### Énoncé

> L'extrait décrit une verrière de 3 200 mm de large et 2 450 mm de haut, à 6 travées égales séparées par des montants de 60 mm, avec une imposte de 380 mm en partie haute. Donnez la largeur d'une travée puis la hauteur vitrée, en millimètres.

### Ce qui vous est fourni

L'extrait de programme, en toutes lettres.

### Ce qui est attendu

483,3333 mm de largeur de travée, puis 2 070 mm de hauteur vitrée.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-33_sujet.gh`

### Barème

1 point si les deux valeurs sont justes à 0,0001 mm.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-33_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Compter les montants : un de moins que les travées.

**Étape 2.** Retrancher leur largeur cumulée à la largeur totale.

**Étape 3.** Diviser par le nombre de travées.

**Étape 4.** Retrancher l'imposte à la hauteur totale.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Diviser la largeur par le nombre de travées : 533,33 mm. Les cinq montants intérieurs occupent 300 mm qu'aucune travée ne reçoit — la verrière posée sur ce chiffre déborde de 300 mm, et l'erreur ne se voit qu'au montage.

### Pièges fréquents

- Compter autant de montants que de travées.
- Diviser avant de retrancher.

### Pourquoi ce jeu de données

Six travées et cinq montants : c'est l'écart d'une unité qui fait tout le piège, et il est le même que celui des barreaux de garde-corps en B-02. La largeur obtenue n'est pas ronde, ce qui interdit de la deviner.

### Limite de la correction automatique

> Les deux paramètres se déduisent du TEXTE. Ils ne disent pas si la verrière est constructible : une travée de 483 mm en simple vitrage tient, en double vitrage sur 2 070 mm de haut elle demande un calcul de raidissement que le texte ignore.

### Pour aller plus loin

- Refaire le calcul pour sept travées.
- Chercher le nombre de travées qui donne une largeur ronde.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-33_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-33_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-33.json` | Descripteur pour le plugin Magpie |
| `IA-33_fiche.md` | La présente fiche |
| `IA-33_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-33_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-33_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
