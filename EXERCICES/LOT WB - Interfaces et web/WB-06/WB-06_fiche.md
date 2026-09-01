# WB-06 — Le poids du modèle que l'on télécharge

**Fiche d'exercice Magpie** · Lot WB — Interfaces, web et interopérabilité

| | |
|---|---|
| **Thématique** | WB2 · Publication web |
| **Référence au référentiel** | REF-109 |
| **Compétence visée** | Prévoir le poids d'un fichier d'échange à partir de la structure du maillage exporté, avant de le proposer au téléchargement. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | WB-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-16 Livrable pesé |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Prévoir le poids d'un fichier d'échange à partir de la structure du maillage exporté, avant de le proposer au téléchargement.

### Contexte

Le configurateur propose le téléchargement du modèle. Le fichier part souvent sur une connexion mobile : son poids se prévoit avant de le produire, pas après.

### Énoncé

> Le maillage d'aperçu compte 24 310 faces quadrangulaires. Vous l'exportez dans un format binaire qui ne stocke que des triangles, avec un en-tête de 84 octets et 50 octets par facette. Donnez le poids du fichier, en octets.

### Ce qui vous est fourni

Le nombre de faces du maillage, leur nature, et la structure du format d'export.

### Ce qui est attendu

2 431 084 octets — soit 2,32 Mio.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`WB-06_sujet.gh`

### Barème

1 point si le poids en octets est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `WB-06_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Convertir les faces quadrangulaires en triangles.

**Étape 2.** Multiplier par le poids d'une facette.

**Étape 3.** Ajouter l'en-tête.

**Étape 4.** Convertir en mébioctets pour l'annoncer à l'utilisateur.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter 50 octets par face du maillage : 1 215 584 octets, la moitié. Le format ne connaît que le TRIANGLE ; un maillage quadrangulaire est triangulé à l'export, et chaque quadrangle devient deux facettes. L'erreur ne se voit pas au calcul — elle se voit quand le fichier arrive deux fois plus lourd que promis à l'utilisateur.

### Pièges fréquents

- Compter une facette par face du maillage.
- Oublier l'en-tête.
- Confondre mébioctet et mégaoctet en annonçant le poids.

### Pourquoi ce jeu de données

24 310 quadrangles est l'ordre de grandeur d'un aperçu de meuble correctement maillé. Les deux réponses possibles sont dans un rapport de deux exactement, ce qui rend l'erreur immédiatement identifiable ; et l'en-tête de 84 octets est assez petit pour qu'on l'oublie sans que le résultat change d'ordre de grandeur — donc assez discret pour départager une réponse construite d'une réponse approchée.

### Limite de la correction automatique

> Ce format ne porte ni matière, ni couleur, ni unité. Le poids n'est qu'un critère : la fiche invite à le comparer au 3DM et au glTF, qui portent davantage pour un poids voisin.

### Pour aller plus loin

- Refaire le calcul pour la variante texte du même format et mesurer le rapport.
- Réduire le maillage de moitié et juger ce que l'aperçu y perd.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `WB-06_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `WB-06_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `WB-06.json` | Descripteur pour le plugin Magpie |
| `WB-06_fiche.md` | La présente fiche |
| `WB-06_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `WB-06_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `WB-06_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
