# WB-04 — Ce qu'on expose, et ce qu'on cache

**Fiche d'exercice Magpie** · Lot WB — Interfaces, web et interopérabilité

| | |
|---|---|
| **Thématique** | WB1 · Interfaces utilisateur |
| **Référence au référentiel** | REF-107 |
| **Compétence visée** | Distinguer, parmi les entrées d'une définition, celles qui relèvent d'un choix de l'utilisateur de celles qui se déduisent ou qui règlent l'outil. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | WB-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-17 Passation |
| **Version** | v0.4-260828 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Distinguer, parmi les entrées d'une définition, celles qui relèvent d'un choix de l'utilisateur de celles qui se déduisent ou qui règlent l'outil.

### Contexte

La définition va être pilotée depuis Rhino par quelqu'un qui n'ouvrira jamais le graphe. Tout ce qu'on expose, il faudra le lui expliquer ; tout ce qu'on cache, il ne pourra plus le régler.

### Énoncé

> La définition du meuble compte quatorze entrées, décrites une à une avec ce qu'elles commandent et ce dont elles dépendent. Donnez le nombre d'entrées à exposer dans l'interface.

### Ce qui vous est fourni

La liste des quatorze entrées et leur description.

### Ce qui est attendu

6 — les six entrées qui relèvent d'un choix du client.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`WB-04_sujet.gh`

### Barème

1 point si le compte est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `WB-04_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Classer chaque entrée : choix, grandeur dérivée, ou réglage interne.

**Étape 2.** Écarter les réglages internes : ils appartiennent à l'auteur de la définition.

**Étape 3.** Écarter les grandeurs dérivées : les exposer autoriserait des saisies contradictoires.

**Étape 4.** Compter ce qui reste.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Exposer les quatorze. L'utilisateur peut alors régler la tolérance de couture et la graine aléatoire du placage, et surtout saisir une hauteur de tiroir incompatible avec la hauteur du meuble : trois entrées se DÉDUISENT des autres, et les exposer revient à autoriser deux vérités contradictoires dans la même définition.

### Pièges fréquents

- Exposer tout ce qui est un curseur.
- Exposer une grandeur dérivée « pour laisser le choix », et créer une incohérence silencieuse.
- Cacher un vrai choix parce qu'il a une valeur par défaut raisonnable.

### Pourquoi ce jeu de données

Quatorze entrées : six choix, trois grandeurs dérivées, cinq réglages internes. Les trois familles donnent trois réponses distinctes — 6, 9 et 14 — donc trois erreurs lisibles. Les dérivées sont le vrai discriminant : les repérer demande de lire les dépendances, pas seulement les intitulés.

### Limite de la correction automatique

> L'exercice valide un compte, pas une interface. Une interface à six champs mal nommés est aussi inutilisable qu'une interface à quatorze : le nommage se juge en WB-01.

### Pour aller plus loin

- Nommer les six entrées en langage client et poser leurs bornes.
- Faire piloter la définition par quelqu'un qui ne connaît pas Grasshopper, et relever ce qu'il demande.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `WB-04_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `WB-04_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `WB-04.json` | Descripteur pour le plugin Magpie |
| `WB-04_fiche.md` | La présente fiche |
| `WB-04_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `WB-04_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `WB-04_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
