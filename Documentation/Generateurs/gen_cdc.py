# -*- coding: utf-8 -*-
"""Genere le cahier des charges detaille des exercices Magpie au format Markdown."""
import os, sys, io
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lots import LOTS as _REGISTRE, TOUS as _TOUS
# LOT_A reste employe plus bas pour le jalonnement des tests.
LOT_A = [e for c, n, d, lot in _REGISTRE if c == "A" for e in lot]
from skill_a import SKILL, CONNAISSANCES
from exos_b import LOT_B, LOT_C
from exos_g import LOT_G

PROJ = r"C:\Users\charl\.claude\projects\MAGPIE"
DOC = os.path.join(PROJ, "Documentation")
if not os.path.isdir(DOC):
    os.makedirs(DOC)
OUT = os.path.join(DOC, "CAHIER_DES_CHARGES_EXERCICES_MAGPIE - IndB - 01-09-2026.md")

VERSION = "v0.5-260902"
INDICE = "Ind. C"
DATE = "01/09/2026"

# Les lots produits viennent du registre ; les lots encore a produire (B, C, G)
# restent decrits ici, a partir de leurs fiches d'origine.
_NIV = {"A": "Débutant", "IA": "Débutant à perfectionnement",
        "RH": "Débutant", "GP": "Débutant à perfectionnement",
        "QT": "Intermédiaire", "FA": "Perfectionnement",
        "PL": "Débutant à intermédiaire",
        "MP": "Intermédiaire à perfectionnement",
        "AV": "Perfectionnement", "DV": "Expert",
        "WB": "Perfectionnement à expert"}
_DESC = {
 "A": "Un exercice par famille de composants natifs de Grasshopper pour Rhino 8. "
      "Aucun plugin tiers n'est autorisé dans ce lot.",
 "IA": "L'intelligence artificielle appliquée à Grasshopper : formuler une demande "
       "exploitable, faire produire un composant scripté, conduire un plugin avec un "
       "agent de code, apprendre d'un jeu de mesures, appeler un modèle de langage, "
       "piloter par un protocole d'agent, et vérifier ce qui revient.",
 "RH": "Le socle Rhino, prérequis de tout le reste. Ce qui produit une géométrie se "
       "valide en la référençant dans Grasshopper et en la mesurant ; ce qui relève de "
       "l'interface ne produit rien de mesurable et devient une question charnière.",
 "GP": "Géométrie paramétrique appliquée : plan coté qui suit ses paramètres, modèle 3D "
       "complet, maillages et SubD.",
 "QT": "Métré, chiffrage et export de données — les gestes que le métier demande le plus "
       "souvent, tous à réponse numérique.",
 "FA": "Aide à la fabrication : estimation d'imbrication et mise à plat.",
 "PL": "L'écosystème de plugins. Presque tout y est connaissance — installer, choisir, "
       "juger — et devient donc question charnière. Un seul exercice, sur l'ergonomie "
       "réellement mise à l'épreuve.",
 "MP": "Méthode et performance : rendre une définition reprenable par un tiers, trouver "
       "ce qui coûte réellement le temps de calcul, comprendre le modèle évènementiel.",
 "AV": "Algorithmique avancée : converger par itérations sur un critère, conduire une "
       "simulation jusqu'à l'équilibre, poser un problème de recherche de forme.",
 "DV": "Développement : quand scripter plutôt que câbler, employer l'interface de "
       "programmation de Rhino, et passer du composant scripté au plugin installé.",
 "WB": "Interfaces et web : rendre une définition utilisable par un tiers, la publier en "
       "ligne, et distinguer ce que Rhino.Inside et Rhino.Compute font respectivement.",
}
LOTS = [(c, n, _NIV.get(c, "—"), lot, _DESC.get(c, ""))
        for c, n, _d, lot in _REGISTRE]
LOTS += [
    ("B", "Algorithmes combinés", "Intermédiaire", LOT_B,
     "Un exercice par situation de conception réaliste, résolue en combinant plusieurs "
     "composants. Spécifié, pas encore produit."),
    ("C", "Projets appliqués", "Expérimenté", LOT_C,
     "Un projet complet par domaine métier — architecture, mobilier, joaillerie, "
     "fabrication. Spécifié, pas encore produit."),
    ("G", "Exercices gamifiés", "Tous niveaux", LOT_G,
     "Un exercice par technique de gamification, transverse aux autres lots. "
     "Spécifié, pas encore produit."),
]


