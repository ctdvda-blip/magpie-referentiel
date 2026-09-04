# CAHIER DES CHARGES — EXERCICES MAGPIE

**Bibliothèque d'exercices Grasshopper autocorrigés pour Rhino 8**

| | |
|---|---|
| Projet | MAGPIE — outil d'exercices Grasshopper autocorrigés (RhinoForYou) |
| Document | Cahier des charges de la bibliothèque d'exercices |
| Version | **v0.3-260826** — **Ind. B** |
| Date | 26/08/2026 |
| Rédacteur | Charles THIERRY DE VILLE D'AVRAY |
| Destinataires | Jérémy CAROLUS, Jacques HABABOU |
| Documents de référence | *Fondamentaux Grasshopper – Ind. B – 26-08-2026.xlsx*, *Compte rendu de session du 11/08/2026*, *Trame de suivi projet Magpie.xlsx*, programmes de formation du catalogue RhinoForYou |
| Statut | Pour revue |

Ce document décrit **211 exercices** répartis en 4 lots et 74 thématiques. Chaque exercice est décrit selon une trame identique en 10 rubriques, afin que la production puisse être répartie entre plusieurs contributeurs sans perte d'homogénéité.

---

## Sommaire

1. [Objet et périmètre](#1-objet-et-périmètre)
2. [Principes pédagogiques](#2-principes-pédagogiques)
3. [Structure imposée du fichier Grasshopper](#3-structure-imposée-du-fichier-grasshopper)
4. [Conventions techniques](#4-conventions-techniques)
5. [Modes de validation et métriques](#5-modes-de-validation-et-métriques)
6. [Trame standard d'une fiche d'exercice](#6-trame-standard-dune-fiche-dexercice)
7. [Nommage et arborescence des livrables](#7-nommage-et-arborescence-des-livrables)
8. [Catalogue des exercices](#8-catalogue-des-exercices)
    - [Lot A — Découverte des composants natifs](#lot-a--découverte-des-composants-natifs) — 49 exercices
    - [Lot IA — IA et assistance générative](#lot-ia--ia-et-assistance-générative) — 25 exercices
    - [Lot RH — Socle Rhino](#lot-rh--socle-rhino) — 22 exercices
    - [Lot GP — Géométrie paramétrique appliquée](#lot-gp--géométrie-paramétrique-appliquée) — 8 exercices
    - [Lot QT — Quantitatifs, chiffrage et export](#lot-qt--quantitatifs,-chiffrage-et-export) — 6 exercices
    - [Lot FA — Aide à la fabrication](#lot-fa--aide-à-la-fabrication) — 4 exercices
    - [Lot PL — Écosystème de plugins](#lot-pl--écosystème-de-plugins) — 12 exercices
    - [Lot MP — Méthode, performance et évènements](#lot-mp--méthode,-performance-et-évènements) — 4 exercices
    - [Lot AV — Algorithmique avancée](#lot-av--algorithmique-avancée) — 3 exercices
    - [Lot DV — Développement, scripting et API](#lot-dv--développement,-scripting-et-api) — 9 exercices
    - [Lot WB — Interfaces, web et interopérabilité](#lot-wb--interfaces,-web-et-interopérabilité) — 7 exercices
    - [Lot B — Algorithmes combinés](#lot-b--algorithmes-combinés) — 18 exercices
    - [Lot C — Projets appliqués](#lot-c--projets-appliqués) — 12 exercices
    - [Lot G — Exercices gamifiés](#lot-g--exercices-gamifiés) — 32 exercices
9. [Bibliothèque des techniques de gamification](#9-bibliothèque-des-techniques-de-gamification)
10. [Plan de production](#10-plan-de-production)
11. [Critères d'acceptation](#11-critères-dacceptation)
12. [Points ouverts](#12-points-ouverts)
13. [Annexes](#13-annexes)

---

## 1. Objet et périmètre

### 1.1 Objet

Le présent cahier des charges définit le contenu, la structure et les règles de production de la bibliothèque d'exercices Grasshopper de l'outil Magpie. Il couvre :

- les exercices simples de découverte des composants natifs de Grasshopper pour Rhino 8 ;
- les exercices intermédiaires combinant plusieurs composants ou groupes de composants pour aboutir à un algorithme solution, dans différents domaines de conception ;
- les projets complexes appliqués à l'architecture, au design de mobilier, à la joaillerie et à la fabrication ;
- un lot d'exercices gamifiés mobilisant une trentaine de techniques de jeu.

### 1.2 Ce que le document ne couvre pas

- Le développement du plugin Magpie lui-même, traité dans la trame de suivi du projet.
- Le moteur de comparaison géométrique, dont les limites actuelles sont rappelées au chapitre 5.
- Les questions de propriété intellectuelle et de licence des exercices, ouvertes à ce jour.

### 1.3 Rattachement au référentiel

Chaque exercice porte une référence explicite vers une ou plusieurs lignes du fichier *Fondamentaux Grasshopper – Ind. B – 26-08-2026.xlsx*, sous la forme `REF-nnn`. Le référentiel est unifié : un identifiant unique et continu couvre les 116 notions, sans distinction de provenance. Cette référence est la clé de traçabilité entre l'offre de formation, le référentiel de notions et les exercices.

---

## 2. Principes pédagogiques

### 2.1 Une notion, un geste, une preuve

Un exercice du lot A porte sur **une seule notion** et se valide par **un seul résultat vérifiable**. Un exercice qui ne peut pas être validé automatiquement doit être reformulé en QCM plutôt qu'en manipulation.

### 2.2 Progression par dépendance, pas par difficulté ressentie

L'ordre des exercices suit l'ordre de dépendance des notions du référentiel. Un exercice ne mobilise que des notions déjà traitées, à l'exception de son objet propre. La colonne **Prérequis** de chaque fiche matérialise cette contrainte et doit être respectée lors de la composition des parcours.

### 2.3 Réalisme des situations

À partir du lot B, chaque énoncé décrit une situation professionnelle plausible, avec des cotes, des matériaux et des contraintes réelles. Les exercices artificiels, faciles à reproduire sans comprendre, sont proscrits : la valeur de Magpie tient à sa capacité à mesurer une compétence utile.

### 2.4 Le corrigé fait partie du livrable

Chaque fichier d'exercice contient son propre corrigé commenté, placé sous la zone SUJET. L'apprenant y accède après validation ou après épuisement de ses tentatives. Le corrigé n'est pas une simple solution : il explique le raisonnement étape par étape et signale les pièges fréquents.

### 2.5 Générique d'abord, métier ensuite

Les lots A et B constituent le socle commun à tous les utilisateurs de Grasshopper. Le lot C, spécialisé par métier, ne doit être produit qu'une fois le socle testé auprès de profils réellement débutants.

### 2.6 Validation humaine obligatoire

Tout exercice, énoncé, corrigé ou illustration produit avec l'aide de l'intelligence artificielle fait l'objet d'une relecture technique et pédagogique par un formateur avant intégration à la bibliothèque.

---

## 3. Structure imposée du fichier Grasshopper

Tout fichier d'exercice `.gh` respecte la même organisation verticale sur le canvas. Cette contrainte est **impérative** : elle permet d'automatiser l'extraction de la zone sujet, de masquer le corrigé et de générer les captures d'illustration.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  BANDEAU  (y = 0)                                                        │
│  Scribble titre : « A-14 · Filtrer avec Cull Pattern »                    │
│  Scribble méta  : niveau · durée cible · réf. référentiel · version       │
├──────────────────────────────────────────────────────────────────────────┤
│  ZONE SUJET  (y = -100 à -600)          groupe nommé  ZONE_SUJET          │
│  Couleur de groupe : bleu clair (200, 220, 245)                           │
│                                                                          │
│  ├─ Scribble ÉNONCÉ  (police 16, largeur max 900 px)                      │
│  ├─ Composants de départ fournis, regroupés dans DONNEES_DE_DEPART        │
│  ├─ Emplacement de travail libre, matérialisé par un cadre pointillé      │
│  └─ Paramètre de réponse nommé  REPONSE  (bordure orange)                 │
├──────────────────────────────────────────────────────────────────────────┤
│  SÉPARATEUR : Scribble « ▼ CORRIGÉ — à consulter après validation ▼ »     │
├──────────────────────────────────────────────────────────────────────────┤
│  ZONE CORRIGÉ  (y = -800 et au-delà)    groupe nommé  ZONE_CORRIGE        │
│  Couleur de groupe : vert clair (215, 240, 215)                           │
│                                                                          │
│  ├─ Sous-groupe ÉTAPE 1 + Scribble d'explication                          │
│  ├─ Sous-groupe ÉTAPE 2 + Scribble d'explication                          │
│  ├─ …                                                                    │
│  ├─ Sous-groupe PIÈGES (couleur rouge clair) + Scribbles                  │
│  └─ Paramètre  SOLUTION_REFERENCE                                         │
└──────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Règles de la zone SUJET

| Règle | Exigence |
|---|---|
| Énoncé | Un Scribble unique, texte intégral repris à l'identique de la rubrique 3 de la fiche |
| Longueur de l'énoncé | 40 mots maximum pour le lot A, 80 mots pour les lots B et G, 120 mots pour le lot C |
| Composants de départ | Regroupés, verrouillés en position, aperçu actif |
| Données internalisées | Systématiquement, sauf géométrie lourde livrée en fichier 3DM externe |
| Paramètre de réponse | Un seul, nommé `REPONSE`, du type attendu par le mode de validation |
| État initial | Le fichier ouvert ne doit produire ni erreur ni avertissement |

### 3.2 Règles de la zone CORRIGÉ

| Règle | Exigence |
|---|---|
| Un sous-groupe par étape | Le découpage suit exactement la rubrique 6 de la fiche |
| Scribble d'explication | Placé au-dessus de chaque sous-groupe, une à trois phrases |
| Numérotation | `ÉTAPE 1`, `ÉTAPE 2`, … cohérente avec la fiche |
| Pièges | Un sous-groupe dédié, avec le montage fautif et son commentaire |
| Aperçu | Désactivé sur tous les composants du corrigé, pour ne pas polluer la vue |
| Décalage vertical | Au moins 200 px sous la zone sujet, pour un masquage fiable |

### 3.3 Deux règles structurantes

**Règle 1 — aucun câble ne relie les deux zones.** Les composants du sujet dont le corrigé a besoin y sont **recopiés**, avec leurs données internalisées, dans un groupe `DONNÉES FOURNIES (copie)` placé en tête de la zone corrigé. Le câblage interne du sujet est rejoué entre ces copies. Les deux zones sont ainsi totalement indépendantes : on peut supprimer l'une sans toucher l'autre, et aucun fil ne traverse le canvas.

**Règle 2 — le corrigé est masqué tant qu'il n'est pas demandé.** L'aperçu est coupé sur tous les composants du corrigé, et son résultat traverse un `Stream Gate` piloté par un `Boolean Toggle` nommé **AFFICHER LE CORRIGÉ**, à faux par défaut. Tant qu'il reste sur faux, la sortie est vide et **rien n'apparaît dans Rhino** ; le remettre sur faux fait disparaître le résultat. Seul le paramètre `REPONSE_CORRIGE`, en aval de la porte, a son aperçu actif.

> Limite à connaître : Grasshopper ne permet pas de faire disparaître des composants du canvas selon une valeur booléenne. Les composants du corrigé restent donc visibles sur le canvas du fichier `_complet.gh` ; c'est leur *résultat* qui est commandé par l'interrupteur. Le fichier à remettre à l'apprenant reste `_sujet.gh`, qui ne contient aucun corrigé.

### 3.4 Deux fichiers par exercice

| Fichier | Contenu | Usage |
|---|---|---|
| `<ID>_sujet.gh` | Zone bandeau et zone sujet uniquement | Chargé par Magpie pour l'apprenant |
| `<ID>_complet.gh` | Bandeau, sujet et corrigé | Support de formation, référence, génération du JSON |
| `<ID>_fiche.md` | Fiche détaillée : sujet et corrigé | Formateur, préparation de séance |
| `<ID>_fiche_sujet.md` | La même, sans le corrigé | Remise à l'apprenant |

Le fichier `_complet.gh` est la source de vérité. Le fichier `_sujet.gh` en est dérivé par suppression du groupe `ZONE_CORRIGE`.

---

## 4. Conventions techniques

### 4.1 Environnement de référence

| Élément | Valeur |
|---|---|
| Logiciel | Rhino 8 (version de service la plus récente au moment de la production) |
| Grasshopper | Version intégrée à Rhino 8 |
| Unités du document | Millimètres |
| Tolérance absolue du document | 0,001 mm |
| Tolérance angulaire | 0,1 degré |
| Langue de l'interface | Français, noms de composants en anglais |

### 4.2 Plugins autorisés par lot

| Lot | Plugins autorisés |
|---|---|
| A | Aucun. Composants natifs exclusivement. |
| B | Aucun par défaut ; un plugin nommé explicitement dans l'énoncé est autorisé (Anemone, OpenNest). |
| C | Anemone, Kangaroo, Galapagos, Weaverbird, OpenNest, LunchBox, Human, Elefront, selon l'énoncé. |
| G | Human (retour sonore et visuel), Metahopper (introspection du canvas). |

Tout plugin employé doit être mentionné dans la rubrique 2 de la fiche et signalé à l'apprenant dans le bandeau du fichier. Un exercice ne doit jamais échouer silencieusement faute de plugin installé : le fichier comporte un contrôle de présence en tête de la zone sujet.

### 4.3 Nommage sur le canvas

| Élément | Convention | Exemple |
|---|---|---|
| Groupe principal | Majuscules, sous-tirets | `ZONE_SUJET` |
| Sous-groupe d'étape | `ÉTAPE n — libellé` | `ÉTAPE 3 — Filtrage` |
| Paramètre d'entrée fourni | Majuscules | `COURBE_GUIDE` |
| Paramètre de réponse | `REPONSE` | — |
| Slider paramétrable | Nom métier, unité entre parenthèses | `Hauteur (mm)` |

### 4.4 Géométrie externe

La géométrie est internalisée dans le fichier chaque fois que la taille du fichier reste inférieure à 2 Mo. Au-delà — maillages denses, projets réels — un fichier `3DM` externe est livré avec l'exercice, référencé par un `Geometry Pipeline` sur un calque au nom normalisé. Le nom du calque attendu est indiqué dans l'énoncé.

---

## 5. Modes de validation et métriques

### 5.1 Modes de validation

| Mode | Nature du résultat | Tolérance | Emploi recommandé |
|---|---|---|---|
| `ExactOrderedList` | Liste dont l'ordre compte | Aucune | Tri, séries, entrelacement |
| `SetEquality` | Ensemble, ordre indifférent | Aucune | Filtrage, répartition, structure d'arbre |
| `SingleValue` | Valeur unique | Aucune ou numérique | Comptage, valeur calculée, booléen |
| `NumericTolerance` | Valeur numérique | Relative ou absolue | Mesures, métrés, chiffrage |
| `GeometryTolerance` | Géométrie | Absolue en mm | Construction géométrique |
| `Conceptuel (QCM)` | Choix dans une liste | Aucune | Notions non mesurables par comparaison |

### 5.2 Limite connue du moteur de comparaison

La comparaison géométrique repose actuellement sur des grandeurs globales — boîte englobante, volume, aire — assorties d'une tolérance. Cette approche convient aux exercices des lots A et B. Pour le lot C, elle est insuffisante : deux solutions de topologies différentes peuvent présenter le même volume. **Recommandation** : pour chaque exercice du lot C, définir un jeu d'au moins trois indicateurs indépendants (volume, aire développée, nombre d'éléments, position d'un point remarquable) et valider sur leur conjonction, en attendant l'évolution du moteur.

### 5.3 Métriques collectées

| Métrique | Usage | Calibration |
|---|---|---|
| Taux de réussite | Validation et déclenchement du certificat | Seuil par parcours |
| Temps total | Comparaison à une durée cible | À calibrer sur des utilisateurs réels avant activation |
| Nombre de composants | Sobriété de la solution | Comparé au champ *Solution de référence* de la fiche |
| Nombre de tentatives | Difficulté ressentie | Alimente les mécaniques de vies et d'indices |
| Écart au chemin attendu | Détection d'une solution sur-complexifiée | Tolérance de 1 à 2 composants |

### 5.4 Règle sur les durées cibles

Les durées indiquées dans les fiches sont des **estimations de conception**, non mesurées. Elles ne doivent pas être utilisées comme critère bloquant tant qu'elles n'ont pas été calibrées par des mesures réelles : d'abord auprès des formateurs, puis auprès d'un échantillon d'apprenants représentatifs.

---

## 6. Trame standard d'une fiche d'exercice

Toutes les fiches du chapitre 8 suivent strictement la trame suivante. Aucune rubrique ne peut être omise ; une rubrique sans contenu porte la mention « sans objet ».

| # | Rubrique | Contenu attendu |
|---|---|---|
| — | En-tête | Identifiant, titre, lot, thématique, référence au référentiel, niveau, durée cible, prérequis, mode de validation et tolérance, taille de la solution de référence, technique de gamification associée, statut de production |
| 1 | Objectif pédagogique | Une phrase énonçant la compétence visée, formulée du point de vue de l'apprenant |
| 2 | Composants mobilisés | Liste des composants, nom anglais, plugin indiqué le cas échéant |
| 3 | Zone SUJET — texte du Scribble | Texte exact à reporter dans le fichier `.gh`, sans reformulation |
| 4 | Données de départ fournies | Composants pré-placés, géométrie internalisée, fichier 3DM externe |
| 5 | Résultat attendu | Description non ambiguë de ce qui est comparé |
| 6 | Zone CORRIGÉ — explication étape par étape | Étapes numérotées, une action par étape, correspondant aux sous-groupes du fichier |
| 7 | Pièges fréquents | Erreurs réellement observées ou anticipées, avec leur symptôme |
| 8 | Variantes et extensions | Déclinaisons possibles pour renouveler l'exercice ou monter en difficulté |
| 9 | Mise en œuvre dans Magpie | Ce que le plugin doit faire, et le cas échéant ce qu'il ne sait pas encore faire |
| 10 | Barème | Répartition des points et seuil de validation |

---

## 7. Nommage et arborescence des livrables

```
/EXERCICES/
    /LOT A - Composants natifs/
        A-01 Premier flux de donnees/
            A-01_sujet.gh
            A-01_complet.gh
            A-01.json                  ← descripteur Magpie
            A-01_fiche.md              ← fiche detaillee : sujet ET corrige
            A-01_fiche_sujet.md        ← fiche sans le corrige, pour l'apprenant
            A-01_illustration.png
            /Ressources/               ← 3DM externes eventuels
    /LOT B - Algorithmes combines/
    /LOT C - Projets appliques/
    /LOT G - Exercices gamifies/
/PARCOURS/
    Parcours 01 - Decouverte.json
    Parcours 02 - Donnees et listes.json
/Documentation/
/Journal des modifications/
/Anciens fichiers/
```

### 7.1 Identifiant d'exercice

`<LOT>-<NN>` où `<LOT>` vaut A, B, C ou G et `<NN>` un numéro à deux chiffres. L'identifiant est **stable** : il ne change jamais, même si l'exercice est remanié. Un exercice retiré voit son identifiant réservé et non réattribué.

### 7.2 Versionnage

Chaque exercice porte une version au format `v0.1-AAMMJJ` affichée dans le bandeau du fichier `.gh` et reprise dans le descripteur JSON. La bibliothèque dans son ensemble porte un indice de révision (`Ind. A`, `Ind. B`, …) porté par le présent cahier des charges.

---

## 8. Catalogue des exercices

### 8.0 Vue d'ensemble

| Lot | Intitulé | Niveau | Nombre d'exercices | Durée cumulée |
|---|---|---|---|---|
| **A** | Découverte des composants natifs | Débutant | 49 | 5 h 31 |
| **IA** | IA et assistance générative | Débutant à perfectionnement | 25 | 9 h 46 |
| **RH** | Socle Rhino | Débutant | 22 | 6 h 21 |
| **GP** | Géométrie paramétrique appliquée | Débutant à perfectionnement | 8 | 3 h 17 |
| **QT** | Quantitatifs, chiffrage et export | Intermédiaire | 6 | 2 h 45 |
| **FA** | Aide à la fabrication | Perfectionnement | 4 | 2 h 10 |
| **PL** | Écosystème de plugins | Débutant à intermédiaire | 12 | 2 h 43 |
| **MP** | Méthode, performance et évènements | Intermédiaire à perfectionnement | 4 | 1 h 28 |
| **AV** | Algorithmique avancée | Perfectionnement | 3 | 1 h 50 |
| **DV** | Développement, scripting et API | Expert | 9 | 4 h 47 |
| **WB** | Interfaces, web et interopérabilité | Perfectionnement à expert | 7 | 4 h 03 |
| **B** | Algorithmes combinés | Intermédiaire | 18 | 7 h 59 |
| **C** | Projets appliqués | Expérimenté | 12 | 16 h 35 |
| **G** | Exercices gamifiés | Tous niveaux | 32 | 8 h 41 |
| | **Total** | | **211** | **77 h 56** |

---

## Lot A — Découverte des composants natifs

**Niveau** : Débutant · **49 exercices** · **5 h 31 cumulées**

Un exercice par famille de composants natifs de Grasshopper pour Rhino 8. Aucun plugin tiers n'est autorisé dans ce lot.

| ID | Titre | Thématique | Niveau | Durée | Validation |
|---|---|---|---|---|---|
| A-01 | Premier flux de données | A1 · Interface, flux de données et paramètres | Débutant | 5 min | SingleValue |
| A-02 | Construire un point par coordonnées | A1 · Interface, flux de données et paramètres | Débutant | 6 min | GeometryTolerance |
| A-03 | Internaliser une donnée | A1 · Interface, flux de données et paramètres | Débutant | 6 min | GeometryTolerance |
| A-04 | Référencer et cuire de la géométrie Rhino | A1 · Interface, flux de données et paramètres | Débutant | 8 min | GeometryTolerance |
| A-05 | Lire ce qui circule dans un câble | A1 · Interface, flux de données et paramètres | Débutant | 5 min | SingleValue |
| A-06 | Conversion implicite Number vers Integer | A2 · Types, conversion et valeurs | Débutant | 6 min | SingleValue |
| A-07 | Quand la conversion échoue | A2 · Types, conversion et valeurs | Débutant | 6 min | SingleValue |
| A-08 | Booléen et nombre | A2 · Types, conversion et valeurs | Débutant | 5 min | SingleValue |
| A-09 | Valeur nulle et propagation | A2 · Types, conversion et valeurs | Débutant | 7 min | SingleValue |
| A-10 | Series et Range | A3 · Listes | Débutant | 7 min | ExactOrderedList |
| A-11 | List Item et indexation | A3 · Listes | Débutant | 6 min | ExactOrderedList |
| A-12 | Longueur et bornes d'une liste | A3 · Listes | Débutant | 5 min | ExactOrderedList |
| A-13 | Trier une liste avec une clé | A3 · Listes | Débutant | 8 min | ExactOrderedList |
| A-14 | Filtrer avec Cull Pattern | A3 · Listes | Débutant | 7 min | ExactOrderedList |
| A-15 | Répartir avec Dispatch | A3 · Listes | Débutant | 7 min | SingleValue |
| A-16 | Décaler et inverser une liste | A3 · Listes | Débutant | 6 min | GeometryTolerance |
| A-17 | Fusionner et entrelacer | A3 · Listes | Débutant | 6 min | ExactOrderedList |
| A-18 | Extraire une portion de liste | A3 · Listes | Débutant | 6 min | ExactOrderedList |
| A-19 | Lire un chemin d'arbre | A4 · Arbres de données | Débutant | 7 min | SingleValue |
| A-20 | Graft et Flatten | A4 · Arbres de données | Débutant | 8 min | GeometryTolerance |
| A-21 | Nettoyer une structure | A4 · Arbres de données | Débutant | 7 min | SetEquality |
| A-22 | Construire un arbre | A4 · Arbres de données | Débutant | 8 min | SetEquality |
| A-23 | Renommer les chemins avec Path Mapper | A4 · Arbres de données | Débutant | 9 min | SetEquality |
| A-24 | Correspondance par défaut | A5 · Comportements implicites | Débutant | 7 min | SingleValue |
| A-25 | Longest List et Cross Reference | A5 · Comportements implicites | Débutant | 8 min | ExactOrderedList |
| A-26 | Ordre d'évaluation et recalcul | A5 · Comportements implicites | Débutant | 6 min | Conceptuel (QCM) |
| A-27 | Construire une chaîne de caractères | A6 · Outils de texte | Débutant | 6 min | Visuel |
| A-28 | Découper et remplacer du texte | A6 · Outils de texte | Débutant | 7 min | Visuel |
| A-29 | Comparer deux valeurs | A7 · Portes logiques | Débutant | 5 min | SingleValue |
| A-30 | Combiner plusieurs conditions | A7 · Portes logiques | Débutant | 7 min | SingleValue |
| A-31 | Orienter un flux avec une condition | A7 · Portes logiques | Débutant | 7 min | GeometryTolerance |
| A-32 | Vecteur, amplitude et direction | A8 · Géométrie vectorielle et filaire | Débutant | 7 min | GeometryTolerance |
| A-33 | Plans de construction | A8 · Géométrie vectorielle et filaire | Débutant | 7 min | GeometryTolerance |
| A-34 | Primitives filaires | A8 · Géométrie vectorielle et filaire | Débutant | 8 min | GeometryTolerance |
| A-35 | Diviser et évaluer une courbe | A8 · Géométrie vectorielle et filaire | Débutant | 8 min | GeometryTolerance |
| A-36 | Courbes passant par des points | A8 · Géométrie vectorielle et filaire | Débutant | 7 min | GeometryTolerance |
| A-37 | Déplacer par un vecteur | A9 · Transformations et réseaux | Débutant | 5 min | GeometryTolerance |
| A-38 | Rotation et symétrie | A9 · Transformations et réseaux | Débutant | 7 min | GeometryTolerance |
| A-39 | Réseaux rectangulaire et polaire | A9 · Transformations et réseaux | Débutant | 8 min | GeometryTolerance |
| A-40 | Mise à l'échelle | A9 · Transformations et réseaux | Débutant | 6 min | GeometryTolerance |
| A-41 | Extrusion et surface réglée | A10 · Surfaces et solides | Débutant | 8 min | GeometryTolerance |
| A-42 | Balayage et révolution | A10 · Surfaces et solides | Débutant | 8 min | GeometryTolerance |
| A-43 | Fermer une polysurface en solide | A10 · Surfaces et solides | Débutant | 7 min | NumericTolerance |
| A-44 | Opérations booléennes | A10 · Surfaces et solides | Débutant | 8 min | NumericTolerance |
| A-45 | Intersections entre géométries | A10 · Surfaces et solides | Débutant | 7 min | NumericTolerance |
| A-46 | Détecter une collision | A10 · Surfaces et solides | Débutant | 7 min | SetEquality |
| A-47 | Longueur, aire et volume | A11 · Mesures géométriques | Débutant | 6 min | NumericTolerance |
| A-48 | Courbure et point le plus proche | A11 · Mesures géométriques | Débutant | 7 min | NumericTolerance |
| A-49 | Centre de gravité | A11 · Mesures géométriques | Débutant | 6 min | GeometryTolerance |

### A1 · Interface, flux de données et paramètres

*5 exercices — A-01, A-02, A-03, A-04, A-05*

#### A-01 — Premier flux de données

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A1 · Interface, flux de données et paramètres |
| **Réf. référentiel** | REF-027, REF-028 |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | — |
| **Compétence visée** | Raccorder deux sources sur les deux entrées d'un même opérateur et lire la valeur produite. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Statut de production** | À produire |

**1. Compétence visée** — Raccorder deux sources sur les deux entrées d'un même opérateur et lire la valeur produite.

**1 bis. Contexte métier** — Un ensemble menuisé se compose d'une imposte et d'un châssis superposés ; leur hauteur cumulée doit remplir exactement la baie.

**2. Composants mobilisés** — Number Slider, Panel, Addition

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La baie mesure 2 400 mm de haut. Une valeur de hauteur vous est déjà fournie pour l'imposte. Ajoutez une seconde valeur réglable pour le châssis, faites-en la somme, et réglez les deux hauteurs pour que la baie soit exactement remplie.

**4. Données de départ fournies** — Un Number Slider (0-100, valeur 17) déjà placé.

**5. Résultat attendu** — La somme des deux hauteurs vaut exactement 2 400.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser un second Number Slider (menu Params > Input) et l'étendre de 0 à 100.
2. Poser un composant Addition (Maths > Operators).
3. Relier le premier slider sur l'entrée A, le second sur l'entrée B.
4. Relier la sortie R vers un Panel (Params > Input > Panel).
5. Ajuster les deux curseurs jusqu'à lire 42 dans le Panel.

**6 bis. Erreur attendue** — Brancher les deux sources sur la même entrée : l'opérateur additionne alors les deux valeurs sur une seule entrée et laisse l'autre vide. Le résultat est faux d'un facteur qui trahit la confusion entre « deux câbles » et « deux entrées ».

**7. Pièges fréquents**

- Relier deux câbles sur la même entrée A : Grasshopper additionne alors les deux valeurs sur A et laisse B vide.
- Slider réglé en entier alors que la cible demande une décimale.

**8. Variantes et extensions**

- Remplacer Addition par Subtraction et viser -42.
- Ajouter un troisième slider avec Mass Addition.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si la valeur du Panel vaut 42.

#### A-02 — Construire un point par coordonnées

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A1 · Interface, flux de données et paramètres |
| **Réf. référentiel** | REF-062 |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-01 |
| **Compétence visée** | Construire une position dans l'espace à partir de trois valeurs séparées, y compris négatives. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,01 mm |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-26 Feedback visuel immédiat |
| **Statut de production** | À produire |

**1. Compétence visée** — Construire une position dans l'espace à partir de trois valeurs séparées, y compris négatives.

**1 bis. Contexte métier** — Le géomètre communique la position d'un repère de nivellement par rapport à la borne de chantier.

**2. Composants mobilisés** — Number Slider, Construct Point, Point

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le repère se trouve à 30 m à l'est, 15 m au sud et 8 m au-dessus de la borne, laquelle est à l'origine du modèle. Placez ce repère dans le modèle à partir de trois valeurs réglables indépendantes.

**4. Données de départ fournies** — Canvas vide.

**5. Résultat attendu** — Un point unique aux coordonnées (30 ; −15 ; 8).

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser trois Number Slider et les nommer X, Y et Z (double-clic sur le nom).
2. Régler les bornes de Y de -50 à 50 pour autoriser la valeur négative.
3. Poser Construct Point (Vector > Point).
4. Relier chaque slider sur l'entrée correspondante X, Y, Z.
5. Vérifier l'aperçu du point dans la vue Rhino.

**6 bis. Erreur attendue** — Laisser la valeur nord-sud bornée aux positifs : le repère se place au nord au lieu du sud. L'erreur révèle qu'on a réglé une valeur sans vérifier l'étendue autorisée.

**7. Pièges fréquents**

- Slider borné à 0-100 : impossible d'atteindre -15.
- Confondre Construct Point et Deconstruct Point.

**8. Variantes et extensions**

- Ajouter un second point et tracer la Line entre les deux.
- Remplacer les sliders par un unique Panel multiligne.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point si le point est à moins de 0,01 mm de la cible.

#### A-03 — Internaliser une donnée

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A1 · Interface, flux de données et paramètres |
| **Réf. référentiel** | REF-027 |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-02 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-19 Le composant mystère |
| **Statut de production** | À produire |

**1. Compétence visée** — Comprendre la différence entre une donnée calculée en amont et une donnée figée dans un paramètre.

**1 bis. Contexte métier** — Un fond de plan doit être transmis à un confrère sans la chaîne de calcul qui l'a produit.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Vous figez un point dans un paramètre autonome, puis vous supprimez toute la chaîne qui l'avait produit. Le point reste affiché. Pourquoi ?
a) Grasshopper garde en mémoire le dernier calcul effectué.
b) La donnée a été recopiée dans le paramètre, qui ne dépend plus de rien. ← réponse
c) Le paramètre reconstruit le point à chaque ouverture du fichier.
d) L'affichage est un reste à l'écran, il disparaîtra au prochain recalcul.

Valeur diagnostique : (a) et (d) révèlent qu'on confond persistance et cache d'affichage ; (c) qu'on croit le paramètre encore lié à sa source. Aucune de ces confusions ne se verrait dans un exercice où le montage fonctionne.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> *Le point vert est produit par un Construct Point. Fige-le dans un paramètre Point autonome puis supprime la chaîne amont : le point doit rester affiché.*

**4. Données de départ fournies** — Un Construct Point alimenté par trois sliders.

**5. Résultat attendu** — Un paramètre Point contenant une donnée internalisée, la chaîne amont supprimée.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser un paramètre Point (Params > Geometry > Point).
2. Relier la sortie du Construct Point vers ce paramètre.
3. Clic droit sur le paramètre > Internalise data.
4. Supprimer le Construct Point et les trois sliders.
5. Vérifier que le point reste affiché : la donnée est désormais portée par le paramètre.

**7. Pièges fréquents**

- Internaliser avant que le paramètre ait reçu la donnée : le paramètre reste vide.
- Confondre Internalise data et Set One Point (saisie manuelle dans Rhino).

**8. Variantes et extensions**

- Internaliser une courbe dessinée dans Rhino.
- Comparer la taille du fichier .gh avant et après internalisation d'un maillage.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point si le point subsiste sans chaîne amont.

#### A-04 — Référencer et cuire de la géométrie Rhino

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A1 · Interface, flux de données et paramètres |
| **Réf. référentiel** | REF-026 |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-03 |
| **Compétence visée** | Faire circuler une géométrie entre Rhino et Grasshopper dans les deux sens, par calque plutôt que par sélection manuelle. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-05 Badges et trophées |
| **Statut de production** | À produire |

**1. Compétence visée** — Faire circuler une géométrie entre Rhino et Grasshopper dans les deux sens, par calque plutôt que par sélection manuelle.

**1 bis. Contexte métier** — Le géomètre a livré l'implantation des poteaux sous forme de cercles ; le bureau d'études doit en produire un calque de contrôle décalé.

**2. Composants mobilisés** — Curve (paramètre), Geometry Pipeline, Bake (menu contextuel)

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les cercles d'implantation occupent le calque « CERCLES » du fichier Rhino. Récupérez-les sans les désigner un par un — l'implantation peut encore changer — remontez-les de 50 mm, et déposez le résultat dans le modèle sur le calque « COPIES ».

**4. Données de départ fournies** — Fichier 3DM joint contenant trois cercles sur le calque CERCLES.

**5. Résultat attendu** — Trois cercles présents sur le calque COPIES, décalés de 50 mm en Z.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Geometry Pipeline (Params > Util) et saisir CERCLES dans le champ Layer.
2. Vérifier que trois courbes sont captées (survol de la sortie).
3. Poser Unit Z (Vector > Vector) et un slider réglé sur 50.
4. Poser Move et relier la géométrie et le vecteur.
5. Clic droit sur Move > Bake, choisir le calque COPIES.

**6 bis. Erreur attendue** — Désigner les cercles à la main : le montage cesse de suivre dès que le géomètre ajoute un poteau. L'erreur ne se voit pas au premier essai, seulement à la mise à jour.

**7. Pièges fréquents**

- Le Geometry Pipeline est sensible à la casse du nom de calque.
- Oublier de multiplier Unit Z par la valeur du slider : le décalage vaut 1 mm.

**8. Variantes et extensions**

- Filtrer le Pipeline par type de géométrie plutôt que par calque.
- Utiliser Elefront pour cuire avec des attributs.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point si les trois cercles sont cuits au bon niveau.

#### A-05 — Lire ce qui circule dans un câble

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A1 · Interface, flux de données et paramètres |
| **Réf. référentiel** | REF-027, REF-028 |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | A-01 |
| **Case Bloom (révisée)** | Comprendre × factuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-17 Quiz éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — Savoir inspecter un flux : nombre d'éléments, type et structure.

**1 bis. Contexte métier** — Reprise d'une définition écrite par un tiers, dont on ignore ce que transportent les liaisons.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Une liaison transporte une donnée que vous n'avez pas produite. Sans rien modifier, où lisez-vous d'un coup d'œil le nombre d'éléments qu'elle transporte, leur type et leur structure ?
a) En survolant la sortie du composant amont. ← réponse
b) En ouvrant les propriétés du composant aval.
c) En branchant obligatoirement un afficheur.
d) Cette information n'est pas accessible sans calcul.

Valeur diagnostique : (c) révèle qu'on croit devoir modifier le graphe pour l'inspecter — le réflexe qui fait casser les définitions des autres ; (d) qu'on ignore l'existence de l'infobulle.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> *Un câble transporte une donnée inconnue. Sans modifier le graphe, indique dans un Panel le nombre d'éléments qu'il transporte.*

**4. Données de départ fournies** — Un composant amont masqué produisant une liste de 12 nombres.

**5. Résultat attendu** — Un Panel affichant 12.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser un Param Viewer et le brancher sur le câble à inspecter.
2. Basculer le Param Viewer en mode texte pour lire la structure.
3. Poser List Length (Sets > List) sur le même câble.
4. Relier la sortie L vers un Panel.

**7. Pièges fréquents**

- Confondre le nombre de branches et le nombre d'éléments.
- Lire la valeur affichée par le Panel plutôt que le nombre de lignes.

**8. Variantes et extensions**

- Ajouter un Tree Statistics pour lire les chemins.
- Comparer List Length avant et après un Flatten.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le Panel affiche 12.

### A2 · Types, conversion et valeurs

*4 exercices — A-06, A-07, A-08, A-09*

#### A-06 — Conversion implicite Number vers Integer

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A2 · Types, conversion et valeurs |
| **Réf. référentiel** | REF-040 |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-01 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-18 Vrai / Faux à élimination |
| **Statut de production** | À produire |

**1. Compétence visée** — Observer qu'un composant attendant un entier arrondit silencieusement une valeur décimale.

**1 bis. Contexte métier** — Un nombre de travées calculé produit une valeur décimale, alors que le composant en aval attend un compte entier.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Une valeur décimale de 4,6 alimente une entrée qui n'accepte que des entiers. Que vaut l'entier réellement utilisé ?
a) 4 — la partie entière est conservée.
b) 5 — la valeur est toujours arrondie au supérieur.
c) 5 — la valeur est arrondie au plus proche. ← réponse
d) Le composant se met en erreur.

Valeur diagnostique : c'est la question la plus utile du lot, parce que (a) et (c) donnent tous deux la bonne réponse pour 4,6 et se trompent pour 4,4. Un apprenant qui coche (c) « réussit » et garde une règle fausse. Sur un approvisionnement — où il faut au moins autant de pièces — c'est bien un arrondi au supérieur qu'il faut, et il doit être posé explicitement : la conversion implicite ne le fera pas.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> *Le slider vaut 4,6. Il alimente l'entrée Count d'un Series qui attend un entier. Combien d'éléments la série contient-elle ? Affiche le nombre dans un Panel et explique la règle appliquée.*

**4. Données de départ fournies** — Un Number Slider décimal réglé sur 4,6 relié à Series.

**5. Résultat attendu** — Un Panel affichant 5 (arrondi au plus proche).

**6. Zone CORRIGÉ — explication étape par étape**

1. Brancher un List Length sur la sortie de Series.
2. Relier vers un Panel : la série contient 5 éléments.
3. Faire varier le slider entre 4,4 et 4,6 pour observer la bascule.
4. Conclure : Grasshopper arrondit au plus proche, il ne tronque pas.

**7. Pièges fréquents**

- Supposer une troncature (4,6 donnerait 4) : c'est faux.
- Ne pas remarquer que le survol de l'entrée affiche déjà la valeur convertie.

**8. Variantes et extensions**

- Refaire l'essai avec 4,5 puis 5,5 pour observer la règle de l'arrondi.
- Insérer un Round explicite pour rendre le comportement visible.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point pour la valeur, 1 point pour la règle énoncée en QCM.

#### A-07 — Quand la conversion échoue

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A2 · Types, conversion et valeurs |
| **Réf. référentiel** | REF-041 |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-06 |
| **Case Bloom (révisée)** | Comprendre × factuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-20 Erreur volontaire à débusquer |
| **Statut de production** | À produire |

**1. Compétence visée** — Reconnaître un composant en échec et lire le message d'erreur.

**1 bis. Contexte métier** — Une donnée saisie en toutes lettres remonte d'un tableur mal rempli.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Un composant passe en orange et sa sortie est vide. Que faites-vous en premier ?
a) Vous le supprimez et le reposez.
b) Vous survolez la pastille pour lire le message, qui nomme l'entrée fautive. ← réponse
c) Vous rebranchez toutes les entrées.
d) Vous relancez le recalcul du document.

Valeur diagnostique : (a) et (c) sont le réflexe de l'apprenant qui ne sait pas que Grasshopper dit précisément ce qui ne va pas ; l'orange signale un avertissement, pas une panne.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> *Un Panel contenant le texte « douze » alimente une Addition. Qu'affiche la sortie ? Corrige le montage pour que l'addition renvoie 15 sans supprimer le Panel.*

**4. Données de départ fournies** — Un Panel contenant « douze » relié à l'entrée A d'une Addition, un slider à 3 sur B.

**5. Résultat attendu** — Composant en orange puis, après correction, résultat 15.

**6. Zone CORRIGÉ — explication étape par étape**

1. Survoler le composant orange pour lire l'avertissement de conversion.
2. Remplacer le contenu du Panel par 12 (valeur numérique).
3. Vérifier que le composant redevient normal et affiche 15.
4. Retenir : un texte non numérique produit une valeur nulle, pas un zéro.

**7. Pièges fréquents**

- Croire qu'un échec de conversion produit 0 : il produit une valeur nulle.
- Confondre un composant orange (avertissement) et rouge (erreur).

**8. Variantes et extensions**

- Tester « 12 » entre guillemets, « 12,5 » et « 12.5 » pour observer le séparateur décimal.
- Insérer un Text To Number explicite.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point pour le diagnostic, 1 point pour la correction.

#### A-08 — Booléen et nombre

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A2 · Types, conversion et valeurs |
| **Réf. référentiel** | REF-040, REF-059 |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | A-06 |
| **Compétence visée** | Dénombrer les éléments d'un lot qui satisfont une condition, en exploitant l'équivalence entre vrai et 1. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-01 Score visible |
| **Statut de production** | À produire |

**1. Compétence visée** — Dénombrer les éléments d'un lot qui satisfont une condition, en exploitant l'équivalence entre vrai et 1.

**1 bis. Contexte métier** — Le contrôle de réception d'un lot de traverses porte sur une cote nominale de 1 200 mm, avec une tolérance de ± 5 mm.

**2. Composants mobilisés** — Boolean Toggle, Mass Addition, Larger Than

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les cotes relevées sur les 28 traverses du lot vous sont fournies. Comptez combien de traverses sortent de la tolérance, sans écarter aucun élément de la liste.

**4. Données de départ fournies** — Les 28 cotes relevées sur le lot, en millimètres, ainsi que la cote nominale de 1 200 mm et la tolérance de 5 mm.

**5. Résultat attendu** — 11 — le nombre de traverses dont l'écart à 1 200 mm dépasse 5 mm.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Larger Than (Maths > Operators) : liste sur A, slider sur B.
2. La sortie est une liste de booléens.
3. Poser Mass Addition (Maths > Operators) sur cette liste de booléens.
4. Le total correspond au nombre de valeurs True.

**6 bis. Erreur attendue** — Compter les traverses conformes au lieu des rebuts — le complément à 28 — ou traiter l'écart sans le ramener en valeur absolue, ce qui ne retient que les cotes trop grandes et laisse passer les trop petites.

**6 ter. Justification du jeu de données** — 28 cotes resserrées autour de 1 200 : impossible de compter à l'œil. Les 11 hors-tolérance sont répartis dans les deux sens — 7 trop grandes, 4 trop petites — pour que l'oubli de la valeur absolue donne 7 au lieu de 11 et se voie donc immédiatement.

**7. Pièges fréquents**

- Brancher Mass Addition sur la liste d'origine au lieu des booléens.
- Utiliser Larger Than au lieu de Larger Than or Equal quand l'énoncé dit « au moins ».

**8. Variantes et extensions**

- Compter les valeurs comprises entre deux bornes avec Gate And.
- Afficher le pourcentage plutôt que le compte.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le compte est exact.

#### A-09 — Valeur nulle et propagation

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A2 · Types, conversion et valeurs |
| **Réf. référentiel** | REF-055 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-07 |
| **Compétence visée** | Écarter les valeurs manquantes d'un relevé et dénombrer ce qui reste exploitable. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-16 Chasse au trésor sur le canvas |
| **Statut de production** | À produire |

**1. Compétence visée** — Écarter les valeurs manquantes d'un relevé et dénombrer ce qui reste exploitable.

**1 bis. Contexte métier** — Un relevé de hauteurs d'allège importé d'un tableur comporte des cellules restées vides.

**2. Composants mobilisés** — Panel, Null Item, Clean Tree, List Length

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le relevé porte sur 24 baies, mais certaines lignes n'ont pas été renseignées. Indiquez combien de hauteurs sont réellement exploitables.

**4. Données de départ fournies** — Le relevé des 24 baies, cellules non renseignées comprises.

**5. Résultat attendu** — 18 — le nombre de hauteurs réellement renseignées.

**6. Zone CORRIGÉ — explication étape par étape**

1. Brancher Null Item (Sets > Tree) pour localiser les nulles.
2. Poser Clean Tree avec Remove Nulls activé.
3. Brancher List Length sur la sortie nettoyée.
4. Relier vers un Panel : 6 éléments valides.

**6 bis. Erreur attendue** — Compter la longueur brute de la liste — 24 — sans voir que les cellules vides y figurent encore. L'erreur révèle qu'on confond « absence de valeur » et « absence d'élément ».

**6 ter. Justification du jeu de données** — 24 lignes dont 6 non renseignées, dispersées et non groupées en fin de liste, pour que le nettoyage ne puisse pas se deviner. Répondre 24 signale qu'on a mesuré la liste sans la nettoyer.

**6 quinquies. Note au formateur** — La solution de référence tient en peu de composants : l'exercice mesure surtout la connaissance du composant de nettoyage. En parcours, le fusionner avec un calcul qui exploite le relevé nettoyé.

**7. Pièges fréquents**

- Un Panel affiche une ligne vide pour une valeur nulle : elle passe inaperçue.
- Clean Tree supprime aussi les branches vides si l'option est cochée.

**8. Variantes et extensions**

- Remplacer les nulles par une valeur par défaut avec Replace Nulls.
- Observer la propagation d'une nulle à travers une Addition.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le Panel affiche 6.

### A3 · Listes

*9 exercices — A-10, A-11, A-12, A-13, A-14, A-15, A-16, A-17, A-18*

#### A-10 — Series et Range

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A3 · Listes |
| **Réf. référentiel** | REF-043, REF-047 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-01 |
| **Compétence visée** | Produire une suite régulière de positions à partir d'un pas et d'un nombre d'intervalles. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-07 Étoiles de performance |
| **Statut de production** | À produire |

**1. Compétence visée** — Produire une suite régulière de positions à partir d'un pas et d'un nombre d'intervalles.

**1 bis. Contexte métier** — Les axes de portique d'une halle sont espacés régulièrement le long d'une file.

**2. Composants mobilisés** — Series, Range, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La halle compte 7 portiques espacés de 5 400 mm, le premier à l'origine de la file. Produisez la liste des abscisses des 7 axes.

**4. Données de départ fournies** — Canvas vide.

**5. Résultat attendu** — 0, 5400, 10800, 16200, 21600, 27000, 32400.

**6. Zone CORRIGÉ — explication étape par étape**

1. Series : Start = 10, Step = 5, Count = 5.
2. Range : Domain = 10 To 30 (Construct Domain), Steps = 4.
3. Relier chaque sortie vers un Panel.
4. Retenir : Series raisonne en pas et nombre d'éléments, Range en domaine et subdivisions.

**6 bis. Erreur attendue** — Produire 7 intervalles au lieu de 7 axes, et donc 8 valeurs : la confusion entre le nombre d'éléments et le nombre d'espaces entre eux, qui se paie d'un portique en trop sur le chantier.

**7. Pièges fréquents**

- Range avec Steps = 5 produit 6 valeurs, pas 5.
- Oublier Construct Domain et saisir le domaine dans un Panel.

**8. Variantes et extensions**

- Produire une suite décroissante avec un pas négatif.
- Générer 5 valeurs entre 0 et 1 pour piloter un paramètre normalisé.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode ExactOrderedList.

**10. Barème** — 2 points : 1 par suite correcte.

#### A-11 — List Item et indexation

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A3 · Listes |
| **Réf. référentiel** | REF-042 |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-10 |
| **Compétence visée** | Atteindre un élément par son rang, et atteindre le dernier sans présumer de l'effectif. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-12 Memory |
| **Statut de production** | À produire |

**1. Compétence visée** — Atteindre un élément par son rang, et atteindre le dernier sans présumer de l'effectif.

**1 bis. Contexte métier** — Une liste de débit est reprise par un opérateur qui doit contrôler deux pièces précises avant lancement.

**2. Composants mobilisés** — List Item, Series, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le débit comporte 24 pièces. Relevez la longueur de la quatrième pièce, puis celle de la dernière — sachant que le débit s'allongera la semaine prochaine et que votre montage devra encore désigner la dernière pièce sans être retouché.

**4. Données de départ fournies** — Les 24 longueurs de débit, en millimètres, dans l'ordre du bon de commande.

**5. Résultat attendu** — Deux longueurs, dans cet ordre : 2 075 mm puis 2 830 mm — celle du quatrième rang, puis celle du dernier.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser List Item et régler l'index à 3 : la lettre D sort (le premier élément porte l'index 0).
2. Pour la dernière lettre, poser List Length puis soustraire 1.
3. Relier ce résultat sur l'index d'un second List Item.
4. Alternative : activer l'index négatif -1 sur List Item (clic droit > Wrap).

**6 bis. Erreur attendue** — Saisir en dur le rang de la dernière pièce. Le montage donne la bonne réponse aujourd'hui et la mauvaise dès que le débit change — une erreur qu'un exercice sans la clause d'évolution ne révélerait jamais.

**6 ter. Justification du jeu de données** — 24 longueurs non ordonnées : ni le rang 4 ni le dernier rang ne se repèrent visuellement.

**7. Pièges fréquents**

- Saisir l'index 4 pour la lettre D.
- Coder 9 en dur : le montage casse si la liste change de taille.

**8. Variantes et extensions**

- Extraire simultanément les index 0, 4 et 9 en branchant une liste d'index.
- Extraire un élément sur deux avec Cull Index.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode ExactOrderedList.

**10. Barème** — 2 points : 1 par extraction correcte.

#### A-12 — Longueur et bornes d'une liste

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A3 · Listes |
| **Réf. référentiel** | REF-043 |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | A-11 |
| **Compétence visée** | Caractériser un lot par son effectif et ses valeurs extrêmes. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-21 Golf de composants |
| **Statut de production** | À produire |

**1. Compétence visée** — Caractériser un lot par son effectif et ses valeurs extrêmes.

**1 bis. Contexte métier** — Un lot de placage est contrôlé en épaisseur avant mise en presse.

**2. Composants mobilisés** — List Length, Bounds, Deconstruct Domain, Sort List

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les épaisseurs relevées sur le lot vous sont fournies, en centièmes de millimètre. Produisez, dans cet ordre, l'effectif du lot, l'épaisseur la plus faible et l'épaisseur la plus forte.

**4. Données de départ fournies** — Les 28 épaisseurs relevées sur le lot, en centièmes de millimètre.

**5. Résultat attendu** — Trois valeurs, dans cet ordre : 28, 51, 78.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser List Length pour l'effectif.
2. Poser Bounds (Maths > Domain) puis Deconstruct Domain pour obtenir min et max.
3. Assembler les trois valeurs avec Merge dans le bon ordre.
4. Relier vers un Panel.

**6 bis. Erreur attendue** — Trier la liste puis lire les extrémités à l'œil : la réponse est juste, mais le montage ne suit plus si le lot change. La difficulté est ici de résister au contournement, pas de trouver le composant.

**6 ter. Justification du jeu de données** — 28 valeurs dispersées entre 51 et 78, sans ordre : les extrêmes ne sautent pas aux yeux et doivent être extraits par construction.

**7. Pièges fréquents**

- Merge respecte l'ordre de branchement des entrées : vérifier l'ordre.
- Utiliser Sort List et lire le premier et le dernier élément fonctionne aussi mais coûte plus de composants.

**8. Variantes et extensions**

- Ajouter la moyenne avec Average.
- Afficher l'index du minimum avec Sort List et List Item.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode ExactOrderedList.

**10. Barème** — 1 point si les trois valeurs sont exactes et dans l'ordre.

#### A-13 — Trier une liste avec une clé

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A3 · Listes |
| **Réf. référentiel** | REF-044, REF-047 |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-12 |
| **Compétence visée** | Réordonner une liste selon les valeurs portées par une autre. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | ExactOrderedList — tolérance — |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-08 Combo / série |
| **Statut de production** | À produire |

**1. Compétence visée** — Réordonner une liste selon les valeurs portées par une autre.

**1 bis. Contexte métier** — L'atelier veut débiter les pièces les plus longues en premier, pour engager la barre la plus contraignante tant que le stock est intact.

**2. Composants mobilisés** — Sort List, Reverse List, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Six pièces portent chacune un numéro de repère et une longueur. L'atelier débite la plus longue en premier. Produisez la liste des numéros de repère dans l'ordre de passage à la scie.

**4. Données de départ fournies** — Les six numéros de repère et les six longueurs correspondantes, dans deux listes de même rang.

**5. Résultat attendu** — 4256, 4207, 4229, 4198, 4183, 4171.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Sort List : longueurs sur Keys, noms sur Values A.
2. La sortie A est triée par longueur croissante.
3. Poser Reverse List sur la sortie A pour obtenir l'ordre décroissant.
4. Relier vers un Panel.

**6 bis. Erreur attendue** — Trier les repères eux-mêmes, ce qui donne un classement alphabétique sans rapport avec les longueurs. L'erreur révèle qu'on n'a pas vu que le tri devait être commandé par une autre liste.

**6 ter. Justification du jeu de données** — Les numéros de repère sont volontairement décorrélés des longueurs : un tri portant sur les repères eux-mêmes donne un ordre différent, donc détectable. La réponse est numérique, comme l'exige le checker.

**7. Pièges fréquents**

- Brancher les noms sur Keys : le tri se fait alors par ordre alphabétique.
- Oublier que Sort List renvoie aussi les clés triées sur la sortie K.

**8. Variantes et extensions**

- Trier selon deux critères successifs.
- Trier des points par distance à un point de référence.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode ExactOrderedList.

**10. Barème** — 1 point si l'ordre exact est respecté.

#### A-14 — Filtrer avec Cull Pattern

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A3 · Listes |
| **Réf. référentiel** | REF-045 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-13 |
| **Compétence visée** | Éliminer les éléments d'une liste selon un motif régulier. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-13 Casino — motifs assortis |
| **Statut de production** | À produire |

**1. Compétence visée** — Éliminer les éléments d'une liste selon un motif régulier.

**1 bis. Contexte métier** — Un bardage à claire-voie se pose en déposant une lame sur trois du calepinage plein.

**2. Composants mobilisés** — Cull Pattern, Boolean Toggle, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le calepinage plein comporte 36 lames. Produisez la liste des lames réellement posées, sachant qu'on conserve la première puis une sur trois.

**4. Données de départ fournies** — Le calepinage plein : les 36 longueurs de lames, en millimètres.

**5. Résultat attendu** — 12 longueurs : les rangs 0, 3, 6, … 33 du calepinage.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Cull Pattern (Sets > Sequence).
2. Dans un Panel, saisir le motif True, False, False sur trois lignes.
3. Relier le Panel sur l'entrée Pattern et la liste sur List.
4. Le motif se répète cycliquement sur toute la liste.

**6 bis. Erreur attendue** — Décaler le motif d'un cran et commencer par déposer la première lame : on obtient encore 12 lames, mais pas les mêmes. L'effectif seul ne suffit donc pas à valider — c'est pourquoi la réponse porte sur les longueurs conservées.

**6 ter. Justification du jeu de données** — 36 lames de longueurs voisines mais toutes distinctes : un décalage du motif conserve l'effectif de 12 tout en changeant la réponse. C'est pourquoi la validation porte sur les longueurs et non sur le seul comptage.

**6 quinquies. Note au formateur** — Un seul composant fait le travail. À terme, mieux vaut l'absorber dans un exercice de calepinage complet que le maintenir isolé.

**7. Pièges fréquents**

- Saisir le motif sur une seule ligne : Grasshopper lit un seul élément.
- Confondre Cull Pattern (motif cyclique) et Cull Index (index explicites).

**8. Variantes et extensions**

- Inverser le motif pour conserver les deux autres tiers.
- Piloter le motif par une comparaison numérique.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode ExactOrderedList.

**10. Barème** — 1 point si les 4 bons éléments sont conservés.

#### A-15 — Répartir avec Dispatch

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A3 · Listes |
| **Réf. référentiel** | REF-045, REF-061 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-14 |
| **Compétence visée** | Scinder un lot en deux ensembles selon une condition, en conservant les deux. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-15 Dessin à compléter |
| **Statut de production** | À produire |

**1. Compétence visée** — Scinder un lot en deux ensembles selon une condition, en conservant les deux.

**1 bis. Contexte métier** — Au-delà de 2,50 m², un panneau ne se pose plus seul : il faut séparer ce qui part en pose individuelle de ce qui part en binôme.

**2. Composants mobilisés** — Dispatch, Larger Than, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les surfaces des 24 panneaux du chantier vous sont fournies. Séparez-les en deux groupes selon qu'ils dépassent ou non 2,50 m², et donnez le nombre de panneaux à poser en binôme.

**4. Données de départ fournies** — Les 24 surfaces de panneaux, en mètres carrés, et le seuil de 2,50 m².

**5. Résultat attendu** — 11 — le nombre de panneaux de plus de 2,50 m², à poser en binôme.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Larger Than or Equal : liste sur A, valeur 50 sur B.
2. Poser Dispatch : liste sur List, booléens sur Pattern.
3. La sortie A reçoit les True, la sortie B les False.
4. Relier chaque sortie vers un Panel.

**6 bis. Erreur attendue** — Ne conserver qu'un seul des deux groupes, puis ne plus pouvoir vérifier que la somme des deux effectifs vaut bien 24.

**6 ter. Justification du jeu de données** — 24 surfaces réelles. Aucune ne vaut exactement 2,50 : la plus proche est à 2,49, de sorte que l'exercice ne dépende pas du sens de l'inégalité, qui n'est pas son objet. La somme des deux groupes doit valoir 24, ce qui donne à l'apprenant son propre moyen de contrôle.

**7. Pièges fréquents**

- Inverser les sorties A et B.
- Utiliser Larger Than strict alors que l'énoncé inclut 50.

**8. Variantes et extensions**

- Répartir des points selon leur coordonnée Z.
- Répartir en trois catégories en chaînant deux Dispatch.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point par sortie correcte.

#### A-16 — Décaler et inverser une liste

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A3 · Listes |
| **Réf. référentiel** | REF-046 |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-11 |
| **Compétence visée** | Relier chaque élément d'une liste au suivant en refermant la boucle, sans traiter le dernier cas à part. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-25 Animation de la solution |
| **Statut de production** | À produire |

**1. Compétence visée** — Relier chaque élément d'une liste au suivant en refermant la boucle, sans traiter le dernier cas à part.

**1 bis. Contexte métier** — Un garde-corps polygonal doit être chiffré en longueur de lisse : il faut les segments entre montants, y compris celui qui referme le contour.

**2. Composants mobilisés** — Shift List, Reverse List, Line

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Huit montants sont disposés en octogone. Tracez les huit lisses qui relient chaque montant au suivant, la dernière revenant au premier, en n'employant qu'une seule fois le composant de tracé.

**4. Données de départ fournies** — Une liste de 8 points internalisée, disposés en cercle.

**5. Résultat attendu** — Huit segments formant un contour fermé.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Shift List avec un décalage de 1 et l'option Wrap activée.
2. Poser Line : liste d'origine sur A, liste décalée sur B.
3. Les huit segments se tracent, le huitième reliant le dernier point au premier.
4. Désactiver Wrap pour observer qu'il ne reste que sept segments.

**6 bis. Erreur attendue** — Obtenir sept segments et refermer le contour à la main. Le montage marche pour huit montants et sera à refaire pour dix : l'exercice vise justement le décalage circulaire qui évite le cas particulier.

**6 quinquies. Note au formateur** — Le décalage circulaire est un vrai geste de conception, mais la solution reste courte : le rapprocher d'un exercice de contour fermé.

**7. Pièges fréquents**

- Wrap désactivé : le polygone reste ouvert.
- Utiliser Polyline avec l'option Closed masque le mécanisme visé par l'exercice.

**8. Variantes et extensions**

- Décaler de 2 pour obtenir les diagonales.
- Comparer avec PolyLine fermée.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point si les 8 segments sont produits.

#### A-17 — Fusionner et entrelacer

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A3 · Listes |
| **Réf. référentiel** | REF-042 |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-13 |
| **Compétence visée** | Entrelacer deux listes selon un motif d'alternance. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | ExactOrderedList — tolérance — |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-11 Mots croisés de composants |
| **Statut de production** | À produire |

**1. Compétence visée** — Entrelacer deux listes selon un motif d'alternance.

**1 bis. Contexte métier** — Un plateau se compose de lames de deux essences posées en alternance stricte.

**2. Composants mobilisés** — Merge, Weave, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Cinq lames de chêne et cinq lames de noyer vous sont fournies dans deux listes séparées, repérées par leur longueur. Produisez l'ordre de pose du plateau, une essence sur deux en commençant par le chêne.

**4. Données de départ fournies** — Les longueurs des cinq lames de chêne et des cinq lames de noyer, dans deux listes séparées.

**5. Résultat attendu** — 1245, 1418, 1268, 1463, 1231, 1437, 1287, 1409, 1252, 1481.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Weave (Sets > List).
2. Relier la première liste sur Stream 0, la seconde sur Stream 1.
3. Laisser le motif par défaut 0, 1 : l'alternance est automatique.
4. Comparer avec Merge qui produirait A, B, C, 1, 2, 3.

**6 bis. Erreur attendue** — Mettre les deux listes bout à bout : on obtient les dix lames, dans un ordre où les cinq chênes précèdent les cinq noyers. L'effectif est bon, le plateau est faux.

**6 ter. Justification du jeu de données** — Les deux essences occupent deux plages de longueur distinctes — chêne autour de 1 250, noyer autour de 1 440. L'alternance se contrôle donc à la lecture, et une mise bout à bout se repère au premier coup d'œil. La réponse est numérique, comme l'exige le checker.

**6 quinquies. Note au formateur** — Un seul composant suffit. La compétence réelle — choisir entre mettre bout à bout et entrelacer — gagnerait à être posée en question charnière avant l'exercice.

**7. Pièges fréquents**

- Confondre Weave (alternance) et Merge (concaténation).
- Motif de tissage personnalisé mal renseigné.

**8. Variantes et extensions**

- Tisser trois listes avec un motif 0, 1, 2.
- Reconstituer les deux listes d'origine avec Cull Pattern.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode ExactOrderedList.

**10. Barème** — 1 point si l'ordre exact est obtenu.

#### A-18 — Extraire une portion de liste

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A3 · Listes |
| **Réf. référentiel** | REF-042, REF-043 |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-12 |
| **Compétence visée** | Prélever une tranche continue d'une liste par ses rangs. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-03 Compte à rebours |
| **Statut de production** | À produire |

**1. Compétence visée** — Prélever une tranche continue d'une liste par ses rangs.

**1 bis. Contexte métier** — Sur un profil en long, seule la section courante intéresse le calcul ; les relevés d'extrémité relèvent des ouvrages voisins.

**2. Composants mobilisés** — Sub List, Construct Domain, Split List

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le profil compte 28 relevés altimétriques. Isolez ceux des rangs 5 à 12 inclus, qui correspondent à la section courante.

**4. Données de départ fournies** — Les 28 relevés altimétriques du profil en long, en millimètres.

**5. Résultat attendu** — Huit relevés : 466, 419, 448, 433, 471, 405, 459, 424.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Construct Domain avec A = 5 et B = 12.
2. Poser Sub List : liste sur L, domaine sur D.
3. Vérifier avec List Length que la sous-liste contient 8 éléments.
4. Retenir : le domaine est inclusif aux deux bornes.

**6 bis. Erreur attendue** — Livrer sept valeurs, en oubliant que la borne haute est incluse — ou neuf, en comptant deux fois une extrémité. L'écart d'une unité est l'erreur canonique sur les domaines de rangs.

**6 ter. Justification du jeu de données** — 28 altitudes non ordonnées : la tranche demandée n'a aucune signature visuelle, il faut la prélever.

**7. Pièges fréquents**

- Croire la borne haute exclusive : on obtiendrait 7 éléments.
- Saisir le domaine dans un Panel sous la forme « 5 to 12 » sans Construct Domain.

**8. Variantes et extensions**

- Couper la liste en deux avec Split List.
- Extraire les 5 derniers éléments quelle que soit la taille de la liste.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode ExactOrderedList.

**10. Barème** — 1 point si les 8 bons éléments sortent.

### A4 · Arbres de données

*5 exercices — A-19, A-20, A-21, A-22, A-23*

#### A-19 — Lire un chemin d'arbre

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A4 · Arbres de données |
| **Réf. référentiel** | REF-048, REF-051 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-05 |
| **Compétence visée** | Lire la structure d'un flux arborescent : nombre de branches et chemin d'une branche donnée. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-31 Carte de progression |
| **Statut de production** | À produire |

**1. Compétence visée** — Lire la structure d'un flux arborescent : nombre de branches et chemin d'une branche donnée.

**1 bis. Contexte métier** — Une définition reçue d'un confrère produit des résultats groupés ; avant d'y brancher quoi que ce soit, il faut savoir comment.

**2. Composants mobilisés** — Param Viewer, Tree Statistics, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le flux fourni est structuré en branches. Indiquez combien il en compte.

**4. Données de départ fournies** — Un arbre internalisé de 4 branches contenant chacune 3 éléments.

**5. Résultat attendu** — 4 — le nombre de branches du flux.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Tree Statistics (Sets > Tree) : la sortie P donne la liste des chemins.
2. Brancher List Length sur P pour obtenir le nombre de branches.
3. Poser List Item sur P avec l'index 2 pour lire le troisième chemin.
4. Relier les deux résultats vers un Panel.

**6 bis. Erreur attendue** — Répondre par le nombre total d'éléments, en confondant l'effectif global et le nombre de regroupements.

**7. Pièges fréquents**

- Confondre nombre de branches et nombre total d'éléments.
- Compter les branches à partir de 1.

**8. Variantes et extensions**

- Afficher le nombre d'éléments par branche avec la sortie C.
- Comparer l'affichage du Param Viewer en mode graphe et en mode texte.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point par réponse correcte.

#### A-20 — Graft et Flatten

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A4 · Arbres de données |
| **Réf. référentiel** | REF-049, REF-052 |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-19 |
| **Compétence visée** | Modifier la structure d'un flux pour obtenir un croisement complet plutôt qu'un appariement terme à terme. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-22 Boss de fin de chapitre |
| **Statut de production** | À produire |

**1. Compétence visée** — Modifier la structure d'un flux pour obtenir un croisement complet plutôt qu'un appariement terme à terme.

**1 bis. Contexte métier** — Une passerelle est haubanée : chaque ancrage de rive doit être relié à chaque ancrage de mât, et non au seul ancrage de même rang.

**2. Composants mobilisés** — Graft, Flatten, Line, Param Viewer

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Trois ancrages de rive et trois ancrages de mât vous sont fournis. Le tracé livre aujourd'hui trois haubans, un par paire de même rang. Obtenez les neuf haubans de toutes les combinaisons possibles, sans dupliquer le composant de tracé.

**4. Données de départ fournies** — Deux listes de 3 points internalisées, reliées par un Line.

**5. Résultat attendu** — Neuf segments.

**6. Zone CORRIGÉ — explication étape par étape**

1. Vérifier l'état initial : 3 segments seulement (correspondance un à un).
2. Clic droit sur l'entrée A du Line > Graft : chaque point part dans sa propre branche.
3. Grasshopper croise alors chaque branche de A avec la liste complète de B : 9 segments.
4. Ajouter un Flatten en sortie et observer que les 9 segments retombent dans une seule liste.

**6 bis. Erreur attendue** — Dupliquer le tracé et le brancher trois fois : on obtient neuf segments par force brute, et un montage qui ne tiendra pas à quatre ancrages. La contrainte d'un seul composant ferme cette voie sans nommer la solution.

**6 quinquies. Note au formateur** — Le geste tient en une option de menu contextuel. L'intérêt est dans la conséquence sur le résultat, ce que l'énoncé exploite déjà ; surveiller qu'il ne se réduise pas à « savoir où cliquer ».

**7. Pièges fréquents**

- Grafter les deux entrées : on retombe à 3 segments.
- Confondre Graft (éclate en branches) et Flatten (aplatit).

**8. Variantes et extensions**

- Obtenir le même résultat avec Cross Reference.
- Grafter une liste de courbes avant un Divide Curve.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point si 9 segments sont produits.

#### A-21 — Nettoyer une structure

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A4 · Arbres de données |
| **Réf. référentiel** | REF-050 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-20 |
| **Compétence visée** | Supprimer les niveaux de regroupement devenus inutiles sans détruire le regroupement utile. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-30 Mode coopératif |
| **Statut de production** | À produire |

**1. Compétence visée** — Supprimer les niveaux de regroupement devenus inutiles sans détruire le regroupement utile.

**1 bis. Contexte métier** — Un enchaînement d'opérations a empilé des niveaux de branche dont aucun ne porte plus de sens.

**2. Composants mobilisés** — Simplify Tree, Trim Tree, Param Viewer

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le flux fourni porte des chemins à quatre niveaux, dont trois ne distinguent plus rien. Ramenez-le à un seul niveau, sans fusionner les groupes entre eux. Indiquez le nombre de branches obtenu.

**4. Données de départ fournies** — Un arbre internalisé de chemins {0;0;0;0} à {0;0;0;3}.

**5. Résultat attendu** — Quatre branches, aux chemins {0} à {3}.

**6. Zone CORRIGÉ — explication étape par étape**

1. Brancher un Param Viewer pour lire les chemins de départ.
2. Poser Simplify Tree : les niveaux communs à toutes les branches sont supprimés.
3. Vérifier les nouveaux chemins dans le Param Viewer.
4. Retenir : Trim Tree supprime le dernier niveau, Simplify supprime les niveaux redondants.

**6 bis. Erreur attendue** — Tout aplatir : on obtient une branche unique et le regroupement est perdu. C'est l'erreur qui distingue « simplifier » de « écraser ».

**7. Pièges fréquents**

- Utiliser Flatten : la structure disparaît complètement.
- Trim Tree avec une profondeur trop grande fusionne des branches utiles.

**8. Variantes et extensions**

- Comparer Simplify et Trim Tree sur le même arbre.
- Reconstruire un chemin cible avec Path Mapper.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SetEquality.

**10. Barème** — 1 point si les chemins finaux sont {0} à {3}.

#### A-22 — Construire un arbre

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A4 · Arbres de données |
| **Réf. référentiel** | REF-048, REF-051 |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-21 |
| **Compétence visée** | Assembler plusieurs listes en un flux structuré, puis en réextraire chaque groupe. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-14 Puzzle de câblage |
| **Statut de production** | À produire |

**1. Compétence visée** — Assembler plusieurs listes en un flux structuré, puis en réextraire chaque groupe.

**1 bis. Contexte métier** — Trois lots de fabrication doivent voyager ensemble dans la définition tout en restant distincts à l'arrivée.

**2. Composants mobilisés** — Entwine, Explode Tree, Merge

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Trois listes de longueurs différentes vous sont fournies. Faites-les circuler dans un flux unique où chacune reste un groupe séparé, puis récupérez les trois listes d'origine à l'identique.

**4. Données de départ fournies** — Trois listes internalisées de 2, 5 et 3 éléments.

**5. Résultat attendu** — Un flux à trois branches, puis trois sorties identiques aux listes de départ.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Entwine et brancher les trois listes sur trois entrées.
2. Vérifier au Param Viewer : trois branches de 2, 5 et 3 éléments.
3. Poser Explode Tree en aval et zoomer pour faire apparaître les sorties.
4. Chaque sortie restitue la liste d'origine.

**6 bis. Erreur attendue** — Obtenir moins de sorties que de groupes : le composant de décomposition n'expose que le nombre de sorties qu'on lui a demandé, et perd silencieusement le reste.

**6 quinquies. Note au formateur** — Assembler puis redécomposer reste un aller-retour scolaire. En parcours, lui donner une finalité : trois lots qui doivent rester distincts jusqu'à l'export.

**7. Pièges fréquents**

- Merge à la place d'Entwine : les trois listes fusionnent en une seule.
- Explode Tree n'affiche ses sorties qu'après un zoom suffisant.

**8. Variantes et extensions**

- Entwiner des géométries de types différents.
- Renommer les chemins produits avec Path Mapper.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SetEquality.

**10. Barème** — 1 point pour l'arbre, 1 point pour la décomposition.

#### A-23 — Renommer les chemins avec Path Mapper

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A4 · Arbres de données |
| **Réf. référentiel** | REF-050 |
| **Niveau** | Débutant |
| **Durée cible** | 9 min |
| **Prérequis** | A-22 |
| **Compétence visée** | Réécrire les chemins d'un flux pour préparer une mise en correspondance. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 3 composants |
| **Gamification associée** | G-32 Indices payants |
| **Statut de production** | À produire |

**1. Compétence visée** — Réécrire les chemins d'un flux pour préparer une mise en correspondance.

**1 bis. Contexte métier** — Deux flux décrivent le même ouvrage, l'un rangé par niveau puis par file, l'autre par file puis par niveau : ils ne s'apparient pas.

**2. Composants mobilisés** — Path Mapper, Param Viewer

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le flux fourni est rangé par niveau puis par file. Réorganisez-le par file puis par niveau, sans modifier les éléments eux-mêmes. Indiquez le nombre de branches obtenu.

**4. Données de départ fournies** — Un arbre internalisé de 12 branches à deux niveaux.

**5. Résultat attendu** — Un flux dont les deux niveaux de chemin sont permutés.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Path Mapper et double-cliquer pour ouvrir l'éditeur.
2. Saisir le masque source {A;B}.
3. Saisir le masque cible {B;A}.
4. Valider et vérifier les chemins au Param Viewer.

**6 bis. Erreur attendue** — Réordonner les éléments au lieu des chemins : le contenu bouge, la structure reste, et l'appariement échoue toujours.

**6 quinquies. Note au formateur** — Le composant de réécriture des chemins est à lui seul la solution. Le maintenir comme exercice n'a de sens que si l'appariement qui suit est réellement demandé.

**7. Pièges fréquents**

- Oublier les accolades dans les masques.
- Utiliser des lettres différentes entre source et cible.

**8. Variantes et extensions**

- Fusionner deux niveaux avec le masque {A;B} vers {A}.
- Insérer un niveau constant avec {A} vers {0;A}.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SetEquality.

**10. Barème** — 1 point si les chemins sont permutés.

### A5 · Comportements implicites

*3 exercices — A-24, A-25, A-26*

#### A-24 — Correspondance par défaut

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A5 · Comportements implicites |
| **Réf. référentiel** | REF-053 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-10 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-09 Récompense cachée |
| **Statut de production** | À produire |

**1. Compétence visée** — Observer la correspondance appliquée par défaut lorsque deux listes de tailles différentes entrent dans un même composant.

**1 bis. Contexte métier** — Deux listes de tailles différentes arrivent dans un même opérateur.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Une liste de 10 valeurs et une liste de 4 valeurs entrent dans un même opérateur, sans réglage particulier. Combien de résultats sortent ?
a) 4 — la liste la plus courte impose sa longueur.
b) 10 — la liste la plus courte est complétée par répétition de son dernier élément. ← réponse
c) 40 — toutes les combinaisons sont calculées.
d) 14 — les deux listes sont mises bout à bout.

Valeur diagnostique : (a) est la représentation fausse la plus répandue, et elle est dangereuse — elle fait croire qu'un appariement déséquilibré se voit, alors qu'il produit silencieusement six résultats calculés sur une valeur répétée. (c) confond le comportement par défaut avec le croisement explicite, qui fait l'objet de l'exercice suivant.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> *Une liste de 10 nombres et une liste de 4 nombres entrent dans une même Addition. Combien de résultats sortent ? Affiche le compte dans un Panel, puis explique comment les 6 derniers ont été calculés.*

**4. Données de départ fournies** — Deux listes internalisées de 10 et 4 éléments reliées à une Addition.

**5. Résultat attendu** — Un Panel affichant 10 : la liste courte est complétée par répétition de son dernier élément.

**6. Zone CORRIGÉ — explication étape par étape**

1. Brancher List Length sur la sortie de l'Addition.
2. Relier vers un Panel : 10 résultats, et non 4.
3. Comparer les 6 derniers résultats à la liste longue : ils ont tous été additionnés au MÊME nombre, le dernier de la liste courte.
4. Constater qu'aucun avertissement n'est émis : ce complètement est silencieux.
5. Retenir : le comportement par défaut est la correspondance sur la liste la plus longue, la liste courte étant prolongée par son dernier élément.

**7. Pièges fréquents**

- Croire que Grasshopper tronque sur la liste la plus courte : ce comportement existe (Shortest List) mais doit être demandé explicitement par clic droit sur le composant.
- Ne pas vérifier la longueur et supposer que chaque paire a bien été formée une seule fois.
- Ne pas voir que les 6 derniers résultats reposent sur une valeur répétée, donc sur une donnée fabriquée.

**8. Variantes et extensions**

- Basculer le composant en Shortest List par clic droit et vérifier que l'on retombe à 4 résultats.
- Reproduire le cas avec des points et un Move : 6 points sont déplacés du même vecteur.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le Panel affiche 4.

#### A-25 — Longest List et Cross Reference

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A5 · Comportements implicites |
| **Réf. référentiel** | REF-054 |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-24 |
| **Compétence visée** | Choisir délibérément un mode d'appariement entre deux listes de tailles différentes. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-23 Duel et classement |
| **Statut de production** | À produire |

**1. Compétence visée** — Choisir délibérément un mode d'appariement entre deux listes de tailles différentes.

**1 bis. Contexte métier** — Un calepinage croise 10 files et 4 niveaux : selon qu'on veut une valeur par file ou une valeur par intersection, l'appariement change.

**2. Composants mobilisés** — Longest List, Cross Reference, Addition, List Length

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Une liste de 10 valeurs et une liste de 4 valeurs vous sont fournies. Produisez d'abord un résultat par file — 10 valeurs — puis un résultat par intersection file × niveau — 40 valeurs.

**4. Données de départ fournies** — Deux listes internalisées de 10 et 4 éléments.

**5. Résultat attendu** — Deux effectifs : 10 puis 40.

**6. Zone CORRIGÉ — explication étape par étape**

1. Insérer Longest List (Sets > List) en amont de l'Addition : la liste courte est complétée par son dernier élément, 10 résultats.
2. Insérer Cross Reference à la place : chaque élément de A est croisé avec chaque élément de B, 40 résultats.
3. Mesurer les deux sorties avec List Length.
4. Comparer avec le Graft de l'exercice A-20 qui produit le même croisement sous forme d'arbre.

**6 bis. Erreur attendue** — Obtenir 40 dans les deux cas en laissant un croisement branché, ou 10 dans les deux cas en ne changeant que la position des câbles. L'appariement est un réglage, pas une conséquence du câblage.

**7. Pièges fréquents**

- Cross Reference propose plusieurs variantes (Holistic, Diagonal) dans son menu contextuel.
- Longest List complète par répétition du dernier élément, pas par des zéros.

**8. Variantes et extensions**

- Obtenir 40 résultats par Graft plutôt que par Cross Reference et comparer les structures.
- Tester le mode Diagonal de Cross Reference.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode ExactOrderedList.

**10. Barème** — 1 point par valeur correcte.

#### A-26 — Ordre d'évaluation et recalcul

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A5 · Comportements implicites |
| **Réf. référentiel** | REF-056, REF-090 |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-24 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-17 Quiz éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — Comprendre que Grasshopper recalcule en cascade selon les dépendances, sans ordre imposé par la position sur le canvas.

**1 bis. Contexte métier** — Deux branches indépendantes cohabitent sur un même canvas.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Deux branches indépendantes produisent chacune un résultat. Dans quel ordre sont-elles évaluées ?
a) De gauche à droite, selon leur position sur le canvas.
b) Dans l'ordre où elles ont été créées.
c) L'ordre entre deux branches indépendantes n'est pas défini ; seules les dépendances imposent un ordre. ← réponse
d) Simultanément, sur plusieurs cœurs.

Valeur diagnostique : (a) est la croyance qui pousse à ranger le canvas pour « corriger » un résultat — un temps perdu considérable. (d) fait espérer un gain de performance qui n'existe pas ici.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> *Deux branches indépendantes du graphe produisent chacune un résultat. Dans quel ordre sont-elles évaluées ? Réponds par QCM et justifie en modifiant un seul slider.*

**4. Données de départ fournies** — Un graphe à deux branches indépendantes.

**5. Résultat attendu** — Réponse QCM : l'ordre dépend du graphe de dépendances, pas de la position sur le canvas.

**6. Zone CORRIGÉ — explication étape par étape**

1. Activer le widget Profiler (menu Display) pour lire les temps par composant.
2. Modifier un slider et observer que seule la branche dépendante se recalcule.
3. Déplacer physiquement un composant : aucun changement d'ordre.
4. Conclure : l'ordre suit les dépendances de données.

**7. Pièges fréquents**

- Croire que la position gauche-droite impose l'ordre d'exécution.
- Confondre ordre d'évaluation et ordre d'affichage.

**8. Variantes et extensions**

- Introduire un Timer et observer le recalcul cyclique.
- Utiliser Metahopper pour visualiser le graphe de dépendances.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode Conceptuel (QCM).

**10. Barème** — 1 point pour la bonne réponse au QCM.

### A6 · Outils de texte

*2 exercices — A-27, A-28*

#### A-27 — Construire une chaîne de caractères

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A6 · Outils de texte |
| **Réf. référentiel** | REF-057 |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-11 |
| **Compétence visée** | Composer un libellé exploitable à partir de valeurs numériques et de fragments de texte. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-11 Mots croisés de composants |
| **Statut de production** | À produire |

**1. Compétence visée** — Composer un libellé exploitable à partir de valeurs numériques et de fragments de texte.

**1 bis. Contexte métier** — Chaque pièce débitée part à l'atelier avec une étiquette portant son repère et sa longueur.

**2. Composants mobilisés** — Concatenate, Text Join, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les numéros et les longueurs des 5 pièces vous sont fournis dans deux listes. Produisez les cinq étiquettes au format « PIECE-01 : 1250 mm », le numéro étant cadré sur deux chiffres.

**4. Données de départ fournies** — Deux listes internalisées : 5 numéros et 5 longueurs.

**5. Résultat attendu** — Cinq libellés au format demandé.

**6. Zone CORRIGÉ — explication étape par étape**

1. Formater le numéro sur deux chiffres avec Format (masque {0:00}).
2. Poser Concatenate et brancher successivement PIECE-, le numéro formaté, le séparateur, la longueur et l'unité.
3. Zoomer sur Concatenate pour ajouter des entrées si nécessaire.
4. Relier vers un Panel et contrôler les espaces.

**6 bis. Erreur attendue** — Livrer « PIECE-1 » au lieu de « PIECE-01 » : le cadrage sur deux chiffres saute, et le tri alphabétique des étiquettes à l'atelier place la pièce 10 avant la pièce 2.

**6 quater. Limite de la correction automatique** — Le livrable de cet exercice est un texte, et le checker Magpie ne sait comparer que des nombres. La validation est donc visuelle : le formateur lit les cinq étiquettes. Ramener la réponse à un nombre — un total de caractères, par exemple — serait une gymnastique imposée par l'outil et non une étape de la tâche ; la skill le déconseille explicitement.

**7. Pièges fréquents**

- Oublier les espaces autour du deux-points.
- Concaténer un nombre décimal sans le formater : 1250,0 s'affiche.

**8. Variantes et extensions**

- Produire un libellé multiligne avec Text Join et un séparateur retour ligne.
- Utiliser ces libellés comme texte de cotation dans Rhino.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode Visuel.

**10. Barème** — 1 point si les 5 libellés sont exacts.

#### A-28 — Découper et remplacer du texte

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A6 · Outils de texte |
| **Réf. référentiel** | REF-058 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-27 |
| **Compétence visée** | Extraire un fragment d'une référence structurée et le normaliser. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-19 Le composant mystère |
| **Statut de production** | À produire |

**1. Compétence visée** — Extraire un fragment d'une référence structurée et le normaliser.

**1 bis. Contexte métier** — Les références fournisseur encodent la famille, le code produit et l'essence ; seul le code produit alimente la commande.

**2. Composants mobilisés** — Text Split, Replace Text, Text Case, Trim

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les références vous sont fournies au format « MEUB-A12-CHENE ». Extrayez le seul code central et livrez-le en minuscules.

**4. Données de départ fournies** — Une liste de 6 références internalisée.

**5. Résultat attendu** — Six codes en minuscules : a12, b07, …

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Text Split avec le séparateur - (tiret).
2. La sortie est un arbre : chaque référence donne une branche de 3 fragments.
3. Poser List Item avec l'index 1 pour prendre le fragment central de chaque branche.
4. Poser Text Case en mode Lower.

**6 bis. Erreur attendue** — Découper par position de caractère plutôt que par séparateur : le montage tient tant que la famille fait quatre lettres, et se rompt à la première référence au format différent.

**6 quater. Limite de la correction automatique** — Même limite qu'en A-27 : le livrable est une liste de codes en minuscules, que le checker ne sait pas comparer. Validation visuelle.

**7. Pièges fréquents**

- Oublier que Text Split produit un arbre et non une liste plate.
- Espaces parasites : appliquer Trim avant le découpage.

**8. Variantes et extensions**

- Remplacer le matériau par un autre avec Replace Text.
- Reconstituer la référence complète après modification.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode Visuel.

**10. Barème** — 1 point si les 6 codes sont exacts.

### A7 · Portes logiques

*3 exercices — A-29, A-30, A-31*

#### A-29 — Comparer deux valeurs

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A7 · Portes logiques |
| **Réf. référentiel** | REF-059 |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | A-08 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-18 Vrai / Faux à élimination |
| **Statut de production** | À produire |

**1. Compétence visée** — Produire un booléen à partir d'une comparaison numérique.

**1 bis. Contexte métier** — Deux cotes calculées par des chemins différents devraient coïncider.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Vous comparez 0,1 + 0,2 à 0,3 par un test d'égalité stricte. Le résultat est faux. Pourquoi ?
a) Grasshopper arrondit les affichages à trois décimales.
b) Les nombres à virgule sont codés en binaire : la somme vaut 0,30000000000000004. ← réponse
c) Le test d'égalité ne fonctionne pas sur les décimaux.
d) Il faut convertir en entiers avant de comparer.

Valeur diagnostique : c'est la connaissance qui, non transmise, produit des heures de débogage sur des géométries « qui devraient se toucher ». Elle explique aussi pourquoi le mode de validation tolérant existe.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> *Compare les valeurs 0,1 + 0,2 et 0,3 avec Equality. Le résultat est-il True ? Corrige le montage pour qu'il le devienne.*

**4. Données de départ fournies** — Deux Number Slider et une Equality.

**5. Résultat attendu** — Un booléen True obtenu par une comparaison avec tolérance.

**6. Zone CORRIGÉ — explication étape par étape**

1. Constater que Equality renvoie False en raison de la représentation des décimaux.
2. Remplacer Equality par Similarity (Maths > Operators).
3. Régler l'entrée de tolérance sur 0,001.
4. La sortie passe à True.

**7. Pièges fréquents**

- Comparer des flottants avec une égalité stricte.
- Confondre la tolérance de Similarity et la tolérance du document Rhino.

**8. Variantes et extensions**

- Comparer deux points avec une distance et un seuil.
- Comparer deux textes avec Equality.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si la sortie vaut True.

#### A-30 — Combiner plusieurs conditions

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A7 · Portes logiques |
| **Réf. référentiel** | REF-060 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-29 |
| **Compétence visée** | Combiner deux conditions en une décision unique par élément. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-06 Niveaux et déblocage |
| **Statut de production** | À produire |

**1. Compétence visée** — Combiner deux conditions en une décision unique par élément.

**1 bis. Contexte métier** — Seules les chutes comprises entre 500 et 1 500 mm sont remises en stock : en deçà elles partent au rebut, au-delà elles retournent en barre.

**2. Composants mobilisés** — Gate And, Gate Or, Gate Not, Larger Than, Smaller Than

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les longueurs des 24 chutes du jour vous sont fournies. Comptez celles qui repartent en stock, bornes incluses.

**4. Données de départ fournies** — Les 24 longueurs de chutes du jour, en millimètres, et les deux bornes de 500 et 1 500 mm.

**5. Résultat attendu** — 16 — le nombre de chutes remises en stock, bornes incluses.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Larger Than or Equal avec 500 sur B.
2. Poser Smaller Than or Equal avec 1500 sur B.
3. Poser Gate And et brancher les deux listes de booléens.
4. Relier vers un Panel pour contrôler.

**6 bis. Erreur attendue** — Traiter les bornes en strict : les chutes à 505 et 1 495 restent prises, mais une chute à exactement 500 ou 1 500 serait écartée. Le jeu de données contient l'une et l'autre pour que l'écart se voie.

**6 ter. Justification du jeu de données** — 24 longueurs, dont une exactement à 500 et une exactement à 1 500. C'est là tout l'intérêt du jeu : bornes incluses la réponse est 16, bornes exclues elle tombe à 14. Un jeu de données sans valeur sur la borne rendrait les deux montages indiscernables.

**7. Pièges fréquents**

- Utiliser Gate Or : toutes les pièces ressortent True.
- Bornes strictes alors que l'énoncé dit « inclus ».

**8. Variantes et extensions**

- Exclure une plage avec Gate Not.
- Ajouter une troisième condition sur le matériau.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si les 20 booléens sont exacts.

#### A-31 — Orienter un flux avec une condition

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A7 · Portes logiques |
| **Réf. référentiel** | REF-061 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-30 |
| **Compétence visée** | Orienter un flux vers l'une ou l'autre de deux sorties selon une condition, sans démonter le montage. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-24 Sons et retours audio |
| **Statut de production** | À produire |

**1. Compétence visée** — Orienter un flux vers l'une ou l'autre de deux sorties selon une condition, sans démonter le montage.

**1 bis. Contexte métier** — Deux variantes de remplissage sont à l'étude ; le client veut les voir alternativement sans qu'on retouche la définition devant lui.

**2. Composants mobilisés** — Stream Filter, Stream Gate, Dispatch, Boolean Toggle

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les deux variantes de remplissage sont montées et fonctionnent. Faites en sorte qu'un seul interrupteur bascule l'affichage de l'une à l'autre, sans supprimer ni débrancher aucun composant.

**4. Données de départ fournies** — Un Circle, un Rectangle et un Boolean Toggle.

**5. Résultat attendu** — Une seule géométrie affichée à la fois, commandée par l'interrupteur.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Stream Filter (Sets > Tree).
2. Brancher le cercle sur Stream 0 et le rectangle sur Stream 1.
3. Brancher le Boolean Toggle sur l'entrée Gate.
4. Basculer le toggle et vérifier l'alternance.

**6 bis. Erreur attendue** — Couper un câble pour masquer une variante : l'affichage est bon, mais la bascule n'est plus réversible et la seconde variante est perdue. La contrainte « sans débrancher » ferme cette voie.

**7. Pièges fréquents**

- Stream Filter attend un entier : le booléen est converti en 0 ou 1.
- Confondre Stream Filter (choisit une entrée) et Stream Gate (aiguille vers une sortie).

**8. Variantes et extensions**

- Piloter trois géométries avec un slider entier.
- Reproduire le comportement avec un Dispatch.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point si l'alternance fonctionne dans les deux sens.

### A8 · Géométrie vectorielle et filaire

*5 exercices — A-32, A-33, A-34, A-35, A-36*

#### A-32 — Vecteur, amplitude et direction

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A8 · Géométrie vectorielle et filaire |
| **Réf. référentiel** | REF-062 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-02 |
| **Compétence visée** | Construire un vecteur entre deux points, puis en régler la longueur sans en changer la direction. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,01 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-26 Feedback visuel immédiat |
| **Statut de production** | À produire |

**1. Compétence visée** — Construire un vecteur entre deux points, puis en régler la longueur sans en changer la direction.

**1 bis. Contexte métier** — Une potence de levage est reprise par un tirant : la direction est imposée par la géométrie, la longueur par la portée à couvrir.

**2. Composants mobilisés** — Unit X, Unit Y, Unit Z, Vector 2Pt, Amplitude, Vector Display

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le tirant part de l'origine et rejoint le point situé à 30 en X et 40 en Y. Construisez sa direction, puis produisez un second tirant de même direction mais de 100 unités de long.

**4. Données de départ fournies** — Deux points internalisés.

**5. Résultat attendu** — Un vecteur de longueur 50 et un vecteur de longueur 100, de même direction.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Vector 2Pt avec les deux points : sa longueur vaut 50.
2. Vérifier avec Vector Length.
3. Poser Amplitude et régler l'amplitude sur 100.
4. Afficher les deux vecteurs avec Vector Display pour comparer.

**6 bis. Erreur attendue** — Multiplier le vecteur par 100 au lieu de porter sa longueur à 100 : on obtient 5 000 unités. L'erreur révèle qu'on confond mise à l'échelle et fixation d'amplitude.

**7. Pièges fréquents**

- Confondre Amplitude (impose une longueur) et Multiplication (multiplie la longueur).
- Oublier d'activer Unitize sur Vector 2Pt quand on veut une direction pure.

**8. Variantes et extensions**

- Construire le vecteur normal d'un plan.
- Additionner deux vecteurs et vérifier la résultante.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point par vecteur correct.

#### A-33 — Plans de construction

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A8 · Géométrie vectorielle et filaire |
| **Réf. référentiel** | REF-062 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-32 |
| **Compétence visée** | Poser un repère orienté et y construire une géométrie. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-07 Étoiles de performance |
| **Statut de production** | À produire |

**1. Compétence visée** — Poser un repère orienté et y construire une géométrie.

**1 bis. Contexte métier** — Une buse traverse un mur en biais : son tracé se pose dans un plan incliné, pas dans le plan horizontal.

**2. Composants mobilisés** — XY Plane, Plane Normal, Construct Plane, Deconstruct Plane

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le percement est circulaire, de 20 de rayon, centré à 50 au-dessus de l'origine, et son plan est incliné de 30° autour de l'axe X. Construisez ce tracé.

**4. Données de départ fournies** — Canvas vide.

**5. Résultat attendu** — Un cercle de rayon 20 dans le plan incliné demandé.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser XY Plane et lui donner l'origine (0;0;50) via Construct Point.
2. Poser Rotate Plane avec un angle de 30° converti en radians (Radians ou saisie 30 avec le composant Degrees).
3. Poser Circle et brancher le plan sur P et 20 sur R.
4. Contrôler visuellement l'inclinaison dans la vue Rhino.

**6 bis. Erreur attendue** — Construire le cercle à plat puis le faire tourner : le résultat est visuellement identique mais le repère local ne suit pas, et tout ce qu'on y accrochera ensuite sera mal orienté.

**7. Pièges fréquents**

- Grasshopper travaille en radians : saisir 30 donne 30 radians.
- Confondre l'origine du plan et le centre du cercle quand on décale ensuite.

**8. Variantes et extensions**

- Construire le plan directement avec Construct Plane et deux vecteurs.
- Décomposer le plan avec Deconstruct Plane pour lire ses axes.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point si le cercle respecte position et inclinaison.

#### A-34 — Primitives filaires

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A8 · Géométrie vectorielle et filaire |
| **Réf. référentiel** | REF-063 |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-33 |
| **Compétence visée** | Produire des primitives filaires en maîtrisant ce que désignent leurs paramètres. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-15 Dessin à compléter |
| **Statut de production** | À produire |

**1. Compétence visée** — Produire des primitives filaires en maîtrisant ce que désignent leurs paramètres.

**1 bis. Contexte métier** — Un poteau de section hexagonale est inscrit dans un fourreau circulaire, lui-même logé dans un coffrage carré.

**2. Composants mobilisés** — Line, Circle, Rectangle, Polygon, Arc, Ellipse

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le fourreau a 40 de rayon. Construisez la section hexagonale inscrite dans ce fourreau, ainsi que le carré de coffrage circonscrit au même fourreau.

**4. Données de départ fournies** — Canvas vide.

**5. Résultat attendu** — Un hexagone de rayon 40 et un carré de 80 × 80.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Polygon avec un plan XY, un rayon de 40 et 6 segments.
2. Poser Rectangle avec le même plan et deux domaines de -40 à 40.
3. Utiliser Construct Domain pour produire ces domaines.
4. Vérifier que le rectangle est tangent au cercle circonscrit.

**6 bis. Erreur attendue** — Prendre 40 pour l'apothème de l'hexagone au lieu du rayon circonscrit : la section ne tient plus dans le fourreau. Inscrit et circonscrit ne se devinent pas, ils se vérifient.

**7. Pièges fréquents**

- Polygon attend un nombre de côtés, pas un nombre de sommets à calculer.
- Rectangle attend des domaines centrés, pas une largeur et une hauteur.

**8. Variantes et extensions**

- Ajouter un congé aux angles du rectangle (entrée R).
- Construire un polygone étoilé avec Polygon Edge.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point par courbe correcte.

#### A-35 — Diviser et évaluer une courbe

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A8 · Géométrie vectorielle et filaire |
| **Réf. référentiel** | REF-064 |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-34 |
| **Compétence visée** | Répartir des positions régulières le long d'une courbe et récupérer le repère local en chaque position. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Statut de production** | À produire |

**1. Compétence visée** — Répartir des positions régulières le long d'une courbe et récupérer le repère local en chaque position.

**1 bis. Contexte métier** — Un conduit souple est maintenu par des colliers régulièrement espacés le long de son tracé ; chaque collier est perpendiculaire au conduit.

**2. Composants mobilisés** — Divide Curve, Divide Length, Evaluate Curve, Curve Frames

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le tracé du conduit vous est fourni. Placez 12 colliers de 5 de rayon, régulièrement espacés le long du tracé et perpendiculaires à celui-ci en chaque point.

**4. Données de départ fournies** — Une courbe libre internalisée.

**5. Résultat attendu** — 12 cercles de rayon 5, perpendiculaires au tracé.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Divide Curve avec Count = 11 pour obtenir 12 points (12 divisions donneraient 13 points).
2. Récupérer la sortie T (tangentes) ou utiliser la sortie P de Perp Frames.
3. Poser Perp Frames avec Count = 11 : les plans sont déjà perpendiculaires.
4. Poser Circle avec ces plans et un rayon de 5.

**6 bis. Erreur attendue** — Placer les colliers à plat dans le plan horizontal : ils sont bien répartis, mais aucun n'enserre le conduit. L'erreur révèle qu'on a récupéré les positions sans les repères qui les accompagnent.

**7. Pièges fréquents**

- Divide Curve avec N divisions produit N+1 points quand la courbe est ouverte.
- Sur une courbe fermée, N divisions produisent N points.

**8. Variantes et extensions**

- Remplacer Divide Curve par Divide Length pour un pas fixe.
- Lofter les 12 cercles pour obtenir un tube.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point si 12 cercles perpendiculaires sont produits.

#### A-36 — Courbes passant par des points

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A8 · Géométrie vectorielle et filaire |
| **Réf. référentiel** | REF-063 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-35 |
| **Compétence visée** | Distinguer une courbe qui passe par des points d'une courbe que ces points contrôlent. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-12 Memory |
| **Statut de production** | À produire |

**1. Compétence visée** — Distinguer une courbe qui passe par des points d'une courbe que ces points contrôlent.

**1 bis. Contexte métier** — Un profil de main courante est défini par des points de passage imposés ; un second tracé, plus souple, sert d'étude de forme.

**2. Composants mobilisés** — Interpolate, Nurbs Curve, PolyLine, Kink Fillet

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Six points vous sont fournis. Tracez la courbe qui passe exactement par chacun d'eux, puis celle qui ne fait que s'en approcher en les prenant pour points de commande. Superposez les deux.

**4. Données de départ fournies** — Une liste de 6 points internalisée.

**5. Résultat attendu** — Deux courbes distinctes appuyées sur les mêmes points.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Interpolate (Curve > Spline) : la courbe passe par les points.
2. Poser Nurbs Curve sur la même liste : les points deviennent des points de contrôle.
3. Comparer visuellement les deux tracés.
4. Faire varier le degré des deux courbes pour observer l'effet.

**6 bis. Erreur attendue** — Obtenir deux courbes confondues : signe qu'on a employé deux fois la même construction. Les deux tracés ne coïncident qu'aux extrémités.

**7. Pièges fréquents**

- Attendre que Nurbs Curve passe par les points.
- Degré supérieur au nombre de points moins un : la courbe échoue.

**8. Variantes et extensions**

- Fermer les deux courbes et comparer la continuité.
- Tracer la PolyLine et arrondir ses angles.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point par courbe correcte.

### A9 · Transformations et réseaux

*4 exercices — A-37, A-38, A-39, A-40*

#### A-37 — Déplacer par un vecteur

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A9 · Transformations et réseaux |
| **Réf. référentiel** | REF-067 |
| **Niveau** | Débutant |
| **Durée cible** | 5 min |
| **Prérequis** | A-32 |
| **Compétence visée** | Appliquer une translation et l'échelonner, en sachant que la transformation ne consomme pas l'original. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-25 Animation de la solution |
| **Statut de production** | À produire |

**1. Compétence visée** — Appliquer une translation et l'échelonner, en sachant que la transformation ne consomme pas l'original.

**1 bis. Contexte métier** — Une rangée d'entretoises est répartie sur la hauteur d'un montant.

**2. Composants mobilisés** — Move, Unit Z, Multiplication, Vector 2Pt

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> L'entretoise de base vous est fournie. Remontez-la de 120 mm, puis produisez cinq entretoises supplémentaires échelonnées tous les 24 mm au-dessus d'elle, sans employer de composant de réseau.

**4. Données de départ fournies** — Un cercle internalisé dans le plan XY.

**5. Résultat attendu** — Six entretoises espacées de 24 mm.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Series avec Start = 0, Step = 24, Count = 6.
2. Poser Unit Z et brancher la série sur son entrée Factor.
3. Poser Move : cercle sur G, liste de vecteurs sur T.
4. Le composant produit 6 cercles : une liste de vecteurs génère une liste de résultats.

**6 bis. Erreur attendue** — Croire que la translation déplace l'original et compter cinq entretoises au lieu de six. La transformation produit une copie ; l'original reste dans le flux.

**7. Pièges fréquents**

- Brancher un seul vecteur et attendre plusieurs copies.
- Oublier que la géométrie d'origine reste visible en plus des copies.

**8. Variantes et extensions**

- Décaler selon un vecteur oblique.
- Faire varier le rayon en même temps que la hauteur.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point si 6 cercles espacés de 24 mm sont produits.

#### A-38 — Rotation et symétrie

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A9 · Transformations et réseaux |
| **Réf. référentiel** | REF-067 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-37 |
| **Compétence visée** | Faire tourner une géométrie autour d'un axe choisi et en produire le symétrique par rapport à un plan choisi. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-14 Puzzle de câblage |
| **Statut de production** | À produire |

**1. Compétence visée** — Faire tourner une géométrie autour d'un axe choisi et en produire le symétrique par rapport à un plan choisi.

**1 bis. Contexte métier** — Un profil d'angle se décline en version droite et version gauche, orientées à 45° sur la trame.

**2. Composants mobilisés** — Rotate, Mirror, Radians, XZ Plane

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le profil vous est fourni. Faites-le tourner de 45° autour de l'axe vertical passant par l'origine, puis produisez sa version symétrique par rapport au plan vertical contenant l'axe X.

**4. Données de départ fournies** — Un profil fermé internalisé.

**5. Résultat attendu** — Le profil tourné et son symétrique.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Rotate : profil sur G, angle sur A, plan XY sur P.
2. Convertir 45° en radians avec Radians, ou saisir directement 45 dans un slider réglé en degrés puis convertir.
3. Poser Mirror : résultat sur G, XZ Plane sur P.
4. Vérifier la position des deux résultats.

**6 bis. Erreur attendue** — Prendre le mauvais plan de symétrie et obtenir une version superposable à l'originale par rotation : une pièce gauche et une pièce droite ne sont pas superposables, c'est le contrôle à faire.

**7. Pièges fréquents**

- Saisir 45 sans conversion : la rotation vaut 45 radians.
- Le plan de symétrie de Mirror est un plan, pas un axe.

**8. Variantes et extensions**

- Enchaîner rotation et symétrie et comparer avec l'ordre inverse.
- Utiliser Rotate Axis pour tourner autour d'un axe quelconque.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point par transformation correcte.

#### A-39 — Réseaux rectangulaire et polaire

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A9 · Transformations et réseaux |
| **Réf. référentiel** | REF-068 |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-38 |
| **Compétence visée** | Produire des répétitions régulières en trame et en couronne, et lire la structure de données obtenue. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,5 mm |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-10 Coffre à butin |
| **Statut de production** | À produire |

**1. Compétence visée** — Produire des répétitions régulières en trame et en couronne, et lire la structure de données obtenue.

**1 bis. Contexte métier** — Une façade est calepinée en modules réguliers ; une verrière circulaire reprend le même module en couronne.

**2. Composants mobilisés** — Rectangular Array, Polar Array, Param Viewer

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le module vous est fourni. Produisez la trame de 5 modules en largeur et 4 en hauteur, espacés de 600 mm et 400 mm, puis la couronne de 12 modules répartis sur un tour complet.

**4. Données de départ fournies** — Un module rectangulaire internalisé.

**5. Résultat attendu** — 20 modules en trame et 12 modules en couronne.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Rectangular Array avec Nx = 5, Ny = 4.
2. Régler la cellule via un Construct Plane ou en réglant les entrées Sx et Sy sur 600 et 400.
3. Poser Polar Array avec Count = 12 et Angle = 2π.
4. Brancher un Param Viewer pour observer l'arbre à deux niveaux produit par le réseau rectangulaire.

**6 bis. Erreur attendue** — Produire 12 modules répartis sur 360° en comptant la position d'origine deux fois : le douzième se superpose au premier et il n'y a que 11 modules visibles.

**7. Pièges fréquents**

- Le réseau rectangulaire produit un arbre, pas une liste plate.
- Polar Array attend un angle en radians.

**8. Variantes et extensions**

- Faire varier la taille des modules selon leur position.
- Combiner les deux réseaux.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point par réseau correct.

#### A-40 — Mise à l'échelle

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A9 · Transformations et réseaux |
| **Réf. référentiel** | REF-067 |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-39 |
| **Compétence visée** | Mettre à l'échelle une géométrie, en maîtrisant le centre et en distinguant l'échelle uniforme de l'échelle par direction. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-04 Système de vies |
| **Statut de production** | À produire |

**1. Compétence visée** — Mettre à l'échelle une géométrie, en maîtrisant le centre et en distinguant l'échelle uniforme de l'échelle par direction.

**1 bis. Contexte métier** — Un profil de menuiserie est décliné en une version réduite et une version surhaussée, sans changer sa largeur de passage.

**2. Composants mobilisés** — Scale, Scale NU, Area, Bounding Box

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le profil vous est fourni. Produisez d'abord une version réduite à 60 % autour de son propre centre de gravité, puis une version deux fois plus haute dont la largeur reste inchangée.

**4. Données de départ fournies** — Un profil fermé internalisé.

**5. Résultat attendu** — Un profil réduit centré et un profil étiré verticalement.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Area sur le profil pour récupérer son centroïde.
2. Poser Scale : centre = centroïde, facteur = 0,6.
3. Poser Scale NU avec X = 1, Y = 1, Z = 2 (ou Y = 2 selon l'orientation).
4. Comparer les deux résultats.

**6 bis. Erreur attendue** — Réduire autour de l'origine du modèle plutôt qu'autour du centre du profil : la taille est bonne, la position ne l'est plus.

**7. Pièges fréquents**

- Scale utilise par défaut l'origine du repère, pas le centre de l'objet.
- Scale NU s'applique selon les axes du plan fourni.

**8. Variantes et extensions**

- Mettre à l'échelle une liste d'objets avec des facteurs différents.
- Utiliser Bounding Box pour recadrer avant mise à l'échelle.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point par mise à l'échelle correcte.

### A10 · Surfaces et solides

*6 exercices — A-41, A-42, A-43, A-44, A-45, A-46*

#### A-41 — Extrusion et surface réglée

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A10 · Surfaces et solides |
| **Réf. référentiel** | REF-069 |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-34 |
| **Compétence visée** | Passer d'une courbe à une surface par extrusion et par transition entre profils. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,5 mm |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-27 Narration Serengeti |
| **Statut de production** | À produire |

**1. Compétence visée** — Passer d'une courbe à une surface par extrusion et par transition entre profils.

**1 bis. Contexte métier** — Une trémie relie deux sections différentes ; un conduit droit relie deux sections identiques.

**2. Composants mobilisés** — Extrude, Loft, Unit Z, Ruled Surface

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Deux profils fermés superposés vous sont fournis. Produisez la surface de transition qui les relie, puis, séparément, la surface obtenue en poussant le profil du bas de 200 mm vers le haut. Comparez les deux.

**4. Données de départ fournies** — Deux profils fermés internalisés à 0 et 300 mm.

**5. Résultat attendu** — Une surface de transition et une surface d'extrusion.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Loft et brancher les deux profils dans l'ordre bas puis haut.
2. Régler les options de Loft (Normal, Straight) via son menu contextuel.
3. Poser Extrude avec Unit Z multiplié par 200.
4. Comparer : Loft suit les deux profils, Extrude conserve la section constante.

**6 bis. Erreur attendue** — Obtenir une transition vrillée parce que les deux profils ne démarrent pas au même endroit : la surface est valide mais inconstruisible.

**7. Pièges fréquents**

- Profils branchés dans le désordre : le Loft se vrille.
- Extrude attend un vecteur, pas une distance.

**8. Variantes et extensions**

- Lofter trois profils et observer la continuité.
- Extruder le long d'une courbe avec Extrude Along.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point par surface correcte.

#### A-42 — Balayage et révolution

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A10 · Surfaces et solides |
| **Réf. référentiel** | REF-069 |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-41 |
| **Compétence visée** | Engendrer une surface par déplacement d'un profil le long d'un guide, et par rotation autour d'un axe. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,5 mm |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-05 Badges et trophées |
| **Statut de production** | À produire |

**1. Compétence visée** — Engendrer une surface par déplacement d'un profil le long d'un guide, et par rotation autour d'un axe.

**1 bis. Contexte métier** — Une main courante tubulaire suit un limon ; un fût de colonne est engendré par rotation de son profil.

**2. Composants mobilisés** — Sweep 1, Sweep 2, Revolution, Rail

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le profil circulaire et son guide vous sont fournis, ainsi qu'un profil plan. Engendrez le tube en promenant le profil circulaire le long du guide, puis le fût en faisant tourner le profil plan autour de l'axe vertical.

**4. Données de départ fournies** — Un profil circulaire, une courbe guide et un profil plan internalisés.

**5. Résultat attendu** — Un tube et une surface de révolution.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Sweep 1 : courbe guide sur Rail, profil sur Sections.
2. Si le profil n'est pas positionné sur le rail, l'orienter d'abord avec Orient ou Perp Frame.
3. Poser Revolution : profil plan sur P, axe Z sur A, domaine 0 à 2π sur D.
4. Contrôler la fermeture des surfaces obtenues.

**6 bis. Erreur attendue** — Omettre de désigner l'axe de rotation : le composant reste en attente et ne produit rien, sans que le montage paraisse faux.

**7. Pièges fréquents**

- Profil non perpendiculaire au rail : le balayage se déforme.
- Domaine de révolution incomplet : le vase reste ouvert.

**8. Variantes et extensions**

- Balayer avec deux rails (Sweep 2).
- Faire varier la section le long du rail.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point par surface correcte.

#### A-43 — Fermer une polysurface en solide

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A10 · Surfaces et solides |
| **Réf. référentiel** | REF-070 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-41 |
| **Compétence visée** | Refermer une enveloppe ouverte et établir qu'elle constitue bien un solide. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 1 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-20 Erreur volontaire à débusquer |
| **Statut de production** | À produire |

**1. Compétence visée** — Refermer une enveloppe ouverte et établir qu'elle constitue bien un solide.

**1 bis. Contexte métier** — Un caisson doit être étanche avant d'être chiffré en volume de remplissage ; une enveloppe ouverte n'a pas de volume.

**2. Composants mobilisés** — Cap Holes, Brep Join, Is Solid (Brep Wireframe / Volume)

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> L'enveloppe fournie présente deux ouvertures. Refermez-la, puis établissez par une valeur numérique qu'elle est désormais un solide.

**4. Données de départ fournies** — Une polysurface ouverte internalisée.

**5. Résultat attendu** — Le volume du solide refermé, non nul — c'est lui qui prouve la fermeture : une enveloppe ouverte n'a pas de volume.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Cap Holes sur la polysurface.
2. Poser Volume : un volume non nul confirme la fermeture.
3. Utiliser Deconstruct Brep ou un composant Is Solid pour obtenir directement le booléen.
4. Relier vers un Panel.

**6 bis. Erreur attendue** — Se fier à l'aspect visuel : une enveloppe non fermée s'affiche exactement comme une enveloppe fermée. Seul le contrôle numérique tranche — c'est tout l'objet de l'exercice.

**6 ter. Justification du jeu de données** — Le tube fourni est ouvert aux deux extrémités. Son volume vaut zéro tant qu'il ne l'est pas : la preuve du caractère fermé est donc déjà numérique, et il n'y a pas lieu de la traduire en booléen.

**7. Pièges fréquents**

- Cap Holes ne ferme que les ouvertures planes.
- Un volume affiché à zéro signale une polysurface encore ouverte.

**8. Variantes et extensions**

- Réparer une ouverture non plane avec un Loft complémentaire puis Brep Join.
- Contrôler l'étanchéité en vue de l'impression 3D.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si le solide est fermé et prouvé.

#### A-44 — Opérations booléennes

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A10 · Surfaces et solides |
| **Réf. référentiel** | REF-071 |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-43 |
| **Compétence visée** | Combiner des solides par soustraction et quantifier la matière retirée. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 1 % |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-21 Golf de composants |
| **Statut de production** | À produire |

**1. Compétence visée** — Combiner des solides par soustraction et quantifier la matière retirée.

**1 bis. Contexte métier** — Une platine d'assemblage est percée pour le passage des boulons ; le poids retiré entre dans le bilan de charge.

**2. Composants mobilisés** — Solid Union, Solid Difference, Solid Intersection

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La platine vous est fournie. Percez-la de quatre trous traversants de 20 mm de diamètre, puis donnez le volume de matière retirée.

**4. Données de départ fournies** — Un bloc et quatre cylindres internalisés.

**5. Résultat attendu** — La platine percée et le volume retiré.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Solid Difference : bloc sur A, cylindres sur B.
2. Vérifier que les cylindres traversent bien le bloc.
3. Calculer le Volume du bloc initial et du bloc percé.
4. Soustraire les deux valeurs et afficher le résultat.

**6 bis. Erreur attendue** — Calculer le volume des quatre cylindres entiers plutôt que la différence des volumes : si les cylindres dépassent de la platine pour garantir le percement, l'écart est exactement la partie qui dépasse.

**7. Pièges fréquents**

- Inverser A et B : on obtient les cylindres percés par le bloc.
- Cylindres tangents à la face : l'opération échoue.

**8. Variantes et extensions**

- Additionner les volumes des cylindres et comparer au volume retiré.
- Remplacer la différence par une intersection.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point pour le perçage, 1 point pour le volume.

#### A-45 — Intersections entre géométries

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A10 · Surfaces et solides |
| **Réf. référentiel** | REF-071 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-44 |
| **Compétence visée** | Extraire le contour d'intersection entre un solide et un plan, et le mesurer. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0,5 % |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-16 Chasse au trésor |
| **Statut de production** | À produire |

**1. Compétence visée** — Extraire le contour d'intersection entre un solide et un plan, et le mesurer.

**1 bis. Contexte métier** — Une coupe horizontale à mi-hauteur sert à chiffrer le linéaire de joint périphérique.

**2. Composants mobilisés** — Curve | Curve, Brep | Plane, Brep | Brep, Curve | Brep

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le solide vous est fourni. Établissez son contour de coupe à mi-hauteur et donnez le linéaire total de ce contour.

**4. Données de départ fournies** — Un solide internalisé.

**5. Résultat attendu** — Le contour de coupe et son linéaire total.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Bounding Box puis Deconstruct Box pour obtenir la hauteur.
2. Construire le plan de coupe à mi-hauteur avec XY Plane et Construct Point.
3. Poser Brep | Plane et récupérer la sortie C (courbes).
4. Poser Length et Mass Addition pour la longueur totale.

**6 bis. Erreur attendue** — Ne mesurer qu'un seul morceau du contour quand la coupe en produit plusieurs : le linéaire est sous-évalué sans que rien ne le signale.

**7. Pièges fréquents**

- Plan de coupe placé hors du solide : aucune courbe produite.
- Plusieurs contours produits : additionner toutes les longueurs.

**8. Variantes et extensions**

- Produire une série de coupes régulières pour un plan de fabrication.
- Intersecter deux solides et récupérer la courbe commune.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point pour le contour, 1 point pour la longueur.

#### A-46 — Détecter une collision

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A10 · Surfaces et solides |
| **Réf. référentiel** | REF-072 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-45 |
| **Compétence visée** | Identifier, dans un ensemble, les objets qui interfèrent avec un volume donné. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SetEquality — tolérance — |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-01 Score visible |
| **Statut de production** | À produire |

**1. Compétence visée** — Identifier, dans un ensemble, les objets qui interfèrent avec un volume donné.

**1 bis. Contexte métier** — Un gabarit de passage doit rester libre : tout élément qui y pénètre est à reprendre.

**2. Composants mobilisés** — Collision One|Many, Graft, Flatten Tree, Dispatch, Custom Preview, Colour Swatch

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Quinze blocs sont disposés autour du gabarit de passage fourni. Indiquez combien d'entre eux empiètent sur ce gabarit.

**4. Données de départ fournies** — 15 blocs et un volume de gabarit internalisés.

**5. Résultat attendu** — Le nombre de blocs en interférence avec le gabarit.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Collision One|Many, mais en inversant les rôles attendus : les blocs sur Collider, le gabarit sur Obstacles.
2. Grafter l'entrée Collider : chaque bloc se retrouve seul dans sa branche.
3. La sortie Collision donne alors un booléen PAR BLOC ; aplatir le résultat avec Flatten Tree.
4. Poser Dispatch : les blocs sur List, les booléens sur Pattern.
5. Afficher la sortie A avec un Custom Preview alimenté par un Colour Swatch rouge.

**6 bis. Erreur attendue** — Obtenir une réponse unique pour l'ensemble au lieu d'une réponse par bloc : le test renvoie un verdict global si on ne lui présente pas les blocs un à un.

**7. Pièges fréquents**

- Brancher le gabarit sur Collider et les blocs sur Obstacles sans grafter : le composant ne renvoie alors qu'un SEUL booléen global et l'index du PREMIER bloc touché, pas la liste complète. C'est le piège central de cet exercice.
- Confondre la sortie Collision (booléens) et la sortie Index.
- Collision One|Many ne détecte pas le simple contact tangent.
- Croire que Collision Many|Many convient : ce composant n'a qu'une entrée et teste un ensemble contre lui-même.

**8. Variantes et extensions**

- Compter les collisions avec Mass Addition.
- Décaler automatiquement les blocs en collision.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SetEquality.

**10. Barème** — 1 point si les bons blocs sont identifiés.

### A11 · Mesures géométriques

*3 exercices — A-47, A-48, A-49*

#### A-47 — Longueur, aire et volume

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A11 · Mesures géométriques |
| **Réf. référentiel** | REF-079 |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-43 |
| **Compétence visée** | Mesurer les trois grandeurs de base d'un assemblage en choisissant l'outil adapté à chaque type de géométrie. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0,5 % |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-29 Défi quotidien |
| **Statut de production** | À produire |

**1. Compétence visée** — Mesurer les trois grandeurs de base d'un assemblage en choisissant l'outil adapté à chaque type de géométrie.

**1 bis. Contexte métier** — Un chiffrage rapide demande le linéaire d'arêtes à souder, la surface à peindre et le volume de matière.

**2. Composants mobilisés** — Length, Area, Volume, Mass Addition

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> L'assemblage vous est fourni. Donnez, dans cet ordre, le linéaire total des arêtes, la surface développée et le volume.

**4. Données de départ fournies** — Un solide internalisé.

**5. Résultat attendu** — Trois valeurs : linéaire, surface, volume.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Deconstruct Brep pour obtenir arêtes et faces.
2. Poser Length sur les arêtes puis Mass Addition.
3. Poser Area sur les faces puis Mass Addition, ou Area directement sur le Brep.
4. Poser Volume sur le Brep et assembler les trois valeurs avec Merge.

**6 bis. Erreur attendue** — Additionner des grandeurs de natures différentes ou mesurer la surface sur les arêtes : chaque grandeur suppose un type de géométrie, et l'assemblage en contient plusieurs.

**7. Pièges fréquents**

- Area sur un Brep fermé renvoie la surface totale : inutile de sommer les faces.
- Volume nul sur une polysurface ouverte.

**8. Variantes et extensions**

- Convertir les unités en m² et m³.
- Comparer avec les valeurs affichées par la commande Rhino.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si les trois valeurs sont dans la tolérance.

#### A-48 — Courbure et point le plus proche

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A11 · Mesures géométriques |
| **Réf. référentiel** | REF-080 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | A-35 |
| **Compétence visée** | Analyser localement une courbe pour y localiser la zone la plus contraignante. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 1 % |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-28 Avatar et personnalisation |
| **Statut de production** | À produire |

**1. Compétence visée** — Analyser localement une courbe pour y localiser la zone la plus contraignante.

**1 bis. Contexte métier** — Un profilé cintré ne peut descendre sous un rayon de cintrage minimal : c'est le point le plus serré du tracé qui décide de la faisabilité.

**2. Composants mobilisés** — Curvature, Curve Closest Point, Evaluate Curve, Graph Mapper

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le tracé vous est fourni. Localisez son point le plus serré et donnez le rayon de cintrage à cet endroit.

**4. Données de départ fournies** — Une courbe libre internalisée.

**5. Résultat attendu** — Le point de courbure maximale et son rayon de courbure.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Divide Curve avec 200 divisions pour échantillonner finement.
2. Poser Curvature sur ces paramètres : la sortie K donne le vecteur de courbure.
3. Poser Vector Length puis Sort List pour trouver la valeur maximale.
4. Le rayon vaut l'inverse de la courbure : poser Division avec 1 sur A.

**6 bis. Erreur attendue** — Confondre courbure et rayon, qui varient en sens inverse : chercher le rayon maximal conduit au point le plus plat, c'est-à-dire exactement l'inverse de ce que la fabrication demande.

**7. Pièges fréquents**

- Courbure nulle sur un segment droit : la division par zéro produit une valeur infinie.
- Échantillonnage trop grossier : le maximum réel est manqué.

**8. Variantes et extensions**

- Colorer la courbe selon sa courbure avec Gradient.
- Détecter les points d'inflexion.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point pour le point, 1 point pour le rayon.

#### A-49 — Centre de gravité

| Rubrique | Valeur |
|---|---|
| **Lot** | A — Découverte des composants natifs |
| **Thématique** | A11 · Mesures géométriques |
| **Réf. référentiel** | REF-081 |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | A-47 |
| **Compétence visée** | Localiser le centre de gravité de pièces et s'en servir comme point d'accroche. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | GeometryTolerance — tolérance 0,5 mm |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-05 Badges et trophées |
| **Statut de production** | À produire |

**1. Compétence visée** — Localiser le centre de gravité de pièces et s'en servir comme point d'accroche.

**1 bis. Contexte métier** — Chaque pièce d'un lot reçoit son repère au centre, à l'endroit où l'étiquette sera collée et où l'élingue sera accrochée.

**2. Composants mobilisés** — Area, Volume, Point, Text Tag 3D

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Six pièces vous sont fournies. Placez au centre de gravité de chacune une étiquette portant son numéro.

**4. Données de départ fournies** — 6 solides internalisés.

**5. Résultat attendu** — Six étiquettes numérotées, placées aux centres de gravité.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Volume sur la liste des solides : la sortie C donne les centroïdes.
2. Poser Series pour produire les numéros de 1 à 6.
3. Formater les numéros avec Format si un affichage sur deux chiffres est souhaité.
4. Poser Text Tag 3D avec les centroïdes en L et les textes en T.

**6 bis. Erreur attendue** — Prendre le centre de la boîte englobante plutôt que le centre de gravité : les deux coïncident sur une pièce symétrique et divergent sur une pièce en L — et c'est précisément là que l'élingue compte.

**7. Pièges fréquents**

- Area donne le centroïde surfacique, Volume le centroïde volumique : ils diffèrent.
- Text Tag 3D n'apparaît qu'en aperçu, il ne se cuit qu'avec un Bake explicite.

**8. Variantes et extensions**

- Trier les pièces par masse en pondérant par la densité.
- Placer un repère orienté au centroïde.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 1 point si les 6 étiquettes sont bien placées.

---

## Lot IA — IA et assistance générative

**Niveau** : Débutant à perfectionnement · **25 exercices** · **9 h 46 cumulées**

L'intelligence artificielle appliquée à Grasshopper : formuler une demande exploitable, faire produire un composant scripté, conduire un plugin avec un agent de code, apprendre d'un jeu de mesures, appeler un modèle de langage, piloter par un protocole d'agent, et vérifier ce qui revient.

| ID | Titre | Thématique | Niveau | Durée | Validation |
|---|---|---|---|---|---|
| IA-01 | Spécifier un composant plutôt que le décrire | IA1 · Formuler et cadrer une demande | Débutant | 20 min | SingleValue |
| IA-02 | Le contexte technique manquant | IA1 · Formuler et cadrer une demande | Débutant | 8 min | — |
| IA-03 | Reprendre une demande sur le point qui échoue | IA1 · Formuler et cadrer une demande | Débutant | 18 min | SingleValue |
| IA-04 | Un composant scripté qui somme un métré | IA2 · Composants scriptés assistés | Intermédiaire | 25 min | NumericTolerance |
| IA-05 | Le code qui tourne et se trompe | IA2 · Composants scriptés assistés | Intermédiaire | 22 min | SingleValue |
| IA-06 | Transposer sans changer le résultat | IA2 · Composants scriptés assistés | Intermédiaire | 20 min | ExactOrderedList |
| IA-07 | Un plugin .gha conduit par un agent | IA3 · Développement de plugins assisté | Perfectionnement | 90 min | Visuel |
| IA-08 | Le GUID que l'on ne régénère pas | IA3 · Développement de plugins assisté | Perfectionnement | 6 min | — |
| IA-09 | Prédire une déperdition sur une baie nouvelle | IA4 · Apprentissage automatique | Perfectionnement | 30 min | NumericTolerance |
| IA-10 | Regrouper un débit pour rationaliser la commande | IA4 · Apprentissage automatique | Perfectionnement | 25 min | SingleValue |
| IA-11 | Un cahier des charges qui devient des paramètres | IA5 · Modèles de langage et IA générative | Perfectionnement | 25 min | SingleValue |
| IA-12 | Faire construire un graphe par un agent | IA6 · Agents et protocoles | Perfectionnement | 35 min | NumericTolerance |
| IA-13 | Ce qui quitte le poste | IA7 · Vérification, licences et limites | Débutant | 8 min | — |
| IA-14 | Le résultat plausible et faux | IA7 · Vérification, licences et limites | Débutant | 15 min | NumericTolerance |
| IA-15 | Relire le graphe qu'un agent a construit | IA7 · Agents et protocoles | Perfectionnement | 30 min | SingleValue |
| IA-16 | Ce qu'un agent ne fait pas sans vous | IA7 · Agents et protocoles | Perfectionnement | 8 min | — |
| IA-17 | Une commande cachée dans un courriel | IA6 · Modèles de langage et IA générative | Perfectionnement | 30 min | SingleValue |
| IA-18 | Ce qu'une image générée ne vous donne pas | IA6 · Modèles de langage et IA générative | Perfectionnement | 8 min | — |
| IA-19 | Regrouper un débit en trois familles | IA5 · Apprentissage automatique | Perfectionnement | 25 min | SingleValue |
| IA-20 | Ce qu'un budget de calcul permet d'essayer | IA5 · Apprentissage automatique | Perfectionnement | 30 min | SingleValue |
| IA-21 | Le script qui compte les intervalles | IA2 · Composants scriptés assistés | Intermédiaire | 25 min | SingleValue |
| IA-22 | L'arrondi qui change avec le langage | IA2 · Composants scriptés assistés | Intermédiaire | 25 min | SingleValue |
| IA-23 | Combien de tours avant que tout passe | IA3 · Développement de plugins assisté | Perfectionnement | 25 min | SingleValue |
| IA-24 | Le composant qui n'apparaît pas | IA3 · Développement de plugins assisté | Perfectionnement | 8 min | — |
| IA-25 | Ce que le service coûte par mois | IA4 · Vérification, licences et limites | Perfectionnement | 25 min | NumericTolerance |

### IA1 · Formuler et cadrer une demande

*3 exercices — IA-01, IA-02, IA-03*

#### IA-01 — Spécifier un composant plutôt que le décrire

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA1 · Formuler et cadrer une demande |
| **Réf. référentiel** | REF-117, REF-139 |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | A-08 |
| **Compétence visée** | Rédiger la spécification d'un composant assez précise pour que le code obtenu soit juste du premier coup. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-01 Score visible |
| **Statut de production** | À produire |

**1. Compétence visée** — Rédiger la spécification d'un composant assez précise pour que le code obtenu soit juste du premier coup.

**1 bis. Contexte métier** — Le contrôle de réception d'un lot de platines porte sur l'entraxe de perçage, nominal 250 mm, toléré à ± 1,5 mm.

**2. Composants mobilisés** — C# Script ou Python 3 Script, Number, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les 28 entraxes relevés vous sont fournis. Faites produire par un assistant un composant scripté qui renvoie le nombre de platines hors tolérance, et branchez sa sortie sur la réponse. Vous ne corrigerez pas le code à la main : si le résultat est faux, c'est la demande qu'il faut reprendre.

**4. Données de départ fournies** — Les 28 entraxes relevés, en millimètres, ainsi que l'entraxe nominal et la tolérance, chacun sur une entrée distincte.

**5. Résultat attendu** — 10 — le nombre de platines dont l'entraxe s'écarte de plus de 1,5 mm de 250 mm.

**6. Zone CORRIGÉ — explication étape par étape**

1. Écrire la spécification avant d'ouvrir l'assistant : trois entrées (liste de cotes, nominale, tolérance), une sortie entière, et la règle exacte — écart absolu strictement supérieur à la tolérance.
2. Préciser le contexte : composant Grasshopper pour Rhino 8, langage retenu, accès en liste sur la première entrée.
3. Coller le code obtenu dans un composant scripté et déclarer les entrées avec les bons types.
4. Relever la sortie et la confronter à un contrôle indépendant — un comptage monté avec des composants natifs.
5. Si l'écart existe, reprendre la spécification sur le point précis qui a manqué, pas la totalité de la demande.

**6 bis. Erreur attendue** — Obtenir un composant qui ne compte que les entraxes trop grands, parce que la demande disait « supérieur à la tolérance » sans préciser qu'il s'agit d'un écart en valeur absolue. Le code est correct, la spécification ne l'était pas — c'est précisément ce que l'exercice mesure.

**6 ter. Justification du jeu de données** — 28 entraxes réels resserrés autour de 250, dont les hors-tolérance sont répartis dans les deux sens — 5 trop grands, 5 trop petits — de sorte qu'une spécification incomplète donne un résultat plausible mais faux, et non une erreur visible.

**7. Pièges fréquents**

- Demander « compte les valeurs hors tolérance » sans définir « hors tolérance » : l'assistant choisit à votre place.
- Laisser l'entrée en accès élément au lieu de liste : le composant s'exécute une fois par valeur et renvoie 28 résultats.
- Accepter le premier code qui s'exécute sans erreur.

**8. Variantes et extensions**

- Refaire la demande dans un second langage et vérifier que les deux composants renvoient le même nombre.
- Ajouter une tolérance asymétrique, +2 / −1, et mesurer ce que la spécification doit gagner en précision.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si la sortie vaut 5 sans retouche manuelle du code.

#### IA-02 — Le contexte technique manquant

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA1 · Formuler et cadrer une demande |
| **Réf. référentiel** | REF-118 |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | — |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Un assistant produit un code qui refuse de se compiler dans Rhino 8 alors qu'il semble correct.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Vous demandez un composant Grasshopper à un assistant, sans autre précision. Le code obtenu ne compile pas. Quelle information manquait le plus probablement ?
a) La version de Rhino et la bibliothèque visée. ← réponse
b) Le nom que vous vouliez donner au composant.
c) La couleur de l'icône.
d) Rien : les assistants ne savent pas écrire de composant.

Valeur diagnostique : (d) est la conclusion qu'en tire l'apprenant découragé, et elle est fausse — le modèle a produit du code valide pour une autre version de l'API. Nommer la version déplace le problème de « l'outil ne marche pas » à « ma demande était incomplète », qui est la seule formulation sur laquelle on peut agir.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

#### IA-03 — Reprendre une demande sur le point qui échoue

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA1 · Formuler et cadrer une demande |
| **Réf. référentiel** | REF-119 |
| **Niveau** | Débutant |
| **Durée cible** | 18 min |
| **Prérequis** | IA-01 |
| **Compétence visée** | Isoler ce qui échoue dans un code produit et reformuler la demande sur ce seul point. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-07 Indice progressif |
| **Statut de production** | À produire |

**1. Compétence visée** — Isoler ce qui échoue dans un code produit et reformuler la demande sur ce seul point.

**1 bis. Contexte métier** — Un relevé de planéité de plancher doit être classé : on cherche l'amplitude totale, du point le plus haut au plus bas.

**2. Composants mobilisés** — C# Script ou Python 3 Script, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les 28 niveaux relevés vous sont fournis, en millimètres autour du zéro. Faites produire un composant qui renvoie l'amplitude du relevé. Le premier code obtenu donnera un résultat faux : reprenez la demande sur le seul point fautif, sans la réécrire en entier.

**4. Données de départ fournies** — Les 28 niveaux relevés, en millimètres, positifs et négatifs.

**5. Résultat attendu** — 48 — l'écart entre le point le plus haut (+25) et le plus bas (−23).

**6. Zone CORRIGÉ — explication étape par étape**

1. Demander un composant renvoyant « l'écart maximal » du relevé, volontairement formulé ainsi.
2. Relever le résultat : 25, qui est la plus grande valeur absolue.
3. Contrôler à la main sur les données : le plus haut vaut +25, le plus bas −23, l'amplitude vaut donc 48.
4. Reformuler sur ce seul point — « la différence entre la valeur maximale et la valeur minimale » — sans redécrire les entrées.
5. Vérifier que la sortie vaut 48.

**6 bis. Erreur attendue** — Obtenir la plus grande valeur absolue, 25, au lieu de l'amplitude, 48 : « l'écart maximal » se comprend des deux façons. Un relevé entièrement positif ne révélerait pas l'ambiguïté — c'est la présence de valeurs négatives qui la rend visible.

**6 ter. Justification du jeu de données** — 28 niveaux répartis de part et d'autre du zéro, de −23 à +25. Sur un relevé positif, la valeur absolue maximale et l'amplitude coïncideraient et l'exercice n'aurait plus d'objet.

**7. Pièges fréquents**

- Repartir d'une demande entièrement neuve : on perd le contexte déjà établi et souvent on réintroduit une autre ambiguïté.
- Corriger le code à la main : l'exercice porte sur la formulation, pas sur la retouche.

**8. Variantes et extensions**

- Demander en plus la position du point le plus bas, et constater que la question du rang se pose exactement comme en A-11.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si la sortie vaut 48 après une seule reformulation.

### IA2 · Composants scriptés assistés

*5 exercices — IA-04, IA-05, IA-06, IA-21, IA-22*

#### IA-04 — Un composant scripté qui somme un métré

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA2 · Composants scriptés assistés |
| **Réf. référentiel** | REF-120, REF-121 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | IA-01 |
| **Compétence visée** | Faire produire, installer et brancher un composant scripté qui traite deux listes appariées. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Statut de production** | À produire |

**1. Compétence visée** — Faire produire, installer et brancher un composant scripté qui traite deux listes appariées.

**1 bis. Contexte métier** — Le calorifugeage d'un réseau de gaines se chiffre à la surface : chaque tronçon développe sa longueur multipliée par le périmètre de sa section.

**2. Composants mobilisés** — C# Script ou Python 3 Script, Number, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les longueurs et les diamètres des 16 tronçons vous sont fournis dans deux listes de même rang. Faites produire un composant scripté qui renvoie la surface totale à calorifuger, en mètres carrés.

**4. Données de départ fournies** — Les 16 longueurs en mètres et les 16 diamètres en millimètres, dans deux listes de même rang.

**5. Résultat attendu** — 58,03 m² — la surface développée totale, à 0,01 près.

**6. Zone CORRIGÉ — explication étape par étape**

1. Spécifier : deux entrées en accès liste, une sortie décimale, et l'unité attendue en sortie.
2. Signaler explicitement que les diamètres sont en millimètres et les longueurs en mètres.
3. Rappeler la formule attendue : périmètre multiplié par longueur, sommé sur tous les tronçons.
4. Installer le code et déclarer les deux entrées en accès liste.
5. Contrôler l'ordre de grandeur avant de valider : quelques dizaines de mètres carrés pour un réseau de cette taille.

**6 bis. Erreur attendue** — Mélanger les unités : les diamètres sont en millimètres et les longueurs en mètres. Un composant qui les multiplie sans conversion donne un résultat mille fois trop grand — assez visible pour être détecté, ce qui est précisément l'intérêt du contexte.

**6 ter. Justification du jeu de données** — Longueurs et diamètres pris dans des séries réelles de gaines circulaires (125 à 400 mm), avec des unités volontairement différentes entre les deux listes : c'est le cas courant en métré, et la spécification doit le dire.

**7. Pièges fréquents**

- Laisser les deux entrées en accès élément : le composant s'exécute 16 fois et la somme n'est jamais faite.
- Oublier de préciser l'unité de sortie et obtenir des millimètres carrés.

**8. Variantes et extensions**

- Ajouter une épaisseur d'isolant et demander le volume.
- Refaire le composant dans l'autre langage et comparer les deux sorties.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si la surface est juste à 0,01 m² près.

#### IA-05 — Le code qui tourne et se trompe

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA2 · Composants scriptés assistés |
| **Réf. référentiel** | REF-124 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 22 min |
| **Prérequis** | IA-04 |
| **Compétence visée** | Localiser une erreur de logique dans un code qui s'exécute sans planter. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-11 Chasse à l'erreur |
| **Statut de production** | À produire |

**1. Compétence visée** — Localiser une erreur de logique dans un code qui s'exécute sans planter.

**1 bis. Contexte métier** — Un composant livré par un confrère chiffre le nombre de tronçons dépassant une longueur de transport de 4 mètres.

**2. Composants mobilisés** — C# Script ou Python 3 Script, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le composant fourni s'exécute sans erreur et annonce un résultat. Ce résultat est faux. Trouvez pourquoi et faites-le corriger, puis donnez le nombre exact de tronçons concernés.

**4. Données de départ fournies** — Les 16 longueurs de tronçons, en mètres, et un composant scripté déjà en place qui les traite.

**5. Résultat attendu** — 9 — le nombre de tronçons de plus de 4 mètres.

**6. Zone CORRIGÉ — explication étape par étape**

1. Ne pas relire le code en premier : établir d'abord la réponse juste par un montage natif indépendant.
2. Comparer les deux résultats et mesurer l'écart.
3. Relire le code en cherchant ce qui produirait cet écart-là, plutôt qu'en cherchant « une erreur ».
4. Décrire à l'assistant le symptôme constaté — la valeur obtenue et la valeur attendue — et non « corrige ce code ».
5. Vérifier que la sortie corrigée vaut 9.

**6 bis. Erreur attendue** — Chercher l'erreur dans le langage plutôt que dans la logique. Le code est syntaxiquement irréprochable : c'est la condition qui est fausse. Un apprenant qui relit la syntaxe ligne à ligne peut y passer un long moment sans rien voir.

**6 ter. Justification du jeu de données** — Les longueurs sont choisies pour qu'une comparaison large et une comparaison stricte donnent le même compte : l'erreur plantée dans le code est ailleurs, ce qui évite de résoudre l'exercice par tâtonnement sur l'inégalité.

**7. Pièges fréquents**

- Demander « corrige ce code » sans dire ce qui cloche : l'assistant réécrit tout et l'erreur peut survivre.
- Faire confiance au fait que le composant ne signale rien : l'absence d'erreur ne dit rien de la justesse.

**8. Variantes et extensions**

- Injecter une seconde erreur et refaire le diagnostic.
- Écrire un contrôle permanent : un composant natif qui recalcule la même chose et signale tout écart.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si la sortie corrigée vaut 9.

#### IA-06 — Transposer sans changer le résultat

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA2 · Composants scriptés assistés |
| **Réf. référentiel** | REF-122, REF-123 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | IA-04 |
| **Compétence visée** | Porter un composant vers un autre langage et établir l'équivalence des deux versions. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | ExactOrderedList — tolérance — |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-18 Duel de versions |
| **Statut de production** | À produire |

**1. Compétence visée** — Porter un composant vers un autre langage et établir l'équivalence des deux versions.

**1 bis. Contexte métier** — Une définition ancienne repose sur un composant VB.NET que plus personne ne maintient ; il faut le porter sans changer un seul résultat.

**2. Composants mobilisés** — C# Script, Python 3 Script, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le composant existant produit une liste de valeurs. Faites-le porter vers un autre langage, puis établissez que les deux versions produisent exactement la même liste, dans le même ordre.

**4. Données de départ fournies** — Le composant d'origine, en place et fonctionnel, et le jeu de données qu'il traite.

**5. Résultat attendu** — Les seize sommes cumulées, de 3,42 à 68,92, dans cet ordre — identiques à celles de l'original.

**6. Zone CORRIGÉ — explication étape par étape**

1. Faire lire le composant d'origine à l'assistant, en fournissant le code, pas une description de ce qu'il fait.
2. Demander une transposition à l'identique, en signalant les cas limites à préserver.
3. Installer la version portée à côté de l'original, sans supprimer ce dernier.
4. Brancher les deux sur les mêmes données et comparer les sorties élément par élément.
5. Ne retirer l'original qu'une fois l'équivalence établie.

**6 bis. Erreur attendue** — Vérifier l'équivalence sur la seule longueur des deux listes, ou sur leurs premières valeurs. Deux implémentations peuvent diverger sur un cas limite — une liste vide, une valeur négative — et coïncider partout ailleurs.

**6 ter. Justification du jeu de données** — Le jeu comprend une valeur limite et une valeur négative, pour que deux implémentations plausibles puissent diverger et que la comparaison ait un sens.

**7. Pièges fréquents**

- Supprimer l'original avant d'avoir comparé : on perd la référence.
- Décrire le composant au lieu de fournir son code : l'assistant réinvente une logique voisine mais différente.

**8. Variantes et extensions**

- Comparer aussi les temps de calcul sur un jeu de données plus grand.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode ExactOrderedList.

**10. Barème** — 1 point si les deux listes sont identiques élément par élément.

#### IA-21 — Le script qui compte les intervalles

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA2 · Composants scriptés assistés |
| **Réf. référentiel** | REF-121 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | IA-04 |
| **Compétence visée** | Relire un script produit par un assistant en confrontant ce qu'il compte à ce que la tâche demande. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-15 Relecture de code |
| **Statut de production** | À produire |

**1. Compétence visée** — Relire un script produit par un assistant en confrontant ce qu'il compte à ce que la tâche demande.

**1 bis. Contexte métier** — La clôture fait 18,60 m et les poteaux ne doivent pas être espacés de plus de 2,50 m. Le script généré rend un nombre, et il paraît raisonnable.

**2. Composants mobilisés** — Division, Round, Addition, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La file mesure 18 600 mm et l'entraxe ne doit pas dépasser 2 500 mm. Donnez le nombre de poteaux.

**4. Données de départ fournies** — La longueur de la file et l'entraxe maximal admis.

**5. Résultat attendu** — 9 poteaux — huit travées de 2 325 mm.

**6. Zone CORRIGÉ — explication étape par étape**

1. Diviser la longueur par l'entraxe maximal.
2. Arrondir au supérieur : c'est le nombre de TRAVÉES.
3. Ajouter un : les poteaux sont un de plus que les travées.
4. Vérifier l'entraxe réel obtenu.

**6 bis. Erreur attendue** — Rendre 8, le nombre de TRAVÉES. C'est ce que rend un script qui divise et arrondit sans se demander ce qu'il compte. Le résultat est plausible, l'ordre de grandeur est juste, et il manque un poteau — celui du bout, qui est aussi celui qui tient la clôture.

**6 ter. Justification du jeu de données** — 18 600 ÷ 2 500 vaut 7,44 : l'arrondi au supérieur donne 8 travées, donc 9 poteaux, et l'entraxe réel tombe à 2 325 mm. Les deux réponses possibles diffèrent d'une unité — l'erreur la plus fréquente en programmation, et celle qui passe le mieux la relecture.

**6 quater. Limite de la correction automatique** — L'exercice suppose les deux extrémités équipées d'un poteau. Une clôture qui vient buter contre un mur n'en a qu'un — et c'est le genre de précision que la consigne doit porter, pas le script.

**7. Pièges fréquents**

- Rendre le nombre de travées.
- Arrondir au plus proche, ce qui donnerait 7 travées et un entraxe de 2 657 mm, au-delà du maximum.

**8. Variantes et extensions**

- Reprendre pour une clôture butant sur un mur à chaque bout.
- Donner la position de chaque poteau depuis l'origine.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre de poteaux est juste.

#### IA-22 — L'arrondi qui change avec le langage

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA2 · Composants scriptés assistés |
| **Réf. référentiel** | REF-123 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | IA-06 |
| **Compétence visée** | Vérifier qu'un script transposé rend le même résultat que l'original, en se méfiant des comportements par défaut. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-15 Relecture de code |
| **Statut de production** | À produire |

**1. Compétence visée** — Vérifier qu'un script transposé rend le même résultat que l'original, en se méfiant des comportements par défaut.

**1 bis. Contexte métier** — Le script de chiffrage est transposé d'un langage à un autre. Il compile, il tourne, et le total a bougé de six unités.

**2. Composants mobilisés** — Nombre, Addition, Round, Mass Addition, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les douze quantités à arrondir vous sont fournies ; toutes tombent sur une demi-unité. Le métier arrondit la demie vers le haut. Donnez la somme des quantités arrondies selon la règle du métier.

**4. Données de départ fournies** — Les douze quantités et la règle d'arrondi du métier.

**5. Résultat attendu** — 170 — la somme des arrondis commerciaux.

**6. Zone CORRIGÉ — explication étape par étape**

1. Arrondir chaque valeur selon la règle du métier.
2. Sommer.
3. Refaire la somme avec l'arrondi par défaut du langage et mesurer l'écart.

**6 bis. Erreur attendue** — Laisser l'arrondi par défaut du langage faire son office : il rend 164. La plupart des langages arrondissent la demie vers le nombre PAIR, pour ne pas biaiser les sommes — 2,5 donne 2 et 3,5 donne 4. C'est statistiquement vertueux et commercialement faux : sur douze lignes, six unités s'évaporent, et le devis ne tombe plus juste.

**6 ter. Justification du jeu de données** — Douze valeurs tombant toutes exactement sur la demie, dont six paires et six impaires : l'arrondi au pair descend une valeur sur deux, d'où un écart de six exactement. Sur des données ordinaires, l'écart serait nul la plupart du temps — et le défaut resterait invisible jusqu'au jour où il ne l'est plus.

**6 quater. Limite de la correction automatique** — Aucune des deux règles n'est « la bonne » dans l'absolu. Ce qui est fautif est de ne pas savoir laquelle le langage applique, et de découvrir l'écart sur une facture.

**7. Pièges fréquents**

- Se fier à l'arrondi par défaut.
- Supposer que deux langages arrondissent pareil.

**8. Variantes et extensions**

- Retrouver l'écart sur un jeu où une valeur sur dix seulement tombe sur la demie.
- Écrire la règle du métier explicitement, sans dépendre du langage.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si la somme selon la règle du métier est juste.

### IA3 · Développement de plugins assisté

*4 exercices — IA-07, IA-08, IA-23, IA-24*

#### IA-07 — Un plugin .gha conduit par un agent

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA3 · Développement de plugins assisté |
| **Réf. référentiel** | REF-125, REF-126, REF-127 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 90 min |
| **Prérequis** | IA-06 |
| **Compétence visée** | Conduire le développement d'un plugin Grasshopper avec un agent de code, jusqu'au composant réellement chargé par Rhino. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-25 Projet jalonné |
| **Statut de production** | À produire |

**1. Compétence visée** — Conduire le développement d'un plugin Grasshopper avec un agent de code, jusqu'au composant réellement chargé par Rhino.

**1 bis. Contexte métier** — Un geste répété dans plusieurs définitions mérite son propre composant, distribuable à l'équipe.

**2. Composants mobilisés** — Visual Studio ou équivalent, agent de code, Rhino 8

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Choisissez un traitement que vous refaites souvent à la main. Faites-en un composant distribuable, chargé par Rhino et visible dans l'onglet de votre choix, en conduisant le développement avec un agent de code.

**4. Données de départ fournies** — Un poste avec l'environnement de compilation en place et un agent de code disposant de l'accès aux fichiers du projet.

**5. Résultat attendu** — Un plugin chargé par Rhino, dont le composant apparaît dans l'onglet visé et produit le résultat attendu.

**6. Zone CORRIGÉ — explication étape par étape**

1. Écrire d'abord, en une page, ce que fait le composant : entrées, sorties, cas limites. C'est le document que l'agent lira.
2. Faire produire le squelette du projet, en imposant un GUID fixe et une catégorie stable.
3. Compiler, déposer le fichier dans le dossier des composants, débloquer le fichier si Windows l'a marqué, redémarrer Rhino.
4. Itérer par petites demandes vérifiables plutôt qu'en une seule grande, et relire chaque modification.
5. Consigner la version et le GUID dans la documentation du plugin avant toute diffusion.

**6 bis. Erreur attendue** — Laisser l'agent régénérer le GUID du composant à chaque itération. Le plugin fonctionne, mais chaque nouvelle version casse les définitions qui employaient la précédente — et le symptôme n'apparaît que chez les collègues.

**6 ter. Justification du jeu de données** — —

**6 quater. Limite de la correction automatique** — Le livrable est un plugin compilé : le checker Magpie ne sait comparer que des nombres. La validation est donc visuelle, sur le composant réellement chargé. Ramener l'exercice à une valeur numérique n'évaluerait plus la compétence visée.

**7. Pièges fréquents**

- Ne pas versionner avant de laisser l'agent modifier les fichiers : une régression devient irrattrapable.
- Accepter une refonte massive proposée par l'agent alors que la demande portait sur un détail.
- Oublier le déblocage du fichier téléchargé : Rhino charge le plugin sans rien dire, et le composant n'apparaît pas.

**8. Variantes et extensions**

- Ajouter une icône et une entrée d'aide au composant.
- Publier le plugin avec un fichier de licence explicite.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode Visuel.

**10. Barème** — Grille : composant chargé (2), résultat juste (2), GUID stable entre deux versions (1), documentation (1).

#### IA-08 — Le GUID que l'on ne régénère pas

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA3 · Développement de plugins assisté |
| **Réf. référentiel** | REF-128 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 6 min |
| **Prérequis** | — |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Une nouvelle version d'un plugin est distribuée à l'équipe.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Vous diffusez la version 2 d'un plugin. Les définitions de vos collègues affichent désormais un composant manquant à la place du vôtre. Que s'est-il passé ?
a) Le nom du composant a changé.
b) Le GUID du composant a été régénéré. ← réponse
c) Le plugin n'est pas signé.
d) Ils doivent vider le cache de Grasshopper.

Valeur diagnostique : (a) est plausible et fausse — le nom peut changer sans rien casser, c'est le GUID qui identifie le composant dans les fichiers enregistrés. (d) est la réponse qui fait perdre une demi-journée à toute l'équipe. Cette connaissance ne se découvre pas en construisant : elle se paie, une fois, très cher.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

#### IA-23 — Combien de tours avant que tout passe

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA3 · Développement de plugins assisté |
| **Réf. référentiel** | REF-126 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | IA-07 |
| **Compétence visée** | Piloter une itération avec un agent de code en s'appuyant sur une batterie de cas, et savoir quand elle est finie. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-20 Contre-expertise |
| **Statut de production** | À produire |

**1. Compétence visée** — Piloter une itération avec un agent de code en s'appuyant sur une batterie de cas, et savoir quand elle est finie.

**1 bis. Contexte métier** — L'agent corrige le composant tour après tour. Sans batterie de cas, on s'arrête quand on est fatigué.

**2. Composants mobilisés** — Nombre, Equality, Cull Pattern, List Item, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Dix-huit cas d'essai doivent passer. Le relevé des cinq tours d'itération vous est fourni. Donnez le numéro du premier tour où tous les cas passent.

**4. Données de départ fournies** — Le nombre de cas à satisfaire, et le nombre de cas qui passent à chaque tour.

**5. Résultat attendu** — 4 — c'est au quatrième tour que les dix-huit cas passent.

**6. Zone CORRIGÉ — explication étape par étape**

1. Comparer, tour par tour, le nombre de cas qui passent à la cible.
2. Retenir le PREMIER tour qui l'atteint.
3. Constater que les tours suivants n'apportent rien.

**6 bis. Erreur attendue** — Rendre 5, le dernier tour du relevé. Le cinquième n'a rien amélioré : il a coûté un aller-retour pour confirmer que le quatrième suffisait. Savoir s'arrêter fait partie de la compétence — une itération sans critère d'arrêt ne s'arrête pas, elle s'épuise.

**6 ter. Justification du jeu de données** — Les cas passent 7, 12, 16, 18, 18 : la progression ralentit, ce qui est le profil habituel, et le palier final rend visible le tour de trop. Le relevé compte cinq tours pour que la réponse ne soit ni le premier ni le dernier.

**6 quater. Limite de la correction automatique** — Dix-huit cas qui passent ne font pas un composant juste : ils font un composant juste SUR CES CAS. La compétence suivante est d'écrire les cas qui manquent.

**7. Pièges fréquents**

- Rendre le dernier tour du relevé.
- Conclure qu'un composant qui passe tous les cas est juste.

**8. Variantes et extensions**

- Estimer le coût des tours inutiles sur une série de dix composants.
- Écrire trois cas supplémentaires qui feraient échouer le composant du quatrième tour.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le numéro du premier tour suffisant est juste.

#### IA-24 — Le composant qui n'apparaît pas

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA3 · Développement de plugins assisté |
| **Réf. référentiel** | REF-127 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 8 min |
| **Prérequis** | IA-23 |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — L'agent annonce que la compilation a réussi. Grasshopper n'affiche aucun nouveau composant, et ne dit rien.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Compilation réussie, aucun composant dans l'onglet, aucun message. Que regardez-vous en premier ?
a) Le code du composant : il manque sans doute une méthode.
b) Où le fichier compilé a été déposé, et si Rhino regarde ce dossier. ← réponse
c) La version du SDK utilisée pour compiler.
d) Le journal de Grasshopper, qui doit contenir l'erreur.

Valeur diagnostique : l'absence de MESSAGE est l'information. Un composant mal écrit produit une erreur ; un composant que Rhino n'a jamais chargé ne produit rien. (a) et (c) supposent que le fichier a été lu, ce que rien n'établit. (d) est un bon réflexe, mais un journal vide dit la même chose que le silence : personne n'a essayé de charger quoi que ce soit.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

### IA4 · Apprentissage automatique

*2 exercices — IA-09, IA-10*

#### IA-09 — Prédire une déperdition sur une baie nouvelle

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA4 · Apprentissage automatique |
| **Réf. référentiel** | REF-129, REF-131, REF-132 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | IA-04 |
| **Compétence visée** | Ajuster un modèle sur des mesures existantes et l'employer pour prédire un cas non mesuré. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 10 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Statut de production** | À produire |

**1. Compétence visée** — Ajuster un modèle sur des mesures existantes et l'employer pour prédire un cas non mesuré.

**1 bis. Contexte métier** — Les déperditions ont été mesurées sur 24 baies d'un bâtiment existant ; une 25e baie est projetée et il faut l'estimer avant instrumentation.

**2. Composants mobilisés** — Composants d'apprentissage automatique pour Grasshopper, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les surfaces et les déperditions mesurées des 24 baies vous sont fournies. Estimez la déperdition d'une baie de 2,75 m².

**4. Données de départ fournies** — Les 24 couples surface / déperdition mesurés, et la surface de la baie à estimer.

**5. Résultat attendu** — Environ 380 W — la déperdition estimée pour une baie de 2,75 m², acceptée à 10 W près.

**6. Zone CORRIGÉ — explication étape par étape**

1. Placer les mesures et les visualiser avant tout calcul : la relation se voit à l'œil et oriente le choix du modèle.
2. Ajuster un modèle sur les 24 couples.
3. Appliquer le modèle à la surface visée.
4. Contrôler l'estimation par un rapport simple — déperdition par mètre carré sur les baies voisines en surface.
5. Écarter l'estimation si elle sort de cet encadrement.

**6 bis. Erreur attendue** — Estimer par la moyenne des déperditions plutôt que par la relation à la surface. La valeur obtenue est du bon ordre de grandeur — ce qui la rend dangereuse — mais ne suit pas la surface, et l'erreur explose sur les baies extrêmes.

**6 ter. Justification du jeu de données** — 24 couples couvrant 1,10 à 3,60 m², assez dispersés pour qu'un ajustement soit nécessaire, et assez cohérents pour qu'il ait un sens. La baie à estimer tombe en milieu de plage : l'exercice porte sur l'ajustement, pas sur l'extrapolation, qui est un autre sujet.

**7. Pièges fréquents**

- Ajuster sur toutes les données puis évaluer sur les mêmes : on ne mesure alors que la capacité du modèle à retenir, pas à prédire.
- Extrapoler hors de la plage mesurée sans le signaler.

**8. Variantes et extensions**

- Retirer les quatre plus grandes baies de l'ajustement et estimer l'une d'elles : mesurer ce que coûte l'extrapolation.
- Comparer l'estimation à un simple rapport moyen et chiffrer l'écart.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si l'estimation tombe à 10 W près de la valeur de référence.

#### IA-10 — Regrouper un débit pour rationaliser la commande

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA4 · Apprentissage automatique |
| **Réf. référentiel** | REF-130 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | IA-09 |
| **Compétence visée** | Regrouper automatiquement des éléments par similarité et exploiter le regroupement obtenu. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Statut de production** | À produire |

**1. Compétence visée** — Regrouper automatiquement des éléments par similarité et exploiter le regroupement obtenu.

**1 bis. Contexte métier** — Le fournisseur consent une remise à partir de trois longueurs standard seulement : il faut ramener un débit dispersé à trois longueurs de commande.

**2. Composants mobilisés** — Composants de regroupement pour Grasshopper, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les longueurs de débit vous sont fournies. Ramenez-les à trois longueurs de commande, chacune au moins égale à la plus longue pièce de son groupe, et donnez le nombre de pièces du groupe le plus fourni.

**4. Données de départ fournies** — Les 24 longueurs de débit, en millimètres.

**5. Résultat attendu** — L'effectif du groupe le plus fourni.

**6. Zone CORRIGÉ — explication étape par étape**

1. Regrouper les longueurs en trois ensembles par similarité.
2. Relever le maximum de chaque groupe : c'est la longueur de commande, pas la moyenne.
3. Compter les pièces de chaque groupe.
4. Contrôler que la somme des trois effectifs vaut bien 24.
5. Chiffrer la chute engendrée, pour vérifier que la remise vaut la matière perdue.

**6 bis. Erreur attendue** — Retenir la longueur moyenne de chaque groupe comme longueur de commande : une pièce sur deux devient alors trop courte. Le contexte impose un arrondi au supérieur, que le regroupement seul ne fournit pas.

**6 ter. Justification du jeu de données** — Les longueurs du débit du lot A sont réemployées ici dans un autre métier et une autre finalité : c'est la variation de contexte que la recherche sur le transfert recommande, à données constantes.

**7. Pièges fréquents**

- Prendre la moyenne du groupe comme longueur de commande.
- Oublier de vérifier que tous les groupes sont non vides.

**8. Variantes et extensions**

- Passer à quatre longueurs et comparer la chute totale.
- Chiffrer le seuil de remise à partir duquel le regroupement devient rentable.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si l'effectif annoncé correspond au regroupement de référence.

### IA5 · Modèles de langage et IA générative

*1 exercices — IA-11*

#### IA-11 — Un cahier des charges qui devient des paramètres

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA5 · Modèles de langage et IA générative |
| **Réf. référentiel** | REF-133, REF-134, REF-135 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | IA-03 |
| **Compétence visée** | Extraire d'un texte de prescription les valeurs exploitables par une définition, et les contrôler. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-16 Enquête documentaire |
| **Statut de production** | À produire |

**1. Compétence visée** — Extraire d'un texte de prescription les valeurs exploitables par une définition, et les contrôler.

**1 bis. Contexte métier** — Un article de CCTP décrit un garde-corps en toutes lettres ; la définition attend des nombres.

**2. Composants mobilisés** — Plugin d'appel à un modèle de langage ou composant script, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> L'article de CCTP vous est fourni. Faites-en extraire les valeurs dimensionnelles par un modèle de langage, puis donnez le nombre de montants nécessaires pour la longueur prescrite.

**4. Données de départ fournies** — Le texte de l'article, internalisé dans la définition, et l'accès à un modèle de langage.

**5. Résultat attendu** — Le nombre de montants, entracte maximal respecté.

**6. Zone CORRIGÉ — explication étape par étape**

1. Demander une extraction structurée, en imposant la liste des grandeurs attendues et leur unité.
2. Exiger que chaque valeur soit accompagnée de la phrase dont elle provient : c'est ce qui rend le contrôle possible.
3. Relire chaque valeur contre sa phrase d'origine.
4. Alimenter le calcul du nombre de montants avec les valeurs contrôlées.
5. Appliquer l'arrondi qu'impose le contexte : il faut au moins autant de montants, donc au supérieur.

**6 bis. Erreur attendue** — Reprendre telle quelle une valeur extraite sans la confronter au texte. Un modèle qui hésite entre deux nombres du même paragraphe produit une valeur crédible et fausse, et rien dans la définition ne le signalera.

**6 ter. Justification du jeu de données** — Le texte contient volontairement deux dimensions proches — une hauteur et un entraxe — de sorte qu'une extraction non contrôlée puisse les intervertir sans que le résultat paraisse absurde.

**6 quater. Limite de la correction automatique** — L'extraction elle-même n'est pas reproductible à l'identique d'un appel à l'autre : c'est le nombre de montants, contrôlé contre le texte, qui est validé — pas la sortie brute du modèle.

**7. Pièges fréquents**

- Accepter une extraction sans justification textuelle.
- Arrondir au plus proche le nombre de montants : il en manque un une fois sur deux.

**8. Variantes et extensions**

- Rejouer l'extraction trois fois et comparer les résultats : la variabilité fait partie du sujet.
- Ajouter une prescription contradictoire dans le texte et observer ce que le modèle en fait.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre de montants est juste et si chaque valeur extraite est justifiée par sa phrase source.

### IA6 · Agents et protocoles

*1 exercices — IA-12*

#### IA-12 — Faire construire un graphe par un agent

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA6 · Agents et protocoles |
| **Réf. référentiel** | REF-136, REF-137, REF-138 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 35 min |
| **Prérequis** | IA-07 |
| **Compétence visée** | Faire construire une définition par un agent connecté à Grasshopper, et relever le résultat produit. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0,1 |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-28 Pilotage à distance |
| **Statut de production** | À produire |

**1. Compétence visée** — Faire construire une définition par un agent connecté à Grasshopper, et relever le résultat produit.

**1 bis. Contexte métier** — Une série de définitions répétitives doit être produite : les monter une à une à la main n'est pas raisonnable.

**2. Composants mobilisés** — Serveur d'outils MCP pour Rhino et Grasshopper, agent de code

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Avec un agent relié à Grasshopper, faites construire une définition qui répartit des points le long d'une courbe et renvoie la longueur cumulée des segments obtenus. Travaillez sur une copie du fichier, et donnez la longueur obtenue.

**4. Données de départ fournies** — Un serveur d'outils relié à Rhino et Grasshopper, en service, et la courbe de référence.

**5. Résultat attendu** — 7 110,8 mm — la longueur de la polyligne inscrite, à 0,1 près.

**6. Zone CORRIGÉ — explication étape par étape**

1. Enregistrer et dupliquer le fichier avant toute action de l'agent.
2. Vérifier que le serveur d'outils répond avant de formuler la demande.
3. Décrire le résultat attendu, pas la suite de composants à poser : l'agent choisit les moyens.
4. Relire le graphe produit avant de lui faire confiance.
5. Relever la longueur et la contrôler par un calcul indépendant.

**6 bis. Erreur attendue** — Laisser l'agent travailler sur le document ouvert plutôt que sur une copie. Le montage produit peut être juste, mais le travail en cours dans le même document est écrasé sans avertissement — et l'agent ne le signalera pas.

**6 ter. Justification du jeu de données** — —

**6 quater. Limite de la correction automatique** — Un agent ne reproduit pas exactement le même graphe d'une fois sur l'autre. C'est la longueur cumulée qui est validée, pas la forme du graphe : deux montages différents et justes doivent tous deux être acceptés.

**7. Pièges fréquents**

- Travailler dans le document ouvert.
- Dicter la liste des composants : on retombe alors sur une saisie assistée, sans le bénéfice de l'agent.
- Accepter un graphe qui produit la bonne valeur mais qu'on serait incapable de maintenir.

**8. Variantes et extensions**

- Faire produire dix variantes paramétrées et comparer les longueurs.
- Demander à l'agent de documenter le graphe qu'il a construit.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si la longueur est juste à 0,1 près et si le travail a été mené sur une copie.

### IA7 · Vérification, licences et limites

*2 exercices — IA-13, IA-14*

#### IA-13 — Ce qui quitte le poste

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA7 · Vérification, licences et limites |
| **Réf. référentiel** | REF-140, REF-141 |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | — |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Un projet est couvert par un accord de confidentialité et l'équipe emploie un assistant en ligne.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Vous collez dans un assistant en ligne un extrait de définition pour le faire corriger. Que faut-il considérer comme transmis ?
a) Rien : le code n'est pas une donnée de projet.
b) Le code seul, sans les valeurs qu'il contient.
c) Tout ce qui est collé, valeurs internalisées, noms de calques et commentaires compris. ← réponse
d) Rien tant qu'on ne coche pas une case de partage.

Valeur diagnostique : (b) est la représentation la plus répandue et la plus risquée — les cotes, les repères et les noms de projet voyagent avec le code, souvent sans qu'on y pense. Poser la question avant la première utilisation coûte quelques minutes ; la poser après une fuite ne sert plus à rien.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

#### IA-14 — Le résultat plausible et faux

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA7 · Vérification, licences et limites |
| **Réf. référentiel** | REF-139, REF-142 |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | IA-01 |
| **Compétence visée** | Contrôler un résultat produit par une IA par un moyen indépendant de la manière dont il a été obtenu. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-11 Chasse à l'erreur |
| **Statut de production** | À produire |

**1. Compétence visée** — Contrôler un résultat produit par une IA par un moyen indépendant de la manière dont il a été obtenu.

**1 bis. Contexte métier** — Un assistant propose une section de poutre pour une portée donnée, avec une assurance qui n'a rien à voir avec sa justesse.

**2. Composants mobilisés** — Volume, Panel, composant scripté fourni

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le composant fourni annonce un volume de matière pour l'assemblage donné. Établissez si ce volume est juste, et donnez le volume exact.

**4. Données de départ fournies** — L'assemblage, et un composant scripté qui en annonce le volume.

**5. Résultat attendu** — 40 800 000 mm³, soit 0,0408 m³ — à comparer aux 40,8 m³ annoncés par le composant fourni.

**6. Zone CORRIGÉ — explication étape par étape**

1. Estimer l'ordre de grandeur à la main avant tout calcul.
2. Mesurer le volume par un moyen natif, indépendant du composant fourni.
3. Comparer les deux valeurs et qualifier l'écart.
4. Identifier la cause de l'écart dans le composant fourni.
5. Retenir la valeur établie par le moyen indépendant.

**6 bis. Erreur attendue** — Recontrôler le résultat avec le même outil, ou en redemandant à l'assistant s'il est sûr. Un contrôle qui emprunte le même chemin que le calcul ne contrôle rien : il faut un moyen indépendant — un ordre de grandeur, un calcul natif, une mesure dans Rhino.

**6 ter. Justification du jeu de données** — Le composant fourni divise par un million au lieu d'un milliard : il annonce 40,8 m³ pour un assemblage qui en fait 0,0408. Un facteur mille, invisible sans contrôle de l'ordre de grandeur.

**7. Pièges fréquents**

- Demander confirmation à l'assistant qui a produit le résultat.
- Conclure que le composant a raison parce qu'il donne une valeur précise : la précision affichée ne dit rien de la justesse.

**8. Variantes et extensions**

- Faire produire par l'assistant son propre contrôle indépendant, et juger si le contrôle est réellement indépendant.
- Reprendre A-47 et comparer les deux démarches.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si le volume exact est donné et si l'écart du composant fourni est expliqué.

### IA7 · Agents et protocoles

*2 exercices — IA-15, IA-16*

#### IA-15 — Relire le graphe qu'un agent a construit

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA7 · Agents et protocoles |
| **Réf. référentiel** | REF-137 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | IA-12 |
| **Compétence visée** | Confronter le graphe produit par un agent à la spécification qu'on lui avait donnée, et compter ce qui diverge — plutôt que de juger sur l'aperçu. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-20 Contre-expertise |
| **Statut de production** | À produire |

**1. Compétence visée** — Confronter le graphe produit par un agent à la spécification qu'on lui avait donnée, et compter ce qui diverge.

**1 bis. Contexte métier** — L'agent a construit la définition en trente secondes. L'aperçu montre un volume plausible. C'est précisément le moment où l'on ne vérifie pas.

**2. Composants mobilisés** — Nombre, Equality, Cull Pattern, List Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Vous aviez spécifié neuf liaisons, chacune avec son entrée de destination. Le relevé du graphe produit vous est fourni en regard. Donnez le nombre de liaisons qui ne sont pas conformes à la spécification.

**4. Données de départ fournies** — Les neuf liaisons demandées et les neuf liaisons produites, chacune avec l'indice de l'entrée de destination.

**5. Résultat attendu** — 3 — trois liaisons aboutissent sur une autre entrée que celle demandée.

**6. Zone CORRIGÉ — explication étape par étape**

1. Mettre les deux relevés en regard, liaison par liaison.
2. Comparer les indices d'entrée, et non les seuls noms.
3. Compter les désaccords.
4. Ne conclure à la conformité qu'après avoir aussi vérifié qu'aucune liaison ne manque.

**6 bis. Erreur attendue** — Compter les liaisons manquantes, et n'en trouver aucune : les neuf liaisons existent bien, et le graphe est complet. Ce qui diffère est leur POINT D'ARRIVÉE. Un graphe complet peut être entièrement faux, et il produit alors un résultat — donc un aperçu — parfaitement crédible.

**6 ter. Justification du jeu de données** — Les trois divergences aboutissent toutes sur l'entrée d'indice 0, et c'est la panne réelle des ponts agentiques : beaucoup d'implémentations ignorent silencieusement l'indice demandé et écrivent sur la première entrée. Le graphe se construit, ne signale rien, et calcule autre chose. Neuf liaisons est un format assez court pour se vérifier à la main, assez long pour qu'on ne le fasse pas.

**6 quater. Limite de la correction automatique** — L'exercice compte les écarts de câblage. Il ne dit rien des valeurs, des types ni des composants choisis — un graphe conforme au câblage près peut encore être faux. Compter est la première vérification, pas la seule.

**7. Pièges fréquents**

- Comparer les noms des composants et s'arrêter là.
- Se fier à l'aperçu, qui est plausible.
- Conclure de « neuf liaisons des deux côtés » à « graphe conforme ».

**8. Variantes et extensions**

- Reprendre la spécification et faire corriger l'agent, puis recompter.
- Écrire la vérification comme une étape automatique du pont, exécutée après chaque construction.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre de divergences est juste.

#### IA-16 — Ce qu'un agent ne fait pas sans vous

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA7 · Agents et protocoles |
| **Réf. référentiel** | REF-138 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 8 min |
| **Prérequis** | IA-15 |
| **Case Bloom (révisée)** | Évaluer × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — L'agent pilote Grasshopper et Rhino par un pont ouvert sur votre poste. Il a accès au document, aux fichiers, et à ce que vous lui laissez.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Vous ouvrez un pont agentique sur votre poste de travail. Quel garde-fou pose-t-on en premier ?
a) Relire chaque commande avant de la laisser passer.
b) Travailler sur une copie du document, et exiger une confirmation pour tout ce qui écrit hors de cette copie. ← réponse
c) Limiter l'agent aux composants natifs.
d) Journaliser les appels pour pouvoir les rejouer.

Valeur diagnostique : (a) est le réflexe naturel et il ne tient pas — un agent émet des dizaines d'appels par minute, personne ne les relit. (d) est utile mais ne protège de rien : un journal se lit après. (c) confond la puissance de l'agent et son droit d'écriture. Le seul garde-fou qui tienne est celui qui reste efficace quand on cesse de regarder : borner ce qui est réversible, et faire confirmer le reste.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

### IA6 · Modèles de langage et IA générative

*2 exercices — IA-17, IA-18*

#### IA-17 — Une commande cachée dans un courriel

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA6 · Modèles de langage et IA générative |
| **Réf. référentiel** | REF-134 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | IA-11 |
| **Compétence visée** | Extraire d'un texte libre les données chiffrées qui engagent, en distinguant ce qui est commandé de ce qui est seulement évoqué. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-18 Dictée technique |
| **Statut de production** | À produire |

**1. Compétence visée** — Extraire d'un texte libre les données chiffrées qui engagent, en distinguant ce qui est commandé de ce qui est seulement évoqué.

**1 bis. Contexte métier** — Le conducteur de travaux commande sa quincaillerie par courriel, en une phrase par ligne et sans tableau. La commande doit en sortir chiffrée.

**2. Composants mobilisés** — Texte, Nombre, Mass Addition, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le courriel vous est fourni tel qu'il a été reçu. Donnez le nombre total de pièces réellement commandées.

**4. Données de départ fournies** — Le courriel du conducteur de travaux, en texte libre.

**5. Résultat attendu** — 96 pièces — 24 paumelles, 48 vis, 18 poignées et 6 serrures.

**6. Zone CORRIGÉ — explication étape par étape**

1. Repérer chaque article cité et la quantité qui l'accompagne.
2. Convertir les quantités écrites en lettres.
3. Repérer les corrections : la dernière valeur annoncée remplace la précédente, elle ne s'y ajoute pas.
4. Écarter ce qui n'est pas une commande.
5. Sommer.

**6 bis. Erreur attendue** — Additionner tout ce qui ressemble à une quantité. On obtient alors 138 : les 30 crémones d'une demande de PRIX y sont comptées comme commandées, et les poignées le sont deux fois, à leur valeur annoncée puis à leur valeur corrigée. Une extraction qui ne distingue pas l'intention du chiffre produit une commande fausse — et personne ne relit une commande produite automatiquement.

**6 ter. Justification du jeu de données** — Le courriel porte trois pièges distincts, et un seul de chaque sorte : une quantité écrite en toutes lettres (que la lecture naïve ignore, donnant 48), une correction plus bas dans le message (qui invite au double comptage), et une demande de prix (qui invite à commander). Les quatre résultats possibles — 96, 48, 108 et 138 — sont tous distincts, donc chaque erreur se lit sans ambiguïté.

**6 quater. Limite de la correction automatique** — L'exercice valide un total, pas la structure extraite. Une extraction juste au total peut avoir mal attribué les quantités : le formateur regarde la table, pas seulement la somme.

**7. Pièges fréquents**

- Ignorer la quantité écrite en toutes lettres.
- Additionner la valeur annoncée et sa correction.
- Commander ce qui faisait l'objet d'une demande de prix.

**8. Variantes et extensions**

- Rendre la table structurée article par article, et non le seul total.
- Reprendre le même courriel avec deux corrections successives sur le même article.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le total est juste.

#### IA-18 — Ce qu'une image générée ne vous donne pas

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA6 · Modèles de langage et IA générative |
| **Réf. référentiel** | REF-135 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 8 min |
| **Prérequis** | IA-17 |
| **Case Bloom (révisée)** | Évaluer × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Le client a apporté une image générée qui lui plaît beaucoup, et demande « le même » en trois dimensions.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Un client apporte une image générée et demande le modèle correspondant. Qu'en tirez-vous réellement ?
a) Une intention de forme et de matière, à traduire en cotes et en constructibilité. ← réponse
b) Une géométrie, qu'un outil de reconstruction saura extraire.
c) Rien d'exploitable : mieux vaut repartir d'un croquis.
d) Une référence de style, à condition d'en avoir les droits.

Valeur diagnostique : (b) est l'erreur coûteuse — les outils de reconstruction rendent une surface, jamais des cotes, et une image générée n'a aucune raison d'être cohérente d'une vue à l'autre. (c) jette ce qui a de la valeur : l'image dit une intention, et c'est beaucoup. (d) est un vrai sujet, mais il vient après. Ce que l'image ne porte pas est ce qui fait le projet : dimensions, épaisseurs, assemblages, et la question de savoir si cela tient debout.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

### IA5 · Apprentissage automatique

*2 exercices — IA-19, IA-20*

#### IA-19 — Regrouper un débit en trois familles

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA5 · Apprentissage automatique |
| **Réf. référentiel** | REF-130 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | IA-10 |
| **Compétence visée** | Regrouper des pièces en familles de fabrication et identifier celle qui pèse le plus dans l'organisation de l'atelier. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Statut de production** | À produire |

**1. Compétence visée** — Regrouper des pièces en familles de fabrication et identifier celle qui pèse le plus dans l'organisation de l'atelier.

**1 bis. Contexte métier** — L'atelier organise ses postes par famille de format. Le débit arrive en vrac, et c'est la famille la plus fournie qui dimensionne le poste.

**2. Composants mobilisés** — Nombre, Smaller Than, Cull Pattern, List Length, Sort List, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les vingt-quatre longueurs du débit vous sont fournies. Les familles sont : petit sous 300 mm, moyen jusqu'à 900 mm exclus, grand au-delà. Donnez l'effectif de la famille la plus fournie.

**4. Données de départ fournies** — Les vingt-quatre longueurs, en millimètres, et les deux seuils.

**5. Résultat attendu** — 9 pièces — l'effectif de la famille des petits.

**6. Zone CORRIGÉ — explication étape par étape**

1. Classer chaque pièce selon les deux seuils.
2. Compter chaque famille.
3. Prendre le plus grand effectif.

**6 bis. Erreur attendue** — Rendre le nombre de familles (3), ou l'effectif de la famille des grands, qu'on suppose la plus nombreuse parce qu'elle occupe le plus de place. Les grands sont sept, les moyens huit : c'est la famille des PETITS qui est la plus fournie, et c'est contre-intuitif — la place occupée n'est pas l'effectif.

**6 ter. Justification du jeu de données** — Neuf, huit et sept : les trois effectifs sont proches, de sorte que la réponse ne se devine pas d'un coup d'œil et qu'un comptage approximatif se trompe de famille. Les longueurs vont de 45 à 1 510 mm, l'étendue ordinaire d'un débit de mobilier.

**6 quater. Limite de la correction automatique** — Les seuils sont donnés. Les TROUVER — c'est-à-dire laisser un regroupement automatique les proposer — est l'étape suivante, et elle demande de juger si les familles obtenues ont un sens pour l'atelier.

**7. Pièges fréquents**

- Rendre le nombre de familles.
- Placer mal la borne : « jusqu'à 900 exclus » n'est pas « jusqu'à 900 ».
- Supposer la réponse au lieu de compter.

**8. Variantes et extensions**

- Donner les trois effectifs.
- Chercher les seuils qui équilibreraient les trois familles.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si l'effectif de la famille la plus fournie est juste.

#### IA-20 — Ce qu'un budget de calcul permet d'essayer

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA5 · Apprentissage automatique |
| **Réf. référentiel** | REF-131, REF-132 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | IA-09 |
| **Compétence visée** | Dimensionner une campagne d'évaluations à partir du temps disponible, et mesurer l'écart avec ce qu'exigerait l'exploration exhaustive. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-13 Chronomètre |
| **Statut de production** | À produire |

**1. Compétence visée** — Dimensionner une campagne d'évaluations à partir du temps disponible, et mesurer l'écart avec ce qu'exigerait l'exploration exhaustive.

**1 bis. Contexte métier** — Chaque évaluation demande un calcul thermique complet. On dispose d'une nuit de machine.

**2. Composants mobilisés** — Multiplication, Division, Round, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le budget est de 6 heures et chaque évaluation prend 42 secondes. Donnez le nombre d'évaluations réalisables.

**4. Données de départ fournies** — Le budget en heures, la durée d'une évaluation, et le nombre de paramètres et de niveaux du problème.

**5. Résultat attendu** — 514 évaluations tiennent dans le budget.

**6. Zone CORRIGÉ — explication étape par étape**

1. Convertir le budget en secondes.
2. Diviser par la durée d'une évaluation.
3. Arrondir à l'entier INFÉRIEUR : une évaluation entamée ne compte pas.
4. Calculer, pour comparaison, la taille du plan complet.

**6 bis. Erreur attendue** — Vouloir explorer toutes les combinaisons. Douze paramètres à cinq niveaux font 244 millions d'évaluations, soit trois cent vingt-cinq ans de machine. Ce n'est pas une question de patience : c'est ce qui rend le métamodèle nécessaire plutôt que confortable.

**6 ter. Justification du jeu de données** — 514 évaluations pour un espace de 244 millions de points : le budget couvre deux millionièmes de pour cent de l'espace. Le chiffre n'est pas là pour impressionner — il dit que le plan d'expériences ne peut pas être régulier, et qu'il faut le choisir.

**6 quater. Limite de la correction automatique** — Le nombre d'évaluations tenables ne dit pas LESQUELLES faire. C'est tout l'objet d'un plan d'expériences, et la qualité du métamodèle en dépend plus que leur nombre.

**7. Pièges fréquents**

- Arrondir au supérieur.
- Oublier de convertir les heures en secondes.
- Croire qu'on peut approcher l'exhaustif en optimisant le calcul.

**8. Variantes et extensions**

- Trouver la durée d'évaluation qui permettrait mille essais.
- Comparer un plan aléatoire et un plan en hypercube latin à budget égal.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre d'évaluations est juste et arrondi à l'inférieur.

### IA4 · Vérification, licences et limites

*1 exercices — IA-25*

#### IA-25 — Ce que le service coûte par mois

| Rubrique | Valeur |
|---|---|
| **Lot** | IA — IA et assistance générative |
| **Thématique** | IA4 · Vérification, licences et limites |
| **Réf. référentiel** | REF-142 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | IA-13 |
| **Compétence visée** | Chiffrer le coût d'usage d'un service d'IA à partir de sa consommation réelle, en distinguant ce qui entre de ce qui sort. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-16 Livrable pesé |
| **Statut de production** | À produire |

**1. Compétence visée** — Chiffrer le coût d'usage d'un service d'IA à partir de sa consommation réelle, en distinguant ce qui entre de ce qui sort.

**1 bis. Contexte métier** — Le composant appelle un service distant à chaque recalcul. La facture arrive à la fin du mois, et personne n'a chiffré avant.

**2. Composants mobilisés** — Multiplication, Addition, Division, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le service traite 4 200 requêtes par mois. Chacune envoie 1 850 jetons et en reçoit 320. L'entrée est facturée 3 € le million de jetons, la sortie 15 €. Donnez le coût mensuel, en euros.

**4. Données de départ fournies** — Le nombre de requêtes, les jetons échangés par requête, et les deux tarifs.

**5. Résultat attendu** — 43,47 € par mois.

**6. Zone CORRIGÉ — explication étape par étape**

1. Chiffrer les jetons d'entrée du mois, et ceux de sortie.
2. Appliquer à chacun SON tarif.
3. Additionner, et ramener au million de jetons.

**6 bis. Erreur attendue** — Appliquer le même tarif à l'entrée et à la sortie : 27,34 €. La sortie coûte cinq fois l'entrée, et c'est structurel — elle se produit jeton par jeton. Un service qui répond peu mais lit beaucoup ne coûte pas comme un service qui lit peu et rédige longuement.

**6 ter. Justification du jeu de données** — 1 850 jetons en entrée pour 320 en sortie est le profil d'un composant qui envoie un contexte et reçoit une réponse courte. Malgré ce rapport de six contre un en volume, la sortie pèse 36 % de la facture : c'est ce renversement que le calcul doit faire apparaître.

**6 quater. Limite de la correction automatique** — Le coût n'est qu'une des trois limites de la fiche. La latence, elle, se paie à chaque recalcul et se mesure en secondes d'attente ; la reproductibilité ne se paie pas, elle s'établit — ou pas.

**7. Pièges fréquents**

- Appliquer un tarif unique.
- Oublier que les tarifs sont donnés au million.
- Compter la sortie comme négligeable parce qu'elle est courte.

**8. Variantes et extensions**

- Chiffrer la part de la sortie dans la facture.
- Reprendre avec une mise en cache qui évite 40 % des requêtes.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si le coût mensuel est juste au centime.

---

## Lot RH — Socle Rhino

**Niveau** : Débutant · **22 exercices** · **6 h 21 cumulées**

Le socle Rhino, prérequis de tout le reste. Ce qui produit une géométrie se valide en la référençant dans Grasshopper et en la mesurant ; ce qui relève de l'interface ne produit rien de mesurable et devient une question charnière.

| ID | Titre | Thématique | Niveau | Durée | Validation |
|---|---|---|---|---|---|
| RH-01 | Retrouver un objet perdu de vue | RH1 · Interface et navigation Rhino | Débutant | 6 min | — |
| RH-02 | Reprendre une implantation par son calque | RH2 · Organisation du document | Débutant | 15 min | SingleValue |
| RH-03 | Une trame de plots posée dans Rhino | RH3 · Modélisation Rhino | Débutant | 20 min | SingleValue |
| RH-04 | Du profil à la surface | RH3 · Modélisation Rhino | Débutant | 20 min | NumericTolerance |
| RH-05 | Percer une platine dans Rhino | RH3 · Modélisation Rhino | Débutant | 15 min | NumericTolerance |
| RH-06 | Groupe ou bloc ? | RH2 · Organisation du document | Débutant | 6 min | — |
| RH-07 | Le fichier au mauvais millimètre | RH4 · Précision et unités | Débutant | 7 min | — |
| RH-08 | Un caisson vraiment fermé | RH5 · Préparation à l'impression 3D | Débutant | 25 min | NumericTolerance |
| RH-09 | Une pièce imprimable | RH5 · Préparation à l'impression 3D | Débutant | 20 min | NumericTolerance |
| RH-10 | Ce que l'export STL perd | RH5 · Préparation à l'impression 3D | Débutant | 7 min | — |
| RH-11 | Ce que le zoom étendue vous apprend | RH1 · Interface et navigation Rhino | Débutant | 15 min | SingleValue |
| RH-12 | Ce qui dépasse le niveau | RH1 · Interface et navigation Rhino | Débutant | 15 min | SingleValue |
| RH-13 | Ce que le fichier contient vraiment | RH1 · Interface et navigation Rhino | Débutant | 15 min | SingleValue |
| RH-14 | La trame percée d'une trémie | RH2 · Modélisation Rhino | Débutant | 20 min | SingleValue |
| RH-15 | Le développé d'un cheminement | RH2 · Modélisation Rhino | Débutant | 20 min | SingleValue |
| RH-16 | La surface d'un rampant | RH2 · Modélisation Rhino | Débutant | 20 min | NumericTolerance |
| RH-17 | Le volume de deux blocs qui se recouvrent | RH2 · Modélisation Rhino | Débutant | 20 min | NumericTolerance |
| RH-18 | Les parois que la machine ne saura pas faire | RH3 · Préparation à l'impression 3D | Débutant | 20 min | SingleValue |
| RH-19 | Ce que la mise à l'échelle fait aux détails | RH3 · Préparation à l'impression 3D | Débutant | 25 min | SingleValue |
| RH-20 | Un maillage est-il fermé | RH3 · Préparation à l'impression 3D | Débutant | 25 min | SingleValue |
| RH-21 | Les faces qui ne mesurent rien | RH3 · Préparation à l'impression 3D | Débutant | 20 min | SingleValue |
| RH-22 | La finesse du maillage à l'export | RH3 · Préparation à l'impression 3D | Débutant | 25 min | SingleValue |

### RH1 · Interface et navigation Rhino

*4 exercices — RH-01, RH-11, RH-12, RH-13*

#### RH-01 — Retrouver un objet perdu de vue

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH1 · Interface et navigation Rhino |
| **Réf. référentiel** | REF-001, REF-002, REF-003 |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | — |
| **Case Bloom (révisée)** | Comprendre × procédurale |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Un fichier reçu d'un confrère s'ouvre sur une vue où l'on ne voit rien : le modèle est quelque part, mais hors champ.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Vous ouvrez un fichier et la vue est vide, alors que le modèle existe. Quel réflexe vous remet devant la géométrie en une action ?
a) Zoomer arrière longuement jusqu'à voir quelque chose.
b) Zoom Étendue — la vue se cadre sur tout ce qui est visible. ← réponse
c) Recréer une vue depuis le menu.
d) Fermer et rouvrir le fichier.

Valeur diagnostique : (a) est ce que fait spontanément un débutant, et cela peut durer longtemps — un objet égaré à 10 km de l'origine ne se rattrape pas à la molette. Cette question vaut surtout pour son prolongement : si le zoom étendue ne montre toujours rien, c'est que les objets sont sur un calque masqué ou hors du plan de coupe — et l'on cherche alors du bon côté.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

#### RH-11 — Ce que le zoom étendue vous apprend

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH1 · Interface et navigation Rhino |
| **Réf. référentiel** | REF-001, REF-002, REF-003 |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | RH-01 |
| **Compétence visée** | Diagnostiquer l'étendue réelle d'un fichier au lieu de juger sur ce que l'écran montre. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-02 Diagnostic éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — Diagnostiquer l'étendue réelle d'un fichier au lieu de juger sur ce que l'écran montre.

**1 bis. Contexte métier** — Le fichier arrive du géomètre. Un zoom étendue et l'on ne voit plus rien : le bâtiment est devenu un point.

**2. Composants mobilisés** — Point, Deconstruct, Bounds, Deconstruct Domain, Subtraction, Division, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le fichier contient cinquante objets, dont les coordonnées vous sont fournies. Donnez l'étendue du fichier selon X, en mètres.

**4. Données de départ fournies** — Les coordonnées en plan des cinquante objets, en millimètres.

**5. Résultat attendu** — 6 050 m — l'étendue selon X de tout ce que le fichier contient.

**6. Zone CORRIGÉ — explication étape par étape**

1. Extraire l'abscisse de chaque objet.
2. En prendre les bornes.
3. Soustraire, puis convertir en mètres.
4. Comparer à l'étendue de ce que l'on croyait voir.

**6 bis. Erreur attendue** — Répondre 8,4 m, l'étendue du bâtiment. C'est ce que l'on VOIT une fois zoomé dessus, et c'est précisément ce que le zoom étendue ne montre pas : deux objets égarés à 4,8 km et à 1,2 km étirent la vue sur six kilomètres, et le bâtiment n'occupe plus qu'un cinq-centième de l'écran.

**6 ter. Justification du jeu de données** — Quarante-huit objets tiennent dans 8,4 m ; deux sont à des kilomètres, l'un dans chaque sens. Le rapport entre l'étendue vue (8,4 m) et l'étendue réelle (6 050 m) vaut 720 : aucune confusion possible entre les deux réponses, et le chiffre dit à lui seul pourquoi l'écran est vide.

**6 quater. Limite de la correction automatique** — L'exercice mesure l'étendue. Il ne dit pas quoi faire ensuite — supprimer les égarés, ou comprendre d'où ils viennent, ce qui est souvent plus utile.

**7. Pièges fréquents**

- Juger sur l'écran.
- Ne regarder que les objets sélectionnés.
- Confondre étendue et distance à l'origine.

**8. Variantes et extensions**

- Donner aussi l'étendue en Y et en Z.
- Trouver les deux objets égarés et dire de quel calque ils viennent.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si l'étendue est juste, en mètres.

#### RH-12 — Ce qui dépasse le niveau

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH1 · Interface et navigation Rhino |
| **Réf. référentiel** | REF-002 |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | RH-11 |
| **Compétence visée** | Compter ce qui franchit un niveau donné, en tranchant explicitement le cas de ce qui s'y trouve exactement. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-02 Diagnostic éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — Compter ce qui franchit un niveau donné, en tranchant explicitement le cas de ce qui s'y trouve exactement.

**1 bis. Contexte métier** — On cherche ce qui dépasse le niveau du faux plafond, posé à 2 800 mm, pour savoir ce qui devra être repris.

**2. Composants mobilisés** — Nombre, Larger Than, Cull Pattern, List Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les altitudes des trente objets vous sont fournies. Donnez le nombre d'objets qui dépassent strictement le niveau de 2 800 mm.

**4. Données de départ fournies** — Les trente altitudes, en millimètres, et le niveau du faux plafond.

**5. Résultat attendu** — 17 objets dépassent strictement 2 800 mm.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser le niveau à comparer.
2. Comparer chaque altitude, en choisissant sciemment entre strict et large.
3. Compter.

**6 bis. Erreur attendue** — Compter 18 en incluant l'objet posé exactement à 2 800. La consigne dit STRICTEMENT, et sur un chantier la différence n'est pas rhétorique : ce qui affleure le plafond passe, ce qui le dépasse se reprend.

**6 ter. Justification du jeu de données** — Un objet exactement à 2 800, douze autres entre 2 788 et 2 820 : la frontière est peuplée, de sorte qu'un comptage à l'œil se trompe, et que le choix entre strict et large change la réponse d'exactement un.

**7. Pièges fréquents**

- Prendre « supérieur ou égal » par défaut.
- Compter à l'œil sur une liste où la frontière est peuplée.

**8. Variantes et extensions**

- Donner aussi le compte de ce qui affleure, à 5 mm près.
- Reprendre avec un plafond relevé à 2 850 mm.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le compte est juste et strict.

#### RH-13 — Ce que le fichier contient vraiment

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH1 · Interface et navigation Rhino |
| **Réf. référentiel** | REF-006, REF-004 |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | RH-02 |
| **Compétence visée** | Distinguer ce qu'un fichier contient de ce qu'il affiche, et compter sur la structure plutôt que sur l'écran. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-17 Passation |
| **Statut de production** | À produire |

**1. Compétence visée** — Distinguer ce qu'un fichier contient de ce qu'il affiche, et compter sur la structure plutôt que sur l'écran.

**1 bis. Contexte métier** — Avant d'envoyer le fichier, on veut savoir ce qu'il transporte : un calque éteint part quand même, avec tout ce qu'il contient.

**2. Composants mobilisés** — Booléen, Nombre, Cull Pattern, Mass Addition, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les huit calques vous sont fournis avec leur état et le nombre d'objets de chacun. Donnez le nombre d'objets actuellement VISIBLES.

**4. Données de départ fournies** — Les huit calques : nom, allumé ou éteint, nombre d'objets.

**5. Résultat attendu** — 176 objets visibles, sur les 270 que contient le fichier.

**6. Zone CORRIGÉ — explication étape par étape**

1. Retenir les seuls calques allumés.
2. Sommer leurs objets.
3. Comparer au total du fichier.

**6 bis. Erreur attendue** — Répondre 270, le contenu du fichier. C'est la bonne réponse à une autre question — et c'est justement l'écart entre les deux qui compte : 94 objets, dont d'anciens relevés, partiront chez le destinataire sans que personne les ait vus.

**6 ter. Justification du jeu de données** — Quatre calques allumés sur huit, et les éteints portent un tiers des objets. Les deux réponses — 176 et 270 — sont assez éloignées pour qu'aucune approximation ne les confonde.

**6 quater. Limite de la correction automatique** — Le compte des objets visibles ne dit rien de leur poids ni de ce qu'ils révèlent. Un calque éteint nommé « anciens relevés » est un problème de confidentialité avant d'être un problème de comptage.

**7. Pièges fréquents**

- Sommer tous les calques.
- Oublier qu'un calque éteint voyage avec le fichier.

**8. Variantes et extensions**

- Donner ce que le fichier transporterait après purge des calques éteints.
- Repérer les calques dont le nom seul pose un problème.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le compte des objets visibles est juste.

### RH2 · Organisation du document

*2 exercices — RH-02, RH-06*

#### RH-02 — Reprendre une implantation par son calque

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH2 · Organisation du document |
| **Réf. référentiel** | REF-004, REF-006, REF-014 |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | A-04 |
| **Compétence visée** | Organiser un document Rhino par calques de sorte qu'une définition puisse en reprendre une partie sans sélection manuelle. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Statut de production** | À produire |

**1. Compétence visée** — Organiser un document Rhino par calques de sorte qu'une définition puisse en reprendre une partie sans sélection manuelle.

**1 bis. Contexte métier** — Le géomètre livre l'implantation d'un plancher : poteaux porteurs et cloisons sont mélangés sur un même calque, alors que seuls les porteurs entrent dans la descente de charges.

**2. Composants mobilisés** — Geometry Pipeline, List Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le fichier fourni contient 18 points d'implantation sur un calque unique. Séparez les 12 porteurs des 6 cloisons sur deux calques distincts, puis faites compter les porteurs par la définition — sans les désigner un par un.

**4. Données de départ fournies** — Un fichier Rhino contenant les 18 points sur le calque « IMPLANTATION », et une définition prête à référencer un calque.

**5. Résultat attendu** — 12 — le nombre de points sur le calque des porteurs.

**6. Zone CORRIGÉ — explication étape par étape**

1. Créer les deux calques, « PORTEURS » et « CLOISONS », avant toute sélection.
2. Isoler les porteurs par leur régularité — un réseau de sélection ou une fenêtre suffit — et les déplacer sur leur calque.
3. Vérifier qu'il ne reste rien sur le calque d'origine.
4. Faire pointer la définition sur le calque des porteurs, pas sur une sélection.
5. Contrôler que le compte tombe à 12.

**6 bis. Erreur attendue** — Sélectionner les porteurs à la main dans la vue plutôt que de les isoler sur un calque. Le compte est juste aujourd'hui, et faux dès que le géomètre livre une mise à jour — ce que l'exercice ne montre qu'à la seconde livraison.

**6 ter. Justification du jeu de données** — Les porteurs forment une trame régulière de 5 400 × 6 200 mm, les cloisons sont décalées à mi-portée. La distinction est lisible à l'œil dans la vue, ce qui rend le tri manuel tentant — et c'est justement le piège.

**7. Pièges fréquents**

- Masquer les cloisons au lieu de les déplacer : elles restent sur le calque et la définition les reprend quand même.
- Nommer les calques après coup : le lien de la définition se fait sur le nom, un renommage le casse.

**8. Variantes et extensions**

- Ajouter deux porteurs dans Rhino et vérifier que le compte suit tout seul.
- Reprendre les porteurs par un filtre sur la couleur plutôt que sur le calque, et juger ce qui est le plus robuste.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le compte vaut 12 et si aucun point n'a été désigné individuellement.

#### RH-06 — Groupe ou bloc ?

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH2 · Organisation du document |
| **Réf. référentiel** | REF-005 |
| **Niveau** | Débutant |
| **Durée cible** | 6 min |
| **Prérequis** | — |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Un même module de façade est répété quarante fois ; le client demande d'en changer la meneau.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Un module se répète quarante fois et devra être modifié d'un coup. Groupe ou bloc ?
a) Un groupe : il rassemble les objets, c'est fait pour ça.
b) Un bloc : modifier sa définition met à jour les quarante instances. ← réponse
c) Les deux se valent, c'est une affaire d'habitude.
d) Ni l'un ni l'autre, il faut un calque par module.

Valeur diagnostique : (a) et (c) sont la représentation la plus coûteuse du lot. Un groupe ne fait que rassembler une sélection ; il faut alors reprendre les quarante copies une à une. Le bloc porte une définition unique. La différence ne se voit pas au moment où l'on modélise — elle se paie au moment où l'on modifie.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

### RH3 · Modélisation Rhino

*3 exercices — RH-03, RH-04, RH-05*

#### RH-03 — Une trame de plots posée dans Rhino

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH3 · Modélisation Rhino |
| **Réf. référentiel** | REF-007, REF-008, REF-013 |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-02 |
| **Compétence visée** | Produire dans Rhino une répétition régulière d'objets à partir d'un original et d'un pas, et la faire mesurer. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 4 composants |
| **Gamification associée** | G-01 Score visible |
| **Statut de production** | À produire |

**1. Compétence visée** — Produire dans Rhino une répétition régulière d'objets à partir d'un original et d'un pas, et la faire mesurer.

**1 bis. Contexte métier** — Une terrasse sur plots demande un plot tous les 600 mm dans les deux sens, sur une emprise donnée.

**2. Composants mobilisés** — Geometry Pipeline, List Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> L'emprise de la terrasse mesure 4 200 mm sur 3 000 mm. Posez un plot cylindrique de 100 mm de diamètre à chaque nœud d'une trame de 600 mm, le premier au coin d'origine. Donnez le nombre de plots.

**4. Données de départ fournies** — Un fichier Rhino avec l'emprise tracée et un plot modèle à l'origine.

**5. Résultat attendu** — 48 — huit rangées de six plots.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser le plot modèle au coin d'origine de l'emprise.
2. Établir le nombre de nœuds avant de lancer le réseau : 4 200 ÷ 600 = 7 intervalles, donc 8 positions.
3. Lancer le réseau rectangulaire avec 8 et 6 éléments, pas 7 et 5.
4. Vérifier visuellement que les quatre angles portent un plot.
5. Faire compter les plots par la définition, par leur calque.

**6 bis. Erreur attendue** — Compter 4 200 ÷ 600 = 7 plots dans la longueur au lieu de 8. C'est la confusion entre le nombre d'intervalles et le nombre de nœuds, déjà vue en A-10 : ici elle laisse un angle de terrasse sans appui.

**6 ter. Justification du jeu de données** — L'emprise tombe juste sur la trame dans les deux sens, pour que l'exercice porte sur le décompte et non sur le traitement des rives incomplètes.

**7. Pièges fréquents**

- Compter les intervalles au lieu des nœuds.
- Réseau lancé depuis le centre du plot modèle sans vérifier que le premier tombe bien sur l'angle.

**8. Variantes et extensions**

- Porter l'emprise à 4 500 mm et traiter la rive incomplète.
- Passer la trame en quinconce et recompter.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le compte vaut 48 et si les quatre angles sont appuyés.

#### RH-04 — Du profil à la surface

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH3 · Modélisation Rhino |
| **Réf. référentiel** | REF-009, REF-010, REF-011 |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-03 |
| **Compétence visée** | Passer d'une courbe tracée dans Rhino à une surface, et contrôler la grandeur obtenue. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Statut de production** | À produire |

**1. Compétence visée** — Passer d'une courbe tracée dans Rhino à une surface, et contrôler la grandeur obtenue.

**1 bis. Contexte métier** — Un bardage courbe se chiffre à la surface développée ; le tracé vient d'un relevé, la surface doit en découler.

**2. Composants mobilisés** — Geometry Pipeline, Area, Division, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le relevé fournit la ligne au sol du bardage. Produisez la surface du bardage en la montant de 2 800 mm à la verticale, puis donnez sa surface en mètres carrés.

**4. Données de départ fournies** — Un fichier Rhino contenant la courbe de relevé au sol.

**5. Résultat attendu** — La surface du bardage, en mètres carrés, à 0,01 près.

**6. Zone CORRIGÉ — explication étape par étape**

1. Vérifier que la courbe de relevé est bien une seule courbe, non une suite de segments disjoints.
2. Monter la surface à la verticale, pas selon la normale.
3. Référencer la surface dans la définition par son calque.
4. Mesurer l'aire, en millimètres carrés.
5. Convertir en mètres carrés : diviser par un million, pas par mille.

**6 bis. Erreur attendue** — Monter la surface en suivant la normale de la courbe plutôt qu'à la verticale : sur une ligne au sol non plane, la hauteur cesse d'être constante et la surface obtenue n'est plus celle d'un bardage.

**6 ter. Justification du jeu de données** — La ligne au sol présente une courbure variable : une extrusion suivant la normale donnerait un résultat visuellement proche et numériquement différent.

**7. Pièges fréquents**

- Une courbe en plusieurs morceaux produit autant de surfaces, et l'aire mesurée n'est plus celle d'un seul objet.
- Conversion d'unités : un mètre carré vaut un million de millimètres carrés.

**8. Variantes et extensions**

- Incliner le bardage de 10° et mesurer l'écart de surface.
- Découper la surface en lés de 1 200 mm et compter les lés.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si la surface est juste à 0,01 m² près.

#### RH-05 — Percer une platine dans Rhino

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH3 · Modélisation Rhino |
| **Réf. référentiel** | REF-012 |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | RH-04 |
| **Compétence visée** | Combiner des solides par soustraction dans Rhino et quantifier la matière retirée. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 1 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-11 Chasse à l'erreur |
| **Statut de production** | À produire |

**1. Compétence visée** — Combiner des solides par soustraction dans Rhino et quantifier la matière retirée.

**1 bis. Contexte métier** — Une platine d'assemblage reçoit quatre boulons ; la matière retirée entre dans le bilan de poids.

**2. Composants mobilisés** — Geometry Pipeline, Volume, Subtraction, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La platine mesure 300 × 200 × 15 mm. Percez-la de quatre trous traversants de 18 mm de diamètre, centrés à 40 mm de chaque bord. Donnez le volume de matière retirée, en millimètres cubes.

**4. Données de départ fournies** — Un fichier Rhino contenant la platine pleine.

**5. Résultat attendu** — 15 268 mm³ environ — quatre cylindres de 18 mm de diamètre sur 15 mm d'épaisseur.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser les quatre cylindres, plus longs que l'épaisseur de la platine et débordant des deux côtés.
2. Mesurer le volume de la platine pleine avant le perçage.
3. Réaliser la soustraction booléenne.
4. Mesurer le volume après perçage.
5. La différence des deux volumes est la matière retirée — et non le volume des cylindres, qui dépassent.

**6 bis. Erreur attendue** — Percer avec des cylindres exactement à fleur des faces : l'opération booléenne échoue ou laisse une face résiduelle, parce que deux surfaces coplanaires ne se coupent pas proprement. Il faut faire dépasser les cylindres.

**6 ter. Justification du jeu de données** — L'épaisseur de 15 mm et le diamètre de 18 mm sont ceux d'une platine courante pour boulons M16 : les valeurs parlent à qui connaît le métier.

**7. Pièges fréquents**

- Cylindres à fleur : la booléenne échoue silencieusement ou laisse un objet non fermé.
- Prendre le volume des cylindres entiers comme réponse : ils dépassent de la platine.

**8. Variantes et extensions**

- Passer les trous en oblongs et refaire le calcul.
- Chiffrer le poids retiré, en acier à 7 850 kg/m³.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si le volume retiré est juste à 1 mm³ près.

### RH4 · Précision et unités

*1 exercices — RH-07*

#### RH-07 — Le fichier au mauvais millimètre

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH4 · Précision et unités |
| **Réf. référentiel** | REF-015, REF-017 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | — |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Un modèle reçu d'un partenaire arrive mille fois trop petit.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Un fichier reçu s'affiche mille fois trop petit. Que faites-vous ?
a) Mettre le modèle à l'échelle 1000.
b) Vérifier d'abord l'unité du document : il a sans doute été modélisé en mètres et ouvert en millimètres. ← réponse
c) Changer l'unité du document, ce qui remet tout d'aplomb sans toucher au modèle.
d) Redemander le fichier.

Valeur diagnostique : (a) « marche » et laisse une tolérance absolue devenue mille fois trop grossière — les jonctions cesseront de se fermer sans qu'on comprenne pourquoi. (c) est presque juste : changer l'unité ne met pas le modèle à l'échelle, il faut choisir explicitement de le faire. C'est la nuance que la question sert à révéler.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

### RH5 · Préparation à l'impression 3D

*3 exercices — RH-08, RH-09, RH-10*

#### RH-08 — Un caisson vraiment fermé

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH5 · Préparation à l'impression 3D |
| **Réf. référentiel** | REF-019, REF-020, REF-021, REF-022, REF-023 |
| **Niveau** | Débutant |
| **Durée cible** | 25 min |
| **Prérequis** | RH-05 |
| **Compétence visée** | Établir qu'un solide est réellement étanche, et le réparer quand il ne l'est pas. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 1 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-11 Chasse à l'erreur |
| **Statut de production** | À produire |

**1. Compétence visée** — Établir qu'un solide est réellement étanche, et le réparer quand il ne l'est pas.

**1 bis. Contexte métier** — Une pièce partant en impression 3D doit être un volume fermé : une enveloppe ouverte n'a pas d'intérieur, et le trancheur la refuse ou la remplit n'importe comment.

**2. Composants mobilisés** — Geometry Pipeline, Is Solid, Volume, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le caisson fourni paraît fermé mais ne l'est pas. Trouvez ce qui l'empêche, réparez-le, et donnez son volume une fois étanche, en millimètres cubes.

**4. Données de départ fournies** — Un fichier Rhino contenant le caisson, 420 × 260 × 180 mm, auquel il manque deux faces.

**5. Résultat attendu** — 19 656 000 mm³ — le volume du caisson une fois refermé. Une enveloppe ouverte n'en a aucun : c'est là toute la preuve.

**6. Zone CORRIGÉ — explication étape par étape**

1. Ne pas mesurer d'abord : contrôler d'abord l'étanchéité.
2. Afficher les arêtes nues — ce sont elles qui nomment les jonctions défaillantes.
3. Réparer par jonction des faces adjacentes, en resserrant la tolérance si nécessaire.
4. Revérifier qu'il ne reste aucune arête nue.
5. Mesurer alors le volume : sur une enveloppe ouverte, il n'aurait aucun sens.

**6 bis. Erreur attendue** — Se fier à l'aspect. Un caisson non fermé s'affiche exactement comme un caisson fermé : rien à l'écran ne distingue les deux. Seul le contrôle des arêtes nues tranche, et il faut le faire avant de mesurer, pas après.

**6 ter. Justification du jeu de données** — Le caisson s'affiche exactement comme s'il était fermé : rien à l'écran ne distingue une enveloppe ouverte d'un solide. C'est ce qui rend le contrôle numérique indispensable, et non facultatif.

**7. Pièges fréquents**

- Mesurer le volume d'un objet non fermé : la valeur sort quand même, et elle est fausse.
- Élargir la tolérance jusqu'à ce que ça ferme : les faces finissent par se joindre au mauvais endroit.

**8. Variantes et extensions**

- Mesurer le volume avant réparation et chiffrer l'écart.
- Ajouter un congé intérieur et refaire le contrôle.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si l'objet est déclaré solide et si le volume est juste.

#### RH-09 — Une pièce imprimable

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH5 · Préparation à l'impression 3D |
| **Réf. référentiel** | REF-016, REF-018 |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-08 |
| **Compétence visée** | Vérifier qu'une pièce respecte les contraintes dimensionnelles d'une machine avant de la lancer. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Statut de production** | À produire |

**1. Compétence visée** — Vérifier qu'une pièce respecte les contraintes dimensionnelles d'une machine avant de la lancer.

**1 bis. Contexte métier** — L'imprimante du bureau accepte 220 × 220 × 250 mm et ne tient pas une paroi sous 1,2 mm.

**2. Composants mobilisés** — Geometry Pipeline, Bounding Box, Deconstruct Brep, Division, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La pièce fournie doit passer sur cette machine. Établissez le facteur d'échelle maximal qui la fait tenir dans le volume d'impression, arrondi au centième inférieur, et donnez-le.

**4. Données de départ fournies** — Un fichier Rhino contenant la pièce — 380 × 260 × 195 mm hors tout — et les cotes du volume d'impression.

**5. Résultat attendu** — 0,57 — le facteur limitant vient de la longueur : 220 ÷ 380 vaut 0,5789, arrondi vers le bas au centième.

**6. Zone CORRIGÉ — explication étape par étape**

1. Encadrer la pièce pour obtenir ses trois dimensions hors tout.
2. Calculer le rapport disponible sur chacun des trois axes.
3. Retenir le plus petit des trois : c'est lui qui limite.
4. Arrondir vers le bas, jamais au plus proche.
5. Contrôler, après mise à l'échelle, que la paroi la plus fine reste au-dessus de 1,2 mm.

**6 bis. Erreur attendue** — Arrondir le facteur au plus proche plutôt qu'au inférieur. À 0,005 près, la pièce dépasse — et la machine s'en aperçoit après trois heures d'impression, pas avant. Le contexte impose le sens de l'arrondi, comme en A-06.

**6 ter. Justification du jeu de données** — Les trois rapports valent 0,579, 0,846 et 1,282 : le troisième axe passerait sans réduction, et prendre la moyenne des trois donnerait 0,90 — une pièce qui ne rentre pas. C'est le plus petit qui commande.

**7. Pièges fréquents**

- Prendre la moyenne des trois rapports.
- Oublier que la mise à l'échelle réduit aussi les parois : une pièce qui rentre peut devenir non imprimable.

**8. Variantes et extensions**

- Faire pivoter la pièce de 90° et voir si le facteur s'améliore.
- Ajouter une marge de 2 mm sur chaque axe et refaire le calcul.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si le facteur est juste et arrondi vers le bas.

#### RH-10 — Ce que l'export STL perd

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH5 · Préparation à l'impression 3D |
| **Réf. référentiel** | REF-024 |
| **Niveau** | Débutant |
| **Durée cible** | 7 min |
| **Prérequis** | RH-08 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Une pièce parfaitement lisse dans Rhino ressort facettée de l'imprimante.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Votre cylindre est parfait dans Rhino, et il sort facetté de l'imprimante. Pourquoi ?
a) L'imprimante n'est pas assez précise.
b) Le format STL ne connaît que des triangles : la conversion a échantillonné la surface, et la finesse de cet échantillonnage est un réglage. ← réponse
c) Le fichier a été enregistré en basse résolution.
d) Il fallait exporter en OBJ.

Valeur diagnostique : (a) fait accuser la machine et acheter du matériel qui ne changera rien. (d) est faux pour la même raison — l'OBJ maille aussi. La bonne réponse déplace l'attention vers le seul endroit où l'on peut agir : les réglages de maillage au moment de l'export.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

### RH2 · Modélisation Rhino

*4 exercices — RH-14, RH-15, RH-16, RH-17*

#### RH-14 — La trame percée d'une trémie

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH2 · Modélisation Rhino |
| **Réf. référentiel** | REF-013, REF-008 |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-03 |
| **Compétence visée** | Compter les éléments d'un réseau régulier dont une zone a été retirée. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Statut de production** | À produire |

**1. Compétence visée** — Compter les éléments d'un réseau régulier dont une zone a été retirée.

**1 bis. Contexte métier** — La dalle repose sur une trame de plots, sauf à l'aplomb de la trémie d'escalier, où ils sont supprimés.

**2. Composants mobilisés** — Multiplication, Subtraction, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La trame compte huit plots en longueur et six en largeur, au pas de 1 200 mm. La trémie en supprime trois en longueur et deux en largeur. Donnez le nombre de plots.

**4. Données de départ fournies** — Les dimensions de la trame, son pas, et l'emprise de la trémie en nombre de plots.

**5. Résultat attendu** — 42 plots — 48 moins les 6 de la trémie.

**6. Zone CORRIGÉ — explication étape par étape**

1. Compter la trame complète.
2. Compter l'emprise de la trémie comme un rectangle.
3. Soustraire.

**6 bis. Erreur attendue** — Retrancher 3 + 2 = 5 au lieu de 3 × 2 = 6. La trémie retire un RECTANGLE de plots, pas une ligne et une colonne : l'erreur ne se voit pas sur le compte, mais le plot qu'on a oublié de retirer se retrouve au milieu de l'escalier.

**6 ter. Justification du jeu de données** — Huit par six donne un total, 48, qui ne se confond avec aucune des réponses fausses ; et 3 × 2 = 6 se distingue nettement de 3 + 2 = 5, donc 42 de 43.

**7. Pièges fréquents**

- Additionner les deux dimensions de la trémie.
- Compter les intervalles au lieu des plots.

**8. Variantes et extensions**

- Donner la position du dernier plot depuis l'origine.
- Ajouter une seconde trémie, qui chevauche la première d'un plot.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le compte est juste.

#### RH-15 — Le développé d'un cheminement

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH2 · Modélisation Rhino |
| **Réf. référentiel** | REF-009 |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-14 |
| **Compétence visée** | Mesurer la longueur réellement parcourue par une polyligne, et non la distance entre ses extrémités. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Statut de production** | À produire |

**1. Compétence visée** — Mesurer la longueur réellement parcourue par une polyligne, et non la distance entre ses extrémités.

**1 bis. Contexte métier** — On chiffre un linéaire de garde-corps le long d'un cheminement qui tourne quatre fois.

**2. Composants mobilisés** — Point, Polyline, Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les six sommets du cheminement vous sont fournis. Donnez sa longueur développée, en millimètres.

**4. Données de départ fournies** — Les coordonnées en plan des six sommets.

**5. Résultat attendu** — 13 400 mm — la somme des cinq segments.

**6. Zone CORRIGÉ — explication étape par étape**

1. Relier les sommets dans l'ordre.
2. Mesurer la courbe obtenue, et non la distance entre ses extrémités.

**6 bis. Erreur attendue** — Mesurer la distance du premier au dernier point : 10 065 mm. C'est la corde, pas le parcours — et 3,3 m de garde-corps manqueraient à la livraison.

**6 ter. Justification du jeu de données** — Cinq segments orthogonaux de longueurs différentes, et un écart de 25 % entre la corde et le développé : assez grand pour que l'erreur se voie au chiffrage, assez petit pour qu'elle ne saute pas aux yeux sur le plan.

**7. Pièges fréquents**

- Mesurer la corde.
- Fermer la polyligne sans que la consigne le demande.

**8. Variantes et extensions**

- Donner la longueur de chaque segment, pour le débit.
- Ajouter un congé de 300 mm à chaque angle et reprendre la mesure.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le développé est juste.

#### RH-16 — La surface d'un rampant

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH2 · Modélisation Rhino |
| **Réf. référentiel** | REF-010, REF-011 |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-15 |
| **Compétence visée** | Mesurer une surface inclinée dans son plan, et non dans sa projection horizontale. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Statut de production** | À produire |

**1. Compétence visée** — Mesurer une surface inclinée dans son plan, et non dans sa projection horizontale.

**1 bis. Contexte métier** — On commande la couverture d'un appentis : le couvreur pose sur le rampant, le plan le montre en projection.

**2. Composants mobilisés** — Multiplication, Addition, Square Root, Division, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> L'appentis mesure 8 400 mm de long, 3 200 mm de profondeur en projection, pour un dénivelé de 1 500 mm. Donnez la surface de couverture à commander, en mètres carrés.

**4. Données de départ fournies** — La longueur, la profondeur en projection et le dénivelé.

**5. Résultat attendu** — 29,69 m² — la surface du rampant, à 0,01 près.

**6. Zone CORRIGÉ — explication étape par étape**

1. Calculer la longueur du rampant par le théorème de Pythagore.
2. Multiplier par la longueur de l'appentis.
3. Convertir en mètres carrés.

**6 bis. Erreur attendue** — Multiplier la longueur par la profondeur en projection : 26,88 m². Il manque 2,81 m², soit près de 10 % — de quoi arrêter le chantier à trois rangs de la faîtière.

**6 ter. Justification du jeu de données** — Un dénivelé de 1 500 pour 3 200 de projection fait une pente de 25°, courante en appentis. L'écart de 10 % entre les deux réponses est trop petit pour se voir sur un plan, trop grand pour se rattraper sur une commande.

**7. Pièges fréquents**

- Prendre la profondeur en projection pour le rampant.
- Oublier la conversion en mètres carrés.

**8. Variantes et extensions**

- Ajouter un débord de 400 mm et reprendre.
- Donner le nombre de plaques de 2 000 × 1 050 mm nécessaires.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si la surface du rampant est juste à 0,01 m² près.

#### RH-17 — Le volume de deux blocs qui se recouvrent

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH2 · Modélisation Rhino |
| **Réf. référentiel** | REF-012 |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-05 |
| **Compétence visée** | Calculer le volume d'une réunion de solides sans compter deux fois la matière commune. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Statut de production** | À produire |

**1. Compétence visée** — Calculer le volume d'une réunion de solides sans compter deux fois la matière commune.

**1 bis. Contexte métier** — Deux massifs de béton se recoupent en angle. On commande le béton au volume.

**2. Composants mobilisés** — Multiplication, Addition, Subtraction, Division, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le premier massif mesure 400 × 300 × 200 mm, le second 250 × 350 × 180 mm, et leur recouvrement 150 × 200 × 180 mm. Donnez le volume de béton, en décimètres cubes.

**4. Données de départ fournies** — Les dimensions des deux massifs et celles de leur recouvrement.

**5. Résultat attendu** — 34,35 dm³ — la réunion des deux massifs.

**6. Zone CORRIGÉ — explication étape par étape**

1. Calculer chaque volume.
2. Additionner les deux massifs.
3. Retrancher une fois le recouvrement.
4. Convertir en décimètres cubes.

**6 bis. Erreur attendue** — Additionner les deux volumes : 39,75 dm³. La zone commune est alors comptée deux fois — 5,4 dm³ de béton commandés pour rien, et l'erreur se répète à chaque massif de la série.

**6 ter. Justification du jeu de données** — Le recouvrement représente 14 % de la réunion : assez pour que l'écart se voie sur une commande, assez peu pour qu'on l'oublie. Les trois volumes sont donnés, de sorte que l'exercice porte sur le raisonnement et non sur la construction géométrique.

**7. Pièges fréquents**

- Additionner sans retrancher.
- Retrancher deux fois le recouvrement.

**8. Variantes et extensions**

- Traiter trois massifs dont deux recouvrements.
- Donner le volume de la seule zone commune.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si le volume de la réunion est juste.

### RH3 · Préparation à l'impression 3D

*5 exercices — RH-18, RH-19, RH-20, RH-21, RH-22*

#### RH-18 — Les parois que la machine ne saura pas faire

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH3 · Préparation à l'impression 3D |
| **Réf. référentiel** | REF-016 |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-08 |
| **Compétence visée** | Confronter une pièce aux contraintes de la machine avant de lancer une impression. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Statut de production** | À produire |

**1. Compétence visée** — Confronter une pièce aux contraintes de la machine avant de lancer une impression.

**1 bis. Contexte métier** — La machine ne descend pas sous 1,2 mm de paroi. En deçà, elle imprime quelque chose — qui casse à la première manipulation.

**2. Composants mobilisés** — Nombre, Smaller Than, Cull Pattern, List Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les quatorze épaisseurs de paroi relevées sur la pièce vous sont fournies. Donnez le nombre de parois strictement inférieures au minimum imprimable de 1,2 mm.

**4. Données de départ fournies** — Les quatorze épaisseurs relevées, en millimètres, et le minimum imprimable.

**5. Résultat attendu** — 5 parois passent sous le minimum.

**6. Zone CORRIGÉ — explication étape par étape**

1. Comparer chaque épaisseur au minimum.
2. Choisir sciemment entre strict et large.
3. Compter.

**6 bis. Erreur attendue** — Compter 6 en incluant la paroi qui vaut exactement 1,2 mm. Le minimum est atteignable : c'est un minimum, pas une borne exclue. Se tromper de sens conduit à reprendre une paroi qui n'en avait pas besoin — ou, dans l'autre sens, à en laisser passer une.

**6 ter. Justification du jeu de données** — Quatorze relevés, dont un exactement au minimum et trois entre 1,1 et 1,25 : la frontière est peuplée, et le sens de la comparaison change la réponse d'exactement un.

**6 quater. Limite de la correction automatique** — L'exercice compte les parois trop minces. Il ne dit pas comment les épaissir — ce qui suppose de savoir laquelle est structurelle et laquelle est décorative.

**7. Pièges fréquents**

- Inclure la paroi qui vaut exactement le minimum.
- Juger sur l'aperçu plutôt que sur les relevés.

**8. Variantes et extensions**

- Donner l'épaisseur minimale relevée.
- Reprendre avec une machine descendant à 0,8 mm.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le compte est juste et strict.

#### RH-19 — Ce que la mise à l'échelle fait aux détails

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH3 · Préparation à l'impression 3D |
| **Réf. référentiel** | REF-017, REF-018 |
| **Niveau** | Débutant |
| **Durée cible** | 25 min |
| **Prérequis** | RH-07 |
| **Compétence visée** | Juger la finesse d'un modèle À L'ÉCHELLE OÙ IL SERA IMPRIMÉ, et non à celle où il a été dessiné. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Statut de production** | À produire |

**1. Compétence visée** — Juger la finesse d'un modèle à l'échelle où il sera imprimé, et non à celle où il a été dessiné.

**1 bis. Contexte métier** — La maquette d'étude est dessinée au 1:25 et sera imprimée à l'échelle 1. La machine ne distingue rien sous 0,4 mm.

**2. Composants mobilisés** — Multiplication, Smaller Than, Cull Pattern, List Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les douze détails les plus fins du modèle vous sont fournis, mesurés sur la maquette. Le modèle sera agrandi 25 fois. Donnez le nombre de détails qui resteront sous la résolution de 0,4 mm APRÈS agrandissement.

**4. Données de départ fournies** — Les douze dimensions relevées sur la maquette, le facteur d'agrandissement et la résolution de la machine.

**5. Résultat attendu** — 6 détails restent sous la résolution après agrandissement.

**6. Zone CORRIGÉ — explication étape par étape**

1. Appliquer le facteur d'échelle à chaque détail.
2. Comparer ensuite à la résolution de la machine.
3. Compter.

**6 bis. Erreur attendue** — Juger avant l'agrandissement : les douze détails sont alors sous 0,4 mm, et l'on conclut que rien n'est imprimable. L'agrandissement en sauve la moitié — refaire toute la maquette pour rien est une décision coûteuse fondée sur une comparaison faite à la mauvaise échelle.

**6 ter. Justification du jeu de données** — Les douze détails sont tous sous la résolution avant agrandissement et six seulement après : les deux réponses, 12 et 6, sont dans un rapport de deux, et la première est aussi le nombre total de détails — ce qui la rend immédiatement suspecte à qui la relit.

**7. Pièges fréquents**

- Comparer avant d'agrandir.
- Oublier que la tolérance du document, elle aussi, suit l'échelle.

**8. Variantes et extensions**

- Trouver le facteur minimal qui sauve tous les détails.
- Reprendre avec une machine à 0,2 mm de résolution.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le compte après agrandissement est juste.

#### RH-20 — Un maillage est-il fermé

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH3 · Préparation à l'impression 3D |
| **Réf. référentiel** | REF-019, REF-020, REF-021 |
| **Niveau** | Débutant |
| **Durée cible** | 25 min |
| **Prérequis** | RH-08 |
| **Compétence visée** | Établir par le calcul qu'un maillage est ouvert, et de combien, sans se fier à son apparence. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Statut de production** | À produire |

**1. Compétence visée** — Établir par le calcul qu'un maillage est ouvert, et de combien, sans se fier à son apparence.

**1 bis. Contexte métier** — Le maillage part à l'impression. À l'écran, il paraît parfaitement fermé — c'est toujours le cas.

**2. Composants mobilisés** — Multiplication, Subtraction, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le maillage compte 2 960 faces triangulaires et 4 434 arêtes. Donnez le nombre d'arêtes nues.

**4. Données de départ fournies** — Le nombre de faces triangulaires et le nombre d'arêtes.

**5. Résultat attendu** — 12 arêtes nues.

**6. Zone CORRIGÉ — explication étape par étape**

1. Compter les arêtes qu'exigent les faces : trois par triangle.
2. Compter celles qu'offrent les arêtes réelles : deux usages chacune si elles sont intérieures.
3. La différence est le nombre d'arêtes nues.

**6 bis. Erreur attendue** — Conclure que le maillage est fermé parce que rien ne se voit. Un maillage fermé de 2 960 triangles aurait exactement 4 440 arêtes : chaque arête y est partagée par deux faces. Il en manque six, donc douze arêtes ne sont bordées que d'une seule face — et la pièce sortira de la machine avec un trou.

**6 ter. Justification du jeu de données** — Le raisonnement tient en une ligne : trois arêtes par triangle, deux triangles par arête intérieure, donc 3F − 2E arêtes nues. Douze arêtes nues sur 4 434, c'est 0,3 % — invisible à l'œil, rédhibitoire à la machine.

**6 quater. Limite de la correction automatique** — Le compte dit qu'il y a des trous, pas où ils sont. Les localiser demande les outils d'analyse, que RH-21 aborde.

**7. Pièges fréquents**

- Se fier à l'aperçu.
- Confondre arêtes nues et faces manquantes.

**8. Variantes et extensions**

- Retrouver le nombre d'arêtes d'un maillage fermé de même nombre de faces.
- Refaire le calcul pour un maillage quadrangulaire.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre d'arêtes nues est juste.

#### RH-21 — Les faces qui ne mesurent rien

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH3 · Préparation à l'impression 3D |
| **Réf. référentiel** | REF-022, REF-023 |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | RH-20 |
| **Compétence visée** | Repérer les faces dégénérées d'un maillage avant de le réparer, en s'appuyant sur la tolérance du document. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Statut de production** | À produire |

**1. Compétence visée** — Repérer les faces dégénérées d'un maillage avant de le réparer, en s'appuyant sur la tolérance du document.

**1 bis. Contexte métier** — Le maillage vient d'une conversion. Certaines faces sont réduites à un fil : elles ne se voient pas, et font échouer la réparation automatique.

**2. Composants mobilisés** — Nombre, Smaller Than, Cull Pattern, List Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les aires des quinze faces suspectes vous sont fournies, en millimètres carrés. La tolérance du document vaut 0,001 mm². Donnez le nombre de faces dégénérées.

**4. Données de départ fournies** — Les quinze aires relevées et la tolérance du document.

**5. Résultat attendu** — 4 faces dégénérées.

**6. Zone CORRIGÉ — explication étape par étape**

1. Comparer chaque aire à la tolérance, et non à zéro.
2. Compter.
3. Retenir que la face à 0,0012 n'est pas dégénérée au sens du document.

**6 bis. Erreur attendue** — Comparer à zéro. Aucune face n'a une aire exactement nulle : elles valent 0,0003 à 0,0012 mm², ce qui n'est pas zéro mais n'est rien à l'échelle du document. Une comparaison à zéro n'en trouve aucune, et la réparation échoue sans dire pourquoi.

**6 ter. Justification du jeu de données** — Cinq faces sous le millième de millimètre carré, dont une à 0,0012 qui passe JUSTE au-dessus de la tolérance : la réponse est 4, et non 5. C'est la tolérance qui tranche, pas l'intuition.

**7. Pièges fréquents**

- Comparer à zéro.
- Prendre une tolérance choisie au jugé plutôt que celle du document.

**8. Variantes et extensions**

- Reprendre avec une tolérance de 0,01 mm².
- Donner l'aire totale perdue par la suppression de ces faces.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le compte est juste.

#### RH-22 — La finesse du maillage à l'export

| Rubrique | Valeur |
|---|---|
| **Lot** | RH — Socle Rhino |
| **Thématique** | RH3 · Préparation à l'impression 3D |
| **Réf. référentiel** | REF-024 |
| **Niveau** | Débutant |
| **Durée cible** | 25 min |
| **Prérequis** | RH-10 |
| **Compétence visée** | Régler la finesse d'un maillage d'export à partir de l'écart admissible à la surface, et non au jugé. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Statut de production** | À produire |

**1. Compétence visée** — Régler la finesse d'un maillage d'export à partir de l'écart admissible à la surface, et non au jugé.

**1 bis. Contexte métier** — Le cylindre part en fabrication. Le maillage d'export remplace le cercle par un polygone : la question est de savoir de combien il s'en écarte.

**2. Composants mobilisés** — Division, Subtraction, ArcCos, Pi, Round, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le cylindre a 30 mm de rayon. L'écart entre le maillage et la surface réelle ne doit pas dépasser 0,05 mm. Donnez le nombre minimal de facettes sur un demi-tour.

**4. Données de départ fournies** — Le rayon du cylindre et l'écart maximal admis.

**5. Résultat attendu** — 55 facettes sur un demi-tour.

**6. Zone CORRIGÉ — explication étape par étape**

1. Écrire l'écart entre la corde et l'arc en fonction du nombre de facettes.
2. Inverser la relation pour obtenir le nombre de facettes.
3. Arrondir au SUPÉRIEUR.
4. Vérifier l'écart obtenu, et celui d'une facette de moins.

**6 bis. Erreur attendue** — Régler la finesse sur un curseur, au jugé, jusqu'à ce que l'aperçu paraisse lisse. L'aperçu paraît lisse bien avant que l'écart soit tenu — à 54 facettes il vaut déjà 0,0508 mm, au-delà du toléré, et rien à l'écran ne le signale.

**6 ter. Justification du jeu de données** — L'écart d'une corde à son arc vaut r(1 − cos(π/n)). Avec r = 30 et 0,05 mm admis, n vaut 54,41 : la frontière tombe entre deux entiers, de sorte qu'un arrondi au plus proche donnerait 54 — qui ne tient pas l'écart. C'est un arrondi au SUPÉRIEUR.

**6 quater. Limite de la correction automatique** — Le calcul porte sur la circonférence. La finesse selon l'axe, elle, ne dépend pas de l'écart mais du procédé.

**7. Pièges fréquents**

- Arrondir au plus proche.
- Régler au jugé sur l'aperçu.
- Confondre l'écart à la surface et la longueur de la corde.

**8. Variantes et extensions**

- Refaire pour un rayon de 5 mm : le nombre de facettes change peu, le poids du fichier beaucoup.
- Chiffrer le poids du fichier obtenu.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre de facettes est juste et arrondi au supérieur.

---

## Lot GP — Géométrie paramétrique appliquée

**Niveau** : Débutant à perfectionnement · **8 exercices** · **3 h 17 cumulées**

Géométrie paramétrique appliquée : plan coté qui suit ses paramètres, modèle 3D complet, maillages et SubD.

| ID | Titre | Thématique | Niveau | Durée | Validation |
|---|---|---|---|---|---|
| GP-01 | Un plan coté qui suit ses paramètres | GP1 · Plan paramétrique | Débutant | 25 min | NumericTolerance |
| GP-02 | Un modèle paramétrique de bout en bout | GP2 · Synthèse géométrie | Intermédiaire | 45 min | NumericTolerance |
| GP-03 | Un maillage qu'on peut imprimer | GP3 · Maillages et SubD | Perfectionnement | 30 min | NumericTolerance |
| GP-04 | SubD ou NURBS ? | GP3 · Maillages et SubD | Perfectionnement | 7 min | — |
| GP-05 | La chaîne de cotes d'une façade | GP3 · Plan paramétrique | Intermédiaire | 25 min | SingleValue |
| GP-06 | Les sommets d'une nappe maillée | GP4 · Maillages et SubD | Perfectionnement | 20 min | SingleValue |
| GP-07 | Ce que la soudure retire | GP4 · Maillages et SubD | Perfectionnement | 25 min | SingleValue |
| GP-08 | Ce que coûte une subdivision de plus | GP4 · Maillages et SubD | Perfectionnement | 20 min | SingleValue |

### GP1 · Plan paramétrique

*1 exercices — GP-01*

#### GP-01 — Un plan coté qui suit ses paramètres

| Rubrique | Valeur |
|---|---|
| **Lot** | GP — Géométrie paramétrique appliquée |
| **Thématique** | GP1 · Plan paramétrique |
| **Réf. référentiel** | REF-065, REF-066 |
| **Niveau** | Débutant |
| **Durée cible** | 25 min |
| **Prérequis** | A-34 |
| **Compétence visée** | Produire un tracé 2D dont les cotes se mettent à jour avec la géométrie, plutôt que d'être écrites à côté. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0,1 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Statut de production** | À produire |

**1. Compétence visée** — Produire un tracé 2D dont les cotes se mettent à jour avec la géométrie, plutôt que d'être écrites à côté.

**1 bis. Contexte métier** — Un plan de réservation part au gros œuvre ; la dimension bouge encore, et une cote fausse coûte un percement au mauvais endroit.

**2. Composants mobilisés** — Rectangle, Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La réservation est rectangulaire, avec un congé de 60 mm à chaque angle. Produisez son tracé pour une réservation de 1 400 × 850 mm, et donnez le périmètre développé du contour.

**4. Données de départ fournies** — Deux valeurs réglables pour la largeur et la hauteur, et une troisième pour le rayon de congé.

**5. Résultat attendu** — Le périmètre du contour congé compris, à 0,1 mm près.

**6. Zone CORRIGÉ — explication étape par étape**

1. Construire le rectangle à partir des deux valeurs réglables.
2. Appliquer le congé par le paramètre du composant de tracé plutôt qu'en raccordant les angles après coup.
3. Mesurer la longueur du contour obtenu.
4. Faire varier la largeur et vérifier que la cote suit.
5. Contrôler le résultat sur un cas connu : congé nul, le périmètre doit valoir deux fois la somme des côtés.

**6 bis. Erreur attendue** — Calculer le périmètre du rectangle nu et y ajouter les quatre quarts de cercle, sans retrancher ce que les congés ont supprimé des côtés droits. On obtient une valeur trop grande d'environ 4 × (2r − πr/2), soit une erreur systématique que le contexte ne signale pas.

**6 ter. Justification du jeu de données** — Le congé de 60 mm est assez grand pour que l'oubli du retranchement se voie au dixième de millimètre, et assez petit pour rester une réservation plausible.

**7. Pièges fréquents**

- Congé appliqué après coup : le contour cesse d'être une seule courbe et la mesure porte sur des morceaux.
- Rayon de congé supérieur à la moitié du petit côté : le tracé devient impossible et le composant se met en défaut.

**8. Variantes et extensions**

- Ajouter une cotation automatique de la largeur et vérifier qu'elle suit la valeur réglable.
- Passer le congé à zéro et retrouver le périmètre du rectangle.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si le périmètre est juste à 0,1 mm près et si la cote suit une modification de largeur.

### GP2 · Synthèse géométrie

*1 exercices — GP-02*

#### GP-02 — Un modèle paramétrique de bout en bout

| Rubrique | Valeur |
|---|---|
| **Lot** | GP — Géométrie paramétrique appliquée |
| **Thématique** | GP2 · Synthèse géométrie |
| **Réf. référentiel** | REF-073 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 45 min |
| **Prérequis** | GP-01, A-41 |
| **Compétence visée** | Enchaîner tracé, surface et volume dans une définition unique dont un seul paramètre commande l'ensemble. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0,001 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-25 Projet jalonné |
| **Statut de production** | À produire |

**1. Compétence visée** — Enchaîner tracé, surface et volume dans une définition unique dont un seul paramètre commande l'ensemble.

**1 bis. Contexte métier** — Un escalier droit doit être chiffré en volume de béton avant que sa hauteur d'étage soit figée.

**2. Composants mobilisés** — Round, Division, Series, Multiplication, Mass Addition, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> L'escalier est massif, 1 100 mm de large, giron de 280 mm. Pour une hauteur d'étage de 2 700 mm et une hauteur de marche visée de 175 mm, produisez le volume de béton, en mètres cubes.

**4. Données de départ fournies** — Trois valeurs réglables : hauteur d'étage, hauteur de marche visée et giron.

**5. Résultat attendu** — 6,653 m³ — le volume de béton de l'escalier massif, à 0,001 près.

**6. Zone CORRIGÉ — explication étape par étape**

1. Établir le nombre de contremarches : hauteur d'étage divisée par la hauteur visée, arrondi à l'entier le plus proche.
2. En déduire la hauteur de marche réelle : hauteur d'étage divisée par ce nombre entier.
3. Répartir les marches par une suite régulière.
4. Chaque marche est un bloc de giron × largeur × sa hauteur cumulée : la première monte d'une hauteur, la quinzième de quinze.
5. Mesurer le volume et convertir en mètres cubes.

**6 bis. Erreur attendue** — Garder 175 mm comme hauteur de marche réelle. 2 700 ÷ 175 vaut 15,43 : le nombre de contremarches s'arrondit à 15, et c'est alors la HAUTEUR qui se recale, à 180 mm. Conserver 175 mm donne un escalier de 2 625 mm qui n'atteint pas l'étage — de trois quarts de marche.

**6 ter. Justification du jeu de données** — 2 700 n'est pas divisible par 175 : c'est le cas normal, et c'est ce qui oblige à comprendre lequel des deux nombres est la donnée et lequel est le résultat.

**7. Pièges fréquents**

- Prendre la hauteur de marche comme hauteur de chaque bloc : on obtient le volume d'une seule assise, pas de l'escalier.
- Oublier que la dernière contremarche arrive au niveau fini, et poser une marche de trop.

**8. Variantes et extensions**

- Faire varier la hauteur d'étage et vérifier que le nombre de marches se recale seul.
- Ajouter un palier intermédiaire et reprendre le calcul.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — Grille : nombre de marches juste (1), hauteur réelle recalculée (1), volume juste (2).

### GP3 · Maillages et SubD

*2 exercices — GP-03, GP-04*

#### GP-03 — Un maillage qu'on peut imprimer

| Rubrique | Valeur |
|---|---|
| **Lot** | GP — Géométrie paramétrique appliquée |
| **Thématique** | GP3 · Maillages et SubD |
| **Réf. référentiel** | REF-074, REF-075, REF-076 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | RH-08 |
| **Compétence visée** | Produire un maillage à partir d'une surface, en maîtriser la finesse, et le rendre exploitable. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 5 % |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Statut de production** | À produire |

**1. Compétence visée** — Produire un maillage à partir d'une surface, en maîtriser la finesse, et le rendre exploitable.

**1 bis. Contexte métier** — Une pièce de forme libre part en impression : le trancheur n'accepte qu'un maillage fermé, et la finesse décide de la qualité comme du poids du fichier.

**2. Composants mobilisés** — Mesh Brep, Mesh Join, Face Count, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La surface fournie doit devenir un maillage fermé dont l'écart à la surface d'origine ne dépasse nulle part 0,2 mm. Donnez le nombre de faces du maillage obtenu.

**4. Données de départ fournies** — Un fichier contenant la surface fermée d'origine.

**5. Résultat attendu** — 1 024 faces avec les réglages par défaut du mailleur — la correction accepte 5 % autour de cette valeur.

**6. Zone CORRIGÉ — explication étape par étape**

1. Mailler la surface en fixant l'écart maximal, non la densité.
2. Vérifier que le maillage est fermé et sans face dégénérée.
3. Réparer les jonctions si le maillage sort en morceaux.
4. Compter les faces.
5. Contrôler le poids du fichier exporté : c'est la contrepartie directe de la finesse.

**6 bis. Erreur attendue** — Augmenter la densité jusqu'à ce que « ça ait l'air bien ». L'écart maximal est un réglage explicite : à l'œil, on produit soit un maillage grossier qui passe pour lisse à l'écran, soit un maillage inutilement lourd.

**6 ter. Justification du jeu de données** — La surface présente une zone de forte courbure et une zone plane : un maillage à densité uniforme y est toujours mauvais quelque part, ce qui oblige à passer par le critère d'écart.

**6 quater. Limite de la correction automatique** — Le corrigé maille avec les réglages PAR DÉFAUT, et rend 1 024 faces. Il ne pilote pas l'écart maximal : ce réglage se pose dans la boîte de dialogue de maillage et ne se transporte pas dans le fichier. Le corrigé sert donc d'ordre de grandeur ; c'est au formateur de vérifier que l'apprenant a bien raisonné en écart et non en densité.

**7. Pièges fréquents**

- Régler la densité au lieu de l'écart : le résultat n'est plus contrôlable.
- Maillage en plusieurs morceaux non joints : il paraît fermé et ne l'est pas.

**8. Variantes et extensions**

- Doubler l'écart admis et mesurer le gain en nombre de faces.
- Lisser le maillage et vérifier ce que le lissage fait à l'écart.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si l'écart maximal est respecté et le maillage fermé.

#### GP-04 — SubD ou NURBS ?

| Rubrique | Valeur |
|---|---|
| **Lot** | GP — Géométrie paramétrique appliquée |
| **Thématique** | GP3 · Maillages et SubD |
| **Réf. référentiel** | REF-077, REF-078 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 7 min |
| **Prérequis** | GP-03 |
| **Case Bloom (révisée)** | Évaluer × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Une poignée de meuble doit être dessinée en forme libre, puis usinée.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Vous devez dessiner une poignée de forme libre, qui sera ensuite usinée à partir d'un modèle exact. Par quoi commencez-vous ?
a) Directement en NURBS, puisque c'est ce qu'il faut à la fin.
b) En SubD pour la recherche de forme, converti en NURBS pour l'usinage. ← réponse
c) En maillage, plus simple à déformer.
d) Peu importe, les trois sont équivalents.

Valeur diagnostique : (a) est le réflexe de qui connaît la contrainte de sortie et pas les outils de forme — on y passe un temps considérable à recaler des points de contrôle. (c) donne une forme facile à modeler et impossible à usiner proprement. La bonne réponse tient à ce que SubD et NURBS ne s'opposent pas : l'un sert la conception, l'autre la fabrication, et la conversion est prévue pour.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

### GP3 · Plan paramétrique

*1 exercices — GP-05*

#### GP-05 — La chaîne de cotes d'une façade

| Rubrique | Valeur |
|---|---|
| **Lot** | GP — Géométrie paramétrique appliquée |
| **Thématique** | GP3 · Plan paramétrique |
| **Réf. référentiel** | REF-065, REF-066 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | GP-01 |
| **Compétence visée** | Produire une cotation en chaîne qui se recalcule avec le modèle, en distinguant ce qui se mesure d'un voisin à l'autre de ce qui se repère depuis une origine unique. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-08 Relevé contradictoire |
| **Statut de production** | À produire |

**1. Compétence visée** — Produire une cotation en chaîne qui se recalcule avec le modèle, en distinguant ce qui se mesure d'un voisin à l'autre de ce qui se repère depuis une origine unique.

**1 bis. Contexte métier** — Le poseur implante les percements d'une façade au décamètre, depuis un unique point de référence : c'est la seule manière de ne pas cumuler les erreurs de report.

**2. Composants mobilisés** — Nombre, Mass Addition, Addition, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le bureau d'études fournit les entraxes des sept percements, mesurés chacun depuis le précédent, et la distance du premier au point de référence. Donnez la cote du dernier percement telle qu'elle doit figurer au plan de pose, en millimètres.

**4. Données de départ fournies** — La distance du premier percement au point de référence, et les sept entraxes successifs, en millimètres.

**5. Résultat attendu** — 8 955 mm — la position du dernier percement, comptée depuis le point de référence.

**6. Zone CORRIGÉ — explication étape par étape**

1. Distinguer la donnée relative (l'entraxe) de la donnée absolue (la position depuis l'origine).
2. Cumuler les entraxes.
3. Ajouter l'écart d'origine.
4. Vérifier que la première cote vaut bien l'écart d'origine, et non zéro.

**6 bis. Erreur attendue** — Reporter le dernier entraxe (1 290 mm) ou la somme des seuls entraxes (8 535 mm). Le premier oublie que l'entraxe est une distance relative ; le second oublie l'écart d'origine. Sur le chantier, les deux se traduisent par un percement au mauvais endroit — et l'un des deux le met à 420 mm près, un écart assez petit pour n'être vu qu'une fois la menuiserie livrée.

**6 ter. Justification du jeu de données** — Sept entraxes irréguliers, aucun multiple d'un pas commun : la cote finale ne se retrouve pas de tête. L'écart d'origine de 420 mm est du même ordre qu'un tableau de baie, donc plausible et facile à oublier.

**6 quater. Limite de la correction automatique** — L'exercice valide la cote finale, pas la cotation entière. Une chaîne juste sur son dernier maillon peut être fausse au milieu : le formateur regarde le graphe, pas seulement la réponse.

**7. Pièges fréquents**

- Confondre entraxe et cote cumulée.
- Oublier l'écart entre le point de référence et le premier percement.
- Coter chaque percement depuis son voisin sur le plan de pose : les erreurs de report s'additionnent alors.

**8. Variantes et extensions**

- Produire la chaîne complète des huit cotes, et non la seule dernière.
- Ajouter un percement au milieu et vérifier que toutes les cotes suivantes se recalculent seules.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si la cote finale est juste.

### GP4 · Maillages et SubD

*3 exercices — GP-06, GP-07, GP-08*

#### GP-06 — Les sommets d'une nappe maillée

| Rubrique | Valeur |
|---|---|
| **Lot** | GP — Géométrie paramétrique appliquée |
| **Thématique** | GP4 · Maillages et SubD |
| **Réf. référentiel** | REF-074 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 20 min |
| **Prérequis** | GP-03 |
| **Compétence visée** | Distinguer le nombre de faces d'un maillage de son nombre de sommets, et savoir lequel commande quoi. |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Statut de production** | À produire |

**1. Compétence visée** — Distinguer le nombre de faces d'un maillage de son nombre de sommets, et savoir lequel commande quoi.

**1 bis. Contexte métier** — La nappe part vers un calcul aux éléments finis, qui se dimensionne au nombre de NŒUDS, pas de faces.

**2. Composants mobilisés** — Addition, Multiplication, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La nappe est maillée en 48 divisions dans un sens et 30 dans l'autre, en quadrangles. Donnez le nombre de sommets.

**4. Données de départ fournies** — Les deux nombres de divisions.

**5. Résultat attendu** — 1 519 sommets — 49 × 31.

**6. Zone CORRIGÉ — explication étape par étape**

1. Compter les rangées de sommets dans chaque sens : une de plus que les divisions.
2. Multiplier.

**6 bis. Erreur attendue** — Répondre 1 440, le nombre de faces. Un maillage de n divisions a n + 1 rangées de sommets : l'écart de 79 sommets ne se voit pas sur l'image, mais il change la taille du système à résoudre.

**6 ter. Justification du jeu de données** — 48 et 30 sont des divisions courantes pour une nappe d'étude. Les deux réponses — 1 440 et 1 519 — sont assez proches pour qu'on ne les distingue pas à vue, assez différentes pour que le calcul ne soit pas le même.

**7. Pièges fréquents**

- Multiplier les divisions entre elles.
- Oublier que le maillage n'est pas fermé sur lui-même.

**8. Variantes et extensions**

- Donner le nombre d'arêtes.
- Reprendre pour une nappe refermée dans un sens.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre de sommets est juste.

#### GP-07 — Ce que la soudure retire

| Rubrique | Valeur |
|---|---|
| **Lot** | GP — Géométrie paramétrique appliquée |
| **Thématique** | GP4 · Maillages et SubD |
| **Réf. référentiel** | REF-076 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | GP-06 |
| **Compétence visée** | Mesurer la redondance d'un maillage construit face par face, et ce que la soudure des sommets lui retire. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-16 Livrable pesé |
| **Statut de production** | À produire |

**1. Compétence visée** — Mesurer la redondance d'un maillage construit face par face, et ce que la soudure des sommets lui retire.

**1 bis. Contexte métier** — Le maillage a été construit quadrangle par quadrangle. Chaque face porte ses quatre sommets, sans savoir que ses voisines portent les mêmes.

**2. Composants mobilisés** — Multiplication, Addition, Subtraction, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La nappe compte 48 divisions par 30, en quadrangles construits un à un. Donnez le nombre de sommets que la soudure supprimera.

**4. Données de départ fournies** — Les deux nombres de divisions, et le mode de construction face par face.

**5. Résultat attendu** — 4 241 sommets supprimés — de 5 760 à 1 519.

**6. Zone CORRIGÉ — explication étape par étape**

1. Compter les sommets du maillage non soudé : quatre par face.
2. Compter ceux du maillage soudé.
3. Soustraire.

**6 bis. Erreur attendue** — Répondre 1 519, le nombre de sommets APRÈS soudure, au lieu du nombre supprimé. Les deux chiffres racontent la même opération, mais seul le second dit ce que le maillage transportait pour rien : près des trois quarts de ses sommets.

**6 ter. Justification du jeu de données** — Quatre sommets par quadrangle non soudé contre 1 519 après soudure : le maillage brut est 3,8 fois plus lourd que nécessaire. C'est l'ordre de grandeur réel d'un maillage produit face par face, et la raison pour laquelle un fichier d'export paraît parfois inexplicablement gros.

**6 quater. Limite de la correction automatique** — La soudure suppose une tolérance. Trop large, elle referme des arêtes qui devaient rester ouvertes — l'exercice ne traite pas ce réglage.

**7. Pièges fréquents**

- Rendre le nombre de sommets restants.
- Compter trois sommets par face, comme pour un triangle.

**8. Variantes et extensions**

- Chiffrer le gain de poids du fichier exporté.
- Refaire le calcul pour un maillage triangulé.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre de sommets supprimés est juste.

#### GP-08 — Ce que coûte une subdivision de plus

| Rubrique | Valeur |
|---|---|
| **Lot** | GP — Géométrie paramétrique appliquée |
| **Thématique** | GP4 · Maillages et SubD |
| **Réf. référentiel** | REF-077, REF-078 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 20 min |
| **Prérequis** | GP-04 |
| **Compétence visée** | Anticiper la croissance d'une surface de subdivision, et choisir le niveau d'affichage en connaissance de cause. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-04 Comptage réfléchi |
| **Statut de production** | À produire |

**1. Compétence visée** — Anticiper la croissance d'une surface de subdivision, et choisir le niveau d'affichage en connaissance de cause.

**1 bis. Contexte métier** — La cage de subdivision est légère et se manipule bien. C'est l'affichage lissé qui fait ramer la machine.

**2. Composants mobilisés** — Multiplication, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La cage compte 26 faces. Chaque passe de subdivision remplace chaque face par quatre. Donnez le nombre de faces après trois passes.

**4. Données de départ fournies** — Le nombre de faces de la cage et le nombre de passes.

**5. Résultat attendu** — 1 664 faces après trois passes.

**6. Zone CORRIGÉ — explication étape par étape**

1. Comprendre que la croissance est géométrique.
2. Élever quatre à la puissance du nombre de passes.
3. Multiplier par le nombre de faces de la cage.

**6 bis. Erreur attendue** — Multiplier une seule fois par quatre (104), ou multiplier par trois (78). La croissance est GÉOMÉTRIQUE : chaque passe quadruple ce que la précédente a produit. C'est pour cela qu'une passe de plus, décidée sans y penser, fait passer un modèle fluide à un modèle inutilisable.

**6 ter. Justification du jeu de données** — 26 faces est la taille d'une cage de mobilier. Les trois réponses possibles — 78, 104 et 1 664 — sont séparées d'un ordre de grandeur, ce qui rend chaque erreur immédiatement lisible.

**7. Pièges fréquents**

- Multiplier par le nombre de passes.
- N'appliquer le facteur qu'une fois.

**8. Variantes et extensions**

- Trouver le nombre de passes qui dépasse cent mille faces.
- Comparer au coût d'affichage d'un maillage équivalent.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre de faces est juste.

---

## Lot QT — Quantitatifs, chiffrage et export

**Niveau** : Intermédiaire · **6 exercices** · **2 h 45 cumulées**

Métré, chiffrage et export de données — les gestes que le métier demande le plus souvent, tous à réponse numérique.

| ID | Titre | Thématique | Niveau | Durée | Validation |
|---|---|---|---|---|---|
| QT-01 | Le métré d'un plancher bois | QT1 · Quantitatifs et chiffrage | Intermédiaire | 25 min | NumericTolerance |
| QT-02 | Du métré au prix | QT1 · Quantitatifs et chiffrage | Intermédiaire | 25 min | NumericTolerance |
| QT-03 | Une nomenclature exportable | QT2 · Export de données | Intermédiaire | 30 min | NumericTolerance |
| QT-04 | Un débit qui devient une commande | QT3 · Export de données | Intermédiaire | 30 min | SingleValue |
| QT-05 | Le fichier que le fournisseur va lire | QT3 · Export de données | Intermédiaire | 25 min | SingleValue |
| QT-06 | Du métré au devis | QT2 · Quantitatifs et chiffrage | Intermédiaire | 30 min | NumericTolerance |

### QT1 · Quantitatifs et chiffrage

*2 exercices — QT-01, QT-02*

#### QT-01 — Le métré d'un plancher bois

| Rubrique | Valeur |
|---|---|
| **Lot** | QT — Quantitatifs, chiffrage et export |
| **Thématique** | QT1 · Quantitatifs et chiffrage |
| **Réf. référentiel** | REF-082, REF-084 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-47 |
| **Compétence visée** | Établir un métré à partir de sections et de longueurs, en distinguant les grandeurs qui s'additionnent de celles qui ne s'additionnent pas. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0,0001 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-01 Score visible |
| **Statut de production** | À produire |

**1. Compétence visée** — Établir un métré à partir de sections et de longueurs, en distinguant les grandeurs qui s'additionnent de celles qui ne s'additionnent pas.

**1 bis. Contexte métier** — Un plancher bois se commande au volume de bois, mais se pose au linéaire : le métré doit rendre les deux.

**2. Composants mobilisés** — Multiplication, Mass Addition, Division, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les 20 solives du plancher vous sont fournies avec leur section et leur longueur. Donnez le volume total de bois, en mètres cubes.

**4. Données de départ fournies** — Les 20 sections, en millimètres, et les 20 longueurs correspondantes, en millimètres.

**5. Résultat attendu** — Le volume total de bois, en mètres cubes, à 0,0001 près.

**6. Zone CORRIGÉ — explication étape par étape**

1. Calculer l'aire de chaque section, en millimètres carrés.
2. Multiplier chaque aire par la longueur de SA solive, terme à terme.
3. Sommer les vingt volumes.
4. Convertir en mètres cubes : diviser par un milliard.
5. Contrôler l'ordre de grandeur : un plancher de cette taille représente quelques dixièmes de mètre cube.

**6 bis. Erreur attendue** — Multiplier la section moyenne par la longueur totale. Les sections varient, et la moyenne ne rend pas le produit : l'écart est faible, l'ordre de grandeur reste juste, et le chiffrage est faux de quelques pour cent — le genre d'erreur qu'on ne voit jamais.

**6 ter. Justification du jeu de données** — Cinq sections courantes de charpente, réparties de façon que la corrélation entre section et longueur soit positive : la moyenne sous-estime alors le volume, toujours dans le même sens.

**7. Pièges fréquents**

- Appariement des deux listes : sections et longueurs doivent rester au même rang.
- Conversion : un mètre cube vaut un milliard de millimètres cubes, pas un million.

**8. Variantes et extensions**

- Ajouter 10 % de chutes et refaire le chiffrage.
- Sortir aussi le linéaire total et comparer les deux unités.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si le volume est juste à 0,0001 m³ près.

#### QT-02 — Du métré au prix

| Rubrique | Valeur |
|---|---|
| **Lot** | QT — Quantitatifs, chiffrage et export |
| **Thématique** | QT1 · Quantitatifs et chiffrage |
| **Réf. référentiel** | REF-083 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | QT-01 |
| **Compétence visée** | Croiser un métré avec un bordereau de prix pour obtenir un montant, sans apparier les mauvaises lignes. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Statut de production** | À produire |

**1. Compétence visée** — Croiser un métré avec un bordereau de prix pour obtenir un montant, sans apparier les mauvaises lignes.

**1 bis. Contexte métier** — Le bordereau du fournisseur donne un prix au mètre linéaire par section ; le métré donne des longueurs par solive.

**2. Composants mobilisés** — Member Index, List Item, Multiplication, Mass Addition, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le bordereau fournit un prix au mètre linéaire pour chacune des cinq sections. Donnez le montant total du plancher, en euros.

**4. Données de départ fournies** — Les 20 solives avec leur section et leur longueur, et le bordereau des cinq prix unitaires par section.

**5. Résultat attendu** — Le montant total, en euros, à 0,01 près.

**6. Zone CORRIGÉ — explication étape par étape**

1. Convertir les longueurs en mètres.
2. Pour chaque solive, retrouver le RANG de sa section dans le bordereau — c'est cet appariement-là qui compte.
3. Extraire le prix correspondant à ce rang.
4. Multiplier prix par longueur, solive par solive.
5. Sommer, et contrôler par un ordre de grandeur : longueur totale multipliée par un prix moyen.

**6 bis. Erreur attendue** — Apparier le bordereau aux solives par leur rang plutôt que par leur section. Il y a vingt solives et cinq prix : un appariement par rang donne silencieusement un résultat, calculé sur le mauvais prix répété — c'est le comportement par défaut vu en A-24, appliqué ici à de l'argent.

**6 ter. Justification du jeu de données** — Vingt solives pour cinq sections : le déséquilibre est volontaire, c'est lui qui rend l'erreur d'appariement possible et détectable.

**7. Pièges fréquents**

- Laisser les deux listes s'apparier par défaut.
- Oublier la conversion en mètres : le prix est au mètre linéaire, les longueurs sont en millimètres.

**8. Variantes et extensions**

- Appliquer une remise de 8 % au-delà de 100 mètres linéaires.
- Sortir le montant par section plutôt que le total.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si le montant est juste à 0,01 € près.

### QT2 · Export de données

*1 exercices — QT-03*

#### QT-03 — Une nomenclature exportable

| Rubrique | Valeur |
|---|---|
| **Lot** | QT — Quantitatifs, chiffrage et export |
| **Thématique** | QT2 · Export de données |
| **Réf. référentiel** | REF-085, REF-086, REF-087 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | A-27 |
| **Compétence visée** | Mettre en forme des données de projet en un tableau exportable, colonne par colonne, et le sortir en fichier. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0,01 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-16 Enquête documentaire |
| **Statut de production** | À produire |

**1. Compétence visée** — Mettre en forme des données de projet en un tableau exportable, colonne par colonne, et le sortir en fichier.

**1 bis. Contexte métier** — Le bureau d'études attend la nomenclature des menuiseries au format tableur, pour la reprendre dans son chiffrage.

**2. Composants mobilisés** — Concatenate, Text Join, Write File, Multiplication, Mass Addition

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les 18 menuiseries vous sont fournies avec leur repère, leur largeur et leur hauteur. Produisez le tableau à quatre colonnes — repère, largeur, hauteur, surface — et exportez-le en CSV. Donnez la surface totale, en mètres carrés.

**4. Données de départ fournies** — Les 18 repères, les 18 largeurs et les 18 hauteurs, en millimètres.

**5. Résultat attendu** — La surface totale des menuiseries, en mètres carrés, à 0,01 près.

**6. Zone CORRIGÉ — explication étape par étape**

1. Calculer la surface de chaque menuiserie, en mètres carrés.
2. Choisir le séparateur : le point-virgule s'impose en contexte francophone, la virgule servant déjà de séparateur décimal.
3. Assembler chaque ligne en joignant les quatre valeurs par ce séparateur.
4. Ajouter la ligne d'en-tête, puis écrire le fichier.
5. Ouvrir le CSV dans un tableur pour vérifier que les colonnes se séparent bien.

**6 bis. Erreur attendue** — Construire le tableau ligne par ligne en concaténant tout dans une seule chaîne. Le fichier s'ouvre, et le tableur voit une seule colonne : c'est le séparateur qui fait les colonnes, et il faut décider lequel avant d'écrire quoi que ce soit.

**6 ter. Justification du jeu de données** — Dix-huit menuiseries de dimensions courantes, avec des répétitions : le tableau doit rester lisible et le total vérifiable à la main sur quelques lignes.

**6 quater. Limite de la correction automatique** — L'écriture du fichier elle-même n'est pas auto-corrigeable : c'est la surface totale qui est validée. Le formateur ouvre le CSV pour juger la mise en forme.

**7. Pièges fréquents**

- Virgule décimale et virgule séparatrice dans le même fichier : chaque nombre décimal casse une ligne en deux colonnes.
- Oublier l'en-tête : le tableur prend la première menuiserie pour un titre.

**8. Variantes et extensions**

- Ajouter une colonne de type d'ouvrant et trier par type.
- Produire aussi un récapitulatif par dimension.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si la surface totale est juste et si le CSV s'ouvre en quatre colonnes distinctes.

### QT3 · Export de données

*2 exercices — QT-04, QT-05*

#### QT-04 — Un débit qui devient une commande

| Rubrique | Valeur |
|---|---|
| **Lot** | QT — Quantitatifs, chiffrage et export |
| **Thématique** | QT3 · Export de données |
| **Réf. référentiel** | REF-085 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | QT-01 |
| **Compétence visée** | Regrouper un relevé ligne à ligne en une table par référence, de sorte que chaque référence n'apparaisse qu'une fois avec sa quantité cumulée. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-11 Commande à passer |
| **Statut de production** | À produire |

**1. Compétence visée** — Regrouper un relevé ligne à ligne en une table par référence, de sorte que chaque référence n'apparaisse qu'une fois avec sa quantité cumulée.

**1 bis. Contexte métier** — Le débit sort de l'atelier ligne par ligne, dans l'ordre du montage. Le fournisseur, lui, veut une commande : une ligne par référence, et la quantité totale.

**2. Composants mobilisés** — Texte, Nombre, Create Set, Member Index, Mass Addition, Sort List, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le débit vous est fourni tel qu'il sort de l'atelier : vingt-quatre lignes, dans le désordre, où la même référence revient plusieurs fois. Donnez la quantité totale de la référence la plus commandée.

**4. Données de départ fournies** — Les vingt-quatre lignes du débit : une référence de panneau et une quantité par ligne.

**5. Résultat attendu** — 17 — la quantité cumulée de la référence la plus commandée.

**6. Zone CORRIGÉ — explication étape par étape**

1. Établir la liste des références distinctes.
2. Rattacher chaque ligne du débit à sa référence.
3. Cumuler les quantités par référence.
4. Prendre le plus grand cumul.

**6 bis. Erreur attendue** — Prendre la plus grande quantité d'une seule ligne (8) au lieu du cumul par référence. La table n'est alors pas regroupée : elle est seulement triée, et le fournisseur recevra vingt-quatre lignes dont huit références en double.

**6 ter. Justification du jeu de données** — Vingt-quatre lignes pour huit références, réparties de façon que la référence la plus FRÉQUENTE (quatre lignes) ne soit pas celle qui porte la plus grosse ligne unitaire : compter les occurrences donne une autre réponse que cumuler les quantités. Les deux suivantes sont à 15, assez proches pour qu'un cumul approximatif se trompe de référence.

**7. Pièges fréquents**

- Confondre le nombre de lignes et la quantité.
- Regrouper sur un libellé approchant : les références se ressemblent, deux d'entre elles ne diffèrent que par leur épaisseur.

**8. Variantes et extensions**

- Rendre la table complète, une ligne par référence, triée par quantité décroissante.
- Ajouter une colonne de prix unitaire et sortir le montant.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si la quantité cumulée est juste.

#### QT-05 — Le fichier que le fournisseur va lire

| Rubrique | Valeur |
|---|---|
| **Lot** | QT — Quantitatifs, chiffrage et export |
| **Thématique** | QT3 · Export de données |
| **Réf. référentiel** | REF-086, REF-087 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | QT-04 |
| **Compétence visée** | Produire un fichier d'échange dont la structure est celle qu'attend le destinataire, en-tête comprise, et savoir combien de lignes il doit contenir avant de l'ouvrir. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-11 Commande à passer |
| **Statut de production** | À produire |

**1. Compétence visée** — Produire un fichier d'échange dont la structure est celle qu'attend le destinataire, en-tête comprise, et savoir combien de lignes il doit contenir avant de l'ouvrir.

**1 bis. Contexte métier** — La commande part en CSV vers le fournisseur, qui l'importe automatiquement. Un fichier mal structuré n'est pas rejeté : il est importé de travers.

**2. Composants mobilisés** — Create Set, List Length, Addition, Concatenate, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Vous exportez la commande regroupée de l'exercice précédent au format CSV, avec une ligne d'en-tête nommant les colonnes. Donnez le nombre de lignes que le fichier doit contenir.

**4. Données de départ fournies** — Le débit de vingt-quatre lignes, et la commande regroupée qui en découle.

**5. Résultat attendu** — 9 — huit références, plus la ligne d'en-tête.

**6. Zone CORRIGÉ — explication étape par étape**

1. Reprendre la commande regroupée par référence.
2. Compter les références distinctes.
3. Ajouter la ligne d'en-tête.
4. Écrire le fichier, et le rouvrir pour vérifier le compte.

**6 bis. Erreur attendue** — Exporter les vingt-quatre lignes du débit (25 avec l'en-tête) ou oublier l'en-tête (8). Le premier fait commander huit références en double ; le second fait lire la première référence comme un nom de colonne, et elle disparaît de la commande.

**6 ter. Justification du jeu de données** — Le compte attendu — 9 — ne ressemble ni au nombre de lignes du débit (24) ni au nombre de références (8) : les trois erreurs possibles donnent trois valeurs distinctes, donc lisibles.

**6 quater. Limite de la correction automatique** — Le compte des lignes ne dit rien du séparateur ni de l'encodage, qui font échouer autant d'imports. La fiche les signale ; l'exercice ne les valide pas.

**7. Pièges fréquents**

- Oublier l'en-tête.
- Exporter le débit au lieu de la commande.
- Employer la virgule comme séparateur alors que les quantités peuvent être décimales.

**8. Variantes et extensions**

- Ajouter une colonne d'unité et vérifier que le compte des lignes ne change pas.
- Exporter la même commande en XLSX et comparer ce que chaque format garantit.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre de lignes est juste.

### QT2 · Quantitatifs et chiffrage

*1 exercices — QT-06*

#### QT-06 — Du métré au devis

| Rubrique | Valeur |
|---|---|
| **Lot** | QT — Quantitatifs, chiffrage et export |
| **Thématique** | QT2 · Quantitatifs et chiffrage |
| **Réf. référentiel** | REF-083 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | QT-02 |
| **Compétence visée** | Enchaîner les coefficients d'un devis dans le bon ordre, en sachant sur quelle assiette chacun s'applique. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-11 Commande à passer |
| **Statut de production** | À produire |

**1. Compétence visée** — Enchaîner les coefficients d'un devis dans le bon ordre, en sachant sur quelle assiette chacun s'applique.

**1 bis. Contexte métier** — Le métré est fait. Reste à en faire un devis : main d'œuvre, marge, puis taxe — et pas dans un autre ordre.

**2. Composants mobilisés** — Multiplication, Addition, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les matériaux reviennent à 4 820,50 €. La pose demande 22,5 heures à 48 € l'heure. La marge est de 12 %, la taxe de 10 %. Donnez le montant toutes taxes comprises, en euros.

**4. Données de départ fournies** — Le coût des matériaux, les heures et leur taux, le taux de marge et celui de la taxe.

**5. Résultat attendu** — 7 269,42 € toutes taxes comprises.

**6. Zone CORRIGÉ — explication étape par étape**

1. Chiffrer la main d'œuvre.
2. Ajouter les matériaux : c'est le déboursé sec.
3. Appliquer la marge.
4. Appliquer la taxe.

**6 bis. Erreur attendue** — Oublier la marge et facturer 6 490,55 €. L'écart, 778,87 €, est exactement ce que l'entreprise gagnait sur le chantier : le devis reste plausible, il est simplement à prix coûtant.

**6 ter. Justification du jeu de données** — Les taux — 12 % de marge, 10 % de taxe — sont ceux du bâtiment en rénovation. Marge et taxe étant toutes deux multiplicatives, leur ORDRE ne change pas le total : c'est l'oubli de l'une qui se voit, pas leur permutation, et l'exercice porte donc sur ce qui compte vraiment.

**6 quater. Limite de la correction automatique** — Le calcul suppose une marge sur le déboursé sec. Beaucoup d'entreprises appliquent des coefficients distincts aux matériaux et à la main d'œuvre — la structure du calcul reste la même.

**7. Pièges fréquents**

- Oublier la marge.
- Appliquer la marge aux seuls matériaux.
- Confondre marge et taux de marque.

**8. Variantes et extensions**

- Séparer les coefficients matériaux et main d'œuvre.
- Retrouver le prix de vente qui atteint une marge visée.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si le montant TTC est juste au centime.

---

## Lot FA — Aide à la fabrication

**Niveau** : Perfectionnement · **4 exercices** · **2 h 10 cumulées**

Aide à la fabrication : estimation d'imbrication et mise à plat.

| ID | Titre | Thématique | Niveau | Durée | Validation |
|---|---|---|---|---|---|
| FA-01 | Combien de panneaux pour ce débit | FA1 · Imbrication | Perfectionnement | 35 min | SingleValue |
| FA-02 | Le développé d'une virole | FA2 · Déroulé et mise à plat | Perfectionnement | 30 min | NumericTolerance |
| FA-03 | Le développé d'un profil plié | FA2 · Déroulé et mise à plat | Perfectionnement | 35 min | NumericTolerance |
| FA-04 | Combien de pièces par fournée | FA1 · Imbrication | Perfectionnement | 30 min | SingleValue |

### FA1 · Imbrication

*2 exercices — FA-01, FA-04*

#### FA-01 — Combien de panneaux pour ce débit

| Rubrique | Valeur |
|---|---|
| **Lot** | FA — Aide à la fabrication |
| **Thématique** | FA1 · Imbrication |
| **Réf. référentiel** | REF-113, REF-114 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 35 min |
| **Prérequis** | QT-01 |
| **Compétence visée** | Estimer le nombre de panneaux nécessaires à un débit et chiffrer la chute, avant toute imbrication réelle. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Statut de production** | À produire |

**1. Compétence visée** — Estimer le nombre de panneaux nécessaires à un débit et chiffrer la chute, avant toute imbrication réelle.

**1 bis. Contexte métier** — Le débit part sur une découpeuse à commande numérique ; le panneau brut mesure 2 500 × 1 250 mm et se commande à l'unité.

**2. Composants mobilisés** — Multiplication, Mass Addition, Division, Round, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les 20 pièces à débiter vous sont fournies avec leurs dimensions. Donnez le nombre minimal théorique de panneaux, c'est-à-dire celui qu'imposerait déjà la seule surface, avant toute contrainte de placement.

**4. Données de départ fournies** — Les 20 longueurs et les 20 hauteurs, en millimètres, et les dimensions du panneau brut.

**5. Résultat attendu** — 4 — le nombre minimal théorique de panneaux. La surface exige 3,10 panneaux, et l'on n'en commande pas un dixième.

**6. Zone CORRIGÉ — explication étape par étape**

1. Calculer la surface de chaque pièce.
2. Sommer les vingt surfaces.
3. Diviser par la surface d'un panneau brut.
4. Arrondir au supérieur : c'est un approvisionnement.
5. Garder à l'esprit que le nombre réel sera supérieur — la chute de placement s'ajoute à la chute de surface.

**6 bis. Erreur attendue** — Arrondir le rapport de surfaces au plus proche. Un panneau se commande entier : il en faut au moins autant que la surface l'exige, donc un arrondi au supérieur. C'est la même règle qu'en A-06, appliquée à un approvisionnement.

**6 ter. Justification du jeu de données** — Vingt pièces de dimensions réalistes pour du mobilier, dont la surface totale vaut 3,10 panneaux : arrondir au plus proche donnerait 3, et il manquerait de quoi débiter un dixième du lot. Arrondir au supérieur donne 4.

**6 quater. Limite de la correction automatique** — Le nombre RÉEL de panneaux dépend de l'imbrication, qui relève d'un plugin dédié et ne se calcule pas ici. C'est le minorant théorique qui est validé — et c'est aussi ce que sert à comprendre l'exercice : aucune imbrication ne peut faire mieux.

**7. Pièges fréquents**

- Arrondir au plus proche.
- Oublier que ce minorant est inatteignable en pratique et le présenter comme la commande à passer.

**8. Variantes et extensions**

- Ajouter un trait de scie de 4 mm autour de chaque pièce et refaire l'estimation.
- Comparer au résultat d'une imbrication réelle et chiffrer l'écart : c'est le rendement de l'imbrication.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre est juste et arrondi au supérieur.

#### FA-04 — Combien de pièces par fournée

| Rubrique | Valeur |
|---|---|
| **Lot** | FA — Aide à la fabrication |
| **Thématique** | FA1 · Imbrication |
| **Réf. référentiel** | REF-114 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | FA-01 |
| **Compétence visée** | Estimer le remplissage d'un volume de fabrication en raisonnant par encombrement, et non par volume de matière. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 10 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Statut de production** | À produire |

**1. Compétence visée** — Estimer le remplissage d'un volume de fabrication en raisonnant par encombrement, et non par volume de matière.

**1 bis. Contexte métier** — La machine de fabrication additive facture à la fournée, pas à la pièce : le prix unitaire dépend entièrement du nombre de pièces qu'on fait tenir dans le volume de construction.

**2. Composants mobilisés** — Subtraction, Addition, Division, Round, Multiplication, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le volume de construction mesure 250 × 210 × 210 mm. La pièce tient dans un encombrement de 62 × 38 × 95 mm et ne peut pas être réorientée. Il faut 4 mm entre deux pièces et 4 mm entre une pièce et chaque paroi. Donnez le nombre de pièces par fournée.

**4. Données de départ fournies** — Les dimensions du volume de construction, l'encombrement de la pièce et l'écart minimal à respecter.

**5. Résultat attendu** — 24 — soit 3 pièces en longueur, 4 en largeur et 2 en hauteur.

**6. Zone CORRIGÉ — explication étape par étape**

1. Retrancher les deux écarts de paroi de chaque dimension du plateau.
2. Sur chaque axe, chercher combien de pièces séparées d'un écart tiennent dans la longueur utile.
3. Arrondir chaque compte à l'entier INFÉRIEUR : une pièce qui dépasse ne se produit pas.
4. Multiplier les trois comptes.

**6 bis. Erreur attendue** — Diviser le volume du plateau par le volume de la pièce : 11 025 000 ÷ 223 820 donne 49 pièces, soit le double. Le rapport des volumes ignore que les pièces ne se déforment pas pour combler les creux — c'est la même erreur que le rapport des surfaces en FA-01, et elle se paie ici au prix de la fournée.

**6 ter. Justification du jeu de données** — Les trois divisions tombent chacune sur une valeur franchement non entière — 3,72, 4,90 et 2,08 — de sorte qu'un arrondi au plus proche donnerait 4, 5 et 2, soit 40 pièces qui ne rentrent pas. L'écart entre le rapport des volumes (49) et le compte réel (24) est du simple au double : impossible de confondre les deux méthodes.

**6 quater. Limite de la correction automatique** — Le compte suppose une orientation fixe et une grille régulière. Un imbriquement réel, qui autorise la rotation et l'entrelacement, fait mieux — mais jamais autant que le rapport des volumes.

**7. Pièges fréquents**

- Diviser les volumes.
- Arrondir au plus proche au lieu de l'inférieur.
- Compter un écart de trop ou de moins : entre n pièces il y a n − 1 intervalles, plus les deux écarts de paroi.

**8. Variantes et extensions**

- Autoriser la rotation à 90° autour de l'axe vertical et recompter.
- Chiffrer le prix unitaire pour une fournée facturée 380 € et le comparer à celui qu'aurait donné le rapport des volumes.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre de pièces est juste.

### FA2 · Déroulé et mise à plat

*2 exercices — FA-02, FA-03*

#### FA-02 — Le développé d'une virole

| Rubrique | Valeur |
|---|---|
| **Lot** | FA — Aide à la fabrication |
| **Thématique** | FA2 · Déroulé et mise à plat |
| **Réf. référentiel** | REF-115, REF-116 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | A-42 |
| **Compétence visée** | Établir le développé à plat d'une surface réglée et le contrôler par un calcul indépendant. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0,0001 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Statut de production** | À produire |

**1. Compétence visée** — Établir le développé à plat d'une surface réglée et le contrôler par un calcul indépendant.

**1 bis. Contexte métier** — Une virole conique de ventilation se découpe à plat dans la tôle avant d'être roulée.

**2. Composants mobilisés** — Cone, Unroll Brep, Area, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La virole relie un diamètre de 360 mm à un diamètre de 190 mm sur une hauteur de 340 mm. Produisez son développé à plat et donnez la surface développée, en mètres carrés.

**4. Données de départ fournies** — Les deux rayons et la hauteur, en valeurs réglables.

**5. Résultat attendu** — La surface développée, en mètres carrés, à 0,0001 près.

**6. Zone CORRIGÉ — explication étape par étape**

1. Construire la virole comme surface réglée entre les deux cercles.
2. La dérouler à plat.
3. Mesurer l'aire du développé.
4. Contrôler par le calcul : π multiplié par la somme des rayons, multiplié par la génératrice — et non par la hauteur.
5. Comparer les deux valeurs : elles doivent coïncider.

**6 bis. Erreur attendue** — Prendre la hauteur pour l'apothème. La génératrice d'un cône tronqué vaut la racine de la hauteur au carré plus l'écart des rayons au carré : ici 340 contre 348 mm. L'écart est de 2 %, assez petit pour passer inaperçu et assez grand pour que la virole ne se referme pas.

**6 ter. Justification du jeu de données** — L'écart des rayons, 85 mm pour 340 de hauteur, place la génératrice juste assez loin de la hauteur pour que la confusion soit détectable au dixième de millimètre carré, sans être grossière.

**7. Pièges fréquents**

- Confondre hauteur et génératrice.
- Dérouler une surface non développable : un cône l'est, une double courbure ne l'est pas, et le résultat serait une approximation silencieuse.

**8. Variantes et extensions**

- Ajouter un recouvrement de 15 mm pour la soudure.
- Passer à une virole excentrée et constater qu'elle ne se déroule plus exactement.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si la surface développée est juste et si le contrôle par le calcul est fourni.

#### FA-03 — Le développé d'un profil plié

| Rubrique | Valeur |
|---|---|
| **Lot** | FA — Aide à la fabrication |
| **Thématique** | FA2 · Déroulé et mise à plat |
| **Réf. référentiel** | REF-116 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 35 min |
| **Prérequis** | FA-02 |
| **Compétence visée** | Calculer la longueur développée d'une tôle pliée en tenant compte de l'allongement de la matière au droit des plis. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 0.1 |
| **Solution de référence** | 9 composants |
| **Gamification associée** | G-19 Pièce d'essai |
| **Statut de production** | À produire |

**1. Compétence visée** — Calculer la longueur développée d'une tôle pliée en tenant compte de l'allongement de la matière au droit des plis.

**1 bis. Contexte métier** — Le profil en U part au débit avant pliage : la bande découpée doit avoir exactement la longueur qui, une fois pliée, donnera les cotes du plan.

**2. Composants mobilisés** — Subtraction, Multiplication, Addition, Pi, Division, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le profil en U mesure 120 mm d'aile, 300 mm d'âme, cotes extérieures, dans une tôle de 3 mm. Les deux plis à 90° se font sur un rayon intérieur de 5 mm, avec un facteur K de 0,42. Donnez la longueur de la bande à débiter, en millimètres.

**4. Données de départ fournies** — Les cotes extérieures du profil, l'épaisseur de la tôle, le rayon intérieur de pliage et le facteur K.

**5. Résultat attendu** — 527,67 mm — la longueur développée, à 0,1 mm près.

**6. Zone CORRIGÉ — explication étape par étape**

1. Retrancher rayon et épaisseur des cotes extérieures pour obtenir les parties réellement plates.
2. Calculer l'allongement d'un pli à 90° : un quart de cercle sur le rayon de la fibre neutre.
3. La fibre neutre est à r + K·e du centre de courbure.
4. Sommer les parties plates et les deux allongements.

**6 bis. Erreur attendue** — Additionner les cotes extérieures : 120 + 300 + 120 = 540 mm. La matière s'allonge à l'extérieur du pli et se comprime à l'intérieur ; seule la fibre neutre garde sa longueur, et elle ne passe pas au milieu de l'épaisseur — c'est ce que dit le facteur K. L'écart fait 12,3 mm : invisible sur le plan, fatal à l'atelier, et il se répète sur chaque pièce de la série.

**6 ter. Justification du jeu de données** — Un facteur K de 0,42 est la valeur courante pour un acier doux plié sur un rayon voisin de l'épaisseur. Les cotes sont extérieures, comme sur un plan de tôlerie — c'est précisément ce qui oblige à retrancher rayon et épaisseur avant de calculer les parties plates.

**6 quater. Limite de la correction automatique** — Le facteur K dépend de la nuance, du rayon et de l'outil : celui de l'exercice est donné. En atelier, il se relève sur une pièce d'essai, et c'est le vrai geste métier.

**7. Pièges fréquents**

- Sommer les cotes extérieures.
- Placer la fibre neutre au milieu de l'épaisseur, ce qui revient à prendre K = 0,5.
- Oublier que l'âme perd rayon et épaisseur DEUX fois, une par pli.

**8. Variantes et extensions**

- Refaire le calcul avec un facteur K de 0,5 et chiffrer l'écart sur une série de 200 pièces.
- Traiter un profil à trois plis, dont un à 135°.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si le développé est juste à 0,1 mm près.

---

## Lot PL — Écosystème de plugins

**Niveau** : Débutant à intermédiaire · **12 exercices** · **2 h 43 cumulées**

L'écosystème de plugins. Presque tout y est connaissance — installer, choisir, juger — et devient donc question charnière. Un seul exercice, sur l'ergonomie réellement mise à l'épreuve.

| ID | Titre | Thématique | Niveau | Durée | Validation |
|---|---|---|---|---|---|
| PL-01 | Ce qui change quand on passe au paramétrique | PL1 · Principes | Débutant | 8 min | — |
| PL-02 | Où trouver un plugin, et lequel | PL2 · Installation de plugins | Intermédiaire | 8 min | — |
| PL-03 | Les plugins qui ne servent qu'à travailler mieux | PL3 · Plugins d'ergonomie | Intermédiaire | 20 min | Visuel |
| PL-04 | Choisir un plugin fonctionnel | PL4 · Plugins fonctionnels | Intermédiaire | 8 min | — |
| PL-05 | Ce qu'un plugin traîne derrière lui | PL1 · Écosystème de plugins | Intermédiaire | 20 min | SingleValue |
| PL-06 | Qui pourra ouvrir votre définition | PL1 · Écosystème de plugins | Intermédiaire | 20 min | SingleValue |
| PL-07 | Ce qu'un plugin vous épargne d'écrire | PL1 · Écosystème de plugins | Intermédiaire | 20 min | SingleValue |
| PL-08 | Les composants qui ne disent pas leur nom | PL1 · Écosystème de plugins | Intermédiaire | 20 min | SingleValue |
| PL-09 | Ce qui s'installera vraiment sur ce poste | PL1 · Écosystème de plugins | Intermédiaire | 15 min | SingleValue |
| PL-10 | Où chercher un plugin | PL1 · Écosystème de plugins | Intermédiaire | 8 min | — |
| PL-11 | Deux familles de plugins | PL1 · Écosystème de plugins | Intermédiaire | 8 min | — |
| PL-12 | Le plugin qui n'est plus maintenu | PL1 · Écosystème de plugins | Intermédiaire | 8 min | — |

### PL1 · Principes

*1 exercices — PL-01*

#### PL-01 — Ce qui change quand on passe au paramétrique

| Rubrique | Valeur |
|---|---|
| **Lot** | PL — Écosystème de plugins |
| **Thématique** | PL1 · Principes |
| **Réf. référentiel** | REF-025 |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | — |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Un client demande de reprendre une façade déjà modélisée en changeant la trame.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Qu'est-ce qu'une définition paramétrique apporte qu'un modèle dessiné n'apporte pas ?
a) Elle va plus vite à produire la première fois.
b) Elle rend la modification bon marché : on change une valeur, tout suit. ← réponse
c) Elle donne un modèle plus précis.
d) Elle évite d'avoir à connaître Rhino.

Valeur diagnostique : (a) est faux et c'est important de le dire — une définition coûte presque toujours plus cher que le dessin équivalent, la première fois. Croire le contraire mène à en faire pour des cas uniques, où elle ne se rentabilise jamais. Le paramétrique s'amortit sur les variantes, pas sur la première livraison.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

### PL2 · Installation de plugins

*1 exercices — PL-02*

#### PL-02 — Où trouver un plugin, et lequel

| Rubrique | Valeur |
|---|---|
| **Lot** | PL — Écosystème de plugins |
| **Thématique** | PL2 · Installation de plugins |
| **Réf. référentiel** | REF-029, REF-030 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 8 min |
| **Prérequis** | — |
| **Case Bloom (révisée)** | Comprendre × procédurale |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Une définition reçue affiche des composants manquants.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Vous ouvrez une définition et plusieurs composants apparaissent en rouge, marqués manquants. Par où commencez-vous ?
a) Reconstruire les parties manquantes à la main.
b) Lire le nom du composant manquant, qui porte celui du plugin, et l'installer par le gestionnaire de paquets. ← réponse
c) Demander à l'auteur de refaire la définition sans plugin.
d) Réinstaller Rhino.

Valeur diagnostique : (a) est le réflexe coûteux — on reconstruit parfois des heures ce qu'une installation d'une minute aurait résolu. Le point à faire passer : Grasshopper dit toujours ce qui manque, et le gestionnaire de paquets intégré est à préférer au téléchargement manuel, parce qu'il gère les versions et les mises à jour.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

### PL3 · Plugins d'ergonomie

*1 exercices — PL-03*

#### PL-03 — Les plugins qui ne servent qu'à travailler mieux

| Rubrique | Valeur |
|---|---|
| **Lot** | PL — Écosystème de plugins |
| **Thématique** | PL3 · Plugins d'ergonomie |
| **Réf. référentiel** | REF-031, REF-032, REF-033, REF-034, REF-035, REF-036, REF-037 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | PL-02 |
| **Compétence visée** | Installer et régler les plugins d'ergonomie, et juger lesquels valent la place qu'ils prennent. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-18 Duel de versions |
| **Statut de production** | À produire |

**1. Compétence visée** — Installer et régler les plugins d'ergonomie, et juger lesquels valent la place qu'ils prennent.

**1 bis. Contexte métier** — Une définition d'équipe se relit à plusieurs : ce qui la rend lisible fait gagner plus de temps que ce qui la rend puissante.

**2. Composants mobilisés** — Gestionnaire de paquets Rhino, plugins d'ergonomie

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Installez les plugins d'ergonomie proposés, réglez-les, puis reprenez une définition existante et dites, pour chacun, ce qu'il vous a réellement fait gagner. Concluez par les deux que vous garderiez et les raisons.

**4. Données de départ fournies** — Une définition d'exercice déjà produite, à relire, et l'accès au gestionnaire de paquets.

**5. Résultat attendu** — Une définition relue, les plugins réglés, et un jugement motivé sur chacun.

**6. Zone CORRIGÉ — explication étape par étape**

1. Installer les plugins un par un, en relançant Rhino entre chacun : installer en bloc empêche de savoir lequel fait quoi.
2. Reprendre la même définition après chaque installation.
3. Noter ce que le plugin change concrètement : temps gagné, erreur évitée, lisibilité.
4. Désactiver ceux qui n'ont rien apporté.
5. Vérifier que la définition reste lisible pour un collègue qui n'a aucun de ces plugins.

**6 bis. Erreur attendue** — Tout installer et tout garder. Chaque plugin d'ergonomie ajoute un affichage, un raccourci ou une couleur ; empilés sans choix, ils encombrent l'écran plus qu'ils n'aident, et la définition devient illisible pour qui ne les a pas.

**6 ter. Justification du jeu de données** — —

**6 quater. Limite de la correction automatique** — Le livrable est un jugement argumenté, pas un nombre : la validation est visuelle. Ramener cet exercice à une valeur chiffrée n'aurait aucun sens.

**7. Pièges fréquents**

- Confondre confort personnel et lisibilité partagée : une couleur qui vous parle n'existe pas chez le voisin.
- Dépendre d'un plugin d'ergonomie pour comprendre sa propre définition : elle devient intransmissible.

**8. Variantes et extensions**

- Faire relire votre définition par quelqu'un qui n'a aucun plugin installé.
- Chronométrer la même reprise avec et sans.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode Visuel.

**10. Barème** — Grille : plugins installés et réglés (2), jugement motivé sur chacun (2), définition lisible sans eux (1).

### PL4 · Plugins fonctionnels

*1 exercices — PL-04*

#### PL-04 — Choisir un plugin fonctionnel

| Rubrique | Valeur |
|---|---|
| **Lot** | PL — Écosystème de plugins |
| **Thématique** | PL4 · Plugins fonctionnels |
| **Réf. référentiel** | REF-038, REF-039 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 8 min |
| **Prérequis** | PL-02 |
| **Case Bloom (révisée)** | Évaluer × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Un besoin nouveau — imbriquer des pièces — a sûrement déjà un plugin.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Avant d'adopter un plugin fonctionnel dans une définition livrée à un client, qu'est-ce qui compte le plus ?
a) Le nombre de composants qu'il apporte.
b) Sa licence, son entretien et ce qui se passe pour le client s'il disparaît. ← réponse
c) Sa popularité sur les forums.
d) Qu'il soit gratuit.

Valeur diagnostique : (d) est le critère le plus souvent appliqué et le plus dangereux — gratuit ne dit rien du droit d'usage commercial, ni de la survie du projet. Une définition livrée qui dépend d'un plugin abandonné devient inexploitable à la première mise à jour de Rhino, et c'est le client qui le découvre.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

### PL1 · Écosystème de plugins

*8 exercices — PL-05, PL-06, PL-07, PL-08, PL-09, PL-10, PL-11, PL-12*

#### PL-05 — Ce qu'un plugin traîne derrière lui

| Rubrique | Valeur |
|---|---|
| **Lot** | PL — Écosystème de plugins |
| **Thématique** | PL1 · Écosystème de plugins |
| **Réf. référentiel** | REF-029, REF-030 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | PL-02 |
| **Compétence visée** | Établir la liste complète des paquets qu'une installation suppose, en suivant les dépendances jusqu'au bout. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-06 Valise de chantier |
| **Statut de production** | À produire |

**1. Compétence visée** — Établir la liste complète des paquets qu'une installation suppose, en suivant les dépendances jusqu'au bout.

**1 bis. Contexte métier** — Le poste du chantier n'a pas Internet. Ce qui n'est pas emporté sur la clé ne sera pas installé.

**2. Composants mobilisés** — Texte, Member Index, Create Set, List Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le tableau des dépendances déclarées vous est fourni. Donnez le nombre total de paquets à emporter pour installer Nid, celui-ci compris.

**4. Données de départ fournies** — Le tableau des dépendances : pour chaque paquet, ceux qu'il exige.

**5. Résultat attendu** — 6 paquets — Nid, plus les cinq dont il dépend directement ou indirectement.

**6. Zone CORRIGÉ — explication étape par étape**

1. Relever les dépendances directes du paquet visé.
2. Relever celles de chacune, et ainsi de suite.
3. Écarter les doublons.
4. Ajouter le paquet lui-même.

**6 bis. Erreur attendue** — S'arrêter aux dépendances DIRECTES et n'en emporter que trois. Trame et Aiguille en exigent d'autres, qui en exigent encore : la chaîne fait trois niveaux. Sur un poste sans réseau, l'installation s'arrête au premier maillon manquant, et le message ne nomme que celui-là.

**6 ter. Justification du jeu de données** — Le graphe fait trois niveaux de profondeur et comporte un paquet exigé par DEUX autres — Noyau — qu'il ne faut compter qu'une fois. Les réponses fausses plausibles sont 3 (les directes) et 7 (Noyau compté deux fois) : toutes deux distinctes de 6. Les noms sont neutres à dessein — ce qui est évalué est le parcours du graphe, pas la mémoire d'un catalogue.

**7. Pièges fréquents**

- S'arrêter au premier niveau.
- Compter deux fois un paquet exigé par deux autres.

**8. Variantes et extensions**

- Faire la même liste pour Cadran, et mesurer ce que les deux installations partagent.
- Repérer les paquets dont plus rien ne dépend.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le compte total est juste.

#### PL-06 — Qui pourra ouvrir votre définition

| Rubrique | Valeur |
|---|---|
| **Lot** | PL — Écosystème de plugins |
| **Thématique** | PL1 · Écosystème de plugins |
| **Réf. référentiel** | REF-038, REF-039 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | PL-05 |
| **Compétence visée** | Mesurer ce qu'une dépendance à des plugins coûte en portabilité, avant de livrer. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-17 Passation |
| **Statut de production** | À produire |

**1. Compétence visée** — Mesurer ce qu'une dépendance à des plugins coûte en portabilité, avant de livrer.

**1 bis. Contexte métier** — La définition part chez sept destinataires. Chez ceux qui n'ont pas les plugins, elle s'ouvrira — avec des composants rouges à la place du calcul.

**2. Composants mobilisés** — Texte, Member Index, Equality, Cull Pattern, List Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Votre définition exige trois plugins. L'inventaire des sept postes destinataires vous est fourni. Donnez le nombre de postes qui pourront l'exécuter.

**4. Données de départ fournies** — Les trois plugins requis, et pour chacun des sept postes la liste de ceux qu'il possède.

**5. Résultat attendu** — 3 postes sur 7 pourront l'exécuter.

**6. Zone CORRIGÉ — explication étape par étape**

1. Pour chaque poste, vérifier la présence des TROIS plugins.
2. Ne retenir que ceux qui les ont tous.
3. Compter.

**6 bis. Erreur attendue** — Compter les postes qui possèdent AU MOINS UN des trois plugins : six sur sept, et la livraison paraît sans risque. Il les faut TOUS LES TROIS — un composant manquant suffit à rompre la chaîne, et la définition ne rend alors rien.

**6 ter. Justification du jeu de données** — Sept postes, dont un qui n'a rien, un qui a tout et plus, et quatre qui ont une partie : la différence entre « au moins un » (6) et « tous » (3) est du simple au double, et c'est exactement l'écart entre l'impression que la livraison passera et la réalité.

**6 quater. Limite de la correction automatique** — Le compte suppose que posséder le plugin suffit. Une version incompatible se compte comme une absence — c'est l'objet de PL-09.

**7. Pièges fréquents**

- Se contenter d'une intersection non vide.
- Oublier qu'un plugin en trop ne compense pas un plugin manquant.

**8. Variantes et extensions**

- Trouver le plugin dont l'abandon rendrait la définition portable au plus grand nombre.
- Chiffrer ce que coûterait de refaire en natif la part dépendante.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le compte des postes capables est juste.

#### PL-07 — Ce qu'un plugin vous épargne d'écrire

| Rubrique | Valeur |
|---|---|
| **Lot** | PL — Écosystème de plugins |
| **Thématique** | PL1 · Écosystème de plugins |
| **Réf. référentiel** | REF-038, REF-039 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | PL-04 |
| **Compétence visée** | Chiffrer ce qu'un plugin fait gagner en construction, pour le mettre en regard de ce qu'il coûte en dépendance. |
| **Case Bloom (révisée)** | Évaluer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Statut de production** | À produire |

**1. Compétence visée** — Chiffrer ce qu'un plugin fait gagner en construction, pour le mettre en regard de ce qu'il coûte en dépendance.

**1 bis. Contexte métier** — La question n'est jamais « ce plugin est-il bon ». Elle est « ce qu'il m'épargne vaut-il ce qu'il m'impose ».

**2. Composants mobilisés** — Nombre, Mass Addition, Subtraction, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Cinq tâches vous sont données, avec le nombre de composants qu'elles demandent en natif et avec le plugin adapté. Donnez le nombre de composants économisés au total.

**4. Données de départ fournies** — Les cinq tâches, et pour chacune le compte natif et le compte avec plugin.

**5. Résultat attendu** — 115 composants économisés — 123 en natif contre 8 avec plugins.

**6. Zone CORRIGÉ — explication étape par étape**

1. Sommer les comptes natifs.
2. Sommer les comptes avec plugins.
3. Soustraire.

**6 bis. Erreur attendue** — Rendre le compte avec plugins (8) ou le compte natif (123) au lieu de l'écart. C'est l'ÉCART qui se met en balance avec le coût de la dépendance mesuré en PL-06 : 115 composants épargnés contre quatre postes sur sept qui ne pourront plus ouvrir le fichier.

**6 ter. Justification du jeu de données** — Les rapports vont de 9 contre 1 à 34 contre 1 selon la tâche : le gain n'est pas uniforme, et l'exercice se prolonge naturellement en « lequel des cinq mérite vraiment sa dépendance ».

**6 quater. Limite de la correction automatique** — Le nombre de composants n'est qu'un indice. Un plugin peut épargner peu de composants et beaucoup de justesse — une imbrication écrite à la main est fausse avant d'être longue.

**7. Pièges fréquents**

- Rendre l'un des deux totaux.
- Conclure du gain seul, sans regarder ce que la dépendance coûte.

**8. Variantes et extensions**

- Classer les cinq tâches par rapport gain sur dépendance.
- Reprendre en comptant les heures plutôt que les composants.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si l'économie totale est juste.

#### PL-08 — Les composants qui ne disent pas leur nom

| Rubrique | Valeur |
|---|---|
| **Lot** | PL — Écosystème de plugins |
| **Thématique** | PL1 · Écosystème de plugins |
| **Réf. référentiel** | REF-031, REF-032, REF-033 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | PL-03 |
| **Compétence visée** | Repérer, dans une définition, ce qu'un relecteur ne pourra pas comprendre sans remonter les câbles. |
| **Case Bloom (révisée)** | Évaluer × conceptuelle |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-17 Passation |
| **Statut de production** | À produire |

**1. Compétence visée** — Repérer, dans une définition, ce qu'un relecteur ne pourra pas comprendre sans remonter les câbles.

**1 bis. Contexte métier** — Les plugins d'ergonomie affichent les noms, alignent, colorent. Ils ne remplacent pas le fait de nommer : ils rendent visible qu'on ne l'a pas fait.

**2. Composants mobilisés** — Texte, Booléen, Cull Pattern, List Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les vingt-quatre surnoms relevés sur la définition vous sont fournis. Donnez le nombre de composants dont le surnom ne dit pas ce qu'ils font.

**4. Données de départ fournies** — Les vingt-quatre surnoms, tels qu'ils apparaissent sur le canevas.

**5. Résultat attendu** — 10 surnoms ne disent rien de ce que le composant fait.

**6. Zone CORRIGÉ — explication étape par étape**

1. Lire chaque surnom en se demandant ce qu'il apprend à qui n'a pas écrit la définition.
2. Écarter le critère de longueur.
3. Compter les muets.

**6 bis. Erreur attendue** — Compter les surnoms COURTS. « Pt » et « Vec » sont courts et muets, mais « Jeu de pose » est court et parlant, tandis qu'un surnom long et générique ne vaudrait pas mieux que « A ». Ce qui se juge est ce que le surnom APPREND, pas sa longueur.

**6 ter. Justification du jeu de données** — Dix surnoms muets sur vingt-quatre, soit plus de quatre sur dix — la proportion ordinaire d'une définition écrite sans intention de la faire relire. Les muets se répartissent en deux familles : six abréviations de composants (Srf, Mult, Div, Rot, Pt, Vec) et quatre lettres seules (A, D, X, N). Deux familles, pour qu'un critère de longueur seul ne suffise pas à les trouver.

**6 quater. Limite de la correction automatique** — L'exercice compte. Il ne renomme pas — et renommer est le vrai travail, qui se juge en MP-01.

**7. Pièges fréquents**

- Juger sur la longueur.
- Considérer qu'un nom de composant par défaut est acceptable parce qu'il est exact.

**8. Variantes et extensions**

- Proposer un surnom parlant pour chacun des dix.
- Installer un plugin d'affichage des noms et refaire la lecture.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le compte des surnoms muets est juste.

#### PL-09 — Ce qui s'installera vraiment sur ce poste

| Rubrique | Valeur |
|---|---|
| **Lot** | PL — Écosystème de plugins |
| **Thématique** | PL1 · Écosystème de plugins |
| **Réf. référentiel** | REF-030 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 15 min |
| **Prérequis** | PL-02 |
| **Compétence visée** | Confronter les exigences de version d'un ensemble de plugins à la version installée, avant de promettre une configuration. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-06 Valise de chantier |
| **Statut de production** | À produire |

**1. Compétence visée** — Confronter les exigences de version d'un ensemble de plugins à la version installée, avant de promettre une configuration.

**1 bis. Contexte métier** — Le poste tourne sous Rhino 8. La liste des plugins souhaités vient d'ailleurs, et chacun annonce la version qu'il exige.

**2. Composants mobilisés** — Nombre, Smaller Than, Cull Pattern, List Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les neuf plugins vous sont fournis avec la version de Rhino qu'ils exigent au minimum. Le poste tourne sous Rhino 8. Donnez le nombre de plugins installables.

**4. Données de départ fournies** — Les neuf plugins et la version minimale exigée par chacun.

**5. Résultat attendu** — 7 plugins sur 9 sont installables sur Rhino 8.

**6. Zone CORRIGÉ — explication étape par étape**

1. Comprendre que la version déclarée est un minimum.
2. Comparer chaque exigence à la version du poste.
3. Compter.

**6 bis. Erreur attendue** — Ne retenir que ceux qui annoncent exactement 8 — il y en a trois. Une version minimale est un PLANCHER : un plugin écrit pour Rhino 6 s'installe sur Rhino 8. Ce sont les deux qui exigent Rhino 9 qui ne passeront pas.

**6 ter. Justification du jeu de données** — Neuf plugins répartis de Rhino 5 à Rhino 9, dont trois exactement à 8 : la lecture « exactement » donne 3, la lecture « au moins » donne 7, et la lecture « tous sauf le plus récent » donne 8. Trois réponses distinctes pour trois façons de se tromper.

**6 quater. Limite de la correction automatique** — Une version minimale ne garantit pas la compatibilité vers le haut : un plugin écrit pour Rhino 6 peut ne plus fonctionner sous Rhino 8. L'exercice traite ce que le catalogue déclare, pas ce que l'exécution révèle.

**7. Pièges fréquents**

- Chercher l'égalité exacte.
- Supposer qu'un plugin ancien ne fonctionnera pas.

**8. Variantes et extensions**

- Trouver la version de Rhino qui permettrait d'installer les neuf.
- Croiser avec les dépendances de PL-05.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le compte est juste.

#### PL-10 — Où chercher un plugin

| Rubrique | Valeur |
|---|---|
| **Lot** | PL — Écosystème de plugins |
| **Thématique** | PL1 · Écosystème de plugins |
| **Réf. référentiel** | REF-029, REF-030 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 8 min |
| **Prérequis** | PL-02 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Un plugin est disponible à la fois sur le site communautaire et dans le gestionnaire de paquets intégré.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Un plugin est proposé des deux côtés. Par lequel l'installez-vous, et pourquoi ?
a) Le site communautaire : on y trouve la version la plus récente.
b) Le gestionnaire de paquets : il gère les dépendances, les versions et la désinstallation. ← réponse
c) Peu importe, le fichier installé est le même.
d) Le site communautaire, pour lire les avis avant d'installer.

Valeur diagnostique : (c) est vrai du seul fichier et faux de tout le reste — ce qui distingue les deux voies n'est pas le binaire, c'est ce qui l'entoure : les dépendances tirées automatiquement, la mise à jour qui remplace vraiment, et la désinstallation qui nettoie. (a) et (d) décrivent de bonnes raisons de CONSULTER le site, pas d'y télécharger.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

#### PL-11 — Deux familles de plugins

| Rubrique | Valeur |
|---|---|
| **Lot** | PL — Écosystème de plugins |
| **Thématique** | PL1 · Écosystème de plugins |
| **Réf. référentiel** | REF-031, REF-034, REF-035, REF-036, REF-037 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 8 min |
| **Prérequis** | PL-03 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Certains plugins ajoutent des composants ; d'autres ne changent que la façon dont on travaille.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Qu'est-ce qui sépare un plugin d'ERGONOMIE d'un plugin FONCTIONNEL, pour celui qui recevra votre définition ?
a) L'ergonomie est gratuite, le fonctionnel est payant.
b) L'ergonomie ne laisse aucune trace dans le fichier livré ; le fonctionnel devient une dépendance. ← réponse
c) L'ergonomie est réservée aux débutants.
d) Le fonctionnel est plus lourd à installer.

Valeur diagnostique : la question ne porte pas sur ce que le plugin fait pour VOUS, mais sur ce qu'il impose à l'autre. Un plugin qui aligne, colore ou affiche les noms peut être désinstallé sans qu'aucune définition cesse de fonctionner. Un plugin qui ajoute un composant est dans le fichier, et le suit partout — c'est ce que PL-06 mesure.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

#### PL-12 — Le plugin qui n'est plus maintenu

| Rubrique | Valeur |
|---|---|
| **Lot** | PL — Écosystème de plugins |
| **Thématique** | PL1 · Écosystème de plugins |
| **Réf. référentiel** | REF-039 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 8 min |
| **Prérequis** | PL-11 |
| **Case Bloom (révisée)** | Évaluer × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Le plugin sur lequel repose une définition de production n'a pas été mis à jour depuis trois ans.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Une définition de production dépend d'un plugin abandonné depuis trois ans. Que faites-vous en premier ?
a) Chercher un plugin de remplacement équivalent.
b) Repérer ce que ce plugin fait réellement dans la définition, et si c'est encore indispensable. ← réponse
c) Figer la version de Rhino pour que rien ne bouge.
d) Réécrire la partie concernée en natif, sans attendre.

Valeur diagnostique : (c) est la réaction la plus répandue, et c'est un report de décision — figer Rhino gèle aussi tout le reste, et le problème revient dans un an, aggravé. (a) et (d) sont des solutions, mais on ne choisit pas une solution avant de savoir ce qu'on remplace : sur une définition ancienne, il est fréquent que le plugin ne serve plus qu'à une étape devenue inutile.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

---

## Lot MP — Méthode, performance et évènements

**Niveau** : Intermédiaire à perfectionnement · **4 exercices** · **1 h 28 cumulées**

Méthode et performance : rendre une définition reprenable par un tiers, trouver ce qui coûte réellement le temps de calcul, comprendre le modèle évènementiel.

| ID | Titre | Thématique | Niveau | Durée | Validation |
|---|---|---|---|---|---|
| MP-01 | Une définition qu'un autre peut reprendre | MP1 · Organisation et lisibilité | Intermédiaire | 30 min | Visuel |
| MP-02 | Trouver ce qui coûte le temps de calcul | MP2 · Performance d'exécution | Perfectionnement | 25 min | SingleValue |
| MP-03 | Une définition qui réagit | MP3 · Chronologie et évènements | Perfectionnement | 8 min | — |
| MP-04 | Ce qu'un curseur fait recalculer | MP1 · Chronologie et évènements | Perfectionnement | 25 min | SingleValue |

### MP1 · Organisation et lisibilité

*1 exercices — MP-01*

#### MP-01 — Une définition qu'un autre peut reprendre

| Rubrique | Valeur |
|---|---|
| **Lot** | MP — Méthode, performance et évènements |
| **Thématique** | MP1 · Organisation et lisibilité |
| **Réf. référentiel** | REF-088 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | A-31 |
| **Compétence visée** | Organiser une définition pour qu'un tiers la reprenne sans explication orale. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-18 Duel de versions |
| **Statut de production** | À produire |

**1. Compétence visée** — Organiser une définition pour qu'un tiers la reprenne sans explication orale.

**1 bis. Contexte métier** — Vous partez en congés et la définition doit vivre sans vous.

**2. Composants mobilisés** — Groupes, scribbles, paramètres nommés

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Reprenez une de vos définitions et rendez-la reprenable : entrées rassemblées et nommées, étapes groupées et titrées, sorties identifiées. Faites-la relire par quelqu'un qui ne l'a pas écrite, sans un mot d'explication.

**4. Données de départ fournies** — Une définition existante, fonctionnelle mais non organisée.

**5. Résultat attendu** — Une définition dont un tiers retrouve seul les entrées, la logique et les sorties.

**6. Zone CORRIGÉ — explication étape par étape**

1. Rassembler toutes les entrées réglables au même endroit, à gauche, et les nommer par ce qu'elles représentent.
2. Grouper les étapes par intention — « répartir les montants » — et non par famille de composant.
3. Titrer chaque groupe d'une phrase, pas d'un mot.
4. Identifier les sorties et les isoler.
5. Faire l'essai de reprise par un tiers, en silence.

**6 bis. Erreur attendue** — Ajouter des commentaires partout au lieu de structurer. Un scribble sur chaque composant n'est pas de la lisibilité, c'est du bruit : ce qui se lit, c'est un groupe titré par ce qu'il fait, pas par le composant qu'il contient.

**6 ter. Justification du jeu de données** — —

**6 quater. Limite de la correction automatique** — La lisibilité ne se mesure pas par un nombre. Le seul contrôle honnête est celui que l'énoncé prescrit : quelqu'un d'autre reprend la définition, ou n'y arrive pas.

**7. Pièges fréquents**

- Titrer les groupes du nom des composants qu'ils contiennent : cela n'apprend rien à qui lit.
- Laisser des composants orphelins hors de tout groupe : ils font douter de ce qui est actif.

**8. Variantes et extensions**

- Reprendre une définition d'un collègue et mesurer le temps qu'il vous faut pour la comprendre.
- Rédiger la notice d'une page qui l'accompagne.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode Visuel.

**10. Barème** — Grille : entrées rassemblées (1), groupes titrés par intention (2), reprise réussie par un tiers (2).

### MP2 · Performance d'exécution

*1 exercices — MP-02*

#### MP-02 — Trouver ce qui coûte le temps de calcul

| Rubrique | Valeur |
|---|---|
| **Lot** | MP — Méthode, performance et évènements |
| **Thématique** | MP2 · Performance d'exécution |
| **Réf. référentiel** | REF-089 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | MP-01 |
| **Compétence visée** | Localiser le composant qui coûte le temps de recalcul, plutôt que d'optimiser au hasard. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-01 Score visible |
| **Statut de production** | À produire |

**1. Compétence visée** — Localiser le composant qui coûte le temps de recalcul, plutôt que d'optimiser au hasard.

**1 bis. Contexte métier** — Une définition met plusieurs secondes à se recalculer à chaque mouvement de curseur, et le client attend devant l'écran.

**2. Composants mobilisés** — Sort List, Reverse List, Sub List, Mass Addition, Division, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les temps de recalcul des 20 composants d'une définition vous sont fournis, en millisecondes. Donnez la part du temps total que représentent les trois composants les plus coûteux, en pourcentage arrondi à l'entier.

**4. Données de départ fournies** — Les 20 temps mesurés, en millisecondes, dans l'ordre du profil affiché par Grasshopper.

**5. Résultat attendu** — 97 — la part des trois composants les plus coûteux, en pourcentage entier.

**6. Zone CORRIGÉ — explication étape par étape**

1. Sommer les vingt temps pour obtenir le total.
2. Trier les temps par ordre décroissant.
3. Prélever les trois premiers et les sommer.
4. Rapporter au total et convertir en pourcentage.
5. Arrondir à l'entier, et en tirer la conclusion : c'est là, et seulement là, qu'il faut travailler.

**6 bis. Erreur attendue** — Optimiser les composants nombreux plutôt que les composants lents. Dix-sept composants du relevé coûtent moins de 15 ms chacun : les régler tous ne fera rien gagner. Trois en coûtent presque tout — et c'est contre-intuitif tant qu'on n'a pas mesuré.

**6 ter. Justification du jeu de données** — Le relevé est volontairement très déséquilibré : trois composants au-dessus de 1 800 ms, dix-sept sous 30 ms. C'est la répartition réelle d'une définition lente, et c'est ce qui rend la mesure indispensable.

**7. Pièges fréquents**

- Trier sans inverser : on prend les trois plus rapides.
- Conclure que la définition est « globalement lente » : elle ne l'est pas, trois composants le sont.

**8. Variantes et extensions**

- Chiffrer le gain si l'un des trois passait à 100 ms.
- Mesurer le profil réel d'une de vos définitions et refaire l'analyse.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si la part est juste à l'entier près.

### MP3 · Chronologie et évènements

*1 exercices — MP-03*

#### MP-03 — Une définition qui réagit

| Rubrique | Valeur |
|---|---|
| **Lot** | MP — Méthode, performance et évènements |
| **Thématique** | MP3 · Chronologie et évènements |
| **Réf. référentiel** | REF-091, REF-092 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 8 min |
| **Prérequis** | MP-02 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — On voudrait qu'une définition réagisse à une touche ou à un clic dans la vue.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Grasshopper recalcule quand une donnée change. Comment lui faire prendre en compte un évènement clavier ou souris ?
a) C'est impossible, Grasshopper n'écoute rien.
b) Par un composant qui expose l'évènement comme une donnée, laquelle déclenche alors le recalcul habituel. ← réponse
c) En relançant la définition à la main.
d) En écrivant un plugin, il n'y a pas d'autre voie.

Valeur diagnostique : (a) et (d) sont deux façons de renoncer trop tôt. Le point à faire passer est conceptuel : le modèle de Grasshopper reste le même — une donnée change, l'aval se recalcule. L'évènement n'est pas une exception au modèle, c'est une donnée de plus.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

### MP1 · Chronologie et évènements

*1 exercices — MP-04*

#### MP-04 — Ce qu'un curseur fait recalculer

| Rubrique | Valeur |
|---|---|
| **Lot** | MP — Méthode, performance et évènements |
| **Thématique** | MP1 · Chronologie et évènements |
| **Réf. référentiel** | REF-090 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | MP-02 |
| **Compétence visée** | Déterminer ce qu'une modification fait recalculer, en suivant les dépendances plutôt qu'en supposant que tout repasse. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-13 Chronomètre |
| **Statut de production** | À produire |

**1. Compétence visée** — Déterminer ce qu'une modification fait recalculer, en suivant les dépendances plutôt qu'en supposant que tout repasse.

**1 bis. Contexte métier** — La définition met trois secondes à répondre au moindre mouvement de curseur. Avant d'optimiser quoi que ce soit, il faut savoir ce qui repasse réellement.

**2. Composants mobilisés** — Texte, Member Index, Cull Pattern, List Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les liaisons du graphe vous sont fournies. Donnez le nombre de composants qui se recalculent lorsque le curseur Largeur est déplacé.

**4. Données de départ fournies** — Les quatorze composants du graphe et leurs liaisons.

**5. Résultat attendu** — 10 composants se recalculent.

**6. Zone CORRIGÉ — explication étape par étape**

1. Partir du composant modifié.
2. Suivre les liaisons vers l'aval, de proche en proche.
3. Compter ce qui a été atteint, sans compter deux fois ce que deux branches atteignent.

**6 bis. Erreur attendue** — Répondre 13, tout le graphe moins le curseur. Grasshopper ne recalcule que ce qui DÉPEND de ce qui a changé : Hauteur, Essence et Prix unitaire ne dépendent pas de Largeur, et restent intacts. Croire que tout repasse conduit à optimiser au mauvais endroit.

**6 ter. Justification du jeu de données** — Quatorze composants, dont trois entrées indépendantes et un graphe à deux branches qui se rejoignent : suivre les dépendances à la main est faisable mais fastidieux, et c'est exactement le genre de comptage qu'on préfère supposer plutôt que faire.

**6 quater. Limite de la correction automatique** — Le compte des composants n'est pas le compte des secondes : un seul composant lourd pèse plus que neuf légers. C'est le profileur qui le dit, et MP-02 qui l'aborde.

**7. Pièges fréquents**

- Compter tout le graphe.
- Compter deux fois un composant atteint par deux chemins.
- Remonter vers l'amont : ce qui alimente un composant ne se recalcule pas parce qu'il change.

**8. Variantes et extensions**

- Refaire le compte pour le curseur Essence.
- Trouver l'entrée dont la modification recalcule le moins.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le compte des composants recalculés est juste.

---

## Lot AV — Algorithmique avancée

**Niveau** : Perfectionnement · **3 exercices** · **1 h 50 cumulées**

Algorithmique avancée : converger par itérations sur un critère, conduire une simulation jusqu'à l'équilibre, poser un problème de recherche de forme.

| ID | Titre | Thématique | Niveau | Durée | Validation |
|---|---|---|---|---|---|
| AV-01 | Converger vers une portée | AV1 · Boucles et itération | Perfectionnement | 35 min | SingleValue |
| AV-02 | Une chaînette qui se stabilise | AV2 · Simulation physique | Perfectionnement | 35 min | NumericTolerance |
| AV-03 | Chercher la meilleure trame | AV3 · Design génératif | Perfectionnement | 40 min | SingleValue |

### AV1 · Boucles et itération

*1 exercices — AV-01*

#### AV-01 — Converger vers une portée

| Rubrique | Valeur |
|---|---|
| **Lot** | AV — Algorithmique avancée |
| **Thématique** | AV1 · Boucles et itération |
| **Réf. référentiel** | REF-093 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 35 min |
| **Prérequis** | A-30 |
| **Compétence visée** | Faire converger un calcul par itérations successives jusqu'à un critère d'arrêt. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-02 Barre de progression |
| **Statut de production** | À produire |

**1. Compétence visée** — Faire converger un calcul par itérations successives jusqu'à un critère d'arrêt.

**1 bis. Contexte métier** — La flèche d'une poutre dépend de sa portée d'une façon qui ne s'inverse pas simplement : on cherche la portée qui donne la flèche admissible.

**2. Composants mobilisés** — Plugin de boucle, Larger Than, Addition, Division, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La flèche admissible est atteinte pour une portée comprise entre 1 000 et 4 000 mm. Approchez cette portée par bissection jusqu'à ce que l'intervalle passe sous 1 mm, et donnez le nombre d'itérations nécessaires.

**4. Données de départ fournies** — La fonction de flèche, l'intervalle de départ et le critère d'arrêt.

**5. Résultat attendu** — 12 — le nombre de bissections pour ramener 3 000 mm sous 1 mm.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser l'intervalle de départ et le critère d'arrêt avant d'écrire la boucle.
2. À chaque passage, couper l'intervalle en deux et garder la moitié qui encadre la solution.
3. Compter les passages.
4. Sortir dès que la largeur de l'intervalle passe sous 1 mm.
5. Contrôler : 3 000 divisé douze fois par deux vaut 0,73 mm, onze fois seulement 1,46.

**6 bis. Erreur attendue** — Fixer le nombre d'itérations à l'avance plutôt que de sortir sur un critère. Une boucle à compte fixe s'arrête trop tôt ou tourne pour rien ; c'est le critère qui doit commander, et c'est là toute la différence entre répéter et converger.

**6 ter. Justification du jeu de données** — L'intervalle de départ vaut 3 000 mm : chaque bissection le divise par deux, il faut donc douze passages pour descendre sous 1 mm. Le compte est vérifiable à la main, ce qui permet de contrôler la boucle sans la croire sur parole.

**6 quater. Limite de la correction automatique** — L'itération demande un plugin de boucle : ce n'est pas natif. C'est le nombre d'itérations qui est validé, pas le montage.

**7. Pièges fréquents**

- Boucle sans critère de sortie : elle tourne indéfiniment.
- Garder la mauvaise moitié de l'intervalle : la boucle converge, mais ailleurs.

**8. Variantes et extensions**

- Passer le critère à 0,1 mm et prévoir le nombre d'itérations avant de le mesurer.
- Comparer à une recherche par pas constant et chiffrer l'écart.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre d'itérations vaut 12 et si la sortie se fait sur le critère, non sur un compte.

### AV2 · Simulation physique

*1 exercices — AV-02*

#### AV-02 — Une chaînette qui se stabilise

| Rubrique | Valeur |
|---|---|
| **Lot** | AV — Algorithmique avancée |
| **Thématique** | AV2 · Simulation physique |
| **Réf. référentiel** | REF-094 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 35 min |
| **Prérequis** | AV-01 |
| **Compétence visée** | Conduire une simulation jusqu'à l'équilibre et relever une grandeur sur l'état stabilisé. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 5 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Statut de production** | À produire |

**1. Compétence visée** — Conduire une simulation jusqu'à l'équilibre et relever une grandeur sur l'état stabilisé.

**1 bis. Contexte métier** — Un câble de suspension prend, sous son propre poids, une forme qu'on ne dessine pas : on la laisse s'établir.

**2. Composants mobilisés** — Moteur de simulation physique, Divide Curve, Bounds, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le câble mesure 6 000 mm et ses deux ancrages sont distants de 4 800 mm. Laissez la forme s'établir sous son poids propre, et donnez la flèche au point bas, en millimètres.

**4. Données de départ fournies** — Les deux ancrages, la longueur de câble et le moteur de simulation.

**5. Résultat attendu** — La flèche au point bas, à 5 mm près.

**6. Zone CORRIGÉ — explication étape par étape**

1. Discrétiser le câble en segments réguliers.
2. Ancrer les deux extrémités, laisser le reste libre.
3. Appliquer le poids propre et lancer la simulation.
4. Attendre que la valeur relevée cesse d'évoluer — c'est le seul critère d'arrêt honnête.
5. Mesurer l'écart vertical entre les ancrages et le point bas.

**6 bis. Erreur attendue** — Relever la valeur avant stabilisation. Une simulation affiche un résultat dès la première itération, et il change encore. Lire trop tôt donne une valeur plausible et fausse — le seul contrôle est que la valeur cesse de bouger.

**6 ter. Justification du jeu de données** — 6 000 mm de câble pour 4 800 mm de portée : le mou est assez important pour que la flèche soit franche, et la forme obtenue reste une chaînette, dont la flèche se vérifie par le calcul.

**6 quater. Limite de la correction automatique** — La simulation demande un moteur dédié, non natif. La tolérance de 5 mm tient compte de la convergence, qui n'est jamais exactement reproductible.

**7. Pièges fréquents**

- Trop peu de segments : la forme est anguleuse et la flèche sous-évaluée.
- Lire la valeur en cours de convergence.

**8. Variantes et extensions**

- Rallonger le câble de 10 % et prévoir l'effet sur la flèche avant de le mesurer.
- Comparer à la formule de la chaînette.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si la flèche est juste à 5 mm près sur un état stabilisé.

### AV3 · Design génératif

*1 exercices — AV-03*

#### AV-03 — Chercher la meilleure trame

| Rubrique | Valeur |
|---|---|
| **Lot** | AV — Algorithmique avancée |
| **Thématique** | AV3 · Design génératif |
| **Réf. référentiel** | REF-095 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 40 min |
| **Prérequis** | AV-02 |
| **Compétence visée** | Poser un problème de recherche de forme — variables, objectif, contraintes — et juger l'optimum obtenu. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-21 Optimisation comparée |
| **Statut de production** | À produire |

**1. Compétence visée** — Poser un problème de recherche de forme — variables, objectif, contraintes — et juger l'optimum obtenu.

**1 bis. Contexte métier** — Une façade doit être calepinée : moins de panneaux coûte moins cher, mais aucun panneau ne peut dépasser 2 400 mm.

**2. Composants mobilisés** — Moteur d'optimisation, Division, Round, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La façade mesure 18 600 mm de long. Cherchez le calepinage qui minimise le nombre de panneaux sans qu'aucun dépasse 2 400 mm, et donnez ce nombre.

**4. Données de départ fournies** — La longueur de façade, la largeur maximale de panneau, et un moteur de recherche.

**5. Résultat attendu** — 8 — le nombre minimal de panneaux.

**6. Zone CORRIGÉ — explication étape par étape**

1. Écrire d'abord ce qu'on minimise et sous quelle contrainte.
2. Exprimer la contrainte DANS la fonction évaluée, non à côté.
3. Lancer la recherche.
4. Contrôler l'optimum par le calcul direct : 18 600 ÷ 2 400 arrondi au supérieur.
5. Conclure : quand le calcul direct suffit, le moteur de recherche est un luxe — savoir le reconnaître fait partie de la compétence.

**6 bis. Erreur attendue** — Laisser le moteur chercher sans contrainte et retenir son meilleur résultat. Sans la contrainte des 2 400 mm exprimée dans la fonction évaluée, l'optimum est un panneau unique de 18 600 mm : mathématiquement parfait, physiquement absurde. Une recherche de forme ne vaut que ce que vaut ce qu'on lui demande d'optimiser.

**6 ter. Justification du jeu de données** — 18 600 divisé par 2 400 vaut 7,75 : la réponse est 8, et l'exercice ne se résout pas en arrondissant au plus proche. C'est aussi un cas où le moteur de recherche est un détour — le calcul direct suffit, et c'est un enseignement en soi.

**6 quater. Limite de la correction automatique** — La recherche demande un moteur d'optimisation. Ce qui est validé est le nombre de panneaux ; l'exercice vaut surtout pour la formulation du problème, que le formateur relit.

**7. Pièges fréquents**

- Contrainte laissée hors de la fonction évaluée.
- Employer un moteur de recherche là où une division suffit, et ne pas s'en apercevoir.

**8. Variantes et extensions**

- Ajouter une contrainte de panneaux tous égaux et refaire la recherche.
- Introduire un coût par joint et voir l'optimum se déplacer.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre vaut 8 et si la contrainte figure dans la fonction évaluée.

---

## Lot DV — Développement, scripting et API

**Niveau** : Expert · **9 exercices** · **4 h 47 cumulées**

Développement : quand scripter plutôt que câbler, employer l'interface de programmation de Rhino, et passer du composant scripté au plugin installé.

| ID | Titre | Thématique | Niveau | Durée | Validation |
|---|---|---|---|---|---|
| DV-01 | Quand écrire du script plutôt que câbler | DV1 · Scripting dans Grasshopper | Expert | 8 min | — |
| DV-02 | Un composant scripté qui parle à RhinoCommon | DV2 · API et librairies | Expert | 35 min | NumericTolerance |
| DV-03 | Ce que les librairies évitent d'écrire | DV2 · API et librairies | Expert | 8 min | — |
| DV-04 | Du composant scripté au plugin installé | DV3 · Compilation et IDE | Expert | 120 min | Visuel |
| DV-05 | Ce que la compilation change vraiment | DV3 · Compilation et IDE | Expert | 8 min | — |
| DV-06 | Le plugin qui parle aussi à Rhino | DV3 · Compilation et IDE | Expert | 8 min | — |
| DV-07 | Un plugin qui s'installe chez quelqu'un d'autre | DV3 · Compilation et IDE | Expert | 50 min | Visuel |
| DV-08 | Ce que le remappage fait aux branches | DV2 · API et librairies | Expert | 25 min | SingleValue |
| DV-09 | La division qui n'est pas celle qu'on croit | DV1 · Scripting dans Grasshopper | Expert | 25 min | SingleValue |

### DV1 · Scripting dans Grasshopper

*2 exercices — DV-01, DV-09*

#### DV-01 — Quand écrire du script plutôt que câbler

| Rubrique | Valeur |
|---|---|
| **Lot** | DV — Développement, scripting et API |
| **Thématique** | DV1 · Scripting dans Grasshopper |
| **Réf. référentiel** | REF-100 |
| **Niveau** | Expert |
| **Durée cible** | 8 min |
| **Prérequis** | IA-04 |
| **Case Bloom (révisée)** | Évaluer × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Une partie de définition compte quarante composants pour une opération qui s'écrirait en cinq lignes.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Quand vaut-il mieux écrire un composant scripté que câbler des composants natifs ?
a) Dès qu'on sait programmer : c'est toujours plus rapide.
b) Quand la logique est itérative ou conditionnelle, et que le câblage la rendrait illisible. ← réponse
c) Jamais : une définition doit rester lisible par des non-programmeurs.
d) Uniquement pour les performances.

Valeur diagnostique : (a) et (c) sont deux dogmes symétriques et également coûteux. Le premier produit des définitions que personne d'autre ne maintient ; le second fait câbler des boucles sur cinquante composants. Le critère utile est la lisibilité du résultat, pas la préférence de celui qui écrit.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

#### DV-09 — La division qui n'est pas celle qu'on croit

| Rubrique | Valeur |
|---|---|
| **Lot** | DV — Développement, scripting et API |
| **Thématique** | DV1 · Scripting dans Grasshopper |
| **Réf. référentiel** | REF-100, REF-102 |
| **Niveau** | Expert |
| **Durée cible** | 25 min |
| **Prérequis** | DV-01 |
| **Compétence visée** | Anticiper le comportement d'un opérateur selon le TYPE de ses opérandes, dans un composant scripté. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-15 Relecture de code |
| **Statut de production** | À produire |

**1. Compétence visée** — Anticiper le comportement d'un opérateur selon le type de ses opérandes, dans un composant scripté.

**1 bis. Contexte métier** — Le script calcule combien de panneaux entiers chaque pièce consomme. Les quantités sont des entiers, et l'opérateur de division aussi.

**2. Composants mobilisés** — Nombre, Division, Round, Mass Addition, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le script divise chacune des dix quantités par 4 et somme les résultats. Les quantités et le diviseur sont déclarés comme des ENTIERS. Donnez la somme rendue par le script.

**4. Données de départ fournies** — Les dix quantités, le diviseur, et le type déclaré des variables.

**5. Résultat attendu** — 32 — la somme des quotients entiers.

**6. Zone CORRIGÉ — explication étape par étape**

1. Diviser chaque quantité en respectant le type entier.
2. Sommer.
3. Comparer au résultat qu'aurait donné une division réelle.

**6 bis. Erreur attendue** — Calculer en réel et rendre 37. Sur des entiers, la division tronque : 7 ÷ 4 donne 1 et non 1,75. L'écart de 5 est ici visible, mais le même script rendrait un résultat plausible sur d'autres données — et c'est ce qui rend l'erreur durable.

**6 ter. Justification du jeu de données** — Dix quantités dont aucune n'est multiple de 4 : la troncature agit à chaque terme, et l'écart s'accumule au lieu de se compenser. Les deux réponses, 32 et 37, sont assez proches pour paraître toutes deux crédibles — c'est exactement le danger.

**6 quater. Limite de la correction automatique** — Ce que le script doit rendre dépend du métier : pour des panneaux entiers, la troncature est peut-être juste, ou peut-être faut-il arrondir au supérieur. L'exercice porte sur ce que le langage FAIT, pas sur ce qu'il faudrait vouloir.

**7. Pièges fréquents**

- Diviser en réel.
- Arrondir au lieu de tronquer : sur ces données les deux diffèrent.

**8. Variantes et extensions**

- Reprendre en déclarant les variables en réel et mesurer l'écart.
- Rendre le nombre de panneaux réellement nécessaires, arrondi au supérieur.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si la somme des quotients entiers est juste.

### DV2 · API et librairies

*3 exercices — DV-02, DV-03, DV-08*

#### DV-02 — Un composant scripté qui parle à RhinoCommon

| Rubrique | Valeur |
|---|---|
| **Lot** | DV — Développement, scripting et API |
| **Thématique** | DV2 · API et librairies |
| **Réf. référentiel** | REF-101, REF-102, REF-103 |
| **Niveau** | Expert |
| **Durée cible** | 35 min |
| **Prérequis** | IA-04 |
| **Compétence visée** | Employer l'interface de programmation de Rhino depuis un composant scripté pour obtenir ce qu'aucun composant natif ne donne. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | NumericTolerance — tolérance 5 |
| **Solution de référence** | 7 composants |
| **Gamification associée** | G-06 Cible et précision |
| **Statut de production** | À produire |

**1. Compétence visée** — Employer l'interface de programmation de Rhino depuis un composant scripté pour obtenir ce qu'aucun composant natif ne donne.

**1 bis. Contexte métier** — On cherche, sur une courbe, le point où le rayon de courbure passe sous le rayon de cintrage de la machine — information qu'aucun composant natif ne rend directement.

**2. Composants mobilisés** — C# Script ou Python 3 Script, Curve, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le rayon de cintrage minimal de la machine est de 250 mm. Sur la courbe fournie, donnez la longueur cumulée des portions où le rayon de courbure descend sous cette valeur, en millimètres.

**4. Données de départ fournies** — La courbe de tracé et le rayon de cintrage minimal.

**5. Résultat attendu** — La longueur cumulée des portions trop cintrées, à 5 mm près.

**6. Zone CORRIGÉ — explication étape par étape**

1. Choisir un pas d'échantillonnage et le justifier par rapport à la taille de la zone recherchée.
2. Parcourir la courbe et relever la courbure en chaque point, via l'interface de programmation.
3. Convertir la courbure en rayon — l'un est l'inverse de l'autre.
4. Repérer les intervalles où le rayon passe sous le seuil.
5. Sommer leurs longueurs, et contrôler en divisant le pas par deux : le résultat doit peu bouger.

**6 bis. Erreur attendue** — Échantillonner la courbe trop grossièrement. La courbure varie continûment : sur un développé de près de six mètres, un échantillon tous les 200 mm peut enjamber entièrement la zone trop cintrée et conclure que la pièce est fabricable. Le pas d'échantillonnage est un choix, et il doit être justifié — seconde erreur, plus discrète : échantillonner à pas de PARAMÈTRE constant et non à pas de LONGUEUR constante. Les paramètres se resserrent dans les courbes, et la zone trop cintrée ressort quatre fois trop longue.

**6 ter. Justification du jeu de données** — Le tracé mesure 5 988 mm et son rayon tombe à 155 mm sur un coude unique : quelque 106 mm passent sous les 250 mm admis, soit moins de deux pour cent du développé. Assez large pour être trouvé avec un pas raisonnable, assez étroit pour être manqué avec un pas négligent. La tolérance de 5 mm sanctionne la détection, non la finesse du pas : un point tous les 10 mm suffit à passer, un point tous les 20 mm ne suffit plus.

**7. Pièges fréquents**

- Confondre courbure et rayon : ils varient en sens inverse.
- Pas d'échantillonnage choisi au hasard, sans contrôle de convergence.

**8. Variantes et extensions**

- Rendre le pas adaptatif : plus fin là où la courbure varie vite.
- Sortir aussi la position du point le plus cintré.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 1 point si la longueur est juste à 1 mm près et si le pas a été contrôlé par convergence.

#### DV-03 — Ce que les librairies évitent d'écrire

| Rubrique | Valeur |
|---|---|
| **Lot** | DV — Développement, scripting et API |
| **Thématique** | DV2 · API et librairies |
| **Réf. référentiel** | REF-104, REF-105 |
| **Niveau** | Expert |
| **Durée cible** | 8 min |
| **Prérequis** | DV-02 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Un besoin de géométrie de calcul — enveloppe convexe, triangulation — se présente dans un composant scripté.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Vous avez besoin d'une triangulation dans un composant scripté. Par où commencez-vous ?
a) L'écrire : c'est un bon exercice.
b) Chercher si RhinoCommon la fournit déjà, puis une librairie éprouvée. ← réponse
c) La demander à un assistant, qui l'écrira vite.
d) Changer d'approche pour éviter d'en avoir besoin.

Valeur diagnostique : (c) est devenu le réflexe majoritaire et c'est le plus trompeur — un assistant produit vite une triangulation qui marche sur le cas d'essai et échoue sur les cas dégénérés, que trente ans de bibliothèque ont, eux, déjà rencontrés. La question ne porte pas sur la difficulté d'écrire, mais sur le coût de valider.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

#### DV-08 — Ce que le remappage fait aux branches

| Rubrique | Valeur |
|---|---|
| **Lot** | DV — Développement, scripting et API |
| **Thématique** | DV2 · API et librairies |
| **Réf. référentiel** | REF-105 |
| **Niveau** | Expert |
| **Durée cible** | 25 min |
| **Prérequis** | DV-03 |
| **Compétence visée** | Prévoir la structure d'un arbre après un remappage de chemins, en raisonnant sur les chemins plutôt que sur les données. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-09 Arbre relu |
| **Statut de production** | À produire |

**1. Compétence visée** — Prévoir la structure d'un arbre après un remappage de chemins, en raisonnant sur les chemins plutôt que sur les données.

**1 bis. Contexte métier** — Le composant scripté reçoit un arbre à deux niveaux et doit rendre un résultat par valeur du second niveau, toutes origines confondues.

**2. Composants mobilisés** — Series, Cross Reference, Path Mapper, Tree Statistics, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> L'arbre porte trois valeurs au premier niveau de chemin et quatre au second, soit une branche par combinaison. Le remappage ne conserve que le second niveau. Donnez le nombre de branches obtenues.

**4. Données de départ fournies** — La structure de l'arbre de départ et la règle de remappage.

**5. Résultat attendu** — 4 branches — une par valeur du second niveau.

**6. Zone CORRIGÉ — explication étape par étape**

1. Compter les branches de départ : le produit des deux niveaux.
2. Comprendre que le remappage retire un niveau du chemin.
3. Compter les chemins distincts qui subsistent.

**6 bis. Erreur attendue** — Répondre 3, en conservant le mauvais maillon, ou 12 en supposant que le remappage ne change rien. Un remappage qui laisse tomber un niveau FUSIONNE les branches qui ne différaient que par lui : douze branches deviennent quatre, et chacune porte désormais trois fois plus de données.

**6 ter. Justification du jeu de données** — Trois et quatre sont premiers entre eux, de sorte que les trois réponses — 3, 4 et 12 — sont toutes distinctes et qu'aucune n'est un multiple trompeur des autres.

**6 quater. Limite de la correction automatique** — Le compte des branches ne dit rien de leur CONTENU ni de l'ordre dans lequel les données s'y retrouvent — qui dépend de l'ordre de parcours, et se relève plutôt qu'il ne se devine.

**7. Pièges fréquents**

- Conserver le mauvais niveau.
- Croire qu'un remappage ne change que l'étiquette.

**8. Variantes et extensions**

- Donner le nombre d'éléments par branche après remappage.
- Reprendre avec un aplatissement complet.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre de branches est juste.

### DV3 · Compilation et IDE

*4 exercices — DV-04, DV-05, DV-06, DV-07*

#### DV-04 — Du composant scripté au plugin installé

| Rubrique | Valeur |
|---|---|
| **Lot** | DV — Développement, scripting et API |
| **Thématique** | DV3 · Compilation et IDE |
| **Réf. référentiel** | REF-096, REF-097, REF-098, REF-099 |
| **Niveau** | Expert |
| **Durée cible** | 120 min |
| **Prérequis** | IA-07, DV-02 |
| **Compétence visée** | Passer d'un composant scripté à un plugin compilé et installé, côté Grasshopper et côté Rhino. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-25 Projet jalonné |
| **Statut de production** | À produire |

**1. Compétence visée** — Passer d'un composant scripté à un plugin compilé et installé, côté Grasshopper et côté Rhino.

**1 bis. Contexte métier** — Un composant scripté qui a fait ses preuves doit être distribué à l'équipe, sans que chacun recolle du code.

**2. Composants mobilisés** — Environnement de compilation, modèles de projet Rhino, RhinoCommon

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Reprenez le composant scripté de DV-02 et faites-en un plugin compilé, installé et visible dans Grasshopper. Ajoutez-y une commande Rhino qui rend le même service depuis la ligne de commande.

**4. Données de départ fournies** — Le composant scripté de DV-02, un environnement de compilation et les modèles de projet Rhino.

**5. Résultat attendu** — Un plugin chargé par Rhino, dont le composant apparaît dans Grasshopper et dont la commande répond en ligne de commande.

**6. Zone CORRIGÉ — explication étape par étape**

1. Partir du modèle de projet fourni par Rhino, plutôt que d'un projet vide.
2. Reporter le code du composant scripté, en déclarant explicitement entrées et sorties.
3. Figer le GUID du composant dès la première version.
4. Compiler pour la version de Rhino visée, déposer le fichier, le débloquer si Windows l'a marqué, relancer Rhino.
5. Ajouter la commande Rhino, en respectant la convention de nommage du plugin.

**6 bis. Erreur attendue** — Compiler pour la mauvaise cible. Un plugin construit pour une version majeure de Rhino ne se charge pas dans l'autre, et le symptôme est silencieux : le composant n'apparaît simplement pas, sans message d'erreur.

**6 ter. Justification du jeu de données** — —

**6 quater. Limite de la correction automatique** — Le livrable est un plugin compilé : la validation est visuelle, sur le composant et la commande réellement disponibles.

**7. Pièges fréquents**

- Cible de compilation qui ne correspond pas à la version installée : rien ne se charge, rien ne le dit.
- Fichier téléchargé non débloqué : même symptôme.
- GUID régénéré entre deux versions : les définitions des collègues cassent.

**8. Variantes et extensions**

- Ajouter une icône et une entrée d'aide.
- Publier le plugin avec une licence explicite et un numéro de version.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode Visuel.

**10. Barème** — Grille : composant visible dans Grasshopper (2), commande Rhino opérante (2), GUID stable et version documentée (1).

#### DV-05 — Ce que la compilation change vraiment

| Rubrique | Valeur |
|---|---|
| **Lot** | DV — Développement, scripting et API |
| **Thématique** | DV3 · Compilation et IDE |
| **Réf. référentiel** | REF-096 |
| **Niveau** | Expert |
| **Durée cible** | 8 min |
| **Prérequis** | DV-02 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Un composant scripté rend le service attendu depuis six mois, dans une trentaine de définitions. La question de le compiler se pose.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Votre composant scripté fonctionne. Que vous apporte d'abord sa compilation en .gha ?
a) Il ira plus vite : le code n'est plus interprété.
b) Il se distribue et se corrige en un seul endroit, sans que personne n'ouvre les définitions. ← réponse
c) Le code source devient illisible pour l'utilisateur.
d) Il pourra enfin appeler RhinoCommon.

Valeur diagnostique : (a) et (d) révèlent qu'on n'a pas situé ce qu'un composant scripté sait déjà faire — il appelle RhinoCommon, et sa lenteur vient presque toujours de l'algorithme, pas de l'interprétation. (c) est accessoire, et faux au sens strict : un .gha se décompile. Le vrai gain est de DISTRIBUTION : trente définitions qui embarquaient chacune leur copie du script deviennent trente définitions qui pointent vers une version unique.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

#### DV-06 — Le plugin qui parle aussi à Rhino

| Rubrique | Valeur |
|---|---|
| **Lot** | DV — Développement, scripting et API |
| **Thématique** | DV3 · Compilation et IDE |
| **Réf. référentiel** | REF-097, REF-099 |
| **Niveau** | Expert |
| **Durée cible** | 8 min |
| **Prérequis** | DV-05 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Le composant compilé rend service dans Grasshopper. On voudrait le même service depuis la ligne de commande Rhino.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Vous avez un .gha qui marche. Que faut-il pour offrir le même service en commande Rhino ?
a) Rien : un .gha est déjà chargé par Rhino, la commande suit.
b) Un plugin .rhp qui déclare la commande, les deux partageant la même bibliothèque de calcul. ← réponse
c) Réécrire le calcul en RhinoScript.
d) Publier le .gha sur le gestionnaire de paquets.

Valeur diagnostique : (a) confond « chargé par Rhino » et « exposé dans Rhino » — un .gha vit dans Grasshopper, et la ligne de commande ne connaît pas ses composants. La bonne réponse vaut surtout pour ce qu'elle implique : le calcul ne se duplique pas, il se met dans une bibliothèque que les deux plugins référencent. Sans quoi la commande et le composant divergeront à la première correction.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

#### DV-07 — Un plugin qui s'installe chez quelqu'un d'autre

| Rubrique | Valeur |
|---|---|
| **Lot** | DV — Développement, scripting et API |
| **Thématique** | DV3 · Compilation et IDE |
| **Réf. référentiel** | REF-098 |
| **Niveau** | Expert |
| **Durée cible** | 50 min |
| **Prérequis** | DV-06 |
| **Compétence visée** | Livrer un plugin qui se charge sur un poste qui n'est pas celui du développeur, et le prouver. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-23 Livraison à l'aveugle |
| **Statut de production** | À produire |

**1. Compétence visée** — Livrer un plugin qui se charge sur un poste qui n'est pas celui du développeur, et le prouver.

**1 bis. Contexte métier** — Le plugin marche sur votre poste. C'est la situation la moins informative qui soit : votre poste porte le SDK, les dépendances et les chemins de développement.

**2. Composants mobilisés** — Environnement de développement, gabarit de plugin Grasshopper, gestionnaire de paquets

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Reprenez le plugin de DV-04 et rendez-le installable : manifeste renseigné, dépendances embarquées ou déclarées, version visible. Faites-le installer par quelqu'un d'autre, sur un poste où l'environnement de développement n'est pas présent, et faites-lui exécuter le composant sans un mot d'explication.

**4. Données de départ fournies** — Le plugin de DV-04, et un poste qui n'est pas le vôtre.

**5. Résultat attendu** — Un plugin installé et fonctionnel sur un poste tiers, dont le composant apparaît dans l'onglet visé et rend le résultat attendu.

**6. Zone CORRIGÉ — explication étape par étape**

1. Renseigner le manifeste : nom, version, auteur, description, icône.
2. Lister les dépendances et décider, pour chacune, entre l'embarquer et l'exiger.
3. Produire le paquet d'installation.
4. Installer sur un poste tiers, sans environnement de développement.
5. Faire exécuter le composant par son utilisateur, sans assistance.

**6 bis. Erreur attendue** — Livrer le seul fichier compilé. Il se chargera chez vous et nulle part ailleurs : les dépendances qu'il trouve dans votre dossier de compilation n'existent pas sur le poste d'arrivée. Et l'échec ne dit rien — le composant est simplement absent de l'onglet, sans message.

**6 ter. Justification du jeu de données** — —

**6 quater. Limite de la correction automatique** — Le livrable se juge sur grille : il n'y a pas de définition Grasshopper à corriger, et c'est le propre de cet exercice. C'est aussi pourquoi la vérification passe par un TIERS — la seule qui distingue « ça marche » de « ça marche chez moi ».

**7. Pièges fréquents**

- Livrer le binaire seul.
- Oublier de faire croître le numéro de version : la mise à jour ne remplace alors rien.
- Tester sur son propre poste et conclure.

**8. Variantes et extensions**

- Publier sur le gestionnaire de paquets et faire installer par la voie normale.
- Livrer une version 2 et vérifier qu'elle remplace bien la première.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode Visuel.

**10. Barème** — Grille : manifeste complet (1), dépendances traitées (1), installation réussie sur un poste tiers (2), composant exécuté sans assistance (1).

---

## Lot WB — Interfaces, web et interopérabilité

**Niveau** : Perfectionnement à expert · **7 exercices** · **4 h 03 cumulées**

Interfaces et web : rendre une définition utilisable par un tiers, la publier en ligne, et distinguer ce que Rhino.Inside et Rhino.Compute font respectivement.

| ID | Titre | Thématique | Niveau | Durée | Validation |
|---|---|---|---|---|---|
| WB-01 | Une définition utilisable par quelqu'un d'autre | WB1 · Interfaces utilisateur | Perfectionnement | 40 min | Visuel |
| WB-02 | Publier un configurateur | WB2 · Publication web | Perfectionnement | 90 min | Visuel |
| WB-03 | Rhino sans Rhino | WB3 · Interopérabilité | Expert | 8 min | — |
| WB-04 | Ce qu'on expose, et ce qu'on cache | WB1 · Interfaces utilisateur | Perfectionnement | 25 min | SingleValue |
| WB-05 | Dimensionner le calcul d'un configurateur | WB3 · Interopérabilité | Expert | 30 min | SingleValue |
| WB-06 | Le poids du modèle que l'on télécharge | WB2 · Publication web | Perfectionnement | 25 min | SingleValue |
| WB-07 | Le plan qui tient sur la feuille | WB2 · Publication web | Perfectionnement | 25 min | SingleValue |

### WB1 · Interfaces utilisateur

*2 exercices — WB-01, WB-04*

#### WB-01 — Une définition utilisable par quelqu'un d'autre

| Rubrique | Valeur |
|---|---|
| **Lot** | WB — Interfaces, web et interopérabilité |
| **Thématique** | WB1 · Interfaces utilisateur |
| **Réf. référentiel** | REF-106, REF-107 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 40 min |
| **Prérequis** | MP-01 |
| **Compétence visée** | Donner à une définition une interface qui permette de s'en servir sans l'ouvrir. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-25 Projet jalonné |
| **Statut de production** | À produire |

**1. Compétence visée** — Donner à une définition une interface qui permette de s'en servir sans l'ouvrir.

**1 bis. Contexte métier** — Le commercial doit pouvoir configurer un produit devant le client, sans voir un seul composant.

**2. Composants mobilisés** — Paramètres nommés, bornes, groupes, intégration Rhino

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Reprenez une de vos définitions et donnez-lui une interface : seuls les paramètres utiles sont exposés, nommés en langage métier, avec leurs bornes. Faites-la utiliser par quelqu'un qui ne connaît pas Grasshopper.

**4. Données de départ fournies** — Une définition fonctionnelle et organisée.

**5. Résultat attendu** — Une définition pilotable par un tiers, sans ouverture du graphe.

**6. Zone CORRIGÉ — explication étape par étape**

1. Lister les paramètres et distinguer ceux que l'utilisateur doit régler de ceux qui relèvent du concepteur.
2. Renommer les premiers en langage métier — « hauteur d'allège », non « slider 3 ».
3. Poser des bornes qui interdisent les valeurs absurdes.
4. Rassembler l'interface au même endroit et masquer le reste.
5. Faire l'essai avec quelqu'un qui ne connaît pas l'outil.

**6 bis. Erreur attendue** — Exposer tous les paramètres. Une interface qui montre trente curseurs n'est pas une interface : le travail consiste justement à choisir les cinq qui comptent et à cacher le reste.

**6 ter. Justification du jeu de données** — —

**6 quater. Limite de la correction automatique** — L'utilisabilité ne se mesure pas par un nombre. Le contrôle est celui que l'énoncé prescrit : un tiers s'en sert, ou n'y arrive pas.

**7. Pièges fréquents**

- Bornes trop larges : l'utilisateur produit une géométrie impossible et croit s'être trompé.
- Noms techniques conservés : l'interface reste illisible.

**8. Variantes et extensions**

- Ajouter un jeu de valeurs par défaut correspondant au produit courant.
- Intégrer la définition dans Rhino pour qu'elle se lance comme une commande.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode Visuel.

**10. Barème** — Grille : paramètres choisis et nommés (2), bornes posées (1), usage réussi par un tiers (2).

#### WB-04 — Ce qu'on expose, et ce qu'on cache

| Rubrique | Valeur |
|---|---|
| **Lot** | WB — Interfaces, web et interopérabilité |
| **Thématique** | WB1 · Interfaces utilisateur |
| **Réf. référentiel** | REF-107 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | WB-01 |
| **Compétence visée** | Distinguer, parmi les entrées d'une définition, celles qui relèvent d'un choix de l'utilisateur de celles qui se déduisent ou qui règlent l'outil. |
| **Case Bloom (révisée)** | Analyser × conceptuelle |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 5 composants |
| **Gamification associée** | G-17 Passation |
| **Statut de production** | À produire |

**1. Compétence visée** — Distinguer, parmi les entrées d'une définition, celles qui relèvent d'un choix de l'utilisateur de celles qui se déduisent ou qui règlent l'outil.

**1 bis. Contexte métier** — La définition va être pilotée depuis Rhino par quelqu'un qui n'ouvrira jamais le graphe. Tout ce qu'on expose, il faudra le lui expliquer ; tout ce qu'on cache, il ne pourra plus le régler.

**2. Composants mobilisés** — Texte, Member Index, Cull Pattern, List Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La définition du meuble compte quatorze entrées, décrites une à une avec ce qu'elles commandent et ce dont elles dépendent. Donnez le nombre d'entrées à exposer dans l'interface.

**4. Données de départ fournies** — La liste des quatorze entrées et leur description.

**5. Résultat attendu** — 6 — les six entrées qui relèvent d'un choix du client.

**6. Zone CORRIGÉ — explication étape par étape**

1. Classer chaque entrée : choix, grandeur dérivée, ou réglage interne.
2. Écarter les réglages internes : ils appartiennent à l'auteur de la définition.
3. Écarter les grandeurs dérivées : les exposer autoriserait des saisies contradictoires.
4. Compter ce qui reste.

**6 bis. Erreur attendue** — Exposer les quatorze. L'utilisateur peut alors régler la tolérance de couture et la graine aléatoire du placage, et surtout saisir une hauteur de tiroir incompatible avec la hauteur du meuble : trois entrées se DÉDUISENT des autres, et les exposer revient à autoriser deux vérités contradictoires dans la même définition.

**6 ter. Justification du jeu de données** — Quatorze entrées : six choix, trois grandeurs dérivées, cinq réglages internes. Les trois familles donnent trois réponses distinctes — 6, 9 et 14 — donc trois erreurs lisibles. Les dérivées sont le vrai discriminant : les repérer demande de lire les dépendances, pas seulement les intitulés.

**6 quater. Limite de la correction automatique** — L'exercice valide un compte, pas une interface. Une interface à six champs mal nommés est aussi inutilisable qu'une interface à quatorze : le nommage se juge en WB-01.

**7. Pièges fréquents**

- Exposer tout ce qui est un curseur.
- Exposer une grandeur dérivée « pour laisser le choix », et créer une incohérence silencieuse.
- Cacher un vrai choix parce qu'il a une valeur par défaut raisonnable.

**8. Variantes et extensions**

- Nommer les six entrées en langage client et poser leurs bornes.
- Faire piloter la définition par quelqu'un qui ne connaît pas Grasshopper, et relever ce qu'il demande.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le compte est juste.

### WB2 · Publication web

*3 exercices — WB-02, WB-06, WB-07*

#### WB-02 — Publier un configurateur

| Rubrique | Valeur |
|---|---|
| **Lot** | WB — Interfaces, web et interopérabilité |
| **Thématique** | WB2 · Publication web |
| **Réf. référentiel** | REF-108, REF-109, REF-110 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 90 min |
| **Prérequis** | WB-01 |
| **Compétence visée** | Publier une définition sur le web et en faire sortir les livrables attendus par un client. |
| **Case Bloom (révisée)** | Créer × procédurale |
| **Mode de validation** | Visuel — tolérance — |
| **Solution de référence** | 0 composants |
| **Gamification associée** | G-25 Projet jalonné |
| **Statut de production** | À produire |

**1. Compétence visée** — Publier une définition sur le web et en faire sortir les livrables attendus par un client.

**1 bis. Contexte métier** — Le client veut configurer son produit depuis son navigateur et repartir avec un plan et un modèle 3D.

**2. Composants mobilisés** — Plateforme de publication web, export 3D, mise en plan

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Publiez la définition interfacée en WB-01 sur une plateforme web. Le configurateur doit permettre de régler les paramètres, de télécharger le modèle 3D et d'obtenir un plan au format PDF.

**4. Données de départ fournies** — La définition interfacée de WB-01 et un compte sur une plateforme de publication.

**5. Résultat attendu** — Un configurateur en ligne qui rend les trois livrables.

**6. Zone CORRIGÉ — explication étape par étape**

1. Vérifier que la définition ne dépend d'aucun plugin absent de la plateforme.
2. Contrôler les temps de calcul : ce qui prend cinq secondes en local est insupportable en ligne.
3. Publier, puis régler l'interface exposée.
4. Brancher l'export du modèle 3D.
5. Produire le plan PDF et vérifier qu'il reste juste pour toutes les valeurs autorisées.

**6 bis. Erreur attendue** — Publier sans borner les paramètres. En ligne, personne ne surveille : une valeur hors domaine produit une géométrie absurde, ou fait échouer le calcul côté serveur, et c'est le client qui le voit en premier.

**6 ter. Justification du jeu de données** — —

**6 quater. Limite de la correction automatique** — Le livrable est un service en ligne : validation visuelle. Dépend d'une plateforme tierce et d'un compte.

**7. Pièges fréquents**

- Plugin non disponible côté serveur : la définition ne calcule pas.
- Paramètres non bornés.
- Plan PDF correct pour la valeur par défaut seulement.

**8. Variantes et extensions**

- Ajouter un chiffrage automatique au configurateur.
- Mesurer le temps de réponse et l'optimiser.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode Visuel.

**10. Barème** — Grille : configurateur en ligne (2), export 3D (1), plan PDF juste sur toute la plage (2).

#### WB-06 — Le poids du modèle que l'on télécharge

| Rubrique | Valeur |
|---|---|
| **Lot** | WB — Interfaces, web et interopérabilité |
| **Thématique** | WB2 · Publication web |
| **Réf. référentiel** | REF-109 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | WB-02 |
| **Compétence visée** | Prévoir le poids d'un fichier d'échange à partir de la structure du maillage exporté, avant de le proposer au téléchargement. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | G-16 Livrable pesé |
| **Statut de production** | À produire |

**1. Compétence visée** — Prévoir le poids d'un fichier d'échange à partir de la structure du maillage exporté, avant de le proposer au téléchargement.

**1 bis. Contexte métier** — Le configurateur propose le téléchargement du modèle. Le fichier part souvent sur une connexion mobile : son poids se prévoit avant de le produire, pas après.

**2. Composants mobilisés** — Multiplication, Addition, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le maillage d'aperçu compte 24 310 faces quadrangulaires. Vous l'exportez dans un format binaire qui ne stocke que des triangles, avec un en-tête de 84 octets et 50 octets par facette. Donnez le poids du fichier, en octets.

**4. Données de départ fournies** — Le nombre de faces du maillage, leur nature, et la structure du format d'export.

**5. Résultat attendu** — 2 431 084 octets — soit 2,32 Mio.

**6. Zone CORRIGÉ — explication étape par étape**

1. Convertir les faces quadrangulaires en triangles.
2. Multiplier par le poids d'une facette.
3. Ajouter l'en-tête.
4. Convertir en mébioctets pour l'annoncer à l'utilisateur.

**6 bis. Erreur attendue** — Compter 50 octets par face du maillage : 1 215 584 octets, la moitié. Le format ne connaît que le TRIANGLE ; un maillage quadrangulaire est triangulé à l'export, et chaque quadrangle devient deux facettes. L'erreur ne se voit pas au calcul — elle se voit quand le fichier arrive deux fois plus lourd que promis à l'utilisateur.

**6 ter. Justification du jeu de données** — 24 310 quadrangles est l'ordre de grandeur d'un aperçu de meuble correctement maillé. Les deux réponses possibles sont dans un rapport de deux exactement, ce qui rend l'erreur immédiatement identifiable ; et l'en-tête de 84 octets est assez petit pour qu'on l'oublie sans que le résultat change d'ordre de grandeur — donc assez discret pour départager une réponse construite d'une réponse approchée.

**6 quater. Limite de la correction automatique** — Ce format ne porte ni matière, ni couleur, ni unité. Le poids n'est qu'un critère : la fiche invite à le comparer au 3DM et au glTF, qui portent davantage pour un poids voisin.

**7. Pièges fréquents**

- Compter une facette par face du maillage.
- Oublier l'en-tête.
- Confondre mébioctet et mégaoctet en annonçant le poids.

**8. Variantes et extensions**

- Refaire le calcul pour la variante texte du même format et mesurer le rapport.
- Réduire le maillage de moitié et juger ce que l'aperçu y perd.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le poids en octets est juste.

#### WB-07 — Le plan qui tient sur la feuille

| Rubrique | Valeur |
|---|---|
| **Lot** | WB — Interfaces, web et interopérabilité |
| **Thématique** | WB2 · Publication web |
| **Réf. référentiel** | REF-110 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | WB-02 |
| **Compétence visée** | Choisir l'échelle normalisée qui fait tenir une pièce sur un format donné, marges comprises. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-16 Livrable pesé |
| **Statut de production** | À produire |

**1. Compétence visée** — Choisir l'échelle normalisée qui fait tenir une pièce sur un format donné, marges comprises.

**1 bis. Contexte métier** — Le configurateur produit le plan en PDF, que le client imprime lui-même. Une échelle non normalisée rend le plan inutilisable : personne ne mesure au 1:6,1.

**2. Composants mobilisés** — Subtraction, Division, Larger Than, Cull Pattern, List Item, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La pièce mesure 2 380 mm de long et 1 640 mm de haut. Le plan sort sur une feuille de 420 × 297 mm, avec 15 mm de marge sur chaque bord. Les échelles disponibles sont 1:1, 1:2, 1:5, 1:10, 1:20, 1:50 et 1:100. Donnez le dénominateur de la plus grande échelle qui convient.

**4. Données de départ fournies** — Les dimensions de la pièce, le format de la feuille, la marge, et la liste des échelles normalisées.

**5. Résultat attendu** — 10 — l'échelle 1:10, qui donne 238 × 164 mm dans une zone utile de 390 × 267 mm.

**6. Zone CORRIGÉ — explication étape par étape**

1. Retrancher les marges pour obtenir la zone utile.
2. Calculer le rapport nécessaire sur chacune des deux dimensions.
3. Retenir le plus grand des deux.
4. Choisir dans la liste la première échelle dont le dénominateur l'atteint ou le dépasse.

**6 bis. Erreur attendue** — Calculer le rapport exact — 6,10 en longueur — et retenir 1:5 en arrondissant vers l'échelle voisine. Au 1:5, la pièce fait 476 mm et déborde de 86 mm : le PDF s'imprime quand même, tronqué. Une échelle se choisit DANS la liste, et toujours vers la plus petite.

**6 ter. Justification du jeu de données** — Le rapport nécessaire vaut 6,10 en longueur et 6,14 en hauteur : les deux dépassent 5 et aucun n'atteint 10, de sorte que ni la longueur seule ni la hauteur seule ne suffisent à trancher — il faut vérifier les deux. Une pièce plus étroite aurait laissé passer le réflexe de ne regarder que la plus grande dimension.

**6 quater. Limite de la correction automatique** — L'exercice choisit l'échelle, pas la mise en page : cartouche, cotation et nomenclature occupent aussi la feuille, et se traitent au format supérieur ou en plusieurs vues.

**7. Pièges fréquents**

- Ne vérifier que la longueur.
- Oublier les marges.
- Retenir une échelle non normalisée parce qu'elle « tient mieux ».

**8. Variantes et extensions**

- Passer au format inférieur et reprendre le choix.
- Réserver 60 mm de cartouche en bas de feuille et recommencer.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le dénominateur est juste.

### WB3 · Interopérabilité

*2 exercices — WB-03, WB-05*

#### WB-03 — Rhino sans Rhino

| Rubrique | Valeur |
|---|---|
| **Lot** | WB — Interfaces, web et interopérabilité |
| **Thématique** | WB3 · Interopérabilité |
| **Réf. référentiel** | REF-111, REF-112 |
| **Niveau** | Expert |
| **Durée cible** | 8 min |
| **Prérequis** | WB-02 |
| **Case Bloom (révisée)** | Comprendre × conceptuelle |
| **Nature** | Connaissance — question charnière, non notée |
| **Mode de validation** | — |
| **Gamification associée** | G-14 Question éclair |
| **Statut de production** | À produire |

**1. Compétence visée** — —

**1 bis. Contexte métier** — Une application métier doit exploiter la géométrie de Rhino sans que l'utilisateur ouvre Rhino.

**2. Question charnière** — cet item ne donne pas lieu à un exercice noté : la réponse s'obtiendrait en sachant, non en construisant.

Vous voulez faire tourner une définition Grasshopper depuis une application web, sans interface Rhino. Que cherchez-vous ?
a) Rhino.Inside, qui charge Rhino dans un autre logiciel hôte.
b) Rhino.Compute, qui expose le moteur de calcul comme un service appelable à distance. ← réponse
c) Un export en maillage, qui suffit toujours.
d) Les deux font la même chose.

Valeur diagnostique : (a) et (d) confondent deux réponses à deux besoins différents — Rhino.Inside fait cohabiter Rhino avec Revit ou AutoCAD sur le même poste ; Rhino.Compute met le moteur au bout d'un appel réseau. Se tromper de l'un pour l'autre fait partir sur une architecture entière qu'il faudra défaire.

**2 bis. Énoncé d'origine, conservé pour mémoire**

> **

**4. Données de départ fournies** — 

**5. Résultat attendu** — 

**6. Zone CORRIGÉ — explication étape par étape**


**7. Pièges fréquents**


**8. Variantes et extensions**


**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode —.

**10. Barème** — —

#### WB-05 — Dimensionner le calcul d'un configurateur

| Rubrique | Valeur |
|---|---|
| **Lot** | WB — Interfaces, web et interopérabilité |
| **Thématique** | WB3 · Interopérabilité |
| **Réf. référentiel** | REF-112 |
| **Niveau** | Expert |
| **Durée cible** | 30 min |
| **Prérequis** | WB-03 |
| **Compétence visée** | Dimensionner une capacité de calcul distante à partir de la fréquentation attendue, en raisonnant sur la pointe et non sur la moyenne. |
| **Case Bloom (révisée)** | Analyser × procédurale |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-22 Mise en charge |
| **Statut de production** | À produire |

**1. Compétence visée** — Dimensionner une capacité de calcul distante à partir de la fréquentation attendue, en raisonnant sur la pointe et non sur la moyenne.

**1 bis. Contexte métier** — Le configurateur en ligne délègue ses recalculs à un service distant, facturé à l'instance et à l'heure. Sous-dimensionné, il fait attendre ; sur-dimensionné, il coûte pour rien.

**2. Composants mobilisés** — Multiplication, Division, Round, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Le configurateur reçoit 12 000 visites par jour, dont 18 % se concentrent sur l'heure de pointe. Chaque visite déclenche 6 recalculs, et un recalcul occupe une instance pendant 1,2 seconde. Donnez le nombre d'instances nécessaires pour tenir la pointe sans faire attendre.

**4. Données de départ fournies** — La fréquentation quotidienne, la part de l'heure de pointe, le nombre de recalculs par visite et la durée d'un recalcul.

**5. Résultat attendu** — 5 instances — la pointe demande 15 552 secondes de calcul pour 3 600 secondes d'horloge.

**6. Zone CORRIGÉ — explication étape par étape**

1. Ramener la fréquentation à l'heure de pointe.
2. En déduire le nombre de recalculs à absorber dans l'heure.
3. Convertir en secondes de calcul demandées.
4. Rapporter aux 3 600 secondes que rend une instance en une heure.
5. Arrondir au SUPÉRIEUR : une instance ne se loue pas par quart.

**6 bis. Erreur attendue** — Lisser la charge sur les vingt-quatre heures : 12 000 × 6 × 1,2 ÷ 86 400 donne 1 instance. Le service tiendra la nuit et s'effondrera à l'heure où il y a du monde, c'est-à-dire au seul moment qui compte. Un dimensionnement à la moyenne est un dimensionnement pour personne.

**6 ter. Justification du jeu de données** — Une pointe à 18 % de la journée correspond à ce qu'observent les configurateurs grand public, dont le trafic se concentre en soirée. Le rapport entre le dimensionnement à la pointe (5) et à la moyenne (1) vaut cinq : l'erreur ne se rattrape pas par une marge de sécurité.

**6 quater. Limite de la correction automatique** — Le calcul suppose des recalculs indépendants et de durée constante. Une mise en cache des configurations les plus demandées change tout — et c'est le premier levier à actionner avant d'acheter des instances.

**7. Pièges fréquents**

- Dimensionner sur la moyenne quotidienne.
- Arrondir au plus proche : 4,32 devient 4, et la pointe déborde.
- Oublier les six recalculs par visite et compter une visite pour un calcul.

**8. Variantes et extensions**

- Ajouter un cache qui absorbe 40 % des recalculs et refaire le dimensionnement.
- Chiffrer le coût mensuel des deux hypothèses, et le comparer au coût d'une seconde d'attente pour un visiteur.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 1 point si le nombre d'instances est juste et arrondi au supérieur.

---

## Lot B — Algorithmes combinés

**Niveau** : Intermédiaire · **18 exercices** · **7 h 59 cumulées**

Un exercice par situation de conception réaliste, résolue en combinant plusieurs composants. Spécifié, pas encore produit.

| ID | Titre | Thématique | Niveau | Durée | Validation |
|---|---|---|---|---|---|
| B-01 | Escalier droit paramétrique | B1 · Architecture et construction | Intermédiaire | 25 min | NumericTolerance |
| B-02 | Garde-corps à barreaudage régulier | B1 · Architecture et construction | Intermédiaire | 20 min | NumericTolerance |
| B-03 | Façade à trame variable pilotée par un attracteur | B1 · Architecture et construction | Intermédiaire | 30 min | GeometryTolerance |
| B-04 | Pavage hexagonal sur surface | B1 · Architecture et construction | Intermédiaire | 28 min | GeometryTolerance |
| B-05 | Poutre treillis paramétrique | B1 · Architecture et construction | Intermédiaire | 25 min | NumericTolerance |
| B-06 | Caisson de meuble avec épaisseur et rainures | B2 · Design de mobilier | Intermédiaire | 30 min | GeometryTolerance |
| B-07 | Tiroir paramétrique avec jeux fonctionnels | B2 · Design de mobilier | Intermédiaire | 25 min | SingleValue |
| B-08 | Étagère modulaire à pas variable | B2 · Design de mobilier | Intermédiaire | 22 min | ExactOrderedList |
| B-09 | Griffe de sertissage paramétrique | B3 · Joaillerie | Intermédiaire | 28 min | GeometryTolerance |
| B-10 | Motif gravé développé sur un anneau | B3 · Joaillerie | Intermédiaire | 30 min | GeometryTolerance |
| B-11 | Chaîne de maillons le long d'une courbe | B3 · Joaillerie | Intermédiaire | 25 min | GeometryTolerance |
| B-12 | Nomenclature automatique et export CSV | B4 · Données, métrés et livrables | Intermédiaire | 25 min | ExactOrderedList |
| B-13 | Calepinage de plaques et calcul de chute | B4 · Données, métrés et livrables | Intermédiaire | 28 min | NumericTolerance |
| B-14 | Numérotation et étiquetage automatiques | B4 · Données, métrés et livrables | Intermédiaire | 22 min | ExactOrderedList |
| B-15 | Optimisation d'une découpe linéaire | B4 · Données, métrés et livrables | Intermédiaire | 30 min | SingleValue |
| B-16 | Lampe à lamelles de section variable | B5 · Design produit | Intermédiaire | 28 min | GeometryTolerance |
| B-17 | Coque à nervures depuis une surface libre | B5 · Design produit | Intermédiaire | 30 min | GeometryTolerance |
| B-18 | Filetage hélicoïdal paramétrique | B5 · Design produit | Intermédiaire | 28 min | NumericTolerance |

### B1 · Architecture et construction

*5 exercices — B-01, B-02, B-03, B-04, B-05*

#### B-01 — Escalier droit paramétrique

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B1 · Architecture et construction |
| **Réf. référentiel** | REF-067, REF-068, REF-047, REF-043 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-37, A-39, A-10 |
| **Mode de validation** | NumericTolerance — tolérance 1 mm sur la hauteur de marche |
| **Solution de référence** | 18 composants |
| **Gamification associée** | G-02 Barre de progression + G-26 Feedback visuel |
| **Statut de production** | À produire |

**1. Compétence visée** — Chaîner série, transformation et extrusion pour produire un ouvrage réglementé par un calcul.

**2. Composants mobilisés** — Series, Division, Round, Move, Extrude, Rectangle, Mass Addition

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Produis un escalier droit reliant deux niveaux distants de H = 2 850 mm. Le giron est fixé à 280 mm et la hauteur de marche doit rester comprise entre 165 et 180 mm. Détermine automatiquement le nombre de marches et vérifie la règle de Blondel (2h + g compris entre 600 et 650 mm).

**4. Données de départ fournies** — Deux Number Slider (H = 2850, giron = 280) et un Panel de contrôle.

**5. Résultat attendu** — L'escalier modélisé, le nombre de marches et la valeur de Blondel affichés.

**6. Zone CORRIGÉ — explication étape par étape**

1. Diviser H par 172,5 (hauteur moyenne visée) puis arrondir avec Round : on obtient le nombre de contremarches.
2. Recalculer la hauteur réelle h = H / nombre de contremarches.
3. Générer avec Series les positions verticales (0 à H, pas h) et horizontales (0 à n×giron, pas giron).
4. Construire le vecteur de déplacement de chaque marche avec Construct Point puis Vector 2Pt.
5. Poser le rectangle de marche (giron × largeur) et le déplacer par la liste de vecteurs.
6. Extruder chaque marche de l'épaisseur choisie.
7. Calculer 2h + g et le contrôler avec deux Larger Than et un Gate And : afficher CONFORME ou NON CONFORME.

**7. Pièges fréquents**

- Confondre nombre de marches et nombre de contremarches : il y a toujours une contremarche de plus.
- Arrondir la hauteur de marche au lieu de recalculer h à partir du nombre entier de contremarches.
- Oublier que la dernière marche est confondue avec le plancher haut.

**8. Variantes et extensions**

- Ajouter un limon latéral suivant la ligne de foulée.
- Passer en escalier à volée tournante avec un Polar Array partiel.
- Sortir une nomenclature des marches vers CSV.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 2 points pour la géométrie, 1 point pour le nombre de marches, 1 point pour le contrôle de Blondel.

#### B-02 — Garde-corps à barreaudage régulier

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B1 · Architecture et construction |
| **Réf. référentiel** | REF-064, REF-047, REF-043 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | A-35, A-12 |
| **Mode de validation** | NumericTolerance — tolérance 0,5 mm |
| **Solution de référence** | 14 composants |
| **Gamification associée** | G-07 Étoiles de performance |
| **Statut de production** | À produire |

**1. Compétence visée** — Répartir des éléments à pas maximal imposé, cas classique de calcul d'entraxe.

**2. Composants mobilisés** — Divide Curve, Length, Division, Round, Pipe, Line

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Sur la main courante fournie, place des barreaux verticaux de 16 mm de diamètre. L'espacement libre entre barreaux ne doit jamais dépasser 110 mm. Détermine le nombre de barreaux et affiche l'entraxe réel.

**4. Données de départ fournies** — Une courbe de main courante et une hauteur de garde-corps internalisées.

**5. Résultat attendu** — Les barreaux modélisés et un Panel affichant nombre et entraxe.

**6. Zone CORRIGÉ — explication étape par étape**

1. Mesurer la longueur de la main courante avec Length.
2. Calculer le pas maximal admissible : 110 + 16 = 126 mm.
3. Diviser la longueur par 126 puis arrondir à l'entier supérieur (Round avec le mode Ceiling ou Ceiling direct).
4. Recalculer l'entraxe réel = longueur / nombre d'intervalles.
5. Poser Divide Curve avec ce nombre d'intervalles.
6. Tracer les segments verticaux depuis chaque point puis les transformer en Pipe de rayon 8.
7. Afficher nombre et entraxe dans un Panel.

**7. Pièges fréquents**

- Confondre entraxe et espacement libre : l'écart libre vaut entraxe moins le diamètre.
- Arrondir à l'entier le plus proche au lieu de l'entier supérieur : l'espacement dépasse la limite.
- Oublier les barreaux d'extrémité.

**8. Variantes et extensions**

- Suivre une main courante inclinée en gardant les barreaux verticaux.
- Ajouter une lisse basse et calculer le linéaire total de matière.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 2 points pour le barreaudage, 1 point pour le respect strict des 110 mm.

#### B-03 — Façade à trame variable pilotée par un attracteur

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B1 · Architecture et construction |
| **Réf. référentiel** | REF-068, REF-053, REF-054 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | A-39, A-25 |
| **Mode de validation** | GeometryTolerance — tolérance 1 mm |
| **Solution de référence** | 16 composants |
| **Gamification associée** | G-25 Animation + G-13 Casino motifs assortis |
| **Statut de production** | À produire |

**1. Compétence visée** — Faire varier un paramètre géométrique en fonction d'une distance, méthode fondamentale du paramétrique.

**2. Composants mobilisés** — Rectangular Array, Distance, Remap Numbers, Bounds, Circle, Region Difference

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Sur la trame de façade 12 × 8, perce chaque panneau d'une ouverture circulaire dont le rayon varie de 50 mm (loin de l'attracteur) à 350 mm (au plus près). Le point attracteur est déplaçable dans Rhino.

**4. Données de départ fournies** — Une surface de façade et un point attracteur référencés.

**5. Résultat attendu** — 96 panneaux percés d'ouvertures de rayon variable.

**6. Zone CORRIGÉ — explication étape par étape**

1. Diviser la façade avec Divide Surface ou Rectangular Array pour obtenir les 96 centres de panneaux.
2. Mesurer la distance de chaque centre à l'attracteur avec Distance.
3. Poser Bounds sur ces distances pour obtenir le domaine réel.
4. Poser Remap Numbers : source = domaine des distances, cible = domaine 350 à 50 (inversé).
5. Poser Circle avec les centres et les rayons remappés.
6. Percer les panneaux avec Region Difference (2D) ou Solid Difference (3D).
7. Vérifier que le rayon reste inférieur à la demi-largeur du panneau.

**7. Pièges fréquents**

- Domaine cible non inversé : les grandes ouvertures se retrouvent au plus loin.
- Rayon supérieur à la demi-largeur : la découpe déborde sur les panneaux voisins.
- Attracteur non internalisé : la définition casse à l'ouverture du fichier.

**8. Variantes et extensions**

- Piloter la rotation des panneaux plutôt que le rayon.
- Utiliser une courbe attractrice au lieu d'un point.
- Contraindre le taux de vide global à une valeur cible.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 2 points pour la variation, 1 point pour la borne de sécurité du rayon.

#### B-04 — Pavage hexagonal sur surface

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B1 · Architecture et construction |
| **Réf. référentiel** | REF-068, REF-069, REF-049 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 28 min |
| **Prérequis** | B-03, A-20 |
| **Mode de validation** | GeometryTolerance — tolérance 2 mm |
| **Solution de référence** | 20 composants |
| **Gamification associée** | G-22 Boss de fin de chapitre |
| **Statut de production** | À produire |

**1. Compétence visée** — Projeter une trame plane sur une surface libre en maîtrisant la structure de données.

**2. Composants mobilisés** — Hexagonal (Lunchbox ou natif Polygon), Surface Closest Point, Evaluate Surface, Graft

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Applique un pavage hexagonal de 400 mm de côté sur la surface libre fournie, puis extrude chaque hexagone de 60 mm suivant la normale locale de la surface.

**4. Données de départ fournies** — Une surface libre internalisée.

**5. Résultat attendu** — Le pavage projeté et extrudé selon les normales.

**6. Zone CORRIGÉ — explication étape par étape**

1. Construire la trame hexagonale plane par deux Rectangular Array décalés d'un demi-pas.
2. Poser Polygon avec 6 côtés sur chaque centre.
3. Projeter les centres sur la surface avec Surface Closest Point.
4. Récupérer les normales avec Evaluate Surface (sortie N).
5. Construire un plan local par centre avec Plane Normal.
6. Orienter les hexagones sur ces plans avec Orient.
7. Extruder chaque hexagone suivant sa normale : Graft nécessaire pour associer un vecteur par hexagone.

**7. Pièges fréquents**

- Oublier le Graft : tous les hexagones reçoivent le même vecteur.
- Trame plane plus petite que la surface : des zones restent non pavées.
- Surface très courbe : les hexagones se chevauchent.

**8. Variantes et extensions**

- Faire varier la hauteur d'extrusion selon la courbure locale.
- Découper les hexagones dépassant du contour de la surface.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 2 points pour le pavage, 2 points pour l'orientation selon les normales.

#### B-05 — Poutre treillis paramétrique

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B1 · Architecture et construction |
| **Réf. référentiel** | REF-046, REF-063, REF-079 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-16, A-47 |
| **Mode de validation** | NumericTolerance — tolérance 0,5 % |
| **Solution de référence** | 22 composants |
| **Gamification associée** | G-21 Golf de composants |
| **Statut de production** | À produire |

**1. Compétence visée** — Construire une structure par décalage de listes et produire directement son métré.

**2. Composants mobilisés** — Series, Shift List, Line, Pipe, Length, Mass Addition, Weave

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Produis une poutre treillis Warren de 12 000 mm de portée et 900 mm de hauteur, avec 8 panneaux. Affiche le linéaire total de tube nécessaire, membrures et diagonales séparées.

**4. Données de départ fournies** — Trois sliders : portée, hauteur, nombre de panneaux.

**5. Résultat attendu** — Le treillis modélisé et deux valeurs de linéaire.

**6. Zone CORRIGÉ — explication étape par étape**

1. Générer les abscisses des nœuds avec Range sur la portée.
2. Construire la membrure basse (Z = 0) et la membrure haute (Z = 900) par Construct Point.
3. Relier chaque nœud au suivant avec Shift List + Line pour les deux membrures.
4. Pour les diagonales, alterner nœud bas i vers nœud haut i+1 puis nœud haut i+1 vers nœud bas i+2 : utiliser Cull Pattern ou Weave.
5. Transformer les lignes en Pipe avec deux diamètres distincts.
6. Mesurer les longueurs avec Length puis Mass Addition sur chaque famille.
7. Afficher les deux linéaires dans un Panel.

**7. Pièges fréquents**

- Shift List sans Wrap : la dernière barre manque ou la première est en trop.
- Alternance des diagonales mal construite : on obtient un treillis Pratt et non Warren.
- Compter deux fois les nœuds partagés dans le métré.

**8. Variantes et extensions**

- Passer d'un treillis Warren à un treillis Pratt par un simple changement de motif.
- Exporter la nomenclature des barres vers Excel.
- Faire varier la hauteur pour obtenir une poutre à inertie variable.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 2 points pour la géométrie, 2 points pour les deux linéaires.

### B2 · Design de mobilier

*3 exercices — B-06, B-07, B-08*

#### B-06 — Caisson de meuble avec épaisseur et rainures

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B2 · Design de mobilier |
| **Réf. référentiel** | REF-070, REF-071, REF-068 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | A-43, A-44 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 26 composants |
| **Gamification associée** | G-06 Niveaux et déblocage |
| **Statut de production** | À produire |

**1. Compétence visée** — Modéliser un assemblage menuisé où toutes les cotes dérivent de trois paramètres.

**2. Composants mobilisés** — Box, Solid Difference, Move, Deconstruct Box, Construct Domain

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Modélise un caisson de largeur L, hauteur H et profondeur P, en panneaux de 19 mm. Les joues reçoivent une rainure de 6 mm de profondeur pour le fond de 8 mm. Le dessus et le dessous s'insèrent entre les joues.

**4. Données de départ fournies** — Trois sliders L, H, P et un slider d'épaisseur.

**5. Résultat attendu** — Le caisson en 5 panneaux distincts, rainures comprises.

**6. Zone CORRIGÉ — explication étape par étape**

1. Construire le volume englobant à partir de L, H, P.
2. Déduire la géométrie de chaque joue : épaisseur × H × P, positionnée à gauche et à droite.
3. Déduire dessus et dessous : (L − 2 × 19) × 19 × P, positionnés entre les joues.
4. Construire le volume de rainure : boîte de 8 mm d'épaisseur, profondeur 6 mm, courant sur toute la hauteur.
5. Soustraire cette boîte des quatre panneaux avec Solid Difference.
6. Poser le fond de 8 mm dans la rainure, avec un jeu de 0,2 mm.
7. Contrôler visuellement l'assemblage en vue éclatée par un Move paramétrable.

**7. Pièges fréquents**

- Oublier de retirer deux épaisseurs à la longueur du dessus et du dessous.
- Rainure positionnée au nu arrière sans tenir compte de sa profondeur.
- Jeu de montage nul : les pièces s'interpénètrent lors du contrôle de collision.

**8. Variantes et extensions**

- Passer d'un assemblage rainuré à un assemblage par tourillons.
- Ajouter une nomenclature de débit avec chants.
- Générer la vue éclatée animée.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 3 points pour l'assemblage, 1 point pour la rainure correcte.

#### B-07 — Tiroir paramétrique avec jeux fonctionnels

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B2 · Design de mobilier |
| **Réf. référentiel** | REF-070, REF-072 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | B-06, A-46 |
| **Mode de validation** | SingleValue — tolérance — |
| **Solution de référence** | 20 composants |
| **Gamification associée** | G-04 Système de vies |
| **Statut de production** | À produire |

**1. Compétence visée** — Intégrer des jeux de fonctionnement et vérifier l'absence de collision.

**2. Composants mobilisés** — Box, Solid Difference, Collision Many|Many, Boolean Toggle, Move

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Insère dans le caisson un tiroir sur coulisses de 13 mm de jeu latéral par côté et 2 mm en hauteur. Le tiroir doit pouvoir coulisser de toute sa profondeur sans collision : prouve-le.

**4. Données de départ fournies** — Le caisson de l'exercice B-06.

**5. Résultat attendu** — Le tiroir modélisé et un Panel affichant l'absence de collision en position ouverte.

**6. Zone CORRIGÉ — explication étape par étape**

1. Calculer la largeur intérieure disponible : L − 2 × 19.
2. Déduire la largeur du tiroir : intérieur − 2 × 13.
3. Construire le caisson de tiroir en panneaux de 15 mm.
4. Poser un slider de course de 0 à P pour piloter l'ouverture.
5. Déplacer le tiroir de cette course avec Move.
6. Poser Collision Many|Many entre les panneaux du tiroir et ceux du caisson.
7. Afficher dans un Panel le nombre de collisions détectées : il doit rester à zéro sur toute la course.

**7. Pièges fréquents**

- Appliquer le jeu une seule fois au lieu de deux fois (un par côté).
- Tester la collision uniquement en position fermée.
- Tolérance de collision de Grasshopper trop lâche : un contact tangent passe inaperçu.

**8. Variantes et extensions**

- Ajouter une façade en applique avec débord.
- Générer plusieurs tiroirs de hauteurs différentes réparties automatiquement.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 2 points pour le tiroir, 2 points pour la preuve d'absence de collision.

#### B-08 — Étagère modulaire à pas variable

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B2 · Design de mobilier |
| **Réf. référentiel** | REF-043, REF-044, REF-047 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 22 min |
| **Prérequis** | A-13, A-10 |
| **Mode de validation** | ExactOrderedList — tolérance 1 mm |
| **Solution de référence** | 16 composants |
| **Gamification associée** | G-08 Combo / série |
| **Statut de production** | À produire |

**1. Compétence visée** — Répartir des tablettes selon une progression non uniforme pilotée par une courbe.

**2. Composants mobilisés** — Graph Mapper, Range, Remap Numbers, Move, Box, Sort List

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Répartis 6 tablettes sur une hauteur de 2 000 mm de sorte que les entre-deux augmentent progressivement du bas vers le haut, la plus petite hauteur libre valant au moins 220 mm.

**4. Données de départ fournies** — Un slider de hauteur totale et un slider de nombre de tablettes.

**5. Résultat attendu** — Les tablettes réparties et un Panel listant les hauteurs libres.

**6. Zone CORRIGÉ — explication étape par étape**

1. Générer une série normalisée de 0 à 1 avec Range.
2. Passer cette série dans un Graph Mapper réglé en courbe puissance.
3. Remapper le résultat sur le domaine 0 à 2000 : les positions se resserrent en bas.
4. Poser les tablettes à ces altitudes avec Move.
5. Calculer les entre-deux par Shift List et soustraction, puis retirer l'épaisseur de tablette.
6. Contrôler la valeur minimale avec Bounds et un Larger Than.
7. Afficher les hauteurs libres dans un Panel.

**7. Pièges fréquents**

- Oublier de retirer l'épaisseur des tablettes pour obtenir la hauteur libre.
- Graph Mapper non internalisé : la courbe se réinitialise à l'ouverture du fichier.
- Contrainte de 220 mm vérifiée sur les entraxes et non sur les vides.

**8. Variantes et extensions**

- Inverser la progression du haut vers le bas.
- Imposer un nombre entier de modules standards.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode ExactOrderedList.

**10. Barème** — 2 points pour la répartition, 1 point pour la contrainte de 220 mm.

### B3 · Joaillerie

*3 exercices — B-09, B-10, B-11*

#### B-09 — Griffe de sertissage paramétrique

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B3 · Joaillerie |
| **Réf. référentiel** | REF-068, REF-069, REF-067 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 28 min |
| **Prérequis** | A-39, A-42 |
| **Mode de validation** | GeometryTolerance — tolérance 0,02 mm |
| **Solution de référence** | 22 composants |
| **Gamification associée** | G-10 Coffre à butin |
| **Statut de production** | À produire |

**1. Compétence visée** — Construire un détail technique répétitif autour d'un axe, avec contrôle d'inclinaison.

**2. Composants mobilisés** — Polar Array, Pipe, Rotate Axis, Circle, Sweep 1, Interpolate

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Modélise 4 griffes réparties à 90° autour d'une pierre ronde de 5 mm de diamètre. Chaque griffe est un fil de 0,9 mm de diamètre, incliné de 12° vers l'intérieur, avec une tête arrondie recouvrant la ceinture de la pierre.

**4. Données de départ fournies** — Un slider de diamètre de pierre et une sphère de gabarit.

**5. Résultat attendu** — 4 griffes correctement réparties et inclinées.

**6. Zone CORRIGÉ — explication étape par étape**

1. Construire le cercle de ceinture de la pierre.
2. Tracer le profil d'une griffe par Interpolate sur 3 ou 4 points de contrôle.
3. Incliner ce profil de 12° avec Rotate Axis autour d'un axe tangent au cercle.
4. Transformer le profil en solide avec Pipe de rayon 0,45.
5. Répartir par Polar Array avec Count = 4 et Angle = 2π.
6. Vérifier que la tête de griffe recouvre bien la ceinture par une intersection Brep|Brep.
7. Contrôler l'absence de collision entre griffes voisines.

**7. Pièges fréquents**

- Angle saisi en degrés au lieu de radians.
- Axe de rotation mal choisi : les griffes s'inclinent hors du plan attendu.
- Pipe de rayon égal au diamètre : la griffe fait le double de la cote demandée.

**8. Variantes et extensions**

- Passer à 6 griffes et vérifier la non-collision.
- Faire varier l'inclinaison en fonction du diamètre de pierre.
- Ajouter un panier sous la pierre.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 2 points pour la géométrie, 1 point pour l'inclinaison, 1 point pour le recouvrement.

#### B-10 — Motif gravé développé sur un anneau

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B3 · Joaillerie |
| **Réf. référentiel** | REF-115, REF-069, REF-049 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | B-04, A-42 |
| **Mode de validation** | GeometryTolerance — tolérance 0,05 mm |
| **Solution de référence** | 24 composants |
| **Gamification associée** | G-09 Récompense cachée |
| **Statut de production** | À produire |

**1. Compétence visée** — Concevoir un motif à plat puis l'enrouler sur une surface de révolution.

**2. Composants mobilisés** — Rectangle, Divide Domain2, Surface Morph, Flow along Surface (Morph), Revolution

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Dessine à plat un motif géométrique répétitif de 12 modules, puis applique-le sur la face extérieure d'un anneau de taille 54 et de 4 mm de large. Le motif doit boucler sans rupture.

**4. Données de départ fournies** — Un anneau de révolution internalisé et un module de motif plan.

**5. Résultat attendu** — Le motif appliqué sur l'anneau, raccord continu.

**6. Zone CORRIGÉ — explication étape par étape**

1. Calculer la circonférence de l'anneau : diamètre intérieur = 54/π, puis circonférence extérieure.
2. Diviser cette circonférence par 12 pour obtenir la largeur exacte du module.
3. Construire le motif dans un rectangle de référence exactement de cette largeur.
4. Répliquer le module 12 fois avec Rectangular Array.
5. Construire la surface développée de référence (rectangle circonférence × largeur).
6. Appliquer Surface Morph ou Sporph entre la surface plane et la surface de l'anneau.
7. Vérifier la continuité au raccord en superposant le premier et le dernier module.

**7. Pièges fréquents**

- Largeur de module arrondie : le raccord présente un décalage cumulé.
- Confondre diamètre intérieur et diamètre extérieur pour le calcul de circonférence.
- Surface de référence et surface cible de proportions différentes : le motif se déforme.

**8. Variantes et extensions**

- Rendre le nombre de modules paramétrable et recalculer automatiquement la largeur.
- Graver le motif en creux par Solid Difference.
- Adapter au cas d'un anneau de section variable.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 2 points pour le motif, 2 points pour la continuité du raccord.

#### B-11 — Chaîne de maillons le long d'une courbe

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B3 · Joaillerie |
| **Réf. référentiel** | REF-064, REF-067, REF-046 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-35, A-38 |
| **Mode de validation** | GeometryTolerance — tolérance 0,05 mm |
| **Solution de référence** | 20 composants |
| **Gamification associée** | G-12 Memory |
| **Statut de production** | À produire |

**1. Compétence visée** — Répartir et orienter alternativement des éléments le long d'un parcours.

**2. Composants mobilisés** — Divide Length, Perp Frames, Orient, Cull Pattern, Rotate, Torus

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Répartis des maillons ovales de 4 mm le long de la courbe fournie, chaque maillon tourné de 90° par rapport au précédent, sans jeu ni recouvrement excessif.

**4. Données de départ fournies** — Une courbe de collier internalisée.

**5. Résultat attendu** — La chaîne complète avec alternance des orientations.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Divide Length avec un pas égal au pas de maillon (longueur moins recouvrement).
2. Poser Perp Frames pour obtenir un plan par position.
3. Modéliser un maillon de référence dans le plan XY.
4. Orienter le maillon sur chaque plan avec Orient.
5. Séparer les positions paires et impaires avec Cull Pattern (motif True, False).
6. Appliquer une rotation de 90° (π/2) aux maillons impairs avec Rotate Axis.
7. Recombiner les deux familles avec Weave pour retrouver l'ordre initial.

**7. Pièges fréquents**

- Pas de division égal à la longueur du maillon : les maillons ne se touchent pas.
- Recombiner avec Merge au lieu de Weave : l'ordre est perdu.
- Courbe trop courbée : les maillons se coincent.

**8. Variantes et extensions**

- Faire varier la taille des maillons selon la position sur la courbe.
- Ajouter un fermoir aux extrémités.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 2 points pour la répartition, 2 points pour l'alternance.

### B4 · Données, métrés et livrables

*4 exercices — B-12, B-13, B-14, B-15*

#### B-12 — Nomenclature automatique et export CSV

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B4 · Données, métrés et livrables |
| **Réf. référentiel** | REF-082, REF-083, REF-085, REF-087 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 25 min |
| **Prérequis** | A-27, A-47 |
| **Mode de validation** | ExactOrderedList — tolérance 0,5 % |
| **Solution de référence** | 24 composants |
| **Gamification associée** | G-01 Score visible |
| **Statut de production** | À produire |

**1. Compétence visée** — Transformer un modèle en tableau de données exploitable.

**2. Composants mobilisés** — Deconstruct Brep, Volume, Area, Sort List, Concatenate, Format, Text Join, Write File

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> À partir du modèle fourni, produis une nomenclature triée par volume décroissant comportant, pour chaque pièce, le repère, le volume en dm³, la surface en dm² et la masse en kg pour une densité de 700 kg/m³. Exporte le tableau au format CSV.

**4. Données de départ fournies** — Un assemblage de 14 solides internalisés.

**5. Résultat attendu** — Un fichier CSV de 14 lignes plus l'en-tête, trié par volume décroissant.

**6. Zone CORRIGÉ — explication étape par étape**

1. Mesurer Volume et Area de chaque solide.
2. Convertir les unités : mm³ vers dm³ (division par 1 000 000), mm² vers dm² (division par 10 000).
3. Calculer la masse : volume en m³ multiplié par 700.
4. Générer les repères avec Series et Format (masque PCE-{0:000}).
5. Trier l'ensemble par volume décroissant avec Sort List puis Reverse List, en propageant toutes les listes.
6. Formater chaque valeur à deux décimales avec Format.
7. Assembler chaque ligne avec Concatenate et le séparateur point-virgule.
8. Ajouter la ligne d'en-tête avec Merge, puis écrire le fichier avec Write File.

**7. Pièges fréquents**

- Trier une seule liste et pas les autres : les données se désynchronisent.
- Séparateur décimal virgule et séparateur de colonne virgule : le CSV devient illisible.
- Oublier l'en-tête ou le placer après le tri.

**8. Variantes et extensions**

- Ajouter une colonne matériau lue depuis les calques Rhino.
- Grouper les pièces identiques et compter les occurrences.
- Exporter vers Excel plutôt que CSV.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode ExactOrderedList.

**10. Barème** — 2 points pour les calculs, 1 point pour le tri, 1 point pour le format du fichier.

#### B-13 — Calepinage de plaques et calcul de chute

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B4 · Données, métrés et livrables |
| **Réf. référentiel** | REF-113, REF-082, REF-045 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 28 min |
| **Prérequis** | B-12, A-15 |
| **Mode de validation** | NumericTolerance — tolérance 1 % |
| **Solution de référence** | 20 composants |
| **Gamification associée** | G-23 Duel et classement |
| **Statut de production** | À produire |

**1. Compétence visée** — Optimiser un débit et quantifier la perte matière.

**2. Composants mobilisés** — Rectangular Array, Region Difference, Area, Mass Addition, Division, Dispatch

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Les 22 pièces rectangulaires fournies doivent être débitées dans des plaques de 2 800 × 2 070 mm. Calcule le nombre de plaques nécessaires et le taux de chute en pourcentage.

**4. Données de départ fournies** — Une liste de 22 rectangles et les dimensions de plaque.

**5. Résultat attendu** — Un Panel affichant le nombre de plaques et le taux de chute.

**6. Zone CORRIGÉ — explication étape par étape**

1. Mesurer l'aire de chaque pièce avec Area puis sommer avec Mass Addition.
2. Calculer l'aire d'une plaque : 2800 × 2070.
3. Diviser l'aire totale des pièces par l'aire d'une plaque et arrondir à l'entier supérieur : nombre théorique minimal.
4. Placer les pièces par un calepinage simple en bandes (tri par hauteur décroissante puis remplissage ligne par ligne).
5. Compter le nombre réel de plaques utilisées.
6. Calculer le taux de chute : 1 − (aire des pièces / aire des plaques utilisées).
7. Afficher les deux valeurs et signaler l'écart avec le minimum théorique.

**7. Pièges fréquents**

- Confondre le minimum théorique et le nombre réellement atteignable.
- Oublier le trait de scie entre les pièces.
- Ne pas gérer les pièces plus grandes que la plaque.

**8. Variantes et extensions**

- Ajouter une contrainte de sens de fil du bois.
- Comparer le résultat avec l'imbrication OpenNest.
- Chiffrer le coût matière à partir du prix de plaque.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 2 points pour le calepinage, 1 point pour le nombre de plaques, 1 point pour le taux de chute.

#### B-14 — Numérotation et étiquetage automatiques

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B4 · Données, métrés et livrables |
| **Réf. référentiel** | REF-066, REF-081, REF-057 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 22 min |
| **Prérequis** | A-49, A-27 |
| **Mode de validation** | ExactOrderedList — tolérance 1 mm |
| **Solution de référence** | 18 composants |
| **Gamification associée** | G-11 Mots croisés de composants |
| **Statut de production** | À produire |

**1. Compétence visée** — Produire des repères lisibles, cohérents et positionnés dans le modèle.

**2. Composants mobilisés** — Sort List, Series, Format, Text Tag 3D, Volume, Point, Plane

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Numérote les 14 pièces de l'assemblage de gauche à droite puis de bas en haut, au format R-A01 à R-A14, et place l'étiquette au centre de gravité de chaque pièce, orientée face à la vue de face.

**4. Données de départ fournies** — Un assemblage de 14 solides internalisés.

**5. Résultat attendu** — 14 étiquettes correctement numérotées et positionnées.

**6. Zone CORRIGÉ — explication étape par étape**

1. Récupérer les centroïdes avec Volume.
2. Décomposer les points avec Deconstruct pour obtenir X et Z.
3. Construire une clé de tri combinée : Z multiplié par un grand facteur plus X.
4. Trier les pièces et les centroïdes avec Sort List sur cette clé.
5. Générer les numéros avec Series et Format (masque R-A{0:00}).
6. Poser Text Tag 3D avec un plan orienté XZ pour la lisibilité en vue de face.
7. Contrôler l'ordre obtenu dans un Panel.

**7. Pièges fréquents**

- Clé de tri mal pondérée : le tri secondaire prend le pas sur le tri principal.
- Format sans masque : les numéros s'affichent sans zéro de tête.
- Étiquettes orientées dans le plan XY donc illisibles en élévation.

**8. Variantes et extensions**

- Ajouter le repère dans un attribut Rhino via Elefront.
- Générer une planche de repérage cotée.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode ExactOrderedList.

**10. Barème** — 2 points pour l'ordre, 1 point pour le format, 1 point pour le placement.

#### B-15 — Optimisation d'une découpe linéaire

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B4 · Données, métrés et livrables |
| **Réf. référentiel** | REF-044, REF-045, REF-082 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | B-13 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 18 composants |
| **Gamification associée** | G-23 Duel et classement + G-03 Compte à rebours |
| **Statut de production** | À produire |

**1. Compétence visée** — Mettre en œuvre un algorithme de placement glouton et en mesurer la performance.

**2. Composants mobilisés** — Sort List, Reverse List, Anemone ou Python, Mass Addition, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Débite 30 pièces de longueurs variées dans des barres de 6 000 mm. Applique la règle du plus grand d'abord et affiche le nombre de barres consommées ainsi que la chute totale.

**4. Données de départ fournies** — Une liste de 30 longueurs internalisée.

**5. Résultat attendu** — Un Panel affichant le nombre de barres et la chute totale en mm.

**6. Zone CORRIGÉ — explication étape par étape**

1. Trier les longueurs par ordre décroissant avec Sort List puis Reverse List.
2. Mettre en place une boucle Anemone : à chaque itération, tenter de placer la pièce suivante dans une barre ouverte.
3. Si aucune barre ne peut l'accueillir, ouvrir une nouvelle barre.
4. Accumuler l'état des barres dans la boucle avec un paramètre de rebouclage.
5. En sortie de boucle, compter les barres et sommer les chutes.
6. Afficher les deux valeurs.
7. Comparer avec le minimum théorique (somme des longueurs divisée par 6000, arrondi supérieur).

**7. Pièges fréquents**

- Boucle sans condition d'arrêt : Grasshopper se fige.
- Oublier le trait de scie dans le cumul.
- Tri croissant au lieu de décroissant : le résultat se dégrade nettement.

**8. Variantes et extensions**

- Comparer avec une stratégie du meilleur ajustement.
- Écrire l'algorithme en composant Python plutôt qu'en boucle Anemone.
- Autoriser plusieurs longueurs de barre commerciale.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode SingleValue.

**10. Barème** — 2 points pour l'algorithme, 1 point pour le nombre de barres, 1 point pour la chute.

### B5 · Design produit

*3 exercices — B-16, B-17, B-18*

#### B-16 — Lampe à lamelles de section variable

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B5 · Design produit |
| **Réf. référentiel** | REF-064, REF-069, REF-067 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 28 min |
| **Prérequis** | A-35, A-41 |
| **Mode de validation** | GeometryTolerance — tolérance 0,2 mm |
| **Solution de référence** | 22 composants |
| **Gamification associée** | G-28 Avatar et personnalisation |
| **Statut de production** | À produire |

**1. Compétence visée** — Faire varier une section le long d'un parcours par interpolation contrôlée.

**2. Composants mobilisés** — Divide Curve, Perp Frames, Circle, Graph Mapper, Loft, Polar Array

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Produis un abat-jour composé de 24 lamelles réparties autour d'un axe. Chaque lamelle suit un profil dont la largeur varie de 15 mm aux extrémités à 45 mm au milieu, selon une courbe douce.

**4. Données de départ fournies** — Une courbe génératrice internalisée et un slider de nombre de lamelles.

**5. Résultat attendu** — 24 lamelles réparties, largeur variable respectée.

**6. Zone CORRIGÉ — explication étape par étape**

1. Diviser la courbe génératrice en 30 stations avec Divide Curve.
2. Générer une série normalisée de 0 à 1 sur ces stations.
3. Passer cette série dans un Graph Mapper en courbe de Bézier symétrique.
4. Remapper la sortie sur le domaine 15 à 45 : on obtient la largeur à chaque station.
5. Construire un rectangle de cette largeur dans le plan perpendiculaire de chaque station.
6. Lofter ces rectangles pour obtenir la lamelle.
7. Répartir par Polar Array avec Count = 24.

**7. Pièges fréquents**

- Graph Mapper non symétrique : les deux extrémités n'ont pas la même largeur.
- Rectangles non alignés : le Loft se vrille.
- Lamelles voisines en interférence près de l'axe.

**8. Variantes et extensions**

- Faire varier aussi l'épaisseur.
- Contrôler l'ouverture lumineuse résultante.
- Adapter le nombre de lamelles à un diamètre imposé.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 2 points pour la variation, 2 points pour la répartition.

#### B-17 — Coque à nervures depuis une surface libre

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B5 · Design produit |
| **Réf. référentiel** | REF-069, REF-101, REF-049 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | A-45, B-04 |
| **Mode de validation** | GeometryTolerance — tolérance 0,5 mm |
| **Solution de référence** | 24 composants |
| **Gamification associée** | G-22 Boss de fin de chapitre |
| **Statut de production** | À produire |

**1. Compétence visée** — Extraire des sections structurelles d'une forme libre et préparer leur fabrication.

**2. Composants mobilisés** — Brep | Plane, Offset Curve, Extrude, Series, Rectangle, Boundary Surfaces

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Sur la coque libre fournie, extrais 9 nervures transversales espacées régulièrement, donne-leur 12 mm d'épaisseur et 60 mm de hauteur vers l'intérieur, puis prépare leur mise à plat.

**4. Données de départ fournies** — Une surface de coque internalisée.

**5. Résultat attendu** — 9 nervures modélisées et leur développé à plat.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Bounding Box puis Deconstruct Box pour connaître l'étendue en X.
2. Générer 9 plans de coupe régulièrement espacés avec Range et YZ Plane.
3. Poser Brep | Plane pour obtenir les 9 courbes de section.
4. Décaler chaque section vers l'intérieur de 60 mm avec Offset Curve.
5. Construire la surface de nervure entre la section et son décalé avec Boundary Surfaces ou Loft.
6. Extruder de 12 mm pour donner l'épaisseur.
7. Aligner chaque nervure à plat par Orient vers le plan XY pour la mise à plat.

**7. Pièges fréquents**

- Offset Curve du mauvais côté : la nervure sort de la coque.
- Courbes de section multiples sur une coque non convexe : les traiter en arbre.
- Oublier de conserver le repérage des nervures après mise à plat.

**8. Variantes et extensions**

- Ajouter des encoches d'assemblage aux croisements avec des longerons.
- Exporter les développés en DXF.
- Faire varier l'espacement selon la courbure.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 2 points pour les nervures, 2 points pour la mise à plat.

#### B-18 — Filetage hélicoïdal paramétrique

| Rubrique | Valeur |
|---|---|
| **Lot** | B — Algorithmes combinés |
| **Thématique** | B5 · Design produit |
| **Réf. référentiel** | REF-069, REF-103 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 28 min |
| **Prérequis** | A-42 |
| **Mode de validation** | NumericTolerance — tolérance 0,05 mm |
| **Solution de référence** | 22 composants |
| **Gamification associée** | G-32 Indices payants |
| **Statut de production** | À produire |

**1. Compétence visée** — Construire une hélice et balayer un profil normalisé le long de celle-ci.

**2. Composants mobilisés** — Helix (Curve > Primitive), Sweep 1, Perp Frames, Polygon, Solid Difference, Cylinder

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Modélise une vis M10 au pas de 1,5 mm sur 30 mm de longueur filetée, profil triangulaire à 60°, et vérifie que le diamètre à fond de filet correspond bien à la valeur normalisée de 8,376 mm.

**4. Données de départ fournies** — Trois sliders : diamètre nominal, pas, longueur filetée.

**5. Résultat attendu** — La vis modélisée et un Panel affichant le diamètre à fond de filet mesuré.

**6. Zone CORRIGÉ — explication étape par étape**

1. Construire l'hélice avec le composant Helix : rayon 5, pas 1,5, nombre de tours = 30 / 1,5 = 20.
2. Construire le profil triangulaire du filet ISO dans un plan perpendiculaire au départ de l'hélice.
3. Poser Sweep 1 avec l'hélice comme rail et le profil comme section.
4. Construire le cylindre nominal de diamètre 10.
5. Soustraire le balayage du cylindre avec Solid Difference.
6. Couper le résultat par un plan passant par l'axe et mesurer le diamètre à fond de filet.
7. Comparer à 8,376 mm avec Similarity et afficher CONFORME ou NON CONFORME.

**7. Pièges fréquents**

- Nombre de tours calculé à partir de la longueur totale et non de la longueur filetée.
- Profil non perpendiculaire à l'hélice : le filet se vrille.
- Confondre le pas et le pas hélicoïdal sur un filetage multiple.

**8. Variantes et extensions**

- Modéliser l'écrou correspondant et vérifier le jeu.
- Paramétrer pour toute la série métrique M3 à M20.
- Ajouter un chanfrein d'entrée.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 2 points pour le filetage, 2 points pour la vérification dimensionnelle.

---

## Lot C — Projets appliqués

**Niveau** : Expérimenté · **12 exercices** · **16 h 35 cumulées**

Un projet complet par domaine métier — architecture, mobilier, joaillerie, fabrication. Spécifié, pas encore produit.

| ID | Titre | Thématique | Niveau | Durée | Validation |
|---|---|---|---|---|---|
| C-01 | Enveloppe à brise-soleil orientés selon l'ensoleillement | C1 · Architecture | Expérimenté | 90 min | NumericTolerance |
| C-02 | Résille structurelle sur plan libre | C1 · Architecture | Expérimenté | 90 min | NumericTolerance |
| C-03 | Gradins avec contrôle de visibilité | C1 · Architecture | Expérimenté | 80 min | NumericTolerance |
| C-04 | Métré et chiffrage complet d'un module | C1 · Architecture | Expérimenté | 75 min | NumericTolerance |
| C-05 | Bibliothèque paramétrique avec débit et mise à plat CNC | C2 · Design de mobilier | Expérimenté | 90 min | GeometryTolerance |
| C-06 | Chaise à assise en lamelles courbes | C2 · Design de mobilier | Expérimenté | 85 min | NumericTolerance |
| C-07 | Table de nuit configurable | C2 · Design de mobilier | Expérimenté | 80 min | GeometryTolerance |
| C-08 | Bague solitaire complète | C3 · Joaillerie | Expérimenté | 85 min | NumericTolerance |
| C-09 | Pavage de pierres sur surface libre | C3 · Joaillerie | Expérimenté | 85 min | NumericTolerance |
| C-10 | Motif gravé génératif sur bijou | C3 · Joaillerie | Expérimenté | 80 min | NumericTolerance |
| C-11 | Déroulé de tôle pliée avec compensation | C4 · Fabrication | Expérimenté | 80 min | NumericTolerance |
| C-12 | Imbrication et export de fabrication | C4 · Fabrication | Expérimenté | 75 min | NumericTolerance |

### C1 · Architecture

*4 exercices — C-01, C-02, C-03, C-04*

#### C-01 — Enveloppe à brise-soleil orientés selon l'ensoleillement

| Rubrique | Valeur |
|---|---|
| **Lot** | C — Projets appliqués |
| **Thématique** | C1 · Architecture |
| **Réf. référentiel** | REF-027, REF-068, REF-095, REF-079 |
| **Niveau** | Expérimenté |
| **Durée cible** | 90 min |
| **Prérequis** | B-03, B-04 |
| **Mode de validation** | NumericTolerance — tolérance 2 % |
| **Solution de référence** | 45 composants |
| **Gamification associée** | G-22 Boss de fin de chapitre + G-23 Classement |
| **Statut de production** | À produire |

**1. Compétence visée** — Construire une enveloppe dont chaque élément réagit à une donnée d'analyse, et justifier le résultat par une mesure.

**2. Composants mobilisés** — Divide Surface, Evaluate Surface, Vector 2Pt, Angle, Rotate Axis, Remap Numbers, Area, Galapagos

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La façade sud du bâtiment reçoit 180 lames brise-soleil. Oriente chaque lame perpendiculairement à la direction du soleil au 21 juin à 15 h, puis optimise l'angle moyen pour limiter la surface exposée à 40 % de la surface vitrée tout en préservant au moins 25 % de vue directe.

**4. Données de départ fournies** — Une façade, un vecteur solaire et le contour vitré internalisés.

**5. Résultat attendu** — Les 180 lames orientées, deux indicateurs affichés, un jeu de paramètres optimisé.

**6. Zone CORRIGÉ — explication étape par étape**

1. Diviser la façade en 180 stations avec Divide Surface.
2. Récupérer les plans locaux avec Evaluate Surface.
3. Construire le vecteur solaire à partir de l'azimut et de la hauteur fournis.
4. Calculer pour chaque station l'angle entre la normale de lame et le vecteur solaire avec Angle.
5. Faire tourner chaque lame avec Rotate Axis autour de son axe horizontal.
6. Projeter les lames sur le plan perpendiculaire au soleil et mesurer l'aire projetée cumulée avec Area.
7. Calculer le taux d'ombrage et le taux de vue directe.
8. Brancher Galapagos sur l'angle de base et l'amplitude de variation, fonction objectif combinant les deux critères.
9. Lancer l'optimisation et internaliser le meilleur jeu de paramètres.

**7. Pièges fréquents**

- Aires projetées additionnées sans traiter les recouvrements entre lames.
- Fonction objectif à un seul critère : l'optimiseur ferme totalement la façade.
- Galapagos relié à un slider non borné : la recherche n'aboutit pas.

**8. Variantes et extensions**

- Étendre l'étude à quatre dates de référence.
- Piloter la largeur de lame plutôt que son angle.
- Produire la nomenclature des lames par angle distinct.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 4 points géométrie, 3 points indicateurs, 3 points optimisation.

#### C-02 — Résille structurelle sur plan libre

| Rubrique | Valeur |
|---|---|
| **Lot** | C — Projets appliqués |
| **Thématique** | C1 · Architecture |
| **Réf. référentiel** | REF-069, REF-094, REF-074, REF-049 |
| **Niveau** | Expérimenté |
| **Durée cible** | 90 min |
| **Prérequis** | B-04, C-01 |
| **Mode de validation** | NumericTolerance — tolérance 1 % |
| **Solution de référence** | 50 composants |
| **Gamification associée** | G-25 Animation de la relaxation |
| **Statut de production** | À produire |

**1. Compétence visée** — Générer une structure maillée relaxée et en extraire les données de fabrication.

**2. Composants mobilisés** — Mesh, Kangaroo, Weaverbird, Pipe, Deconstruct Mesh, Sort List, Text Tag 3D

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Sur le contour libre fourni, génère une toiture en résille triangulée, relaxe-la par Kangaroo pour obtenir une forme en équilibre de traction, puis produis la nomenclature des barres regroupées par longueur à 5 mm près et la liste des nœuds avec leur nombre de branches.

**4. Données de départ fournies** — Un contour fermé et trois points d'appui internalisés.

**5. Résultat attendu** — La résille relaxée, la nomenclature des barres et celle des nœuds.

**6. Zone CORRIGÉ — explication étape par étape**

1. Mailler le contour avec Mesh Surface ou Delaunay Mesh.
2. Extraire les arêtes du maillage avec Deconstruct Mesh et Mesh Edges.
3. Configurer Kangaroo : Length goal sur les arêtes, Anchor sur les appuis, Load vertical.
4. Lancer la relaxation jusqu'à convergence et figer le résultat.
5. Mesurer la longueur de chaque arête avec Length.
6. Regrouper les longueurs par tranche de 5 mm avec une division, un Round et un Create Set.
7. Compter les occurrences de chaque groupe avec Member Index.
8. Compter le nombre d'arêtes par sommet pour caractériser les nœuds.
9. Produire les deux tableaux et les exporter.

**7. Pièges fréquents**

- Relaxation non figée : le résultat change à chaque recalcul et la nomenclature devient instable.
- Regroupement par arrondi au plus proche : deux barres de 102 et 108 mm tombent dans des groupes différents alors qu'elles sont à 6 mm l'une de l'autre.
- Arêtes comptées deux fois car partagées par deux faces.

**8. Variantes et extensions**

- Comparer une résille triangulée et une résille quadrangulaire.
- Ajouter une contrainte de longueur maximale de barre.
- Générer les platines de nœud.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 4 points structure, 3 points nomenclature barres, 3 points nomenclature nœuds.

#### C-03 — Gradins avec contrôle de visibilité

| Rubrique | Valeur |
|---|---|
| **Lot** | C — Projets appliqués |
| **Thématique** | C1 · Architecture |
| **Réf. référentiel** | REF-047, REF-079, REF-046, REF-060 |
| **Niveau** | Expérimenté |
| **Durée cible** | 80 min |
| **Prérequis** | B-01, B-08 |
| **Mode de validation** | NumericTolerance — tolérance 1 mm |
| **Solution de référence** | 35 composants |
| **Gamification associée** | G-02 Barre de progression + G-20 Erreur à débusquer |
| **Statut de production** | À produire |

**1. Compétence visée** — Construire une géométrie pilotée par une contrainte de performance vérifiée rang par rang.

**2. Composants mobilisés** — Series, Shift List, Line, Angle, Larger Than, Gate And, Extrude, Graph Mapper

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Modélise 18 rangs de gradins de 850 mm de profondeur. La ligne de visée de chaque spectateur vers le point focal doit passer au moins 90 mm au-dessus de la tête du spectateur du rang précédent. Détermine automatiquement la hauteur de chaque marche et signale tout rang non conforme.

**4. Données de départ fournies** — Le point focal, la profondeur de rang et le nombre de rangs.

**5. Résultat attendu** — Les 18 rangs conformes et un tableau de contrôle du dégagement obtenu par rang.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser le premier rang à une altitude de départ connue.
2. Pour chaque rang, calculer la hauteur minimale garantissant 90 mm de dégagement par géométrie de la ligne de visée.
3. Mettre en place le calcul cumulatif avec une boucle Anemone ou un composant Python, la hauteur d'un rang dépendant du précédent.
4. Générer les positions de tous les rangs.
5. Construire le profil en gradins par PolyLine puis extruder sur la largeur.
6. Recalculer a posteriori le dégagement réel de chaque rang.
7. Contrôler avec Larger Than et afficher le tableau de conformité.

**7. Pièges fréquents**

- Calcul non cumulatif : le dégagement se dégrade à partir du troisième rang.
- Hauteur d'œil du spectateur oubliée (environ 1 200 mm en position assise).
- Vérification effectuée sur la hauteur de marche et non sur le dégagement de visée.

**8. Variantes et extensions**

- Comparer une courbe de gradins optimisée et une pente constante.
- Ajouter les circulations et les paliers.
- Calculer le volume de béton.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 4 points géométrie, 3 points calcul cumulatif, 3 points contrôle.

#### C-04 — Métré et chiffrage complet d'un module

| Rubrique | Valeur |
|---|---|
| **Lot** | C — Projets appliqués |
| **Thématique** | C1 · Architecture |
| **Réf. référentiel** | REF-082, REF-083, REF-084, REF-086 |
| **Niveau** | Expérimenté |
| **Durée cible** | 75 min |
| **Prérequis** | B-12, B-13 |
| **Mode de validation** | NumericTolerance — tolérance 0,5 % |
| **Solution de référence** | 45 composants |
| **Gamification associée** | G-01 Score visible + G-29 Défi quotidien |
| **Statut de production** | À produire |

**1. Compétence visée** — Produire un livrable économique complet à partir d'un modèle, avec traçabilité des hypothèses.

**2. Composants mobilisés** — Deconstruct Brep, Area, Volume, Sort List, Create Set, Member Index, Concatenate, Write File

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> À partir du module constructif fourni, produis un devis quantitatif estimatif par lot (gros œuvre, menuiserie, second œuvre) avec quantités, unités, prix unitaires et totaux, ainsi qu'un récapitulatif par lot et un total général. Le calcul doit rester juste si l'on modifie les dimensions du module.

**4. Données de départ fournies** — Un module constructif complet et une table de prix unitaires internalisée.

**5. Résultat attendu** — Un fichier CSV de devis structuré par lot avec sous-totaux et total général.

**6. Zone CORRIGÉ — explication étape par étape**

1. Classer les solides par lot à partir de leur calque d'origine via Geometry Pipeline.
2. Mesurer les quantités pertinentes par lot : volumes pour le gros œuvre, surfaces pour le second œuvre, linéaires pour les menuiseries.
3. Convertir chaque quantité dans son unité de devis (m³, m², ml).
4. Associer chaque poste à son prix unitaire par Member Index dans la table des prix.
5. Calculer les totaux par poste puis les sous-totaux par lot avec Mass Addition sur arbre.
6. Calculer le total général.
7. Composer les lignes de texte avec Concatenate et Format à deux décimales.
8. Écrire le fichier CSV et vérifier la recalculabilité en modifiant une dimension du module.

**7. Pièges fréquents**

- Sous-totaux calculés sur l'arbre aplati : les lots se mélangent.
- Prix unitaires codés en dur dans le graphe au lieu d'une table.
- Doubles comptes entre postes (une paroi comptée en volume et en surface).

**8. Variantes et extensions**

- Ajouter un coefficient de perte par lot.
- Produire une variante haute et une variante basse.
- Exporter vers Excel avec mise en forme.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 4 points quantités, 3 points structure du devis, 3 points recalculabilité.

### C2 · Design de mobilier

*3 exercices — C-05, C-06, C-07*

#### C-05 — Bibliothèque paramétrique avec débit et mise à plat CNC

| Rubrique | Valeur |
|---|---|
| **Lot** | C — Projets appliqués |
| **Thématique** | C2 · Design de mobilier |
| **Réf. référentiel** | REF-070, REF-082, REF-115, REF-087 |
| **Niveau** | Expérimenté |
| **Durée cible** | 90 min |
| **Prérequis** | B-06, B-12, B-17 |
| **Mode de validation** | GeometryTolerance — tolérance 0,2 mm |
| **Solution de référence** | 50 composants |
| **Gamification associée** | G-06 Niveaux et déblocage + G-05 Badges |
| **Statut de production** | À produire |

**1. Compétence visée** — Aller du modèle paramétrique au fichier de fabrication, en passant par la nomenclature.

**2. Composants mobilisés** — Box, Solid Difference, Orient, Rectangle, Text Tag 3D, Sort List, Write File

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Modélise une bibliothèque de largeur, hauteur et profondeur paramétrables, à montants verticaux tous les 800 mm maximum et tablettes réglables. Produis la nomenclature de débit et la mise à plat repérée de tous les panneaux, prête pour la CNC.

**4. Données de départ fournies** — Trois sliders de dimensions générales et un slider d'épaisseur de panneau.

**5. Résultat attendu** — Le meuble modélisé, la nomenclature de débit et les panneaux mis à plat et repérés.

**6. Zone CORRIGÉ — explication étape par étape**

1. Calculer le nombre de travées : largeur divisée par 800, arrondi supérieur.
2. Répartir les montants et en déduire la largeur réelle de travée.
3. Construire montants, traverses et tablettes par Box paramétrés.
4. Percer les rangées de trous de tablettes par un réseau de cylindres et Solid Difference.
5. Extraire la face principale de chaque panneau avec Deconstruct Brep et un tri par aire.
6. Orienter chaque face vers le plan XY avec Orient.
7. Répartir les panneaux à plat sans recouvrement par un calepinage simple.
8. Repérer chaque panneau avec Text Tag 3D et produire la nomenclature de débit.
9. Contrôler que le total des surfaces à plat correspond à la somme des faces d'origine.

**7. Pièges fréquents**

- Faces sélectionnées par index fixe : le tri casse dès qu'un panneau change de forme.
- Panneaux mis à plat qui se recouvrent.
- Repères perdus lors de la mise à plat car non propagés en parallèle des géométries.

**8. Variantes et extensions**

- Ajouter des portes et calculer leurs jeux.
- Générer le fichier DXF des panneaux.
- Ajouter une contrainte de nombre de plaques disponibles.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 4 points modèle, 3 points nomenclature, 3 points mise à plat.

#### C-06 — Chaise à assise en lamelles courbes

| Rubrique | Valeur |
|---|---|
| **Lot** | C — Projets appliqués |
| **Thématique** | C2 · Design de mobilier |
| **Réf. référentiel** | REF-069, REF-064, REF-074 |
| **Niveau** | Expérimenté |
| **Durée cible** | 85 min |
| **Prérequis** | B-16, B-17 |
| **Mode de validation** | NumericTolerance — tolérance 1 mm |
| **Solution de référence** | 42 composants |
| **Gamification associée** | G-26 Feedback visuel + G-07 Étoiles |
| **Statut de production** | À produire |

**1. Compétence visée** — Conjuguer une forme ergonomique libre et une contrainte de fabrication en lamelles droites.

**2. Composants mobilisés** — Interpolate, Divide Curve, Perp Frames, Loft, Sweep 1, Curvature, Larger Than

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Modélise l'assise et le dossier d'une chaise en 22 lamelles de 40 mm de large et 8 mm d'épaisseur suivant deux courbes directrices. Le rayon de courbure de chaque lamelle ne doit jamais descendre sous 350 mm, limite de cintrage du matériau : signale toute lamelle non conforme.

**4. Données de départ fournies** — Deux courbes directrices internalisées.

**5. Résultat attendu** — Les 22 lamelles et un tableau de contrôle du rayon minimal par lamelle.

**6. Zone CORRIGÉ — explication étape par étape**

1. Diviser les deux directrices en 22 stations.
2. Construire la courbe de chaque lamelle par Interpolate entre les points correspondants.
3. Récupérer les plans perpendiculaires au départ de chaque lamelle.
4. Construire la section de 40 × 8 mm et la balayer le long de chaque lamelle avec Sweep 1.
5. Échantillonner chaque lamelle avec Divide Curve et mesurer la courbure.
6. Convertir en rayon de courbure et prendre le minimum par lamelle avec Bounds.
7. Comparer à 350 mm avec Larger Than et afficher les lamelles non conformes en rouge.
8. Ajuster les directrices jusqu'à conformité générale.

**7. Pièges fréquents**

- Courbure mesurée sur un échantillonnage trop grossier : le point critique est manqué.
- Confondre courbure et rayon de courbure (l'un est l'inverse de l'autre).
- Sections non perpendiculaires : les lamelles se vrillent.

**8. Variantes et extensions**

- Ajouter le piètement et vérifier la stabilité par le centre de gravité.
- Faire varier la largeur de lamelle selon la zone.
- Produire les gabarits de cintrage.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 4 points géométrie, 3 points contrôle de courbure, 3 points conformité générale.

#### C-07 — Table de nuit configurable

| Rubrique | Valeur |
|---|---|
| **Lot** | C — Projets appliqués |
| **Thématique** | C2 · Design de mobilier |
| **Réf. référentiel** | REF-070, REF-072, REF-082, REF-106 |
| **Niveau** | Expérimenté |
| **Durée cible** | 80 min |
| **Prérequis** | B-06, B-07 |
| **Mode de validation** | GeometryTolerance — tolérance 0,2 mm |
| **Solution de référence** | 48 composants |
| **Gamification associée** | G-28 Avatar + G-10 Coffre à butin |
| **Statut de production** | À produire |

**1. Compétence visée** — Produire un configurateur complet, avec variantes discrètes et contrôle de cohérence.

**2. Composants mobilisés** — Stream Filter, Box, Solid Difference, Collision Many|Many, Value List, Volume, Concatenate

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Réalise un configurateur de table de nuit : 4 types de pieds au choix, de 1 à 3 tiroirs, deux matériaux avec des épaisseurs différentes. Le modèle doit rester valide dans toutes les combinaisons et produire son prix estimatif.

**4. Données de départ fournies** — Une Value List de types de pied, un slider de nombre de tiroirs, une Value List de matériau.

**5. Résultat attendu** — Le meuble reconfiguré à la volée et un Panel affichant le prix.

**6. Zone CORRIGÉ — explication étape par étape**

1. Modéliser les quatre familles de pieds dans des groupes distincts.
2. Sélectionner la famille active avec Stream Filter piloté par la Value List.
3. Déduire l'épaisseur de panneau du matériau choisi via Member Index dans une table.
4. Répartir automatiquement les tiroirs sur la hauteur disponible selon leur nombre.
5. Appliquer les jeux fonctionnels et vérifier l'absence de collision dans chaque configuration.
6. Mesurer les volumes par matériau et appliquer les prix unitaires.
7. Composer le libellé de configuration et le prix dans un Panel.
8. Balayer systématiquement les 24 combinaisons pour vérifier qu'aucune ne produit d'erreur.

**7. Pièges fréquents**

- Une seule combinaison testée : les cas limites (3 tiroirs, panneau épais) échouent.
- Stream Filter alimenté par une Value List dont les valeurs ne sont pas des entiers consécutifs.
- Hauteur de tiroir négative quand la hauteur disponible est insuffisante.

**8. Variantes et extensions**

- Ajouter une poignée au choix.
- Publier le configurateur sur le web avec ShapeDiver.
- Générer la fiche produit PDF.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode GeometryTolerance.

**10. Barème** — 4 points configurateur, 3 points robustesse, 3 points chiffrage.

### C3 · Joaillerie

*3 exercices — C-08, C-09, C-10*

#### C-08 — Bague solitaire complète

| Rubrique | Valeur |
|---|---|
| **Lot** | C — Projets appliqués |
| **Thématique** | C3 · Joaillerie |
| **Réf. référentiel** | REF-069, REF-068, REF-081, REF-079 |
| **Niveau** | Expérimenté |
| **Durée cible** | 85 min |
| **Prérequis** | B-09, B-10 |
| **Mode de validation** | NumericTolerance — tolérance 0,05 g et 0,05 mm |
| **Solution de référence** | 45 composants |
| **Gamification associée** | G-05 Badges + G-09 Récompense cachée |
| **Statut de production** | À produire |

**1. Compétence visée** — Assembler plusieurs sous-ensembles techniques en un bijou complet, avec contrôle de poids.

**2. Composants mobilisés** — Revolution, Polar Array, Sweep 1, Solid Union, Volume, Multiplication, Collision

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Modélise une bague solitaire pour une pierre ronde de 6,5 mm : anneau de taille paramétrable, chaton, panier et 4 griffes. Contrôle que la masse en or 750 reste inférieure à 3,2 g et que la hauteur totale ne dépasse pas 8 mm.

**4. Données de départ fournies** — Un slider de taille de doigt et un slider de diamètre de pierre.

**5. Résultat attendu** — La bague complète et deux indicateurs : masse et hauteur.

**6. Zone CORRIGÉ — explication étape par étape**

1. Calculer le diamètre intérieur à partir de la taille française : diamètre = (taille + 40) / π.
2. Construire le profil de l'anneau et le révolutionner.
3. Construire le chaton et le panier par balayage et révolution.
4. Reprendre les griffes de l'exercice B-09 et les répartir par Polar Array.
5. Unir l'ensemble avec Solid Union et vérifier que le résultat est un solide unique fermé.
6. Mesurer le volume total et le multiplier par la masse volumique de l'or 750 (environ 15,6 g/cm³).
7. Mesurer la hauteur totale par Bounding Box.
8. Afficher les deux indicateurs avec un test de conformité.

**7. Pièges fréquents**

- Solid Union renvoyant plusieurs solides : des éléments ne se touchent pas réellement.
- Volume en mm³ multiplié directement par une masse volumique en g/cm³.
- Taille de doigt confondue avec le diamètre.

**8. Variantes et extensions**

- Ajouter un pavage sur le corps de bague.
- Optimiser le profil pour minimiser la masse à rigidité constante.
- Produire la vue technique cotée.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 4 points géométrie, 3 points unicité du solide, 3 points indicateurs.

#### C-09 — Pavage de pierres sur surface libre

| Rubrique | Valeur |
|---|---|
| **Lot** | C — Projets appliqués |
| **Thématique** | C3 · Joaillerie |
| **Réf. référentiel** | REF-068, REF-101, REF-080, REF-045 |
| **Niveau** | Expérimenté |
| **Durée cible** | 85 min |
| **Prérequis** | B-04, C-08 |
| **Mode de validation** | NumericTolerance — tolérance 0,01 mm |
| **Solution de référence** | 48 composants |
| **Gamification associée** | G-13 Casino motifs assortis + G-16 Chasse au trésor |
| **Statut de production** | À produire |

**1. Compétence visée** — Répartir des éléments de tailles variées sur une surface courbe en respectant des distances minimales.

**2. Composants mobilisés** — Populate Geometry, Surface Closest Point, Evaluate Surface, Distance, Cull Pattern, Sphere, Solid Difference

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Pave la surface libre fournie de pierres rondes de 1,2 à 2,5 mm réparties de manière quasi aléatoire mais sans jamais laisser moins de 0,3 mm de métal entre deux pierres voisines. Perce ensuite les logements coniques correspondants.

**4. Données de départ fournies** — Une surface libre internalisée et un slider de densité.

**5. Résultat attendu** — Les pierres réparties, aucune distance inter-pierres inférieure à 0,3 mm, et les logements percés.

**6. Zone CORRIGÉ — explication étape par étape**

1. Semer des points sur la surface avec Populate Geometry.
2. Attribuer un diamètre aléatoire à chaque point avec Random dans le domaine 1,2 à 2,5.
3. Calculer les distances entre paires de points voisins avec Closest Points.
4. Comparer chaque distance à la somme des deux rayons plus 0,3 mm.
5. Éliminer itérativement les points en conflit avec un Cull Pattern piloté par ce test, dans une boucle Anemone.
6. Récupérer les normales locales avec Evaluate Surface et construire un plan par pierre.
7. Modéliser chaque pierre et son logement conique dans ce plan.
8. Percer la surface épaissie avec Solid Difference.
9. Recontrôler a posteriori que la distance minimale est respectée.

**7. Pièges fréquents**

- Test de distance effectué sur les centres sans tenir compte des rayons.
- Élimination en une seule passe : de nouveaux conflits apparaissent après suppression.
- Logements percés perpendiculairement au plan global et non à la normale locale.

**8. Variantes et extensions**

- Imposer une densité variable pilotée par un attracteur.
- Trier les pierres par taille et produire la nomenclature de commande.
- Calculer le poids en carats.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 4 points répartition, 3 points respect de la distance, 3 points logements.

#### C-10 — Motif gravé génératif sur bijou

| Rubrique | Valeur |
|---|---|
| **Lot** | C — Projets appliqués |
| **Thématique** | C3 · Joaillerie |
| **Réf. référentiel** | REF-115, REF-095, REF-069 |
| **Niveau** | Expérimenté |
| **Durée cible** | 80 min |
| **Prérequis** | B-10, C-08 |
| **Mode de validation** | NumericTolerance — tolérance 0,05 mm² |
| **Solution de référence** | 45 composants |
| **Gamification associée** | G-27 Narration Serengeti + G-09 Récompense cachée |
| **Statut de production** | À produire |

**1. Compétence visée** — Produire un motif non répétitif contrôlé par des règles, puis le graver physiquement.

**2. Composants mobilisés** — Voronoi, Random, Offset Curve, Surface Morph, Solid Difference, Area, Galapagos

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Génère sur le corps de bague un motif de type Voronoï dont les cellules mesurent entre 0,8 et 2,2 mm², sépare les cellules par un filet de 0,25 mm, grave à 0,3 mm de profondeur, et fais en sorte que le motif boucle sans rupture visible.

**4. Données de départ fournies** — La bague de l'exercice C-08 et un slider de densité de motif.

**5. Résultat attendu** — Le motif gravé, continu au raccord, cellules dans le domaine d'aire imposé.

**6. Zone CORRIGÉ — explication étape par étape**

1. Construire la surface développée du corps de bague (rectangle circonférence × largeur).
2. Semer des points avec Populate 2D dans ce rectangle, en dupliquant une bande aux deux extrémités pour assurer la continuité du raccord.
3. Générer le diagramme de Voronoï sur ces points.
4. Décaler chaque cellule vers l'intérieur de 0,125 mm avec Offset Curve pour créer le filet.
5. Mesurer l'aire de chaque cellule et éliminer celles hors du domaine 0,8 à 2,2 mm².
6. Appliquer le motif sur la surface de la bague par Surface Morph.
7. Extruder vers l'intérieur de 0,3 mm et soustraire avec Solid Difference.
8. Vérifier la continuité au raccord et régler la densité par Galapagos si nécessaire.

**7. Pièges fréquents**

- Points semés uniquement dans le rectangle : le raccord présente une rupture nette.
- Offset produisant des cellules dégénérées pour les petites cellules.
- Profondeur de gravure supérieure à l'épaisseur locale de l'anneau.

**8. Variantes et extensions**

- Remplacer le Voronoï par un motif hexagonal déformé.
- Faire varier la profondeur de gravure selon la position.
- Exporter en STL pour impression cire.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 4 points motif, 3 points contraintes d'aire, 3 points raccord.

### C4 · Fabrication

*2 exercices — C-11, C-12*

#### C-11 — Déroulé de tôle pliée avec compensation

| Rubrique | Valeur |
|---|---|
| **Lot** | C — Projets appliqués |
| **Thématique** | C4 · Fabrication |
| **Réf. référentiel** | REF-116, REF-115, REF-082 |
| **Niveau** | Expérimenté |
| **Durée cible** | 80 min |
| **Prérequis** | B-17, C-05 |
| **Mode de validation** | NumericTolerance — tolérance 0,1 mm |
| **Solution de référence** | 40 composants |
| **Gamification associée** | G-20 Erreur à débusquer + G-03 Compte à rebours |
| **Statut de production** | À produire |

**1. Compétence visée** — Calculer un développé industriel exact et produire le plan de pliage.

**2. Composants mobilisés** — Brep | Plane, Unroll (Squid ou Python), Length, Series, Text Tag 3D, Write File

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La pièce en tôle de 2 mm comporte 5 plis à 90° de rayon intérieur 3 mm. Produis son développé en tenant compte du facteur K de 0,44, cote les lignes de pli et vérifie que la longueur développée calculée correspond à la longueur mesurée sur le développé.

**4. Données de départ fournies** — Une pièce en tôle pliée internalisée et les paramètres matière.

**5. Résultat attendu** — Le développé à plat, les lignes de pli cotées et la vérification de longueur.

**6. Zone CORRIGÉ — explication étape par étape**

1. Identifier les faces planes et les zones de pli par analyse des normales.
2. Calculer pour chaque pli la longueur de la fibre neutre : (rayon intérieur + K × épaisseur) × angle en radians.
3. Sommer les longueurs des faces planes et des fibres neutres pour obtenir la longueur développée théorique.
4. Déplier la pièce face par face avec Orient successifs, ou utiliser un composant de dépliage.
5. Insérer les longueurs de fibre neutre entre les faces dépliées.
6. Tracer les lignes de pli et les coter avec Text Tag 3D en indiquant le sens de pliage.
7. Mesurer la longueur du développé obtenu et la comparer à la valeur théorique.
8. Exporter le développé en DXF.

**7. Pièges fréquents**

- Utiliser le rayon extérieur au lieu du rayon intérieur dans la formule.
- Angle de pli confondu avec l'angle d'ouverture (90° de pli correspond à un angle complémentaire selon la convention).
- Facteur K appliqué à l'épaisseur totale au lieu de la position de la fibre neutre.

**8. Variantes et extensions**

- Traiter des plis à angles quelconques.
- Gérer plusieurs épaisseurs et facteurs K.
- Ajouter les dégagements de pli aux angles.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 4 points développé, 3 points compensation, 3 points cotation.

#### C-12 — Imbrication et export de fabrication

| Rubrique | Valeur |
|---|---|
| **Lot** | C — Projets appliqués |
| **Thématique** | C4 · Fabrication |
| **Réf. référentiel** | REF-113, REF-114, REF-087 |
| **Niveau** | Expérimenté |
| **Durée cible** | 75 min |
| **Prérequis** | B-13, C-05 |
| **Mode de validation** | NumericTolerance — tolérance 1 % |
| **Solution de référence** | 38 composants |
| **Gamification associée** | G-21 Golf de composants + G-23 Classement |
| **Statut de production** | À produire |

**1. Compétence visée** — Boucler la chaîne conception-fabrication avec un livrable machine.

**2. Composants mobilisés** — OpenNest, Rectangle, Sort List, Text Tag 3D, Write File, Area, Mass Addition

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Imbrique les 46 pièces découpées fournies dans des plaques de 3 000 × 1 500 mm avec un espacement de 8 mm entre pièces et 15 mm de bord de plaque. Produis le plan de découpe repéré, le nombre de plaques et le taux de matière utile, puis exporte en DXF par plaque.

**4. Données de départ fournies** — 46 contours de pièces internalisés.

**5. Résultat attendu** — Le plan d'imbrication, les indicateurs et un fichier DXF par plaque.

**6. Zone CORRIGÉ — explication étape par étape**

1. Préparer les contours : vérifier qu'ils sont fermés et plans avec un contrôle en amont.
2. Construire le contour de plaque utile en retirant 15 mm sur chaque bord.
3. Configurer OpenNest avec l'espacement de 8 mm et autoriser la rotation par pas de 90°.
4. Lancer l'imbrication et récupérer les pièces placées et leur numéro de plaque.
5. Compter les plaques avec Create Set sur les numéros de plaque.
6. Calculer le taux de matière utile : aire des pièces divisée par aire des plaques utilisées.
7. Repérer chaque pièce avec Text Tag 3D en conservant son repère d'origine.
8. Grouper les pièces par plaque avec un arbre et écrire un DXF par branche.

**7. Pièges fréquents**

- Repères perdus car non triés dans le même ordre que les pièces placées.
- Espacement configuré comme un décalage de contour au lieu d'une distance entre pièces.
- Pièces non fermées silencieusement ignorées par l'imbrication.

**8. Variantes et extensions**

- Comparer avec le calepinage manuel de l'exercice B-13.
- Ajouter une contrainte de sens de fil.
- Générer le parcours d'outil approximatif et estimer le temps de découpe.

**9. Mise en œuvre dans Magpie** — Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode NumericTolerance.

**10. Barème** — 4 points imbrication, 3 points indicateurs, 3 points export.

---

## Lot G — Exercices gamifiés

**Niveau** : Tous niveaux · **32 exercices** · **8 h 41 cumulées**

Un exercice par technique de gamification, transverse aux autres lots. Spécifié, pas encore produit.

| ID | Titre | Thématique | Niveau | Durée | Validation |
|---|---|---|---|---|---|
| G-01 | Le tableau des scores | G1 · Progression et récompense | Débutant | 10 min | ExactOrderedList |
| G-02 | La barre de progression | G1 · Progression et récompense | Débutant | 12 min | GeometryTolerance |
| G-03 | Contre la montre | G1 · Progression et récompense | Intermédiaire | 6 min | ExactOrderedList |
| G-04 | Trois vies | G1 · Progression et récompense | Intermédiaire | 15 min | SingleValue |
| G-05 | La collection de badges | G1 · Progression et récompense | Intermédiaire | 20 min | NumericTolerance |
| G-06 | Le déblocage progressif | G1 · Progression et récompense | Intermédiaire | 18 min | SetEquality |
| G-07 | Une, deux ou trois étoiles | G1 · Progression et récompense | Intermédiaire | 15 min | GeometryTolerance |
| G-08 | La série de bonnes réponses | G1 · Progression et récompense | Intermédiaire | 16 min | ExactOrderedList |
| G-09 | Le composant caché | G2 · Exploration et découverte | Débutant | 10 min | SingleValue |
| G-10 | Le coffre à butin | G2 · Exploration et découverte | Intermédiaire | 14 min | SetEquality |
| G-11 | Les mots croisés des composants | G2 · Exploration et découverte | Débutant | 15 min | SingleValue |
| G-12 | Le memory des composants | G2 · Exploration et découverte | Débutant | 12 min | SetEquality |
| G-13 | La machine à sous des motifs | G2 · Exploration et découverte | Intermédiaire | 15 min | ExactOrderedList |
| G-14 | Le puzzle de câblage | G3 · Manipulation et adresse | Débutant | 12 min | GeometryTolerance |
| G-15 | Le dessin à compléter | G3 · Manipulation et adresse | Débutant | 14 min | GeometryTolerance |
| G-16 | La chasse au trésor | G3 · Manipulation et adresse | Intermédiaire | 18 min | SingleValue |
| G-17 | Le quiz éclair | G4 · Connaissance et mémorisation | Débutant | 8 min | ExactOrderedList |
| G-18 | Vrai ou faux à élimination | G4 · Connaissance et mémorisation | Débutant | 10 min | ExactOrderedList |
| G-19 | Le composant mystère | G4 · Connaissance et mémorisation | Intermédiaire | 12 min | ExactOrderedList |
| G-20 | La chasse aux bugs | G4 · Connaissance et mémorisation | Intermédiaire | 20 min | SetEquality |
| G-21 | Le golf de composants | G5 · Performance et compétition | Intermédiaire | 20 min | GeometryTolerance |
| G-22 | Le boss de fin de chapitre | G5 · Performance et compétition | Perfectionnement | 45 min | ExactOrderedList |
| G-23 | Le duel | G5 · Performance et compétition | Intermédiaire | 20 min | ExactOrderedList |
| G-24 | Le retour sonore | G6 · Sensations et immersion | Débutant | 10 min | SingleValue |
| G-25 | L'animation de la solution | G6 · Sensations et immersion | Perfectionnement | 25 min | SetEquality |
| G-26 | Le retour visuel immédiat | G6 · Sensations et immersion | Débutant | 12 min | SingleValue |
| G-27 | La savane paramétrique | G6 · Sensations et immersion | Débutant | 20 min | GeometryTolerance |
| G-28 | L'avatar paramétrique | G6 · Sensations et immersion | Intermédiaire | 22 min | SingleValue |
| G-29 | Le défi du jour | G7 · Régularité et communauté | Intermédiaire | 10 min | NumericTolerance |
| G-30 | Le relais à deux | G7 · Régularité et communauté | Perfectionnement | 30 min | SetEquality |
| G-31 | L'arbre de compétences | G7 · Régularité et communauté | Intermédiaire | 15 min | SetEquality |
| G-32 | Les indices payants | G7 · Régularité et communauté | Intermédiaire | 20 min | SetEquality |

### G1 · Progression et récompense

*8 exercices — G-01, G-02, G-03, G-04, G-05, G-06, G-07, G-08*

#### G-01 — Le tableau des scores

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G1 · Progression et récompense |
| **Réf. référentiel** | REF-047, REF-043 |
| **Niveau** | Débutant |
| **Durée cible** | 10 min |
| **Prérequis** | A-10 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | Score visible et barème explicite (scoreboard) |
| **Statut de production** | À produire |

**1. Compétence visée** — Rendre visible la performance immédiate de l'apprenant sur une tâche de tri.

**2. Composants mobilisés** — Series, Sort List, Panel, Mass Addition, Value Tracker (Human)

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Trie les 12 valeurs par ordre croissant. Chaque valeur correctement placée rapporte 10 points, chaque valeur mal placée en coûte 5. Le score s'affiche en direct dans le panneau SCORE.

**4. Données de départ fournies** — Une liste de 12 nombres mélangés et un groupe SCORE pré-câblé.

**5. Résultat attendu** — Liste triée et score final de 120 points.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Sort List sur la liste fournie.
2. Brancher la sortie sur le paramètre de réponse attendu par Magpie.
3. Le groupe SCORE compare position par position et cumule les points.
4. Le score atteint 120 lorsque les 12 valeurs sont bien placées.

**7. Pièges fréquents**

- Trier une copie de la liste sans la rebrancher sur le paramètre de réponse.
- Score partiel accepté comme réussite : le seuil de validation reste à 100 %.

**8. Variantes et extensions**

- Introduire un malus de temps.
- Afficher un score cumulé sur tout le parcours.

**9. Mise en œuvre dans Magpie** — Magpie compare la proposition à la solution élément par élément et calcule le score par la formule 10×justes − 5×faux. Le score est renvoyé au plugin comme métrique secondaire et affiché en temps réel dans le panneau de l'exercice.

**10. Barème** — 120 points maximum, validation à 120.

#### G-02 — La barre de progression

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G1 · Progression et récompense |
| **Réf. référentiel** | REF-062, REF-063 |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | A-34 |
| **Mode de validation** | GeometryTolerance — tolérance 0,5 mm |
| **Solution de référence** | 14 composants |
| **Gamification associée** | Barre de progression et jalons intermédiaires |
| **Statut de production** | À produire |

**1. Compétence visée** — Découper une tâche en jalons visibles pour soutenir l'effort.

**2. Composants mobilisés** — Circle, Rectangle, Polygon, Line, Boolean Toggle, Gradient

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Reconstitue le logo en 5 étapes. Chaque forme correctement placée fait progresser la barre de 20 %. La barre passe au vert à 100 %.

**4. Données de départ fournies** — Un gabarit du logo en filigrane et une barre de progression pré-câblée.

**5. Résultat attendu** — Les 5 formes placées, barre à 100 %.

**6. Zone CORRIGÉ — explication étape par étape**

1. Identifier les 5 formes du gabarit : cercle, rectangle, triangle, hexagone, segment.
2. Construire chaque forme avec le composant natif adapté.
3. Positionner chaque forme sur son repère.
4. Brancher chaque forme sur l'entrée correspondante du groupe de contrôle.
5. Observer la barre progresser à chaque forme validée.

**7. Pièges fréquents**

- Formes correctes mais mal positionnées : le sous-critère reste rouge.
- Brancher toutes les formes sur une seule entrée.

**8. Variantes et extensions**

- Barre segmentée par chapitre.
- Ajouter un pourcentage chiffré.

**9. Mise en œuvre dans Magpie** — Magpie évalue 5 sous-critères indépendants. Le taux de réussite partiel pilote la largeur d'un rectangle de progression dessiné sur le canvas et sa couleur via un Gradient.

**10. Barème** — 20 % par forme, validation à 100 %.

#### G-03 — Contre la montre

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G1 · Progression et récompense |
| **Réf. référentiel** | REF-042, REF-043 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 6 min |
| **Prérequis** | A-11, A-12 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 12 composants |
| **Gamification associée** | Compte à rebours et mode time attack |
| **Statut de production** | À produire |

**1. Compétence visée** — Travailler la vitesse d'exécution sur des gestes déjà maîtrisés.

**2. Composants mobilisés** — List Item, List Length, Sub List, Panel, Timer

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Cinq extractions de listes à réaliser en moins de 180 secondes. Le chronomètre démarre à l'ouverture de l'exercice et s'affiche en haut du canvas.

**4. Données de départ fournies** — Cinq listes internalisées et cinq paramètres de réponse.

**5. Résultat attendu** — Les cinq extractions correctes dans le temps imparti.

**6. Zone CORRIGÉ — explication étape par étape**

1. Lire les cinq consignes affichées dans le Scribble.
2. Traiter chaque liste avec le composant adapté sans chercher l'élégance.
3. Brancher les cinq réponses.
4. Valider avant la fin du compte à rebours.

**7. Pièges fréquents**

- Perdre du temps à ranger le canvas au lieu de répondre.
- Réponse correcte soumise après l'échéance : la validation reste acquise, le bonus est perdu.

**8. Variantes et extensions**

- Mode survie où chaque erreur retire 15 secondes.
- Classement des temps entre apprenants.

**9. Mise en œuvre dans Magpie** — Magpie exploite la métrique de durée déjà collectée par le plugin et la compare à une durée cible stockée dans le JSON de l'exercice. Au-delà, l'exercice reste validable mais sans le bonus de temps.

**10. Barème** — 5 points, plus 3 points de bonus si le temps cible est tenu.

#### G-04 — Trois vies

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G1 · Progression et récompense |
| **Réf. référentiel** | REF-053, REF-054 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 15 min |
| **Prérequis** | A-24, A-25 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 10 composants |
| **Gamification associée** | Système de vies et tentatives limitées |
| **Statut de production** | À produire |

**1. Compétence visée** — Inciter à réfléchir avant de soumettre, en limitant le nombre de tentatives.

**2. Composants mobilisés** — Longest List, Cross Reference, Addition, List Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Trois questions sur les modes de correspondance de données. Tu disposes de trois vies : chaque mauvaise soumission en coûte une. À zéro vie, l'exercice se recharge depuis le début.

**4. Données de départ fournies** — Deux listes de tailles différentes et trois paramètres de réponse.

**5. Résultat attendu** — Les trois réponses correctes avec au moins une vie restante.

**6. Zone CORRIGÉ — explication étape par étape**

1. Déterminer par le raisonnement le nombre de résultats attendus dans chaque mode.
2. Vérifier mentalement avant de brancher.
3. Soumettre les trois réponses en une seule validation.
4. Utiliser les vies restantes comme indicateur de maîtrise.

**7. Pièges fréquents**

- Soumettre par essais successifs : les vies s'épuisent en trois coups.
- Confondre Longest List et Cross Reference.

**8. Variantes et extensions**

- Vies régénérées par une bonne réponse d'affilée.
- Mode sans faute avec une seule vie.

**9. Mise en œuvre dans Magpie** — Magpie utilise la métrique du nombre de tentatives. Au-delà de trois soumissions infructueuses, le plugin déclenche le rechargement de l'exercice et remet le compteur à zéro.

**10. Barème** — 3 points, moins 1 point par vie perdue.

#### G-05 — La collection de badges

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G1 · Progression et récompense |
| **Réf. référentiel** | REF-079, REF-081, REF-098 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | A-47, A-49 |
| **Mode de validation** | NumericTolerance — tolérance 0,5 % |
| **Solution de référence** | 16 composants |
| **Gamification associée** | Badges et trophées par compétence |
| **Statut de production** | À produire |

**1. Compétence visée** — Valoriser la maîtrise d'une famille complète de composants.

**2. Composants mobilisés** — Length, Area, Volume, Point, Bounding Box, Text Tag 3D

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Six mesures à produire sur le même assemblage. Chaque mesure exacte débloque un badge. La collection complète débloque le badge doré ARPENTEUR.

**4. Données de départ fournies** — Un assemblage internalisé et six paramètres de réponse.

**5. Résultat attendu** — Les six mesures exactes et le badge doré.

**6. Zone CORRIGÉ — explication étape par étape**

1. Mesurer le développé des arêtes avec Length et Mass Addition.
2. Mesurer la surface totale avec Area.
3. Mesurer le volume avec Volume.
4. Localiser le centre de gravité avec la sortie C de Volume.
5. Mesurer l'encombrement avec Bounding Box et Deconstruct Box.
6. Compter les faces avec Deconstruct Brep et List Length.

**7. Pièges fréquents**

- Mesurer la surface d'une face au lieu de la surface totale.
- Encombrement mesuré dans un repère tourné.

**8. Variantes et extensions**

- Badges de rareté selon le nombre de tentatives.
- Badge secret pour une solution en moins de 12 composants.

**9. Mise en œuvre dans Magpie** — Chaque sous-critère validé écrit un identifiant de badge dans le résultat du parcours. Le plugin agrège les badges au niveau du parcours et les fait figurer sur le certificat PDF.

**10. Barème** — 1 point par badge, badge doré à 6/6.

#### G-06 — Le déblocage progressif

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G1 · Progression et récompense |
| **Réf. référentiel** | REF-059, REF-060, REF-061 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 18 min |
| **Prérequis** | A-29, A-30, A-31 |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 18 composants |
| **Gamification associée** | Niveaux et déblocage séquentiel (unlock) |
| **Statut de production** | À produire |

**1. Compétence visée** — Enchaîner des difficultés croissantes, chaque niveau ouvrant l'accès au suivant.

**2. Composants mobilisés** — Equality, Larger Than, Gate And, Gate Or, Stream Filter, Dispatch

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Trois niveaux de logique. Le niveau 2 ne devient actif qu'une fois le niveau 1 validé, et ainsi de suite. Les groupes verrouillés apparaissent grisés.

**4. Données de départ fournies** — Trois groupes de travail dont deux verrouillés.

**5. Résultat attendu** — Les trois niveaux validés successivement.

**6. Zone CORRIGÉ — explication étape par étape**

1. Niveau 1 : produire un booléen unique par comparaison.
2. Niveau 2 : combiner deux conditions par Gate And.
3. Niveau 3 : orienter un flux géométrique selon la condition combinée.
4. Valider chaque niveau avant de passer au suivant.

**7. Pièges fréquents**

- Tenter de câbler le niveau 3 avant validation du niveau 1.
- Réutiliser un booléen d'un niveau antérieur devenu obsolète.

**8. Variantes et extensions**

- Déblocage d'un niveau bonus caché.
- Retour possible sur un niveau validé pour améliorer son score.

**9. Mise en œuvre dans Magpie** — Le parcours Magpie enchaîne trois exercices distincts avec un seuil de réussite par étape. Le bouton Suivant reste inactif tant que l'étape courante n'est pas validée, comportement déjà présent dans le prototype.

**10. Barème** — 3 points, 1 par niveau.

#### G-07 — Une, deux ou trois étoiles

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G1 · Progression et récompense |
| **Réf. référentiel** | REF-067, REF-068 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 15 min |
| **Prérequis** | A-39 |
| **Mode de validation** | GeometryTolerance — tolérance 0,5 mm |
| **Solution de référence** | 9 composants |
| **Gamification associée** | Notation par étoiles selon la qualité de la solution |
| **Statut de production** | À produire |

**1. Compétence visée** — Distinguer la simple réussite de la réussite élégante.

**2. Composants mobilisés** — Rectangular Array, Polar Array, Move, Series, Graft

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Produis la trame demandée. Une étoile pour un résultat juste, deux étoiles si la solution tient en moins de 12 composants, trois étoiles si elle reste juste après changement des paramètres de trame.

**4. Données de départ fournies** — Un module et une trame cible affichée en filigrane.

**5. Résultat attendu** — La trame produite, idéalement en moins de 12 composants et paramétrique.

**6. Zone CORRIGÉ — explication étape par étape**

1. Analyser la trame cible : nombre de rangs, nombre de colonnes, entraxes.
2. Choisir Rectangular Array plutôt qu'une suite de Move.
3. Paramétrer les entraxes par des sliders et non par des valeurs codées en dur.
4. Vérifier que le résultat reste juste après modification des sliders.

**7. Pièges fréquents**

- Placer les modules un par un : le résultat est juste mais coûte 40 composants.
- Coder les entraxes en dur : la troisième étoile est perdue.

**8. Variantes et extensions**

- Étoile bonus pour une solution sans Graft.
- Comparatif des solutions de la promotion.

**9. Mise en œuvre dans Magpie** — Magpie exploite deux métriques déjà disponibles : le nombre de composants et l'écart au chemin attendu. Une troisième vérification relance la comparaison avec un second jeu de paramètres pour tester la robustesse.

**10. Barème** — 3 étoiles, validation dès la première.

#### G-08 — La série de bonnes réponses

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G1 · Progression et récompense |
| **Réf. référentiel** | REF-044, REF-045, REF-046 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 16 min |
| **Prérequis** | A-13, A-14, A-16 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 20 composants |
| **Gamification associée** | Combo et multiplicateur de série (streak) |
| **Statut de production** | À produire |

**1. Compétence visée** — Récompenser la régularité plutôt que le coup de chance.

**2. Composants mobilisés** — Sort List, Cull Pattern, Shift List, Reverse List, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Huit manipulations de listes s'enchaînent. Chaque bonne réponse consécutive augmente le multiplicateur : ×1, ×1,5, ×2, ×3. Une erreur remet le multiplicateur à ×1.

**4. Données de départ fournies** — Huit listes internalisées et huit paramètres de réponse.

**5. Résultat attendu** — Les huit réponses correctes, multiplicateur maximal atteint.

**6. Zone CORRIGÉ — explication étape par étape**

1. Traiter les huit consignes dans l'ordre imposé par le Scribble.
2. Vérifier chaque résultat dans un Panel avant de brancher la réponse.
3. Ne soumettre qu'une fois l'ensemble contrôlé.
4. Observer le multiplicateur monter dans le panneau de score.

**7. Pièges fréquents**

- Traiter les listes dans le désordre : la série se casse.
- Confondre Cull Pattern et Cull Index sur la manipulation 4.

**8. Variantes et extensions**

- Série conservée d'une session à l'autre.
- Bonus de série sur toute une thématique.

**9. Mise en œuvre dans Magpie** — Le parcours Magpie enchaîne huit micro-exercices. Le plugin conserve l'état de la série entre exercices et applique le multiplicateur au score du parcours.

**10. Barème** — 8 points de base, jusqu'à 24 points avec multiplicateur.

### G2 · Exploration et découverte

*5 exercices — G-09, G-10, G-11, G-12, G-13*

#### G-09 — Le composant caché

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G2 · Exploration et découverte |
| **Réf. référentiel** | REF-028, REF-056 |
| **Niveau** | Débutant |
| **Durée cible** | 10 min |
| **Prérequis** | A-05 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 1 composants |
| **Gamification associée** | Récompense cachée (easter egg) |
| **Statut de production** | À produire |

**1. Compétence visée** — Encourager l'exploration du canvas et des menus contextuels.

**2. Composants mobilisés** — Panel, Param Viewer, Scribble, Cluster

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Un composant a été rendu invisible sur ce canvas. Trouve-le, révèle-le et recopie dans le Panel le mot de passe qu'il contient.

**4. Données de départ fournies** — Un canvas contenant un composant masqué via le menu contextuel.

**5. Résultat attendu** — Le mot de passe correctement recopié.

**6. Zone CORRIGÉ — explication étape par étape**

1. Utiliser Ctrl+A pour sélectionner tout le contenu du canvas et repérer l'élément invisible.
2. Ou utiliser Metahopper pour lister tous les composants du document.
3. Réactiver son affichage via le menu contextuel.
4. Lire le mot de passe et le recopier dans le Panel de réponse.

**7. Pièges fréquents**

- Chercher uniquement à l'écran sans utiliser la sélection globale.
- Recopier le mot de passe avec un espace parasite.

**8. Variantes et extensions**

- Plusieurs easter eggs dans un même parcours.
- Mot de passe déblocant un exercice bonus.

**9. Mise en œuvre dans Magpie** — L'exercice est livré avec un composant dont l'aperçu et l'affichage sont désactivés. Magpie valide sur une chaîne de caractères exacte, insensible à la casse.

**10. Barème** — 1 point, plus badge secret EXPLORATEUR.

#### G-10 — Le coffre à butin

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G2 · Exploration et découverte |
| **Réf. référentiel** | REF-068, REF-045 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 14 min |
| **Prérequis** | A-14, A-39 |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | Récompense aléatoire (loot box) |
| **Statut de production** | À produire |

**1. Compétence visée** — Introduire une part d'aléatoire maîtrisé pour renouveler l'intérêt.

**2. Composants mobilisés** — Random, Jitter, Cull Pattern, Rectangular Array, Sphere

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Vingt coffres sont disposés en trame. Trois contiennent une récompense, désignés par le tirage aléatoire de graine 7. Identifie-les et affiche leurs index.

**4. Données de départ fournies** — Une trame de 20 positions et un Random de graine imposée.

**5. Résultat attendu** — Les trois index corrects affichés dans un Panel.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Random avec Seed = 7 et Number = 3 dans le domaine 0 à 19.
2. Arrondir les valeurs avec Round pour obtenir des index entiers.
3. Poser List Item ou Cull Index pour marquer les coffres correspondants.
4. Afficher les index dans un Panel.

**7. Pièges fréquents**

- Changer la graine : le résultat ne correspond plus à l'attendu.
- Random produit des décimales : sans arrondi les index sont invalides.

**8. Variantes et extensions**

- Récompense de rareté variable.
- Coffre à ouvrir en résolvant une énigme.

**9. Mise en œuvre dans Magpie** — La graine du Random est figée dans le fichier d'exercice : le résultat est donc déterministe et vérifiable, tout en donnant à l'apprenant l'impression d'un tirage.

**10. Barème** — 3 points, 1 par coffre correctement identifié.

#### G-11 — Les mots croisés des composants

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G2 · Exploration et découverte |
| **Réf. référentiel** | REF-057, REF-058 |
| **Niveau** | Débutant |
| **Durée cible** | 15 min |
| **Prérequis** | A-27, A-28 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 10 composants |
| **Gamification associée** | Mots croisés et grille de lettres |
| **Statut de production** | À produire |

**1. Compétence visée** — Consolider le vocabulaire des composants natifs par un jeu de lettres.

**2. Composants mobilisés** — Text Split, Concatenate, List Item, Panel, Text Tag 3D

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Complète la grille de mots croisés dessinée sur le canvas. Chaque définition renvoie au nom anglais d'un composant natif. Assemble ensuite les lettres des cases grisées pour former le mot final.

**4. Données de départ fournies** — Une grille dessinée en Text Tag 3D et une liste de définitions en Scribble.

**5. Résultat attendu** — Le mot final correctement reconstitué.

**6. Zone CORRIGÉ — explication étape par étape**

1. Résoudre chaque définition : par exemple « éclate une liste en branches » donne GRAFT.
2. Saisir chaque réponse dans le Panel correspondant.
3. Extraire les lettres des cases grisées avec List Item aux index indiqués.
4. Assembler avec Concatenate et soumettre le mot final.

**7. Pièges fréquents**

- Répondre en français alors que les noms de composants sont en anglais.
- Index de cases grisées comptés à partir de 1.

**8. Variantes et extensions**

- Grille thématique par domaine du référentiel.
- Version mots mêlés.

**9. Mise en œuvre dans Magpie** — La grille est produite par un cluster fourni. Magpie valide uniquement le mot final, ce qui rend la correction robuste tout en obligeant à résoudre l'ensemble de la grille.

**10. Barème** — 1 point par définition, 3 points pour le mot final.

#### G-12 — Le memory des composants

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G2 · Exploration et découverte |
| **Réf. référentiel** | REF-047, REF-051, REF-049 |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | A-20 |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | Memory et appariement de paires |
| **Statut de production** | À produire |

**1. Compétence visée** — Associer chaque composant à son effet sur les données, par appariement.

**2. Composants mobilisés** — Weave, Cull Pattern, Param Viewer, Panel, Text Tag 3D

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Douze cartes affichent d'un côté un nom de composant, de l'autre une structure de données avant/après. Reconstitue les six paires en indiquant les couples d'index.

**4. Données de départ fournies** — Douze cartes numérotées et douze structures de données affichées.

**5. Résultat attendu** — Six paires correctement appariées.

**6. Zone CORRIGÉ — explication étape par étape**

1. Analyser chaque structure avec le Param Viewer fourni.
2. Identifier l'opération réalisée entre l'état avant et l'état après.
3. Associer cette opération au nom de composant correspondant.
4. Saisir les six couples dans le Panel de réponse, index le plus petit en premier.

**7. Pièges fréquents**

- Confondre Graft et Simplify sur la carte 5.
- Saisir les couples dans un ordre interne inversé.

**8. Variantes et extensions**

- Memory chronométré.
- Memory à trois cartes par famille (nom, icône, effet).

**9. Mise en œuvre dans Magpie** — La réponse attendue est une liste de six couples d'entiers. Magpie valide en mode SetEquality sur les couples normalisés (index le plus petit en premier), l'ordre des paires étant indifférent.

**10. Barème** — 6 points, 1 par paire.

#### G-13 — La machine à sous des motifs

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G2 · Exploration et découverte |
| **Réf. référentiel** | REF-045, REF-068 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 15 min |
| **Prérequis** | A-14, B-03 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 12 composants |
| **Gamification associée** | Machine à sous et alignement de motifs |
| **Statut de production** | À produire |

**1. Compétence visée** — Comprendre la logique des motifs cycliques par une mécanique de rouleaux.

**2. Composants mobilisés** — Cull Pattern, Shift List, Series, Rectangular Array, Colour Swatch

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Trois rouleaux affichent chacun une séquence de 8 motifs. Trouve les trois valeurs de décalage qui alignent trois motifs identiques sur la ligne centrale.

**4. Données de départ fournies** — Trois listes de 8 motifs et trois sliders de décalage.

**5. Résultat attendu** — Trois motifs identiques alignés et les trois décalages soumis.

**6. Zone CORRIGÉ — explication étape par étape**

1. Lire les trois séquences dans les Panels fournis.
2. Repérer un motif présent dans les trois séquences.
3. Calculer pour chaque rouleau le décalage amenant ce motif en position centrale.
4. Régler les trois sliders et soumettre le triplet.

**7. Pièges fréquents**

- Shift List sans Wrap : les positions extrêmes deviennent inaccessibles.
- Motif présent dans deux séquences seulement.

**8. Variantes et extensions**

- Rouleaux animés par un Timer.
- Motifs géométriques plutôt que textuels.

**9. Mise en œuvre dans Magpie** — Magpie valide sur le triplet de décalages. Un seul triplet est correct dans le domaine 0 à 7, ce qui rend la solution unique et vérifiable.

**10. Barème** — 3 points, validation sur le triplet exact.

### G3 · Manipulation et adresse

*3 exercices — G-14, G-15, G-16*

#### G-14 — Le puzzle de câblage

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G3 · Manipulation et adresse |
| **Réf. référentiel** | REF-027, REF-048 |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | A-01, A-19 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 6 composants |
| **Gamification associée** | Puzzle de connexion à ports contraints |
| **Statut de production** | À produire |

**1. Compétence visée** — Travailler la lecture des entrées et sorties d'un composant.

**2. Composants mobilisés** — Construct Point, Construct Plane, Circle, Rotate, Deconstruct

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Six composants sont posés sur le canvas, tous les câbles ont été supprimés. Rétablis le câblage pour reproduire la géométrie affichée en filigrane, sans ajouter ni supprimer aucun composant.

**4. Données de départ fournies** — Six composants dispersés, aucun câble, une géométrie cible en filigrane.

**5. Résultat attendu** — La géométrie cible reproduite avec exactement six composants.

**6. Zone CORRIGÉ — explication étape par étape**

1. Identifier le composant terminal produisant la géométrie visible.
2. Remonter la chaîne : quelle entrée attend un plan, laquelle attend un nombre.
3. Câbler de l'amont vers l'aval en contrôlant le type attendu à chaque port.
4. Vérifier la superposition avec le filigrane.

**7. Pièges fréquents**

- Brancher un point sur une entrée attendant un plan : conversion silencieuse en plan XY à cette origine.
- Ajouter un composant pour contourner une difficulté : le contrôle du nombre échoue.

**8. Variantes et extensions**

- Puzzle à 12 composants.
- Version où deux câblages différents donnent le même résultat.

**9. Mise en œuvre dans Magpie** — Magpie contrôle simultanément la géométrie produite et le nombre de composants, ce dernier devant rester strictement égal à six. Toute aide par ajout de composant est ainsi éliminée.

**10. Barème** — 1 point pour la géométrie, 1 point pour le respect du nombre de composants.

#### G-15 — Le dessin à compléter

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G3 · Manipulation et adresse |
| **Réf. référentiel** | REF-063, REF-067 |
| **Niveau** | Débutant |
| **Durée cible** | 14 min |
| **Prérequis** | A-34, A-38 |
| **Mode de validation** | GeometryTolerance — tolérance 0,05 mm |
| **Solution de référence** | 6 composants |
| **Gamification associée** | Silhouette à compléter et symétrie |
| **Statut de production** | À produire |

**1. Compétence visée** — Reconstituer une figure par déduction géométrique.

**2. Composants mobilisés** — Mirror, Rotate, Polygon, Arc, Join Curves

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> La moitié gauche du motif est dessinée. Complète la moitié droite pour obtenir une figure parfaitement symétrique, puis referme le contour.

**4. Données de départ fournies** — Une demi-figure internalisée et un axe de symétrie.

**5. Résultat attendu** — Le contour fermé complet et symétrique.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser Mirror avec le plan de symétrie fourni.
2. Vérifier que la copie miroir se raccorde exactement à l'original.
3. Poser Join Curves pour souder les deux moitiés.
4. Contrôler la fermeture avec un composant de test de courbe fermée.

**7. Pièges fréquents**

- Plan de symétrie décalé : un décrochement apparaît à la jonction.
- Join Curves sans tolérance suffisante : le contour reste ouvert.

**8. Variantes et extensions**

- Symétrie centrale plutôt qu'axiale.
- Figure à compléter par rotation d'ordre 5.

**9. Mise en œuvre dans Magpie** — Magpie valide en GeometryTolerance sur le contour fermé résultant. La fermeture est vérifiée séparément par un booléen renvoyé au plugin.

**10. Barème** — 1 point pour la symétrie, 1 point pour la fermeture.

#### G-16 — La chasse au trésor

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G3 · Manipulation et adresse |
| **Réf. référentiel** | REF-055, REF-101 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 18 min |
| **Prérequis** | A-09, A-45 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | Chasse au trésor et indices successifs |
| **Statut de production** | À produire |

**1. Compétence visée** — Rechercher une donnée anormale dans un ensemble volumineux.

**2. Composants mobilisés** — Null Item, Bounds, Sort List, Distance, Dispatch, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Parmi 500 points, un seul est aberrant : il est hors du volume de référence. Trouve son index. Trois indices sont disponibles, chacun coûte 2 points.

**4. Données de départ fournies** — 500 points internalisés et un volume de référence.

**5. Résultat attendu** — L'index du point aberrant.

**6. Zone CORRIGÉ — explication étape par étape**

1. Poser un test d'inclusion des points dans le volume de référence.
2. Récupérer la liste de booléens résultante.
3. Poser Gate Not puis un composant d'index des True pour localiser le point hors volume.
4. Afficher son index dans le Panel de réponse.

**7. Pièges fréquents**

- Chercher visuellement dans la vue Rhino sur 500 points.
- Confondre l'index dans la liste filtrée et l'index dans la liste d'origine.

**8. Variantes et extensions**

- Plusieurs points aberrants.
- Indice révélant une zone au lieu du point.

**9. Mise en œuvre dans Magpie** — Les trois indices sont fournis dans des groupes repliés du canvas, dont l'ouverture est comptabilisée comme une tentative supplémentaire par Magpie, ce qui réduit le score final.

**10. Barème** — 10 points, moins 2 points par indice consulté.

### G4 · Connaissance et mémorisation

*4 exercices — G-17, G-18, G-19, G-20*

#### G-17 — Le quiz éclair

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G4 · Connaissance et mémorisation |
| **Réf. référentiel** | REF-040, REF-053, REF-056 |
| **Niveau** | Débutant |
| **Durée cible** | 8 min |
| **Prérequis** | A-06, A-24, A-26 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 10 composants |
| **Gamification associée** | QCM chronométré à réponse unique |
| **Statut de production** | À produire |

**1. Compétence visée** — Vérifier des connaissances conceptuelles non mesurables par comparaison de géométrie.

**2. Composants mobilisés** — Value List, Panel, Boolean Toggle

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Dix questions à choix multiple sur les comportements implicites de Grasshopper. Trente secondes par question, une seule réponse possible.

**4. Données de départ fournies** — Dix Value List pré-configurées.

**5. Résultat attendu** — Les dix bonnes réponses sélectionnées.

**6. Zone CORRIGÉ — explication étape par étape**

1. Lire chaque question dans le Scribble associé.
2. Sélectionner la réponse dans la Value List correspondante.
3. Ne pas modifier l'ordre des questions.
4. Soumettre l'ensemble en une seule validation.

**7. Pièges fréquents**

- Value List laissée sur sa valeur par défaut, comptée comme réponse.
- Passer trop de temps sur une question et perdre le bonus de temps.

**8. Variantes et extensions**

- Banque de questions tirées aléatoirement.
- Questions illustrées par une capture de canvas.

**9. Mise en œuvre dans Magpie** — Chaque question est une Value List dont la valeur sélectionnée est comparée à la valeur attendue. Ce format couvre les notions conceptuelles du référentiel signalées en mode Conceptuel (QCM).

**10. Barème** — 10 points, 1 par bonne réponse.

#### G-18 — Vrai ou faux à élimination

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G4 · Connaissance et mémorisation |
| **Réf. référentiel** | REF-040, REF-041, REF-059 |
| **Niveau** | Débutant |
| **Durée cible** | 10 min |
| **Prérequis** | A-06, A-07, A-29 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 15 composants |
| **Gamification associée** | Vrai/faux à élimination progressive |
| **Statut de production** | À produire |

**1. Compétence visée** — Lever les idées reçues sur les conversions et les comparaisons.

**2. Composants mobilisés** — Boolean Toggle, Panel, Gate And

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Quinze affirmations sur les types et les conversions. Réponds par vrai ou faux. Une erreur élimine l'affirmation et ses deux suivantes du décompte : mieux vaut réfléchir que deviner.

**4. Données de départ fournies** — Quinze Boolean Toggle et quinze affirmations en Scribble.

**5. Résultat attendu** — Les quinze réponses correctes.

**6. Zone CORRIGÉ — explication étape par étape**

1. Traiter chaque affirmation en la vérifiant mentalement sur un cas concret.
2. En cas de doute, tester rapidement dans un coin du canvas.
3. Positionner les toggles.
4. Soumettre l'ensemble.

**7. Pièges fréquents**

- Répondre au hasard sur les affirmations portant sur l'arrondi.
- Confondre valeur nulle et valeur zéro à l'affirmation 8.

**8. Variantes et extensions**

- Affirmations tirées d'erreurs réellement commises par les apprenants.
- Mode duel à deux.

**9. Mise en œuvre dans Magpie** — Magpie compare la liste des quinze booléens à la liste attendue. La règle d'élimination est appliquée au calcul du score, pas à la validation, qui reste à 15/15.

**10. Barème** — 15 points, avec pénalité d'élimination sur le score.

#### G-19 — Le composant mystère

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G4 · Connaissance et mémorisation |
| **Réf. référentiel** | REF-028, REF-042 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 12 min |
| **Prérequis** | A-05, A-11 |
| **Mode de validation** | ExactOrderedList — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | Devinette par observation du comportement (boîte noire) |
| **Statut de production** | À produire |

**1. Compétence visée** — Identifier un composant par son comportement plutôt que par son nom.

**2. Composants mobilisés** — Cluster, Panel, Param Viewer, Value List

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Quatre clusters anonymes transforment les données. Observe leurs entrées et sorties, puis identifie le composant natif que chacun reproduit.

**4. Données de départ fournies** — Quatre clusters verrouillés et des jeux de données de test.

**5. Résultat attendu** — Les quatre noms de composants correctement identifiés.

**6. Zone CORRIGÉ — explication étape par étape**

1. Alimenter chaque cluster avec une liste simple de 1 à 5 et observer la sortie.
2. Répéter avec une liste contenant des doublons puis avec un arbre à deux branches.
3. Déduire la transformation opérée à partir des trois essais.
4. Sélectionner le nom dans la Value List correspondante.

**7. Pièges fréquents**

- Conclure après un seul jeu de test : plusieurs composants ont le même effet sur une liste simple.
- Ne pas tester le comportement sur un arbre, seul discriminant entre Flatten et Simplify.

**8. Variantes et extensions**

- Clusters combinant deux composants.
- Épreuve chronométrée.

**9. Mise en œuvre dans Magpie** — Chaque cluster est protégé par mot de passe pour empêcher son ouverture. La réponse est saisie via quatre Value List proposant chacune huit candidats.

**10. Barème** — 4 points, 1 par cluster identifié.

#### G-20 — La chasse aux bugs

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G4 · Connaissance et mémorisation |
| **Réf. référentiel** | REF-041, REF-053, REF-055 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | A-07, A-09, A-24 |
| **Mode de validation** | SetEquality — tolérance 0,1 mm |
| **Solution de référence** | 30 composants |
| **Gamification associée** | Débogage d'une définition volontairement fautive |
| **Statut de production** | À produire |

**1. Compétence visée** — Développer le réflexe de diagnostic sur une définition qui ne produit pas le résultat attendu.

**2. Composants mobilisés** — Param Viewer, Panel, List Length, Null Item, Profiler

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Cette définition devrait produire 24 modules, elle n'en produit que 6. Trois défauts se cachent dans le graphe. Identifie-les et corrige la définition sans en changer la structure générale.

**4. Données de départ fournies** — Une définition fautive de 30 composants.

**5. Résultat attendu** — 24 modules produits et les trois défauts corrigés.

**6. Zone CORRIGÉ — explication étape par étape**

1. Brancher un Param Viewer en plusieurs points de la chaîne pour localiser la rupture.
2. Défaut 1 : une correspondance en Shortest List tronque une liste de 24 à 6.
3. Défaut 2 : un Flatten mal placé écrase la structure d'arbre attendue.
4. Défaut 3 : une valeur nulle en entrée invalide quatre éléments.
5. Corriger les trois points et vérifier le compte final.

**7. Pièges fréquents**

- Corriger le symptôme en aval plutôt que la cause en amont.
- Supprimer le composant fautif au lieu de le régler : le contrôle du nombre échoue.

**8. Variantes et extensions**

- Cinq défauts dont deux sans effet visible.
- Définition fournie par un autre apprenant.

**9. Mise en œuvre dans Magpie** — Magpie valide sur le résultat géométrique et contrôle que le nombre de composants reste inchangé, ce qui interdit de reconstruire la définition plutôt que de la corriger.

**10. Barème** — 3 points, 1 par défaut corrigé.

### G5 · Performance et compétition

*3 exercices — G-21, G-22, G-23*

#### G-21 — Le golf de composants

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G5 · Performance et compétition |
| **Réf. référentiel** | REF-068, REF-043, REF-046 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | A-16, A-39 |
| **Mode de validation** | GeometryTolerance — tolérance 0,1 mm |
| **Solution de référence** | 7 composants |
| **Gamification associée** | Contrainte de score minimal (code golf) |
| **Statut de production** | À produire |

**1. Compétence visée** — Chercher la solution la plus économe, exercice d'élégance algorithmique.

**2. Composants mobilisés** — Series, Shift List, Line, Rectangular Array, Graft

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Produis la géométrie cible avec le moins de composants possible. Le par du trou est fixé à 7 composants. Sliders et Panels comptent.

**4. Données de départ fournies** — Une géométrie cible en filigrane.

**5. Résultat attendu** — La géométrie reproduite, idéalement en 7 composants ou moins.

**6. Zone CORRIGÉ — explication étape par étape**

1. Analyser la cible pour identifier la répétition sous-jacente.
2. Préférer un composant de réseau à une suite de transformations.
3. Utiliser les expressions dans les entrées pour éviter des composants de calcul.
4. Compter les composants et chercher à descendre sous le par.

**7. Pièges fréquents**

- Optimiser au détriment de la lisibilité au point de rendre la solution invérifiable.
- Oublier que les sliders comptent dans le total.

**8. Variantes et extensions**

- Parcours de 9 trous de difficulté croissante.
- Classement de la promotion sur chaque trou.

**9. Mise en œuvre dans Magpie** — Magpie utilise directement la métrique du nombre de composants et l'écart au chemin attendu. Le score de golf est renvoyé comme métrique principale, la validation géométrique restant obligatoire.

**10. Barème** — Par 7 : 3 points au par, 5 points sous le par, 1 point au-dessus.

#### G-22 — Le boss de fin de chapitre

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G5 · Performance et compétition |
| **Réf. référentiel** | REF-047, REF-051, REF-068, REF-079 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 45 min |
| **Prérequis** | Tous les exercices du chapitre Données |
| **Mode de validation** | ExactOrderedList — tolérance 0,1 % |
| **Solution de référence** | 32 composants |
| **Gamification associée** | Affrontement final de chapitre (boss fight) à phases successives |
| **Statut de production** | À produire |

**1. Compétence visée** — Éprouver en une seule tâche l'ensemble des notions du chapitre Données et logique.

**2. Composants mobilisés** — Series, Sort List, Cull Pattern, Graft, Path Mapper, Gate And, Dispatch, Mass Addition

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Trois phases s'enchaînent sans validation intermédiaire. Phase 1 : structurer les données en arbre. Phase 2 : filtrer selon deux conditions combinées. Phase 3 : produire le tableau de synthèse. Toute erreur en phase 3 impose de reprendre depuis la phase 1.

**4. Données de départ fournies** — Un jeu de 240 valeurs et un modèle de tableau de sortie.

**5. Résultat attendu** — Le tableau de synthèse exact.

**6. Zone CORRIGÉ — explication étape par étape**

1. Phase 1 : répartir les 240 valeurs en 12 branches de 20 avec Partition List puis contrôler au Param Viewer.
2. Phase 2 : construire les deux conditions et les combiner avec Gate And.
3. Phase 2 : filtrer chaque branche avec Dispatch en conservant la structure d'arbre.
4. Phase 3 : calculer par branche le compte, la somme et la moyenne avec Mass Addition et Average.
5. Phase 3 : assembler le tableau avec Merge dans l'ordre imposé et soumettre.

**7. Pièges fréquents**

- Aplatir l'arbre en phase 2 : les statistiques de phase 3 portent alors sur l'ensemble et non par branche.
- Ordre des colonnes du tableau non respecté.
- Moyenne calculée sur la liste filtrée mais compte calculé sur la liste complète.

**8. Variantes et extensions**

- Boss de chapitre pour chaque domaine du référentiel.
- Version chronométrée avec classement.

**9. Mise en œuvre dans Magpie** — Le boss est un exercice unique agrégeant trois sous-critères, tous nécessaires à la validation. Le seuil de réussite est fixé à 100 %, contrairement aux exercices ordinaires du chapitre.

**10. Barème** — 10 points, validation à 100 % uniquement.

#### G-23 — Le duel

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G5 · Performance et compétition |
| **Réf. référentiel** | REF-082, REF-044 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | B-12 |
| **Mode de validation** | ExactOrderedList — tolérance 0,5 % |
| **Solution de référence** | 18 composants |
| **Gamification associée** | Duel et classement entre apprenants (leaderboard) |
| **Statut de production** | À produire |

**1. Compétence visée** — Confronter deux approches d'un même problème et en mesurer les écarts.

**2. Composants mobilisés** — Sort List, Mass Addition, Length, Panel, Profiler

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Même énoncé pour tous : produire la nomenclature triée de l'assemblage. Trois critères départagent les participants : justesse, nombre de composants, temps d'exécution de la définition.

**4. Données de départ fournies** — Un assemblage identique pour tous les participants.

**5. Résultat attendu** — La nomenclature exacte, avec les trois métriques relevées.

**6. Zone CORRIGÉ — explication étape par étape**

1. Produire la nomenclature comme dans l'exercice B-12.
2. Relever le nombre de composants dans le panneau de métriques.
3. Activer le Profiler pour relever le temps de calcul de la définition.
4. Soumettre et exporter le résultat.

**7. Pièges fréquents**

- Optimiser le temps de calcul au détriment de la justesse.
- Comparer des temps mesurés sur des machines différentes.

**8. Variantes et extensions**

- Duel en direct pendant une session de formation.
- Classement par thématique du référentiel.

**9. Mise en œuvre dans Magpie** — Magpie remonte les trois métriques déjà collectées par le plugin. Le classement est établi hors de l'outil, à partir des fichiers de résultats exportés en fin de parcours.

**10. Barème** — Classement combiné sur les trois critères, validation à la justesse seule.

### G6 · Sensations et immersion

*5 exercices — G-24, G-25, G-26, G-27, G-28*

#### G-24 — Le retour sonore

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G6 · Sensations et immersion |
| **Réf. référentiel** | REF-027, REF-061 |
| **Niveau** | Débutant |
| **Durée cible** | 10 min |
| **Prérequis** | A-31 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | Sons et signaux audio contextuels |
| **Statut de production** | À produire |

**1. Compétence visée** — Associer un retour immédiat perceptible à chaque action correcte ou fautive.

**2. Composants mobilisés** — Boolean Toggle, Stream Filter, Panel, Play Sound (Human)

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Câble la définition de sorte qu'un son de validation retentisse quand la condition est vraie et un son d'erreur quand elle est fausse. Puis résous l'énigme logique qui déclenche le son de victoire.

**4. Données de départ fournies** — Deux fichiers audio référencés et un cluster de logique incomplet.

**5. Résultat attendu** — Les sons correctement déclenchés et l'énigme résolue.

**6. Zone CORRIGÉ — explication étape par étape**

1. Brancher le booléen de condition sur un Stream Filter à deux entrées sonores.
2. Vérifier l'alternance en basculant manuellement le toggle.
3. Résoudre l'énigme logique du cluster : trouver la combinaison de trois booléens rendant la sortie vraie.
4. Soumettre la combinaison.

**7. Pièges fréquents**

- Son déclenché à chaque recalcul et non au seul changement d'état.
- Chemin de fichier audio absolu, non transportable d'un poste à l'autre.

**8. Variantes et extensions**

- Palette sonore par thématique.
- Son de compte à rebours dans les dix dernières secondes.

**9. Mise en œuvre dans Magpie** — Le retour audio s'appuie sur un composant de lecture sonore du plugin Human, ou à défaut sur un composant de son ajouté au plugin Magpie. La validation Magpie porte sur la résolution de l'énigme, le son restant un retour d'expérience.

**10. Barème** — 2 points : 1 pour le câblage sonore, 1 pour l'énigme.

#### G-25 — L'animation de la solution

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G6 · Sensations et immersion |
| **Réf. référentiel** | REF-090, REF-093, REF-067 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | A-37, B-05 |
| **Mode de validation** | SetEquality — tolérance 0,1 mm |
| **Solution de référence** | 14 composants |
| **Gamification associée** | Animation temporelle et révélation progressive |
| **Statut de production** | À produire |

**1. Compétence visée** — Rendre visible le déroulement d'un algorithme plutôt que son seul résultat.

**2. Composants mobilisés** — Timer, Series, Sub List, Move, Custom Preview, Gradient

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Anime la construction de la structure : les 40 barres doivent apparaître une par une en trois secondes, puis la structure entière change de couleur. Le pilotage se fait par un unique slider de 0 à 1.

**4. Données de départ fournies** — Une structure de 40 barres déjà modélisée.

**5. Résultat attendu** — L'animation pilotée par un slider unique, complète à 1.

**6. Zone CORRIGÉ — explication étape par étape**

1. Multiplier la valeur du slider par 40 et arrondir pour obtenir le nombre de barres visibles.
2. Construire le domaine 0 à ce nombre avec Construct Domain.
3. Poser Sub List pour ne conserver que les barres de ce domaine.
4. Poser Custom Preview avec un Gradient piloté par le même slider.
5. Vérifier les deux états de contrôle, à 0,5 puis à 1.

**7. Pièges fréquents**

- Sub List sur un domaine non entier : le nombre de barres devient imprévisible.
- Timer branché en permanence : la définition recalcule sans arrêt et devient inutilisable.

**8. Variantes et extensions**

- Animation par vagues plutôt que séquentielle.
- Export de l'animation en séquence d'images.

**9. Mise en œuvre dans Magpie** — L'exercice est validé sur l'état final (slider à 1, 40 barres visibles) et sur un état intermédiaire imposé (slider à 0,5, 20 barres visibles), ce qui garantit que l'animation est bien progressive.

**10. Barème** — 2 points : 1 pour l'état final, 1 pour l'état intermédiaire.

#### G-26 — Le retour visuel immédiat

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G6 · Sensations et immersion |
| **Réf. référentiel** | REF-026, REF-059 |
| **Niveau** | Débutant |
| **Durée cible** | 12 min |
| **Prérequis** | A-29 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 12 composants |
| **Gamification associée** | Retour visuel par couleur conditionnelle |
| **Statut de production** | À produire |

**1. Compétence visée** — Colorer le résultat en fonction de sa conformité, pour un diagnostic instantané.

**2. Composants mobilisés** — Custom Preview, Colour Swatch, Stream Filter, Larger Than, Gradient

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Vingt pièces doivent mesurer entre 400 et 900 mm. Colore en vert celles qui sont conformes, en rouge les autres, et affiche le nombre de non-conformes.

**4. Données de départ fournies** — Vingt pièces internalisées de longueurs variées.

**5. Résultat attendu** — Coloration correcte et compte des non-conformes.

**6. Zone CORRIGÉ — explication étape par étape**

1. Mesurer les longueurs avec Length.
2. Construire le test de conformité avec deux comparaisons et un Gate And.
3. Séparer les pièces avec Dispatch selon ce booléen.
4. Poser deux Custom Preview avec deux Colour Swatch distincts.
5. Compter les non-conformes avec Mass Addition sur le booléen inversé.

**7. Pièges fréquents**

- Custom Preview appliqué à la liste complète : toutes les pièces prennent la même couleur.
- Aperçu du composant amont resté actif : les deux couleurs se superposent.

**8. Variantes et extensions**

- Dégradé continu plutôt que deux couleurs.
- Coloration par famille de matériau.

**9. Mise en œuvre dans Magpie** — La validation Magpie porte sur le nombre de non-conformes. La coloration est un retour d'expérience évalué visuellement par le formateur lors de la revue de l'exercice.

**10. Barème** — 2 points : 1 pour la coloration, 1 pour le compte.

#### G-27 — La savane paramétrique

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G6 · Sensations et immersion |
| **Réf. référentiel** | REF-063, REF-067, REF-068 |
| **Niveau** | Débutant |
| **Durée cible** | 20 min |
| **Prérequis** | A-34, A-39 |
| **Mode de validation** | GeometryTolerance — tolérance 1 mm |
| **Solution de référence** | 14 composants |
| **Gamification associée** | Narration et univers thématique (scénarisation) |
| **Statut de production** | À produire |

**1. Compétence visée** — Inscrire une série d'exercices dans un fil narratif cohérent avec l'identité de la marque.

**2. Composants mobilisés** — Polygon, Circle, Rectangular Array, Move, Custom Preview, Text Tag 3D

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Chapitre 1 de la savane : construis l'abreuvoir circulaire, puis dispose la harde de 12 animaux en trame autour du point d'eau, chacun orienté vers le centre.

**4. Données de départ fournies** — Un décor de fond et un module d'animal simplifié.

**5. Résultat attendu** — L'abreuvoir et les 12 modules orientés vers le centre.

**6. Zone CORRIGÉ — explication étape par étape**

1. Construire l'abreuvoir par un Circle centré à l'origine.
2. Répartir 12 positions par Polar Array ou Divide Curve sur un cercle plus grand.
3. Construire pour chaque position le vecteur pointant vers le centre avec Vector 2Pt.
4. Orienter chaque module avec Orient ou Rotate selon l'angle calculé.
5. Vérifier que tous les modules regardent bien le centre.

**7. Pièges fréquents**

- Vecteur construit du centre vers la position : les animaux tournent le dos à l'eau.
- Angle calculé sans Atan2 : l'orientation est fausse sur deux quadrants.

**8. Variantes et extensions**

- Chapitres successifs formant un parcours complet.
- Personnages débloqués par les badges.

**9. Mise en œuvre dans Magpie** — La narration est portée par les Scribbles et le décor du canvas. Magpie valide la géométrie produite ; le fil narratif se déploie sur l'ensemble du parcours via les consignes successives.

**10. Barème** — 2 points : 1 pour la disposition, 1 pour l'orientation.

#### G-28 — L'avatar paramétrique

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G6 · Sensations et immersion |
| **Réf. référentiel** | REF-067, REF-106, REF-061 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 22 min |
| **Prérequis** | B-16, A-31 |
| **Mode de validation** | SingleValue — tolérance 0 |
| **Solution de référence** | 20 composants |
| **Gamification associée** | Avatar et personnalisation persistante |
| **Statut de production** | À produire |

**1. Compétence visée** — Faire construire à l'apprenant un objet personnel qu'il retrouvera tout au long du parcours.

**2. Composants mobilisés** — Value List, Stream Filter, Polygon, Circle, Colour Swatch, Custom Preview

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Compose ton avatar : 3 formes de corps, 4 motifs, 6 couleurs. Ton avatar doit rester valide dans les 72 combinaisons possibles et son code de configuration doit s'afficher dans le Panel.

**4. Données de départ fournies** — Trois Value List et les bibliothèques de formes et de motifs.

**5. Résultat attendu** — L'avatar composé et son code de configuration affiché.

**6. Zone CORRIGÉ — explication étape par étape**

1. Sélectionner la forme active avec Stream Filter piloté par la première Value List.
2. Appliquer le motif choisi par la même mécanique.
3. Appliquer la couleur avec un Colour Swatch sélectionné par la troisième Value List.
4. Composer le code avec Concatenate à partir des trois index.
5. Balayer les 72 combinaisons pour vérifier qu'aucune ne produit d'erreur.

**7. Pièges fréquents**

- Value List renvoyant du texte plutôt qu'un entier : Stream Filter échoue.
- Combinaisons non testées : certaines produisent une géométrie invalide.

**8. Variantes et extensions**

- Avatar évoluant avec le niveau atteint.
- Avatar exporté en image pour le certificat.

**9. Mise en œuvre dans Magpie** — Le code de configuration (par exemple B2-M3-C5) est la donnée validée par Magpie. Il est conservé dans le profil de l'apprenant et repris sur le certificat.

**10. Barème** — 2 points : 1 pour la robustesse, 1 pour le code de configuration.

### G7 · Régularité et communauté

*4 exercices — G-29, G-30, G-31, G-32*

#### G-29 — Le défi du jour

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G7 · Régularité et communauté |
| **Réf. référentiel** | REF-047, REF-079 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 10 min |
| **Prérequis** | A-13, A-47 |
| **Mode de validation** | NumericTolerance — tolérance 0,1 % |
| **Solution de référence** | 10 composants |
| **Gamification associée** | Défi quotidien à énoncé variable |
| **Statut de production** | À produire |

**1. Compétence visée** — Installer une habitude de pratique par une tâche courte et renouvelée.

**2. Composants mobilisés** — Random, Series, Sort List, Length, Panel

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Un défi court, différent chaque jour, tiré d'une banque de 30 micro-tâches. Celui du jour : trie les pièces par longueur et donne la longueur médiane.

**4. Données de départ fournies** — Une banque de micro-tâches et un jeu de données du jour.

**5. Résultat attendu** — La réponse au défi du jour.

**6. Zone CORRIGÉ — explication étape par étape**

1. Lire l'énoncé du jour affiché dans le Scribble.
2. Mesurer les longueurs avec Length.
3. Trier avec Sort List.
4. Extraire l'élément médian avec List Length, une division par 2 et List Item.
5. Soumettre la valeur.

**7. Pièges fréquents**

- Confondre médiane et moyenne.
- Liste de taille paire : la médiane est la moyenne des deux valeurs centrales.

**8. Variantes et extensions**

- Série de sept jours donnant un badge hebdomadaire.
- Défi collectif avec objectif commun.

**9. Mise en œuvre dans Magpie** — Le fichier JSON de l'exercice contient les 30 variantes. Le plugin sélectionne la variante à partir de la date du poste, ce qui rend le défi identique pour tous les apprenants d'une même journée.

**10. Barème** — 1 point par défi, badge à 7 jours consécutifs.

#### G-30 — Le relais à deux

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G7 · Régularité et communauté |
| **Réf. référentiel** | REF-088, REF-048 |
| **Niveau** | Perfectionnement |
| **Durée cible** | 30 min |
| **Prérequis** | B-05, A-21 |
| **Mode de validation** | SetEquality — tolérance 0,1 mm |
| **Solution de référence** | 30 composants |
| **Gamification associée** | Mode coopératif en relais |
| **Statut de production** | À produire |

**1. Compétence visée** — Travailler la lisibilité et la transmissibilité d'une définition.

**2. Composants mobilisés** — Cluster, Group, Param Viewer, Scribble, Metahopper

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Première moitié : construis la structure de données jusqu'au point de passage marqué, en la rendant compréhensible par un tiers. Ton binôme reprendra le fichier pour la seconde moitié sans explication orale.

**4. Données de départ fournies** — Un énoncé en deux parties et un point de passage matérialisé sur le canvas.

**5. Résultat attendu** — La définition complète produite par les deux contributions successives.

**6. Zone CORRIGÉ — explication étape par étape**

1. Construire la première moitié en nommant explicitement toutes les sorties.
2. Regrouper les blocs fonctionnels avec Group et les titrer.
3. Documenter les hypothèses dans des Scribbles.
4. Transmettre le fichier au binôme.
5. Le binôme complète sans poser de question et signale les points restés obscurs.

**7. Pièges fréquents**

- Nommage par défaut conservé : le binôme perd du temps à décoder.
- Structure d'arbre non documentée au point de passage.

**8. Variantes et extensions**

- Relais à quatre sur un projet complet.
- Évaluation croisée de la lisibilité.

**9. Mise en œuvre dans Magpie** — L'exercice est livré en deux fichiers JSON enchaînés. Le fichier intermédiaire produit par le premier apprenant sert de point de départ au second, ce qui suppose la fonction d'import de composants de départ déjà présente dans Magpie.

**10. Barème** — 4 points : 2 pour le résultat, 2 pour la lisibilité évaluée par le binôme.

#### G-31 — L'arbre de compétences

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G7 · Régularité et communauté |
| **Réf. référentiel** | REF-048, REF-051 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 15 min |
| **Prérequis** | A-19, A-22 |
| **Mode de validation** | SetEquality — tolérance 1 mm |
| **Solution de référence** | 22 composants |
| **Gamification associée** | Carte de progression et arbre de compétences (skill tree) |
| **Statut de production** | À produire |

**1. Compétence visée** — Donner à l'apprenant une vue d'ensemble de son avancement et des chemins possibles.

**2. Composants mobilisés** — Tree Statistics, Param Viewer, Text Tag 3D, Line, Circle, Custom Preview

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Construis la représentation graphique de ton propre arbre de compétences à partir de la liste des exercices validés : un nœud par notion, une branche par domaine, un code couleur par niveau atteint.

**4. Données de départ fournies** — La liste des exercices validés exportée par Magpie et la structure du référentiel.

**5. Résultat attendu** — L'arbre de compétences dessiné, cohérent avec les données d'entrée.

**6. Zone CORRIGÉ — explication étape par étape**

1. Lire le fichier de résultats et en extraire les identifiants d'exercices validés.
2. Rattacher chaque identifiant à son domaine et à sa catégorie via la table du référentiel.
3. Construire l'arbre de données correspondant avec Entwine puis Path Mapper.
4. Placer un nœud par notion sur un cercle par domaine.
5. Relier les nœuds à leur domaine avec Line et colorer selon le niveau atteint.
6. Étiqueter chaque nœud avec Text Tag 3D.

**7. Pièges fréquents**

- Structure d'arbre construite à plat : les domaines se mélangent.
- Nœuds superposés faute d'avoir réparti les angles selon le nombre de notions par domaine.

**8. Variantes et extensions**

- Arbre mis à jour automatiquement après chaque parcours.
- Comparaison avec la moyenne de la promotion.

**9. Mise en œuvre dans Magpie** — Le fichier de résultats exporté en fin de parcours alimente l'exercice. La lecture de ce fichier suppose une fonction d'import de résultats à ajouter au plugin, actuellement absente du prototype.

**10. Barème** — 4 points : 2 pour la structure, 2 pour la lisibilité.

#### G-32 — Les indices payants

| Rubrique | Valeur |
|---|---|
| **Lot** | G — Exercices gamifiés |
| **Thématique** | G7 · Régularité et communauté |
| **Réf. référentiel** | REF-052, REF-049, REF-050 |
| **Niveau** | Intermédiaire |
| **Durée cible** | 20 min |
| **Prérequis** | A-20, A-21, A-23 |
| **Mode de validation** | SetEquality — tolérance 0 |
| **Solution de référence** | 6 composants |
| **Gamification associée** | Économie d'indices à coût décroissant sur le score |
| **Statut de production** | À produire |

**1. Compétence visée** — Responsabiliser l'apprenant sur le recours à l'aide.

**2. Composants mobilisés** — Path Mapper, Graft, Flatten, Simplify, Param Viewer

> Cette liste ne figure pas sur la fiche remise à l'apprenant : nommer l'outil reviendrait à donner la réponse.

**3. Zone SUJET — texte du Scribble**

> Restructure l'arbre fourni pour atteindre la structure cible. Quatre indices sont disponibles, du plus général au plus précis, coûtant respectivement 1, 2, 3 et 4 points sur un total de 12.

**4. Données de départ fournies** — Un arbre source, une structure cible affichée et quatre groupes d'indices repliés.

**5. Résultat attendu** — La structure cible atteinte.

**6. Zone CORRIGÉ — explication étape par étape**

1. Comparer les chemins source et cible dans le Param Viewer.
2. Identifier l'opération nécessaire : ajout de niveau, suppression, permutation.
3. Appliquer Path Mapper avec les masques adaptés.
4. Vérifier la structure obtenue avant de soumettre.

**7. Pièges fréquents**

- Utiliser Flatten puis Graft pour reconstruire : la structure obtenue diffère de la cible.
- Consommer les quatre indices avant d'avoir essayé.

**8. Variantes et extensions**

- Indices sous forme de vidéo courte.
- Indices offerts par une série de bonnes réponses.

**9. Mise en œuvre dans Magpie** — Chaque indice est un groupe du canvas dont l'ouverture est détectée par Magpie comme un événement, décomptée du score final. Le mécanisme réutilise le compteur de tentatives du plugin.

**10. Barème** — 12 points, moins le coût des indices consultés.

---

## 9. Bibliothèque des techniques de gamification

Le lot G met en œuvre **32 techniques**, chacune portée par un exercice dédié. Le tableau ci-dessous sert de bibliothèque de référence : une technique peut être réemployée sur n'importe quel exercice des lots A, B ou C.

| Technique | Exercice porteur | Famille | Ce que le plugin doit fournir | Réemployable sur |
|---|---|---|---|---|
| Score visible et barème explicite (scoreboard) | G-01 — Le tableau des scores | Progression et récompense | Score partiel par sous-critère | Tout exercice à sous-critères |
| Barre de progression et jalons intermédiaires | G-02 — La barre de progression | Progression et récompense | Taux de réussite partiel exposé en cours d'exercice | Exercices en plusieurs formes |
| Compte à rebours et mode time attack | G-03 — Contre la montre | Progression et récompense | Durée cible et compte à rebours affiché | Tout exercice court |
| Système de vies et tentatives limitées | G-04 — Trois vies | Progression et récompense | Limitation du nombre de tentatives et rechargement | Exercices à réponse unique |
| Badges et trophées par compétence | G-05 — La collection de badges | Progression et récompense | Identifiants de badge dans le résultat et sur le certificat | Familles complètes de notions |
| Niveaux et déblocage séquentiel (unlock) | G-06 — Le déblocage progressif | Progression et récompense | Verrouillage du bouton Suivant — déjà présent | Tout parcours |
| Notation par étoiles selon la qualité de la solution | G-07 — Une, deux ou trois étoiles | Progression et récompense | Métriques nombre de composants et robustesse paramétrique | Lots A et B |
| Combo et multiplicateur de série (streak) | G-08 — La série de bonnes réponses | Progression et récompense | État de série conservé entre exercices d'un parcours | Parcours de micro-exercices |
| Récompense cachée (easter egg) | G-09 — Le composant caché | Exploration et découverte | Validation sur chaîne de caractères insensible à la casse | Tout exercice |
| Récompense aléatoire (loot box) | G-10 — Le coffre à butin | Exploration et découverte | Graine aléatoire figée dans le descripteur | Exercices à jeu de données variable |
| Mots croisés et grille de lettres | G-11 — Les mots croisés des composants | Exploration et découverte | Validation sur un mot final unique | Vocabulaire des composants |
| Memory et appariement de paires | G-12 — Le memory des composants | Exploration et découverte | Validation d'une liste de couples en SetEquality | Associations notion / effet |
| Machine à sous et alignement de motifs | G-13 — La machine à sous des motifs | Exploration et découverte | Validation d'un triplet de valeurs | Motifs cycliques |
| Puzzle de connexion à ports contraints | G-14 — Le puzzle de câblage | Manipulation et adresse | Contrôle strict du nombre de composants | Lecture de graphe |
| Silhouette à compléter et symétrie | G-15 — Le dessin à compléter | Manipulation et adresse | Validation géométrique et contrôle de fermeture | Géométrie 2D |
| Chasse au trésor et indices successifs | G-16 — La chasse au trésor | Manipulation et adresse | Décompte des indices consultés comme tentatives | Recherche dans un grand jeu de données |
| QCM chronométré à réponse unique | G-17 — Le quiz éclair | Connaissance et mémorisation | Comparaison de valeurs de Value List | Notions conceptuelles du référentiel |
| Vrai/faux à élimination progressive | G-18 — Vrai ou faux à élimination | Connaissance et mémorisation | Comparaison d'une liste de booléens | Idées reçues et pièges |
| Devinette par observation du comportement (boîte noire) | G-19 — Le composant mystère | Connaissance et mémorisation | Clusters protégés par mot de passe | Comportement des composants |
| Débogage d'une définition volontairement fautive | G-20 — La chasse aux bugs | Connaissance et mémorisation | Contrôle du nombre de composants inchangé | Diagnostic de définition |
| Contrainte de score minimal (code golf) | G-21 — Le golf de composants | Performance et compétition | Métrique du nombre de composants comme score principal | Tout exercice géométrique |
| Affrontement final de chapitre (boss fight) à phases successives | G-22 — Le boss de fin de chapitre | Performance et compétition | Sous-critères tous obligatoires, seuil à 100 % | Fin de chapitre |
| Duel et classement entre apprenants (leaderboard) | G-23 — Le duel | Performance et compétition | Export des trois métriques pour classement externe | Tout exercice |
| Sons et signaux audio contextuels | G-24 — Le retour sonore | Sensations et immersion | Lecture de fichier audio embarqué | Tout exercice |
| Animation temporelle et révélation progressive | G-25 — L'animation de la solution | Sensations et immersion | Validation sur deux états d'un même paramètre | Algorithmes progressifs |
| Retour visuel par couleur conditionnelle | G-26 — Le retour visuel immédiat | Sensations et immersion | Aucun besoin spécifique — retour porté par la définition | Tout exercice de contrôle |
| Narration et univers thématique (scénarisation) | G-27 — La savane paramétrique | Sensations et immersion | Enchaînement scénarisé de parcours | Parcours débutant |
| Avatar et personnalisation persistante | G-28 — L'avatar paramétrique | Sensations et immersion | Conservation d'un code de configuration dans le profil | Configurateurs |
| Défi quotidien à énoncé variable | G-29 — Le défi du jour | Régularité et communauté | Sélection d'une variante par date dans le descripteur | Micro-tâches |
| Mode coopératif en relais | G-30 — Le relais à deux | Régularité et communauté | Import du fichier produit par l'apprenant précédent | Travaux collectifs |
| Carte de progression et arbre de compétences (skill tree) | G-31 — L'arbre de compétences | Régularité et communauté | Import du fichier de résultats — **fonction à créer** | Bilan de parcours |
| Économie d'indices à coût décroissant sur le score | G-32 — Les indices payants | Régularité et communauté | Détection de l'ouverture d'un groupe d'indice | Exercices difficiles |

### 9.1 Règles d'emploi de la gamification

- **Public adulte professionnel** : ton mesuré, humour discret, aucun effet infantilisant.
- **La mécanique ne remplace jamais le contenu** : un exercice gamifié doit rester un exercice valide sans sa couche de jeu.
- **Durée courte** : un test public ne dépasse pas dix questions, afin de préserver l'attention.
- **Le son est toujours désactivable**, et jamais indispensable à la compréhension.
- **Aucune mécanique aléatoire non reproductible** : toute graine est figée dans le descripteur, afin que la correction reste déterministe.
- **Les récompenses sont partageables** : un badge doit pouvoir être publié sur un réseau professionnel.

### 9.2 Techniques identifiées mais non retenues au premier lot

| Technique | Raison |
|---|---|
| Monnaie virtuelle et boutique | Nécessite une gestion de compte persistante, hors périmètre de la V1 |
| Classement mondial en temps réel | Nécessite un serveur, à traiter avec l'extension web |
| Guildes et équipes permanentes | Suppose une communauté déjà constituée |
| Notifications de rappel | Suppose une application mobile ou un envoi de courriels |
| Réalité augmentée | Sans rapport avec le geste métier visé |

---

## 10. Plan de production

### 10.1 Ordre de production recommandé

| Phase | Contenu | Volume | Condition de passage à la phase suivante |
|---|---|---|---|
| 1 | Exercices pilotes A-01, A-10, A-20, A-24 | 4 exercices | Validation de la structure de fichier et des modes de validation |
| 2 | Lot A complet | 49 exercices | Test par au moins deux profils réellement débutants |
| 3 | Lot G, familles G1 à G4 | 20 exercices | Retour d'expérience sur l'acceptabilité des mécaniques |
| 4 | Lot B complet | 18 exercices | Calibration des durées cibles sur utilisateurs réels |
| 5 | Lot G, familles G5 à G7 | 12 exercices | — |
| 6 | Lot C complet | 12 projets | Évolution préalable du moteur de comparaison géométrique |

### 10.2 Charge estimée

Les durées ci-dessous sont des **estimations non mesurées**, à confirmer après production des exercices pilotes.

| Lot | Exercices | Estimation par exercice | Estimation du lot |
|---|---|---|---|
| A | 49 | 1.5 h | 73.5 h |
| IA | 25 | 3.5 h | 87.5 h |
| RH | 22 | 2.0 h | 44.0 h |
| GP | 8 | 3.0 h | 24.0 h |
| QT | 6 | 2.5 h | 15.0 h |
| FA | 4 | 3.0 h | 12.0 h |
| PL | 12 | 2.0 h | 24.0 h |
| MP | 4 | 2.5 h | 10.0 h |
| AV | 3 | 4.0 h | 12.0 h |
| DV | 9 | 5.0 h | 45.0 h |
| WB | 7 | 5.0 h | 35.0 h |
| B | 18 | 4.0 h | 72.0 h |
| C | 12 | 8.0 h | 96.0 h |
| G | 32 | 2.5 h | 80.0 h |
| | **211** | | **630.0 h** |

Ce volume dépasse largement l'enveloppe initiale de dix heures de contribution. Il est donc proposé de traiter en priorité les phases 1 et 2, et de statuer sur la suite au vu des retours des premiers tests.

### 10.3 Répartition proposée

| Contributeur | Périmètre proposé |
|---|---|
| Jérémy CAROLUS | Structure des fichiers, descripteurs JSON, exercices pilotes, lot A |
| Charles THIERRY DE VILLE D'AVRAY | Lot G, mécaniques de gamification, exercices de joaillerie et de mobilier |
| Jacques HABABOU | Arbitrage pédagogique, cohérence avec l'offre RhinoForYou, tests utilisateurs |
| À définir | Lot C, après clarification du moteur de comparaison |

---

## 11. Critères d'acceptation

Un exercice n'est réputé livré que lorsque **tous** les points suivants sont vérifiés.

| # | Critère | Vérification |
|---|---|---|
| 1 | Les deux fichiers `_sujet.gh` et `_complet.gh` existent et s'ouvrent sans erreur | Ouverture sur un poste vierge |
| 2 | Le descripteur JSON est présent et cohérent avec la fiche | Comparaison champ à champ |
| 3 | La zone sujet respecte la structure du chapitre 3 | Contrôle visuel |
| 4 | La zone corrigé comporte un sous-groupe par étape de la fiche | Comparaison avec la rubrique 6 |
| 5 | Le corrigé produit bien le résultat attendu | Exécution du corrigé et validation par Magpie |
| 6 | L'exercice est validé par une solution différente du corrigé | Test par un second contributeur |
| 7 | Une solution volontairement fausse est bien rejetée | Test négatif |
| 8 | La tolérance retenue ne laisse pas passer une solution approximative | Test aux bornes |
| 9 | Le nombre de composants de la solution de référence est renseigné et exact | Comptage |
| 10 | La version est affichée dans le bandeau du fichier | Contrôle visuel |
| 11 | Aucun chemin de fichier absolu ne subsiste | Ouverture depuis un autre dossier |
| 12 | L'exercice a été réalisé par au moins une personne du niveau visé | Fiche de test signée |
| 13 | La fiche d'exercice existe en version complète et en version sujet seul | Présence des deux `.md` |
| 14 | Aucun objet ni groupe du corrigé ne subsiste dans le `_sujet.gh` | Contrôle automatisé d'étanchéité |
| 15 | Aucun chevauchement d'objets sur le canvas | Audit de mise en page |
| 16 | Aucun câble ne relie la zone sujet à la zone corrigé | Contrôle automatisé d'étanchéité des zones |
| 17 | Interrupteur sur faux : le corrigé ne produit rien | Contrôle automatisé, les deux états testés |
| 18 | La fiche Word existe en version complète et en version sujet seul, illustrées | Présence des deux `.docx` et des captures |

---

## 12. Points ouverts

| # | Point | Impact | Décision attendue de |
|---|---|---|---|
| 1 | Le moteur de comparaison géométrique ne distingue pas deux topologies de même volume | Bloque le lot C | Jérémy CAROLUS |
| 2 | Magpie ne sait pas importer un fichier de résultats existant | Bloque l'exercice G-31 | Jérémy CAROLUS |
| 3 | Aucun composant de lecture sonore n'est intégré au plugin | Bloque l'exercice G-24 sans Human | Jérémy CAROLUS |
| 4 | Les durées cibles ne sont pas calibrées | Empêche l'activation du critère temps | Tous, après tests |
| 5 | La propriété des exercices n'est pas qualifiée | Bloque la diffusion | Jacques HABABOU / VAC |
| 6 | Les 10 fondamentaux V1 absents des programmes doivent-ils être ajoutés aux programmes ? | Cohérence offre / outil | Jacques HABABOU |
| 7 | Le lot C mobilise des plugins tiers dont la disponibilité chez l'apprenant n'est pas garantie | Risque d'échec silencieux | Jérémy CAROLUS |
| 8 | Volume total de production très supérieur à l'enveloppe initiale | Planification | Tous |

---

## 13. Annexes

### 13.1 Récapitulatif de tous les exercices

| ID | Titre | Lot | Thématique | Niveau | Durée | Validation | Réf. référentiel |
|---|---|---|---|---|---|---|---|
| A-01 | Premier flux de données | A | A1 · Interface, flux de données et paramètres | Débutant | 5 min | SingleValue | REF-027, REF-028 |
| A-02 | Construire un point par coordonnées | A | A1 · Interface, flux de données et paramètres | Débutant | 6 min | GeometryTolerance | REF-062 |
| A-03 | Internaliser une donnée | A | A1 · Interface, flux de données et paramètres | Débutant | 6 min | GeometryTolerance | REF-027 |
| A-04 | Référencer et cuire de la géométrie Rhino | A | A1 · Interface, flux de données et paramètres | Débutant | 8 min | GeometryTolerance | REF-026 |
| A-05 | Lire ce qui circule dans un câble | A | A1 · Interface, flux de données et paramètres | Débutant | 5 min | SingleValue | REF-027, REF-028 |
| A-06 | Conversion implicite Number vers Integer | A | A2 · Types, conversion et valeurs | Débutant | 6 min | SingleValue | REF-040 |
| A-07 | Quand la conversion échoue | A | A2 · Types, conversion et valeurs | Débutant | 6 min | SingleValue | REF-041 |
| A-08 | Booléen et nombre | A | A2 · Types, conversion et valeurs | Débutant | 5 min | SingleValue | REF-040, REF-059 |
| A-09 | Valeur nulle et propagation | A | A2 · Types, conversion et valeurs | Débutant | 7 min | SingleValue | REF-055 |
| A-10 | Series et Range | A | A3 · Listes | Débutant | 7 min | ExactOrderedList | REF-043, REF-047 |
| A-11 | List Item et indexation | A | A3 · Listes | Débutant | 6 min | ExactOrderedList | REF-042 |
| A-12 | Longueur et bornes d'une liste | A | A3 · Listes | Débutant | 5 min | ExactOrderedList | REF-043 |
| A-13 | Trier une liste avec une clé | A | A3 · Listes | Débutant | 8 min | ExactOrderedList | REF-044, REF-047 |
| A-14 | Filtrer avec Cull Pattern | A | A3 · Listes | Débutant | 7 min | ExactOrderedList | REF-045 |
| A-15 | Répartir avec Dispatch | A | A3 · Listes | Débutant | 7 min | SingleValue | REF-045, REF-061 |
| A-16 | Décaler et inverser une liste | A | A3 · Listes | Débutant | 6 min | GeometryTolerance | REF-046 |
| A-17 | Fusionner et entrelacer | A | A3 · Listes | Débutant | 6 min | ExactOrderedList | REF-042 |
| A-18 | Extraire une portion de liste | A | A3 · Listes | Débutant | 6 min | ExactOrderedList | REF-042, REF-043 |
| A-19 | Lire un chemin d'arbre | A | A4 · Arbres de données | Débutant | 7 min | SingleValue | REF-048, REF-051 |
| A-20 | Graft et Flatten | A | A4 · Arbres de données | Débutant | 8 min | GeometryTolerance | REF-049, REF-052 |
| A-21 | Nettoyer une structure | A | A4 · Arbres de données | Débutant | 7 min | SetEquality | REF-050 |
| A-22 | Construire un arbre | A | A4 · Arbres de données | Débutant | 8 min | SetEquality | REF-048, REF-051 |
| A-23 | Renommer les chemins avec Path Mapper | A | A4 · Arbres de données | Débutant | 9 min | SetEquality | REF-050 |
| A-24 | Correspondance par défaut | A | A5 · Comportements implicites | Débutant | 7 min | SingleValue | REF-053 |
| A-25 | Longest List et Cross Reference | A | A5 · Comportements implicites | Débutant | 8 min | ExactOrderedList | REF-054 |
| A-26 | Ordre d'évaluation et recalcul | A | A5 · Comportements implicites | Débutant | 6 min | Conceptuel (QCM) | REF-056, REF-090 |
| A-27 | Construire une chaîne de caractères | A | A6 · Outils de texte | Débutant | 6 min | Visuel | REF-057 |
| A-28 | Découper et remplacer du texte | A | A6 · Outils de texte | Débutant | 7 min | Visuel | REF-058 |
| A-29 | Comparer deux valeurs | A | A7 · Portes logiques | Débutant | 5 min | SingleValue | REF-059 |
| A-30 | Combiner plusieurs conditions | A | A7 · Portes logiques | Débutant | 7 min | SingleValue | REF-060 |
| A-31 | Orienter un flux avec une condition | A | A7 · Portes logiques | Débutant | 7 min | GeometryTolerance | REF-061 |
| A-32 | Vecteur, amplitude et direction | A | A8 · Géométrie vectorielle et filaire | Débutant | 7 min | GeometryTolerance | REF-062 |
| A-33 | Plans de construction | A | A8 · Géométrie vectorielle et filaire | Débutant | 7 min | GeometryTolerance | REF-062 |
| A-34 | Primitives filaires | A | A8 · Géométrie vectorielle et filaire | Débutant | 8 min | GeometryTolerance | REF-063 |
| A-35 | Diviser et évaluer une courbe | A | A8 · Géométrie vectorielle et filaire | Débutant | 8 min | GeometryTolerance | REF-064 |
| A-36 | Courbes passant par des points | A | A8 · Géométrie vectorielle et filaire | Débutant | 7 min | GeometryTolerance | REF-063 |
| A-37 | Déplacer par un vecteur | A | A9 · Transformations et réseaux | Débutant | 5 min | GeometryTolerance | REF-067 |
| A-38 | Rotation et symétrie | A | A9 · Transformations et réseaux | Débutant | 7 min | GeometryTolerance | REF-067 |
| A-39 | Réseaux rectangulaire et polaire | A | A9 · Transformations et réseaux | Débutant | 8 min | GeometryTolerance | REF-068 |
| A-40 | Mise à l'échelle | A | A9 · Transformations et réseaux | Débutant | 6 min | GeometryTolerance | REF-067 |
| A-41 | Extrusion et surface réglée | A | A10 · Surfaces et solides | Débutant | 8 min | GeometryTolerance | REF-069 |
| A-42 | Balayage et révolution | A | A10 · Surfaces et solides | Débutant | 8 min | GeometryTolerance | REF-069 |
| A-43 | Fermer une polysurface en solide | A | A10 · Surfaces et solides | Débutant | 7 min | NumericTolerance | REF-070 |
| A-44 | Opérations booléennes | A | A10 · Surfaces et solides | Débutant | 8 min | NumericTolerance | REF-071 |
| A-45 | Intersections entre géométries | A | A10 · Surfaces et solides | Débutant | 7 min | NumericTolerance | REF-071 |
| A-46 | Détecter une collision | A | A10 · Surfaces et solides | Débutant | 7 min | SetEquality | REF-072 |
| A-47 | Longueur, aire et volume | A | A11 · Mesures géométriques | Débutant | 6 min | NumericTolerance | REF-079 |
| A-48 | Courbure et point le plus proche | A | A11 · Mesures géométriques | Débutant | 7 min | NumericTolerance | REF-080 |
| A-49 | Centre de gravité | A | A11 · Mesures géométriques | Débutant | 6 min | GeometryTolerance | REF-081 |
| IA-01 | Spécifier un composant plutôt que le décrire | IA | IA1 · Formuler et cadrer une demande | Débutant | 20 min | SingleValue | REF-117, REF-139 |
| IA-02 | Le contexte technique manquant | IA | IA1 · Formuler et cadrer une demande | Débutant | 8 min | — | REF-118 |
| IA-03 | Reprendre une demande sur le point qui échoue | IA | IA1 · Formuler et cadrer une demande | Débutant | 18 min | SingleValue | REF-119 |
| IA-04 | Un composant scripté qui somme un métré | IA | IA2 · Composants scriptés assistés | Intermédiaire | 25 min | NumericTolerance | REF-120, REF-121 |
| IA-05 | Le code qui tourne et se trompe | IA | IA2 · Composants scriptés assistés | Intermédiaire | 22 min | SingleValue | REF-124 |
| IA-06 | Transposer sans changer le résultat | IA | IA2 · Composants scriptés assistés | Intermédiaire | 20 min | ExactOrderedList | REF-122, REF-123 |
| IA-07 | Un plugin .gha conduit par un agent | IA | IA3 · Développement de plugins assisté | Perfectionnement | 90 min | Visuel | REF-125, REF-126, REF-127 |
| IA-08 | Le GUID que l'on ne régénère pas | IA | IA3 · Développement de plugins assisté | Perfectionnement | 6 min | — | REF-128 |
| IA-09 | Prédire une déperdition sur une baie nouvelle | IA | IA4 · Apprentissage automatique | Perfectionnement | 30 min | NumericTolerance | REF-129, REF-131, REF-132 |
| IA-10 | Regrouper un débit pour rationaliser la commande | IA | IA4 · Apprentissage automatique | Perfectionnement | 25 min | SingleValue | REF-130 |
| IA-11 | Un cahier des charges qui devient des paramètres | IA | IA5 · Modèles de langage et IA générative | Perfectionnement | 25 min | SingleValue | REF-133, REF-134, REF-135 |
| IA-12 | Faire construire un graphe par un agent | IA | IA6 · Agents et protocoles | Perfectionnement | 35 min | NumericTolerance | REF-136, REF-137, REF-138 |
| IA-13 | Ce qui quitte le poste | IA | IA7 · Vérification, licences et limites | Débutant | 8 min | — | REF-140, REF-141 |
| IA-14 | Le résultat plausible et faux | IA | IA7 · Vérification, licences et limites | Débutant | 15 min | NumericTolerance | REF-139, REF-142 |
| IA-15 | Relire le graphe qu'un agent a construit | IA | IA7 · Agents et protocoles | Perfectionnement | 30 min | SingleValue | REF-137 |
| IA-16 | Ce qu'un agent ne fait pas sans vous | IA | IA7 · Agents et protocoles | Perfectionnement | 8 min | — | REF-138 |
| IA-17 | Une commande cachée dans un courriel | IA | IA6 · Modèles de langage et IA générative | Perfectionnement | 30 min | SingleValue | REF-134 |
| IA-18 | Ce qu'une image générée ne vous donne pas | IA | IA6 · Modèles de langage et IA générative | Perfectionnement | 8 min | — | REF-135 |
| IA-19 | Regrouper un débit en trois familles | IA | IA5 · Apprentissage automatique | Perfectionnement | 25 min | SingleValue | REF-130 |
| IA-20 | Ce qu'un budget de calcul permet d'essayer | IA | IA5 · Apprentissage automatique | Perfectionnement | 30 min | SingleValue | REF-131, REF-132 |
| IA-21 | Le script qui compte les intervalles | IA | IA2 · Composants scriptés assistés | Intermédiaire | 25 min | SingleValue | REF-121 |
| IA-22 | L'arrondi qui change avec le langage | IA | IA2 · Composants scriptés assistés | Intermédiaire | 25 min | SingleValue | REF-123 |
| IA-23 | Combien de tours avant que tout passe | IA | IA3 · Développement de plugins assisté | Perfectionnement | 25 min | SingleValue | REF-126 |
| IA-24 | Le composant qui n'apparaît pas | IA | IA3 · Développement de plugins assisté | Perfectionnement | 8 min | — | REF-127 |
| IA-25 | Ce que le service coûte par mois | IA | IA4 · Vérification, licences et limites | Perfectionnement | 25 min | NumericTolerance | REF-142 |
| RH-01 | Retrouver un objet perdu de vue | RH | RH1 · Interface et navigation Rhino | Débutant | 6 min | — | REF-001, REF-002, REF-003 |
| RH-02 | Reprendre une implantation par son calque | RH | RH2 · Organisation du document | Débutant | 15 min | SingleValue | REF-004, REF-006, REF-014 |
| RH-03 | Une trame de plots posée dans Rhino | RH | RH3 · Modélisation Rhino | Débutant | 20 min | SingleValue | REF-007, REF-008, REF-013 |
| RH-04 | Du profil à la surface | RH | RH3 · Modélisation Rhino | Débutant | 20 min | NumericTolerance | REF-009, REF-010, REF-011 |
| RH-05 | Percer une platine dans Rhino | RH | RH3 · Modélisation Rhino | Débutant | 15 min | NumericTolerance | REF-012 |
| RH-06 | Groupe ou bloc ? | RH | RH2 · Organisation du document | Débutant | 6 min | — | REF-005 |
| RH-07 | Le fichier au mauvais millimètre | RH | RH4 · Précision et unités | Débutant | 7 min | — | REF-015, REF-017 |
| RH-08 | Un caisson vraiment fermé | RH | RH5 · Préparation à l'impression 3D | Débutant | 25 min | NumericTolerance | REF-019, REF-020, REF-021, REF-022, REF-023 |
| RH-09 | Une pièce imprimable | RH | RH5 · Préparation à l'impression 3D | Débutant | 20 min | NumericTolerance | REF-016, REF-018 |
| RH-10 | Ce que l'export STL perd | RH | RH5 · Préparation à l'impression 3D | Débutant | 7 min | — | REF-024 |
| RH-11 | Ce que le zoom étendue vous apprend | RH | RH1 · Interface et navigation Rhino | Débutant | 15 min | SingleValue | REF-001, REF-002, REF-003 |
| RH-12 | Ce qui dépasse le niveau | RH | RH1 · Interface et navigation Rhino | Débutant | 15 min | SingleValue | REF-002 |
| RH-13 | Ce que le fichier contient vraiment | RH | RH1 · Interface et navigation Rhino | Débutant | 15 min | SingleValue | REF-006, REF-004 |
| RH-14 | La trame percée d'une trémie | RH | RH2 · Modélisation Rhino | Débutant | 20 min | SingleValue | REF-013, REF-008 |
| RH-15 | Le développé d'un cheminement | RH | RH2 · Modélisation Rhino | Débutant | 20 min | SingleValue | REF-009 |
| RH-16 | La surface d'un rampant | RH | RH2 · Modélisation Rhino | Débutant | 20 min | NumericTolerance | REF-010, REF-011 |
| RH-17 | Le volume de deux blocs qui se recouvrent | RH | RH2 · Modélisation Rhino | Débutant | 20 min | NumericTolerance | REF-012 |
| RH-18 | Les parois que la machine ne saura pas faire | RH | RH3 · Préparation à l'impression 3D | Débutant | 20 min | SingleValue | REF-016 |
| RH-19 | Ce que la mise à l'échelle fait aux détails | RH | RH3 · Préparation à l'impression 3D | Débutant | 25 min | SingleValue | REF-017, REF-018 |
| RH-20 | Un maillage est-il fermé | RH | RH3 · Préparation à l'impression 3D | Débutant | 25 min | SingleValue | REF-019, REF-020, REF-021 |
| RH-21 | Les faces qui ne mesurent rien | RH | RH3 · Préparation à l'impression 3D | Débutant | 20 min | SingleValue | REF-022, REF-023 |
| RH-22 | La finesse du maillage à l'export | RH | RH3 · Préparation à l'impression 3D | Débutant | 25 min | SingleValue | REF-024 |
| GP-01 | Un plan coté qui suit ses paramètres | GP | GP1 · Plan paramétrique | Débutant | 25 min | NumericTolerance | REF-065, REF-066 |
| GP-02 | Un modèle paramétrique de bout en bout | GP | GP2 · Synthèse géométrie | Intermédiaire | 45 min | NumericTolerance | REF-073 |
| GP-03 | Un maillage qu'on peut imprimer | GP | GP3 · Maillages et SubD | Perfectionnement | 30 min | NumericTolerance | REF-074, REF-075, REF-076 |
| GP-04 | SubD ou NURBS ? | GP | GP3 · Maillages et SubD | Perfectionnement | 7 min | — | REF-077, REF-078 |
| GP-05 | La chaîne de cotes d'une façade | GP | GP3 · Plan paramétrique | Intermédiaire | 25 min | SingleValue | REF-065, REF-066 |
| GP-06 | Les sommets d'une nappe maillée | GP | GP4 · Maillages et SubD | Perfectionnement | 20 min | SingleValue | REF-074 |
| GP-07 | Ce que la soudure retire | GP | GP4 · Maillages et SubD | Perfectionnement | 25 min | SingleValue | REF-076 |
| GP-08 | Ce que coûte une subdivision de plus | GP | GP4 · Maillages et SubD | Perfectionnement | 20 min | SingleValue | REF-077, REF-078 |
| QT-01 | Le métré d'un plancher bois | QT | QT1 · Quantitatifs et chiffrage | Intermédiaire | 25 min | NumericTolerance | REF-082, REF-084 |
| QT-02 | Du métré au prix | QT | QT1 · Quantitatifs et chiffrage | Intermédiaire | 25 min | NumericTolerance | REF-083 |
| QT-03 | Une nomenclature exportable | QT | QT2 · Export de données | Intermédiaire | 30 min | NumericTolerance | REF-085, REF-086, REF-087 |
| QT-04 | Un débit qui devient une commande | QT | QT3 · Export de données | Intermédiaire | 30 min | SingleValue | REF-085 |
| QT-05 | Le fichier que le fournisseur va lire | QT | QT3 · Export de données | Intermédiaire | 25 min | SingleValue | REF-086, REF-087 |
| QT-06 | Du métré au devis | QT | QT2 · Quantitatifs et chiffrage | Intermédiaire | 30 min | NumericTolerance | REF-083 |
| FA-01 | Combien de panneaux pour ce débit | FA | FA1 · Imbrication | Perfectionnement | 35 min | SingleValue | REF-113, REF-114 |
| FA-02 | Le développé d'une virole | FA | FA2 · Déroulé et mise à plat | Perfectionnement | 30 min | NumericTolerance | REF-115, REF-116 |
| FA-03 | Le développé d'un profil plié | FA | FA2 · Déroulé et mise à plat | Perfectionnement | 35 min | NumericTolerance | REF-116 |
| FA-04 | Combien de pièces par fournée | FA | FA1 · Imbrication | Perfectionnement | 30 min | SingleValue | REF-114 |
| PL-01 | Ce qui change quand on passe au paramétrique | PL | PL1 · Principes | Débutant | 8 min | — | REF-025 |
| PL-02 | Où trouver un plugin, et lequel | PL | PL2 · Installation de plugins | Intermédiaire | 8 min | — | REF-029, REF-030 |
| PL-03 | Les plugins qui ne servent qu'à travailler mieux | PL | PL3 · Plugins d'ergonomie | Intermédiaire | 20 min | Visuel | REF-031, REF-032, REF-033, REF-034, REF-035, REF-036, REF-037 |
| PL-04 | Choisir un plugin fonctionnel | PL | PL4 · Plugins fonctionnels | Intermédiaire | 8 min | — | REF-038, REF-039 |
| PL-05 | Ce qu'un plugin traîne derrière lui | PL | PL1 · Écosystème de plugins | Intermédiaire | 20 min | SingleValue | REF-029, REF-030 |
| PL-06 | Qui pourra ouvrir votre définition | PL | PL1 · Écosystème de plugins | Intermédiaire | 20 min | SingleValue | REF-038, REF-039 |
| PL-07 | Ce qu'un plugin vous épargne d'écrire | PL | PL1 · Écosystème de plugins | Intermédiaire | 20 min | SingleValue | REF-038, REF-039 |
| PL-08 | Les composants qui ne disent pas leur nom | PL | PL1 · Écosystème de plugins | Intermédiaire | 20 min | SingleValue | REF-031, REF-032, REF-033 |
| PL-09 | Ce qui s'installera vraiment sur ce poste | PL | PL1 · Écosystème de plugins | Intermédiaire | 15 min | SingleValue | REF-030 |
| PL-10 | Où chercher un plugin | PL | PL1 · Écosystème de plugins | Intermédiaire | 8 min | — | REF-029, REF-030 |
| PL-11 | Deux familles de plugins | PL | PL1 · Écosystème de plugins | Intermédiaire | 8 min | — | REF-031, REF-034, REF-035, REF-036, REF-037 |
| PL-12 | Le plugin qui n'est plus maintenu | PL | PL1 · Écosystème de plugins | Intermédiaire | 8 min | — | REF-039 |
| MP-01 | Une définition qu'un autre peut reprendre | MP | MP1 · Organisation et lisibilité | Intermédiaire | 30 min | Visuel | REF-088 |
| MP-02 | Trouver ce qui coûte le temps de calcul | MP | MP2 · Performance d'exécution | Perfectionnement | 25 min | SingleValue | REF-089 |
| MP-03 | Une définition qui réagit | MP | MP3 · Chronologie et évènements | Perfectionnement | 8 min | — | REF-091, REF-092 |
| MP-04 | Ce qu'un curseur fait recalculer | MP | MP1 · Chronologie et évènements | Perfectionnement | 25 min | SingleValue | REF-090 |
| AV-01 | Converger vers une portée | AV | AV1 · Boucles et itération | Perfectionnement | 35 min | SingleValue | REF-093 |
| AV-02 | Une chaînette qui se stabilise | AV | AV2 · Simulation physique | Perfectionnement | 35 min | NumericTolerance | REF-094 |
| AV-03 | Chercher la meilleure trame | AV | AV3 · Design génératif | Perfectionnement | 40 min | SingleValue | REF-095 |
| DV-01 | Quand écrire du script plutôt que câbler | DV | DV1 · Scripting dans Grasshopper | Expert | 8 min | — | REF-100 |
| DV-02 | Un composant scripté qui parle à RhinoCommon | DV | DV2 · API et librairies | Expert | 35 min | NumericTolerance | REF-101, REF-102, REF-103 |
| DV-03 | Ce que les librairies évitent d'écrire | DV | DV2 · API et librairies | Expert | 8 min | — | REF-104, REF-105 |
| DV-04 | Du composant scripté au plugin installé | DV | DV3 · Compilation et IDE | Expert | 120 min | Visuel | REF-096, REF-097, REF-098, REF-099 |
| DV-05 | Ce que la compilation change vraiment | DV | DV3 · Compilation et IDE | Expert | 8 min | — | REF-096 |
| DV-06 | Le plugin qui parle aussi à Rhino | DV | DV3 · Compilation et IDE | Expert | 8 min | — | REF-097, REF-099 |
| DV-07 | Un plugin qui s'installe chez quelqu'un d'autre | DV | DV3 · Compilation et IDE | Expert | 50 min | Visuel | REF-098 |
| DV-08 | Ce que le remappage fait aux branches | DV | DV2 · API et librairies | Expert | 25 min | SingleValue | REF-105 |
| DV-09 | La division qui n'est pas celle qu'on croit | DV | DV1 · Scripting dans Grasshopper | Expert | 25 min | SingleValue | REF-100, REF-102 |
| WB-01 | Une définition utilisable par quelqu'un d'autre | WB | WB1 · Interfaces utilisateur | Perfectionnement | 40 min | Visuel | REF-106, REF-107 |
| WB-02 | Publier un configurateur | WB | WB2 · Publication web | Perfectionnement | 90 min | Visuel | REF-108, REF-109, REF-110 |
| WB-03 | Rhino sans Rhino | WB | WB3 · Interopérabilité | Expert | 8 min | — | REF-111, REF-112 |
| WB-04 | Ce qu'on expose, et ce qu'on cache | WB | WB1 · Interfaces utilisateur | Perfectionnement | 25 min | SingleValue | REF-107 |
| WB-05 | Dimensionner le calcul d'un configurateur | WB | WB3 · Interopérabilité | Expert | 30 min | SingleValue | REF-112 |
| WB-06 | Le poids du modèle que l'on télécharge | WB | WB2 · Publication web | Perfectionnement | 25 min | SingleValue | REF-109 |
| WB-07 | Le plan qui tient sur la feuille | WB | WB2 · Publication web | Perfectionnement | 25 min | SingleValue | REF-110 |
| B-01 | Escalier droit paramétrique | B | B1 · Architecture et construction | Intermédiaire | 25 min | NumericTolerance | REF-067, REF-068, REF-047, REF-043 |
| B-02 | Garde-corps à barreaudage régulier | B | B1 · Architecture et construction | Intermédiaire | 20 min | NumericTolerance | REF-064, REF-047, REF-043 |
| B-03 | Façade à trame variable pilotée par un attracteur | B | B1 · Architecture et construction | Intermédiaire | 30 min | GeometryTolerance | REF-068, REF-053, REF-054 |
| B-04 | Pavage hexagonal sur surface | B | B1 · Architecture et construction | Intermédiaire | 28 min | GeometryTolerance | REF-068, REF-069, REF-049 |
| B-05 | Poutre treillis paramétrique | B | B1 · Architecture et construction | Intermédiaire | 25 min | NumericTolerance | REF-046, REF-063, REF-079 |
| B-06 | Caisson de meuble avec épaisseur et rainures | B | B2 · Design de mobilier | Intermédiaire | 30 min | GeometryTolerance | REF-070, REF-071, REF-068 |
| B-07 | Tiroir paramétrique avec jeux fonctionnels | B | B2 · Design de mobilier | Intermédiaire | 25 min | SingleValue | REF-070, REF-072 |
| B-08 | Étagère modulaire à pas variable | B | B2 · Design de mobilier | Intermédiaire | 22 min | ExactOrderedList | REF-043, REF-044, REF-047 |
| B-09 | Griffe de sertissage paramétrique | B | B3 · Joaillerie | Intermédiaire | 28 min | GeometryTolerance | REF-068, REF-069, REF-067 |
| B-10 | Motif gravé développé sur un anneau | B | B3 · Joaillerie | Intermédiaire | 30 min | GeometryTolerance | REF-115, REF-069, REF-049 |
| B-11 | Chaîne de maillons le long d'une courbe | B | B3 · Joaillerie | Intermédiaire | 25 min | GeometryTolerance | REF-064, REF-067, REF-046 |
| B-12 | Nomenclature automatique et export CSV | B | B4 · Données, métrés et livrables | Intermédiaire | 25 min | ExactOrderedList | REF-082, REF-083, REF-085, REF-087 |
| B-13 | Calepinage de plaques et calcul de chute | B | B4 · Données, métrés et livrables | Intermédiaire | 28 min | NumericTolerance | REF-113, REF-082, REF-045 |
| B-14 | Numérotation et étiquetage automatiques | B | B4 · Données, métrés et livrables | Intermédiaire | 22 min | ExactOrderedList | REF-066, REF-081, REF-057 |
| B-15 | Optimisation d'une découpe linéaire | B | B4 · Données, métrés et livrables | Intermédiaire | 30 min | SingleValue | REF-044, REF-045, REF-082 |
| B-16 | Lampe à lamelles de section variable | B | B5 · Design produit | Intermédiaire | 28 min | GeometryTolerance | REF-064, REF-069, REF-067 |
| B-17 | Coque à nervures depuis une surface libre | B | B5 · Design produit | Intermédiaire | 30 min | GeometryTolerance | REF-069, REF-101, REF-049 |
| B-18 | Filetage hélicoïdal paramétrique | B | B5 · Design produit | Intermédiaire | 28 min | NumericTolerance | REF-069, REF-103 |
| C-01 | Enveloppe à brise-soleil orientés selon l'ensoleillement | C | C1 · Architecture | Expérimenté | 90 min | NumericTolerance | REF-027, REF-068, REF-095, REF-079 |
| C-02 | Résille structurelle sur plan libre | C | C1 · Architecture | Expérimenté | 90 min | NumericTolerance | REF-069, REF-094, REF-074, REF-049 |
| C-03 | Gradins avec contrôle de visibilité | C | C1 · Architecture | Expérimenté | 80 min | NumericTolerance | REF-047, REF-079, REF-046, REF-060 |
| C-04 | Métré et chiffrage complet d'un module | C | C1 · Architecture | Expérimenté | 75 min | NumericTolerance | REF-082, REF-083, REF-084, REF-086 |
| C-05 | Bibliothèque paramétrique avec débit et mise à plat CNC | C | C2 · Design de mobilier | Expérimenté | 90 min | GeometryTolerance | REF-070, REF-082, REF-115, REF-087 |
| C-06 | Chaise à assise en lamelles courbes | C | C2 · Design de mobilier | Expérimenté | 85 min | NumericTolerance | REF-069, REF-064, REF-074 |
| C-07 | Table de nuit configurable | C | C2 · Design de mobilier | Expérimenté | 80 min | GeometryTolerance | REF-070, REF-072, REF-082, REF-106 |
| C-08 | Bague solitaire complète | C | C3 · Joaillerie | Expérimenté | 85 min | NumericTolerance | REF-069, REF-068, REF-081, REF-079 |
| C-09 | Pavage de pierres sur surface libre | C | C3 · Joaillerie | Expérimenté | 85 min | NumericTolerance | REF-068, REF-101, REF-080, REF-045 |
| C-10 | Motif gravé génératif sur bijou | C | C3 · Joaillerie | Expérimenté | 80 min | NumericTolerance | REF-115, REF-095, REF-069 |
| C-11 | Déroulé de tôle pliée avec compensation | C | C4 · Fabrication | Expérimenté | 80 min | NumericTolerance | REF-116, REF-115, REF-082 |
| C-12 | Imbrication et export de fabrication | C | C4 · Fabrication | Expérimenté | 75 min | NumericTolerance | REF-113, REF-114, REF-087 |
| G-01 | Le tableau des scores | G | G1 · Progression et récompense | Débutant | 10 min | ExactOrderedList | REF-047, REF-043 |
| G-02 | La barre de progression | G | G1 · Progression et récompense | Débutant | 12 min | GeometryTolerance | REF-062, REF-063 |
| G-03 | Contre la montre | G | G1 · Progression et récompense | Intermédiaire | 6 min | ExactOrderedList | REF-042, REF-043 |
| G-04 | Trois vies | G | G1 · Progression et récompense | Intermédiaire | 15 min | SingleValue | REF-053, REF-054 |
| G-05 | La collection de badges | G | G1 · Progression et récompense | Intermédiaire | 20 min | NumericTolerance | REF-079, REF-081, REF-098 |
| G-06 | Le déblocage progressif | G | G1 · Progression et récompense | Intermédiaire | 18 min | SetEquality | REF-059, REF-060, REF-061 |
| G-07 | Une, deux ou trois étoiles | G | G1 · Progression et récompense | Intermédiaire | 15 min | GeometryTolerance | REF-067, REF-068 |
| G-08 | La série de bonnes réponses | G | G1 · Progression et récompense | Intermédiaire | 16 min | ExactOrderedList | REF-044, REF-045, REF-046 |
| G-09 | Le composant caché | G | G2 · Exploration et découverte | Débutant | 10 min | SingleValue | REF-028, REF-056 |
| G-10 | Le coffre à butin | G | G2 · Exploration et découverte | Intermédiaire | 14 min | SetEquality | REF-068, REF-045 |
| G-11 | Les mots croisés des composants | G | G2 · Exploration et découverte | Débutant | 15 min | SingleValue | REF-057, REF-058 |
| G-12 | Le memory des composants | G | G2 · Exploration et découverte | Débutant | 12 min | SetEquality | REF-047, REF-051, REF-049 |
| G-13 | La machine à sous des motifs | G | G2 · Exploration et découverte | Intermédiaire | 15 min | ExactOrderedList | REF-045, REF-068 |
| G-14 | Le puzzle de câblage | G | G3 · Manipulation et adresse | Débutant | 12 min | GeometryTolerance | REF-027, REF-048 |
| G-15 | Le dessin à compléter | G | G3 · Manipulation et adresse | Débutant | 14 min | GeometryTolerance | REF-063, REF-067 |
| G-16 | La chasse au trésor | G | G3 · Manipulation et adresse | Intermédiaire | 18 min | SingleValue | REF-055, REF-101 |
| G-17 | Le quiz éclair | G | G4 · Connaissance et mémorisation | Débutant | 8 min | ExactOrderedList | REF-040, REF-053, REF-056 |
| G-18 | Vrai ou faux à élimination | G | G4 · Connaissance et mémorisation | Débutant | 10 min | ExactOrderedList | REF-040, REF-041, REF-059 |
| G-19 | Le composant mystère | G | G4 · Connaissance et mémorisation | Intermédiaire | 12 min | ExactOrderedList | REF-028, REF-042 |
| G-20 | La chasse aux bugs | G | G4 · Connaissance et mémorisation | Intermédiaire | 20 min | SetEquality | REF-041, REF-053, REF-055 |
| G-21 | Le golf de composants | G | G5 · Performance et compétition | Intermédiaire | 20 min | GeometryTolerance | REF-068, REF-043, REF-046 |
| G-22 | Le boss de fin de chapitre | G | G5 · Performance et compétition | Perfectionnement | 45 min | ExactOrderedList | REF-047, REF-051, REF-068, REF-079 |
| G-23 | Le duel | G | G5 · Performance et compétition | Intermédiaire | 20 min | ExactOrderedList | REF-082, REF-044 |
| G-24 | Le retour sonore | G | G6 · Sensations et immersion | Débutant | 10 min | SingleValue | REF-027, REF-061 |
| G-25 | L'animation de la solution | G | G6 · Sensations et immersion | Perfectionnement | 25 min | SetEquality | REF-090, REF-093, REF-067 |
| G-26 | Le retour visuel immédiat | G | G6 · Sensations et immersion | Débutant | 12 min | SingleValue | REF-026, REF-059 |
| G-27 | La savane paramétrique | G | G6 · Sensations et immersion | Débutant | 20 min | GeometryTolerance | REF-063, REF-067, REF-068 |
| G-28 | L'avatar paramétrique | G | G6 · Sensations et immersion | Intermédiaire | 22 min | SingleValue | REF-067, REF-106, REF-061 |
| G-29 | Le défi du jour | G | G7 · Régularité et communauté | Intermédiaire | 10 min | NumericTolerance | REF-047, REF-079 |
| G-30 | Le relais à deux | G | G7 · Régularité et communauté | Perfectionnement | 30 min | SetEquality | REF-088, REF-048 |
| G-31 | L'arbre de compétences | G | G7 · Régularité et communauté | Intermédiaire | 15 min | SetEquality | REF-048, REF-051 |
| G-32 | Les indices payants | G | G7 · Régularité et communauté | Intermédiaire | 20 min | SetEquality | REF-052, REF-049, REF-050 |

### 13.2 Couverture du référentiel par les exercices

142 lignes du référentiel sont couvertes par au moins un exercice.

| Réf. référentiel | Exercices |
|---|---|
| REF-001 | RH-01, RH-11 |
| REF-002 | RH-01, RH-11, RH-12 |
| REF-003 | RH-01, RH-11 |
| REF-004 | RH-02, RH-13 |
| REF-005 | RH-06 |
| REF-006 | RH-02, RH-13 |
| REF-007 | RH-03 |
| REF-008 | RH-03, RH-14 |
| REF-009 | RH-04, RH-15 |
| REF-010 | RH-04, RH-16 |
| REF-011 | RH-04, RH-16 |
| REF-012 | RH-05, RH-17 |
| REF-013 | RH-03, RH-14 |
| REF-014 | RH-02 |
| REF-015 | RH-07 |
| REF-016 | RH-09, RH-18 |
| REF-017 | RH-07, RH-19 |
| REF-018 | RH-09, RH-19 |
| REF-019 | RH-08, RH-20 |
| REF-020 | RH-08, RH-20 |
| REF-021 | RH-08, RH-20 |
| REF-022 | RH-08, RH-21 |
| REF-023 | RH-08, RH-21 |
| REF-024 | RH-10, RH-22 |
| REF-025 | PL-01 |
| REF-026 | A-04, G-26 |
| REF-027 | A-01, A-03, A-05, C-01, G-14, G-24 |
| REF-028 | A-01, A-05, G-09, G-19 |
| REF-029 | PL-02, PL-05, PL-10 |
| REF-030 | PL-02, PL-05, PL-09, PL-10 |
| REF-031 | PL-03, PL-08, PL-11 |
| REF-032 | PL-03, PL-08 |
| REF-033 | PL-03, PL-08 |
| REF-034 | PL-03, PL-11 |
| REF-035 | PL-03, PL-11 |
| REF-036 | PL-03, PL-11 |
| REF-037 | PL-03, PL-11 |
| REF-038 | PL-04, PL-06, PL-07 |
| REF-039 | PL-04, PL-06, PL-07, PL-12 |
| REF-040 | A-06, A-08, G-17, G-18 |
| REF-041 | A-07, G-18, G-20 |
| REF-042 | A-11, A-17, A-18, G-03, G-19 |
| REF-043 | A-10, A-12, A-18, B-01, B-02, B-08, G-01, G-03, G-21 |
| REF-044 | A-13, B-08, B-15, G-08, G-23 |
| REF-045 | A-14, A-15, B-13, B-15, C-09, G-08, G-10, G-13 |
| REF-046 | A-16, B-05, B-11, C-03, G-08, G-21 |
| REF-047 | A-10, A-13, B-01, B-02, B-08, C-03, G-01, G-12, G-22, G-29 |
| REF-048 | A-19, A-22, G-14, G-30, G-31 |
| REF-049 | A-20, B-04, B-10, B-17, C-02, G-12, G-32 |
| REF-050 | A-21, A-23, G-32 |
| REF-051 | A-19, A-22, G-12, G-22, G-31 |
| REF-052 | A-20, G-32 |
| REF-053 | A-24, B-03, G-04, G-17, G-20 |
| REF-054 | A-25, B-03, G-04 |
| REF-055 | A-09, G-16, G-20 |
| REF-056 | A-26, G-09, G-17 |
| REF-057 | A-27, B-14, G-11 |
| REF-058 | A-28, G-11 |
| REF-059 | A-08, A-29, G-06, G-18, G-26 |
| REF-060 | A-30, C-03, G-06 |
| REF-061 | A-15, A-31, G-06, G-24, G-28 |
| REF-062 | A-02, A-32, A-33, G-02 |
| REF-063 | A-34, A-36, B-05, G-02, G-15, G-27 |
| REF-064 | A-35, B-02, B-11, B-16, C-06 |
| REF-065 | GP-01, GP-05 |
| REF-066 | GP-01, GP-05, B-14 |
| REF-067 | A-37, A-38, A-40, B-01, B-09, B-11, B-16, G-07, G-15, G-25, G-27, G-28 |
| REF-068 | A-39, B-01, B-03, B-04, B-06, B-09, C-01, C-08, C-09, G-07, G-10, G-13, G-21, G-22, G-27 |
| REF-069 | A-41, A-42, B-04, B-09, B-10, B-16, B-17, B-18, C-02, C-06, C-08, C-10 |
| REF-070 | A-43, B-06, B-07, C-05, C-07 |
| REF-071 | A-44, A-45, B-06 |
| REF-072 | A-46, B-07, C-07 |
| REF-073 | GP-02 |
| REF-074 | GP-03, GP-06, C-02, C-06 |
| REF-075 | GP-03 |
| REF-076 | GP-03, GP-07 |
| REF-077 | GP-04, GP-08 |
| REF-078 | GP-04, GP-08 |
| REF-079 | A-47, B-05, C-01, C-03, C-08, G-05, G-22, G-29 |
| REF-080 | A-48, C-09 |
| REF-081 | A-49, B-14, C-08, G-05 |
| REF-082 | QT-01, B-12, B-13, B-15, C-04, C-05, C-07, C-11, G-23 |
| REF-083 | QT-02, QT-06, B-12, C-04 |
| REF-084 | QT-01, C-04 |
| REF-085 | QT-03, QT-04, B-12 |
| REF-086 | QT-03, QT-05, C-04 |
| REF-087 | QT-03, QT-05, B-12, C-05, C-12 |
| REF-088 | MP-01, G-30 |
| REF-089 | MP-02 |
| REF-090 | A-26, MP-04, G-25 |
| REF-091 | MP-03 |
| REF-092 | MP-03 |
| REF-093 | AV-01, G-25 |
| REF-094 | AV-02, C-02 |
| REF-095 | AV-03, C-01, C-10 |
| REF-096 | DV-04, DV-05 |
| REF-097 | DV-04, DV-06 |
| REF-098 | DV-04, DV-07, G-05 |
| REF-099 | DV-04, DV-06 |
| REF-100 | DV-01, DV-09 |
| REF-101 | DV-02, B-17, C-09, G-16 |
| REF-102 | DV-02, DV-09 |
| REF-103 | DV-02, B-18 |
| REF-104 | DV-03 |
| REF-105 | DV-03, DV-08 |
| REF-106 | WB-01, C-07, G-28 |
| REF-107 | WB-01, WB-04 |
| REF-108 | WB-02 |
| REF-109 | WB-02, WB-06 |
| REF-110 | WB-02, WB-07 |
| REF-111 | WB-03 |
| REF-112 | WB-03, WB-05 |
| REF-113 | FA-01, B-13, C-12 |
| REF-114 | FA-01, FA-04, C-12 |
| REF-115 | FA-02, B-10, C-05, C-10, C-11 |
| REF-116 | FA-02, FA-03, C-11 |
| REF-117 | IA-01 |
| REF-118 | IA-02 |
| REF-119 | IA-03 |
| REF-120 | IA-04 |
| REF-121 | IA-04, IA-21 |
| REF-122 | IA-06 |
| REF-123 | IA-06, IA-22 |
| REF-124 | IA-05 |
| REF-125 | IA-07 |
| REF-126 | IA-07, IA-23 |
| REF-127 | IA-07, IA-24 |
| REF-128 | IA-08 |
| REF-129 | IA-09 |
| REF-130 | IA-10, IA-19 |
| REF-131 | IA-09, IA-20 |
| REF-132 | IA-09, IA-20 |
| REF-133 | IA-11 |
| REF-134 | IA-11, IA-17 |
| REF-135 | IA-11, IA-18 |
| REF-136 | IA-12 |
| REF-137 | IA-12, IA-15 |
| REF-138 | IA-12, IA-16 |
| REF-139 | IA-01, IA-14 |
| REF-140 | IA-13 |
| REF-141 | IA-13 |
| REF-142 | IA-14, IA-25 |

### 13.3 Répartition par mode de validation

| Mode | Nombre d'exercices |
|---|---|
| SingleValue | 67 |
| NumericTolerance | 44 |
| GeometryTolerance | 34 |
| — | 23 |
| ExactOrderedList | 21 |
| SetEquality | 12 |
| Visuel | 9 |
| Conceptuel (QCM) | 1 |

### 13.4 Journal des indices

| Indice | Objet | Date | Auteur |
|---|---|---|---|
| Ind. A | Création. Définition de la trame, des conventions de fichier et du catalogue de 211 exercices répartis en 4 lots. | 25/08/2026 | C. THIERRY DE VILLE D'AVRAY |
| Ind. B | Référentiel unifié : les références des exercices passent aux identifiants continus `REF-nnn`, sans distinction de provenance. Ajout des règles d'étanchéité entre zones et d'affichage conditionnel du corrigé, et des fiches Word illustrées. | 26/08/2026 | C. THIERRY DE VILLE D'AVRAY |

---

*Fin du document — v0.3-260826 Ind. B — 26/08/2026*
