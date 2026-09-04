# RH-28 — La surface d'une extrusion

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH2 · Modélisation Rhino |
| **Référence au référentiel** | REF-009, REF-010, REF-011 |
| **Compétence visée** | Établir la surface développée d'une extrusion à partir du périmètre de son contour, refermé. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 14 min |
| **Prérequis** | RH-04 |
| **Mode de validation** | NumericTolerance — tolérance 0.0001 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-14 Le puzzle de câblage |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Établir la surface développée d'une extrusion à partir du périmètre de son contour, refermé.

### Contexte

Le bardage d'un local technique se commande au mètre carré. Sa surface est celle du contour au sol, développé sur la hauteur.

### Énoncé

> Le contour au sol vous est donné par ses cinq sommets, en millimètres. Le bardage monte à 2 600 mm. Donnez sa surface, en mètres carrés.

### Ce qui vous est fourni

Les cinq sommets du contour et la hauteur de bardage.

### Ce qui est attendu

15,7566 m² de bardage, à 0,0001 près.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.0001.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-28_sujet.gh`

### Barème

1 point si la surface est juste à 0,0001 m².

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-28_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Construire les cinq points depuis leurs coordonnées.

**Étape 2.** Tracer la polyligne en la refermant.

**Étape 3.** Mesurer sa longueur.

**Étape 4.** Multiplier par la hauteur, puis convertir en mètres carrés.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Laisser le contour OUVERT : 12,1166 m², soit 3,64 m² de moins. Le segment de fermeture mesure 1 400 mm — c'est un mur entier, et l'aperçu d'une polyligne ouverte ressemble à celui d'une polyligne fermée.

### Pièges fréquents

- Laisser la polyligne ouverte.
- Convertir une seule fois au lieu de deux : les millimètres carrés font un million par mètre carré.

### Pourquoi ce jeu de données

Cinq sommets, dont un pan coupé oblique qui interdit de retrouver le périmètre par une somme de cotes lues sur le plan. Le segment de fermeture pèse 23 % du total : l'oubli ne se rattrape pas au jugé.

### Limite de la correction automatique

> La surface est celle de l'ENVELOPPE. Elle ne déduit ni les portes ni les grilles de ventilation, et n'ajoute pas les recouvrements de lames : la commande se fait sur une surface majorée.

### Pour aller plus loin

- Déduire une porte de 900 × 2 100.
- Refaire le calcul pour une hauteur variable.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-28_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-28_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-28.json` | Descripteur pour le plugin Magpie |
| `RH-28_fiche.md` | La présente fiche |
| `RH-28_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-28_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-28_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
