# A-21 — Nettoyer une structure

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A4 · Arbres de données |
| **Référence au référentiel** | REF-050 |
| **Compétence visée** | Supprimer les niveaux de regroupement devenus inutiles sans détruire le regroupement utile. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-20 |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-30 Mode coopératif |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Supprimer les niveaux de regroupement devenus inutiles sans détruire le regroupement utile.

### Contexte

Un enchaînement d'opérations a empilé des niveaux de branche dont aucun ne porte plus de sens.

### Énoncé

> Le flux fourni porte des chemins à quatre niveaux, dont trois ne distinguent plus rien. Ramenez-le à un seul niveau, sans fusionner les groupes entre eux. Indiquez le nombre de branches obtenu.

### Ce qui vous est fourni

Un arbre internalisé de chemins {0;0;0;0} à {0;0;0;3}.

### Ce qui est attendu

Quatre branches, aux chemins {0} à {3}.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SetEquality**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-21_sujet.gh`

### Barème

1 point si les chemins finaux sont {0} à {3}.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-21_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Brancher un Param Viewer pour lire les chemins de départ.

**Étape 2.** Poser Simplify Tree : les niveaux communs à toutes les branches sont supprimés.

**Étape 3.** Vérifier les nouveaux chemins dans le Param Viewer.

**Étape 4.** Retenir : Trim Tree supprime le dernier niveau, Simplify supprime les niveaux redondants.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Tout aplatir : on obtient une branche unique et le regroupement est perdu. C'est l'erreur qui distingue « simplifier » de « écraser ».

### Pièges fréquents

- Utiliser Flatten : la structure disparaît complètement.
- Trim Tree avec une profondeur trop grande fusionne des branches utiles.

### Pour aller plus loin

- Comparer Simplify et Trim Tree sur le même arbre.
- Reconstruire un chemin cible avec Path Mapper.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-21_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-21_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-21.json` | Descripteur pour le plugin Magpie |
| `A-21_fiche.md` | La présente fiche |
| `A-21_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-21_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-21_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
