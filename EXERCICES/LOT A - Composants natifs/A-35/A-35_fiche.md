# A-35 — Diviser et évaluer une courbe

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A8 · Géométrie vectorielle et filaire |
| **Référence au référentiel** | REF-064 |
| **Compétence visée** | Répartir des positions régulières le long d'une courbe et récupérer le repère local en chaque position. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-34 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Répartir des positions régulières le long d'une courbe et récupérer le repère local en chaque position.

### Contexte

Un conduit souple est maintenu par des colliers régulièrement espacés le long de son tracé ; chaque collier est perpendiculaire au conduit.

### Énoncé

> Le tracé du conduit vous est fourni. Placez 12 colliers de 5 de rayon, régulièrement espacés le long du tracé et perpendiculaires à celui-ci en chaque point.

### Ce qui vous est fourni

Une courbe libre internalisée.

### Ce qui est attendu

Autant de cercles de 5 de rayon que la consigne en demande, perpendiculaires au tracé en chacune de leurs positions.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-35_sujet.gh`

### Barème

1 point si 12 cercles perpendiculaires sont produits.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-35_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 12 cercles de rayon 5, perpendiculaires au tracé.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Poser Divide Curve avec Count = 11 pour obtenir 12 points (12 divisions donneraient 13 points).

**Étape 2.** Récupérer la sortie T (tangentes) ou utiliser la sortie P de Perp Frames.

**Étape 3.** Poser Perp Frames avec Count = 11 : les plans sont déjà perpendiculaires.

**Étape 4.** Poser Circle avec ces plans et un rayon de 5.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Placer les colliers à plat dans le plan horizontal : ils sont bien répartis, mais aucun n'enserre le conduit. L'erreur révèle qu'on a récupéré les positions sans les repères qui les accompagnent.

### Pièges fréquents

- Divide Curve avec N divisions produit N+1 points quand la courbe est ouverte.
- Sur une courbe fermée, N divisions produisent N points.

### Pour aller plus loin

- Remplacer Divide Curve par Divide Length pour un pas fixe.
- Lofter les 12 cercles pour obtenir un tube.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-35_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-35_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-35.json` | Descripteur pour le plugin Magpie |
| `A-35_fiche.md` | La présente fiche |
| `A-35_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-35_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-35_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