def fiche(e, lot_code):
    """Rend une fiche d'exercice selon la trame standard, identique pour tous les lots."""
    gamif = e.get("gamif") or e.get("tech") or "—"
    impl = e.get("impl") or (
        "Exercice standard : Magpie charge les composants de départ décrits ci-dessus, affiche l'énoncé "
        "dans la zone SUJET et compare la sortie branchée sur le paramètre de réponse en mode %s." % e["mode"])
    L = []
    L.append("#### %s — %s\n" % (e["id"], e["titre"]))
    L.append("| Rubrique | Valeur |")
    L.append("|---|---|")
    L.append("| **Lot** | %s |" % lot_code)
    L.append("| **Thématique** | %s |" % e["them"])
    L.append("| **Réf. référentiel** | %s |" % e["ref"])
    L.append("| **Niveau** | %s |" % e["niv"])
    L.append("| **Durée cible** | %d min |" % e["duree"])
    L.append("| **Prérequis** | %s |" % e["prereq"])
    if e.get("competence") and e["competence"] != u"—":
        L.append("| **Compétence visée** | %s |" % e["competence"])
    if e.get("bloom"):
        L.append("| **Case Bloom (révisée)** | %s |" % e["bloom"])
    if e.get("verdict") == u"connaissance":
        L.append("| **Nature** | Connaissance — question charnière, non notée |")
        L.append("| **Mode de validation** | — |")
    else:
        L.append("| **Mode de validation** | %s — tolérance %s |" % (e["mode"], e["tol"]))
        L.append("| **Solution de référence** | %s composants |" % e["nb"])
    L.append("| **Gamification associée** | %s |" % gamif)
    L.append("| **Statut de production** | À produire |")
    L.append("")
    L.append("**1. Compétence visée** — %s" % e["obj"])
    L.append("")
    if e.get("contexte"):
        L.append("**1 bis. Contexte métier** — %s" % e["contexte"])
        L.append("")
    if e.get("verdict") == u"connaissance":
        L.append("**2. Question charnière** — cet item ne donne pas lieu à un "
                 "exercice noté : la réponse s'obtiendrait en sachant, non en "
                 "construisant.")
        L.append("")
        for _l in (e.get("charniere") or u"").split(chr(10)):
            L.append(_l)
        L.append("")
        L.append("**2 bis. Énoncé d'origine, conservé pour mémoire**")
        L.append("")
        L.append("> *%s*" % e.get("enonce_origine", e["enonce"]))
        L.append("")
    else:
        L.append("**2. Composants mobilisés** — %s" % e["comp"])
        L.append("")
        L.append("> Cette liste ne figure pas sur la fiche remise à "
                 "l'apprenant : nommer l'outil reviendrait à donner la réponse.")
        L.append("")
        L.append("**3. Zone SUJET — texte du Scribble**")
        L.append("")
        L.append("> %s" % e["enonce"])
        L.append("")
    L.append("**4. Données de départ fournies** — %s" % e["depart"])
    L.append("")
    L.append("**5. Résultat attendu** — %s" % e["att"])
    L.append("")
    L.append("**6. Zone CORRIGÉ — explication étape par étape**")
    L.append("")
    for i, s in enumerate(e["etapes"], 1):
        L.append("%d. %s" % (i, s))
    L.append("")
    if e.get("erreur"):
        L.append("**6 bis. Erreur attendue** — %s" % e["erreur"])
        L.append("")
    if e.get("donnees_note"):
        L.append("**6 ter. Justification du jeu de données** — %s" % e["donnees_note"])
        L.append("")
    if e.get("limite"):
        L.append("**6 quater. Limite de la correction automatique** — %s" % e["limite"])
        L.append("")
    if e.get("alerte"):
        L.append("**6 quinquies. Note au formateur** — %s" % e["alerte"])
        L.append("")
    L.append("**7. Pièges fréquents**")
    L.append("")
    for p in e["pieges"]:
        L.append("- %s" % p)
    L.append("")
    L.append("**8. Variantes et extensions**")
    L.append("")
    for v in e["var"]:
        L.append("- %s" % v)
    L.append("")
    L.append("**9. Mise en œuvre dans Magpie** — %s" % impl)
    L.append("")
    L.append("**10. Barème** — %s" % e["bareme"])
    L.append("")
    return "\n".join(L)


M = []
A = M.append

A("# CAHIER DES CHARGES — EXERCICES MAGPIE")
A("")
A("**Bibliothèque d'exercices Grasshopper autocorrigés pour Rhino 8**")
A("")
A("| | |")
A("|---|---|")
A("| Projet | MAGPIE — outil d'exercices Grasshopper autocorrigés (RhinoForYou) |")
A("| Document | Cahier des charges de la bibliothèque d'exercices |")
A("| Version | **%s** — **%s** |" % (VERSION, INDICE))
A("| Date | %s |" % DATE)
A("| Rédacteur | Charles THIERRY DE VILLE D'AVRAY |")
A("| Destinataires | Jérémy CAROLUS, Jacques HABABOU |")
A("| Documents de référence | *Fondamentaux Grasshopper – Ind. B – 26-08-2026.xlsx*, "
  "*Compte rendu de session du 11/08/2026*, *Trame de suivi projet Magpie.xlsx*, "
  "programmes de formation du catalogue RhinoForYou |")
A("| Statut | Pour revue |")
A("")
nb_tot = sum(len(l[3]) for l in LOTS)
A("Ce document décrit **%d exercices** répartis en 4 lots et %d thématiques. "
  "Chaque exercice est décrit selon une trame identique en 10 rubriques, "
  "afin que la production puisse être répartie entre plusieurs contributeurs sans perte d'homogénéité."
  % (nb_tot, len(set(e["them"] for l in LOTS for e in l[3]))))
A("")
A("---")
A("")

# ---------------------------------------------------------------- SOMMAIRE
A("## Sommaire")
A("")
A("1. [Objet et périmètre](#1-objet-et-périmètre)")
A("2. [Principes pédagogiques](#2-principes-pédagogiques)")
A("3. [Structure imposée du fichier Grasshopper](#3-structure-imposée-du-fichier-grasshopper)")
A("4. [Conventions techniques](#4-conventions-techniques)")
A("5. [Modes de validation et métriques](#5-modes-de-validation-et-métriques)")
A("6. [Trame standard d'une fiche d'exercice](#6-trame-standard-dune-fiche-dexercice)")
A("7. [Nommage et arborescence des livrables](#7-nommage-et-arborescence-des-livrables)")
A("8. [Catalogue des exercices](#8-catalogue-des-exercices)")
for code, nom, niv, lst, desc in LOTS:
    A("    - [Lot %s — %s](#lot-%s--%s) — %d exercices" % (
        code, nom, code.lower(), nom.lower().replace(" ", "-"), len(lst)))
A("9. [Bibliothèque des techniques de gamification](#9-bibliothèque-des-techniques-de-gamification)")
A("10. [Plan de production](#10-plan-de-production)")
A("11. [Critères d'acceptation](#11-critères-dacceptation)")
A("12. [Points ouverts](#12-points-ouverts)")
A("13. [Annexes](#13-annexes)")
A("")
A("---")
A("")

# ------------------------------------------------------------------- 1. OBJET
A("## 1. Objet et périmètre")
A("")
A("### 1.1 Objet")
A("")
A("Le présent cahier des charges définit le contenu, la structure et les règles de production "
  "de la bibliothèque d'exercices Grasshopper de l'outil Magpie. Il couvre :")
