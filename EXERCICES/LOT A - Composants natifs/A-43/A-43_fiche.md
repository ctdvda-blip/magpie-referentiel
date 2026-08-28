# A-43 — Fermer une polysurface en solide

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A10 · Surfaces et solides |
| **Référence au référentiel** | REF-070 |
| **Compétence visée** | Refermer une enveloppe ouverte et établir qu'elle constitue bien un solide. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-41 |
| **Mode de validation** | SingleValue — tolérance — |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-20 Erreur volontaire à débusquer |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Refermer une enveloppe ouverte et établir qu'elle constitue bien un solide.

### Contexte

Un caisson doit être étanche avant d'être chiffré en volume de remplissage ; une enveloppe ouverte n'a pas de volume.

### Énoncé

> L'enveloppe fournie présente deux ouvertures. Refermez-la, puis établissez par une valeur numérique qu'elle est désormais un solide.

### Ce qui vous est fourni

Une polysurface ouverte internalisée.

### Ce qui est attendu

Une valeur numérique attestant le caractère fermé, et un volume non nul.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-43_sujet.gh`

### Barème

1 point si le solide est fermé et prouvé.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-43_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Cap Holes sur la polysurface.

**Étape 2.** Poser Volume : un volume non nul confirme la fermeture.

**Étape 3.** Utiliser Deconstruct Brep ou un composant Is Solid pour obtenir directement le booléen.

**Étape 4.** Relier vers un Panel.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Se fier à l'aspect visuel : une enveloppe non fermée s'affiche exactement comme une enveloppe fermée. Seul le contrôle numérique tranche — c'est tout l'objet de l'exercice.

### Pièges fréquents

- Cap Holes ne ferme que les ouvertures planes.
- Un volume affiché à zéro signale une polysurface encore ouverte.

### Pour aller plus loin

- Réparer une ouverture non plane avec un Loft complémentaire puis Brep Join.
- Contrôler l'étanchéité en vue de l'impression 3D.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-43_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-43_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-43.json` | Descripteur pour le plugin Magpie |
| `A-43_fiche.md` | La présente fiche |
| `A-43_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-43_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-43_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
