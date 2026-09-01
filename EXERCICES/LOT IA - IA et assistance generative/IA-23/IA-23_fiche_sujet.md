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
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
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

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
