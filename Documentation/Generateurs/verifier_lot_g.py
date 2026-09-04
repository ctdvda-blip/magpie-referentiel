# -*- coding: utf-8 -*-
"""Recalcule les trente-deux indicateurs du lot G et les confronte aux fiches.

    python Documentation/Generateurs/verifier_lot_g.py

La difference avec les lots B et C : la plupart des reponses du lot G sont des
LISTES — dix rangs de quiz, huit reponses d'une serie, seize colonnes d'un
tableau de synthese. La fiche est donc lue par tous ses nombres, et non par le
premier : chaque entree declare combien de valeurs sa reponse comporte.
"""
import io
import math
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)

import skill_g as G
from lots import TOUS

RE_NOMBRE = re.compile(u"[-+]?[0-9][0-9   ]*(?:[.,][0-9]+)?")


def annonces(txt, combien):
    """Les `combien` premiers nombres ecrits dans la reponse de la fiche."""
    out = []
    for m in RE_NOMBRE.finditer(txt or u""):
        brut = m.group(0)
        for espace in (u" ", u" ", u" "):
            brut = brut.replace(espace, u"")
        out.append(float(brut.replace(u",", u".")))
        if len(out) == combien:
            break
    return out


# ---------------------------------------------------------------------------
# Les trente-deux calculs
# ---------------------------------------------------------------------------

def g01():
    """Le tri, qui est la tache — et le score en decoule."""
    return sorted(G.D_G01)


def g02():
    """La somme des cinq perimetres : un polygone regulier fait n x cote."""
    d = G.D_G02
    return [2 * math.pi * d["rayon"] + 2 * sum(d["rectangle"])
            + 3 * d["triangle"] + 6 * d["hexagone"] + d["segment"]]


