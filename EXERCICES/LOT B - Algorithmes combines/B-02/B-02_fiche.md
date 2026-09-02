# B-02 — Garde-corps à barreaudage régulier

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B1 · Architecture et construction |
| **Référence au référentiel** | REF-064, REF-047, REF-043 |
| **Compétence visée** | Répartir des éléments sous une contrainte d'espacement LIBRE, en distinguant l'entraxe de l'espace entre matières. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | A-35, A-12 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 14 composants |
| **Gamification associée** | G-07 Étoiles de performance |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Répartir des éléments à pas maximal imposé, cas classique de calcul d'entraxe.

### Contexte

L'espacement libre d'un garde-corps est une règle de sécurité : c'est le vide qui est mesuré, pas la distance d'axe en axe.

### Énoncé

> Sur la main courante fournie, place des barreaux verticaux de 16 mm de diamètre. L'espacement libre entre barreaux ne doit jamais dépasser 110 mm. Détermine le nombre de barreaux et affiche l'entraxe réel.

### Ce qui vous est fourni

Une courbe de main courante et une hauteur de garde-corps internalisées.

### Ce qui est attendu

25 barreaux, pour un espacement libre de 108 mm.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-02_sujet.gh`

### Barème

2 points pour le barreaudage, 1 point pour le respect strict des 110 mm.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-02_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Mesurer la longueur de la main courante avec Length.

**Étape 2.** Calculer le pas maximal admissible : 110 + 16 = 126 mm.

**Étape 3.** Diviser la longueur par 126 puis arrondir à l'entier supérieur (Round avec le mode Ceiling ou Ceiling direct).

**Étape 4.** Recalculer l'entraxe réel = longueur / nombre d'intervalles.

**Étape 5.** Poser Divide Curve avec ce nombre d'intervalles.

**Étape 6.** Tracer les segments verticaux depuis chaque point puis les transformer en Pipe de rayon 8.

**Étape 7.** Afficher nombre et entraxe dans un Panel.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Diviser la longueur par l'espacement libre seul : on obtient 30 barreaux. Le barreau occupe 16 mm qu'il faut ajouter à chaque pas — sinon cinq barreaux de trop sont commandés, et l'espacement réel tombe à 92 mm au lieu des 108 possibles.

### Pièges fréquents

- Confondre entraxe et espacement libre : l'écart libre vaut entraxe moins le diamètre.
- Arrondir à l'entier le plus proche au lieu de l'entier supérieur : l'espacement dépasse la limite.
- Oublier les barreaux d'extrémité.

### Pourquoi ce jeu de données

3 240 mm de main courante, barreaux de 16 mm, 110 mm de libre admis : le calcul juste donne 25 barreaux et 108 mm de libre — juste sous la limite, ce qui est le cas réel d'un garde-corps optimisé. Le calcul faux en donne 30, soit 20 % de matière en trop.

### Pour aller plus loin

- Suivre une main courante inclinée en gardant les barreaux verticaux.
- Ajouter une lisse basse et calculer le linéaire total de matière.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-02_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-02_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-02.json` | Descripteur pour le plugin Magpie |
| `B-02_fiche.md` | La présente fiche |
| `B-02_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-02_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-02_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
