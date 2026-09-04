# -*- coding: utf-8 -*-
"""Recalcule les reponses de la vague 3 et les confronte aux fiches.

Meme mecanique que `verifier_vague1.py` et `verifier_vague2.py`.

    python Documentation/Generateurs/verifier_vague3.py
"""
import io
import math
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)

import exercices_vague3 as V3
from verifier_vague1 import annonce
from lots import TOUS


def rh23():
    """Objets qui satisfont les DEUX proprietes."""
    cal, typ = V3.D_RH23_CIBLE
    return sum(1 for c, t in V3.D_RH23_OBJETS if c == cal and t == typ)


def a50():
    """References distinctes une fois les libelles nettoyes."""
    return len(set(x.strip().upper() for x in V3.D_A50_LIBELLES))


def a51():
    """Repere en tete d'un tri de TEXTE — pas de nombres."""
    return int(sorted(V3.D_A51_REPERES)[0])


def gp09():
    """Petite base d'un trapeze rectangle."""
    d = V3.D_GP09
    recul = d["hauteur"] / math.tan(math.radians(d["angle"]))
    return d["base"] - recul


def gp11():
    """Ecart de perimetre entre les deux ordres d'operations."""
    d = V3.D_GP11
    l, h, r, o = d["longueur"], d["hauteur"], d["rayon"], d["decalage"]
    # conge puis decalage : les rayons grandissent de l'offset
    p1 = 2 * (l - 2 * r) + 2 * (h - 2 * r) + 2 * math.pi * (r + o)
    # decalage puis conge : le contour grandit, les rayons restent
    p2 = 2 * (l + 2 * o - 2 * r) + 2 * (h + 2 * o - 2 * r) + 2 * math.pi * r
    return abs(p1 - p2)


def gp12():
    """Distance entre les deux compositions possibles."""
    d = V3.D_GP12
    a = math.radians(d["angle"])
    p, t = d["point"], d["translation"]

    def rot(q):
        return (q[0] * math.cos(a) - q[1] * math.sin(a),
                q[0] * math.sin(a) + q[1] * math.cos(a))

    rt = (rot(p)[0] + t[0], rot(p)[1] + t[1])
    tr = rot((p[0] + t[0], p[1] + t[1]))
    return math.hypot(rt[0] - tr[0], rt[1] - tr[1])


def mp05():
    """Part du composant le plus lourd, en pour cent, arrondie."""
    temps = [t for _n, t in V3.D_MP05_TEMPS]
    return int(round(100.0 * max(temps) / sum(temps)))


def av04():
    """Passes necessaires pour descendre sous le seuil."""
    d = V3.D_AV04
    return int(math.ceil(math.log(d["seuil"] / d["depart"])
                         / math.log(d["facteur"])))


def av05():
    """Rang de la premiere piece qui fait depasser la capacite."""
    cum = 0
    for i, x in enumerate(V3.D_AV05_LONGUEURS, 1):
        cum += x
        if cum > V3.D_AV05_CAPACITE:
            return i
    return None


def av07():
    """Solutions qu'aucune autre ne surpasse sur les deux criteres."""
    s = V3.D_AV07_SOLUTIONS
    n = 0
    for _nom, cout, perf in s:
        domine = any(c2 <= cout and p2 >= perf and (c2 < cout or p2 > perf)
                     for _n2, c2, p2 in s)
        if not domine:
            n += 1
    return n


def av08():
    """Premiere passe a partir de laquelle le residu RESTE sous la tolerance."""
    r = V3.D_AV08_RESIDUS
    for k in range(len(r)):
        if all(v < V3.D_AV08_TOLERANCE for _i, v in r[k:]):
            return r[k][0]
    return None


def wb08():
    """Reglages dont les tablettes ne tiennent pas dans la hauteur."""
    return sum(1 for h, n, e in V3.D_WB08_CAS
               if n > 0 and h < n * (V3.D_WB08_LIBRE + e))


def wb09():
    """Formats qui portent TOUT ce que l'echange exige."""
    idx = {u"geometrie": 1, u"unites": 2, u"calques": 3, u"matieres": 4,
           u"metadonnees": 5, u"courbes": 6}
    return sum(1 for f in V3.D_WB09_FORMATS
               if all(f[idx[b]] for b in V3.D_WB09_BESOIN))


def fa06():
    """Pieces par panneau, rives et trait de scie deduits."""
    d = V3.D_FA06
    utile = d["panneau"] - 2 * d["rive"]
    return int((utile + d["trait"]) // (d["piece"] + d["trait"]))


CALCULS = [
    (u"RH-23", rh23, 0), (u"A-50", a50, 0), (u"A-51", a51, 0),
    (u"GP-09", gp09, 2), (u"GP-11", gp11, 2), (u"GP-12", gp12, 2),
    (u"MP-05", mp05, 0),
    (u"AV-04", av04, 0), (u"AV-05", av05, 0), (u"AV-07", av07, 0),
    (u"AV-08", av08, 0),
    (u"WB-08", wb08, 0), (u"WB-09", wb09, 0), (u"FA-06", fa06, 0),
]


def main():
    par_id = dict((e["id"], e) for e in TOUS)
    lg = 66
    print("=" * lg)
    print(u"VÉRIFICATION DE LA VAGUE 3 — valeurs recalculées")
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
            ecarts.append((eid, u"aucune valeur lisible", calcule))
            continue
        ok = abs(float(calcule) - dite) <= (0.5 * 10 ** (-dec) if dec else 1e-9)
        gabarit = u"%%-8s calculé %%.%df   fiche %%.%df   %%s" % (dec, dec)
        print(gabarit % (eid, calcule, dite, u"OK" if ok else u"<<< ÉCART"))
        if not ok:
            ecarts.append((eid, dite, calcule))
    print("-" * lg)
    if absents:
        print(u"Absents du registre : %s" % u", ".join(absents))
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
