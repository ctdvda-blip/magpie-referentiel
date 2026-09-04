# -*- coding: utf-8 -*-
"""Recalcule les vingt-quatre reponses de la vague 4 et les confronte aux fiches.

    python Documentation/Generateurs/verifier_vague4.py

Comme pour le lot G, deux reponses sont des LISTES : chaque entree declare
combien de valeurs elle comporte, et la fiche est lue par ses premiers
nombres.
"""
import io
import itertools
import math
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)

import exercices_vague4 as V
from lots import TOUS

RE_NOMBRE = re.compile(u"[-+]?[0-9][0-9   ]*(?:[.,][0-9]+)?")


def annonces(txt, combien):
    """Les `combien` premiers nombres ecrits dans la reponse de la fiche."""
    out = []
    for m in RE_NOMBRE.finditer(txt or u""):
        brut = m.group(0)
        for espace in (u" ", u" ", u" "):
            brut = brut.replace(espace, u"")
        out.append(float(brut.replace(u",", u".")))
        if len(out) == combien:
            break
    return out


# ---------------------------------------------------------------------------
# Les vingt-quatre calculs
# ---------------------------------------------------------------------------

def pl13():
    """Seulement sur Food4Rhino : l'EXCLUSIVITE, pas la presence."""
    return [len([1 for _n, pm, f4r in V.D_PL13 if f4r and not pm])]


def pl14():
    """Ce que l'ergonomie AJOUTE : sans ce qu'un autre plugin exige deja."""
    return [sum(ms for _n, ms, deja in V.D_PL14 if not deja)]


def pl15():
    """Le plus petit nombre de plugins couvrant les douze composants."""
    fourni = dict((n, set(c)) for n, c in V.D_PL15_FOURNI)
    besoin = set(V.D_PL15_BESOIN)
    noms = sorted(fourni)
    for k in range(1, len(noms) + 1):
        for combi in itertools.combinations(noms, k):
            couvre = set()
            for c in combi:
                couvre |= fourni[c]
            if besoin <= couvre:
                return [float(k)]
    raise ValueError(u"PL-15 : aucun sous-ensemble ne couvre le besoin")


def pl16():
    """Les DEUX bornes de l'intervalle de compatibilite."""
    return [len([1 for _n, mi, ma in V.D_PL16 if mi <= 8 <= ma])]


def rh24():
    """Les parois trop minces APRES mise a l'echelle."""
    return [len([1 for v in V.D_RH24
                 if v / 100.0 * V.D_RH24_ECHELLE < V.D_RH24_MINI])]


def rh25():
    """Etanche : zero arete nue ET zero arete non-manifold."""
    return [len([1 for nu, nm in V.D_RH25 if nu == 0 and nm == 0])]


def rh26():
    """STL binaire : 84 octets d'en-tete, 50 par triangle."""
    return [84 + 50 * V.D_RH26_TRIANGLES]


def rh27():
    """Socle plus fut, moins la partie encastree — comptee deux fois."""
    d = V.D_RH27
    socle = d["longueur"] * d["largeur"] * d["hauteur"]
    fut = math.pi * d["rayon"] ** 2 * d["hauteur_cyl"]
    commun = math.pi * d["rayon"] ** 2 * d["enfoncement"]
    return [(socle + fut - commun) / 1e6]


def rh28():
    """Le perimetre du contour FERME, developpe sur la hauteur."""
    p = V.D_RH28
    per = sum(math.hypot(p[(i + 1) % len(p)][0] - p[i][0],
                         p[(i + 1) % len(p)][1] - p[i][1])
              for i in range(len(p)))
    return [per * V.D_RH28_HAUTEUR / 1e6]


def rh29():
    """L'aire d'un trou va comme le carre du RAYON, pas du diametre."""
    d = V.D_RH29
    plein = d["longueur"] * d["largeur"] * d["epaisseur"]
    trous = (d["nx"] * d["ny"] * math.pi * (d["diametre"] / 2.0) ** 2
             * d["epaisseur"])
    return [(plein - trous) / 1e6]


def rh30():
    """Le bon type, le bon calque, et NON verrouille."""
    return [len([1 for ty, ca, ve in V.D_RH30
                 if ty == u"Courbe" and ca == u"10-Porteurs" and not ve])]


def rh31():
    """Visible : calque allume ET objet non masque."""
    return [len([1 for _g, calque, masque in V.D_RH31 if calque and not masque])]


