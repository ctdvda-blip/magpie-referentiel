# A-42 — Balayage et révolution

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A10 · Surfaces et solides |
| **Référence au référentiel** | REF-069 |
| **Compétence visée** | Engendrer une surface par déplacement d'un profil le long d'un guide, et par rotation autour d'un axe. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-41 |
| **Mode de validation** | GeometryTolerance — tolérance 0,5 mm |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-05 Badges et trophées |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Engendrer une surface par déplacement d'un profil le long d'un guide, et par rotation autour d'un axe.

### Contexte

Une main courante tubulaire suit un limon ; un fût de colonne est engendré par rotation de son profil.

### Énoncé

> Le profil circulaire et son guide vous sont fournis, ainsi qu'un profil plan. Engendrez le tube en promenant le profil circulaire le long du guide, puis le fût en faisant tourner le profil plan autour de l'axe vertical.

### Ce qui vous est fourni

Un profil circulaire, une courbe guide et un profil plan internalisés.

### Ce qui est attendu

Un tube et une surface de révolution.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **GeometryTolerance** avec une tolérance de 0,5 mm.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-42_sujet.gh`

### Barème

1 point par surface correcte.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-42_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Poser Sweep 1 : courbe guide sur Rail, profil sur Sections.

**Étape 2.** Si le profil n'est pas positionné sur le rail, l'orienter d'abord avec Orient ou Perp Frame.

**Étape 3.** Poser Revolution : profil plan sur P, axe Z sur A, domaine 0 à 2π sur D.

**Étape 4.** Contrôler la fermeture des surfaces obtenues.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Omettre de désigner l'axe de rotation : le composant reste en attente et ne produit rien, sans que le montage paraisse faux.

### Pièges fréquents

- Profil non perpendiculaire au rail : le balayage se déforme.
- Domaine de révolution incomplet : le vase reste ouvert.

### Pour aller plus loin

- Balayer avec deux rails (Sweep 2).
- Faire varier la section le long du rail.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-42_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-42_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-42.json` | Descripteur pour le plugin Magpie |
| `A-42_fiche.md` | La présente fiche |
| `A-42_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-42_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-42_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
