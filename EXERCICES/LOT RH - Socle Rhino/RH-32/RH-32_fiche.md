# RH-32 — Ce qui suivra le calque

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Organisation du document Rhino |
| **Référence au référentiel** | REF-014, REF-015, REF-143 |
| **Compétence visée** | Prévoir quels objets suivront un changement de calque, selon que leur couleur est héritée ou forcée. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | RH-07 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-01 Le tableau des scores |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Prévoir quels objets suivront un changement de calque, selon que leur couleur est héritée ou forcée.

### Contexte

Changer la couleur d'un calque doit changer celle de ses objets. Ceux dont la couleur a été forcée à la main ne bougeront pas, et le plan ressort en deux teintes.

### Énoncé

> L'inventaire donne la couleur de vingt objets : « ParCalque » ou une couleur propre. Le calque va changer de couleur. Donnez le nombre d'objets qui suivront.

### Ce qui vous est fourni

L'inventaire des couleurs des vingt objets.

### Ce qui est attendu

13 objets suivront le calque.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-32_sujet.gh`

### Barème

1 point si le compte est exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-32_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Tester l'égalité de la couleur à « ParCalque ».

**Étape 2.** Compter les vrais.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter les couleurs PROPRES — sept — en croyant répondre à la question. Ce sont justement celles qui ne suivront pas : l'inventaire se lit dans le sens de la question, et les deux comptes se complètent à vingt.

### Pièges fréquents

- Compter les couleurs forcées.
- Confondre la couleur d'affichage et la couleur d'impression.

### Pourquoi ce jeu de données

Vingt objets, treize hérités et sept forcés en quatre couleurs différentes. Ni la majorité écrasante ni la moitié : les deux réponses sont distinctes, et aucune ne se devine.

### Limite de la correction automatique

> La couleur n'est qu'une des propriétés héritées. Type de ligne, épaisseur d'impression et matériau suivent la même logique et peuvent être forcés séparément : un objet peut suivre son calque en couleur et pas en matériau.

### Pour aller plus loin

- Donner le nombre d'objets à repasser en ParCalque.
- Compter les couleurs propres distinctes.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-32_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-32_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-32.json` | Descripteur pour le plugin Magpie |
| `RH-32_fiche.md` | La présente fiche |
| `RH-32_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-32_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-32_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
