# RH-12 — Ce qui dépasse le niveau

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH1 · Interface et navigation Rhino |
| **Référence au référentiel** | REF-002 |
| **Compétence visée** | Compter ce qui franchit un niveau donné, en tranchant explicitement le cas de ce qui s'y trouve exactement. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | RH-11 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-02 Diagnostic éclair |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Compter ce qui franchit un niveau donné, en tranchant explicitement le cas de ce qui s'y trouve exactement.

### Contexte

On cherche ce qui dépasse le niveau du faux plafond, posé à 2 800 mm, pour savoir ce qui devra être repris.

### Énoncé

> Les altitudes des trente objets vous sont fournies. Donnez le nombre d'objets qui dépassent strictement le niveau de 2 800 mm.

### Ce qui vous est fourni

Les trente altitudes, en millimètres, et le niveau du faux plafond.

### Ce qui est attendu

17 objets dépassent strictement 2 800 mm.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-12_sujet.gh`

### Barème

1 point si le compte est juste et strict.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-12_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser le niveau à comparer.

**Étape 2.** Comparer chaque altitude, en choisissant sciemment entre strict et large.

**Étape 3.** Compter.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter 18 en incluant l'objet posé exactement à 2 800. La consigne dit STRICTEMENT, et sur un chantier la différence n'est pas rhétorique : ce qui affleure le plafond passe, ce qui le dépasse se reprend.

### Pièges fréquents

- Prendre « supérieur ou égal » par défaut.
- Compter à l'œil sur une liste où la frontière est peuplée.

### Pourquoi ce jeu de données

Un objet exactement à 2 800, douze autres entre 2 788 et 2 820 : la frontière est peuplée, de sorte qu'un comptage à l'œil se trompe, et que le choix entre strict et large change la réponse d'exactement un.

### Pour aller plus loin

- Donner aussi le compte de ce qui affleure, à 5 mm près.
- Reprendre avec un plafond relevé à 2 850 mm.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-12_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-12_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-12.json` | Descripteur pour le plugin Magpie |
| `RH-12_fiche.md` | La présente fiche |
| `RH-12_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-12_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-12_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
