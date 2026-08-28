# GP-02 — Un modèle paramétrique de bout en bout

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP2 · Synthèse géométrie |
| **Référence au référentiel** | REF-073 |
| **Compétence visée** | Enchaîner tracé, surface et volume dans une définition unique dont un seul paramètre commande l'ensemble. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 45 min |
| **Prérequis** | GP-01, A-41 |
| **Mode de validation** | NumericTolerance — tolérance 0,001 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-25 Projet jalonné |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Enchaîner tracé, surface et volume dans une définition unique dont un seul paramètre commande l'ensemble.

### Contexte

Un escalier droit doit être chiffré en volume de béton avant que sa hauteur d'étage soit figée.

### Énoncé

> L'escalier fait 1 100 mm de large, avec un giron de 280 mm et une paillasse de 150 mm d'épaisseur. Pour une hauteur d'étage de 2 700 mm et des marches de 175 mm, produisez le volume de béton, en mètres cubes.

### Ce qui vous est fourni

Trois valeurs réglables : hauteur d'étage, hauteur de marche visée et giron.

### Ce qui est attendu

Le volume de béton, en mètres cubes, à 0,001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-02_sujet.gh`

### Barème

Grille : nombre de marches juste (1), hauteur réelle recalculée (1), volume juste (2).

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `GP-02_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Établir le nombre de contremarches : hauteur d'étage divisée par la hauteur visée, arrondi à l'entier le plus proche.

**Étape 2.** En déduire la hauteur de marche réelle : hauteur d'étage divisée par ce nombre entier.

**Étape 3.** Répartir les marches par une suite régulière.

**Étape 4.** Construire la paillasse et les marches, les réunir en un solide unique.

**Étape 5.** Mesurer le volume et convertir en mètres cubes.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Prendre 2 700 ÷ 175 = 15,43 marches et arrondir au plus proche. Un escalier a un nombre entier de contremarches, et c'est la hauteur de marche qui s'ajuste, pas la hauteur d'étage. Arrondir la marche au lieu du compte donne un escalier qui n'arrive pas au niveau.

### Pièges fréquents

- Réunir les volumes sans booléenne : les recouvrements sont comptés deux fois.
- Oublier que la dernière contremarche arrive au niveau fini, et poser une marche de trop.

### Pourquoi ce jeu de données

2 700 n'est pas divisible par 175 : c'est le cas normal, et c'est ce qui oblige à comprendre lequel des deux nombres est la donnée et lequel est le résultat.

### Pour aller plus loin

- Faire varier la hauteur d'étage et vérifier que le nombre de marches se recale seul.
- Ajouter un palier intermédiaire et reprendre le calcul.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `GP-02_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `GP-02_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `GP-02.json` | Descripteur pour le plugin Magpie |
| `GP-02_fiche.md` | La présente fiche |
| `GP-02_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `GP-02_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `GP-02_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
