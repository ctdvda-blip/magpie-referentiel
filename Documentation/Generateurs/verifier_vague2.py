# -*- coding: utf-8 -*-
"""Recalcule les reponses de la vague 2 et les confronte aux fiches.

Meme role que `verifier_vague1.py`, dont il partage la mecanique de lecture :
le premier nombre du champ `att` est confronte au resultat recalcule depuis
les seules donnees. Un desaccord bloque.

    python Documentation/Generateurs/verifier_vague2.py
"""
import io
import math
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)

import exercices_vague2 as V2
import exercices_vague2_avance as V2A
from verifier_vague1 import annonce
from lots import TOUS


# ---------------------------------------------------------------- lot RH
def rh11():
    """Etendue selon X, en metres, egares compris."""
    xs = [p[0] for p in V2.D_RH11_BATI + V2.D_RH11_EGARES]
    return (max(xs) - min(xs)) / 1000.0


def rh12():
    return sum(1 for z in V2.D_RH12_ALTITUDES if z > V2.D_RH12_NIVEAU)


def rh13():
    return sum(q for _n, allume, q in V2.D_RH13_CALQUES if allume)


def rh14():
    d = V2.D_RH14
    return d["nx"] * d["ny"] - d["tremie"][0] * d["tremie"][1]


def rh15():
    p = V2.D_RH15_PTS
    return sum(math.hypot(p[i + 1][0] - p[i][0], p[i + 1][1] - p[i][1])
               for i in range(len(p) - 1))


def rh16():
    """Aire du rampant, en metres carres : le rampant, pas la projection."""
    d = V2.D_RH16
    rampant = math.hypot(d["profondeur"], d["denivele"])
    return d["base"] * rampant / 1e6


def rh17():
    """Reunion de deux volumes, en decimetres cubes."""
    d = V2.D_RH17
    def v(t):
        return t[0] * t[1] * t[2]
    return (v(d["a"]) + v(d["b"]) - v(d["intersection"])) / 1e6


def rh18():
    return sum(1 for p in V2.D_RH18_PAROIS if p < V2.D_RH18_MINI)


def rh19():
    d = V2.D_RH19
    return sum(1 for x in V2.D_RH19_DETAILS
               if x * d["facteur"] < d["resolution"])


def rh20():
    """Aretes nues : trois par triangle, deux par arete interieure."""
    d = V2.D_RH20
    return 3 * d["faces"] - 2 * d["aretes"]


def rh21():
    return sum(1 for a in V2.D_RH21_AIRES if a < V2.D_RH21_TOL)


def rh22():
    """Facettes sur un demi-tour pour tenir la fleche admise."""
    d = V2.D_RH22
    return int(math.ceil(math.pi / math.acos(1.0 - d["fleche"] / d["rayon"])))


# ---------------------------------------------------------------- lot GP
def gp06():
    d = V2.D_GP06
    return (d["u"] + 1) * (d["v"] + 1)


def gp07():
    d = V2.D_GP06
    return d["u"] * d["v"] * 4 - (d["u"] + 1) * (d["v"] + 1)


def gp08():
    d = V2.D_GP08
    return d["faces"] * 4 ** d["passes"]


# ---------------------------------------------------------- lots QT et MP
def qt06():
    d = V2.D_QT06
    sec = d["materiaux"] + d["heures"] * d["taux"]
    return sec * (1 + d["marge"]) * (1 + d["tva"])


def mp04():
    """Ce qui se recalcule en aval de Largeur, sans compter deux fois."""
    g = V2.D_MP04_GRAPHE
    vus, pile = set(), [u"Largeur"]
    while pile:
        for suivant in g.get(pile.pop(), []):
            if suivant not in vus:
                vus.add(suivant)
                pile.append(suivant)
    return len(vus)


