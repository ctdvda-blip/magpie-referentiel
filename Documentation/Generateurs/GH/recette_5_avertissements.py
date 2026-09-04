# -*- coding: utf-8 -*-
"""Audit des AVERTISSEMENTS (et non plus seulement des erreurs), sujets et corriges."""
import os
import clr
clr.AddReference("Grasshopper")
from Grasshopper.Kernel import GH_DocumentIO, GH_RuntimeMessageLevel as LVL

RACINE = r"C:\Users\charl\.claude\projects\MAGPIE\EXERCICES\LOT A - Composants natifs"


def analyser(path, activer_corrige):
    io = GH_DocumentIO()
    if not io.Open(path):
        return None
    doc = io.Document
    doc.Enabled = True
    if activer_corrige:
        for o in doc.Objects:
            try:
                if (o.NickName or "") == u"AFFICHER LE CORRIGÉ":
                    o.Value = True
                    o.ExpireSolution(False)
            except Exception:
                pass
    try:
        doc.NewSolution(True)
    except Exception as e:
        return [("SOLUTION", str(e))]
    msgs = []
    for o in doc.Objects:
        try:
            lvl = o.RuntimeMessageLevel
        except Exception:
            continue
        for niveau, code in ((LVL.Error, "ERR"), (LVL.Warning, "AVT")):
            if lvl == niveau or code == "AVT":
                try:
                    for m in o.RuntimeMessages(niveau):
                        msgs.append((code, u"%s : %s" % (o.Name, m)))
                except Exception:
                    pass
    return msgs


agg = {}
detail = []
for d in sorted(os.listdir(RACINE)):
    dd = os.path.join(RACINE, d)
    if not os.path.isdir(dd):
        continue
    ident = d.split(" ")[0]
    for suffixe, act in (("_sujet.gh", False), ("_complet.gh", True)):
        p = os.path.join(dd, ident + suffixe)
        if not os.path.isfile(p):
            continue
        msgs = analyser(p, act) or []
        for code, m in msgs:
            cle = (suffixe.replace(".gh", "").strip("_"), code, m.split(" : ")[0],
                   m.split(" : ", 1)[1][:70] if " : " in m else m)
            agg[cle] = agg.get(cle, 0) + 1
            detail.append((ident, suffixe, code, m))

print("AUDIT DES AVERTISSEMENTS ET ERREURS")
print("=" * 78)
if not agg:
    print("Aucun message : ni erreur, ni avertissement.")
else:
    print("%-8s %-4s %-22s %-46s %s" % ("FICHIER", "NIV", "COMPOSANT", "MESSAGE", "NB"))
    for (fic, code, comp, msg), n in sorted(agg.items(), key=lambda kv: -kv[1]):
        print("%-8s %-4s %-22s %-46s %d" % (fic, code, comp[:22], msg[:46], n))
print("")
print("Total de messages : %d" % len(detail))
sujets = sorted(set(i for i, s, c, m in detail if "sujet" in s))
print("Exercices dont le SUJET emet un message (%d) : %s" % (len(sujets), ", ".join(sujets)))