A("")
A("- les exercices simples de découverte des composants natifs de Grasshopper pour Rhino 8 ;")
A("- les exercices intermédiaires combinant plusieurs composants ou groupes de composants "
  "pour aboutir à un algorithme solution, dans différents domaines de conception ;")
A("- les projets complexes appliqués à l'architecture, au design de mobilier, à la joaillerie et à la fabrication ;")
A("- un lot d'exercices gamifiés mobilisant une trentaine de techniques de jeu.")
A("")
A("### 1.2 Ce que le document ne couvre pas")
A("")
A("- Le développement du plugin Magpie lui-même, traité dans la trame de suivi du projet.")
A("- Le moteur de comparaison géométrique, dont les limites actuelles sont rappelées au chapitre 5.")
A("- Les questions de propriété intellectuelle et de licence des exercices, ouvertes à ce jour.")
A("")
A("### 1.3 Rattachement au référentiel")
A("")
A("Chaque exercice porte une référence explicite vers une ou plusieurs lignes du fichier "
  "*Fondamentaux Grasshopper – Ind. B – 26-08-2026.xlsx*, sous la forme `REF-nnn`. "
  "Le référentiel est unifié : un identifiant unique et continu couvre les 116 notions, "
  "sans distinction de provenance. Cette référence est la clé de traçabilité entre l'offre "
  "de formation, le référentiel de notions et les exercices.")
A("")
A("---")
A("")

# ------------------------------------------------------- 2. PRINCIPES PEDAGO
A("## 2. Principes pédagogiques")
A("")
A("### 2.1 Une notion, un geste, une preuve")
A("")
A("Un exercice du lot A porte sur **une seule notion** et se valide par **un seul résultat vérifiable**. "
  "Un exercice qui ne peut pas être validé automatiquement doit être reformulé en QCM plutôt qu'en manipulation.")
A("")
A("### 2.2 Progression par dépendance, pas par difficulté ressentie")
A("")
A("L'ordre des exercices suit l'ordre de dépendance des notions du référentiel. Un exercice ne mobilise "
  "que des notions déjà traitées, à l'exception de son objet propre. La colonne **Prérequis** de chaque fiche "
  "matérialise cette contrainte et doit être respectée lors de la composition des parcours.")
A("")
A("### 2.3 Réalisme des situations")
A("")
A("À partir du lot B, chaque énoncé décrit une situation professionnelle plausible, avec des cotes, "
  "des matériaux et des contraintes réelles. Les exercices artificiels, faciles à reproduire sans comprendre, "
  "sont proscrits : la valeur de Magpie tient à sa capacité à mesurer une compétence utile.")
A("")
A("### 2.4 Le corrigé fait partie du livrable")
A("")
A("Chaque fichier d'exercice contient son propre corrigé commenté, placé sous la zone SUJET. "
  "L'apprenant y accède après validation ou après épuisement de ses tentatives. Le corrigé n'est pas "
  "une simple solution : il explique le raisonnement étape par étape et signale les pièges fréquents.")
A("")
A("### 2.5 Générique d'abord, métier ensuite")
A("")
A("Les lots A et B constituent le socle commun à tous les utilisateurs de Grasshopper. "
  "Le lot C, spécialisé par métier, ne doit être produit qu'une fois le socle testé auprès de profils réellement débutants.")
A("")
A("### 2.6 Validation humaine obligatoire")
A("")
A("Tout exercice, énoncé, corrigé ou illustration produit avec l'aide de l'intelligence artificielle "
  "fait l'objet d'une relecture technique et pédagogique par un formateur avant intégration à la bibliothèque.")
A("")
A("---")
A("")

# ------------------------------------------- 3. STRUCTURE DU FICHIER GH
A("## 3. Structure imposée du fichier Grasshopper")
A("")
A("Tout fichier d'exercice `.gh` respecte la même organisation verticale sur le canvas. "
  "Cette contrainte est **impérative** : elle permet d'automatiser l'extraction de la zone sujet, "
  "de masquer le corrigé et de générer les captures d'illustration.")
A("")
A("```")
A("┌──────────────────────────────────────────────────────────────────────────┐")
A("│  BANDEAU  (y = 0)                                                        │")
A("│  Scribble titre : « A-14 · Filtrer avec Cull Pattern »                    │")
A("│  Scribble méta  : niveau · durée cible · réf. référentiel · version       │")
A("├──────────────────────────────────────────────────────────────────────────┤")
A("│  ZONE SUJET  (y = -100 à -600)          groupe nommé  ZONE_SUJET          │")
A("│  Couleur de groupe : bleu clair (200, 220, 245)                           │")
A("│                                                                          │")
A("│  ├─ Scribble ÉNONCÉ  (police 16, largeur max 900 px)                      │")
A("│  ├─ Composants de départ fournis, regroupés dans DONNEES_DE_DEPART        │")
A("│  ├─ Emplacement de travail libre, matérialisé par un cadre pointillé      │")
A("│  └─ Paramètre de réponse nommé  REPONSE  (bordure orange)                 │")
A("├──────────────────────────────────────────────────────────────────────────┤")
A("│  SÉPARATEUR : Scribble « ▼ CORRIGÉ — à consulter après validation ▼ »     │")
A("├──────────────────────────────────────────────────────────────────────────┤")
A("│  ZONE CORRIGÉ  (y = -800 et au-delà)    groupe nommé  ZONE_CORRIGE        │")
A("│  Couleur de groupe : vert clair (215, 240, 215)                           │")
A("│                                                                          │")
A("│  ├─ Sous-groupe ÉTAPE 1 + Scribble d'explication                          │")
A("│  ├─ Sous-groupe ÉTAPE 2 + Scribble d'explication                          │")
A("│  ├─ …                                                                    │")
A("│  ├─ Sous-groupe PIÈGES (couleur rouge clair) + Scribbles                  │")
A("│  └─ Paramètre  SOLUTION_REFERENCE                                         │")
A("└──────────────────────────────────────────────────────────────────────────┘")
A("```")
A("")
A("### 3.1 Règles de la zone SUJET")
A("")
A("| Règle | Exigence |")
A("|---|---|")
A("| Énoncé | Un Scribble unique, texte intégral repris à l'identique de la rubrique 3 de la fiche |")
A("| Longueur de l'énoncé | 40 mots maximum pour le lot A, 80 mots pour les lots B et G, 120 mots pour le lot C |")
A("| Composants de départ | Regroupés, verrouillés en position, aperçu actif |")
A("| Données internalisées | Systématiquement, sauf géométrie lourde livrée en fichier 3DM externe |")
A("| Paramètre de réponse | Un seul, nommé `REPONSE`, du type attendu par le mode de validation |")
A("| État initial | Le fichier ouvert ne doit produire ni erreur ni avertissement |")
A("")
A("### 3.2 Règles de la zone CORRIGÉ")
A("")
A("| Règle | Exigence |")
A("|---|---|")
A("| Un sous-groupe par étape | Le découpage suit exactement la rubrique 6 de la fiche |")
A("| Scribble d'explication | Placé au-dessus de chaque sous-groupe, une à trois phrases |")
A("| Numérotation | `ÉTAPE 1`, `ÉTAPE 2`, … cohérente avec la fiche |")
A("| Pièges | Un sous-groupe dédié, avec le montage fautif et son commentaire |")
A("| Aperçu | Désactivé sur tous les composants du corrigé, pour ne pas polluer la vue |")
A("| Décalage vertical | Au moins 200 px sous la zone sujet, pour un masquage fiable |")
A("")
A("### 3.3 Deux règles structurantes")
A("")
A("**Règle 1 — aucun câble ne relie les deux zones.** Les composants du sujet dont le corrigé "
  "a besoin y sont **recopiés**, avec leurs données internalisées, dans un groupe "
  "`DONNÉES FOURNIES (copie)` placé en tête de la zone corrigé. Le câblage interne du sujet est "
  "rejoué entre ces copies. Les deux zones sont ainsi totalement indépendantes : on peut "
  "supprimer l'une sans toucher l'autre, et aucun fil ne traverse le canvas.")
