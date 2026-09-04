# A-51 — Le repère qui arrive en tête

**Fiche d'exercice Magpie** · Lot A — Découverte des composants natifs

| | |
|---|---|
| **Thématique** | A2 · Types et conversion implicite |
| **Référence au référentiel** | REF-145 |
| **Compétence visée** | Reconnaître qu'un tri dépend du TYPE des valeurs triées, et pas seulement de leur apparence. |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | A-06 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-14 Question éclair |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Reconnaître qu'un tri dépend du type des valeurs triées, et pas seulement de leur apparence.

### Contexte

Les repères de pièces sortent d'un tableur, où ils sont du texte. Le bon de débit les veut dans l'ordre.

### Énoncé

> Les douze repères vous sont fournis tels qu'ils arrivent du tableur : ce sont des chaînes de caractères. Triés en l'état, donnez le repère qui arrive en tête.

### Ce qui vous est fourni

Les douze repères, sous forme de texte.

### Ce qui est attendu

10 — c'est ce repère qui arrive en tête d'un tri de TEXTE.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`A-51_sujet.gh`

### Barème

1 point si le repère de tête du tri de texte est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `A-51_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Trier les repères tels qu'ils sont, en texte.

**Étape 2.** Prendre le premier.

**Étape 3.** Refaire le tri après conversion en nombres, et comparer.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Répondre 2, le plus petit nombre. Un tri de texte compare caractère par caractère : « 1 » vient avant « 2 », donc 10 et 100 précèdent 2. Sur un bon de débit, les pièces sortent alors dans un ordre qui n'est celui de personne.

### Pièges fréquents

- Répondre par le plus petit nombre.
- Supposer qu'un tri « comprend » ce que les valeurs représentent.

### Pourquoi ce jeu de données

Douze repères de 2 à 100, choisis pour que les deux tris donnent des têtes DIFFÉRENTES — 10 contre 2 — et des queues différentes aussi : 9 contre 100. Aucune des deux réponses n'est absurde à l'œil, et c'est précisément pourquoi l'erreur passe.

### Limite de la correction automatique

> L'exercice montre le symptôme. Le remède — convertir avant de trier — se pose en amont, au moment de la lecture du tableur, et pas au moment du tri.

### Pour aller plus loin

- Donner aussi le repère qui arrive en queue dans chaque tri.
- Compter combien de repères changent de place entre les deux tris.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `A-51_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `A-51_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `A-51.json` | Descripteur pour le plugin Magpie |
| `A-51_fiche.md` | La présente fiche |
| `A-51_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `A-51_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `A-51_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
