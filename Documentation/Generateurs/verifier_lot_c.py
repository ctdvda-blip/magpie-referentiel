# -*- coding: utf-8 -*-
"""Recalcule les douze indicateurs du lot C et les confronte aux fiches.

    python Documentation/Generateurs/verifier_lot_c.py
"""
import io
import math
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)

import skill_c as C
from verifier_vague1 import annonce
from lots import TOUS


def c01():
    """Profondeur de lame : l'entraxe DIVISE par la tangente."""
    d = C.D_C01
    return d["entraxe"] / math.tan(math.radians(d["hauteur_solaire"]))


def c02():
    """Lineaire de barres, diagonales comprises, en metres."""
    d = C.D_C02
    nx, ny = int(d["largeur"] / d["maille"]), int(d["profondeur"] / d["maille"])
    horiz = (ny + 1) * nx * d["maille"]
    verti = (nx + 1) * ny * d["maille"]
    diago = nx * ny * math.hypot(d["maille"], d["maille"])
    return (horiz + verti + diago) / 1000.0


def c03():
    """Hauteur du dernier rang : le degagement se PROPAGE."""
    d = C.D_C03
    h = [0.0]
    for i in range(1, d["rangs"]):
        d_prec = d["foyer"] + (i - 1) * d["profondeur"]
        d_cour = d["foyer"] + i * d["profondeur"]
        h.append((h[-1] + d["degagement"]) * d_cour / d_prec)
    return h[-1]


def c04():
    return sum(q * pu for _n, lignes in C.D_C04_LOTS
               for _d, q, _u, pu in lignes)


def c05():
    """Panneaux : montants (travees + 1), tablettes, traverses et fond."""
    d = C.D_C05
    travees = int(math.ceil(d["largeur"] / d["entraxe_max"]))
    montants = travees + 1
    tablettes = travees * d["tablettes_par_travee"]
    return montants + tablettes + 3


def c06():
    """Rayon de la directrice, retrouve de sa corde et de sa fleche."""
    d = C.D_C06
    return (d["corde"] ** 2 / 4 + d["fleche"] ** 2) / (2 * d["fleche"])


def c07():
    """Prix : la matiere majore TOUT le meuble."""
    d = C.D_C07
    pied, tiroirs, matiere = d["choix"]
    return ((d["base"] + C.D_C07_PIEDS[pied] + tiroirs * d["par_tiroir"])
            * C.D_C07_MATIERE[matiere])


def c08():
    """Masse : le volume se calcule sur la FIBRE MOYENNE."""
    d = C.D_C08
    circ = d["taille"] + math.pi * d["epaisseur"]
    vol = circ * d["largeur"] * d["epaisseur"] + d["chaton"]
    return vol * d["densite"] / 1000.0


def c09():
    """Pierres : maille hexagonale, pas = diametre + metal."""
    d = C.D_C09
    pas = d["diametre"] + d["metal"]
    return int(d["surface"] / (math.sqrt(3) / 2 * pas ** 2))


def c10():
    """Cellules : le filet s'ajoute au cote de la cellule."""
    d = C.D_C10
    cote = math.sqrt(d["aire_cellule"])
    return int(d["surface"] / (cote + d["filet"]) ** 2)


def c11():
    """Developpe : deux plis par segment interieur, un aux extremites."""
    d = C.D_C11
    plats = []
    for i, c in enumerate(d["cotes"]):
        nb = 1 if i in (0, len(d["cotes"]) - 1) else 2
        plats.append(c - nb * (d["rayon"] + d["epaisseur"]))
    ba = (math.pi / 2.0) * (d["rayon"] + d["k"] * d["epaisseur"])
    return sum(plats) + (len(d["cotes"]) - 1) * ba


def c12():
    """Taux de chute, espacement et bords perdus compris, en pour cent."""
    d = C.D_C12
    aire = sum((a + d["espacement"]) * (b + d["espacement"])
               for a, b in C.D_C12_PIECES)
    utile = ((C.D_C12_PLAQUE[0] - 2 * d["bord"])
             * (C.D_C12_PLAQUE[1] - 2 * d["bord"]))
    n = int(math.ceil(aire / utile))
    nue = sum(a * b for a, b in C.D_C12_PIECES)
    return 100.0 * (1.0 - nue / (n * C.D_C12_PLAQUE[0] * C.D_C12_PLAQUE[1]))


CALCULS = [
    (u"C-01", c01, 2), (u"C-02", c02, 2), (u"C-03", c03, 2),
    (u"C-04", c04, 2), (u"C-05", c05, 0), (u"C-06", c06, 2),
    (u"C-07", c07, 2), (u"C-08", c08, 3), (u"C-09", c09, 0),
    (u"C-10", c10, 0), (u"C-11", c11, 2), (u"C-12", c12, 2),
]


def main():
    par_id = dict((e["id"], e) for e in TOUS)
    lg = 66
    print("=" * lg)
    print(u"VÉRIFICATION DU LOT C — indicateurs recalculés")
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
        print(u"Les %d indicateurs annoncés correspondent au calcul."
              % len(CALCULS))
    print("=" * lg)
    return 0 if not ecarts and not absents else 1


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    sys.exit(main())
