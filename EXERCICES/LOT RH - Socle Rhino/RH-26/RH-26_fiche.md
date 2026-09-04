# RH-26 — Le poids du fichier à envoyer

**Fiche d'exercice Magpie** · Lot RH — Socle Rhino

| | |
|---|---|
| **Thématique** | RH5 · Préparation à l'impression 3D |
| **Référence au référentiel** | REF-022, REF-023, REF-024 |
| **Compétence visée** | Prévoir le poids d'un export maillé à partir du nombre de triangles et du format retenu. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | RH-22 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-05 La collection de badges |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Prévoir le poids d'un export maillé à partir du nombre de triangles et du format retenu.

### Contexte

Un STL s'envoie à un prestataire. Savoir avant l'export s'il fera sept mégaoctets ou trente-cinq décide du format et du moyen de transmission.

### Énoncé

> Le maillage compte 148 520 triangles. Un STL binaire pèse 84 octets d'en-tête plus 50 octets par triangle. Donnez le poids du fichier, en octets.

### Ce qui vous est fourni

Le nombre de triangles du maillage et la structure du format.

### Ce qui est attendu

7 426 084 octets, soit 7,08 Mo.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`RH-26_sujet.gh`

### Barème

1 point si le poids est exact à l'octet.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `RH-26_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Multiplier le nombre de triangles par cinquante.

**Étape 2.** Ajouter les quatre-vingt-quatre octets d'en-tête.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Exporter en STL ASCII sans y penser : environ 35 Mo pour le même maillage, cinq fois plus lourd, pour une géométrie strictement identique. Le format par défaut de la boîte de dialogue n'est pas toujours le binaire.

### Pièges fréquents

- Oublier l'en-tête.
- Confondre octets et bits, ou mégaoctets et mébioctets.

### Pourquoi ce jeu de données

148 520 triangles est un maillage de pièce courante, ni trivial ni monstrueux. La structure du binaire est FIXE — 84 + 50 n —, ce qui rend le calcul exact et vérifiable à l'octet près, là où l'ASCII ne peut s'estimer.

### Limite de la correction automatique

> La formule vaut pour le STL BINAIRE, dont chaque triangle occupe exactement cinquante octets. L'OBJ, le 3MF et le PLY ont des structures différentes, et le 3MF est compressé : son poids dépend de la géométrie elle-même.

### Pour aller plus loin

- Donner le nombre de triangles tenant dans une pièce jointe de 10 Mo.
- Comparer au poids du même maillage en 3MF.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `RH-26_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `RH-26_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `RH-26.json` | Descripteur pour le plugin Magpie |
| `RH-26_fiche.md` | La présente fiche |
| `RH-26_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `RH-26_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `RH-26_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
