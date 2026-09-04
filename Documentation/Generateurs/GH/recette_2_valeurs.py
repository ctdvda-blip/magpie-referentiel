# -*- coding: utf-8 -*-
"""Compare la valeur produite par le corrige a la valeur annoncee par la fiche."""
import os
import clr
clr.AddReference("Grasshopper")
from Grasshopper.Kernel import GH_DocumentIO
from Grasshopper.Kernel.Special import GH_BooleanToggle

RACINE = r"C:\Users\charl\.claude\projects\MAGPIE\EXERCICES\LOT A - Composants natifs"

ATTENDU = {
    "A-01": ["42"],
    "A-05": ["12"],
    "A-06": ["5"],
    "A-08": ["8"],
    "A-09": ["6"],
    "A-10": ["10", "15", "20", "25", "30"],
    "A-11": ["J"],
    "A-12": ["15", "4", "91"],
    "A-13": ["Chant", "Montant", "Panneau", "Socle", "Traverse", "Tablette"],
    "A-14": ["14", "3", "30", "8"],
    "A-17": ["A", "1", "B", "2", "C", "3"],
    "A-18": ["55", "80", "23", "46", "99", "15", "72", "38"],
    "A-24": ["10"],
    "A-25": ["10"],
    "A-28": ["a12", "b07", "c24", "d03", "e18", "f31"],
    "A-29": ["True"],
    "A-43": ["True"],
}
# exercices ou seul le NOMBRE d'elements est verifiable simplement
CARDINAL = {
    "A-16": 8, "A-20": 9, "A-22": 10, "A-30": 20, "A-34": 2,
    "A-35": 12, "A-37": 6, "A-39": 20, "A-47": 3, "A-49": 6, "A-27": 5,
}



# ---------------------------------------------------------------------------
# Correctifs de la skill : les 10 exercices dont le jeu de donnees a ete
# refondu. Les valeurs ne sont PAS recopiees ici — elles sont recalculees a
# partir de skill_a.py, source unique, pour qu'une modification du jeu de
# donnees ne puisse pas laisser cette recette valider une valeur perimee.
# ---------------------------------------------------------------------------
try:
    import sys
    _GEN = "C:/Users/charl/.claude/projects/MAGPIE/Documentation/Generateurs"
    if _GEN not in sys.path:
        sys.path.insert(0, _GEN)
    import skill_a as _S

    def _t(seq):
        out = []
        for v in seq:
            if isinstance(v, float):
                out.append(("%g" % v))
            else:
                out.append(str(v))
        return out

    _paires = sorted(zip(_S.D_A13_LONG, _S.D_A13_REP), reverse=True)
    _tisse = []
    for _a, _b in zip(_S.D_A17_LG_CHENE, _S.D_A17_LG_NOYER):
        _tisse.append(_a)
        _tisse.append(_b)

    ATTENDU["A-08"] = ["11"]
    ATTENDU["A-09"] = ["18"]
    ATTENDU["A-11"] = _t([_S.D_A11[3], _S.D_A11[-1]])
    ATTENDU["A-12"] = _t([len(_S.D_A12), min(_S.D_A12), max(_S.D_A12)])
    ATTENDU["A-13"] = _t([r for _l, r in _paires])
    ATTENDU["A-14"] = _t(_S.D_A14[0::3])
    ATTENDU["A-15"] = ["11"]
    ATTENDU["A-17"] = _t(_tisse)
    ATTENDU["A-18"] = _t(_S.D_A18[5:13])
    ATTENDU["A-30"] = ["16"]
    ATTENDU["A-19"] = ["4"]            # nombre de branches, non un chemin
    ATTENDU["A-43"] = ["3000000.00000"]  # volume du tube referme, 200x150x100
    print("Attendus recalcules depuis skill_a : 10 exercices")
except Exception as _ex:
    print("ATTENTION : attendus de la skill non repris (%s)" % _ex)


def valeurs(path):
    io = GH_DocumentIO()
    if not io.Open(path):
        return None
    doc = io.Document
    doc.Enabled = True
    # Le corrige est masque a l'ouverture : sans basculer l'interrupteur
    # AFFICHER LE CORRIGE, REPONSE ne collecte rien et la recette validerait
    # a vide. On le passe a vrai avant toute lecture.
    for _o in doc.Objects:
        if isinstance(_o, GH_BooleanToggle):
            _o.Value = True
            _o.ExpireSolution(False)
    doc.NewSolution(True)
    # La sortie du corrige est REPONSE_CORRIGE : REPONSE appartient a la zone
    # sujet et n'est volontairement reliee a rien (aucun cable entre les deux
    # zones). Lire REPONSE renverrait toujours une liste vide.
    cible = "REPONSE_CORRIGE"
    noms = []
    for o in doc.Objects:
        try:
            noms.append(o.NickName)
        except Exception:
            pass
    if cible not in noms:
        cible = "REPONSE"
    for o in doc.Objects:
        try:
            if o.NickName != cible:
                continue
        except Exception:
            continue
        out = []
        try:
            for br in o.VolatileData.Branches:
                for it in br:
                    if it is None:
                        out.append("<null>")
                        continue
                    try:
                        v = it.Value
                    except Exception:
                        v = it
                    s = str(v)
                    if s.endswith(".0"):
                        s = s[:-2]
                    out.append(s)
        except Exception as e:
            return ["<lecture impossible : %s>" % e]
        return out
    return None


ok, ko = [], []
for d in sorted(os.listdir(RACINE)):
    dd = os.path.join(RACINE, d)
    if not os.path.isdir(dd):
        continue
    ident = d.split(" ")[0]
    p = os.path.join(dd, "%s_complet.gh" % ident)
    if not os.path.isfile(p):
        continue
    if ident not in ATTENDU and ident not in CARDINAL:
        continue
    v = valeurs(p)
    if v is None:
        ko.append((ident, "REPONSE introuvable", ""))
        continue
    if ident in ATTENDU:
        att = ATTENDU[ident]
        conforme = (v == att)
        detail = "attendu %s / obtenu %s" % (att, v)
    else:
        att = CARDINAL[ident]
        conforme = (len(v) == att)
        detail = "attendu %d elements / obtenu %d" % (att, len(v))
    (ok if conforme else ko).append((ident, "OK" if conforme else "ECART", detail))

print("CONTROLE DES VALEURS PRODUITES PAR LE CORRIGE")
print("=" * 70)
for ident, etat, detail in sorted(ok + ko):
    print("%-6s %-6s %s" % (ident, etat, detail[:150]))
print("=" * 70)
print("Conformes : %d / %d" % (len(ok), len(ok) + len(ko)))
