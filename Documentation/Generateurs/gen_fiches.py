# -*- coding: utf-8 -*-
"""Genere une fiche d'exercice detaillee dans le dossier de chaque exercice.

Deux fichiers par exercice, sur le modele des .gh :
    <ID>_fiche.md         sujet ET corrige      -> formateur, reference
    <ID>_fiche_sujet.md   sujet seul            -> apprenant

Depuis la v0.3, les fiches sont produites a partir de la fusion entre exos_a.py
(le contenu d'origine) et skill_a.py (la couche de conception pedagogique issue
de la skill magpie-conception-exercices v2.3).

Les items requalifies en CONNAISSANCE ne produisent pas une fiche d'exercice
mais une fiche de question charniere : ils ne sont pas notes.

Aucune dependance externe, aucun besoin de Rhino.
"""
import os
import sys
import io

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)

from lots import LOTS as _LOTS
from skill_a import SKILL

PROJET = os.path.abspath(os.path.join(ICI, "..", ".."))

VERSION = "v0.4-260828"
INDICE = "Ind. B"
DATE = "26/08/2026"
LOT = "A — Découverte des composants natifs"

# reglages que l'API Grasshopper ne sait pas poser : repris des recettes
MANUELS = {}
try:
    sys.path.insert(0, os.path.join(ICI, "GH"))
    import recipes_a1, recipes_a2, recipes_a3, recipes_a4
    for m in (recipes_a1, recipes_a2, recipes_a3, recipes_a4):
        for k, v in m.R.items():
            if v.get("manuel"):
                MANUELS[k] = v["manuel"]
except Exception as e:
    print("  (réglages manuels non repris : %s)" % e)


def entete(e):
    connaissance = e.get("verdict") == u"connaissance"
    L = []
    L.append(u"# %s — %s" % (e["id"], e["titre"]))
    L.append(u"")
    if connaissance:
        L.append(u"**Question charnière Magpie** · Lot %s" % LOT)
        L.append(u"")
        L.append(u"> Cet item **n'est pas un exercice noté**. Il porte une "
                 u"connaissance nécessaire, mais qui s'acquiert et se vérifie "
                 u"par une question, non par un montage — la construire dans "
                 u"Grasshopper mesurerait la mémoire, pas la compétence.")
    else:
        L.append(u"**Fiche d'exercice Magpie** · Lot %s" % LOT)
    L.append(u"")
    L.append(u"| | |")
    L.append(u"|---|---|")
    L.append(u"| **Thématique** | %s |" % e["them"])
    L.append(u"| **Référence au référentiel** | %s |" % e["ref"])
    if e.get("competence") and e["competence"] != u"—":
        L.append(u"| **Compétence visée** | %s |" % e["competence"])
    if e.get("bloom"):
        L.append(u"| **Case Bloom (révisée)** | %s |" % e["bloom"])
    L.append(u"| **Niveau** | %s |" % e["niv"])
    L.append(u"| **Durée cible** | %d min |" % e["duree"])
    L.append(u"| **Prérequis** | %s |" % e["prereq"])
    if connaissance:
        L.append(u"| **Mode de validation** | — (non notée) |")
    else:
        L.append(u"| **Mode de validation** | %s — tolérance %s |"
                 % (e["mode"], e["tol"]))
        L.append(u"| **Solution de référence** | %s composants |" % e["nb"])
    L.append(u"| **Gamification associée** | %s |" % (e.get("gamif") or u"—"))
    L.append(u"| **Version** | %s — %s — %s |" % (VERSION, INDICE, DATE))
    L.append(u"| **Conception** | %s |" % SKILL)
    L.append(u"")
    return L


def charniere(e):
    """Fiche d'un item requalifie en connaissance."""
    L = []
    L.append(u"---")
    L.append(u"")
    L.append(u"## POURQUOI CE N'EST PAS UN EXERCICE")
    L.append(u"")
    L.append(u"L'énoncé d'origine demandait de **constater un comportement** du "
             u"logiciel plutôt que de produire un résultat. La réponse "
             u"s'obtenait en sachant, non en construisant : c'est le signal "
             u"qu'on paie le coût d'un exercice pour la valeur d'une question.")
    L.append(u"")
    L.append(u"L'énoncé initial est conservé ci-dessous à titre d'archive.")
    L.append(u"")
    L.append(u"> *%s*" % e.get("enonce_origine", e["enonce"]))
    L.append(u"")
    L.append(u"## CONTEXTE")
    L.append(u"")
    L.append(e.get("contexte") or u"—")
    L.append(u"")
    L.append(u"## LA QUESTION")
    L.append(u"")
    for ligne in (e.get("charniere") or u"").split(u"\n"):
        L.append(ligne)
    L.append(u"")
    L.append(u"## COMMENT L'EMPLOYER")
    L.append(u"")
    L.append(u"- **Avant** l'exercice qui mobilise cette connaissance, pas "
             u"après : elle en est un prérequis.")
    L.append(u"- Poser la question à main levée, relever la répartition des "
             u"réponses, et n'expliquer que si une réponse fausse est "
             u"majoritaire.")
    L.append(u"- La valeur est dans la **mauvaise** réponse : elle nomme la "
             u"représentation à corriger.")
    L.append(u"")
    if e.get("etapes"):
        L.append(u"## DÉMONSTRATION FACULTATIVE")
        L.append(u"")
        L.append(u"Le fichier `%s_complet.gh` reste disponible comme support de "
                 u"démonstration au vidéoprojecteur. Il n'est pas à faire "
                 u"construire." % e["id"])
        L.append(u"")
        for i, s in enumerate(e["etapes"], 1):
            L.append(u"**%d.** %s" % (i, s))
            L.append(u"")
    return L


