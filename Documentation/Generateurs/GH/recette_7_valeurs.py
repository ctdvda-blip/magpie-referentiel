# -*- coding: utf-8 -*-
"""Recette de non-regression sur les VALEURS, sur tous les lots.

La recette 6 verifie qu'un corrige produit quelque chose. Elle ne verifie pas
que ce quelque chose est toujours le meme. Or une recette de construction se
modifie : on change un cablage, une donnee, l'indice d'une sortie — et la
valeur attendue par le correcteur Magpie bouge sans que rien ne le signale.
C'est exactement ce qui s'est produit sur RH-09, dont le corrige a longtemps
rendu 1 au lieu de 0,57 parce que Deconstruct Box rend des intervalles.

Ce fichier fige donc les valeurs et les compare.

    python client_pont_rhino.py recette_7_valeurs.py           -> compare
    python client_pont_rhino.py recette_7_valeurs.py --figer   -> (re)fige

Le fichier de reference est `valeurs_attendues.json`, a cote de ce script. Il
n'est PAS produit a la main : on le fige apres avoir verifie les valeurs, et
toute divergence ulterieure est signalee. Refiger est un geste delibere — s'il
devient une habitude, la recette ne sert plus a rien.

Les valeurs sont comparees a 1e-6 pres en relatif : la reconstruction d'une
definition passe par des GUID neufs, mais le calcul, lui, doit tomber juste.
"""
import io
import json
import os
import sys
import clr

clr.AddReference("Grasshopper")
from Grasshopper.Kernel import GH_DocumentIO
from Grasshopper.Kernel.Special import GH_BooleanToggle

# Le pont rhinomcp execute le code sans lui donner de __file__.
try:
    ICI = os.path.dirname(os.path.abspath(__file__))
except NameError:
    ICI = r"C:\Users\charl\.claude\projects\MAGPIE\Documentation\Generateurs\GH"
GEN = os.path.abspath(os.path.join(ICI, ".."))
for _p in (ICI, GEN):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from lots import TOUS, DOSSIER

PROJET = os.path.abspath(os.path.join(GEN, "..", ".."))
REFERENCE = os.path.join(ICI, "valeurs_attendues.json")

#: tolerance relative. Un ecart au-dela n'est pas du bruit de calcul : c'est
#: la definition qui a change de reponse.
RELATIF = 1e-6


def dossier_exercice(eid):
    racine = os.path.join(PROJET, DOSSIER[eid].replace("/", os.sep))
    if not os.path.isdir(racine):
        return None
    for d in sorted(os.listdir(racine)):
        if d == eid or d.startswith(eid + " "):
            p = os.path.join(racine, d)
            if os.path.isdir(p):
                return p
    return None


def lire(chemin):
    """Valeurs de REPONSE_CORRIGE, corrige revele."""
    io_ = GH_DocumentIO()
    if not io_.Open(chemin):
        return None
    doc = io_.Document
    doc.Enabled = True
    for o in doc.Objects:
        if isinstance(o, GH_BooleanToggle):
            o.Value = True
            o.ExpireSolution(False)
    doc.NewSolution(True)
    for o in doc.Objects:
        try:
            if o.NickName != "REPONSE_CORRIGE":
                continue
        except Exception:
            continue
        out = []
        try:
            for br in o.VolatileData.Branches:
                for it in br:
                    if it is None:
                        out.append(None)
                        continue
                    try:
                        out.append(it.Value)
                    except Exception:
                        out.append(str(it))
        except Exception:
            return None
        return out
    return None