# ---------------------------------------------------------------- lot PL
def pl05():
    """Fermeture des dependances, le paquet vise compris."""
    dep = V2A.D_PL05_DEPENDANCES
    vus, pile = set(), list(dep.get(V2A.D_PL05_CIBLE, []))
    while pile:
        n = pile.pop()
        if n in vus:
            continue
        vus.add(n)
        pile.extend(dep.get(n, []))
    return len(vus) + 1


def pl06():
    requis = set(V2A.D_PL06_REQUIS)
    return sum(1 for _p, d in V2A.D_PL06_POSTES if requis <= set(d))


def pl07():
    t = V2A.D_PL07_TACHES
    return sum(a for _n, a, _b in t) - sum(b for _n, _a, b in t)


def pl08():
    return sum(1 for _s, parlant in V2A.D_PL08_SURNOMS if not parlant)


def pl09():
    return sum(1 for _n, v in V2A.D_PL09_PLUGINS if v <= V2A.D_PL09_CIBLE)


# ---------------------------------------------------------------- lot DV
def dv08():
    return V2A.D_DV08["niveau_b"]


def dv09():
    """Division ENTIERE, comme le langage la fait sur deux entiers."""
    return sum(v // V2A.D_DV09_DIVISEUR for v in V2A.D_DV09_VALEURS)


# ---------------------------------------------------------------- lot IA
def ia19():
    bas, haut = V2A.D_IA19_SEUILS
    petit = sum(1 for d in V2A.D_IA19_DEBITS if d < bas)
    moyen = sum(1 for d in V2A.D_IA19_DEBITS if bas <= d < haut)
    grand = sum(1 for d in V2A.D_IA19_DEBITS if d >= haut)
    return max(petit, moyen, grand)


def ia20():
    d = V2A.D_IA20
    return int(d["budget_heures"] * 3600 / d["duree_seconde"])


def ia21():
    d = V2A.D_IA21
    travees = int(math.ceil(d["longueur"] / d["entraxe_max"]))
    return travees + 1


def ia22():
    """Arrondi COMMERCIAL : la demie monte, quelle que soit la parite."""
    return sum(int(math.floor(v + 0.5)) for v in V2A.D_IA22_VALEURS)


def ia23():
    for tour, passants in V2A.D_IA23_TOURS:
        if passants >= V2A.D_IA23_CIBLE:
            return tour
    return None


def ia25():
    d = V2A.D_IA25
    return d["requetes"] * (d["jetons_entree"] * d["prix_entree"] +
                            d["jetons_sortie"] * d["prix_sortie"]) / 1e6


CALCULS = [
    (u"RH-11", rh11, 0), (u"RH-12", rh12, 0), (u"RH-13", rh13, 0),
    (u"RH-14", rh14, 0), (u"RH-15", rh15, 0), (u"RH-16", rh16, 2),
    (u"RH-17", rh17, 2), (u"RH-18", rh18, 0), (u"RH-19", rh19, 0),
    (u"RH-20", rh20, 0), (u"RH-21", rh21, 0), (u"RH-22", rh22, 0),
    (u"GP-06", gp06, 0), (u"GP-07", gp07, 0), (u"GP-08", gp08, 0),
    (u"QT-06", qt06, 2), (u"MP-04", mp04, 0),
    (u"PL-05", pl05, 0), (u"PL-06", pl06, 0), (u"PL-07", pl07, 0),
    (u"PL-08", pl08, 0), (u"PL-09", pl09, 0),
    (u"DV-08", dv08, 0), (u"DV-09", dv09, 0),
    (u"IA-19", ia19, 0), (u"IA-20", ia20, 0), (u"IA-21", ia21, 0),
    (u"IA-22", ia22, 0), (u"IA-23", ia23, 0), (u"IA-25", ia25, 2),
]


def main():
    par_id = dict((e["id"], e) for e in TOUS)
    lg = 66
    print("=" * lg)
    print(u"VÉRIFICATION DE LA VAGUE 2 — valeurs recalculées")
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
