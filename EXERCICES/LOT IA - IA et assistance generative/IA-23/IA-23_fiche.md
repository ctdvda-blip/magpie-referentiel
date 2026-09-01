# IA-23 — Combien de tours avant que tout passe

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA3 · Développement de plugins assisté |
| **Référence au référentiel** | REF-126 |
| **Compétence visée** | Piloter une itération avec un agent de code en s'appuyant sur une batterie de cas, et savoir quand elle est finie. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | IA-07 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-20 Contre-expertise |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Piloter une itération avec un agent de code en s'appuyant sur une batterie de cas, et savoir quand elle est finie.

### Contexte

L'agent corrige le composant tour après tour. Sans batterie de cas, on s'arrête quand on est fatigué.

### Énoncé

> Dix-huit cas d'essai doivent passer. Le relevé des cinq tours d'itération vous est fourni. Donnez le numéro du premier tour où tous les cas passent.

### Ce qui vous est fourni

Le nombre de cas à satisfaire, et le nombre de cas qui passent à chaque tour.

### Ce qui est attendu

4 — c'est au quatrième tour que les dix-huit cas passent.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-23_sujet.gh`

### Barème

1 point si le numéro du premier tour suffisant est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-23_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Comparer, tour par tour, le nombre de cas qui passent à la cible.

**Étape 2.** Retenir le PREMIER tour qui l'atteint.

**Étape 3.** Constater que les tours suivants n'apportent rien.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Rendre 5, le dernier tour du relevé. Le cinquième n'a rien amélioré : il a coûté un aller-retour pour confirmer que le quatrième suffisait. Savoir s'arrêter fait partie de la compétence — une itération sans critère d'arrêt ne s'arrête pas, elle s'épuise.

### Pièges fréquents

- Rendre le dernier tour du relevé.
- Conclure qu'un composant qui passe tous les cas est juste.

### Pourquoi ce jeu de données

Les cas passent 7, 12, 16, 18, 18 : la progression ralentit, ce qui est le profil habituel, et le palier final rend visible le tour de trop. Le relevé compte cinq tours pour que la réponse ne soit ni le premier ni le dernier.

### Limite de la correction automatique

> Dix-huit cas qui passent ne font pas un composant juste : ils font un composant juste SUR CES CAS. La compétence suivante est d'écrire les cas qui manquent.

### Pour aller plus loin

- Estimer le coût des tours inutiles sur une série de dix composants.
- Écrire trois cas supplémentaires qui feraient échouer le composant du quatrième tour.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-23_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-23_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-23.json` | Descripteur pour le plugin Magpie |
| `IA-23_fiche.md` | La présente fiche |
| `IA-23_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-23_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-23_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
