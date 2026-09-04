# -*- coding: utf-8 -*-
"""Recette 8 — un nom d'objet ne doit designer qu'une seule chose.

Les recettes nomment leurs objets par une cle courte, et le moteur les range
dans une table nom -> objet. Si le sujet appelle un curseur « m » et que le
corrige appelle « m » une division, la seconde ECRASE le premier : les fils
partent alors du mauvais objet, silencieusement. Le .gh se construit, il
s'ouvre, il ne signale rien — et il repond faux.

C'est exactement ce qui est arrive a C-02, dont le lineaire de barres est
tombe a 0,0034 m au lieu de 695,53. La valeur relevee l'a rattrape ; ce
controle le rattrape plus tot, et sur les cent quatre-vingt-dix recettes a la
fois.

    python Documentation/Generateurs/GH/recette_8_noms_uniques.py
"""
import importlib
import io
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.abspath(os.path.join(ICI, ".."))
for _p in (ICI, GEN):
    if _p not in sys.path:
        sys.path.insert(0, _p)


def modules():
    """Les modules de recettes, DECOUVERTS et non listes."""
    return [f[:-3] for f in sorted(os.listdir(ICI))
            if f.startswith("recipes_") and f.endswith(".py")]


def doublons(recette):
    """Les noms employes deux fois, avec l'endroit du premier emploi."""
    vus, dbl = {}, []
    for o in recette.get("sujet", []):
        vus[o[0]] = u"sujet"
    for _commentaire, objets in recette.get("corrige", []):
        for o in objets:
            if o[0] in vus:
                dbl.append((o[0], vus[o[0]]))
            vus[o[0]] = u"corrigé"
    return dbl


def main():
    lg = 74
    print("=" * lg)
    print(u"RECETTE 8 — unicité des noms d'objets dans les recettes")
    print("=" * lg)
    fautives, recettes, illisibles = [], 0, []
    for nom in modules():
        try:
            mod = importlib.import_module(nom)
        except Exception as ex:
            illisibles.append((nom, ex))
            continue
        for eid, r in sorted(getattr(mod, "R", {}).items()):
            recettes += 1
            dbl = doublons(r)
            if dbl:
                fautives.append((eid, nom, dbl))
    for eid, nom, dbl in fautives:
        print(u"%-8s (%s) : %s" % (eid, nom, u", ".join(
            u"« %s » déjà employé dans le %s" % t for t in dbl)))
    for nom, ex in illisibles:
        print(u"%-8s module illisible : %s" % (nom, ex))
    print("-" * lg)
    print(u"%d recettes contrôlées, %d avec doublon de nom." % (recettes, len(fautives)))
    print("=" * lg)
    return 0 if not fautives and not illisibles else 1


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    sys.exit(main())
