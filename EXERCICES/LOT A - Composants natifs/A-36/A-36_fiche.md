# A-36 — Courbes passant par des points

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A8 · Géométrie vectorielle et filaire |
| **Référence au référentiel** | REF-063 |
| **Compétence visée** | Distinguer une courbe qui passe par des points d'une courbe que ces points contrôlent. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-35 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-12 Memory |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Distinguer une courbe qui passe par des points d'une courbe que ces points contrôlent.

### Contexte

Un profil de main courante est défini par des points de passage imposés ; un second tracé, plus souple, sert d'étude de forme.

### Énoncé

> Six points vous sont fournis. Tracez la courbe qui passe exactement par chacun d'eux, puis celle qui ne fait que s'en approcher en les prenant pour points de commande. Superposez les deux.

### Ce qui vous est fourni

Une liste de 6 points internalisée.

### Ce qui est attendu

Deux courbes distinctes appuyées sur les mêmes points.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,1 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-36_sujet.gh`

### Barème

1 point par courbe correcte.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-36_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Interpolate (Curve > Spline) : la courbe passe par les points.

**Étape 2.** Poser Nurbs Curve sur la même liste : les points deviennent des points de contrôle.

**Étape 3.** Comparer visuellement les deux tracés.

**Étape 4.** Faire varier le degré des deux courbes pour observer l'effet.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Obtenir deux courbes confondues : signe qu'on a employé deux fois la même construction. Les deux tracés ne coïncident qu'aux extrémités.

### Pièges fréquents

- Attendre que Nurbs Curve passe par les points.
- Degré supérieur au nombre de points moins un : la courbe échoue.

### Limite de la correction automatique

> Les deux courbes s'appuient sur les mêmes points. Laquelle convient dépend de la NATURE des points : des points relevés, entachés d'erreur, appellent l'approximation ; des points de conception appellent l'interpolation. Le modèle ne le sait pas.

### Pour aller plus loin

- Fermer les deux courbes et comparer la continuité.
- Tracer la PolyLine et arrondir ses angles.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-36_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-36_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-36.json` | Descripteur pour le plugin Magpie |
| `A-36_fiche.md` | La présente fiche |
| `A-36_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-36_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-36_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
