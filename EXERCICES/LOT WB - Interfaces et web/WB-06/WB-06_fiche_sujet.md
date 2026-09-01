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
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
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

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
