# B-12 — Nomenclature automatique et export CSV

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B4 · Données, métrés et livrables |
| **Référence au référentiel** | REF-082, REF-083, REF-085, REF-087 |
| **Compétence visée** | Produire un livrable d'échange dont on connaît la structure avant de l'ouvrir. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-27, A-47 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 24 composants |
| **Gamification associée** | G-01 Score visible |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Transformer un modèle en tableau de données exploitable.

### Contexte

La nomenclature part au bureau des méthodes, qui l'importe automatiquement. Un fichier mal structuré n'est pas rejeté : il est importé de travers.

### Énoncé

> À partir du modèle fourni, produis une nomenclature triée par volume décroissant comportant, pour chaque pièce, le repère, le volume en dm³, la surface en dm² et la masse en kg pour une densité de 700 kg/m³. Exporte le tableau au format CSV.

### Ce qui vous est fourni

Un assemblage de 14 solides internalisés.

### Ce qui est attendu

15 lignes — quatorze pièces, plus l'en-tête.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-12_sujet.gh`

### Barème

2 points pour les calculs, 1 point pour le tri, 1 point pour le format du fichier.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-12_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Mesurer Volume et Area de chaque solide.

**Étape 2.** Convertir les unités : mm³ vers dm³ (division par 1 000 000), mm² vers dm² (division par 10 000).

**Étape 3.** Calculer la masse : volume en m³ multiplié par 700.

**Étape 4.** Générer les repères avec Series et Format (masque PCE-{0:000}).

**Étape 5.** Trier l'ensemble par volume décroissant avec Sort List puis Reverse List, en propageant toutes les listes.

**Étape 6.** Formater chaque valeur à deux décimales avec Format.

**Étape 7.** Assembler chaque ligne avec Concatenate et le séparateur point-virgule.

**Étape 8.** Ajouter la ligne d'en-tête avec Merge, puis écrire le fichier avec Write File.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Oublier la ligne d'en-tête : la première pièce est alors lue comme un nom de colonne et disparaît de la nomenclature, sans message.

### Pièges fréquents

- Trier une seule liste et pas les autres : les données se désynchronisent.
- Séparateur décimal virgule et séparateur de colonne virgule : le CSV devient illisible.
- Oublier l'en-tête ou le placer après le tri.

### Pourquoi ce jeu de données

Quatorze pièces : les trois réponses possibles — 14, 15 et le nombre de lignes du modèle source — sont distinctes. C'est le même contrôle que QT-05, appliqué à un assemblage plutôt qu'à un débit : la répétition espacée est intentionnelle.

### Pour aller plus loin

- Ajouter une colonne matériau lue depuis les calques Rhino.
- Grouper les pièces identiques et compter les occurrences.
- Exporter vers Excel plutôt que CSV.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-12_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-12_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-12.json` | Descripteur pour le plugin Magpie |
| `B-12_fiche.md` | La présente fiche |
| `B-12_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-12_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-12_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
