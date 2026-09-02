# IA-01 — Spécifier un composant plutôt que le décrire

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA1 · Formuler et cadrer une demande |
| **Référence au référentiel** | REF-117, REF-139 |
| **Compétence visée** | Rédiger la spécification d'un composant assez précise pour que le code obtenu soit juste du premier coup. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | A-08 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-01 Score visible |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Rédiger la spécification d'un composant assez précise pour que le code obtenu soit juste du premier coup.

### Contexte

Le contrôle de réception d'un lot de platines porte sur l'entraxe de perçage, nominal 250 mm, toléré à ± 1,5 mm.

### Énoncé

> Les 28 entraxes relevés vous sont fournis. Faites produire par un assistant un composant scripté qui renvoie le nombre de platines hors tolérance, et branchez sa sortie sur la réponse. Vous ne corrigerez pas le code à la main : si le résultat est faux, c'est la demande qu'il faut reprendre.

### Ce qui vous est fourni

Les 28 entraxes relevés, en millimètres, ainsi que l'entraxe nominal et la tolérance, chacun sur une entrée distincte.

### Ce qui est attendu

Un nombre entier : combien de platines sortent de la tolérance. Il doit sortir du composant produit par l'assistant, non d'un comptage à la main.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-01_sujet.gh`

### Barème

1 point si la sortie vaut 5 sans retouche manuelle du code.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-01_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### La valeur attendue

> 10 — le nombre de platines dont l'entraxe s'écarte de plus de 1,5 mm de 250 mm.

*Cette valeur ne figure pas sur la fiche remise à l'apprenant : elle y écrirait la réponse.*

### Marche à suivre

**Étape 1.** Écrire la spécification avant d'ouvrir l'assistant : trois entrées (liste de cotes, nominale, tolérance), une sortie entière, et la règle exacte — écart absolu strictement supérieur à la tolérance.

**Étape 2.** Préciser le contexte : composant Grasshopper pour Rhino 8, langage retenu, accès en liste sur la première entrée.

**Étape 3.** Coller le code obtenu dans un composant scripté et déclarer les entrées avec les bons types.

**Étape 4.** Relever la sortie et la confronter à un contrôle indépendant — un comptage monté avec des composants natifs.

**Étape 5.** Si l'écart existe, reprendre la spécification sur le point précis qui a manqué, pas la totalité de la demande.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Obtenir un composant qui ne compte que les entraxes trop grands, parce que la demande disait « supérieur à la tolérance » sans préciser qu'il s'agit d'un écart en valeur absolue. Le code est correct, la spécification ne l'était pas — c'est précisément ce que l'exercice mesure.

### Pièges fréquents

- Demander « compte les valeurs hors tolérance » sans définir « hors tolérance » : l'assistant choisit à votre place.
- Laisser l'entrée en accès élément au lieu de liste : le composant s'exécute une fois par valeur et renvoie 28 résultats.
- Accepter le premier code qui s'exécute sans erreur.

### Pourquoi ce jeu de données

28 entraxes réels resserrés autour de 250, dont les hors-tolérance sont répartis dans les deux sens — 5 trop grands, 5 trop petits — de sorte qu'une spécification incomplète donne un résultat plausible mais faux, et non une erreur visible.

### Pour aller plus loin

- Refaire la demande dans un second langage et vérifier que les deux composants renvoient le même nombre.
- Ajouter une tolérance asymétrique, +2 / −1, et mesurer ce que la spécification doit gagner en précision.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-01_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-01_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-01.json` | Descripteur pour le plugin Magpie |
| `IA-01_fiche.md` | La présente fiche |
| `IA-01_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-01_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-01_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
