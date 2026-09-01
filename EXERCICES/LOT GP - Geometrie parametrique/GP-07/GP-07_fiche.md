# GP-07 — Ce que la soudure retire

**Fiche d'exercice Magpie** · Lot GP — Géométrie paramétrique appliquée

| | |
|---|---|
| **Thématique** | GP4 · Maillages et SubD |
| **Référence au référentiel** | REF-076 |
| **Compétence visée** | Mesurer la redondance d'un maillage construit face par face, et ce que la soudure des sommets lui retire. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | GP-06 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-16 Livrable pesé |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mesurer la redondance d'un maillage construit face par face, et ce que la soudure des sommets lui retire.

### Contexte

Le maillage a été construit quadrangle par quadrangle. Chaque face porte ses quatre sommets, sans savoir que ses voisines portent les mêmes.

### Énoncé

> La nappe compte 48 divisions par 30, en quadrangles construits un à un. Donnez le nombre de sommets que la soudure supprimera.

### Ce qui vous est fourni

Les deux nombres de divisions, et le mode de construction face par face.

### Ce qui est attendu

4 241 sommets supprimés — de 5 760 à 1 519.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`GP-07_sujet.gh`

### Barème

1 point si le nombre de sommets supprimés est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `GP-07_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Compter les sommets du maillage non soudé : quatre par face.

**Étape 2.** Compter ceux du maillage soudé.

**Étape 3.** Soustraire.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Répondre 1 519, le nombre de sommets APRÈS soudure, au lieu du nombre supprimé. Les deux chiffres racontent la même opération, mais seul le second dit ce que le maillage transportait pour rien : près des trois quarts de ses sommets.

### Pièges fréquents

- Rendre le nombre de sommets restants.
- Compter trois sommets par face, comme pour un triangle.

### Pourquoi ce jeu de données

Quatre sommets par quadrangle non soudé contre 1 519 après soudure : le maillage brut est 3,8 fois plus lourd que nécessaire. C'est l'ordre de grandeur réel d'un maillage produit face par face, et la raison pour laquelle un fichier d'export paraît parfois inexplicablement gros.

### Limite de la correction automatique

> La soudure suppose une tolérance. Trop large, elle referme des arêtes qui devaient rester ouvertes — l'exercice ne traite pas ce réglage.

### Pour aller plus loin

- Chiffrer le gain de poids du fichier exporté.
- Refaire le calcul pour un maillage triangulé.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `GP-07_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `GP-07_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `GP-07.json` | Descripteur pour le plugin Magpie |
| `GP-07_fiche.md` | La présente fiche |
| `GP-07_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `GP-07_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `GP-07_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
