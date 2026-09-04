# -*- coding: utf-8 -*-
"""Recalcule les dix-huit reponses du lot B et les confronte aux fiches.

Meme mecanique que les verificateurs de vague.

    python Documentation/Generateurs/verifier_lot_b.py
"""
import io
import math
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)

import skill_b as B
from verifier_vague1 import annonce
from lots import TOUS


def b01():
    """Blondel, sur la hauteur de marche RECALEE."""
    d = B.D_B01
    n = int(round(d["hauteur"] / d["visee"]))
    return 2 * (d["hauteur"] / n) + d["giron"]


def b02():
    """Barreaux : le pas est l'espacement libre PLUS le diametre."""
    d = B.D_B02
    n = int(math.ceil((d["longueur"] - d["diametre"])
                      / (d["libre_max"] + d["diametre"])))
    return n - 1


def b03():
    """Aire percee, en metres carres. L'aire varie comme le carre du rayon."""
    d = B.D_B03
    att = (d["attracteur"][0] * d["pas"], d["attracteur"][1] * d["pas"])
    centres = [((i + 0.5) * d["pas"], (j + 0.5) * d["pas"])
               for j in range(d["ny"]) for i in range(d["nx"])]
    dist = [math.hypot(c[0] - att[0], c[1] - att[1]) for c in centres]
    dmin, dmax = min(dist), max(dist)
    rayons = [d["rayon_max"] + (d["rayon_min"] - d["rayon_max"])
              * (x - dmin) / (dmax - dmin) for x in dist]
    return sum(math.pi * r * r for r in rayons) / 1e6


def b04():
    """Hexagones : le pas d'une trame hexagonale n'est pas son cote."""
    d = B.D_B04
    px, py = math.sqrt(3) * d["cote"], 1.5 * d["cote"]
    return int(d["largeur"] // px) * int(d["profondeur"] // py)


def b05():
    """Lineaire de membrures et de diagonales, en metres."""
    d = B.D_B05
    pas = d["portee"] / d["panneaux"]
    diag = d["panneaux"] * math.hypot(pas, d["hauteur"])
    return (2 * d["portee"] + diag) / 1000.0


def b06():
    """Volume de panneau, fond compris avec ses rainures, en dm3."""
    d = B.D_B06
    l, h, p, e, r = (d["largeur"], d["hauteur"], d["profondeur"],
                     d["epaisseur"], d["rainure"])
    joues = 2 * (h * p * e)
    traverses = 2 * ((l - 2 * e) * p * e)
    fond = (l - 2 * e + 2 * r) * (h - 2 * e + 2 * r) * e
    return (joues + traverses + fond) / 1e6


def b07():
    """Largeur du tiroir : le jeu se retranche des DEUX cotes."""
    d, j = B.D_B06, B.D_B07
    return d["largeur"] - 2 * d["epaisseur"] - 2 * j["jeu_lateral"]


def b08():
    """Le plus grand entre-deux d'une progression arithmetique."""
    d = B.D_B08
    n = d["tablettes"] + 1
    libre = d["hauteur"] - d["tablettes"] * d["epaisseur"]
    r = (libre - n * d["mini"]) / (n * (n - 1) / 2.0)
    return d["mini"] + (n - 1) * r


def b09():
    """Longueur de fil : la griffe est inclinee."""
    d = B.D_B09
    return d["griffes"] * d["hauteur"] / math.cos(math.radians(d["inclinaison"]))


def b10():
    d = B.D_B10
    return d["circonference"] / d["modules"]


def b11():
    """Maillons : le pas est le maillon MOINS le recouvrement."""
    d = B.D_B11
    pas = d["maillon"] - d["recouvrement"]
    return int(math.floor((d["courbe"] - d["maillon"]) / pas)) + 1


def b12():
    return B.D_B12["pieces"] + 1


def b13():
    """Taux de chute theorique, en pour cent."""
    aire = sum(a * b for a, b in B.D_B13_PIECES)
    plaque = B.D_B13_PLAQUE[0] * B.D_B13_PLAQUE[1]
    n = int(math.ceil(aire / plaque))
    return 100.0 * (1.0 - aire / (n * plaque))


def b14():
    """Rang de la piece visee : rangee d'abord, colonne ensuite."""
    pos = B.D_B14_POSITIONS
    ordre = sorted(range(len(pos)), key=lambda i: (pos[i][1], pos[i][0]))
    return ordre.index(pos.index(B.D_B14_CIBLE)) + 1


def b15():
    """Barres consommees par la regle du plus grand d'abord."""
    restes = []
    for x in sorted(B.D_B15_LONGUEURS, reverse=True):
        for k, r in enumerate(restes):
            if r >= x:
                restes[k] = r - x
                break
        else:
            restes.append(B.D_B15_BARRE - x)
    return len(restes)


def b16():
    """Surface developpee, en metres carres. La largeur varie lineairement."""
    d = B.D_B16
    moyenne = (d["largeur_extremite"] + d["largeur_milieu"]) / 2.0
    return d["lamelles"] * d["hauteur"] * moyenne / 1e6


def b17():
    """Lineaire de nervure, en metres : l'ARC, pas la corde."""
    d = B.D_B17
    r = (d["corde"] ** 2 / 4 + d["fleche"] ** 2) / (2 * d["fleche"])
    arc = 2 * math.asin(d["corde"] / (2 * r)) * r
    return d["nervures"] * arc / 1000.0


def b18():
    """Diametre a fond de filet ISO : d - 1,2269 x pas."""
    d = B.D_B18
    return d["diametre"] - 1.226869 * d["pas"]


CALCULS = [
    (u"B-01", b01, 2), (u"B-02", b02, 0), (u"B-03", b03, 2),
    (u"B-04", b04, 0), (u"B-05", b05, 2), (u"B-06", b06, 2),
    (u"B-07", b07, 0), (u"B-08", b08, 2), (u"B-09", b09, 2),
    (u"B-10", b10, 2), (u"B-11", b11, 0), (u"B-12", b12, 0),
    (u"B-13", b13, 2), (u"B-14", b14, 0), (u"B-15", b15, 0),
    (u"B-16", b16, 4), (u"B-17", b17, 2), (u"B-18", b18, 2),
]


def main():
    par_id = dict((e["id"], e) for e in TOUS)
    lg = 66
    print("=" * lg)
    print(u"VÉRIFICATION DU LOT B — valeurs recalculées")
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
