# IA-17 — Une commande cachée dans un courriel

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA6 · Modèles de langage et IA générative |
| **Référence au référentiel** | REF-134 |
| **Compétence visée** | Extraire d'un texte libre les données chiffrées qui engagent, en distinguant ce qui est commandé de ce qui est seulement évoqué. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | IA-11 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-18 Dictée technique |
| **Version** | v0.4-260901 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Extraire d'un texte libre les données chiffrées qui engagent, en distinguant ce qui est commandé de ce qui est seulement évoqué.

### Contexte

Le conducteur de travaux commande sa quincaillerie par courriel, en une phrase par ligne et sans tableau. La commande doit en sortir chiffrée.

### Énoncé

> Le courriel vous est fourni tel qu'il a été reçu. Donnez le nombre total de pièces réellement commandées.

### Ce qui vous est fourni

Le courriel du conducteur de travaux, en texte libre.

### Ce qui est attendu

96 pièces — 24 paumelles, 48 vis, 18 poignées et 6 serrures.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-17_sujet.gh`

### Barème

1 point si le total est juste.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-17_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Repérer chaque article cité et la quantité qui l'accompagne.

**Étape 2.** Convertir les quantités écrites en lettres.

**Étape 3.** Repérer les corrections : la dernière valeur annoncée remplace la précédente, elle ne s'y ajoute pas.

**Étape 4.** Écarter ce qui n'est pas une commande.

**Étape 5.** Sommer.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Additionner tout ce qui ressemble à une quantité. On obtient alors 138 : les 30 crémones d'une demande de PRIX y sont comptées comme commandées, et les poignées le sont deux fois, à leur valeur annoncée puis à leur valeur corrigée. Une extraction qui ne distingue pas l'intention du chiffre produit une commande fausse — et personne ne relit une commande produite automatiquement.

### Pièges fréquents

- Ignorer la quantité écrite en toutes lettres.
- Additionner la valeur annoncée et sa correction.
- Commander ce qui faisait l'objet d'une demande de prix.

### Pourquoi ce jeu de données

Le courriel porte trois pièges distincts, et un seul de chaque sorte : une quantité écrite en toutes lettres (que la lecture naïve ignore, donnant 48), une correction plus bas dans le message (qui invite au double comptage), et une demande de prix (qui invite à commander). Les quatre résultats possibles — 96, 48, 108 et 138 — sont tous distincts, donc chaque erreur se lit sans ambiguïté.

### Limite de la correction automatique

> L'exercice valide un total, pas la structure extraite. Une extraction juste au total peut avoir mal attribué les quantités : le formateur regarde la table, pas seulement la somme.

### Pour aller plus loin

- Rendre la table structurée article par article, et non le seul total.
- Reprendre le même courriel avec deux corrections successives sur le même article.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-17_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-17_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-17.json` | Descripteur pour le plugin Magpie |
| `IA-17_fiche.md` | La présente fiche |
| `IA-17_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-17_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-17_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
