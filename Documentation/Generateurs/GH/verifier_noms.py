# -*- coding: utf-8 -*-
import re, sys, difflib
import glob, os
BASE = r"C:/Program Files/Rhino 8/Plug-ins/Grasshopper"
FILES = [os.path.join(BASE, "Grasshopper.dll")] + sorted(
    glob.glob(os.path.join(BASE, "Components", "*.gha")))
raw = b""
for f in FILES:
    raw += open(f, "rb").read()
print("Assemblages scannes : %d (%.1f Mo)" % (len(FILES), len(raw)/1048576.0))

# chaines UTF-16LE : caracteres ASCII imprimables alternes avec 0x00
pat = re.compile(rb'(?:[\x20-\x7E]\x00){2,60}')
strings = set()
for m in pat.finditer(raw):
    s = m.group().decode('utf-16-le')
    strings.add(s)
print("Chaines UTF-16 distinctes extraites :", len(strings))

sys.path.insert(0, r"C:/Users/charl/.claude/projects/MAGPIE/Documentation/Generateurs/GH")
sys.path.insert(0, r"C:/Users/charl/.claude/projects/MAGPIE/Documentation/Generateurs")
import recipes_a1, recipes_a2, recipes_a3, recipes_a4
R = {}
for m in (recipes_a1, recipes_a2, recipes_a3, recipes_a4): R.update(m.R)
SPECIAUX = ("SLIDER","PANEL","TOGGLE","VALUELIST","REPONSE")
labels = set()
for r in R.values():
    specs = list(r.get("sujet", []))
    for _, ss in r.get("corrige", []): specs += ss
    for s in specs:
        l = s[1]
        if l not in SPECIAUX and not l.startswith(("DATA:","PARAM:","GEO:")):
            labels.add(l)

ok, ko = [], []
for l in sorted(labels):
    (ok if l in strings else ko).append(l)
print("")
print("TROUVES  : %d / %d" % (len(ok), len(labels)))
print("ABSENTS  : %d" % len(ko))
print("")
for l in ko:
    prop = difflib.get_close_matches(l, [s for s in strings if 2 < len(s) < 32], n=6, cutoff=0.62)
    print("  %-24s -> propositions : %s" % (l, ", ".join(repr(p) for p in prop) if prop else "(aucune)"))
