# -*- coding: utf-8 -*-
"""Recette 10 — l'enonce donne-t-il la reponse ?

    python Documentation/Generateurs/GH/recette_10_enonce_fuite.py

Un exercice dont la reponse figure dans son propre enonce ne demande rien. Le
cas trouve le 10/09/2026 : A-12 demandait « l'effectif du lot » et son
materiel de depart annonçait « les 28 epaisseurs relevees ». `List Length`
devenait gratuit, et l'apprenant pouvait recopier.

CE QUE LE CONTROLE NE PEUT PAS SAVOIR
-------------------------------------
Sur un exercice de CONSTRUCTION, la reponse reprend legitimement la donnee :
« construisez un cercle de rayon 20 » a pour reponse « un cercle de rayon
20 ». Le travail est de BATIR, pas de trouver le nombre. Ces cas sont
exemptes, et la regle qui les distingue est simple : le mode de validation.

    GeometryTolerance  -> la reponse EST la geometrie, le nombre la decrit
    SingleValue, listes -> le nombre est le resultat d'un calcul

Le controle ne signale donc que les seconds. Restent deux coincidences que
seule la lecture tranche, exemptees nommement.
"""
import io
import os
import re
import sys

try:
    ICI = os.path.dirname(os.path.abspath(__file__))
except NameError:
    ICI = r"C:\Users\charl\.claude\projects\MAGPIE\Documentation\Generateurs\GH"
GEN = os.path.abspath(os.path.join(ICI, ".."))
for _p in (ICI, GEN):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from lots import TOUS

RE_NOMBRE = re.compile(u"[-+]?[0-9][0-9   ]*(?:[.,][0-9]+)?")

#: Les modes ou la reponse DECRIT une geometrie construite : le nombre y
#: reprend la donnee sans rien donner.
MODES_CONSTRUCTION = set([u"GeometryTolerance", u"Visuel", u"—"])

#: Nombres si courants qu'une coincidence ne prouve rien.
BANALS = set([0, 1, 2, 3, 4, 5, 6, 10, 12, 100])

#: Coincidences relues et tranchees.
EXEMPTS = {
    u"A-01": u"2 400 est la CIBLE à atteindre, pas une réponse cachée : "
             u"l'exercice est de câbler deux entrées, et sans la cible il "
             u"n'aurait aucune consigne",
    u"G-10": u"le 7 de l'énoncé est la GRAINE du tirage ; le premier index "
             u"trouvé vaut 7 par coïncidence",
}


def nombres(txt):
    out = []
    for m in RE_NOMBRE.finditer(txt or u""):
        brut = m.group(0)
        for espace in (u" ", u" ", u" "):
            brut = brut.replace(espace, u"")
        try:
            out.append(float(brut.replace(u",", u".")))
        except ValueError:
            pass
    return out


def main():
    lg = 74
    print("=" * lg)
    print(u"RECETTE 10 — l'énoncé donne-t-il la réponse ?")
    print("=" * lg)
    controles, fuites, exemptes, construction = 0, [], [], 0
    for e in TOUS:
        if e.get(u"verdict") == u"connaissance":
            continue
        na = nombres(u"%s" % (e.get(u"att") or u""))
        if not na:
            continue
        if u"%s" % (e.get(u"mode") or u"") in MODES_CONSTRUCTION:
            construction += 1
            continue
        controles += 1
        bonne = na[0]
        if bonne in BANALS:
            continue
        source = u"%s %s" % (e.get(u"enonce") or u"", e.get(u"depart") or u"")
        marge = max(1e-9, abs(bonne) * 1e-9)
        if not any(abs(x - bonne) <= marge for x in nombres(source)):
            continue
        if e["id"] in EXEMPTS:
            exemptes.append((e["id"], EXEMPTS[e["id"]]))
        else:
            fuites.append((e["id"], bonne, e.get(u"titre")))

    print(u"%d exercices à réponse calculée contrôlés" % controles)
    print(u"  %-42s %d" % (u"exercices de construction, écartés", construction))
    print(u"  %-42s %d" % (u"coïncidences exemptées", len(exemptes)))
    print(u"  %-42s %d" % (u"ÉNONCÉ QUI FUITE", len(fuites)))
    for eid, motif in exemptes:
        print(u"      %-7s exempté : %s" % (eid, motif))
    for eid, val, titre in fuites:
        print(u"      %-7s la réponse %s figure dans l'énoncé — %s"
              % (eid, val, (titre or u"")[:34]))
    print("-" * lg)
    if fuites:
        print(u"Retirer la valeur du matériel de départ, ou changer la question.")
    else:
        print(u"Aucun énoncé ne donne sa réponse.")
    print("=" * lg)
    return 0 if not fuites else 1


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    sys.exit(main())