A("")
A("**Règle 2 — le corrigé est masqué tant qu'il n'est pas demandé.** L'aperçu est coupé sur "
  "tous les composants du corrigé, et son résultat traverse un `Stream Gate` piloté par un "
  "`Boolean Toggle` nommé **AFFICHER LE CORRIGÉ**, à faux par défaut. Tant qu'il reste sur faux, "
  "la sortie est vide et **rien n'apparaît dans Rhino** ; le remettre sur faux fait disparaître "
  "le résultat. Seul le paramètre `REPONSE_CORRIGE`, en aval de la porte, a son aperçu actif.")
A("")
A("> Limite à connaître : Grasshopper ne permet pas de faire disparaître des composants du "
  "canvas selon une valeur booléenne. Les composants du corrigé restent donc visibles sur le "
  "canvas du fichier `_complet.gh` ; c'est leur *résultat* qui est commandé par l'interrupteur. "
  "Le fichier à remettre à l'apprenant reste `_sujet.gh`, qui ne contient aucun corrigé.")
A("")
A("### 3.4 Deux fichiers par exercice")
A("")
A("| Fichier | Contenu | Usage |")
A("|---|---|---|")
A("| `<ID>_sujet.gh` | Zone bandeau et zone sujet uniquement | Chargé par Magpie pour l'apprenant |")
A("| `<ID>_complet.gh` | Bandeau, sujet et corrigé | Support de formation, référence, génération du JSON |")
A("| `<ID>_fiche.md` | Fiche détaillée : sujet et corrigé | Formateur, préparation de séance |")
A("| `<ID>_fiche_sujet.md` | La même, sans le corrigé | Remise à l'apprenant |")
A("")
A("Le fichier `_complet.gh` est la source de vérité. Le fichier `_sujet.gh` en est dérivé "
  "par suppression du groupe `ZONE_CORRIGE`.")
A("")
A("---")
A("")

# ---------------------------------------------------- 4. CONVENTIONS TECHNIQUES
A("## 4. Conventions techniques")
A("")
A("### 4.1 Environnement de référence")
A("")
A("| Élément | Valeur |")
A("|---|---|")
A("| Logiciel | Rhino 8 (version de service la plus récente au moment de la production) |")
A("| Grasshopper | Version intégrée à Rhino 8 |")
A("| Unités du document | Millimètres |")
A("| Tolérance absolue du document | 0,001 mm |")
A("| Tolérance angulaire | 0,1 degré |")
A("| Langue de l'interface | Français, noms de composants en anglais |")
A("")
A("### 4.2 Plugins autorisés par lot")
A("")
A("| Lot | Plugins autorisés |")
A("|---|---|")
A("| A | Aucun. Composants natifs exclusivement. |")
A("| B | Aucun par défaut ; un plugin nommé explicitement dans l'énoncé est autorisé (Anemone, OpenNest). |")
A("| C | Anemone, Kangaroo, Galapagos, Weaverbird, OpenNest, LunchBox, Human, Elefront, selon l'énoncé. |")
A("| G | Human (retour sonore et visuel), Metahopper (introspection du canvas). |")
A("")
A("Tout plugin employé doit être mentionné dans la rubrique 2 de la fiche et signalé à l'apprenant "
  "dans le bandeau du fichier. Un exercice ne doit jamais échouer silencieusement faute de plugin installé : "
  "le fichier comporte un contrôle de présence en tête de la zone sujet.")
A("")
A("### 4.3 Nommage sur le canvas")
A("")
A("| Élément | Convention | Exemple |")
A("|---|---|---|")
A("| Groupe principal | Majuscules, sous-tirets | `ZONE_SUJET` |")
A("| Sous-groupe d'étape | `ÉTAPE n — libellé` | `ÉTAPE 3 — Filtrage` |")
A("| Paramètre d'entrée fourni | Majuscules | `COURBE_GUIDE` |")
A("| Paramètre de réponse | `REPONSE` | — |")
A("| Slider paramétrable | Nom métier, unité entre parenthèses | `Hauteur (mm)` |")
A("")
A("### 4.4 Géométrie externe")
A("")
A("La géométrie est internalisée dans le fichier chaque fois que la taille du fichier reste inférieure à 2 Mo. "
  "Au-delà — maillages denses, projets réels — un fichier `3DM` externe est livré avec l'exercice, "
  "référencé par un `Geometry Pipeline` sur un calque au nom normalisé. "
  "Le nom du calque attendu est indiqué dans l'énoncé.")
