# -*- coding: utf-8 -*-
"""Dresse la liste des entrees/sorties reelles de chaque composant employe."""
import sys
GH = r"C:\Users\charl\.claude\projects\MAGPIE\Documentation\Generateurs\GH"
GEN = r"C:\Users\charl\.claude\projects\MAGPIE\Documentation\Generateurs"
for p in (GH, GEN):
    if p not in sys.path:
        sys.path.insert(0, p)
for m in ("gh_engine", "recipes_a1", "recipes_a2", "recipes_a3", "recipes_a4"):
    if m in sys.modules:
        del sys.modules[m]

import gh_engine as E
import recipes_a1, recipes_a2, recipes_a3, recipes_a4

R = {}
for m in (recipes_a1, recipes_a2, recipes_a3, recipes_a4):
    R.update(m.R)

SPECIAUX = ("SLIDER", "PANEL", "TOGGLE", "VALUELIST", "REPONSE")
labels = set()
for r in R.values():
    specs = list(r.get("sujet", []))
    for _, ss in r.get("corrige", []):
        specs += ss
    for s in specs:
        l = s[1]
        if l not in SPECIAUX and not l.startswith(("DATA:", "PARAM:", "GEO:")):
            labels.add(l)

for lb in sorted(labels):
    try:
        o = E.emit(lb)
    except Exception as e:
        print("%-30s INSTANCIATION IMPOSSIBLE : %s" % (lb, e))
        continue
    try:
        ins = [p.Name for p in o.Params.Input]
        outs = [p.Name for p in o.Params.Output]
    except Exception:
        print("%-30s (parametre flottant)" % lb)
        continue
    print("%-30s IN  %s" % (lb.split("/")[-1], " | ".join("%d:%s" % (i, n) for i, n in enumerate(ins))))
    print("%-30s OUT %s" % ("", " | ".join("%d:%s" % (i, n) for i, n in enumerate(outs))))
