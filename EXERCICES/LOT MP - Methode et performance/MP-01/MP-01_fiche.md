# MP-01 — Une définition qu'un autre peut reprendre

**Fiche d'exercice Magpie** · Lot MP — Méthode, performance et évènements

| | |
|---|---|
| **Thématique** | MP1 · Organisation et lisibilité |
| **Référence au référentiel** | REF-088 |
| **Compétence visée** | Organiser une définition pour qu'un tiers la reprenne sans explication orale. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | A-31 |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-18 Duel de versions |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Organiser une définition pour qu'un tiers la reprenne sans explication orale.

### Contexte

Vous partez en congés et la définition doit vivre sans vous.

### Énoncé

> Reprenez une de vos définitions et rendez-la reprenable : entrées rassemblées et nommées, étapes groupées et titrées, sorties identifiées. Faites-la relire par quelqu'un qui ne l'a pas écrite, sans un mot d'explication.

### Ce qui vous est fourni

Une définition existante, fonctionnelle mais non organisée.

### Ce qui est attendu

Une définition dont un tiers retrouve seul les entrées, la logique et les sorties.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **Visuel**.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`MP-01_sujet.gh`

### Barème

Grille : entrées rassemblées (1), groupes titrés par intention (2), reprise réussie par un tiers (2).

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `MP-01_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Rassembler toutes les entrées réglables au même endroit, à gauche, et les nommer par ce qu'elles représentent.

**Étape 2.** Grouper les étapes par intention — « répartir les montants » — et non par famille de composant.

**Étape 3.** Titrer chaque groupe d'une phrase, pas d'un mot.

**Étape 4.** Identifier les sorties et les isoler.

**Étape 5.** Faire l'essai de reprise par un tiers, en silence.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Ajouter des commentaires partout au lieu de structurer. Un scribble sur chaque composant n'est pas de la lisibilité, c'est du bruit : ce qui se lit, c'est un groupe titré par ce qu'il fait, pas par le composant qu'il contient.

### Pièges fréquents

- Titrer les groupes du nom des composants qu'ils contiennent : cela n'apprend rien à qui lit.
- Laisser des composants orphelins hors de tout groupe : ils font douter de ce qui est actif.

### Pourquoi ce jeu de données

—

### Limite de la correction automatique

> La lisibilité ne se mesure pas par un nombre. Le seul contrôle honnête est celui que l'énoncé prescrit : quelqu'un d'autre reprend la définition, ou n'y arrive pas.

### Pour aller plus loin

- Reprendre une définition d'un collègue et mesurer le temps qu'il vous faut pour la comprendre.
- Rédiger la notice d'une page qui l'accompagne.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `MP-01_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `MP-01_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `MP-01.json` | Descripteur pour le plugin Magpie |
| `MP-01_fiche.md` | La présente fiche |
| `MP-01_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `MP-01_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `MP-01_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
