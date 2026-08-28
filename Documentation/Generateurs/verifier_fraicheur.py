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
LOTS = [os.path.join(PROJET, "EXERCICES", "LOT A - Composants natifs"),
        os.path.join(PROJET, "EXERCICES",
                     "LOT IA - IA et assistance generative")]
LOT = LOTS[0]

# Chaque lot a ses propres sources : dater le lot A d'apres domaine_ia.py le
# declarerait perime a chaque retouche du domaine IA, ce qui serait faux.
SOURCES = {
    "A": [os.path.join(ICI, "skill_a.py"), os.path.join(ICI, "exos_a.py")],
    "IA": [os.path.join(ICI, "domaine_ia.py")],
}


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

    ts = {}
    for lot, fics in SOURCES.items():
        vals = [d for d in (date(f) for f in fics) if d]
        ts[lot] = max(vals) if vals else 0
    perimes, manquants = [], []

    for dd in bases:
        if not os.path.isdir(dd):
            continue
        eid = os.path.basename(dd).split(" ")[0]
        lot = "IA" if eid.startswith("IA-") else "A"
        t_source = ts[lot]
        origine = u"domaine_ia.py" if lot == "IA" else u"skill_a.py"

        # --- livrables qui doivent suivre la source pedagogique -----------
        # IA-07 a pour livrable un plugin compile : il n'a volontairement ni
        # definition ni descripteur.
        attendus = ["%s_sujet.gh", "%s_complet.gh", "%s.json",
                    "%s_fiche.md", "%s_fiche_sujet.md",
                    "%s_fiche.docx", "%s_fiche_sujet.docx"]
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
        if tp is None:
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

    print(u"Tous les livrables du lot A sont à jour par rapport à leur source.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
