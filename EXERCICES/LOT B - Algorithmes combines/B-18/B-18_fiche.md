# B-18 — Filetage hélicoïdal paramétrique

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B5 · Design produit |
| **Référence au référentiel** | REF-069, REF-103 |
| **Compétence visée** | Retrouver une cote fonctionnelle à partir d'une norme, plutôt que de la mesurer sur un modèle. |
| **Case Bloom (révisée)** | Appliquer × conceptuelle |
| **Niveau** | Intermédiaire |
| **Durée cible** | 28 min |
| **Prérequis** | A-42 |
| **Mode de validation** | NumericTolerance — tolérance 0.001 |
| **Solution de référence** | 22 composants |
| **Gamification associée** | G-32 Indices payants |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Construire une hélice et balayer un profil normalisé le long de celle-ci.

### Contexte

Le diamètre à fond de filet décide de la section résistante de la vis. Il ne se lit pas sur la désignation.

### Énoncé

> Modélise une vis M10 au pas de 1,5 mm sur 30 mm de longueur filetée, profil triangulaire à 60°, et vérifie que le diamètre à fond de filet correspond bien à la valeur normalisée de 8,376 mm.

### Ce qui vous est fourni

Trois sliders : diamètre nominal, pas, longueur filetée.

### Ce qui est attendu

8,16 mm — le diamètre à fond de filet, à 0,001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-18_sujet.gh`

### Barème

2 points pour le filetage, 2 points pour la vérification dimensionnelle.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-18_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Construire l'hélice avec le composant Helix : rayon 5, pas 1,5, nombre de tours = 30 / 1,5 = 20.

**Étape 2.** Construire le profil triangulaire du filet ISO dans un plan perpendiculaire au départ de l'hélice.

**Étape 3.** Poser Sweep 1 avec l'hélice comme rail et le profil comme section.

**Étape 4.** Construire le cylindre nominal de diamètre 10.

**Étape 5.** Soustraire le balayage du cylindre avec Solid Difference.

**Étape 6.** Couper le résultat par un plan passant par l'axe et mesurer le diamètre à fond de filet.

**Étape 7.** Comparer à 8,376 mm avec Similarity et afficher CONFORME ou NON CONFORME.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Retrancher le pas au diamètre nominal : 8,50 mm. Le profil ISO retire 1,2269 fois le pas, pas une fois — le filet est triangulaire à 60° et tronqué. L'erreur surestime la section résistante de 8 %, ce qui se traduit par une vis qu'on croit plus solide qu'elle n'est.

### Pièges fréquents

- Nombre de tours calculé à partir de la longueur totale et non de la longueur filetée.
- Profil non perpendiculaire à l'hélice : le filet se vrille.
- Confondre le pas et le pas hélicoïdal sur un filetage multiple.

### Pourquoi ce jeu de données

M10 au pas de 1,5 : les trois lectures possibles donnent 8,16 (juste), 8,50 (pas retranché une fois) et 7,40 (deux fois la hauteur théorique du triangle non tronqué). Trois valeurs distinctes, dont deux plausibles.

### Limite de la correction automatique

> Le diamètre à fond de filet n'est pas le diamètre de la section résistante, qui se calcule sur une moyenne avec le diamètre sur flancs. L'exercice s'arrête au premier.

### Pour aller plus loin

- Modéliser l'écrou correspondant et vérifier le jeu.
- Paramétrer pour toute la série métrique M3 à M20.
- Ajouter un chanfrein d'entrée.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-18_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-18_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-18.json` | Descripteur pour le plugin Magpie |
| `B-18_fiche.md` | La présente fiche |
| `B-18_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-18_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-18_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
