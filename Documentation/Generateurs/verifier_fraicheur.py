# -*- coding: utf-8 -*-
"""Verifie qu'aucun livrable derive n'est plus ancien que sa source.

Une chaine de generation interrompue laisse des fichiers coherents en apparence
mais perimes : la fiche Word dit une chose, le PDF tire de la version d'avant en
dit une autre. Rien ne le signale, et c'est exactement ce qui s'est produit le
26/08/2026 quand la conversion PDF a ete coupee apres la reecriture des .docx.

Ce script compare les dates de modification le long de la chaine :

    skill_a.py / exos_a.py  ->  .gh, .json, fiches .md, fiches .docx
    fiche .docx             ->  fiche .pdf
    illustrations .png      ->  vignettes web .jpg

Sortie en code 1 des qu'un livrable est perime.
"""
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PROJET = os.path.abspath(os.path.join(ICI, "..", ".."))
from lots import LOTS as _REGISTRE, AVEC_DEFINITIONS
LOTS = [os.path.join(PROJET, d.replace("/", os.sep))
        for _c, _n, d, _l in _REGISTRE]
LOT = LOTS[0]

# Chaque exercice a ses propres sources : dater le lot A d'apres domaine_ia.py
# le declarerait perime a chaque retouche du domaine IA, ce qui serait faux.
#
# La table etait ecrite a la main et ne connaissait que A et IA : les neuf
# autres lots n'etaient donc compares a RIEN, et un exercice reecrit sans
# regeneration serait passe inapercu. Elle est desormais DEDUITE des modules :
# on demande a chacun quels identifiants il declare. Ajouter un module de
# contenu suffit a ce qu'il soit surveille.
# La liste des modules etait elle aussi ecrite a la main, et la vague 3 est
# arrivee sans y figurer : dix-huit exercices se sont retrouves « sans source
# declaree ». On la DECOUVRE donc, par le nom des fichiers — la convention
# etant tenue depuis le debut. Ajouter un module de contenu suffit desormais,
# sans toucher a ce fichier.
# Quatre familles de modules portent du contenu : les lots d'origine
# (exos_*), leurs couches pedagogiques (skill_*), les domaines ajoutes
# (domaine_*) et les vagues d'equilibrage (exercices_*). Le lot B est
# arrive par exos_b + skill_b, que les deux premiers prefixes ne
# couvraient pas : ses dix-huit exercices se sont retrouves « sans source
# declaree ». La liste des prefixes couvre desormais les quatre.
PREFIXES = ("exercices_", "domaine_", "exos_", "skill_")
NOMMES = ()


def modules_de_contenu():
    noms = set(NOMMES)
    for f in sorted(os.listdir(ICI)):
        if not f.endswith(".py"):
            continue
        base = f[:-3]
        if base.startswith(PREFIXES):
            noms.add(base)
    return sorted(noms)


def _declares(mod, connus):
    """Identifiants d'exercice qu'un module declare, quelle qu'en soit la forme.

    Les modules de domaine exposent des LISTES de fiches ; skill_a expose des
    DICTIONNAIRES indexes par identifiant. On ratisse les deux, puis on croise
    avec le registre : sans ce croisement, les identifiants de notions
    (REF-nnn) entreraient dans le lot.
    """
    trouves = set()
    for nom in dir(mod):
        if nom.startswith("__"):
            continue
        v = getattr(mod, nom)
        if isinstance(v, list):
            for x in v:
                if isinstance(x, dict) and x.get("id"):
                    trouves.add(x["id"])
        elif isinstance(v, dict):
            trouves |= set(k for k in v if isinstance(k, basestring_))
    return trouves & connus


try:
    basestring_ = basestring          # Python 2 / IronPython
except NameError:
    basestring_ = str


def sources_par_exercice():
    """identifiant -> [modules qui le declarent]."""
    from lots import TOUS
    connus = set(e["id"] for e in TOUS)
    par_id = {}
    for nom in modules_de_contenu():
        chemin = os.path.join(ICI, nom + ".py")
        if not os.path.isfile(chemin):
            continue
        try:
            mod = __import__(nom)
        except Exception as ex:
            print(u"  (%s non chargé : %s)" % (nom, ex))
            continue
        for eid in _declares(mod, connus):
            par_id.setdefault(eid, []).append(chemin)
    return par_id