A("")
A("---")
A("")

# ------------------------------------------------- 5. VALIDATION ET METRIQUES
A("## 5. Modes de validation et métriques")
A("")
A("### 5.1 Modes de validation")
A("")
A("| Mode | Nature du résultat | Tolérance | Emploi recommandé |")
A("|---|---|---|---|")
A("| `ExactOrderedList` | Liste dont l'ordre compte | Aucune | Tri, séries, entrelacement |")
A("| `SetEquality` | Ensemble, ordre indifférent | Aucune | Filtrage, répartition, structure d'arbre |")
A("| `SingleValue` | Valeur unique | Aucune ou numérique | Comptage, valeur calculée, booléen |")
A("| `NumericTolerance` | Valeur numérique | Relative ou absolue | Mesures, métrés, chiffrage |")
A("| `GeometryTolerance` | Géométrie | Absolue en mm | Construction géométrique |")
A("| `Conceptuel (QCM)` | Choix dans une liste | Aucune | Notions non mesurables par comparaison |")
A("")
A("### 5.2 Limite connue du moteur de comparaison")
A("")
A("La comparaison géométrique repose actuellement sur des grandeurs globales — boîte englobante, volume, "
  "aire — assorties d'une tolérance. Cette approche convient aux exercices des lots A et B. "
  "Pour le lot C, elle est insuffisante : deux solutions de topologies différentes peuvent présenter "
  "le même volume. **Recommandation** : pour chaque exercice du lot C, définir un jeu d'au moins trois "
  "indicateurs indépendants (volume, aire développée, nombre d'éléments, position d'un point remarquable) "
  "et valider sur leur conjonction, en attendant l'évolution du moteur.")
A("")
A("### 5.3 Métriques collectées")
A("")
A("| Métrique | Usage | Calibration |")
A("|---|---|---|")
A("| Taux de réussite | Validation et déclenchement du certificat | Seuil par parcours |")
A("| Temps total | Comparaison à une durée cible | À calibrer sur des utilisateurs réels avant activation |")
A("| Nombre de composants | Sobriété de la solution | Comparé au champ *Solution de référence* de la fiche |")
A("| Nombre de tentatives | Difficulté ressentie | Alimente les mécaniques de vies et d'indices |")
A("| Écart au chemin attendu | Détection d'une solution sur-complexifiée | Tolérance de 1 à 2 composants |")
A("")
A("### 5.4 Règle sur les durées cibles")
A("")
A("Les durées indiquées dans les fiches sont des **estimations de conception**, non mesurées. "
  "Elles ne doivent pas être utilisées comme critère bloquant tant qu'elles n'ont pas été calibrées "
  "par des mesures réelles : d'abord auprès des formateurs, puis auprès d'un échantillon d'apprenants représentatifs.")
A("")
A("---")
A("")

# --------------------------------------------------------------- 6. TRAME
A("## 6. Trame standard d'une fiche d'exercice")
A("")
A("Toutes les fiches du chapitre 8 suivent strictement la trame suivante. "
  "Aucune rubrique ne peut être omise ; une rubrique sans contenu porte la mention « sans objet ».")
A("")
A("| # | Rubrique | Contenu attendu |")
A("|---|---|---|")
A("| — | En-tête | Identifiant, titre, lot, thématique, référence au référentiel, niveau, durée cible, prérequis, mode de validation et tolérance, taille de la solution de référence, technique de gamification associée, statut de production |")
A("| 1 | Objectif pédagogique | Une phrase énonçant la compétence visée, formulée du point de vue de l'apprenant |")
A("| 2 | Composants mobilisés | Liste des composants, nom anglais, plugin indiqué le cas échéant |")
A("| 3 | Zone SUJET — texte du Scribble | Texte exact à reporter dans le fichier `.gh`, sans reformulation |")
A("| 4 | Données de départ fournies | Composants pré-placés, géométrie internalisée, fichier 3DM externe |")
A("| 5 | Résultat attendu | Description non ambiguë de ce qui est comparé |")
A("| 6 | Zone CORRIGÉ — explication étape par étape | Étapes numérotées, une action par étape, correspondant aux sous-groupes du fichier |")
A("| 7 | Pièges fréquents | Erreurs réellement observées ou anticipées, avec leur symptôme |")
A("| 8 | Variantes et extensions | Déclinaisons possibles pour renouveler l'exercice ou monter en difficulté |")
A("| 9 | Mise en œuvre dans Magpie | Ce que le plugin doit faire, et le cas échéant ce qu'il ne sait pas encore faire |")
A("| 10 | Barème | Répartition des points et seuil de validation |")
A("")
A("---")
A("")

# ---------------------------------------------------- 7. NOMMAGE ARBORESCENCE
A("## 7. Nommage et arborescence des livrables")
A("")
A("```")
A("/EXERCICES/")
A("    /LOT A - Composants natifs/")
A("        A-01 Premier flux de donnees/")
A("            A-01_sujet.gh")
A("            A-01_complet.gh")
A("            A-01.json                  ← descripteur Magpie")
A("            A-01_fiche.md              ← fiche detaillee : sujet ET corrige")
A("            A-01_fiche_sujet.md        ← fiche sans le corrige, pour l'apprenant")
A("            A-01_illustration.png")
A("            /Ressources/               ← 3DM externes eventuels")
A("    /LOT B - Algorithmes combines/")
A("    /LOT C - Projets appliques/")
A("    /LOT G - Exercices gamifies/")
A("/PARCOURS/")
A("    Parcours 01 - Decouverte.json")
A("    Parcours 02 - Donnees et listes.json")
A("/Documentation/")
A("/Journal des modifications/")
A("/Anciens fichiers/")
A("```")
A("")
A("### 7.1 Identifiant d'exercice")
A("")
A("`<LOT>-<NN>` où `<LOT>` vaut A, B, C ou G et `<NN>` un numéro à deux chiffres. "
  "L'identifiant est **stable** : il ne change jamais, même si l'exercice est remanié. "
  "Un exercice retiré voit son identifiant réservé et non réattribué.")
