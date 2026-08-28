# -*- coding: utf-8 -*-
"""Controles finaux : etancheite des sujets, accentuation, cas A-46."""
import os
import clr
clr.AddReference("Grasshopper")
from Grasshopper.Kernel import GH_DocumentIO
from Grasshopper.Kernel.Special import GH_Scribble

RACINE = r"C:\Users\charl\.claude\projects\MAGPIE\EXERCICES\LOT A - Composants natifs"


def ouvrir(p):
    io = GH_DocumentIO()
    if not io.Open(p):
        return None
    return io.Document


# --- 1. etancheite des fichiers sujet
fuites, sans_rep, ok = [], [], 0
for d in sorted(os.listdir(RACINE)):
    dd = os.path.join(RACINE, d)
    if not os.path.isdir(dd):
        continue
    ident = d.split(" ")[0]
    p = os.path.join(dd, "%s_sujet.gh" % ident)
    if not os.path.isfile(p):
        continue
    doc = ouvrir(p)
    if doc is None:
        fuites.append((ident, "ouverture impossible"))
        continue
    noms = []
    rep = None
    for o in doc.Objects:
        try:
            noms.append(o.NickName or "")
        except Exception:
            pass
        try:
            if o.NickName == "REPONSE":
                rep = o
        except Exception:
            pass
    txt = " ".join(noms)
    if u"CORRIG" in txt.upper() or u"TAPE " in txt.upper():
        fuites.append((ident, "le corrige subsiste : " + txt[:80]))
    if rep is None:
        sans_rep.append(ident)
    else:
        try:
            n = rep.SourceCount
        except Exception:
            n = -1
        if n != 0:
            fuites.append((ident, "REPONSE encore alimentee (%s source)" % n))
        else:
            ok += 1

print("1. ETANCHEITE DES FICHIERS SUJET")
print("   sujets avec REPONSE libre de toute source : %d" % ok)
print("   sans parametre REPONSE                    : %d %s" % (len(sans_rep), sans_rep))
print("   anomalies                                 : %d" % len(fuites))
for i, m in fuites[:10]:
    print("      %s : %s" % (i, m))

# --- 2. accentuation des scribbles
print("")
print("2. ACCENTUATION (scribbles du fichier A-13)")
p = os.path.join(RACINE, u"A-13 Trier une liste avec une cl\u00e9", "A-13_complet.gh")
doc = ouvrir(p)
if doc:
    n = 0
    for o in doc.Objects:
        if isinstance(o, GH_Scribble):
            t = o.Text or ""
            if n < 4:
                print("   %s" % t.replace("\n", " / ")[:110])
            n += 1

# --- 3. A-46 : sous-ensemble de blocs en collision
print("")
print("3. A-46 : blocs designes comme en collision")
p = os.path.join(RACINE, u"A-46 D\u00e9tecter une collision", "A-46_complet.gh")
doc = ouvrir(p)
if doc:
    doc.Enabled = True
    doc.NewSolution(True)
    for o in doc.Objects:
        try:
            if o.NickName == "REPONSE":
                print("   blocs retenus : %d sur 15" % o.VolatileDataCount)
        except Exception:
            pass
