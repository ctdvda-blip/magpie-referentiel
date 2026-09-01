# QT-03 — Une nomenclature exportable

**Fiche d'exercice Magpie** · Lot QT — Quantitatifs, chiffrage et export

| | |
|---|---|
| **Thématique** | QT2 · Export de données |
| **Référence au référentiel** | REF-085, REF-086, REF-087 |
| **Compétence visée** | Mettre en forme des données de projet en un tableau exportable, colonne par colonne, et le sortir en fichier. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | A-27 |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-16 Enquête documentaire |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mettre en forme des données de projet en un tableau exportable, colonne par colonne, et le sortir en fichier.

### Contexte

Le bureau d'études attend la nomenclature des menuiseries au format tableur, pour la reprendre dans son chiffrage.

### Énoncé

> Les 18 menuiseries vous sont fournies avec leur repère, leur largeur et leur hauteur. Produisez le tableau à quatre colonnes — repère, largeur, hauteur, surface — et exportez-le en CSV. Donnez la surface totale, en mètres carrés.

### Ce qui vous est fourni

Les 18 repères, les 18 largeurs et les 18 hauteurs, en millimètres.

### Ce qui est attendu

La surface totale des menuiseries, en mètres carrés, à 0,01 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0,01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`QT-03_sujet.gh`

### Barème

1 point si la surface totale est juste et si le CSV s'ouvre en quatre colonnes distinctes.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `QT-03_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Calculer la surface de chaque menuiserie, en mètres carrés.

**Étape 2.** Choisir le séparateur : le point-virgule s'impose en contexte francophone, la virgule servant déjà de séparateur décimal.

**Étape 3.** Assembler chaque ligne en joignant les quatre valeurs par ce séparateur.

**Étape 4.** Ajouter la ligne d'en-tête, puis écrire le fichier.

**Étape 5.** Ouvrir le CSV dans un tableur pour vérifier que les colonnes se séparent bien.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Construire le tableau ligne par ligne en concaténant tout dans une seule chaîne. Le fichier s'ouvre, et le tableur voit une seule colonne : c'est le séparateur qui fait les colonnes, et il faut décider lequel avant d'écrire quoi que ce soit.

### Pièges fréquents

- Virgule décimale et virgule séparatrice dans le même fichier : chaque nombre décimal casse une ligne en deux colonnes.
- Oublier l'en-tête : le tableur prend la première menuiserie pour un titre.

### Pourquoi ce jeu de données

Dix-huit menuiseries de dimensions courantes, avec des répétitions : le tableau doit rester lisible et le total vérifiable à la main sur quelques lignes.

### Limite de la correction automatique

> L'écriture du fichier elle-même n'est pas auto-corrigeable : c'est la surface totale qui est validée. Le formateur ouvre le CSV pour juger la mise en forme.

### Pour aller plus loin

- Ajouter une colonne de type d'ouvrant et trier par type.
- Produire aussi un récapitulatif par dimension.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `QT-03_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `QT-03_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `QT-03.json` | Descripteur pour le plugin Magpie |
| `QT-03_fiche.md` | La présente fiche |
| `QT-03_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `QT-03_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `QT-03_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
