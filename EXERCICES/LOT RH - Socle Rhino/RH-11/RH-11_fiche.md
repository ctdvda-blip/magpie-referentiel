# RH-11 — Ce que le zoom étendue vous apprend

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH1 · Interface et navigation Rhino |
| **Référence au référentiel** | REF-001, REF-002, REF-003 |
| **Compétence visée** | Diagnostiquer l'étendue réelle d'un fichier au lieu de juger sur ce que l'écran montre. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | RH-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-02 Diagnostic éclair |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Diagnostiquer l'étendue réelle d'un fichier au lieu de juger sur ce que l'écran montre.

### Contexte

Le fichier arrive du géomètre. Un zoom étendue et l'on ne voit plus rien : le bâtiment est devenu un point.

### Énoncé

> Le fichier contient cinquante objets, dont les coordonnées vous sont fournies. Donnez l'étendue du fichier selon X, en mètres.

### Ce qui vous est fourni

Les coordonnées en plan des cinquante objets, en millimètres.

### Ce qui est attendu

6 050 m — l'étendue selon X de tout ce que le fichier contient.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-11_sujet.gh`

### Barème

1 point si l'étendue est juste, en mètres.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-11_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Extraire l'abscisse de chaque objet.

**Étape 2.** En prendre les bornes.

**Étape 3.** Soustraire, puis convertir en mètres.

**Étape 4.** Comparer à l'étendue de ce que l'on croyait voir.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Répondre 8,4 m, l'étendue du bâtiment. C'est ce que l'on VOIT une fois zoomé dessus, et c'est précisément ce que le zoom étendue ne montre pas : deux objets égarés à 4,8 km et à 1,2 km étirent la vue sur six kilomètres, et le bâtiment n'occupe plus qu'un cinq-centième de l'écran.

### Pièges fréquents

- Juger sur l'écran.
- Ne regarder que les objets sélectionnés.
- Confondre étendue et distance à l'origine.

### Pourquoi ce jeu de données

Quarante-huit objets tiennent dans 8,4 m ; deux sont à des kilomètres, l'un dans chaque sens. Le rapport entre l'étendue vue (8,4 m) et l'étendue réelle (6 050 m) vaut 720 : aucune confusion possible entre les deux réponses, et le chiffre dit à lui seul pourquoi l'écran est vide.

### Limite de la correction automatique

> L'exercice mesure l'étendue. Il ne dit pas quoi faire ensuite — supprimer les égarés, ou comprendre d'où ils viennent, ce qui est souvent plus utile.

### Pour aller plus loin

- Donner aussi l'étendue en Y et en Z.
- Trouver les deux objets égarés et dire de quel calque ils viennent.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-11_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-11_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-11.json` | Descripteur pour le plugin Magpie |
| `RH-11_fiche.md` | La présente fiche |
| `RH-11_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-11_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-11_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
