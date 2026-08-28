# -*- coding: utf-8 -*-
"""Recette des deux regles structurantes du corrige.

1. Aucun cable ne relie la zone sujet a la zone corrige.
2. Le corrige ne produit rien tant que l'interrupteur est sur faux,
   et produit le resultat attendu des qu'il passe a vrai.
"""
import os
import clr
clr.AddReference("Grasshopper")
from Grasshopper.Kernel import GH_DocumentIO
from Grasshopper.Kernel.Special import GH_Group, GH_BooleanToggle

RACINE = r"C:\Users\charl\.claude\projects\MAGPIE\EXERCICES\LOT A - Composants natifs"


def ouvrir(p):
    io = GH_DocumentIO()
    return io.Document if io.Open(p) else None


def membres(doc, nom):
    for o in doc.Objects:
        if isinstance(o, GH_Group) and (o.NickName or "") == nom:
            return set(str(i) for i in o.ObjectIDs)
    return set()


def compte(param):
    try:
        return param.VolatileDataCount
    except Exception:
        return -1


def trouver(doc, nick):
    for o in doc.Objects:
        try:
            if (o.NickName or "") == nick:
                return o
        except Exception:
            pass
    return None


croisements, sans_toggle, fuite_off, muet_on, ok = [], [], [], [], 0
total = 0
for d in sorted(os.listdir(RACINE)):
    dd = os.path.join(RACINE, d)
    if not os.path.isdir(dd):
        continue
    ident = d.split(" ")[0]
    p = os.path.join(dd, "%s_complet.gh" % ident)
    if not os.path.isfile(p):
        continue
    total += 1
    doc = ouvrir(p)
    if doc is None:
        continue

    # --- 1. etancheite du cablage entre zones
    sujet = membres(doc, u"ZONE_SUJET")
    corr = membres(doc, u"ZONE_CORRIGE")
    n_croise = 0
    for o in doc.Objects:
        cible = str(o.InstanceGuid)
        zc = "S" if cible in sujet else ("C" if cible in corr else "?")
        entrees = []
        try:
            entrees = list(o.Params.Input)
        except Exception:
            try:
                entrees = [o] if o.SourceCount >= 0 else []
            except Exception:
                entrees = []
        for par in entrees:
            try:
                srcs = list(par.Sources)
            except Exception:
                continue
            for sp in srcs:
                sid = str(sp.InstanceGuid)
                # remonter au composant proprietaire si c'est un parametre
                prop = sp
                try:
                    if sp.Attributes is not None and sp.Attributes.GetTopLevel is not None:
                        prop = sp.Attributes.GetTopLevel.DocObject
                except Exception:
                    pass
                sid = str(prop.InstanceGuid)
                zs = "S" if sid in sujet else ("C" if sid in corr else "?")
                if zs in ("S", "C") and zc in ("S", "C") and zs != zc:
                    n_croise += 1
    if n_croise:
        croisements.append((ident, n_croise))

    # --- 2. comportement de l'interrupteur
    tg = trouver(doc, u"AFFICHER LE CORRIGÉ")
    rc = trouver(doc, u"REPONSE_CORRIGE")
    if tg is None or rc is None:
        sans_toggle.append(ident)
        continue
    doc.Enabled = True
    tg.Value = False
    tg.ExpireSolution(False)
    doc.NewSolution(True)
    n_off = compte(rc)
    tg.Value = True
    tg.ExpireSolution(False)
    doc.NewSolution(True)
    n_on = compte(rc)
    if n_off != 0:
        fuite_off.append((ident, n_off))
    if n_on <= 0:
        muet_on.append(ident)
    if n_off == 0 and n_on > 0 and n_croise == 0:
        ok += 1

print("RECETTE DES DEUX REGLES DU CORRIGE")
print("=" * 68)
print("Fichiers _complet controles         : %d" % total)
print("Conformes sur les deux regles       : %d" % ok)
print("")
print("1. Cables traversant les deux zones : %d fichier(s)" % len(croisements))
for i, n in croisements[:8]:
    print("     %s : %d cable(s)" % (i, n))
print("2. Sans interrupteur ou sans sortie : %d %s" % (len(sans_toggle), sans_toggle[:8]))
print("   Corrige produit malgre faux      : %d %s" % (len(fuite_off), fuite_off[:8]))
print("   Corrige muet malgre vrai         : %d %s" % (len(muet_on), muet_on[:8]))
print("=" * 68)
