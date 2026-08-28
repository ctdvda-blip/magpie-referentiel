# A-44 — Opérations booléennes

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A10 · Surfaces et solides |
| **Référence au référentiel** | REF-071 |
| **Compétence visée** | Combiner des solides par soustraction et quantifier la matière retirée. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-43 |
| **Mode de validation** | NumericTolerance — tolérance 1 % |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-21 Golf de composants |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Combiner des solides par soustraction et quantifier la matière retirée.

### Contexte

Une platine d'assemblage est percée pour le passage des boulons ; le poids retiré entre dans le bilan de charge.

### Énoncé

> La platine vous est fournie. Percez-la de quatre trous traversants de 20 mm de diamètre, puis donnez le volume de matière retirée.

### Ce qui vous est fourni

Un bloc et quatre cylindres internalisés.

### Ce qui est attendu

La platine percée et le volume retiré.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 1 %.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-44_sujet.gh`

### Barème

1 point pour le perçage, 1 point pour le volume.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-44_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Solid Difference : bloc sur A, cylindres sur B.

**Étape 2.** Vérifier que les cylindres traversent bien le bloc.

**Étape 3.** Calculer le Volume du bloc initial et du bloc percé.

**Étape 4.** Soustraire les deux valeurs et afficher le résultat.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Calculer le volume des quatre cylindres entiers plutôt que la différence des volumes : si les cylindres dépassent de la platine pour garantir le percement, l'écart est exactement la partie qui dépasse.

### Pièges fréquents

- Inverser A et B : on obtient les cylindres percés par le bloc.
- Cylindres tangents à la face : l'opération échoue.

### Pour aller plus loin

- Additionner les volumes des cylindres et comparer au volume retiré.
- Remplacer la différence par une intersection.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-44_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-44_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-44.json` | Descripteur pour le plugin Magpie |
| `A-44_fiche.md` | La présente fiche |
| `A-44_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-44_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-44_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
