# -*- coding: utf-8 -*-
"""Reconstruit TOUTES les definitions, quel que soit le lot.

    python Documentation/Generateurs/GH/client_pont_rhino.py \\
           Documentation/Generateurs/GH/build_tout.py

Pourquoi ce fichier existe
--------------------------
Chaque lot avait son pilote — `build_lot_a.py`, `build_lot_ia.py`,
`build_lots_nouveaux.py`, plus un script jetable par vague et par lot recent.
Aucun ne couvrait l'ensemble, et il fallait se souvenir lequel lancer apres
avoir touche quel module. C'est la sixieme forme de la meme erreur dans ce
projet : une liste tenue a la main qui decroche de ce qu'elle couvre.

Ici, les modules de recettes sont DECOUVERTS : tout fichier `recipes_*.py`
pose a cote de celui-ci entre dans la production. Ajouter un lot demain ne
demandera aucune modification.

Les recettes du lot A passent par `recettes_skill.appliquer`, qui leur ajoute
les correctifs de la refonte pedagogique — c'est la seule difference de
traitement, et elle tient au fait que le lot A precede cette refonte.
"""
import importlib
import os
import sys

try:
    ICI = os.path.dirname(os.path.abspath(__file__))
except NameError:
    ICI = r"C:\Users\charl\.claude\projects\MAGPIE\Documentation\Generateurs\GH"
GEN = os.path.abspath(os.path.join(ICI, ".."))
for _p in (ICI, GEN):
    if _p not in sys.path:
        sys.path.insert(0, _p)

#: Les modules a recharger : eux aussi sont deduits, par prefixe, de ce que
#: le dossier contient reellement.
_PREFIXES = ("recipes_", "exercices_", "domaine_", "exos_", "skill_")
_NOMMES = ("gh_engine", "lots", "recettes_skill", "attendus_sujet",
           "notions_complement", "equilibrer_qcm", "build_lots_nouveaux")


def _recharger():
    """Vide le cache d'import : le pont execute plusieurs scripts de suite
    dans la MEME session Rhino, et un module deja importe garderait sa
    version precedente — c'est ainsi qu'une correction de recette peut
    sembler sans effet."""
    a_vider = set(_NOMMES)
    for dossier in (ICI, GEN):
        for f in os.listdir(dossier):
            if f.endswith(".py") and f.startswith(_PREFIXES):
                a_vider.add(f[:-3])
    for m in list(sys.modules):
        if m.split(".")[0] in a_vider:
            del sys.modules[m]


def recettes():
    """Toutes les recettes, celles du lot A passees par la refonte."""
    lot_a, autres = {}, {}
    for f in sorted(os.listdir(ICI)):
        if not (f.startswith("recipes_") and f.endswith(".py")):
            continue
        mod = importlib.import_module(f[:-3])
        cible = lot_a if f.startswith("recipes_a") else autres
        cible.update(getattr(mod, "R", {}))
    import recettes_skill
    recettes_skill.appliquer(lot_a)
    tout = dict(lot_a)
    tout.update(autres)
    return tout


def main():
    _recharger()
    import build_lots_nouveaux as B
    from lots import TOUS
    R = recettes()
    B.RECETTES = dict(R)
    B.LOT_A = [f for f in TOUS if f["id"] in R]
    print("Recettes decouvertes : %d" % len(R))
    print("A construire         : %d" % len(B.LOT_A))
    sans = sorted(f["id"] for f in TOUS if f["id"] not in R)
    if sans:
        print("Sans recette (note sur grille) : %d %s"
              % (len(sans), ", ".join(sans)))
    B.main()


main()
