# A-11 — List Item et indexation

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A3 · Listes |
| **Référence au référentiel** | REF-042 |
| **Compétence visée** | Atteindre un élément par son rang, et atteindre le dernier sans présumer de l'effectif. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-10 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-12 Memory |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Atteindre un élément par son rang, et atteindre le dernier sans présumer de l'effectif.

### Contexte

Une liste de débit est reprise par un opérateur qui doit contrôler deux pièces précises avant lancement.

### Énoncé

> Le débit comporte 24 pièces. Relevez la longueur de la quatrième pièce, puis celle de la dernière — sachant que le débit s'allongera la semaine prochaine et que votre montage devra encore désigner la dernière pièce sans être retouché.

### Ce qui vous est fourni

Les 24 longueurs de débit, en millimètres, dans l'ordre du bon de commande.

### Ce qui est attendu

Deux longueurs, dans cet ordre : 2 075 mm puis 2 830 mm — celle du quatrième rang, puis celle du dernier.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-11_sujet.gh`

### Barème

2 points : 1 par extraction correcte.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-11_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser List Item et régler l'index à 3 : la lettre D sort (le premier élément porte l'index 0).

**Étape 2.** Pour la dernière lettre, poser List Length puis soustraire 1.

**Étape 3.** Relier ce résultat sur l'index d'un second List Item.

**Étape 4.** Alternative : activer l'index négatif -1 sur List Item (clic droit > Wrap).

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Saisir en dur le rang de la dernière pièce. Le montage donne la bonne réponse aujourd'hui et la mauvaise dès que le débit change — une erreur qu'un exercice sans la clause d'évolution ne révélerait jamais.

### Pièges fréquents

- Saisir l'index 4 pour la lettre D.
- Coder 9 en dur : le montage casse si la liste change de taille.

### Pourquoi ce jeu de données

24 longueurs non ordonnées : ni le rang 4 ni le dernier rang ne se repèrent visuellement.

### Pour aller plus loin

- Extraire simultanément les index 0, 4 et 9 en branchant une liste d'index.
- Extraire un élément sur deux avec Cull Index.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-11_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-11_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-11.json` | Descripteur pour le plugin Magpie |
| `A-11_fiche.md` | La présente fiche |
| `A-11_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-11_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-11_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
