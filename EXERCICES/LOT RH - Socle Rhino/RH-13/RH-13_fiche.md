# RH-13 — Ce que le fichier contient vraiment

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH1 · Interface et navigation Rhino |
| **Référence au référentiel** | REF-006, REF-004 |
| **Compétence visée** | Distinguer ce qu'un fichier contient de ce qu'il affiche, et compter sur la structure plutôt que sur l'écran. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | RH-02 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-17 Passation |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Distinguer ce qu'un fichier contient de ce qu'il affiche, et compter sur la structure plutôt que sur l'écran.

### Contexte

Avant d'envoyer le fichier, on veut savoir ce qu'il transporte : un calque éteint part quand même, avec tout ce qu'il contient.

### Énoncé

> Les huit calques vous sont fournis avec leur état et le nombre d'objets de chacun. Donnez le nombre d'objets actuellement VISIBLES.

### Ce qui vous est fourni

Les huit calques : nom, allumé ou éteint, nombre d'objets.

### Ce qui est attendu

176 objets visibles, sur les 270 que contient le fichier.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-13_sujet.gh`

### Barème

1 point si le compte des objets visibles est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-13_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Retenir les seuls calques allumés.

**Étape 2.** Sommer leurs objets.

**Étape 3.** Comparer au total du fichier.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Répondre 270, le contenu du fichier. C'est la bonne réponse à une autre question — et c'est justement l'écart entre les deux qui compte : 94 objets, dont d'anciens relevés, partiront chez le destinataire sans que personne les ait vus.

### Pièges fréquents

- Sommer tous les calques.
- Oublier qu'un calque éteint voyage avec le fichier.

### Pourquoi ce jeu de données

Quatre calques allumés sur huit, et les éteints portent un tiers des objets. Les deux réponses — 176 et 270 — sont assez éloignées pour qu'aucune approximation ne les confonde.

### Limite de la correction automatique

> Le compte des objets visibles ne dit rien de leur poids ni de ce qu'ils révèlent. Un calque éteint nommé « anciens relevés » est un problème de confidentialité avant d'être un problème de comptage.

### Pour aller plus loin

- Donner ce que le fichier transporterait après purge des calques éteints.
- Repérer les calques dont le nom seul pose un problème.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-13_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-13_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-13.json` | Descripteur pour le plugin Magpie |
| `RH-13_fiche.md` | La présente fiche |
| `RH-13_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-13_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-13_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
