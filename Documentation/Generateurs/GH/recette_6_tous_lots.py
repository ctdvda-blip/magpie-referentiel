# -*- coding: utf-8 -*-
"""Recette de structure, sur les ONZE lots.

Les recettes 1 a 5 ont ete ecrites pour le lot A et n'interrogent que son
dossier. Les dix lots ajoutes depuis n'avaient donc aucun controle structurel :
c'est ce que comble ce fichier. Il ne juge pas les VALEURS — la recette 2 s'en
charge la ou une valeur attendue est connue — mais les quatre proprietes qui
font qu'un exercice est distribuable :

  1. les deux fichiers s'ouvrent ;
  2. le sujet est ETANCHE : son parametre REPONSE n'est alimente par rien, et
     aucun objet du corrige n'y subsiste ;
  3. le corrige est MASQUE a l'ouverture : l'interrupteur est a faux, et le
     corrige ne se revele qu'apres l'avoir bascule ;
  4. une fois bascule, REPONSE_CORRIGE porte une valeur, et aucun composant ne
     leve d'erreur ni d'avertissement.

Les deux parametres flottants du sujet — celui qui attend la geometrie de
l'apprenant, et REPONSE lui-meme — signalent normalement qu'ils n'ont rien
collecte. Ces deux avertissements-la sont attendus et ne sont pas comptes.

S'execute dans Rhino, comme les autres :
    python client_pont_rhino.py recette_6_tous_lots.py
"""
import os
import sys
import clr

clr.AddReference("Grasshopper")
from Grasshopper.Kernel import GH_DocumentIO
from Grasshopper.Kernel import GH_RuntimeMessageLevel as LVL
from Grasshopper.Kernel.Special import GH_BooleanToggle

# Le pont rhinomcp execute le code sans lui donner de __file__ : on retombe
# alors sur le chemin connu du projet, comme le font les recettes 1 a 5.
try:
    _ICI = os.path.dirname(os.path.abspath(__file__))
except NameError:
    _ICI = r"C:\Users\charl\.claude\projects\MAGPIE\Documentation\Generateurs\GH"
_GEN = os.path.abspath(os.path.join(_ICI, ".."))
for _p in (_ICI, _GEN):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from lots import TOUS, DOSSIER

PROJET = os.path.abspath(os.path.join(_GEN, "..", ".."))

#: avertissements attendus, et pourquoi : le sujet a deux parametres qui ne
#: collectent rien tant que l'apprenant n'a pas travaille.
ATTENDUS = ("failed to collect data",)


def ouvrir(chemin):
    io = GH_DocumentIO()
    if not io.Open(chemin):
        return None
    return io.Document


def dossier_exercice(eid):
    """Le dossier peut etre nomme par le seul identifiant, ou le porter suivi
    du titre : les lots recents ont ete raccourcis pour la limite de chemin de
    Windows, le lot A ne l'a pas ete."""
    racine = os.path.join(PROJET, DOSSIER[eid].replace("/", os.sep))
    if not os.path.isdir(racine):
        return None
    for d in sorted(os.listdir(racine)):
        if d == eid or d.startswith(eid + " "):
            p = os.path.join(racine, d)
            if os.path.isdir(p):
                return p
    return None


def messages(doc):
    """Erreurs et avertissements, ceux qu'on attend mis a part."""
    out = []
    for o in doc.Objects:
        try:
            nom = o.NickName
        except Exception:
            nom = "?"
        for niv in (LVL.Error, LVL.Warning):
            try:
                lus = list(o.RuntimeMessages(niv))
            except Exception:
                continue
            for m in lus:
                if any(a in m for a in ATTENDUS):
                    continue
                out.append("%s : %s" % (nom, m))
    return out


def main():
    absents, casses, sans_gh = [], [], []
    fuites, masques, muets, bruyants = [], [], [], []
    controles = 0

    for e in TOUS:
        eid = e["id"]
        dd = dossier_exercice(eid)
        if dd is None:
            absents.append(eid)
            continue
        ps = os.path.join(dd, "%s_sujet.gh" % eid)
        pc = os.path.join(dd, "%s_complet.gh" % eid)
        if not (os.path.isfile(ps) and os.path.isfile(pc)):
            sans_gh.append(eid)
            continue
        controles += 1

        # --- 1 et 2 : le sujet s'ouvre, et il est etanche
        doc = ouvrir(ps)
        if doc is None:
            casses.append((eid, "sujet illisible"))
            continue
        noms, rep = [], None
        for o in doc.Objects:
            try:
                n = o.NickName or ""
            except Exception:
                continue
            noms.append(n)
            if n == "REPONSE":
                rep = o
        haut = " ".join(noms).upper()
        if "CORRIG" in haut or u"TAPE " in haut:
            fuites.append((eid, "le corrige subsiste dans le sujet"))
        if rep is None:
            fuites.append((eid, "pas de parametre REPONSE"))
        else:
            try:
                src = rep.SourceCount
            except Exception:
                src = -1
            if src != 0:
                fuites.append((eid, "REPONSE alimentee par %s source" % src))

        # --- 3 : le corrige est masque a l'ouverture
        doc = ouvrir(pc)
        if doc is None:
            casses.append((eid, "corrige illisible"))
            continue
        bascules = [o for o in doc.Objects if isinstance(o, GH_BooleanToggle)]
        if not bascules:
            masques.append((eid, "aucun interrupteur"))
        elif any(o.Value for o in bascules):
            masques.append((eid, "interrupteur deja a vrai"))

        # --- 4 : bascule, puis lecture
        doc.Enabled = True
        for o in bascules:
            o.Value = True
            o.ExpireSolution(False)
        doc.NewSolution(True)

        val = []
        for o in doc.Objects:
            try:
                if o.NickName != "REPONSE_CORRIGE":
                    continue
                for br in o.VolatileData.Branches:
                    for it in br:
                        val.append(it)
            except Exception:
                continue
        if not val:
            muets.append(eid)
        ennuis = messages(doc)
        if ennuis:
            bruyants.append((eid, ennuis[:3]))

    lg = 74
    print("=" * lg)
    print("RECETTE 6 - structure des definitions, tous lots")
    print("=" * lg)
    print("Exercices controles : %d sur %d" % (controles, len(TOUS)))
    print("Dossier introuvable : %d %s" % (len(absents), ", ".join(absents)))
    print("Sans .gh (livrable non graphique, note sur grille) : %d %s"
          % (len(sans_gh), ", ".join(sans_gh)))
    print("")

    def bloc(titre, liste, rendu=lambda x: x):
        print("%-46s %s" % (titre, "OK" if not liste else "%d cas" % len(liste)))
        for x in liste[:10]:
            print("      %s" % rendu(x))

    bloc("1. fichiers lisibles", casses, lambda t: "%s : %s" % t)
    bloc("2. sujets etanches", fuites, lambda t: "%s : %s" % t)
    bloc("3. corriges masques a l'ouverture", masques, lambda t: "%s : %s" % t)
    bloc("4. REPONSE_CORRIGE alimentee", muets)
    bloc("5. aucun avertissement inattendu", bruyants,
         lambda t: "%s : %s" % (t[0], " | ".join(t[1])))
    print("=" * lg)
    return 0


main()
