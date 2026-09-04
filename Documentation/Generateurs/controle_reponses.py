# -*- coding: utf-8 -*-
"""Recalcule les reponses attendues du lot A sur les jeux de donnees refondus.

La skill impose (« Verifier avant de livrer », point 2) que les valeurs
attendues soient RELEVEES et non deduites. Ce script rejoue le calcul a partir
de la source unique (skill_a.py) et compare a ce que les fiches annoncent.
Il sort en code 1 des qu'un ecart apparait : la chaine de generation ne doit
pas produire de fiche affirmant une valeur fausse.
"""
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)

import skill_a as S
from exos_a import LOT_A
from skill_a import fusionner


def attendus():
    """Les valeurs recalculees, exercice par exercice."""
    d = {}
    d[u"A-08"] = sum(1 for v in S.D_A08 if abs(v - 1200) > 5)
    d[u"A-09"] = sum(1 for v in S.D_A09 if v is not None)
    d[u"A-11"] = (S.D_A11[3], S.D_A11[-1])
    d[u"A-12"] = (len(S.D_A12), min(S.D_A12), max(S.D_A12))
    d[u"A-14"] = len(S.D_A14[0::3])
    d[u"A-15"] = sum(1 for v in S.D_A15 if v > 2.50)
    d[u"A-18"] = tuple(S.D_A18[5:13])
    d[u"A-30"] = sum(1 for v in S.D_A30 if 500 <= v <= 1500)
    paires = sorted(zip(S.D_A13_LONG, S.D_A13_REP), reverse=True)
    d[u"A-13"] = tuple(r for _, r in paires)
    tisse = []
    for a, b in zip(S.D_A17_LG_CHENE, S.D_A17_LG_NOYER):
        tisse.extend([a, b])
    d[u"A-17"] = tuple(tisse)
    return d


def nombres(txt):
    """Extrait les entiers d'un texte, espaces insecables des milliers compris."""
    txt = txt.replace(u"\u00a0", u"").replace(u"\u202f", u"")
    txt = re.sub(u"(?<=[0-9]) (?=[0-9])", u"", txt)
    return [int(x) for x in re.findall(u"[0-9]+", txt)]


def main():
    calc = attendus()
    fiches = dict((e["id"], fusionner(e)) for e in LOT_A)
    ecarts = []
    for eid, valeur in sorted(calc.items()):
        annonce = nombres(fiches[eid]["att"])
        if isinstance(valeur, tuple):
            attendu = list(valeur)
        else:
            attendu = [valeur]
        # la fiche peut citer d'autres nombres (unites, bornes) : on verifie
        # que la suite attendue y figure telle quelle, dans l'ordre.
        ok = any(annonce[i:i + len(attendu)] == attendu
                 for i in range(len(annonce) - len(attendu) + 1))
        etat = u"ok" if ok else u"ECART"
        if not ok:
            ecarts.append((eid, attendu, annonce))
        print(u"%-6s %-6s calcule=%s  fiche=%s"
              % (eid, etat, attendu, annonce))

    print(u"")
    if ecarts:
        print(u"%d écart(s) entre le calcul et ce qu'annoncent les fiches." % len(ecarts))
        return 1
    print(u"Les %d réponses attendues sont conformes au calcul." % len(calc))
    return 0


if __name__ == "__main__":
    sys.exit(main())