A("")
A("### 7.2 Versionnage")
A("")
A("Chaque exercice porte une version au format `v0.1-AAMMJJ` affichée dans le bandeau du fichier `.gh` "
  "et reprise dans le descripteur JSON. La bibliothèque dans son ensemble porte un indice de révision "
  "(`Ind. A`, `Ind. B`, …) porté par le présent cahier des charges.")
A("")
A("---")
A("")

# ------------------------------------------------------------- 8. CATALOGUE
A("## 8. Catalogue des exercices")
A("")
A("### 8.0 Vue d'ensemble")
A("")
A("| Lot | Intitulé | Niveau | Nombre d'exercices | Durée cumulée |")
A("|---|---|---|---|---|")
for code, nom, niv, lst, desc in LOTS:
    A("| **%s** | %s | %s | %d | %d h %02d |" % (
        code, nom, niv, len(lst), sum(e["duree"] for e in lst) // 60, sum(e["duree"] for e in lst) % 60))
tot_min = sum(e["duree"] for c, n, v, l, d in LOTS for e in l)
A("| | **Total** | | **%d** | **%d h %02d** |" % (nb_tot, tot_min // 60, tot_min % 60))
A("")

for code, nom, niv, lst, desc in LOTS:
    A("---")
    A("")
    A("## Lot %s — %s" % (code, nom))
    A("")
    A("**Niveau** : %s · **%d exercices** · **%d h %02d cumulées**"
      % (niv, len(lst), sum(e["duree"] for e in lst) // 60, sum(e["duree"] for e in lst) % 60))
    A("")
    A(desc)
    A("")
    # index du lot
    A("| ID | Titre | Thématique | Niveau | Durée | Validation |")
    A("|---|---|---|---|---|---|")
    for e in lst:
        A("| %s | %s | %s | %s | %d min | %s |" % (
            e["id"], e["titre"], e["them"], e["niv"], e["duree"], e["mode"]))
    A("")
    # fiches par thematique
    themes = OrderedDict()
    for e in lst:
        themes.setdefault(e["them"], []).append(e)
    for th, exos in themes.items():
        A("### %s" % th)
        A("")
        A("*%d exercices — %s*" % (len(exos), ", ".join(e["id"] for e in exos)))
        A("")
        for e in exos:
            A(fiche(e, "%s — %s" % (code, nom)))

# --------------------------------------------------------- 9. GAMIFICATION
A("---")
A("")
A("## 9. Bibliothèque des techniques de gamification")
A("")
A("Le lot G met en œuvre **%d techniques**, chacune portée par un exercice dédié. "
  "Le tableau ci-dessous sert de bibliothèque de référence : une technique peut être réemployée "
  "sur n'importe quel exercice des lots A, B ou C." % len(LOT_G))
A("")
A("| Technique | Exercice porteur | Famille | Ce que le plugin doit fournir | Réemployable sur |")
A("|---|---|---|---|---|")
FAM = {"G1": "Progression et récompense", "G2": "Exploration et découverte",
       "G3": "Manipulation et adresse", "G4": "Connaissance et mémorisation",
       "G5": "Performance et compétition", "G6": "Sensations et immersion",
       "G7": "Régularité et communauté"}
BESOIN = {
 "G-01": ("Score partiel par sous-critère", "Tout exercice à sous-critères"),
 "G-02": ("Taux de réussite partiel exposé en cours d'exercice", "Exercices en plusieurs formes"),
 "G-03": ("Durée cible et compte à rebours affiché", "Tout exercice court"),
 "G-04": ("Limitation du nombre de tentatives et rechargement", "Exercices à réponse unique"),
 "G-05": ("Identifiants de badge dans le résultat et sur le certificat", "Familles complètes de notions"),
 "G-06": ("Verrouillage du bouton Suivant — déjà présent", "Tout parcours"),
 "G-07": ("Métriques nombre de composants et robustesse paramétrique", "Lots A et B"),
 "G-08": ("État de série conservé entre exercices d'un parcours", "Parcours de micro-exercices"),
 "G-09": ("Validation sur chaîne de caractères insensible à la casse", "Tout exercice"),
 "G-10": ("Graine aléatoire figée dans le descripteur", "Exercices à jeu de données variable"),
 "G-11": ("Validation sur un mot final unique", "Vocabulaire des composants"),
 "G-12": ("Validation d'une liste de couples en SetEquality", "Associations notion / effet"),
 "G-13": ("Validation d'un triplet de valeurs", "Motifs cycliques"),
 "G-14": ("Contrôle strict du nombre de composants", "Lecture de graphe"),
 "G-15": ("Validation géométrique et contrôle de fermeture", "Géométrie 2D"),
 "G-16": ("Décompte des indices consultés comme tentatives", "Recherche dans un grand jeu de données"),
 "G-17": ("Comparaison de valeurs de Value List", "Notions conceptuelles du référentiel"),
 "G-18": ("Comparaison d'une liste de booléens", "Idées reçues et pièges"),
 "G-19": ("Clusters protégés par mot de passe", "Comportement des composants"),
 "G-20": ("Contrôle du nombre de composants inchangé", "Diagnostic de définition"),
 "G-21": ("Métrique du nombre de composants comme score principal", "Tout exercice géométrique"),
 "G-22": ("Sous-critères tous obligatoires, seuil à 100 %", "Fin de chapitre"),
 "G-23": ("Export des trois métriques pour classement externe", "Tout exercice"),
 "G-24": ("Lecture de fichier audio embarqué", "Tout exercice"),
 "G-25": ("Validation sur deux états d'un même paramètre", "Algorithmes progressifs"),
 "G-26": ("Aucun besoin spécifique — retour porté par la définition", "Tout exercice de contrôle"),
 "G-27": ("Enchaînement scénarisé de parcours", "Parcours débutant"),
 "G-28": ("Conservation d'un code de configuration dans le profil", "Configurateurs"),
 "G-29": ("Sélection d'une variante par date dans le descripteur", "Micro-tâches"),
 "G-30": ("Import du fichier produit par l'apprenant précédent", "Travaux collectifs"),
 "G-31": ("Import du fichier de résultats — **fonction à créer**", "Bilan de parcours"),
 "G-32": ("Détection de l'ouverture d'un groupe d'indice", "Exercices difficiles"),
}
for e in LOT_G:
    fam = FAM.get(e["them"].split(" ")[0], e["them"])
    b = BESOIN.get(e["id"], ("—", "—"))
    A("| %s | %s — %s | %s | %s | %s |" % (
        e.get("tech", "—"), e["id"], e["titre"], fam, b[0], b[1]))
A("")
A("### 9.1 Règles d'emploi de la gamification")
A("")
A("- **Public adulte professionnel** : ton mesuré, humour discret, aucun effet infantilisant.")
A("- **La mécanique ne remplace jamais le contenu** : un exercice gamifié doit rester un exercice valide "
  "sans sa couche de jeu.")
A("- **Durée courte** : un test public ne dépasse pas dix questions, afin de préserver l'attention.")
A("- **Le son est toujours désactivable**, et jamais indispensable à la compréhension.")
A("- **Aucune mécanique aléatoire non reproductible** : toute graine est figée dans le descripteur, "
  "afin que la correction reste déterministe.")
A("- **Les récompenses sont partageables** : un badge doit pouvoir être publié sur un réseau professionnel.")
A("")
A("### 9.2 Techniques identifiées mais non retenues au premier lot")
A("")
A("| Technique | Raison |")
A("|---|---|")
A("| Monnaie virtuelle et boutique | Nécessite une gestion de compte persistante, hors périmètre de la V1 |")
A("| Classement mondial en temps réel | Nécessite un serveur, à traiter avec l'extension web |")
A("| Guildes et équipes permanentes | Suppose une communauté déjà constituée |")
A("| Notifications de rappel | Suppose une application mobile ou un envoi de courriels |")
A("| Réalité augmentée | Sans rapport avec le geste métier visé |")
A("")
A("---")
A("")

# ------------------------------------------------------- 10. PLAN DE PRODUCTION
A("## 10. Plan de production")
A("")
A("### 10.1 Ordre de production recommandé")
A("")
A("| Phase | Contenu | Volume | Condition de passage à la phase suivante |")
A("|---|---|---|---|")
A("| 1 | Exercices pilotes A-01, A-10, A-20, A-24 | 4 exercices | Validation de la structure de fichier et des modes de validation |")
A("| 2 | Lot A complet | %d exercices | Test par au moins deux profils réellement débutants |" % len(LOT_A))
A("| 3 | Lot G, familles G1 à G4 | 20 exercices | Retour d'expérience sur l'acceptabilité des mécaniques |")
A("| 4 | Lot B complet | %d exercices | Calibration des durées cibles sur utilisateurs réels |" % len(LOT_B))
A("| 5 | Lot G, familles G5 à G7 | 12 exercices | — |")
A("| 6 | Lot C complet | %d projets | Évolution préalable du moteur de comparaison géométrique |" % len(LOT_C))
A("")
A("### 10.2 Charge estimée")
A("")
A("Les durées ci-dessous sont des **estimations non mesurées**, à confirmer après production des exercices pilotes.")
A("")
A("| Lot | Exercices | Estimation par exercice | Estimation du lot |")
A("|---|---|---|---|")
# Le lot IA est estime plus haut que le lot A : la moitie de ses
# exercices demande un environnement (agent, plugin d'apprentissage,
# acces a un modele) a mettre en place et a documenter.
est = {"A": 1.5, "B": 4.0, "C": 8.0, "G": 2.5, "IA": 3.5,
       "RH": 2.0, "GP": 3.0, "QT": 2.5, "FA": 3.0, "PL": 2.0,
       "MP": 2.5, "AV": 4.0, "DV": 5.0, "WB": 5.0}
tot_h = 0
for code, nom, niv, lst, desc in LOTS:
    h = est.get(code, 3.0) * len(lst)
    tot_h += h
    A("| %s | %d | %s h | %s h |" % (code, len(lst), est.get(code, 3.0), round(h, 1)))
A("| | **%d** | | **%s h** |" % (nb_tot, round(tot_h, 1)))
A("")
A("Ce volume dépasse largement l'enveloppe initiale de dix heures de contribution. "
  "Il est donc proposé de traiter en priorité les phases 1 et 2, et de statuer sur la suite "
  "au vu des retours des premiers tests.")
A("")
A("### 10.3 Répartition proposée")
A("")
A("| Contributeur | Périmètre proposé |")
A("|---|---|")
A("| Jérémy CAROLUS | Structure des fichiers, descripteurs JSON, exercices pilotes, lot A |")
A("| Charles THIERRY DE VILLE D'AVRAY | Lot G, mécaniques de gamification, exercices de joaillerie et de mobilier |")
A("| Jacques HABABOU | Arbitrage pédagogique, cohérence avec l'offre RhinoForYou, tests utilisateurs |")
A("| À définir | Lot C, après clarification du moteur de comparaison |")
A("")
A("---")
A("")

# --------------------------------------------------- 11. CRITERES ACCEPTATION
A("## 11. Critères d'acceptation")
A("")
A("Un exercice n'est réputé livré que lorsque **tous** les points suivants sont vérifiés.")
A("")
A("| # | Critère | Vérification |")
A("|---|---|---|")
A("| 1 | Les deux fichiers `_sujet.gh` et `_complet.gh` existent et s'ouvrent sans erreur | Ouverture sur un poste vierge |")
A("| 2 | Le descripteur JSON est présent et cohérent avec la fiche | Comparaison champ à champ |")
A("| 3 | La zone sujet respecte la structure du chapitre 3 | Contrôle visuel |")
A("| 4 | La zone corrigé comporte un sous-groupe par étape de la fiche | Comparaison avec la rubrique 6 |")
A("| 5 | Le corrigé produit bien le résultat attendu | Exécution du corrigé et validation par Magpie |")
A("| 6 | L'exercice est validé par une solution différente du corrigé | Test par un second contributeur |")
A("| 7 | Une solution volontairement fausse est bien rejetée | Test négatif |")
A("| 8 | La tolérance retenue ne laisse pas passer une solution approximative | Test aux bornes |")
A("| 9 | Le nombre de composants de la solution de référence est renseigné et exact | Comptage |")
A("| 10 | La version est affichée dans le bandeau du fichier | Contrôle visuel |")
A("| 11 | Aucun chemin de fichier absolu ne subsiste | Ouverture depuis un autre dossier |")
A("| 12 | L'exercice a été réalisé par au moins une personne du niveau visé | Fiche de test signée |")
A("| 13 | La fiche d'exercice existe en version complète et en version sujet seul | Présence des deux `.md` |")
A("| 14 | Aucun objet ni groupe du corrigé ne subsiste dans le `_sujet.gh` | Contrôle automatisé d'étanchéité |")
A("| 15 | Aucun chevauchement d'objets sur le canvas | Audit de mise en page |")
A("| 16 | Aucun câble ne relie la zone sujet à la zone corrigé | Contrôle automatisé d'étanchéité des zones |")
A("| 17 | Interrupteur sur faux : le corrigé ne produit rien | Contrôle automatisé, les deux états testés |")
A("| 18 | La fiche Word existe en version complète et en version sujet seul, illustrées | Présence des deux `.docx` et des captures |")
A("")
A("---")
A("")

# ------------------------------------------------------------ 12. POINTS OUVERTS
A("## 12. Points ouverts")
A("")
A("| # | Point | Impact | Décision attendue de |")
A("|---|---|---|---|")
A("| 1 | Le moteur de comparaison géométrique ne distingue pas deux topologies de même volume | Bloque le lot C | Jérémy CAROLUS |")
A("| 2 | Magpie ne sait pas importer un fichier de résultats existant | Bloque l'exercice G-31 | Jérémy CAROLUS |")
A("| 3 | Aucun composant de lecture sonore n'est intégré au plugin | Bloque l'exercice G-24 sans Human | Jérémy CAROLUS |")
A("| 4 | Les durées cibles ne sont pas calibrées | Empêche l'activation du critère temps | Tous, après tests |")
A("| 5 | La propriété des exercices n'est pas qualifiée | Bloque la diffusion | Jacques HABABOU / VAC |")
A("| 6 | Les 10 fondamentaux V1 absents des programmes doivent-ils être ajoutés aux programmes ? | Cohérence offre / outil | Jacques HABABOU |")
A("| 7 | Le lot C mobilise des plugins tiers dont la disponibilité chez l'apprenant n'est pas garantie | Risque d'échec silencieux | Jérémy CAROLUS |")
A("| 8 | Volume total de production très supérieur à l'enveloppe initiale | Planification | Tous |")
A("")
A("---")
A("")

# ------------------------------------------------------------------ 13. ANNEXES
A("## 13. Annexes")
A("")
A("### 13.1 Récapitulatif de tous les exercices")
A("")
A("| ID | Titre | Lot | Thématique | Niveau | Durée | Validation | Réf. référentiel |")
A("|---|---|---|---|---|---|---|---|")
for code, nom, niv, lst, desc in LOTS:
    for e in lst:
        A("| %s | %s | %s | %s | %s | %d min | %s | %s |" % (
            e["id"], e["titre"], code, e["them"], e["niv"], e["duree"], e["mode"], e["ref"]))
A("")
A("### 13.2 Couverture du référentiel par les exercices")
A("")
refs = {}
for code, nom, niv, lst, desc in LOTS:
    for e in lst:
        for r in [x.strip() for x in e["ref"].split(",")]:
            if r:
                refs.setdefault(r, []).append(e["id"])
A("%d lignes du référentiel sont couvertes par au moins un exercice." % len(refs))
A("")
A("| Réf. référentiel | Exercices |")
A("|---|---|")
for r in sorted(refs):
    A("| %s | %s |" % (r, ", ".join(refs[r])))
A("")
A("### 13.3 Répartition par mode de validation")
A("")
modes = {}
for code, nom, niv, lst, desc in LOTS:
    for e in lst:
        modes[e["mode"]] = modes.get(e["mode"], 0) + 1
A("| Mode | Nombre d'exercices |")
A("|---|---|")
for m in sorted(modes, key=lambda x: -modes[x]):
    A("| %s | %d |" % (m, modes[m]))
A("")
A("### 13.4 Journal des indices")
A("")
A("| Indice | Objet | Date | Auteur |")
A("|---|---|---|---|")
A("| Ind. A | Création. Définition de la trame, des conventions de fichier et du catalogue de %d exercices "
  "répartis en 4 lots. | 25/08/2026 | C. THIERRY DE VILLE D'AVRAY |" % nb_tot)
A("| Ind. B | Référentiel unifié : les références des exercices passent aux identifiants continus "
  "`REF-nnn`, sans distinction de provenance. Ajout des règles d'étanchéité entre zones et "
  "d'affichage conditionnel du corrigé, et des fiches Word illustrées. | %s | "
  "C. THIERRY DE VILLE D'AVRAY |" % DATE)
A("")
A("---")
A("")
A("*Fin du document — %s %s — %s*" % (VERSION, INDICE, DATE))
A("")

io.open(OUT, "w", encoding="utf-8").write("\n".join(M))
print("OK ->", OUT)
print("Exercices :", nb_tot, "| Lignes MD :", len(M))
for code, nom, niv, lst, desc in LOTS:
    print("  Lot %s : %d exercices" % (code, len(lst)))
