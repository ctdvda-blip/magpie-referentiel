# IA-07 — Un plugin .gha conduit par un agent

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA3 · Développement de plugins assisté |
| **Référence au référentiel** | REF-125, REF-126, REF-127 |
| **Compétence visée** | Conduire le développement d'un plugin Grasshopper avec un agent de code, jusqu'au composant réellement chargé par Rhino. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 90 min |
| **Prérequis** | IA-06 |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-25 Projet jalonné |
| **Version** | v0.3-260826 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Conduire le développement d'un plugin Grasshopper avec un agent de code, jusqu'au composant réellement chargé par Rhino.

### Contexte

Un geste répété dans plusieurs définitions mérite son propre composant, distribuable à l'équipe.

### Énoncé

> Choisissez un traitement que vous refaites souvent à la main. Faites-en un composant distribuable, chargé par Rhino et visible dans l'onglet de votre choix, en conduisant le développement avec un agent de code.

### Ce qui vous est fourni

Un poste avec l'environnement de compilation en place et un agent de code disposant de l'accès aux fichiers du projet.

### Ce qui est attendu

Un plugin chargé par Rhino, dont le composant apparaît dans l'onglet visé et produit le résultat attendu.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **Visuel**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-07_sujet.gh`

### Barème

Grille : composant chargé (2), résultat juste (2), GUID stable entre deux versions (1), documentation (1).

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-07_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Écrire d'abord, en une page, ce que fait le composant : entrées, sorties, cas limites. C'est le document que l'agent lira.

**Étape 2.** Faire produire le squelette du projet, en imposant un GUID fixe et une catégorie stable.

**Étape 3.** Compiler, déposer le fichier dans le dossier des composants, débloquer le fichier si Windows l'a marqué, redémarrer Rhino.

**Étape 4.** Itérer par petites demandes vérifiables plutôt qu'en une seule grande, et relire chaque modification.

**Étape 5.** Consigner la version et le GUID dans la documentation du plugin avant toute diffusion.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Laisser l'agent régénérer le GUID du composant à chaque itération. Le plugin fonctionne, mais chaque nouvelle version casse les définitions qui employaient la précédente — et le symptôme n'apparaît que chez les collègues.

### Pièges fréquents

- Ne pas versionner avant de laisser l'agent modifier les fichiers : une régression devient irrattrapable.
- Accepter une refonte massive proposée par l'agent alors que la demande portait sur un détail.
- Oublier le déblocage du fichier téléchargé : Rhino charge le plugin sans rien dire, et le composant n'apparaît pas.

### Pourquoi ce jeu de données

—

### Limite de la correction automatique

> Le livrable est un plugin compilé : le checker Magpie ne sait comparer que des nombres. La validation est donc visuelle, sur le composant réellement chargé. Ramener l'exercice à une valeur numérique n'évaluerait plus la compétence visée.

### Pour aller plus loin

- Ajouter une icône et une entrée d'aide au composant.
- Publier le plugin avec un fichier de licence explicite.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-07_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-07_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-07.json` | Descripteur pour le plugin Magpie |
| `IA-07_fiche.md` | La présente fiche |
| `IA-07_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-07_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-07_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
