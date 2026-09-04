# PL-13 — Où trouver chaque plugin

**Fiche d'exercice Magpie** · Lot PL — Écosystème de plugins

| | |
|---|---|
| **Thématique** | PL2 · Installation de plugins |
| **Référence au référentiel** | REF-029, REF-030 |
| **Compétence visée** | Distinguer les deux canaux de distribution d'un plugin, et savoir lesquels imposent une installation manuelle. |
| **Case Bloom (révisée)** | Analyser × factuelle |
| **Niveau** | Intermédiaire |
| **Durée cible** | 12 min |
| **Prérequis** | PL-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-06 Le déblocage progressif |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Distinguer les deux canaux de distribution d'un plugin, et savoir lesquels imposent une installation manuelle.

### Contexte

Préparer un poste de formation, c'est savoir ce qui s'installe en une commande et ce qui demande un téléchargement, un déblocage de fichier et un redémarrage.

### Énoncé

> Le tableau vous donne, pour quatorze plugins, leur présence sur le gestionnaire de paquets et sur Food4Rhino. Donnez le nombre de plugins qui ne sont disponibles QUE sur Food4Rhino.

### Ce qui vous est fourni

Le tableau des quatorze plugins et de leurs deux canaux.

### Ce qui est attendu

6 plugins ne sont disponibles que sur Food4Rhino.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`PL-13_sujet.gh`

### Barème

1 point si le compte est exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `PL-13_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Isoler la colonne « présent sur le gestionnaire ».

**Étape 2.** En prendre la négation.

**Étape 3.** La croiser par un ET avec la colonne Food4Rhino.

**Étape 4.** Compter les vrais.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter les plugins PRÉSENTS sur Food4Rhino — treize sur quatorze. La question porte sur l'exclusivité : ce sont les six absents du gestionnaire qui imposeront un téléchargement, un déblocage du fichier et un redémarrage sur chaque poste.

### Pièges fréquents

- Compter la colonne Food4Rhino seule.
- Oublier la négation et compter les plugins présents partout.

### Pourquoi ce jeu de données

Treize plugins sur quatorze sont sur Food4Rhino et huit sur le gestionnaire : les deux comptes sont proches, et seul le croisement donne six. Un seul plugin — Kangaroo — n'est que sur le gestionnaire, ce qui empêche de raisonner par symétrie.

### Limite de la correction automatique

> Le tableau décrit une situation DATÉE. Les canaux changent : un plugin publié sur le gestionnaire six mois plus tard fait tomber le compte, et c'est pourquoi une liste d'installation se revérifie à chaque session de formation.

### Pour aller plus loin

- Compter ceux qui ne sont sur aucun des deux canaux.
- Donner la liste des noms plutôt que le compte.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `PL-13_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `PL-13_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `PL-13.json` | Descripteur pour le plugin Magpie |
| `PL-13_fiche.md` | La présente fiche |
| `PL-13_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `PL-13_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `PL-13_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
