# B-07 — Tiroir paramétrique avec jeux fonctionnels

**Fiche d'exercice Magpie** · Lot B — Algorithmes combinés

| | |
|---|---|
| **Thématique** | B2 · Design de mobilier |
| **Référence au référentiel** | REF-070, REF-072 |
| **Compétence visée** | Appliquer un jeu fonctionnel du bon côté, et le bon nombre de fois. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | B-06, A-46 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 20 composants |
| **Gamification associée** | G-04 Système de vies |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Intégrer des jeux de fonctionnement et vérifier l'absence de collision.

### Contexte

La coulisse demande 13 mm de chaque côté. Un tiroir trop large ne rentre pas ; trop étroit, il se met en travers.

### Énoncé

> Insère dans le caisson un tiroir sur coulisses de 13 mm de jeu latéral par côté et 2 mm en hauteur. Le tiroir doit pouvoir coulisser de toute sa profondeur sans collision : prouve-le.

### Ce qui vous est fourni

Le caisson de l'exercice B-06.

### Ce qui est attendu

736 mm de largeur de tiroir.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`B-07_sujet.gh`

### Barème

2 points pour le tiroir, 2 points pour la preuve d'absence de collision.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `B-07_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Calculer la largeur intérieure disponible : L − 2 × 19.

**Étape 2.** Déduire la largeur du tiroir : intérieur − 2 × 13.

**Étape 3.** Construire le caisson de tiroir en panneaux de 15 mm.

**Étape 4.** Poser un slider de course de 0 à P pour piloter l'ouverture.

**Étape 5.** Déplacer le tiroir de cette course avec Move.

**Étape 6.** Poser Collision Many|Many entre les panneaux du tiroir et ceux du caisson.

**Étape 7.** Afficher dans un Panel le nombre de collisions détectées : il doit rester à zéro sur toute la course.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Ne retrancher le jeu qu'une fois : 749 mm. La coulisse se pose des DEUX côtés, et 13 mm de trop suffisent à empêcher le tiroir d'entrer. C'est l'erreur de jeu la plus répandue en agencement.

### Pièges fréquents

- Appliquer le jeu une seule fois au lieu de deux fois (un par côté).
- Tester la collision uniquement en position fermée.
- Tolérance de collision de Grasshopper trop lâche : un contact tangent passe inaperçu.

### Pourquoi ce jeu de données

Caisson de 800 mm en panneaux de 19 : intérieur 762 mm, moins deux fois 13 = 736. Les deux réponses, 736 et 749, ne diffèrent que de 13 mm — assez peu pour n'être vues qu'au montage.

### Limite de la correction automatique

> 736 mm est la largeur du CAISSON de tiroir. La façade, elle, suit un jeu différent — celui du rainurage entre façades, typiquement 3 mm — et ne se déduit pas de ce calcul.

### Pour aller plus loin

- Ajouter une façade en applique avec débord.
- Générer plusieurs tiroirs de hauteurs différentes réparties automatiquement.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `B-07_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `B-07_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `B-07.json` | Descripteur pour le plugin Magpie |
| `B-07_fiche.md` | La présente fiche |
| `B-07_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `B-07_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `B-07_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
