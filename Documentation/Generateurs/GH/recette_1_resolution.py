# -*- coding: utf-8 -*-
"""Recette des fichiers produits : ouverture, resolution, etat des composants."""
import os
import clr
clr.AddReference("Grasshopper")
import Grasshopper as GH
from Grasshopper.Kernel import GH_DocumentIO, GH_RuntimeMessageLevel as LVL

RACINE = r"C:\Users\charl\.claude\projects\MAGPIE\EXERCICES\LOT A - Composants natifs"

def ouvrir(path):
    io = GH_DocumentIO()
    if not io.Open(path):
        return None
    return io.Document

def controler(path):
    doc = ouvrir(path)
    if doc is None:
        return None, ["ouverture impossible"], 0, None
    doc.Enabled = True
    try:
        doc.NewSolution(True)
    except Exception as e:
        return doc, ["solution impossible : %s" % e], doc.ObjectCount, None
    err = []
    for o in doc.Objects:
        try:
            lvl = o.RuntimeMessageLevel
        except Exception:
            continue
        if lvl == LVL.Error:
            for m in o.RuntimeMessages(LVL.Error):
                err.append("%s : %s" % (o.Name, m))
    rep = None
    for o in doc.Objects:
        try:
            if o.NickName == "REPONSE":
                rep = o.VolatileDataCount
                break
        except Exception:
            pass
    return doc, err, doc.ObjectCount, rep

total = 0
sans_erreur = 0
sans_reponse = []
en_erreur = []
lignes = []
for d in sorted(os.listdir(RACINE)):
    dd = os.path.join(RACINE, d)
    if not os.path.isdir(dd):
        continue
    ident = d.split(" ")[0]
    p = os.path.join(dd, "%s_complet.gh" % ident)
    if not os.path.isfile(p):
        lignes.append("%s : FICHIER ABSENT" % ident)
        continue
    total += 1
    doc, err, n, rep = controler(p)
    etat = "OK " if not err else "ERR"
    if err:
        en_erreur.append((ident, err))
    else:
        sans_erreur += 1
    if rep in (None, 0):
        sans_reponse.append(ident)
    lignes.append("%s %s  objets=%-3s  REPONSE=%s%s"
                  % (etat, ident, n, rep,
                     ("  <-- " + err[0][:70]) if err else ""))

print("\n".join(lignes))
print("")
print("=" * 70)
print("Fichiers _complet controles : %d" % total)
print("Sans erreur de composant    : %d" % sans_erreur)
print("REPONSE vide ou absente     : %d %s" % (len(sans_reponse), sans_reponse))
print("=" * 70)
if en_erreur:
    print("")
    print("DETAIL DES ERREURS")
    for ident, err in en_erreur:
        print("  %s" % ident)
        for m in err[:4]:
            print("      %s" % m[:150])
