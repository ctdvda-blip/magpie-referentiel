# WB-02 — Publier un configurateur

**Fiche d'exercice Magpie** · Lot WB — Interfaces, web et interopérabilité

| | |
|---|---|
| **Thématique** | WB2 · Publication web |
| **Référence au référentiel** | REF-108, REF-109, REF-110 |
| **Compétence visée** | Publier une définition sur le web et en faire sortir les livrables attendus par un client. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 90 min |
| **Prérequis** | WB-01 |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-25 Projet jalonné |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Publier une définition sur le web et en faire sortir les livrables attendus par un client.

### Contexte

Le client veut configurer son produit depuis son navigateur et repartir avec un plan et un modèle 3D.

### Énoncé

> Publiez la définition interfacée en WB-01 sur une plateforme web. Le configurateur doit permettre de régler les paramètres, de télécharger le modèle 3D et d'obtenir un plan au format PDF.

### Ce qui vous est fourni

La définition interfacée de WB-01 et un compte sur une plateforme de publication.

### Ce qui est attendu

Un configurateur en ligne qui rend les trois livrables.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **Visuel**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`WB-02_sujet.gh`

### Barème

Grille : configurateur en ligne (2), export 3D (1), plan PDF juste sur toute la plage (2).

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `WB-02_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Vérifier que la définition ne dépend d'aucun plugin absent de la plateforme.

**Étape 2.** Contrôler les temps de calcul : ce qui prend cinq secondes en local est insupportable en ligne.

**Étape 3.** Publier, puis régler l'interface exposée.

**Étape 4.** Brancher l'export du modèle 3D.

**Étape 5.** Produire le plan PDF et vérifier qu'il reste juste pour toutes les valeurs autorisées.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Publier sans borner les paramètres. En ligne, personne ne surveille : une valeur hors domaine produit une géométrie absurde, ou fait échouer le calcul côté serveur, et c'est le client qui le voit en premier.

### Pièges fréquents

- Plugin non disponible côté serveur : la définition ne calcule pas.
- Paramètres non bornés.
- Plan PDF correct pour la valeur par défaut seulement.

### Pourquoi ce jeu de données

—

### Limite de la correction automatique

> Le livrable est un service en ligne : validation visuelle. Dépend d'une plateforme tierce et d'un compte.

### Pour aller plus loin

- Ajouter un chiffrage automatique au configurateur.
- Mesurer le temps de réponse et l'optimiser.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `WB-02_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `WB-02_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `WB-02.json` | Descripteur pour le plugin Magpie |
| `WB-02_fiche.md` | La présente fiche |
| `WB-02_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `WB-02_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `WB-02_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
