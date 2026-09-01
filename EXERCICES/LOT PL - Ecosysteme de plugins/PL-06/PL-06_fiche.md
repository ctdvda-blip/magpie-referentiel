# PL-06 — Qui pourra ouvrir votre définition

**Fiche d'exercice Magpie** · Lot PL — Écosystème de plugins

| | |
|---|---|
| **Thématique** | PL1 · Écosystème de plugins |
| **Référence au référentiel** | REF-038, REF-039 |
| **Compétence visée** | Mesurer ce qu'une dépendance à des plugins coûte en portabilité, avant de livrer. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | PL-05 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-17 Passation |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mesurer ce qu'une dépendance à des plugins coûte en portabilité, avant de livrer.

### Contexte

La définition part chez sept destinataires. Chez ceux qui n'ont pas les plugins, elle s'ouvrira — avec des composants rouges à la place du calcul.

### Énoncé

> Votre définition exige trois plugins. L'inventaire des sept postes destinataires vous est fourni. Donnez le nombre de postes qui pourront l'exécuter.

### Ce qui vous est fourni

Les trois plugins requis, et pour chacun des sept postes la liste de ceux qu'il possède.

### Ce qui est attendu

3 postes sur 7 pourront l'exécuter.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`PL-06_sujet.gh`

### Barème

1 point si le compte des postes capables est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `PL-06_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Pour chaque poste, vérifier la présence des TROIS plugins.

**Étape 2.** Ne retenir que ceux qui les ont tous.

**Étape 3.** Compter.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter les postes qui possèdent AU MOINS UN des trois plugins : six sur sept, et la livraison paraît sans risque. Il les faut TOUS LES TROIS — un composant manquant suffit à rompre la chaîne, et la définition ne rend alors rien.

### Pièges fréquents

- Se contenter d'une intersection non vide.
- Oublier qu'un plugin en trop ne compense pas un plugin manquant.

### Pourquoi ce jeu de données

Sept postes, dont un qui n'a rien, un qui a tout et plus, et quatre qui ont une partie : la différence entre « au moins un » (6) et « tous » (3) est du simple au double, et c'est exactement l'écart entre l'impression que la livraison passera et la réalité.

### Limite de la correction automatique

> Le compte suppose que posséder le plugin suffit. Une version incompatible se compte comme une absence — c'est l'objet de PL-09.

### Pour aller plus loin

- Trouver le plugin dont l'abandon rendrait la définition portable au plus grand nombre.
- Chiffrer ce que coûterait de refaire en natif la part dépendante.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `PL-06_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `PL-06_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `PL-06.json` | Descripteur pour le plugin Magpie |
| `PL-06_fiche.md` | La présente fiche |
| `PL-06_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `PL-06_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `PL-06_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
