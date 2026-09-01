# PL-08 — Les composants qui ne disent pas leur nom

**Fiche d'exercice Magpie** · Lot PL — Écosystème de plugins

| | |
|---|---|
| **Thématique** | PL1 · Écosystème de plugins |
| **Référence au référentiel** | REF-031, REF-032, REF-033 |
| **Compétence visée** | Repérer, dans une définition, ce qu'un relecteur ne pourra pas comprendre sans remonter les câbles. |
| **Case Bloom (révisée)** | Évaluer × conceptuelle |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | PL-03 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-17 Passation |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Repérer, dans une définition, ce qu'un relecteur ne pourra pas comprendre sans remonter les câbles.

### Contexte

Les plugins d'ergonomie affichent les noms, alignent, colorent. Ils ne remplacent pas le fait de nommer : ils rendent visible qu'on ne l'a pas fait.

### Énoncé

> Les vingt-quatre surnoms relevés sur la définition vous sont fournis. Donnez le nombre de composants dont le surnom ne dit pas ce qu'ils font.

### Ce qui vous est fourni

Les vingt-quatre surnoms, tels qu'ils apparaissent sur le canevas.

### Ce qui est attendu

10 surnoms ne disent rien de ce que le composant fait.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`PL-08_sujet.gh`

### Barème

1 point si le compte des surnoms muets est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `PL-08_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Lire chaque surnom en se demandant ce qu'il apprend à qui n'a pas écrit la définition.

**Étape 2.** Écarter le critère de longueur.

**Étape 3.** Compter les muets.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter les surnoms COURTS. « Pt » et « Vec » sont courts et muets, mais « Jeu de pose » est court et parlant, tandis qu'un surnom long et générique ne vaudrait pas mieux que « A ». Ce qui se juge est ce que le surnom APPREND, pas sa longueur.

### Pièges fréquents

- Juger sur la longueur.
- Considérer qu'un nom de composant par défaut est acceptable parce qu'il est exact.

### Pourquoi ce jeu de données

Dix surnoms muets sur vingt-quatre, soit plus de quatre sur dix — la proportion ordinaire d'une définition écrite sans intention de la faire relire. Les muets se répartissent en deux familles : six abréviations de composants (Srf, Mult, Div, Rot, Pt, Vec) et quatre lettres seules (A, D, X, N). Deux familles, pour qu'un critère de longueur seul ne suffise pas à les trouver.

### Limite de la correction automatique

> L'exercice compte. Il ne renomme pas — et renommer est le vrai travail, qui se juge en MP-01.

### Pour aller plus loin

- Proposer un surnom parlant pour chacun des dix.
- Installer un plugin d'affichage des noms et refaire la lecture.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `PL-08_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `PL-08_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `PL-08.json` | Descripteur pour le plugin Magpie |
| `PL-08_fiche.md` | La présente fiche |
| `PL-08_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `PL-08_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `PL-08_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