def rh32():
    """Suivront le calque : ceux dont la couleur est heritee."""
    return [len([1 for c in V.D_RH32 if c == u"ParCalque"])]


def gp13():
    """Rectangle, moins les quatre conges, moins les sept percages."""
    d = V.D_GP13
    aire = d["longueur"] * d["largeur"] - (4 - math.pi) * d["conge"] ** 2
    aire -= d["percements"] * math.pi * (d["percage"] / 2.0) ** 2
    return [aire * d["epaisseur"] / 1e6]


def wb10():
    """Ce que le format PERD, pas ce qu'il conserve."""
    return [len([1 for _a, formats in V.D_WB10
                 if V.D_WB10_FORMAT not in formats])]


def wb11():
    """Le temps local, multiplie par le facteur serveur."""
    return [sum(V.D_WB11) * V.D_WB11_FACTEUR / 1000.0]


def ia26():
    """Les sommes cumulees, dans l'ordre."""
    out, cumul = [], 0
    for v in V.D_IA26:
        cumul += v
        out.append(float(cumul))
    return out


def ia27():
    """Le compte exact : la DERNIERE valeur compte aussi."""
    return [len([1 for v in V.D_IA27 if v > V.D_IA27_SEUIL])]


def ia28():
    """L'effectif de la famille la plus fournie, sur DEUX criteres."""
    sl, se = V.D_IA28_SEUILS
    familles = {}
    for lg, ep in V.D_IA28:
        cle = (lg > sl, ep > se)
        familles[cle] = familles.get(cle, 0) + 1
    return [float(max(familles.values()))]


def ia29():
    """Les DEFINITIONS cassees, pas les composants regeneres."""
    return [sum(n for _c, garde, n in V.D_IA29 if not garde)]


def ia30():
    """Trois appels par recalcul, pas un."""
    d = V.D_IA30
    return [d["appels_par_recalcul"] * d["recalculs"] * d["prix"]]


def ia31():
    """Toute operation d'ECRITURE, pas seulement ajout et suppression."""
    ecr = set(V.D_IA31_ECRITURE)
    return [len([1 for a in V.D_IA31 if a in ecr])]


def ia32():
    """Quatre lectures defendables d'une meme consigne."""
    j = V.D_IA32
    seuil = V.D_IA32_SEUIL
    moyenne = sum(j) / float(len(j))
    tri = sorted(j)
    n = len(tri)
    mediane = (tri[n // 2] if n % 2 else (tri[n // 2 - 1] + tri[n // 2]) / 2.0)
    return [float(len([1 for v in j if v > seuil])),
            float(len([1 for v in j if v >= seuil])),
            float(len([1 for v in j if v > moyenne])),
            float(len([1 for v in j if v > mediane]))]


def ia33():
    """Cinq montants pour six travees, et l'imposte a deduire."""
    d = V.D_IA33
    largeur = (d["largeur"] - (d["travees"] - 1) * d["montant"]) / d["travees"]
    return [largeur, d["hauteur"] - d["imposte"]]


#: (identifiant, fonction, nombre de decimales comparees)
CALCULS = [
    (u"PL-13", pl13, 0), (u"PL-14", pl14, 0), (u"PL-15", pl15, 0),
    (u"PL-16", pl16, 0), (u"RH-24", rh24, 0), (u"RH-25", rh25, 0),
    (u"RH-26", rh26, 0), (u"RH-27", rh27, 4), (u"RH-28", rh28, 4),
    (u"RH-29", rh29, 4), (u"RH-30", rh30, 0), (u"RH-31", rh31, 0),
    (u"RH-32", rh32, 0), (u"GP-13", gp13, 4), (u"WB-10", wb10, 0),
    (u"WB-11", wb11, 4), (u"IA-26", ia26, 0), (u"IA-27", ia27, 0),
    (u"IA-28", ia28, 0), (u"IA-29", ia29, 0), (u"IA-30", ia30, 2),
    (u"IA-31", ia31, 0), (u"IA-32", ia32, 0), (u"IA-33", ia33, 4),
]


def main():
    par_id = dict((e["id"], e) for e in TOUS)
    lg = 74
    print("=" * lg)
    print(u"VÉRIFICATION DE LA VAGUE 4 — valeurs recalculées")
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
        print(u"Les %d valeurs annoncées correspondent au calcul."
              % len(CALCULS))
    print("=" * lg)
    return 0 if not ecarts and not absents else 1


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    sys.exit(main())
