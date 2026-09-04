# WB-10 — Ce qu'un format d'échange laisse en route

**Fiche d'exercice Magpie** · Lot WB — Interfaces, web et interopérabilité

| | |
|---|---|
| **Thématique** | WB3 · Interopérabilité |
| **Référence au référentiel** | REF-111, REF-112, REF-158 |
| **Compétence visée** | Savoir, avant d'exporter, quelles propriétés du modèle le format retenu ne transportera pas. |
| **Case Bloom (révisée)** | Analyser × factuelle |
| **Niveau** | Perfectionnement |
| **Durée cible** | 15 min |
| **Prérequis** | WB-09 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-18 Vrai ou faux à élimination |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Savoir, avant d'exporter, quelles propriétés du modèle le format retenu ne transportera pas.

### Contexte

Transmettre un modèle à un bureau d'études, c'est choisir ce qu'on accepte de perdre. Le choix se fait avant l'export, pas quand le destinataire signale que les calques ont disparu.

### Énoncé

> Le tableau donne, pour huit propriétés du modèle, les formats qui les transportent. Donnez le nombre de propriétés perdues par un export au format STEP.

### Ce qui vous est fourni

Le tableau des huit propriétés et des formats qui les portent.

### Ce qui est attendu

5 propriétés sur 8 sont perdues par un export STEP.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **SingleValue**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`WB-10_sujet.gh`

### Barème

1 point si le compte est exact.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `WB-10_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Pour chaque propriété, chercher si STEP figure dans sa liste.

**Étape 2.** Prendre la négation.

**Étape 3.** Compter les propriétés retenues.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Compter ce que STEP CONSERVE — trois — en croyant répondre. La question porte sur la perte, et c'est elle qui décide : un modèle exporté en STEP arrive sans matériaux, sans blocs, sans historique, sans couleurs d'objet et sans maillages.

### Pièges fréquents

- Compter les propriétés conservées.
- Oublier qu'une propriété peut être portée par plusieurs formats.

### Pourquoi ce jeu de données

Huit propriétés et cinq formats. Le 3DM les porte toutes, ce qui donne au tableau son point de comparaison ; aucun autre format n'en porte plus de quatre, et les pertes diffèrent d'un format à l'autre — DWG en perd quatre, mais pas les mêmes.

### Limite de la correction automatique

> Le tableau raisonne par PROPRIÉTÉ, pas par fidélité. Un STEP transporte la géométrie NURBS, mais un échange réel dégrade aussi les tolérances et peut casser des surfaces trimées : la propriété survit, sa qualité pas toujours.

### Pour aller plus loin

- Refaire le compte pour DWG, puis pour OBJ.
- Chercher le format qui préserve le plus de propriétés après le 3DM.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `WB-10_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `WB-10_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `WB-10.json` | Descripteur pour le plugin Magpie |
| `WB-10_fiche.md` | La présente fiche |
| `WB-10_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `WB-10_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `WB-10_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
