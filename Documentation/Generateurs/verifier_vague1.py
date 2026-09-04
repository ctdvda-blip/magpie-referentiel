# -*- coding: utf-8 -*-
"""Recalcule les reponses de la vague 1 et les confronte aux fiches.

La skill demande des valeurs RELEVEES, jamais posees de tete. Les onze
exercices a reponse numerique de la vague sont donc recalcules ici, depuis
leurs jeux de donnees, et compares au chiffre annonce dans le champ `att` de
la fiche. Un desaccord n'est pas une alerte : c'est un defaut, et il bloque.

Ce fichier attrape aussi la derive la plus insidieuse — celle ou l'on retouche
un jeu de donnees sans reprendre la fiche qui en annonce le resultat.

    python Documentation/Generateurs/verifier_vague1.py
"""
import io
import math
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)

import exercices_vague1 as V1
import exercices_vague1_avance as V1A
from lots import TOUS


# ---------------------------------------------------------------------------
# Les calculs, refaits depuis les seules donnees
# ---------------------------------------------------------------------------

def gp05():
    """Cote du dernier percement, comptee depuis le point de reference."""
    return V1.D_GP05_ORIGINE + sum(V1.D_GP05_ENTRAXES)


def _regroupe():
    g = {}
    for ref, q in V1.D_QT04_DEBIT:
        g[ref] = g.get(ref, 0) + q
    return g


def qt04():
    """Quantite cumulee de la reference la plus commandee."""
    return max(_regroupe().values())


def qt05():
    """Lignes du fichier exporte : une par reference, plus l'en-tete."""
    return len(_regroupe()) + 1


def fa03():
    """Longueur developpee d'un profil en U plie deux fois a 90 degres."""
    d = V1.D_FA03
    t, r, k = d["epaisseur"], d["rayon"], d["k"]
    plat_aile = d["aile"] - (r + t)          # une aile ne porte qu'un pli
    plat_ame = d["ame"] - 2 * (r + t)        # l'ame en porte deux
    allongement = (math.pi / 2.0) * (r + k * t)
    return 2 * plat_aile + plat_ame + 2 * allongement


def fa04():
    """Pieces par fournee, par encombrement et non par volume."""
    d = V1.D_FA04
    n = 1
    for i in range(3):
        utile = d["plateau"][i] - 2 * d["ecart"]
        # n pieces laissent n-1 intervalles : n*(p+e) - e <= utile
        n *= int((utile + d["ecart"]) // (d["piece"][i] + d["ecart"]))
    return n


def wb04():
    """Entrees a exposer : les choix, ni les derivees ni les reglages."""
    return sum(1 for _n, nature in V1A.D_WB04_ENTREES if nature == u"choix")


def wb05():
    """Instances necessaires a l'heure de pointe, arrondi au superieur."""
    d = V1A.D_WB05
    secondes = d["visites"] * d["part_pointe"] * d["recalculs"] * d["duree"]
    return int(math.ceil(secondes / 3600.0))


def wb06():
    """Poids du fichier : l'en-tete, plus deux facettes par quadrangle."""
    d = V1A.D_WB06
    return d["entete"] + d["par_facette"] * 2 * d["quads"]


def wb07():
    """Denominateur de la plus grande echelle qui fait tenir la piece."""
    d = V1A.D_WB07
    zone = (d["feuille"][0] - 2 * d["marge"], d["feuille"][1] - 2 * d["marge"])
    for e in d["echelles"]:
        if d["longueur"] / e <= zone[0] and d["hauteur"] / e <= zone[1]:
            return e
    return None


def ia15():
    """Liaisons dont l'entree d'arrivee n'est pas celle demandee."""
    return sum(1 for _s, _c, demande, produit in V1A.D_IA15_GRAPHE
               if demande != produit)


def ia17():
    """Pieces reellement commandees."""
    return sum(q for _a, q, _p in V1A.D_IA17_COMMANDE)


CALCULS = [
    (u"GP-05", gp05, 0), (u"QT-04", qt04, 0), (u"QT-05", qt05, 0),
    (u"FA-03", fa03, 2), (u"FA-04", fa04, 0),
    (u"WB-04", wb04, 0), (u"WB-05", wb05, 0), (u"WB-06", wb06, 0),
    (u"WB-07", wb07, 0),
    (u"IA-15", ia15, 0), (u"IA-17", ia17, 0),
]


# ---------------------------------------------------------------------------
# Confrontation aux fiches
# ---------------------------------------------------------------------------

#: le premier nombre du champ `att`, espaces insecables et fines compris
RE_NOMBRE = re.compile(u"[-+]?[0-9][0-9   ]*(?:[.,][0-9]+)?")


def annonce(txt):
    m = RE_NOMBRE.search(txt or u"")
    if not m:
        return None
    brut = m.group(0)
    for espace in (u" ", u" ", u" "):
        brut = brut.replace(espace, u"")
    return float(brut.replace(u",", u"."))


def main():
    par_id = dict((e["id"], e) for e in TOUS)
    lg = 66
    print("=" * lg)
    print(u"VÉRIFICATION DE LA VAGUE 1 — valeurs recalculées")
    print("=" * lg)
    ecarts, absents = [], []
    for eid, fn, dec in CALCULS:
        e = par_id.get(eid)
        if e is None:
            absents.append(eid)
            continue
        calcule = fn()
        dite = annonce(e.get(u"att"))
        if dite is None:
            ecarts.append((eid, u"aucune valeur lisible dans la fiche", calcule))
            continue
        ok = abs(float(calcule) - dite) <= (0.5 * 10 ** (-dec) if dec else 1e-9)
        gabarit = u"%%-8s calculé %%.%df   fiche %%.%df   %%s" % (dec, dec)
        print(gabarit % (eid, calcule, dite, u"OK" if ok else u"<<< ÉCART"))
        if not ok:
            ecarts.append((eid, dite, calcule))
    print("-" * lg)
    if absents:
        print(u"Exercices absents du registre : %s" % u", ".join(absents))
    if ecarts:
        print(u"ÉCARTS : %d" % len(ecarts))
        for eid, dite, calcule in ecarts:
            print(u"   %-8s fiche %s / calcul %s" % (eid, dite, calcule))
    else:
        print(u"Les %d valeurs annoncées correspondent au calcul." % len(CALCULS))
    print("=" * lg)
    return 0 if not ecarts and not absents else 1


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    sys.exit(main())
