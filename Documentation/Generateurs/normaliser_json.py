# -*- coding: utf-8 -*-
"""Reecrit les descripteurs .json des exercices, clefs triees.

Les constructeurs ecrivaient `json.dumps(d, indent=2)` sans `sort_keys`.
IronPython rend alors les clefs dans un ordre qui varie d'une execution a
l'autre : le fichier differait a chaque reconstruction sans qu'un caractere de
contenu ait bouge, et la publication recopiait des dizaines de mega-octets de
definitions et de fiches pour cette seule raison.

Les constructeurs sont corriges. Ce script remet les fichiers deja produits
dans la forme triee, sans rien reconstruire — donc sans Rhino, et sans
reattribuer les GUID des definitions.

    python Documentation/Generateurs/normaliser_json.py
"""
import io
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PROJET = os.path.abspath(os.path.join(ICI, "..", ".."))
sys.path.insert(0, ICI)
from lots import LOTS


def main():
    tries, deja = 0, 0
    for _code, _nom, rel, lot in LOTS:
        racine = os.path.join(PROJET, rel.replace("/", os.sep))
        if not os.path.isdir(racine):
            continue
        for d in sorted(os.listdir(racine)):
            dd = os.path.join(racine, d)
            if not os.path.isdir(dd):
                continue
            eid = d.split(" ")[0]
            p = os.path.join(dd, "%s.json" % eid)
            if not os.path.isfile(p):
                continue
            avant = io.open(p, encoding="utf-8").read()
            # Meme forme canonique que les constructeurs : clefs triees ET
            # separateur fige. IronPython ecrit sinon une espace avant le
            # saut de ligne, la ou Python 3 n'en met pas — trente-deux
            # espaces invisibles d'ecart, et la publication recopie.
            apres = json.dumps(json.loads(avant), indent=2,
                               ensure_ascii=False, sort_keys=True,
                               separators=(",", ": "))
            if avant.rstrip() == apres.rstrip():
                deja += 1
                continue
            fh = io.open(p, "w", encoding="utf-8")
            try:
                fh.write(apres)
            finally:
                fh.close()
            tries += 1
    print(u"Descripteurs triés  : %d" % tries)
    print(u"Déjà en forme       : %d" % deja)
    return 0


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    sys.exit(main())
