# MAGPIE — référentiel et exercices Grasshopper

Référentiel des notions Rhino / Grasshopper et bibliothèque d'exercices
autocorrigés pour le plugin **Magpie**, édité par RhinoForYou.

👉 **[Consulter l'application](https://ctdvda-blip.github.io/magpie-referentiel/)**
— accès réservé, identifiant et mot de passe communiqués séparément.

Version `v0.5-260902` · référentiel Ind. C

---

## Ce que contient ce dépôt

| | |
|---|---|
| Référentiel | **160 notions**, 11 domaines, 41 catégories |
| Exercices | **253**, en quatorze lots |
| Définitions Grasshopper | **492** fichiers `.gh` — sujet et corrigé pour 246 exercices |
| Fiches | Markdown, Word illustrées et PDF, sujet seul et sujet + corrigé |
| Durée cible cumulée | 90,5 h |

Chaque notion du référentiel est couverte, **aucune catégorie ne porte moins
de trois notions**, et **aucune n'a moins d'exercices qu'elle n'a de
notions**. La catégorie la moins servie en compte 1,25 par notion.

### Les quatorze lots

| Lot | | Exercices |
|---|---|---|
| **A** | Découverte des composants natifs | 51 |
| **IA** | IA et assistance générative | 33 |
| **RH** | Socle Rhino | 32 |
| **G** | Exercices gamifiés | 32 |
| **B** | Algorithmes combinés | 18 |
| **PL** | Écosystème de plugins | 16 |
| **GP** | Géométrie paramétrique appliquée | 13 |
| **C** | Projets appliqués | 12 |
| **WB** | Interfaces, web et interopérabilité | 11 |
| **AV** | Algorithmique avancée | 9 |
| **DV** | Développement, scripting et API | 9 |
| **QT** | Quantitatifs, chiffrage et export | 6 |
| **FA** | Aide à la fabrication | 6 |
| **MP** | Méthode, performance et évènements | 5 |

Les quatorze lots sont produits. Le référentiel spécifié au cahier des
charges est entièrement construit, et quatre vagues d'équilibrage ont comblé
les catégories les plus maigres.

---

## Comment sont conçus les exercices

Tous les exercices suivent la skill **magpie-conception-exercices**
(`SKILL.md`), qui s'appuie sur la recherche en sciences de l'apprentissage. En
pratique :

- **Un exercice teste une compétence, pas une connaissance.** Trente-quatre
  items dont la réponse s'obtient en *sachant* plutôt qu'en *construisant*
  sont des **questions charnières** : chacune de leurs mauvaises réponses est
  diagnostique. Leur bonne réponse est répartie sur les quatre positions —
  9 en a, 8 en b, 8 en c, 9 en d — pour qu'un apprenant qui coche toujours la
  même lettre n'obtienne rien.
- **Aucune consigne ne nomme de composant.** Nommer l'outil, c'est donner la
  réponse ; la liste des composants figure côté corrigé uniquement.
- **Chaque exercice porte un contexte métier en une phrase** — réception de
  lot, calepinage de bardage, débit d'atelier, développé de tôle, plateau de
  fabrication additive, dimensionnement d'un service de calcul distant.
- **Les jeux de données sont longs, non ordonnés et non devinables.**
- **Chaque exercice anticipe son erreur attendue**, choisie pour produire une
  valeur DIFFÉRENTE de la bonne — donc lisible — là où un simple « faux » ne
  dirait rien.

### Deux règles structurantes des fichiers `.gh`

1. **Aucun câble ne relie le résultat de la zone sujet à la zone corrigé.** Le
   paramètre `REPONSE` reste libre de toute source : c'est l'apprenant qui l'y
   branche.
2. **Le corrigé ne produit rien tant qu'un interrupteur n'est pas basculé.**
   Remis sur faux, le résultat disparaît.

### Les exercices qui mesurent au lieu de construire

Une dizaine d'exercices demandent de modéliser dans **Rhino**. Leur définition
n'a alors rien à construire : elle **mesure**. Le sujet porte un paramètre de
référence vide et la chaîne de mesure — tant que rien n'est modélisé, rien ne
sort, et c'est le principe. Le corrigé porte la géométrie de référence
internalisée : c'est un **étalon** auquel confronter sa production, pas une
solution à recopier.

---

## Ce qui est vérifié, et comment

Les valeurs attendues ne sont **jamais posées de tête**. Elles sont recalculées
depuis leurs jeux de données, puis relevées en ouvrant chaque définition dans
Rhino, en basculant l'interrupteur et en lisant la sortie. Les deux doivent
concorder.

```bash
python Documentation/Generateurs/verifier_fraicheur.py   # cohérence des livrables
python Documentation/Generateurs/couverture.py           # couverture du référentiel
python Documentation/Generateurs/verifier_vague1.py      # réponses recalculées
python Documentation/Generateurs/verifier_vague2.py      # réponses recalculées
python Documentation/Generateurs/verifier_vague3.py      # réponses recalculées
python Documentation/Generateurs/verifier_liens.py <dossier>   # liens de la page
```

Et, dans Rhino, par le pont TCP (`Documentation/Generateurs/GH/`) :

```bash
python client_pont_rhino.py recette_6_tous_lots.py   # structure des définitions
python client_pont_rhino.py recette_7_valeurs.py     # non-régression des valeurs
```

La recette 7 fige la valeur rendue par chaque corrigé et la recompare : c'est
elle qui attrape le défaut le plus discret, celui d'une définition qui change
de réponse sans que rien ne le signale.

La recette 8 n'a pas besoin de Rhino : elle vérifie qu'à l'intérieur d'une
recette, un nom ne désigne qu'un seul objet. Un nom réemployé écrase le
premier et déplace des fils sans rien signaler — c'est ce qui a fait répondre
0,0034 m à C-02 au lieu de 695,53.

```bash
python Documentation/Generateurs/GH/recette_8_noms_uniques.py
```

---

## Deux dépôts, deux usages

Le même README accompagne les deux : ils ne portent pas la même chose.

| | |
|---|---|
| **Dépôt du projet** | de quoi **fabriquer** — les 86 modules de la chaîne de génération, la documentation, les 506 fiches Markdown, les 246 descripteurs et les 492 définitions `.gh`. Les 280 Mo de fiches Word, de PDF et d'images n'y sont pas : tous portent un horodatage interne ou sont refabriqués à chaque passe. |
| **`ctdvda-blip/magpie-referentiel`** | de quoi **consulter** — les livrables complets, PDF et Word compris, dans une arborescence aplatie pour la limite de chemin de Windows, avec l'application `index.html`. |

Depuis le dépôt du projet, tout ce qui manque se reconstitue :

```bash
python Documentation/Generateurs/finaliser.py
```

### Deux points à connaître avant de cloner

- **Les chemins sont longs.** Les lots A et IA nomment leurs dossiers par le
  titre complet de l'exercice, et un clone posé quelques niveaux trop bas
  échoue avec « Filename too long ». Clonez près de la racine, ou activez les
  chemins longs :

  ```bash
  git config --global core.longpaths true
  ```

- **Les définitions `.gh` sont binaires**, et `.gitattributes` le déclare.
  Sans cette déclaration, git peut leur appliquer une conversion de fin de
  ligne qui les corrompt sans rien signaler : le fichier s'ouvre encore, et
  son contenu a changé.

---

## Limites connues

- **Le checker Magpie ne compare que des nombres.** Un booléen ou un texte
  branché sur `REPONSE` échoue. Les exercices concernés rendent un comptage ou
  un indicateur numérique — ce qui reste une étape naturelle de la tâche, pas
  une gymnastique imposée par l'outil.
- **Sept exercices n'ont pas de définition Grasshopper** : IA-07, PL-03, MP-01,
  DV-04, DV-07, WB-01, WB-02. Leur livrable est un plugin compilé, un
  configurateur en ligne ou une définition remaniée par l'apprenant. Ils se
  notent sur grille, et leur en fabriquer une reviendrait à livrer le travail
  demandé.
- **La protection de l'application est une porte, pas un coffre.** Elle garde
  la consultation ; le dépôt est public et chaque fichier reste atteignable par
  son adresse directe.

---

## Organisation

```text
index.html                       l'application, servie par GitHub Pages
VERSION                          le numéro logique de la version courante
EXERCICES/                       les quatorze lots produits
Documentation/                   cahier des charges, guide, planning, générateurs
Journal des modifications/       ce qui a été fait, jour par jour
Fondamentaux Grasshopper - IndC  le référentiel au format Excel
SKILL.md                         la skill de conception des exercices
REPRISE_SESSION.md               état du projet et décisions prises
```

---

## Auteurs

Prototype et conception d'origine : **Jérémy CAROLUS**.
Référentiel, lots d'exercices et application : **Charles THIERRY DE VILLE D'AVRAY**.
Édition : **RhinoForYou**.