def g03():
    """Cinq extractions de cinq natures differentes."""
    a, b, c, d, e = G.D_G03
    return [a[3], b[-1], max(c), min(d), sorted(e)[len(e) // 2]]


def g04():
    """Les trois modes d'appariement : min, max, et le PRODUIT."""
    a, b = G.D_G04["a"], G.D_G04["b"]
    return [min(a, b) + max(a, b) + a * b]


def g05():
    """Six mesures d'un portique a profil CREUX."""
    d = G.D_G05
    dev = 2 * d["hauteur"] + d["entraxe"]
    sec = (d["largeur"] * d["section"]
           - (d["largeur"] - 2 * d["epaisseur"])
           * (d["section"] - 2 * d["epaisseur"]))
    vol = sec * dev
    return [dev, sec, vol / 1000.0, vol * d["densite"],
            d["hauteur"] + d["section"] / 2.0, d["entraxe"] - d["largeur"]]


def g06():
    """Trois filtres, chacun applique a ce que le precedent a LAISSE.

    Le troisieme seuil est la moyenne des survivants du deuxieme, pas celle
    des soixante valeurs de depart : c'est ce qui interdit de traiter les
    trois conditions independamment.
    """
    v = G.D_G06
    n1 = [i for i, x in enumerate(v) if x % 2 == 0]
    n2 = [i for i in n1 if v[i] > 500]
    moyenne = sum(v[i] for i in n2) / float(len(n2))
    return sorted(i for i in n2 if v[i] > moyenne)


def g07():
    """Le nombre de modules decoule du pas, arrondi vers le BAS."""
    d = G.D_G07
    return [int(d["longueur"] // d["pas_x"]) * int(d["largeur"] // d["pas_y"])]


def g08():
    """Huit manipulations ; la cinquieme exige un tri prealable."""
    s = G.D_G08
    return [len([v for v in s if v % 2 == 0]), max(s), min(s), sum(s),
            sorted(s)[len(s) // 2], s[0] + s[-1],
            len([v for v in s if v > 500]), sum(s[:4])]


def g09():
    return [sum(G.D_G09)]


def g10():
    """Les INDEX des trois coffres les plus riches, pas leurs contenus."""
    v = G.D_G10
    seuil = sorted(v)[-3]
    return sorted(i for i, x in enumerate(v) if x >= seuil)


def g11():
    return [sum(len(m) for m in G.D_G11)]


def g12():
    """Le partenaire de chaque carte : une permutation involutive."""
    part = [0] * 13
    for x, y in G.D_G12:
        part[x], part[y] = y, x
    return part[1:]


def g13():
    """Le seul triplet de decalages qui aligne la ligne CENTRALE."""
    r1, r2, r3 = G.D_G13
    c, n = G.D_G13_CENTRE, len(r1)
    sols = [[d1, d2, d3]
            for d1 in range(n) for d2 in range(n) for d3 in range(n)
            if r1[(c + d1) % n] == r2[(c + d2) % n] == r3[(c + d3) % n]]
    if len(sols) != 1:
        raise ValueError(u"G-13 : %d triplets alignent, la reponse n'est "
                         u"pas unique" % len(sols))
    return sols[0]


def g14():
    """La polyligne FERMEE : le segment de retour compte."""
    p = G.D_G14
    lg = sum(math.hypot(p[i + 1][0] - p[i][0], p[i + 1][1] - p[i][1])
             for i in range(len(p) - 1))
    return [lg + math.hypot(p[0][0] - p[-1][0], p[0][1] - p[-1][1])]


def _plein_g15():
    """La figure complete : la moitie droite SANS redoubler les points d'axe."""
    return G.D_G15 + [(-x, y) for x, y in reversed(G.D_G15[1:-1])]


def g15():
    p = _plein_g15()
    aire = 0.0
    for i in range(len(p)):
        x1, y1 = p[i]
        x2, y2 = p[(i + 1) % len(p)]
        aire += x1 * y2 - x2 * y1
    per = sum(math.hypot(p[(i + 1) % len(p)][0] - p[i][0],
                         p[(i + 1) % len(p)][1] - p[i][1])
              for i in range(len(p)))
    return [abs(aire) / 2.0, per]


def g16():
    """L'index du seul point qui sort du volume de reference."""
    lx, ly, lz = G.D_G16_VOLUME
    dehors = [i for i in range(len(G.D_G16_X))
              if not (0 <= G.D_G16_X[i] <= lx and 0 <= G.D_G16_Y[i] <= ly
                      and 0 <= G.D_G16_Z[i] <= lz)]
    if len(dehors) != 1:
        raise ValueError(u"G-16 : %d points hors volume, la reponse n'est "
                         u"pas unique" % len(dehors))
    return [float(dehors[0])]


def g17():
    return [float(rang) for _q, _p, rang in G.D_G17]


def g18():
    return [float(i + 1) for i, (_t, vrai) in enumerate(G.D_G18) if vrai]


def g19():
    """Les quatre composants reconnus, appliques au jeu de preuve."""
    j = G.D_G19
    return [len([v for v in j if v > 50]), sum(sorted(j)[-3:]),
            j.index(max(j)), len(set(v % 7 for v in j))]


def g20():
    d = G.D_G20
    return [d["nx"] * d["ny"] * d["cote"] ** 2]


def g21():
    """Le perimetre de l'etoile : deux sommets par branche."""
    d = G.D_G21
    n, re_, rc = d["dents"], d["rayon"], d["rayon"] - d["creux"]
    per = 0.0
    for i in range(2 * n):
        a1 = 2 * math.pi * i / (2 * n)
        a2 = 2 * math.pi * (i + 1) / (2 * n)
        r1 = re_ if i % 2 == 0 else rc
        r2 = re_ if (i + 1) % 2 == 0 else rc
        per += math.hypot(r2 * math.cos(a2) - r1 * math.cos(a1),
                          r2 * math.sin(a2) - r1 * math.sin(a1))
    return [per]


def g22():
    """Huit branches par pas de huit, double filtre, comptes puis sommes."""
    v, br = G.D_G22, G.D_G22_BRANCHES
    arbre = [v[i::br] for i in range(br)]
    gardes = [[x for x in b if x > 400 and x % 3 == 0] for b in arbre]
    return ([float(len(g)) for g in gardes] + [float(sum(g)) for g in gardes])


def g23():
    """La nomenclature triee par QUANTITE decroissante, pas par nom."""
    return [float(q) for _n, q in sorted(G.D_G23, key=lambda p: -p[1])]


def g24():
    """Les trois conditions par un ET, pas par un OU."""
    return [float(len([v for v in G.D_G24
                       if v % 4 == 0 and v > 120 and str(v)[-1] in u"048"]))]


def g25():
    """La longueur cumulee a mi-parcours, barres revelees de la plus courte."""
    lb = G.D_G25
    ordre = sorted(range(len(lb)), key=lambda i: lb[i])
    n_vis = int(round(G.D_G25_T * len(lb)))
    return [float(sum(lb[i] for i in ordre[:n_vis]))]


def g26():
    """Les DEUX bornes de la tolerance."""
    bas, haut = G.D_G26_BORNES
    return [float(len([v for v in G.D_G26 if v < bas or v > haut]))]


def g27():
    """Le perimetre de la harde : rayon de l'abreuvoir PLUS l'ecart au bord."""
    d = G.D_G27
    r = d["rayon_abreuvoir"] + d["ecart"]
    n = d["animaux"]
    return [n * 2 * r * math.sin(math.pi / n)]


def g28():
    """La somme des codes des soixante-douze combinaisons."""
    d = G.D_G28
    return [float(sum(f * 100 + m * 10 + c
                      for f in range(1, d["formes"] + 1)
                      for m in range(1, d["motifs"] + 1)
                      for c in range(1, d["couleurs"] + 1)))]


def g29():
    """La MEDIANE, pas la moyenne."""
    s = sorted(G.D_G29)
    return [float(s[len(s) // 2])]


def g30():
    """Les extremes ecartes DANS CHAQUE branche, puis moyennes."""
    v, br, ec = G.D_G30, G.D_G30_BRANCHES, G.D_G30_ECARTES
    par = len(v) // br
    total = 0.0
    for i in range(br):
        b = sorted(v[i * par:(i + 1) * par])[ec:-ec]
        total += sum(b) / float(len(b))
    return [total]


def g31():
    """Les notions COMPLETES, pas les notions entamees."""
    return [float(len([i for i in range(len(G.D_G31_PORTE))
                       if G.D_G31_VALIDE[i] >= G.D_G31_PORTE[i]]))]


def g32():
    """La structure cible decrite par ses EFFECTIFS de branche."""
    v, br = G.D_G32, G.D_G32_BRANCHES
    par = len(v) // br
    return [float(len([x for x in v[i * par:(i + 1) * par] if x % 5 == 0]))
            for i in range(br)]


#: (identifiant, fonction, nombre de decimales comparees)
CALCULS = [
    (u"G-01", g01, 0), (u"G-02", g02, 2), (u"G-03", g03, 0),
    (u"G-04", g04, 0), (u"G-05", g05, 1), (u"G-06", g06, 0),
    (u"G-07", g07, 0), (u"G-08", g08, 0), (u"G-09", g09, 0),
    (u"G-10", g10, 0), (u"G-11", g11, 0), (u"G-12", g12, 0),
    (u"G-13", g13, 0), (u"G-14", g14, 2), (u"G-15", g15, 2),
    (u"G-16", g16, 0), (u"G-17", g17, 0), (u"G-18", g18, 0),
    (u"G-19", g19, 0), (u"G-20", g20, 0), (u"G-21", g21, 2),
    (u"G-22", g22, 0), (u"G-23", g23, 0), (u"G-24", g24, 0),
    (u"G-25", g25, 0), (u"G-26", g26, 0), (u"G-27", g27, 2),
    (u"G-28", g28, 0), (u"G-29", g29, 0), (u"G-30", g30, 4),
    (u"G-31", g31, 0), (u"G-32", g32, 0),
]


def main():
    par_id = dict((e["id"], e) for e in TOUS)
    lg = 74
    print("=" * lg)
    print(u"VÉRIFICATION DU LOT G — indicateurs recalculés")
    print("=" * lg)
    ecarts, absents = [], []
    for eid, fn, dec in CALCULS:
        e = par_id.get(eid)
        if e is None:
            absents.append(eid)
            continue
        try:
            calcule = fn()
        except ValueError as ex:
            ecarts.append((eid, u"%s" % ex, u"—"))
            print(u"%-8s %s" % (eid, ex))
            continue
        dites = annonces(e.get(u"att"), len(calcule))
        marge = 0.5 * 10 ** (-dec) if dec else 1e-9
        ok = (len(dites) == len(calcule)
              and all(abs(float(a) - b) <= marge
                      for a, b in zip(calcule, dites)))
        apercu = u", ".join((u"%%.%df" % dec) % v for v in calcule)
        if len(apercu) > 44:
            apercu = apercu[:41] + u"..."
        print(u"%-8s %-46s %s" % (eid, apercu, u"OK" if ok else u"<<< ÉCART"))
        if not ok:
            ecarts.append((eid, dites, calcule))
    print("-" * lg)
    if absents:
        print(u"Absents du registre : %s" % u", ".join(absents))
    if ecarts:
        print(u"ÉCARTS : %d" % len(ecarts))
        for eid, dite, calcule in ecarts:
            print(u"   %-8s fiche   %s" % (eid, dite))
            print(u"   %-8s calcul  %s" % (u"", calcule))
    else:
        print(u"Les %d indicateurs annoncés correspondent au calcul."
              % len(CALCULS))
    print("=" * lg)
    return 0 if not ecarts and not absents else 1


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    sys.exit(main())
