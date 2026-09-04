# RH-31 — Ce qui reste visible

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH1 · Interface et navigation Rhino |
| **Référence au référentiel** | REF-005, REF-006 |
| **Compétence visée** | Distinguer la visibilité d'un objet de celle de son calque, deux mécanismes qui produisent le même symptôme. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | RH-06 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-26 Le retour visuel immédiat |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Distinguer la visibilité d'un objet de celle de son calque, deux mécanismes qui produisent le même symptôme.

### Contexte

Un objet qui n'apparaît pas peut être masqué, ou reposer sur un calque éteint. Le remède n'est pas le même, et « Montrer tout » ne règle que le premier cas.

### Énoncé

> L'inventaire donne, pour dix-huit objets, leur groupe, la visibilité de leur calque et leur propre état de masquage. Donnez le nombre d'objets réellement visibles à l'écran.

### Ce qui vous est fourni

L'inventaire des dix-huit objets et de leurs trois attributs.

### Ce qui est attendu

10 objets sont réellement visibles.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-31_sujet.gh`

### Barème

1 point si le compte est exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-31_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Prendre la colonne de visibilité de calque.

**Étape 2.** Prendre la négation du masquage d'objet.

**Étape 3.** Combiner par un ET, puis compter.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Ne regarder que le masquage d'objet : treize. Trois objets non masqués reposent sur un calque éteint — « Montrer tout » ne les fera pas revenir, et c'est le motif d'appel le plus fréquent en formation.

### Pièges fréquents

- Ne tester qu'un des deux mécanismes.
- Additionner les deux causes en croyant qu'elles s'excluent.

### Pourquoi ce jeu de données

Dix-huit objets, dont cinq masqués individuellement et quatre sur calque éteint, avec un recouvrement d'un objet cumulant les deux. Les deux causes se distinguent donc, et le total ne s'obtient par aucune soustraction simple.

### Limite de la correction automatique

> L'inventaire ignore l'ISOLATION, troisième mécanisme : isoler une sélection masque tout le reste sans toucher aux calques ni aux objets, et se défait par une commande encore différente.

### Pour aller plus loin

- Compter les objets qu'un « Montrer tout » ferait réapparaître.
- Donner le groupe le plus affecté.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-31_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-31_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-31.json` | Descripteur pour le plugin Magpie |
| `RH-31_fiche.md` | La présente fiche |
| `RH-31_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-31_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-31_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
