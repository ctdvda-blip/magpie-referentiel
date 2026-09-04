# -*- coding: utf-8 -*-
"""Propage le numero de version aux descripteurs .json deja produits.

Le champ `version` d'un descripteur vient de `gh_engine.VERSION`, posee a la
CONSTRUCTION de la definition. Le propager par une reconstruction reviendrait
a reecrire les 284 fichiers .gh — et Grasshopper leur reattribue des GUID a
chaque ecriture, donc a republier une centaine de megaoctets pour un champ de
texte.

Ce script fait le contraire : il reecrit le seul champ `version`, laisse les
definitions intactes, et conserve l'ordre trie des clefs.

    python Documentation/Generateurs/propager_version.py
"""
import io
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PROJET = os.path.abspath(os.path.join(ICI, "..", ".."))
sys.path.insert(0, ICI)
sys.path.insert(0, os.path.join(ICI, "GH"))

from lots import LOTS


def version_courante():
    """Celle des generateurs, source unique."""
    import re
    s = io.open(os.path.join(ICI, "gen_application.py"), encoding="utf-8").read()
    m = re.search(r'^VERSION = "([^"]+)"', s, re.M)
    return m.group(1) if m else None


def main():
    version = version_courante()
    if not version:
        print(u"Version introuvable dans gen_application.py.")
        return 1
    print(u"Version à propager : %s" % version)
    touches, deja, absents = 0, 0, 0
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
                absents += 1
                continue
            data = json.loads(io.open(p, encoding="utf-8").read())
            if data.get(u"version") == version:
                deja += 1
                continue
            data[u"version"] = version
            fh = io.open(p, "w", encoding="utf-8")
            try:
                # meme separateur que les constructeurs : sans lui, les
                # deux ecritures different d'une espace par ligne.
                fh.write(json.dumps(data, indent=2, ensure_ascii=False,
                                    sort_keys=True,
                                    separators=(",", ": ")))
            finally:
                fh.close()
            touches += 1
    print(u"Descripteurs mis à jour : %d" % touches)
    print(u"Déjà à la bonne version : %d" % deja)
    if absents:
        print(u"Sans descripteur (livrable non graphique) : %d" % absents)
    return 0


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    sys.exit(main())
