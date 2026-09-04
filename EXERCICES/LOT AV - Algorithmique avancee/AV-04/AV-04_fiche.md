# AV-04 — Ce qui met fin à la boucle

**Fiche d'exercice Magpie** · Lot AV — Algorithmique avancée

| | |
|---|---|
| **Thématique** | AV1 · Boucles et itération |
| **Référence au référentiel** | REF-151 |
| **Compétence visée** | Déterminer le nombre de passages qu'exige un critère d'arrêt, et savoir que c'est LUI qui commande la sortie. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | AV-01 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-13 Chronomètre |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Déterminer le nombre de passages qu'exige un critère d'arrêt, et savoir que c'est lui qui commande la sortie.

### Contexte

Le tassement du remblai décroît de 15 % à chaque passe de compactage. On s'arrête quand il descend sous 5 mm.

### Énoncé

> Le tassement initial vaut 48 mm et chaque passe le réduit de 15 %. Donnez le nombre de passes nécessaires pour descendre sous 5 mm.

### Ce qui vous est fourni

Le tassement initial, le facteur de décroissance et le seuil.

### Ce qui est attendu

14 passes — la treizième laisse encore 5,80 mm.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`AV-04_sujet.gh`

### Barème

1 point si le nombre de passes est juste et arrondi au supérieur.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `AV-04_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Écrire le tassement après n passes comme un produit de facteurs.

**Étape 2.** En déduire n par le logarithme du rapport des seuils.

**Étape 3.** Arrondir au SUPÉRIEUR : une passe entamée ne compte pas à moitié.

**Étape 4.** Vérifier la valeur atteinte à n et à n − 1.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Fixer un nombre de passes à l'avance, dix par exemple, parce que « ça devrait suffire ». Il en reste alors 9,45 mm, soit près du double du toléré — et la boucle s'est arrêtée sur un compte, pas sur un état.

### Pièges fréquents

- Fixer le nombre de passes d'avance.
- Arrondir à l'inférieur, ce qui laisse le tassement au-dessus du seuil.

### Pourquoi ce jeu de données

48 mm ramenés sous 5 par un facteur 0,85 demandent exactement 14 passes : la treizième laisse 5,80 et la quatorzième 4,93. La frontière tombe donc entre deux entiers, et un arrondi au plus proche donnerait 14 — juste par hasard, ce que la variante d'énoncé permet de vérifier.

### Limite de la correction automatique

> La décroissance géométrique est une hypothèse commode. Un tassement réel ralentit autrement, et c'est le relevé qui le dit — l'exercice porte sur le critère d'arrêt, pas sur la géotechnique.

### Pour aller plus loin

- Trouver le facteur qui atteindrait le seuil en dix passes.
- Ajouter un nombre maximal de passes, et dire ce qui se produit si le critère n'est jamais atteint.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `AV-04_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `AV-04_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `AV-04.json` | Descripteur pour le plugin Magpie |
| `AV-04_fiche.md` | La présente fiche |
| `AV-04_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `AV-04_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `AV-04_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
