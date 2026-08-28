# FA-02 — Le développé d'une virole

**Fiche d'exercice Magpie** · Lot FA — Aide à la fabrication

| | |
|---|---|
| **Thématique** | FA2 · Déroulé et mise à plat |
| **Référence au référentiel** | REF-115, REF-116 |
| **Compétence visée** | Établir le développé à plat d'une surface réglée et le contrôler par un calcul indépendant. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | A-42 |
| **Mode de validation** | NumericTolerance — tolérance 0,0001 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir le développé à plat d'une surface réglée et le contrôler par un calcul indépendant.

### Contexte

Une virole conique de ventilation se découpe à plat dans la tôle avant d'être roulée.

### Énoncé

> La virole relie un diamètre de 360 mm à un diamètre de 190 mm sur une hauteur de 340 mm. Produisez son développé à plat et donnez la surface développée, en mètres carrés.

### Ce qui vous est fourni

Les deux rayons et la hauteur, en valeurs réglables.

### Ce qui est attendu

La surface développée, en mètres carrés, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`FA-02_sujet.gh`

### Barème

1 point si la surface développée est juste et si le contrôle par le calcul est fourni.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `FA-02_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Construire la virole comme surface réglée entre les deux cercles.

**Étape 2.** La dérouler à plat.

**Étape 3.** Mesurer l'aire du développé.

**Étape 4.** Contrôler par le calcul : π multiplié par la somme des rayons, multiplié par la génératrice — et non par la hauteur.

**Étape 5.** Comparer les deux valeurs : elles doivent coïncider.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Prendre la hauteur pour l'apothème. La génératrice d'un cône tronqué vaut la racine de la hauteur au carré plus l'écart des rayons au carré : ici 340 contre 348 mm. L'écart est de 2 %, assez petit pour passer inaperçu et assez grand pour que la virole ne se referme pas.

### Pièges fréquents

- Confondre hauteur et génératrice.
- Dérouler une surface non développable : un cône l'est, une double courbure ne l'est pas, et le résultat serait une approximation silencieuse.

### Pourquoi ce jeu de données

L'écart des rayons, 85 mm pour 340 de hauteur, place la génératrice juste assez loin de la hauteur pour que la confusion soit détectable au dixième de millimètre carré, sans être grossière.

### Pour aller plus loin

- Ajouter un recouvrement de 15 mm pour la soudure.
- Passer à une virole excentrée et constater qu'elle ne se déroule plus exactement.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `FA-02_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `FA-02_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `FA-02.json` | Descripteur pour le plugin Magpie |
| `FA-02_fiche.md` | La présente fiche |
| `FA-02_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `FA-02_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `FA-02_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