def date(chemin):
    try:
        return os.path.getmtime(chemin)
    except OSError:
        return None


def main():
    bases = []
    for _l in LOTS:
        if os.path.isdir(_l):
            bases += [os.path.join(_l, _d) for _d in sorted(os.listdir(_l))]
    if not bases:
        print(u"Aucun dossier d'exercice trouvé.")
        return 1

    par_id = sources_par_exercice()
    perimes, manquants, orphelins = [], [], []

    for dd in bases:
        if not os.path.isdir(dd):
            continue
        eid = os.path.basename(dd).split(" ")[0]
        fics = par_id.get(eid)
        if not fics:
            # Un dossier sans source declaree : soit l'exercice a ete retire du
            # registre, soit un module a change de forme. Les deux meritent
            # d'etre dits plutot que d'etre ignores silencieusement.
            orphelins.append(eid)
            continue
        dates = [d for d in (date(f) for f in fics) if d]
        t_source = max(dates) if dates else 0
        origine = u", ".join(sorted(os.path.basename(f) for f in fics))

        # --- livrables qui doivent suivre la source pedagogique -----------
        # IA-07 a pour livrable un plugin compile : il n'a volontairement ni
        # definition ni descripteur.
        attendus = ["%s_fiche.md", "%s_fiche_sujet.md",
                    "%s_fiche.docx", "%s_fiche_sujet.docx"]
        if eid in AVEC_DEFINITIONS:
            attendus = ["%s_sujet.gh", "%s_complet.gh", "%s.json"] + attendus
        if eid == "IA-07":
            attendus = ["%s_fiche.md", "%s_fiche_sujet.md",
                        "%s_fiche.docx", "%s_fiche_sujet.docx"]
        for nom in attendus:
            f = os.path.join(dd, nom % eid)
            t = date(f)
            if t is None:
                manquants.append(nom % eid)
            elif t < t_source:
                perimes.append((nom % eid, u"plus ancien que %s" % origine))

        # --- le PDF doit suivre son .docx ---------------------------------
        doc = os.path.join(dd, "%s_fiche.docx" % eid)
        pdf = os.path.join(dd, "%s_fiche.pdf" % eid)
        td, tp = date(doc), date(pdf)
        if tp is None and td is not None:
            manquants.append("%s_fiche.pdf" % eid)   # conversion en cours ?
        elif td is not None and tp < td:
            perimes.append(("%s_fiche.pdf" % eid, u"plus ancien que sa fiche Word"))

        # --- la vignette web doit suivre l'illustration pleine resolution --
        for suf in ("sujet", "corrige"):
            png = os.path.join(dd, "Illustrations", "%s_canvas_%s.png" % (eid, suf))
            jpg = os.path.join(dd, "Illustrations", "web",
                               "%s_canvas_%s.jpg" % (eid, suf))
            tpn, tjp = date(png), date(jpg)
            if tpn is not None and tjp is not None and tjp < tpn:
                perimes.append(("%s_canvas_%s.jpg" % (eid, suf),
                                u"plus ancienne que le PNG"))

    if orphelins:
        print(u"SANS SOURCE DÉCLARÉE (%d) : %s" % (len(orphelins),
                                                   u", ".join(orphelins)))
        print(u"")

    if manquants:
        print(u"MANQUANTS (%d) :" % len(manquants))
        for m in manquants[:20]:
            print(u"  %s" % m)
        if len(manquants) > 20:
            print(u"  … et %d autres" % (len(manquants) - 20))
        print(u"")

    if perimes:
        print(u"PÉRIMÉS (%d) :" % len(perimes))
        for nom, raison in perimes[:30]:
            print(u"  %-26s %s" % (nom, raison))
        if len(perimes) > 30:
            print(u"  … et %d autres" % (len(perimes) - 30))
        print(u"")
        print(u"Relancez la chaîne : "
              u"python Documentation/Generateurs/finaliser.py")
        return 1

    if manquants:
        return 1

    if orphelins:
        return 1
    # Le nombre de lots a change quatre fois ; l'ecrire en toutes lettres
    # dans le message revient a le laisser vieillir en silence.
    print(u"Tous les livrables des %d lots sont à jour par rapport à "
          u"leur source." % len(LOTS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