def sujet(e, seul):
    L = []
    L.append(u"---")
    L.append(u"")
    L.append(u"## SUJET")
    L.append(u"")
    L.append(u"### Compétence visée")
    L.append(u"")
    L.append(e["obj"])
    L.append(u"")
    if e.get("contexte"):
        L.append(u"### Contexte")
        L.append(u"")
        L.append(e["contexte"])
        L.append(u"")
    L.append(u"### Énoncé")
    L.append(u"")
    L.append(u"> %s" % e["enonce"])
    L.append(u"")
    L.append(u"### Ce qui vous est fourni")
    L.append(u"")
    L.append(e["depart"])
    L.append(u"")
    L.append(u"### Ce qui est attendu")
    L.append(u"")
    L.append(e["att"])
    L.append(u"")
    L.append(u"Branchez votre résultat sur le paramètre **`REPONSE`**, en haut "
             u"à droite de la zone de travail. La correction compare cette "
             u"sortie en mode **%s**%s."
             % (e["mode"],
                u"" if e["tol"] in (u"—", u"0") else
                u" avec une tolérance de %s" % e["tol"]))
    L.append(u"")
    L.append(u"> **La consigne ne nomme aucun composant**, et c'est "
             u"délibéré : nommer l'outil reviendrait à donner la réponse. "
             u"Ce lot n'autorise que des composants natifs de Grasshopper "
             u"pour Rhino 8 — aucun plugin tiers n'est nécessaire.")
    L.append(u"")
    L.append(u"### Fichier à ouvrir")
    L.append(u"")
    L.append(u"`%s_sujet.gh`" % e["id"])
    L.append(u"")
    L.append(u"### Barème")
    L.append(u"")
    L.append(e["bareme"])
    L.append(u"")
    if seul:
        L.append(u"---")
        L.append(u"")
        L.append(u"*Le corrigé fait l'objet d'une fiche distincte, remise "
                 u"après validation ou en fin de séance.*")
        L.append(u"")
    return L