def _txt(v):
    """Rend une valeur comparable d'une execution a l'autre.

    Le piege est la geometrie : `str()` d'une courbe RhinoCommon contient son
    ADRESSE MEMOIRE, qui change a chaque ouverture du document. Comparee telle
    quelle, toute definition qui rend de la geometrie serait signalee en ecart
    a chaque passage — quatorze faux positifs au premier essai. On la remplace
    donc par ce qui la caracterise vraiment : son type, et sa mesure.
    """
    if v is None:
        return u"<null>"
    if isinstance(v, float):
        return repr(v)
    if isinstance(v, (bool, int, str)):
        return u"%s" % v
    nom = type(v).__name__
    for mesure, gabarit in ((u"GetLength", u"L=%.6f"),
                            (u"GetArea", u"A=%.6f"),
                            (u"GetVolume", u"V=%.6f")):
        fn = getattr(v, mesure, None)
        if fn is None:
            continue
        try:
            return u"%s %s" % (nom, gabarit % fn())
        except Exception:
            continue
    for attribut in (u"X", u"Length"):                 # points, vecteurs
        if hasattr(v, attribut):
            try:
                if attribut == u"X":
                    return u"%s (%.6f, %.6f, %.6f)" % (nom, v.X, v.Y, v.Z)
                return u"%s L=%.6f" % (nom, v.Length)
            except Exception:
                pass
    return nom


def proches(a, b):
    """Deux relevés disent-ils la meme chose ?"""
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        try:
            fx, fy = float(x), float(y)
        except (TypeError, ValueError):
            if _txt(x) != _txt(y):
                return False
            continue
        ecart = abs(fx - fy)
        if ecart > RELATIF * max(1.0, abs(fx), abs(fy)):
            return False
    return True


def relever():
    releve, muets = {}, []
    for e in TOUS:
        eid = e["id"]
        dd = dossier_exercice(eid)
        if dd is None:
            continue
        p = os.path.join(dd, "%s_complet.gh" % eid)
        if not os.path.isfile(p):
            continue
        v = lire(p)
        if not v:
            muets.append(eid)
            continue
        releve[eid] = [_txt(x) for x in v]
    return releve, muets


def main():
    figer = "--figer" in sys.argv
    releve, muets = relever()
    lg = 74
    print("=" * lg)
    print("RECETTE 7 - valeurs des corriges, tous lots")
    print("=" * lg)
    print("Definitions relevees : %d" % len(releve))
    if muets:
        print("Sans valeur lisible  : %d %s" % (len(muets), ", ".join(muets)))

    if figer or not os.path.isfile(REFERENCE):
        fh = io.open(REFERENCE, "w", encoding="utf-8")
        try:
            fh.write(json.dumps(releve, indent=1, ensure_ascii=False,
                                sort_keys=True))
        finally:
            fh.close()
        print("")
        print("Valeurs figees dans %s" % os.path.basename(REFERENCE))
        print("Relire ce fichier : c'est desormais la reference.")
        return 0

    attendu = json.loads(io.open(REFERENCE, encoding="utf-8").read())
    ecarts, neufs, disparus = [], [], []
    for eid, v in sorted(releve.items()):
        if eid not in attendu:
            neufs.append(eid)
        elif not proches(v, attendu[eid]):
            ecarts.append((eid, attendu[eid], v))
    for eid in sorted(attendu):
        if eid not in releve:
            disparus.append(eid)

    print("")
    print("%-46s %s" % ("valeurs conformes a la reference",
                        "OK" if not ecarts else "%d ECART(S)" % len(ecarts)))
    for eid, a, b in ecarts[:12]:
        print("      %-7s attendu %s" % (eid, ", ".join(a)[:40]))
        print("      %-7s obtenu  %s" % ("", ", ".join(b)[:40]))
    if neufs:
        print("Definitions nouvelles, a figer : %s" % ", ".join(neufs))
    if disparus:
        print("Definitions disparues          : %s" % ", ".join(disparus))
    print("=" * lg)
    return 0 if not ecarts else 1


# Comme gen_images.py : le fichier se lance de lui-meme quand on l'execute,
# mais une relance ciblee l'IMPORTE pour reutiliser `lire()` et
# `dossier_exercice()`. Sans cette garde, l'import relancerait le releve
# complet des 108 definitions.
if __name__ != "recette_7_valeurs":
    main()
