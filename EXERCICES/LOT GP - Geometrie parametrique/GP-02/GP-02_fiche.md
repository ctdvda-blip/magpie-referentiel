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
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Enchaîner tracé, surface et volume dans une définition unique dont un seul paramètre commande l'ensemble.

### Contexte

Un escalier droit doit être chiffré en volume de béton avant que sa hauteur d'étage soit figée.

### Énoncé

> L'escalier est massif, 1 100 mm de large, giron de 280 mm. Pour une hauteur d'étage de 2 700 mm et une hauteur de marche visée de 175 mm, produisez le volume de béton, en mètres cubes.

### Ce qui vous est fourni

Trois valeurs réglables : hauteur d'étage, hauteur de marche visée et giron.

### Ce qui est attendu

6,653 m³ — le volume de béton de l'escalier massif, à 0,001 près.

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

**Étape 4.** Chaque marche est un bloc de giron × largeur × sa hauteur cumulée : la première monte d'une hauteur, la quinzième de quinze.

**Étape 5.** Mesurer le volume et convertir en mètres cubes.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Garder 175 mm comme hauteur de marche réelle. 2 700 ÷ 175 vaut 15,43 : le nombre de contremarches s'arrondit à 15, et c'est alors la HAUTEUR qui se recale, à 180 mm. Conserver 175 mm donne un escalier de 2 625 mm qui n'atteint pas l'étage — de trois quarts de marche.

### Pièges fréquents

- Prendre la hauteur de marche comme hauteur de chaque bloc : on obtient le volume d'une seule assise, pas de l'escalier.
- Oublier que la dernière contremarche arrive au niveau fini, et poser une marche de trop.

### Pourquoi ce jeu de données

2 700 n'est pas divisible par 175 : c'est le cas normal, et c'est ce qui oblige à comprendre lequel des deux nombres est la donnée et lequel est le résultat.

### Limite de la correction automatique

> 6,653 m³ est le volume GÉOMÉTRIQUE de l'escalier massif. Le béton réellement commandé s'y ajoute des pertes de coffrage et de reprise — de 3 à 8 % selon l'ouvrage — que ce modèle n'anticipe pas.

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