def corrige(e, ressource=None):
    L = []
    L.append(u"---")
    L.append(u"")
    L.append(u"## CORRIGÉ")
    L.append(u"")
    L.append(u"> À ne consulter qu'après avoir cherché. Dans le fichier "
             u"`%s_complet.gh`, le corrigé occupe la zone basse du canvas, "
             u"chaque étape formant un groupe distinct. Il est **autonome** : "
             u"les données fournies y sont recopiées, aucun câble ne le relie "
             u"à la zone sujet. Il ne produit rien tant que l'interrupteur "
             u"**AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — "
             u"remettez-le sur faux pour faire disparaître le résultat."
             % e["id"])
    L.append(u"")
    L.append(u"### Marche à suivre")
    L.append(u"")
    for i, s in enumerate(e["etapes"], 1):
        L.append(u"**Étape %d.** %s" % (i, s))
        L.append(u"")

    if e.get("erreur"):
        L.append(u"### L'erreur attendue")
        L.append(u"")
        L.append(u"C'est l'erreur qu'il faut guetter, parce qu'elle est "
                 u"*diagnostique* : elle dit ce que l'apprenant a mal compris, "
                 u"là où un simple « faux » ne dirait rien.")
        L.append(u"")
        L.append(u"> %s" % e["erreur"])
        L.append(u"")

    L.append(u"### Pièges fréquents")
    L.append(u"")
    for p in e["pieges"]:
        L.append(u"- %s" % p)
    L.append(u"")

    if e.get("donnees_note"):
        L.append(u"### Pourquoi ce jeu de données")
        L.append(u"")
        L.append(e["donnees_note"])
        L.append(u"")

    if e["id"] in MANUELS:
        L.append(u"### Réglages à poser à la main")
        L.append(u"")
        L.append(u"Ces réglages ne peuvent pas être enregistrés dans le "
                 u"fichier : ils sont à poser dans Grasshopper.")
        L.append(u"")
        for m in MANUELS[e["id"]]:
            L.append(u"- %s" % m)
        L.append(u"")

    if e.get("limite"):
        L.append(u"### Limite de la correction automatique")
        L.append(u"")
        L.append(u"> %s" % e["limite"])
        L.append(u"")

    if e.get("alerte"):
        L.append(u"### Note au formateur")
        L.append(u"")
        L.append(u"> %s" % e["alerte"])
        L.append(u"")

    L.append(u"### Pour aller plus loin")
    L.append(u"")
    for v in e["var"]:
        L.append(u"- %s" % v)
    L.append(u"")
    L.append(u"---")
    L.append(u"")
    L.append(u"### Fichiers de cet exercice")
    L.append(u"")
    L.append(u"| Fichier | Contenu |")
    L.append(u"|---|---|")
    L.append(u"| `%s_sujet.gh` | Énoncé et données de départ, sans le corrigé |"
             % e["id"])
    L.append(u"| `%s_complet.gh` | Énoncé **et** corrigé commenté étape par étape |"
             % e["id"])
    L.append(u"| `%s.json` | Descripteur pour le plugin Magpie |" % e["id"])
    L.append(u"| `%s_fiche.md` | La présente fiche |" % e["id"])
    L.append(u"| `%s_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |"
             % e["id"])
    L.append(u"| `%s_fiche.docx` | La fiche Word illustrée, sujet et corrigé |"
             % e["id"])
    L.append(u"| `%s_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |"
             % e["id"])
    L.append(u"| `Illustrations/` | Captures du canvas, sujet et corrigé |")
    if ressource:
        L.append(u"| `Ressources/%s` | Géométrie Rhino à ouvrir avant de commencer |"
                 % ressource)
    L.append(u"")
    return L


def ecrire(chemin, lignes):
    fh = io.open(chemin, "w", encoding="utf-8")
    try:
        fh.write(u"\n".join(lignes))
    finally:
        fh.close()


def produire(corpus, sortie, lot, fusion=True):
    """Ecrit les fiches d'un lot. Retourne (exercices, charnieres, absents)."""
    if not sortie or not os.path.isdir(sortie):
        print("Dossier introuvable : %s" % sortie)
        return 0, 0, []
    dossiers = {}
    for d in os.listdir(sortie):
        if os.path.isdir(os.path.join(sortie, d)):
            dossiers[d.split(" ")[0]] = os.path.join(sortie, d)

    faits, chn, absents = 0, 0, []
    for brut in corpus:
        e = fusionner(brut) if fusion else dict(brut)
        e["enonce_origine"] = brut["enonce"]
        dd = dossiers.get(e["id"])
        if dd is None:
            absents.append(e["id"])
            continue
        res = None
        rd = os.path.join(dd, "Ressources")
        if os.path.isdir(rd):
            fics = [f for f in os.listdir(rd) if f.lower().endswith(".3dm")]
            res = fics[0] if fics else None

        if e.get("verdict") == u"connaissance":
            corps = entete(e) + charniere(e)
            ecrire(os.path.join(dd, "%s_fiche.md" % e["id"]), corps)
            ecrire(os.path.join(dd, "%s_fiche_sujet.md" % e["id"]), corps)
            chn += 1
        else:
            ecrire(os.path.join(dd, "%s_fiche.md" % e["id"]),
                   entete(e) + sujet(e, False) + corrige(e, res))
            ecrire(os.path.join(dd, "%s_fiche_sujet.md" % e["id"]),
                   entete(e) + sujet(e, True))
            faits += 1

    return faits, chn, absents


def main():
    global LOT
    total = [0, 0]
    for code, libelle, dossier, corpus in _LOTS:
        sortie = os.path.join(PROJET, dossier.replace("/", os.sep))
        if not os.path.isdir(sortie):
            os.makedirs(sortie)
        # Le lot A nomme ses dossiers « A-01 Titre » : ne pas en creer un
        # second, nu, a cote. On ne cree que ce qui manque vraiment.
        presents = set()
        for d in os.listdir(sortie):
            if os.path.isdir(os.path.join(sortie, d)):
                presents.add(d.split(" ")[0])
        for e in corpus:
            if e["id"] not in presents:
                os.makedirs(os.path.join(sortie, e["id"]))
        LOT = u"%s — %s" % (code, libelle)
        f, c, absents = produire(corpus, sortie, code, fusion=False)
        total[0] += f
        total[1] += c
        print(u"  lot %-3s %-40s %2d exercices, %d charnières"
              % (code, libelle[:40], f, c))
    print(u"Fichiers écrits : %d" % (2 * (total[0] + total[1])))


if __name__ == "__main__":
    main()
