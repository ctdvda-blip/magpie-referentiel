# RH-19 — Ce que la mise à l'échelle fait aux détails

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH3 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-017, REF-018 |
| **Compétence visée** | Juger la finesse d'un modèle À L'ÉCHELLE OÙ IL SERA IMPRIMÉ, et non à celle où il a été dessiné. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 25 min |
| **Prérequis** | RH-07 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Juger la finesse d'un modèle à l'échelle où il sera imprimé, et non à celle où il a été dessiné.

### Contexte

La maquette d'étude est dessinée au 1:25 et sera imprimée à l'échelle 1. La machine ne distingue rien sous 0,4 mm.

### Énoncé

> Les douze détails les plus fins du modèle vous sont fournis, mesurés sur la maquette. Le modèle sera agrandi 25 fois. Donnez le nombre de détails qui resteront sous la résolution de 0,4 mm APRÈS agrandissement.

### Ce qui vous est fourni

Les douze dimensions relevées sur la maquette, le facteur d'agrandissement et la résolution de la machine.

### Ce qui est attendu

6 détails restent sous la résolution après agrandissement.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-19_sujet.gh`

### Barème

1 point si le compte après agrandissement est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-19_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Appliquer le facteur d'échelle à chaque détail.

**Étape 2.** Comparer ensuite à la résolution de la machine.

**Étape 3.** Compter.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Juger avant l'agrandissement : les douze détails sont alors sous 0,4 mm, et l'on conclut que rien n'est imprimable. L'agrandissement en sauve la moitié — refaire toute la maquette pour rien est une décision coûteuse fondée sur une comparaison faite à la mauvaise échelle.

### Pièges fréquents

- Comparer avant d'agrandir.
- Oublier que la tolérance du document, elle aussi, suit l'échelle.

### Pourquoi ce jeu de données

Les douze détails sont tous sous la résolution avant agrandissement et six seulement après : les deux réponses, 12 et 6, sont dans un rapport de deux, et la première est aussi le nombre total de détails — ce qui la rend immédiatement suspecte à qui la relit.

### Pour aller plus loin

- Trouver le facteur minimal qui sauve tous les détails.
- Reprendre avec une machine à 0,2 mm de résolution.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-19_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-19_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-19.json` | Descripteur pour le plugin Magpie |
| `RH-19_fiche.md` | La présente fiche |
| `RH-19_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-19_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-19_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
