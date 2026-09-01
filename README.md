# MAGPIE — référentiel et exercices Grasshopper

Référentiel des notions Rhino / Grasshopper et bibliothèque d'exercices
autocorrigés pour le plugin **Magpie**, édité par RhinoForYou.

👉 **[Consulter l'application](https://magpie-project.github.io/Magpie/)**

---

## Ce que contient ce dépôt

| | |
|---|---|
| Référentiel | **142 notions**, 11 domaines, une trentaine de catégories |
| Exercices | **63** produits, en deux lots |
| Définitions Grasshopper | **124** fichiers `.gh`, sujet et corrigé |
| Fiches | Markdown et Word illustrées, sujet seul et sujet + corrigé |

### Les lots

**Lot A — Découverte des composants natifs** (49 exercices)
Un exercice par famille de composants natifs de Grasshopper pour Rhino 8.
Aucun plugin tiers.

**Lot IA — IA et assistance générative** (14 exercices)
Formuler une demande exploitable, faire produire un composant scripté,
conduire le développement d'un plugin avec un agent de code, employer
l'apprentissage automatique, appeler un modèle de langage, piloter Grasshopper
par un protocole d'agent, et vérifier ce que l'outil renvoie.

Les lots B (algorithmes combinés), C (projets appliqués) et G (exercices
gamifiés) sont spécifiés au cahier des charges mais pas encore produits.

---

## Comment sont conçus les exercices

Tous les exercices suivent la skill **magpie-conception-exercices** (`SKILL.md`),
qui s'appuie sur la recherche en sciences de l'apprentissage. En pratique :

- **Un exercice teste une compétence, pas une connaissance.** Dix items dont la
  réponse s'obtenait en *sachant* plutôt qu'en *construisant* ont été requalifiés
  en **questions charnières** : ils ne sont pas notés, et chacune de leurs
  mauvaises réponses est diagnostique.
- **Aucune consigne ne nomme de composant.** Nommer l'outil, c'est donner la
  réponse ; la liste des composants figure côté corrigé uniquement.
- **Chaque exercice porte un contexte métier en une phrase** — réception de lot,
  calepinage de bardage, débit d'atelier, haubanage, platine d'assemblage.
- **Les jeux de données sont longs, non ordonnés et non devinables** : 24 à 36
  valeurs plutôt que des listes lisibles à l'œil.
- **Chaque exercice anticipe son erreur attendue**, choisie pour dire ce que
  l'apprenant a mal compris là où un simple « faux » ne dirait rien.

### Deux règles structurantes des fichiers `.gh`

1. **Aucun câble ne relie la zone sujet à la zone corrigé.** Les données
   fournies sont recopiées dans le corrigé, qui est donc autonome.
2. **Le corrigé ne produit rien tant qu'un interrupteur n'est pas basculé.**
   Remis sur faux, le résultat disparaît.

Les deux règles sont vérifiées automatiquement sur les 124 définitions.

---

## Ce qui est vérifié, et comment

Les valeurs attendues ne sont **jamais déduites de tête** : elles sont relevées
en ouvrant chaque définition dans Rhino, en basculant l'interrupteur et en
lisant la sortie. Trois contrôles rejouables :

```bash
python Documentation/Generateurs/audit_skill.py --fusion   # conformité à la skill
python Documentation/Generateurs/controle_reponses.py      # réponses recalculées
python Documentation/Generateurs/verifier_fraicheur.py     # cohérence des livrables
```

---

## Limites connues

- **Le checker Magpie ne compare que des nombres.** Les exercices dont le
  livrable est un texte, un plugin ou une conversation sont déclarés hors
  correction automatique et le disent explicitement, plutôt que d'être tordus
  pour entrer dans l'outil.
- **IA-07** n'a pas de définition Grasshopper : son livrable est un plugin
  `.gha` compilé.
- **Les lots B, C et G** n'ont pas encore de recettes de construction.

---

## Organisation

```text
index.html                       l'application, servie par GitHub Pages
EXERCICES/                       les deux lots produits
Documentation/                   cahier des charges, générateurs, journal
Fondamentaux Grasshopper - IndB  le référentiel au format Excel
SKILL.md                         la skill de conception des exercices
REPRISE_SESSION.md               état du projet et décisions prises
```

---

## Auteurs

Prototype et conception d'origine : **Jérémy CAROLUS**.
Référentiel, lots d'exercices et application : **Charles THIERRY DE VILLE D'AVRAY**.
Édition : **RhinoForYou**.
