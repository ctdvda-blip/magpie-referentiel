# IA-32 — Ce qu'une demande floue laisse passer

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA1 · Formuler et cadrer une demande |
| **Référence au référentiel** | REF-117, REF-119 |
| **Compétence visée** | Mesurer l'écart entre plusieurs lectures défendables d'une même consigne, pour comprendre ce qu'une spécification doit trancher. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | IA-01 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 12 composants |
| **Gamification associée** | G-17 Le quiz éclair |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Mesurer l'écart entre plusieurs lectures défendables d'une même consigne, pour comprendre ce qu'une spécification doit trancher.

### Contexte

« Compte les grandes valeurs » se lit de quatre façons. L'assistant en choisit une, silencieusement, et le résultat est juste au regard de sa lecture.

### Énoncé

> La consigne dit « compte les grandes valeurs » sur les seize relevés fournis. Appliquez-lui quatre lectures : strictement au-dessus de 500, au moins 500, au-dessus de la moyenne, au-dessus de la médiane. Donnez les quatre comptes, dans cet ordre.

### Ce qui vous est fourni

Les seize relevés et les quatre lectures à appliquer.

### Ce qui est attendu

Les quatre comptes, dans l'ordre : 7, 8, 9, 8.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **ExactOrderedList**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-32_sujet.gh`

### Barème

1 point si les quatre comptes concordent dans l'ordre.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-32_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Compter les valeurs strictement au-dessus de 500.

**Étape 2.** Recommencer avec la comparaison large.

**Étape 3.** Calculer la moyenne, puis compter au-dessus.

**Étape 4.** Trier pour obtenir la médiane, puis compter au-dessus.

**Étape 5.** Assembler les quatre comptes dans l'ordre.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Croire que la question du seuil strict est théorique. Un relevé vaut EXACTEMENT 500 : c'est lui qui sépare les deux premières lectures, et c'est le cas limite qu'une spécification doit nommer explicitement.

### Pièges fréquents

- Confondre moyenne et médiane.
- Employer la même comparaison pour les deux premières lectures.

### Pourquoi ce jeu de données

Seize relevés de 100 à 999, dont un posé exactement au seuil. La moyenne, 472,81, et la médiane, 491,50, encadrent le seuil de 500 sans coïncider avec lui : les quatre lectures donnent trois comptes différents, et aucune n'est plus légitime que les autres.

### Limite de la correction automatique

> Quatre lectures ne sont pas toutes les lectures. « Grande » peut aussi vouloir dire au-dessus du troisième quartile, ou au-dessus d'un seuil métier absent des données : l'exercice montre le problème, il n'en épuise pas les cas.

### Pour aller plus loin

- Ajouter un second relevé à 500 et refaire les quatre comptes.
- Rédiger la spécification qui lèverait l'ambiguïté.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-32_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-32_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-32.json` | Descripteur pour le plugin Magpie |
| `IA-32_fiche.md` | La présente fiche |
| `IA-32_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-32_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-32_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
